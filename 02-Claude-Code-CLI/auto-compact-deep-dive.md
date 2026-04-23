---
title: "Auto-Compact Deep Dive — Window vs Percentage Override"
category: "02-Claude-Code-CLI"
tags: ["claude-code", "testing"]
---

# Auto-Compact Deep Dive — Window vs Percentage Override

**Topic**: `CLAUDE_CODE_AUTO_COMPACT_WINDOW` vs `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`
**Binary**: Claude Code 2.1.75
**Status**: Both active, fully implemented

---

## TL;DR

- **`CLAUDE_CODE_AUTO_COMPACT_WINDOW`** = "Pretend the context window is this size" (caps max window)
- **`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`** = "Trigger compaction at X% of (possibly capped) window"
- They **compose**: window override runs first, percentage applies to the result
- **Order matters**: Window cap → percentage calculation → 13K safety headroom
- For **Opus 1M**, use both: `WINDOW=350000` + `PCT=85` to maintain 200K-like behavior

---

## The Calculation Pipeline

### Step 1: `BB(model)` — Calculate Effective Window

```javascript
function BB(H) {  // H = model
  let buffer = Math.min(PnH(H), 20000),        // Reserved buffer (~20K)
      baseWindow = LY(H, Qw()),                 // Model's native context window
      override = process.env.CLAUDE_CODE_AUTO_COMPACT_WINDOW;

  if (override) {
    let parsed = parseInt(override, 10);
    if (!isNaN(parsed) && parsed > 0)
      baseWindow = Math.min(baseWindow, parsed);  // ← CAP DOWN (never extends)
  }

  return baseWindow - buffer;  // Effective window
}
```

**Key**: `Math.min(native, override)` — only applies if override is LOWER than native.

---

### Step 2: `bQH(model)` — Calculate Auto-Compact Threshold

```javascript
function bQH(H) {  // H = model
  let effectiveWindow = BB(H),                  // From step 1
      safeThreshold = effectiveWindow - 13000,  // Leave 13K headroom
      pctOverride = process.env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE;

  if (pctOverride) {
    let pct = parseFloat(pctOverride);
    if (!isNaN(pct) && pct > 0 && pct <= 100) {
      let pctThreshold = Math.floor(effectiveWindow * (pct / 100));
      return Math.min(pctThreshold, safeThreshold);  // ← Never exceed safe headroom
    }
  }

  return safeThreshold;  // Default: effectiveWindow - 13K
}
```

**Key**: Percentage is calculated on the **capped window** (if window override is active).

---

### Step 3: `PKH(tokens, model)` — Check Thresholds

```javascript
function PKH(H, $) {  // H = current tokens, $ = model
  let autoCompactThreshold = bQH($),             // From step 2
      effectiveWindow = BB($),                   // From step 1
      percentLeft = Math.max(0, Math.round((effectiveWindow - H) / effectiveWindow * 100)),

      warningThreshold = effectiveWindow - 20000,
      errorThreshold = effectiveWindow - 20000,
      isAboveAutoCompactThreshold = oy() && H >= autoCompactThreshold,

      blockingLimit = effectiveWindow - 3000,
      blockingOverride = process.env.CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE,
      actualBlockingLimit = blockingOverride
                            ? parseInt(blockingOverride, 10)
                            : blockingLimit,
      isAtBlockingLimit = H >= actualBlockingLimit;

  return {
    percentLeft,
    isAboveWarningThreshold,
    isAboveErrorThreshold,
    isAboveAutoCompactThreshold,  // ← Triggers auto-compact
    isAtBlockingLimit
  };
}
```

---

## Default Behavior (No Overrides)

### Sonnet 4.6 (200K context)

```
Model native window:    200,000 tokens
Buffer:                 -20,000 tokens
─────────────────────────────────────
Effective window:       180,000 tokens
Safe headroom:          -13,000 tokens
─────────────────────────────────────
Threshold:              167,000 tokens  (~93%)
```

**Auto-compact triggers at 167K tokens** (~93% of effective window).

---

### Opus 1M (1M context)

```
Model native window:  1,000,000 tokens
Buffer:                 -20,000 tokens
─────────────────────────────────────
Effective window:       980,000 tokens
Safe headroom:          -13,000 tokens
─────────────────────────────────────
Threshold:              967,000 tokens  (~99%)
```

