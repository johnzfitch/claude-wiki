# Opus 1M Context Migration — Implementation Details

**Feature Flag**: `tengu_cobalt_compass`
**Binary**: Claude Code 2.1.75
**Status**: Gradual rollout (feature-flagged)
**Impact**: Auto-migrates `model: "opus"` → `model: "opus[1m]"` when enabled

---

## Overview

2.1.75 introduces a **migration pathway** to automatically upgrade Opus users to the 1M context variant. This is gated by the `tengu_cobalt_compass` feature flag and only applies to first-party (non-enterprise) users.

---

## Gate Function

**File**: `cli.js:6819`

```javascript
function Yw() {
  if (ts() || MR() || BL() !== "firstParty") return false;
  return IA("tengu_cobalt_compass", false)
}
```

**Conditions**:
- ✅ **First-party users only** (`BL() === "firstParty"`)
- ❌ Disabled if `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` (via `ts()`)
- ❌ Disabled for enterprise users (via `MR()`)
- ⚙️ Controlled by `tengu_cobalt_compass` feature flag

---

## Migration Logic

**File**: `cli.js:6988` (function `EI8()`)

```javascript
function EI8() {
  // Only run if gate is open
  if (!Yw()) return;

  // Only migrate users with model: "opus"
  if (RA("userSettings")?.model !== "opus") return;

  // Target model: opus[1m]
  let newModel = "opus[1m]",
      actualModel = W1(newModel) === W1(wV()) ? undefined : newModel;

  // Write to settings.json
  EL("userSettings", { model: actualModel });

  // Log telemetry event
  Q("tengu_opus_to_opus1m_migration", {});
}
```

**Behavior**:
1. Reads `~/.claude/settings.json`
2. Checks if `model` field is `"opus"`
3. Migrates to `"opus[1m]"` (1M context variant)
4. Writes updated settings
5. Logs `tengu_opus_to_opus1m_migration` telemetry event

---

## When Does It Run?

**Trigger**: Startup migrations (function `TI8()`)

The migration runs during **CLI initialization** along with other one-time migrations:
- Auto-updates settings migration
- Permission mode migrations
- MCP approval field migrations
- **Opus 1M migration** ← NEW in 2.1.75

---

## Model Variants

### Before Migration

```json
{
  "model": "opus"
}
```

**Resolves to**: `claude-opus-4-6` (200K context)

---

### After Migration

```json
{
  "model": "opus[1m]"
}
```

**Resolves to**: `claude-opus-4-6[1m]` (1M context)

---

## Opt-Out

### Method 1: Environment Variable

```bash
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1
```

**Effect**: Disables ALL 1M context features:
- Blocks auto-migration
- Prevents manual selection of `[1m]` models
- Related function: `ts()` checks this env var

---

### Method 2: Use Explicit Model ID

Don't use the `"opus"` alias — use the explicit model ID:

```json
{
  "model": "claude-opus-4-6"
}
```

**Migration check** only looks for `"opus"` string, not explicit IDs.

---

### Method 3: Downgrade After Migration

If already migrated, manually edit settings:

```bash
# Edit settings
vim ~/.claude/settings.json

# Change:
#   "model": "opus[1m]"
# To:
#   "model": "opus"
# OR:
#   "model": "claude-opus-4-6"
```

---

## Feature Flag Rollout

### Current State (2.1.75)

```javascript
IA("tengu_cobalt_compass", false)  // Default: false
```

**Status**: Opt-in / gradual rollout. Most users won't see migration yet.

---

### Future State

When Anthropic enables the flag for your account:

```javascript
IA("tengu_cobalt_compass", true)  // Enabled
```

**Migration happens on next CLI startup** if you have `model: "opus"`.

---

## Telemetry Events

### `tengu_opus_to_opus1m_migration`

Fired when migration executes:

```javascript
Q("tengu_opus_to_opus1m_migration", {});
```

**Payload**: Empty (event presence indicates migration occurred)

---

### Related Events

From 2.1.74 analysis:

- `tengu_grey_wool` — Controls legacy model remapping (separate from 1M migration)
- `tengu_reset_pro_to_opus_default` — Pro plan → Opus 4.6 default (separate migration)

---

## Context Window Comparison

| Model | Alias | Context | Auto-Compact Default | Notes |
|-------|-------|---------|----------------------|-------|
| `claude-opus-4-6` | `opus` | 200K | 167K (~93%) | Pre-migration |
| `claude-opus-4-6[1m]` | `opus[1m]` | 1M | 967K (~99%) | Post-migration ⚠️ |

⚠️ **Critical**: The default auto-compact threshold for 1M is **967K tokens** — almost the entire window. See [auto-compact-deep-dive.md](./auto-compact-deep-dive.md) for recommended overrides.

