# 2.1.74 Deep Analysis

**Binary:** `/home/zack/claude-binary/2.1.74/2.1.74`
**Analyzed:** 2026-03-13
**pyghidra:** `e5613610deee76cd-deep` (68,720 functions)
**JS payload:** `2.1.74_bunfs_extracted/src/entrypoints/cli.js` (14,676 lines, 11MB)
**Delta base:** 2.1.72 (diff.md), 2.1.70 (function count)

---

## Summary Stats

| Metric | 2.1.70 | 2.1.74 | Delta |
|--------|--------|--------|-------|
| Binary size | 241MB | 235MB | -6MB |
| Functions (deep) | 68,960 | 68,720 | -240 |
| JS payload lines | 13,026 | 14,676 | +1,650 |
| JS payload size | 11MB | 11MB | ~0 |

The +1,650 line jump with no file size increase is explained by embedded SDK documentation
(see section 5). The binary shrunk slightly — likely JS minification improvement.

---

## 1. Diff.md Flag Classifications — Corrections

The `claude-binary-intel` diff extracted strings that are NOT new Claude Code CLI flags:

| "Flag" | Actual location | True meaning |
|--------|----------------|--------------|
| `--auto-approve` | Safety rules warning text (L2827) | Dangerous Terraform/infra pattern in safety blocklist |
| `--kill-after` | `ZQ()` bash security parser (L6395) | Unix `timeout(1)` flag — now ALLOWED by security checker |
| `--preserve-status` | same | same |
| `--signal` | same | same |
| `--remote-control` | ✅ Real — `remoteControlSpawnMode` | New Claude Code remote session spawn mode flag |

### `ZQ()` Bash Security Parser Update

`ZQ()` is the bash command security classifier. Its allowlist regex was updated in 2.1.74
to recognize `timeout --kill-after=N --signal=X duration cmd` as a safe pattern:

```javascript
function ZQ(H) {
  let $ = [
    /^timeout[ \t]+(?:(?:--(?:foreground|preserve-status|verbose)|
     --(?:kill-after|signal)=[A-Za-z0-9_.+-]+|
     --(?:kill-after|signal)[ \t]+[A-Za-z0-9_.+-]+|
     -v|-[ks][ \t]+[A-Za-z0-9_.+-]+|-[ks][A-Za-z0-9_.+-]+)[ \t]+)*
     (?:--[ \t]+)?\d+(?:\.\d+)?[smhd]?[ \t]+/,
    // ...
  ]
}
```

Before 2.1.74, using `timeout --kill-after=5 30 cmd` would trigger a security review.
Now it passes through. This is a security policy relaxation, not a new Claude Code feature.

---

## 2. `ANTHROPIC_UNIX_SOCKET` — Local API Proxy Architecture

Three separate call sites, each with distinct behavior:

### L170 — Network dispatch (`SDH()`)
```javascript
function SDH(H) {
  if (H?.forAnthropicAPI) {
    let A = process.env.ANTHROPIC_UNIX_SOCKET;
    if (A && typeof Bun !== "undefined") return { unix: A };  // Bun-only
  }
  let $ = ZN();  // proxy check
  if ($) {
    if (typeof Bun !== "undefined") return { proxy: $ };
    return { dispatcher: tLA($) };
  }
  return kD$();
}
```
Routes all Anthropic API HTTP calls through a Unix domain socket. **Bun runtime only** —
falls through to standard HTTP if not running under Bun.

### L6825 — Auth gate (`jO()`)
```javascript
function jO() {
  if (process.env.ANTHROPIC_UNIX_SOCKET)
    return !!process.env.CLAUDE_CODE_OAUTH_TOKEN;
  // normal auth check: bedrock / vertex / foundry / API key ...
}
```
When `ANTHROPIC_UNIX_SOCKET` is set, the only valid auth is `CLAUDE_CODE_OAUTH_TOKEN`.
API keys, bedrock, vertex, foundry auth are all bypassed. The proxy is expected to handle auth.