**Auto-compact triggers at 967K tokens** (~99% of effective window).

⚠️ **Problem**: Compacting at 99% means:
- Massive conversation history to summarize
- Slow compaction (takes minutes)
- Risk of memory exhaustion
- Poor compaction quality (too much context)

---

## Percentage Override Only

### Example: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85`

#### Sonnet 4.6 (200K)

```
Effective window:       180,000 tokens
Percentage threshold:   floor(180,000 × 0.85) = 153,000
Safe headroom:          180,000 - 13,000      = 167,000
─────────────────────────────────────
Actual threshold:       min(153,000, 167,000) = 153,000 tokens  (~85%)
```

**Auto-compact at 153K** (~85% of effective window). ✅ Good.

---

#### Opus 1M (1M)

```
Effective window:       980,000 tokens
Percentage threshold:   floor(980,000 × 0.85) = 833,000
Safe headroom:          980,000 - 13,000      = 967,000
─────────────────────────────────────
Actual threshold:       min(833,000, 967,000) = 833,000 tokens  (~85%)
```

**Auto-compact at 833K** (~85% of effective window).

⚠️ **Still problematic**: 833K is **4.8x larger** than the 200K experience. Compaction will be slow and may fail.

---

## Window Override Only

### Example: `CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000`

#### Sonnet 4.6 (200K)

```
Model native window:    200,000 tokens
Override:               350,000 tokens
Capped window:          min(200,000, 350,000) = 200,000  ← NO EFFECT
─────────────────────────────────────
(Same as default — 167K threshold)
```

**No change.** Window override is higher than native, so `Math.min()` picks native.

---

#### Opus 1M (1M)

```
Model native window:  1,000,000 tokens
Override:               350,000 tokens
Capped window:          min(1,000,000, 350,000) = 350,000  ← CAPPED
Buffer:                                           -20,000
─────────────────────────────────────
Effective window:                                 330,000 tokens
Safe headroom:                                    -13,000 tokens
─────────────────────────────────────
Threshold:                                        317,000 tokens  (~96% of capped)
```

**Auto-compact at 317K** (~96% of the capped window).

✅ **Better**, but still using fixed 13K headroom on a 330K window → 96% is late.

---

## Both Overrides (Recommended)

### Example: `CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000` + `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85`

#### Sonnet 4.6 (200K)

```
Capped window:          min(200,000, 350,000) = 200,000  ← NO EFFECT
Effective window:       180,000
Threshold:              floor(180,000 × 0.85) = 153,000 tokens  (~85%)
```

Same as percentage-only case. Window override ignored.

---

#### Opus 1M (1M)

```
Model native window:  1,000,000 tokens
Override:               350,000 tokens
Capped window:          min(1,000,000, 350,000) = 350,000  ← CAPPED
Buffer:                                           -20,000
─────────────────────────────────────
Effective window:                                 330,000 tokens
Percentage threshold:   floor(330,000 × 0.85)   = 280,500
Safe headroom:          330,000 - 13,000        = 317,000
─────────────────────────────────────
Actual threshold:       min(280,500, 317,000)   = 280,500 tokens  (~85% of capped)
```

**Auto-compact at 280.5K** (~85% of the capped 350K window).

✅ **Excellent**: Similar to the 200K experience (153K @ 85%) but with room for larger individual inputs.

---

## Comparison Table

| Model | Window Override | PCT Override | Threshold | vs 200K Default |
|-------|----------------|--------------|-----------|-----------------|
| **Sonnet 4.6** (200K) | — | — | **167K** | Baseline (93%) |
| **Sonnet 4.6** (200K) | — | 85 | **153K** | -14K (-8%) |
| **Sonnet 4.6** (200K) | 350K | 85 | **153K** | No change (override ignored) |
| **Opus 1M** (1M) | — | — | **967K** | +800K (+579%) 🔴 |
| **Opus 1M** (1M) | — | 85 | **833K** | +666K (+480%) 🔴 |
| **Opus 1M** (1M) | 500K | — | **467K** | +300K (+280%) ⚠️ |
| **Opus 1M** (1M) | 500K | 85 | **408K** | +241K (+244%) ⚠️ |
| **Opus 1M** (1M) | **350K** | **85** | **280K** | **+113K (+168%)** ✅ |
| **Opus 1M** (1M) | **300K** | **85** | **238K** | **+71K (+142%)** ✅ |

