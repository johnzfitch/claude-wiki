# Environment Variables — 2.1.75 Reference

Complete reference for new and updated environment variables in Claude Code 2.1.75.

---

## New in 2.1.75

### `CLAUDE_CODE_AUTO_COMPACT_WINDOW`

**Type**: Integer (tokens)
**Default**: Undefined (uses model's native context window)
**Since**: 2.1.75
**Status**: Active

**Purpose**: Caps the effective context window used for auto-compact threshold calculations.

**Behavior**:
```javascript
if (override) {
  baseWindow = Math.min(nativeWindow, parseInt(override));  // CAP DOWN only
}
```

**Key Property**: Uses `Math.min()` — only caps DOWN, never extends UP.

**Examples**:

```bash
# No effect on 200K models (200K < 500K)
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=500000

# Caps 1M models to 350K effective window
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000

# Aggressive compaction even on 200K models
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=150000
```

**Use Cases**:
- Force more aggressive compaction on 1M models
- Simulate smaller context windows for testing
- Prevent excessive context accumulation

**Related**:
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` — Applies percentage to the capped window
- See: [auto-compact-deep-dive.md](./auto-compact-deep-dive.md)

---

### `CLAUDE_PLUGIN_OPTION_<PLUGIN>_<KEY>`

**Type**: String
**Default**: Undefined
**Since**: 2.1.75
**Status**: Infrastructure only (not yet implemented)

**Purpose**: Future plugin configuration system. Allows plugins to expose settings via environment variables.

**Expected Format**:
```bash
export CLAUDE_PLUGIN_OPTION_MYPLUGIN_API_KEY="sk-..."
export CLAUDE_PLUGIN_OPTION_LINTER_STRICT_MODE="true"
```

**Current State**: Prefix exists in code but no consumers. Likely activated in future release.

**Related**:
- `tengu_orchid_trellis` — MCP marketplace gate (may use this system)

---

## Updated Defaults

### `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`

**Type**: Float (percentage, 0-100)
**Default**: Undefined (uses fixed 13K headroom)
**Since**: Pre-2.1.59
**Updated**: Interaction with window override clarified in 2.1.75

**Purpose**: Sets the auto-compact threshold as a percentage of the effective window.

**Behavior**:
```javascript
if (override) {
  threshold = Math.floor(effectiveWindow * (override / 100));
  threshold = Math.min(threshold, effectiveWindow - 13000);  // Safety cap
}
```

**Default Calculation** (when NOT set):
```javascript
threshold = effectiveWindow - 13000;  // Fixed headroom
```

**Effective Defaults**:

| Model | Effective Window | Default Threshold | Effective % |
|-------|------------------|-------------------|-------------|
| Sonnet 4.6 (200K) | 180K | 167K | **~93%** |
| Opus 4.6 (200K) | 180K | 167K | **~93%** |
| Sonnet 1M | 980K | 967K | **~99%** ⚠️ |
| Opus 1M | 980K | 967K | **~99%** ⚠️ |

**Recommendation**: Set to `85` for all models.

```bash
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Interaction with `CLAUDE_CODE_AUTO_COMPACT_WINDOW`**:
1. Window cap applied FIRST
2. Percentage calculated SECOND (on capped window)
3. 13K safety headroom enforced as ceiling

**Related**:
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW` — Caps the base window
- See: [auto-compact-deep-dive.md](./auto-compact-deep-dive.md)

---

## Existing Variables (Relevant to 2.1.75)

### `CLAUDE_CODE_DISABLE_1M_CONTEXT`

**Type**: Boolean (`1` | `0` | `true` | `false`)
**Default**: `0` (enabled)
**Since**: Pre-2.1.59
**Updated**: Now blocks `tengu_cobalt_compass` migration

**Purpose**: Disables all 1M context features.

**Effects in 2.1.75**:
- ✅ Blocks auto-migration from `opus` → `opus[1m]`
- ✅ Prevents manual selection of `[1m]` model variants
- ✅ Forces models to use 200K max context

**Example**:
```bash
# Opt out of 1M context entirely
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1
```

**Related**:
- `tengu_cobalt_compass` — Opus 1M migration gate
- See: [opus-1m-migration.md](./opus-1m-migration.md)

---

### `DISABLE_AUTO_COMPACT`

**Type**: Boolean
**Default**: Undefined (auto-compact enabled)
**Since**: Pre-2.1.59
**Status**: Active

**Purpose**: Disables automatic compaction entirely. Requires manual `/compact`.

**Example**:
```bash
# Disable auto-compact (manual only)
export DISABLE_AUTO_COMPACT=1
```

**Warning**: Without auto-compact, you can hit the blocking limit (context full) and be unable to continue. Use with caution.

**Related**:
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW` — Ignored when auto-compact is disabled
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` — Ignored when auto-compact is disabled

---

### `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE`

**Type**: Integer (tokens)
**Default**: Undefined (uses `effectiveWindow - 3000`)
**Since**: Pre-2.1.59
**Status**: Active

**Purpose**: Overrides the hard blocking limit (point at which you cannot continue).

**Default Calculation**:
```javascript
blockingLimit = effectiveWindow - 3000;
```

**Example**:
```bash
# Custom blocking limit
export CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE=195000
```

**Warning**: Setting this too high can cause OOM (out of memory) errors.

---

## Recommended Settings by Model

### 200K Models (Sonnet 4.6, Opus 4.6, Haiku 4.5)

```bash
# Percentage override only
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85

# No need for window override (no effect on 200K models)
```

**Result**: Auto-compact at ~153K tokens (~85% of effective 180K window).

---

### 1M Models (Sonnet 1M, Opus 1M)

```bash
# Cap window + percentage (recommended)
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Result**: Auto-compact at ~280K tokens (~85% of capped 350K window).

**Alternative** (more aggressive):
```bash
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=300000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Result**: Auto-compact at ~238K tokens (~85% of capped 300K window).

---

### Opt Out of 1M Migration

```bash
# Block auto-migration from opus → opus[1m]
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1
```

---

## Testing Environment Variables

### Check Active Values

```bash
# Show all compact-related env vars
env | grep -i "COMPACT\|AUTOCOMPACT"
```

---

### Verify Runtime Behavior

Start a session and look for debug logs:

```
v(`autocompact: tokens=${tokens} threshold=${threshold} effectiveWindow=${effectiveWindow}`)
```

**Example**:
```
autocompact: tokens=165000 threshold=153000 effectiveWindow=180000
```

Decode:
- `tokens=165000` — current conversation size
- `threshold=153000` — auto-compact will trigger at this level
- `effectiveWindow=180000` — 200K - 20K buffer

---

## Environment Variable Precedence

### Auto-Compact Threshold

1. `DISABLE_AUTO_COMPACT=1` — Disables entirely (overrides all)
2. `CLAUDE_CODE_AUTO_COMPACT_WINDOW` — Caps base window
3. `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` — Percentage of (possibly capped) window
4. Default: `effectiveWindow - 13000` (fixed headroom)

### Model Selection

1. Session override (`/model`)
2. `ANTHROPIC_MODEL` env var
3. `~/.claude/settings.json` → `model` field
4. Default: `sonnet` (Sonnet 4.6)

---

## Debugging

### Check Settings File

```bash
cat ~/.claude/settings.json | jq
```

**Look for**:
- `model` — Current model selection
- `env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` — Percentage override
- `env.CLAUDE_CODE_AUTO_COMPACT_WINDOW` — Window override

---

### Check Runtime Config

```bash
# During a session
/config

# Shows:
# - Active model
# - Auto-compact settings
# - Context window info
```

---

## Related Documentation

- [analysis.md](./analysis.md) — Main 2.1.75 analysis
- [auto-compact-deep-dive.md](./auto-compact-deep-dive.md) — Window vs percentage mechanics
- [opus-1m-migration.md](./opus-1m-migration.md) — Opus 1M migration details
- [feature-flags.md](./feature-flags.md) — Feature flag reference