### L6915 — Credential stripping (`AoH()`)
```javascript
function AoH(H) {
  if (!H || !process.env.ANTHROPIC_UNIX_SOCKET) return H || {};
  let {
    ANTHROPIC_UNIX_SOCKET: $,
    ANTHROPIC_BASE_URL: A,
    ANTHROPIC_API_KEY: L,
    ANTHROPIC_AUTH_TOKEN: D,
    CLAUDE_CODE_OAUTH_TOKEN: f,
    ..._
  } = H;
  return _;  // subprocess env has NO auth vars
}
```
When spawning tool subprocesses (Bash, etc.), strips all auth-related env vars.
Spawned tools cannot exfiltrate credentials when using the unix socket proxy.

### Design Pattern
The three sites together implement a **sidecar proxy architecture**:
```
[Claude Code] --unix socket--> [Local proxy] --HTTPS--> [Anthropic API]
                                    ^
                                    handles auth, routing, logging
     spawned tools: NO CREDENTIALS
```
Intended for enterprise/managed environments where a local proxy controls API access.
Not documented publicly as of 2026-03-13.

---

## 3. Hawthorn System — Message-Level Tool Result Budget (new in 2.1.74)

### Feature flags
- `tengu_hawthorn_window` — numeric: token budget per message (default `$nD`)
- `tengu_hawthorn_steeple` — boolean: enables compression/persistence

### Mechanism
```javascript
function Hb1() {  // get window size
  let H = XA("tengu_hawthorn_window", null);
  return (Number.isFinite(H) && H > 0) ? H : $nD;
}

function MnD(H, $) {  // run compression if enabled
  if (!XA("tengu_hawthorn_steeple", false)) return;
  if (H) return VGA(H, $ ?? []);  // persist oversized results
  return _nD();  // return empty state
}
```

When a tool result exceeds the window budget, it is **persisted to disk** and replaced
with a lightweight reference in the message context. This operates per-tool-result,
below the existing autocompact system (which handles the whole conversation).

### Truncation strategies — `tengu_pewter_ledger`
```javascript
function BM$() {
  let H = XA("tengu_pewter_ledger", null);
  if (H === "trim" || H === "cut" || H === "cap") return H;
  return null;
}
```
Three selectable strategies for content reduction before persistence:
- `"trim"` — trim from edges
- `"cut"` — hard cut
- `"cap"` — cap at limit

### Telemetry events
- `tengu_tool_result_persisted_message_budget` — fires per-persistence with `originalSizeBytes`, `persistedSizeBytes`
- `tengu_message_level_tool_result_budget_enforced` — fires when system activates with `resultsPersisted`, `messagesOverBudget`, `replacedSizeBytes`

### Relationship to autocompact
Hawthorn operates at the **individual message level**, before autocompact kicks in.
It silently shrinks oversized tool results without triggering a full context compaction.
Users cannot observe this happening from the outside.

---

## 4. Tengu Feature Flags — Full Inventory (new in 2.1.74)

| Flag | JS function | Gate |
|------|-------------|------|
| `tengu_hawthorn_window` | `Hb1()` | Tool result budget window size (numeric) |
| `tengu_hawthorn_steeple` | `MnD()` | Enables tool result compression/persistence |
| `tengu_pewter_ledger` | `BM$()` | Truncation strategy: "trim"/"cut"/"cap" |
| `tengu_orchid_trellis` | `T6H()` | MCP plugin **marketplace** — gated feature flag |
| `tengu_chair_sermon` | `Cs6()` | Message array construction: tool result + user message merging |
| `tengu_marble_whisper2` | `s6H()` + `hzf()` | Content pattern detection v2 (regex `d96`) |
| `tengu_auto_mode_state` | `kE6()` | Reports auto mode state in `experiment_gates` notification |
| `tengu_tool_empty_result` | `fnD()` | Empty tool result → replace with `"(tool completed with no output)"` |
| `tengu_voice_stream_early_retry` | voice loop | Pre-transcript stream failure → 250ms retry |
| `tengu_voice_recording_completed` | voice loop | Telemetry on recording completion with char count, duration, audio signal |
| `tengu_compact_failedul` | unknown | Compact failure event |
| `tengu_image_resize_fallbackw` | image pipeline | Image resize fallback path telemetry |