---

## Why `Math.min()` Matters

### Common Mistake

"I'll set `CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000` to use the full 1M context!"

**Result**: No effect. `Math.min(1000000, 1000000) = 1000000` — same as native.

### Correct Use

The override is a **ceiling**, not a floor:
- Set it **lower** than native to cap the window
- Set it **higher** than native → ignored (no effect)

---

## Recommended Settings

### For 200K Models (Sonnet 4.6, Opus 4.6, Haiku 4.5)

```bash
# Percentage override only
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85

# Window override has no effect (200K < any reasonable override)
```

**Threshold**: 153K tokens (~85% of 180K effective window)

---

### For 1M Models (Sonnet 1M, Opus 1M)

```bash
# Recommended: Cap window + percentage
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Threshold**: 280.5K tokens (~85% of capped 350K window)

**Rationale**:
- Maintains similar compaction frequency as 200K models
- Allows larger individual inputs (files, tool results)
- Prevents runaway context accumulation
- Faster compaction (less history to summarize)

---

### Alternative: More Aggressive

```bash
# Tighter control
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=300000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Threshold**: 238K tokens (~85% of capped 300K window)

**Rationale**: Even closer to the 200K experience (153K → 238K is only +55%).

---

## Edge Cases

### What if I set window to 150K (below native 200K)?

```
Sonnet 4.6:
  Capped window:    min(200,000, 150,000) = 150,000  ← CAPPED
  Effective:        150,000 - 20,000     = 130,000
  Threshold (85%):  floor(130,000 × 0.85) = 110,500
```

**Result**: Auto-compact at 110.5K — more aggressive than default. Valid use case for CI/CD or short sessions.

---

### What if I set percentage to 99?

```
Opus 1M with WINDOW=350K:
  Effective:        330,000
  Threshold (99%):  floor(330,000 × 0.99) = 326,700
  Safe headroom:    330,000 - 13,000      = 317,000
  Actual:           min(326,700, 317,000) = 317,000  ← Headroom wins
```

**Result**: Safety headroom (13K) overrides the percentage. Max threshold is always `effectiveWindow - 13K`.

---

### What if I disable auto-compact entirely?

```bash
export DISABLE_AUTO_COMPACT=1
```

**Result**: Overrides are ignored. Manual compaction only (`/compact`). Risky — you can OOM.

---

## Debugging

### Check Current Settings

```bash
# Env vars
env | grep -i "COMPACT\|AUTOCOMPACT"

# Computed values (from logs)
# Run a session and look for:
v(`autocompact: tokens=${currentTokens} threshold=${threshold} effectiveWindow=${effectiveWindow}`)
```

### Example Log Output

```
autocompact: tokens=165000 threshold=153000 effectiveWindow=180000
```

Decode:
- `tokens=165000` — current conversation size
- `threshold=153000` — will compact at this level
- `effectiveWindow=180000` — 200K - 20K buffer

---

## Implementation Details

### Constants

```javascript
var lh6 = 20000,   // Buffer size
    KUA = 13000,   // Safe headroom
    nh6 = 20000,   // Warning threshold offset
    ih6 = 20000,   // Error threshold offset
    qUA = 3000;    // Blocking limit headroom
```

### Related Functions

- `BB(model)` — Effective window calculation
- `bQH(model)` — Auto-compact threshold
- `PKH(tokens, model)` — Threshold checks
- `rh6(messages, model, source, freed)` — Auto-compact decision
- `Inf(...)` — Auto-compact execution

---

## Testing

### Verify Window Override

```bash
# Set a low override
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=100000

# Start a session with a 200K model
# Expect auto-compact to trigger around 68K tokens
# (100K - 20K buffer = 80K effective, 80K - 13K = 67K threshold)
```

### Verify Percentage Override

```bash
# Set a high percentage
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=95

# Start a session with a 200K model
# Expect auto-compact to trigger around 167K tokens
# (95% of 180K effective = 171K, capped by 13K headroom → 167K)
```

---

## Related

- [analysis.md](./analysis.md) — Main 2.1.75 analysis
- [opus-1m-migration.md](./opus-1m-migration.md) — Opus 1M migration details
- [env-vars.md](./env-vars.md) — Environment variable reference
