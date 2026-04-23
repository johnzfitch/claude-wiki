---
title: "Feature Flags — 2.1.75 Reference"
category: "19-Reference"
tags: ["testing"]
---

# Feature Flags — 2.1.75 Reference

Complete reference for new and updated feature flags in Claude Code 2.1.75.

---

## New in 2.1.75

### `tengu_cobalt_compass`

**Type**: Boolean
**Default**: `false` (gradual rollout)
**Since**: 2.1.75
**Status**: Active (feature-flagged)

**Purpose**: Master gate for Opus 1M context migration.

**Behavior**: When enabled, auto-migrates users from `model: "opus"` to `model: "opus[1m]"` on startup.

**Conditions**:
- Only applies to **first-party users** (not Bedrock/Vertex/Foundry)
- Blocks if `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`
- Only migrates if current model is exactly `"opus"` (not explicit IDs)

**Code**:
```javascript
function Yw() {
  if (ts() || MR() || BL() !== "firstParty") return false;
  return IA("tengu_cobalt_compass", false);
}

function EI8() {
  if (!Yw()) return;
  if (RA("userSettings")?.model !== "opus") return;
  EL("userSettings", { model: "opus[1m]" });
  Q("tengu_opus_to_opus1m_migration", {});
}
```

**Related**:
- `tengu_opus_to_opus1m_migration` — Telemetry event
- `CLAUDE_CODE_DISABLE_1M_CONTEXT` — Opt-out mechanism
- See: [opus-1m-migration.md](./opus-1m-migration.md)

---

### `tengu_amber_wren`

**Type**: Object
**Default**: `{}` (uses hardcoded defaults)
**Since**: 2.1.75
**Status**: Active

**Purpose**: Runtime-configurable file read limits.

**Structure**:
```javascript
{
  maxSizeBytes: number,        // Byte limit per file read
  maxTokens: number,            // Token limit per file read (default: 25,000)
  includeMaxSizeInPrompt: boolean  // Show limit in Read tool prompt
}
```

**Code**:
```javascript
s1H = fA(() => {
  let H = IA("tengu_amber_wren", {}),
      maxSizeBytes = typeof H?.maxSizeBytes === "number" ? H.maxSizeBytes : ITA,
      maxTokens = jQ1() ?? (typeof H?.maxTokens === "number" ? H.maxTokens : 25000),
      includeMaxSizeInPrompt = typeof H?.includeMaxSizeInPrompt === "boolean"
                               ? H.includeMaxSizeInPrompt : undefined;
  return { maxSizeBytes, maxTokens, includeMaxSizeInPrompt }
})
```

**Use Case**: Prevent large file reads from consuming excessive memory in 1M context sessions.

**Related**:
- `tengu_pewter_gull` — Byte truncation enforcement
- `tengu_pewter_ledger` — Budget strategy (trim/cut/cap) from 2.1.74

---

### `tengu_pewter_gull`

**Type**: Boolean
**Default**: `false`
**Since**: 2.1.75
**Status**: Active (works with `tengu_amber_wren`)

**Purpose**: Enforces byte-based truncation on file reads when enabled.

**Code**:
```javascript
let enforceByteTruncation = f !== undefined && IA("tengu_pewter_gull", false),
    maxBytes = enforceByteTruncation
               ? Math.min(M, K * aTA(L))  // Byte limit
               : f === undefined ? M : undefined;  // Token limit only
```

**Behavior**: When `true`, applies byte limits from `tengu_amber_wren` to prevent oversized file reads.

**Related**:
- `tengu_amber_wren` — Defines the byte limits
- `tengu_pewter_ledger` — Budget strategy for tool results

---

### `tengu_bridge_repl_ws_closedn`

**Type**: Telemetry event
**Default**: N/A
**Since**: 2.1.75
**Status**: Active (telemetry only)

**Purpose**: Tracks WebSocket close events in Remote Control (bridge REPL) mode.

**Use Case**: Debugging Remote Control disconnections.

---

### `tengu_bug_report_description`

**Type**: Telemetry event
**Default**: N/A
**Since**: 2.1.75
**Status**: Active (telemetry only)

**Purpose**: Logs when users submit bug reports via `/issue`.

**Code**:
```javascript
// When /issue is invoked
Q("tengu_bug_report_description", { ... });
```

---

### `tengu_concurrent_sessions`

**Type**: Unknown (likely counter/limit)
**Default**: Unknown
**Since**: 2.1.75
**Status**: Active (CoWork feature)

**Purpose**: Tracks or limits concurrent sessions for CoWork/teams.

**Context**: Related to the `--cowork` flag and team-based collaboration features.

**Speculation**: May enforce max concurrent sessions per user/team to prevent resource exhaustion.

---

### `tengu_file_read_limits_override`

**Type**: Unknown (likely boolean or object)
**Default**: Unknown
**Since**: 2.1.75
**Status**: Dead code / placeholder

**Purpose**: Intended to override file read limits via environment variable (complementing `tengu_amber_wren`).

**Current State**: Token exists in binary diff but no implementation found. Likely placeholder for future `CLAUDE_CODE_FILE_READ_MAX_BYTES` env var.

---

## Removed in 2.1.75

### `tengu_compact_failedul`

**Reason**: Typo artifact — likely malformed variable name from string extraction.