### Removed flags (were in 2.1.72, gone in 2.1.74)
- `tengu_marble_whisper` → replaced by `tengu_marble_whisper2`
- `tengu_native_version_cleanupk`
- `tengu_output_style_command_inline` / `_inline_help` / `_menu`
- `tengu_pdf_page_extractionm`
- `tengu_unexpected_tool_resulti`

### `tengu_orchid_trellis` — MCP Plugin Marketplace
`T6H()` gates `Bff()`, the MCP plugin marketplace refresh function. This implies a full
plugin marketplace browser is built into Claude Code but gated off. The infrastructure:
```javascript
function T6H() { return XA("tengu_orchid_trellis", false) }
async function Bff(H, $, A) {
  let L = yK(H).marketplace, D = [], f = new Set, _ = [];
  // ... marketplace operations ...
}
```

### `tengu_chair_sermon` — Message Merge Behavior
Controls how tool results combine with subsequent user messages (L6487):
```javascript
function Cs6(H, $) {
  let A = uN(H);
  if (A?.type !== "tool_result") return [...H, ...$];
  if (!CM("tengu_chair_sermon")) {
    // old path: merge string content directly
    if (typeof A.content === "string" && $.every(_ => _.type === "text"))
      return [...H.slice(0,-1), wnA(A, $)];
    return [...H, ...$];
  }
  // new path: different merge logic (attachment-aware)
}
```
When enabled, uses a new code path for message array construction, particularly for
attachment-type messages. "Sermon" — unusual name with no clear semantic.

---

## 5. Embedded SDK Documentation (source of +1,650 lines)

Lines ~8700–9600+ contain Anthropic SDK reference documentation embedded directly
in the JS payload. Claude uses this for answering developer questions without external lookups.

### Coverage
| SDK | Topics |
|-----|--------|
| REST API (curl) | Basic messages, tool use, streaming, extended thinking, required headers |
| Go (`github.com/anthropics/anthropic-sdk-go`) | Client init, messages, streaming, tool use, thinking, context management, beta API |
| Java (`com.anthropic.models.messages`) | Messages, streaming, thinking/adaptive, tool use, structured output, PDF/document input |
| PHP | Client init, `ANTHROPIC_FOUNDRY_AUTH_TOKEN` example |

### Implications for "new env var" misclassification
- `CLAUDE_SONNET_4_6` in diff: NOT a runtime env var — it's `Model.CLAUDE_SONNET_4_6` Java enum in a code example
- `ANTHROPIC_FOUNDRY_AUTH_TOKEN` in diff: appears in PHP example `getenv('ANTHROPIC_FOUNDRY_AUTH_TOKEN')` — likely a real env var but the SDK doc is what surfaced it
- Line count growth (+1,650): almost entirely these docs, not new feature logic

---

## 6. New Env Vars — Verified Behavior

### `CLAUDE_CODE_FRAME_TIMING_LOG` (L14632)
```javascript
let f = process.env.CLAUDE_CODE_FRAME_TIMING_LOG;
return {
  renderOptions: {
    onFrame: (_) => {
      if (L.record(_.durationMs), D.observe("frame_duration_ms", _.durationMs), f && _.phases) {
        let M = JSON.stringify({ total: _.durationMs, phases: _.phases });
        // append to log
      }
    }
  }
}
```
When set (to a file path), logs per-frame render timing as JSON: `{total, phases}`.
Used for diagnosing UI rendering performance / jank.

### `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` (L6774)
```javascript
function pUA() {
  let H = process.env.CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS;
  let $ = H ? parseInt(H, 10) : NaN;
  return (Number.isFinite($) && $ > 0) ? $ : Re6;  // Re6 = default timeout
}
```
Controls timeout for session-end hook execution. Default is `Re6` (constant, not traced).
Allows extending timeout for long-running cleanup hooks.

