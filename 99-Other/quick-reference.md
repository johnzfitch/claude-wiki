---
title: "Quick Reference — 2.1.75"
category: "99-Other"
tags: ["testing"]
---

# Quick Reference — 2.1.75

Fast lookup for common tasks and settings.

---

## Check Your Model

```bash
# In a session
/config

# Or check settings
cat ~/.claude/settings.json | jq '.model'
```

---

## Recommended Settings by Model

### Sonnet 4.6 / Opus 4.6 (200K)

```bash
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Auto-compact at**: ~153K tokens

---

### Sonnet 1M / Opus 1M (1M)

```bash
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Auto-compact at**: ~280K tokens

---

## Opt Out of Opus 1M Migration

```bash
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1
```

Or change settings from `"opus"` to `"claude-opus-4-6"`.

---

## Check If You've Been Migrated

```bash
cat ~/.claude/settings.json | jq '.model'
```

**Before**: `"opus"` or `"claude-opus-4-6"`
**After**: `"opus[1m]"` or `"claude-opus-4-6[1m]"`

---

## Default Auto-Compact Thresholds

| Model | Context | Default Threshold | % |
|-------|---------|-------------------|---|
| Sonnet 4.6 | 200K | 167K | 93% |
| Opus 4.6 | 200K | 167K | 93% |
| Sonnet 1M | 1M | 967K | 99% ⚠️ |
| Opus 1M | 1M | 967K | 99% ⚠️ |

⚠️ **99% is too late** — use overrides!

---

## With Recommended Overrides

| Model | Window Cap | PCT | Threshold | % |
|-------|-----------|-----|-----------|---|
| Sonnet 4.6 | — | 85 | 153K | 85% |
| Opus 4.6 | — | 85 | 153K | 85% |
| Sonnet 1M | 350K | 85 | 280K | 85% |
| Opus 1M | 350K | 85 | 280K | 85% |

---

## Debugging Auto-Compact

### Check Current Env Vars

```bash
env | grep -i "COMPACT\|AUTOCOMPACT"
```

---

### Check Runtime Threshold

Start a session and look for log line:

```
autocompact: tokens=165000 threshold=153000 effectiveWindow=180000
```

Decode:
- `tokens` = current conversation size
- `threshold` = will compact at this level
- `effectiveWindow` = model window - buffer

---

## New Env Vars in 2.1.75

### `CLAUDE_CODE_AUTO_COMPACT_WINDOW`

**Type**: Integer (tokens)
**Purpose**: Caps context window for auto-compact
**Effect**: Only caps DOWN (no effect if set above native window)

```bash
# Cap 1M models to 350K
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
```

---

### `CLAUDE_PLUGIN_OPTION_*`

**Type**: String prefix
**Purpose**: Plugin configuration (not yet implemented)
**Status**: Infrastructure only

```bash
# Future syntax (not working yet):
export CLAUDE_PLUGIN_OPTION_MYPLUGIN_API_KEY="sk-..."
```

---

## New Feature Flags in 2.1.75

| Flag | Purpose | Status |
|------|---------|--------|
| `tengu_cobalt_compass` | Opus 1M migration gate | Gradual rollout |
| `tengu_amber_wren` | File read limits config | Active |
| `tengu_pewter_gull` | Byte truncation enforcement | Active |

All controlled server-side — not user-configurable.

---

## Common Tasks

### Force Compaction Now

```
/compact
```

---

### Check Context Usage

```
/config
```

Look for "Context usage" section.

---

### Switch Models Mid-Session

```
/model opus[1m]
```

---

### Check Auto-Compact Settings

```bash
# Read settings
cat ~/.claude/settings.json | jq '.env'

# Should show:
# {
#   "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "350000",
#   "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "85"
# }
```

---

## Calculation Examples

### Window Override Math

```
Model: Opus 1M (1M native)
Override: 350K

Capped window = Math.min(1,000,000, 350,000) = 350,000
Effective = 350,000 - 20,000 buffer = 330,000
```

---

### Percentage Math

```
Effective window: 330,000
Percentage: 85%

Threshold = floor(330,000 × 0.85) = 280,500
Safety cap = 330,000 - 13,000 = 317,000

Actual = min(280,500, 317,000) = 280,500 tokens
```

---

## Migration Timeline (Estimated)

| Phase | Status | Date |
|-------|--------|------|
| Infrastructure shipped | ✅ Done | 2.1.75 (2026-03-13) |
| Gradual rollout begins | 🔄 In progress | TBD |
| Full rollout | ⏳ Pending | TBD |
| Default alias changes | ⏳ Pending | TBD |

---

## Files to Edit

### Settings

```bash
vim ~/.claude/settings.json
```

Add to `env` object:
```json
{
  "env": {
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "350000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "85"
  }
}
```

---

### Shell RC

```bash
vim ~/.zshrc  # or ~/.bashrc
```

Add:
```bash
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

Then:
```bash
source ~/.zshrc
```

---

## Testing

### Verify Window Override Works

```bash
# Set unrealistically low
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=100000

# Start session with 200K model
# Should auto-compact around 67K tokens
# (100K - 20K - 13K = 67K)
```

---

### Verify Percentage Override Works

```bash
# Set high percentage
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=95

# Start session
# Should auto-compact around 167K (capped by 13K headroom)
# (95% of 180K = 171K, but max is 180K - 13K = 167K)
```

---

## Documentation Links

- [README.md](./README.md) — Start here
- [analysis.md](./analysis.md) — Full analysis
- [auto-compact-deep-dive.md](./auto-compact-deep-dive.md) — Deep dive on window/percentage
- [opus-1m-migration.md](./opus-1m-migration.md) — Migration details
- [env-vars.md](./env-vars.md) — All env vars
- [feature-flags.md](./feature-flags.md) — All feature flags

---

## Help

```
/help
```

Or visit: https://code.claude.com/docs