---

### `tengu_image_resize_fallbackw`

**Reason**: Image resize fallback feature stabilized and merged into main path.

---

### `tengu_marble_lantern_disabled`

**Reason**: Separate "disabled" state no longer needed — merged into main `tengu_marble_lantern` flag.

---

## Existing Flags (Relevant to 2.1.75)

### `tengu_pewter_ledger`

**Type**: Enum (`"trim"` | `"cut"` | `"cap"`)
**Default**: `null`
**Since**: 2.1.74
**Status**: Active (works with `tengu_pewter_gull`)

**Purpose**: Defines the budget strategy for tool results when exceeding token limits.

**Strategies**:
- `"trim"` — Truncate to fit budget
- `"cut"` — Remove lowest-priority sections
- `"cap"` — Hard stop at budget limit

**Code** (from 2.1.74):
```javascript
function tq$() {
  let H = IA("tengu_pewter_ledger", null);
  if (H === "trim" || H === "cut" || H === "cap") return H;
  return null;
}
```

**Related**:
- `tengu_pewter_gull` — File read byte truncation
- `tengu_hawthorn_window` + `tengu_hawthorn_steeple` — Per-tool-result persistence (2.1.74)

---

### `tengu_grey_wool`

**Type**: Boolean
**Default**: `true`
**Since**: Pre-2.1.59
**Status**: Active

**Purpose**: Enables legacy model remapping (e.g., `opus-4-0` → current Opus).

**Code**:
```javascript
function Ux$() {
  if (tH(process.env.CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP)) return false;
  return IA("tengu_grey_wool", true);
}
```

**Related**:
- `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` — Env var override

---

### `tengu_orchid_trellis`

**Type**: Boolean
**Default**: `false` (gated)
**Since**: 2.1.74
**Status**: Active (marketplace infrastructure exists, feature-flagged off)

**Purpose**: Gates the MCP marketplace feature.

**Expected Behavior** (when enabled):
- Exposes plugin/marketplace discovery UI
- Enables plugin installation from marketplace
- May use `CLAUDE_PLUGIN_OPTION_*` env vars for config

**Current State**: Infrastructure exists, UI gated. Likely activating in upcoming release.

---

## Feature Flag Families

### `tengu_amber_*` — UI/UX Features

- `tengu_amber_flint` — Agent teams (active)
- `tengu_amber_prism` — Unknown (active)
- `tengu_amber_quartz` — Unknown (active)
- `tengu_amber_wren` — **NEW**: File read limits (2.1.75)

---

### `tengu_pewter_*` — Budget/Truncation System

- `tengu_pewter_ledger` — Budget strategy (trim/cut/cap) (2.1.74)
- `tengu_pewter_gull` — **NEW**: Byte truncation enforcement (2.1.75)

---

### `tengu_cobalt_*` — NEW Family in 2.1.75

- `tengu_cobalt_compass` — Opus 1M migration gate
- `tengu_cobalt_frost` — Nova 3 STT provider for voice (from voice stream code)

**Speculation**: "Cobalt" family = migration/upgrade pathways.

---

## Telemetry Events

Events logged via `Q()` function (analytics).

### New in 2.1.75

| Event | Trigger | Payload |
|-------|---------|---------|
| `tengu_opus_to_opus1m_migration` | Opus → Opus 1M migration executed | `{}` |
| `tengu_bug_report_description` | `/issue` bug report submitted | Unknown |
| `tengu_bridge_repl_ws_closedn` | Remote Control WebSocket closed | Unknown |

---

### Existing (Related to 2.1.75)

| Event | Trigger | Payload |
|-------|---------|---------|
| `tengu_sm_compact_*` | Session memory compaction | Various |
| `tengu_pdf_page_extraction` | PDF read with page range | `{ success, pageCount, ... }` |
| `tengu_session_file_read` | File read via Read tool | `{ totalLines, readLines, ... }` |
| `tengu_tool_use_diff_computed` | Git diff computed for tool result | `{ isEditTool, durationMs, hasDiff }` |

---

## Debugging Feature Flags

### Check Active Flags

Feature flags are server-controlled and not visible in client-side config. You can infer state from behavior:

```bash
# Check if Opus 1M migration happened
cat ~/.claude/settings.json | jq '.model'
# "opus[1m]" = migration occurred (tengu_cobalt_compass was enabled)

# Check if marketplace is enabled
/marketplace list
# If command works, tengu_orchid_trellis is enabled
```

---

### Telemetry Debug

If you have access to Anthropic's internal telemetry dashboard, search for:

- `tengu_opus_to_opus1m_migration` — Migration count
- `tengu_cobalt_compass` — Flag enablement rate

---

## A/B Testing

Many `tengu_*` flags are used for **gradual rollout** and **A/B testing**:

- Small % of users get `tengu_cobalt_compass = true`
- Anthropic monitors telemetry for issues
- If successful, rollout expands
- Eventually becomes default behavior (flag removed)

---

## Related Documentation

- [analysis.md](./analysis.md) — Main 2.1.75 analysis
- [opus-1m-migration.md](./opus-1m-migration.md) — Opus 1M migration details
- [auto-compact-deep-dive.md](./auto-compact-deep-dive.md) — Context management
- [env-vars.md](./env-vars.md) — Environment variable reference