---

## Recommended Post-Migration Settings

After migration to `opus[1m]`, set auto-compact overrides:

```bash
# Maintain similar compaction behavior as 200K Opus
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=350000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=85
```

**Result**: Auto-compact at ~280K tokens instead of 967K.

See: [auto-compact-deep-dive.md](./auto-compact-deep-dive.md)

---

## Migration Timeline

### Phase 1: 2.1.75 Release (Current)

- Feature flag infrastructure in place
- Migration code shipped
- Default: **disabled** (`tengu_cobalt_compass = false`)
- Users can manually select `opus[1m]` if desired

---

### Phase 2: Gradual Rollout (Future)

- Anthropic enables `tengu_cobalt_compass` for percentage of users
- Auto-migration begins for flagged accounts
- Telemetry collected via `tengu_opus_to_opus1m_migration`

---

### Phase 3: Full Rollout (Future)

- Feature flag enabled for all first-party users
- `opus` alias may eventually resolve directly to `opus[1m]`
- Migration code becomes dead code (all users migrated)

---

## Testing Migration

### Check If Gate Is Open

```bash
# Start a session and check logs for:
# [gate] tengu_cobalt_compass = <true|false>

# Or check indirectly:
claude --version
# If gate is open and you have model: "opus", next startup will migrate
```

---

### Simulate Migration

```bash
# 1. Set model to "opus"
echo '{"model": "opus"}' > ~/.claude/settings.json

# 2. If gate is closed (default), migration won't run
# To test migration logic, you'd need the feature flag enabled server-side

# 3. Check if migrated after restart
cat ~/.claude/settings.json | grep model
# If gate was open: "model": "opus[1m]"
```

---

## Edge Cases

### What if I switch models after migration?

**No re-migration**. The migration only runs if:
- Gate is open (`tengu_cobalt_compass = true`)
- Current model is `"opus"`

If you switch to `"sonnet"` and back to `"opus"`, migration would run again on next startup (gate still open).

---

### What if I'm on Bedrock/Vertex/Foundry?

**No migration**. The gate checks:

```javascript
BL() !== "firstParty"  // Blocks enterprise backends
```

Enterprise/cloud users don't auto-migrate.

---

### What if I have a custom model?

```json
{
  "model": "claude-opus-4-6-custom"
}
```

**No migration**. Check only looks for exact string `"opus"`.

---

## Related Models

### Sonnet 1M

**No auto-migration for Sonnet** in 2.1.75. Users must manually select:

```json
{
  "model": "sonnet[1m]"
}
```

---

### Haiku

**No 1M variant exists** for Haiku. 200K max.

---

## Code References

### Gate Function

```javascript
// cli.js:6819
function Yw() {
  if (ts() || MR() || BL() !== "firstParty") return false;
  return IA("tengu_cobalt_compass", false)
}
```

### Migration Function

```javascript
// cli.js:6988
function EI8() {
  if (!Yw()) return;
  if (RA("userSettings")?.model !== "opus") return;
  let newModel = "opus[1m]";
  EL("userSettings", { model: newModel });
  Q("tengu_opus_to_opus1m_migration", {});
}
```

### Execution Context

```javascript
// Startup migrations (called during init)
function WI8() {
  // ... other migrations ...
  EI8();  // Opus 1M migration
}
```

---

## Monitoring

### Check Settings

```bash
cat ~/.claude/settings.json | jq '.model'
```

**Expected**:
- Pre-migration: `"opus"` or `"claude-opus-4-6"`
- Post-migration: `"opus[1m]"` or `"claude-opus-4-6[1m]"`

---

### Check Session State

```bash
# During a session, run:
/config

# Look for:
# Model: opus[1m] (Claude Opus 4.6 - 1M context)
```

---

## FAQ

### Q: Will this affect my current session?

**A**: No. Migration runs on **startup**, not mid-session. Finish your current work, restart CLI, migration applies.

---

### Q: Can I revert after migration?

**A**: Yes. Edit `~/.claude/settings.json` and change `"model": "opus[1m]"` back to `"model": "opus"`.

---

### Q: Does this cost more?

**A**: Likely yes. 1M context models typically cost more per token. Check Anthropic pricing.

---

### Q: Do I need the auto-compact overrides?

**A**: Highly recommended. Without them, auto-compact triggers at 967K tokens (99% of 1M), which is impractical.

---

### Q: What if I'm on the free tier?

**A**: 1M context may not be available on free tier. Gate may check tier eligibility (not visible in this binary analysis).

---

## Related Documentation

- [analysis.md](./analysis.md) — Main 2.1.75 analysis
- [auto-compact-deep-dive.md](./auto-compact-deep-dive.md) — Context management post-migration
- [env-vars.md](./env-vars.md) — Environment variable reference