### `ANTHROPIC_UNIX_SOCKET` — See section 2 above.

### `CLAUDE_SONNET_4_6` — NOT a Claude Code env var. See section 5.

---

## 7. New Model IDs

### `claude-code-feedback`
Added as a model ID in 2.1.74. References to `#claude-code-feedback` Slack channel
(ID: `C07VBSHV7EV`) in the `/stuck` skill are a coincidence of naming. The model ID
likely routes internal feedback-collection API calls to a specialized endpoint.

### `claude-for-hiring` — See `claude-for-hiring-analysis.md`
Listed in `SN1` internal repo detection array. Its only effect: when Claude Code is run
inside the `anthropics/claude-for-hiring` repo, `PBD()` returns true, causing git commits
to use the real model name in `Co-Authored-By` instead of "Claude Opus 4.6".

---

## 8. `OBD` / `PBD` — Internal Repo Detection (correcting claude-for-hiring-analysis.md)

```javascript
// OBD: async memoized detection
OBD = _x(async () => {
  if (VpH !== null) return VpH === "internal";
  let H = cI$();           // CWD
  let $ = await AM$(H);    // git remote URL
  if (!$) return VpH = "none", false;
  let A = SN1.some((L) => $.includes(L));
  return VpH = A ? "internal" : "external", A;
});

// PBD: synchronous cache reader
function PBD() { return VpH === "internal" }
```

`PBD()` is called **exactly once** (not 2 as stated in the prior analysis file).

### The single call site (L4024) — commit attribution
```javascript
let A = PBD() || $ ? eUA(H) : "Claude Opus 4.6"
let D = `Co-Authored-By: ${A} <noreply@anthropic.com>`
```
- Internal Anthropic repos (or authenticated users via `$`) → `eUA(H)` = real model name
- External users → hardcoded `"Claude Opus 4.6"`

The only feature gate is the git `Co-Authored-By` footer. No special tooling, no telemetry fork.

### Complete `SN1` internal repo list (19 repos, both SSH and HTTPS forms):
```
claude-cli-internal, anthropic, apps, casino, dbt, dotfiles,
terraform-config, hex-export, feedback-v2, labs, argo-rollouts,
starling-configs, ts-tools, ts-capsules, feldspar-testing, trellis,
claude-for-hiring, forge-web, infra-manifests
```

---

## 9. Remote Control — `remoteControlSpawnMode`

`--remote-control` is a real new flag. It prompts the user to choose a spawn mode
during remote session setup (L6915):

```javascript
// User sees:
// [1] same-dir — session shares current directory
// [2] worktree — each session gets an isolated git worktree

let mH = await readline.question("Choose [1/2] (default: 1): ");
let BH = mH.trim() === "2" ? "worktree" : "same-dir";
// → stored in remoteControlSpawnMode
```

Related new env vars: `CLAUDE_CODE_REMOTE_SESSION_ID`, `SESSION_INGRESS_URL`.

---

## 10. Notable / Suspicious Items

1. **MCP Plugin Marketplace** (`tengu_orchid_trellis`) — Full marketplace infrastructure exists, feature-flagged off. Imminent public release likely.

2. **Unix socket credential stripping** (`AoH()`) — Sophisticated security isolation. Not documented publicly. May be the foundation for a future "secure mode" where tools run with zero API access.

3. **Hawthorn budget system** — Operates silently on individual tool results. Users and developers can't observe it without telemetry. Could cause subtle context differences in long tool-heavy sessions.

4. **`tengu_chair_sermon`** — Alters fundamental message array construction. Odd name with no semantic meaning. Potential edge case surface for context corruption. Worth monitoring.

5. **`tengu_marble_whisper` → `tengu_marble_whisper2`** — Content detection pattern matching versioned/rewritten. The original behavior (whatever `d96` regex matches) has changed.

6. **`electron_asar` runtime detection** — `info full` reports both `bunfs` AND `electron_asar` with high confidence. This wasn't flagged in 2.1.70. Could indicate a new bundling artifact or a false positive in pyghidra-lite's detection.
