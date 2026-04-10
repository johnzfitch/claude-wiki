# Claude Code 2.1.59 — Binary Analysis Summary

## Binary Facts
```
File:     ~218MB ELF 64-bit LSB executable, x86-64, not stripped
Build:    Bun 1.3.10 compiled
Runtime:  JavaScriptCore (WebKit) — ~103MB mapped native code
Payload:  BunFS VFS ~124MB — all application logic in cli.js (10.9MB, 11,832 lines)
Symbols:  10,001 (not stripped), 60,300 functions under deep Ghidra analysis
Date:     2026-02-25T23:37:51Z (from VERSION constant)
```

**Key architectural insight:** The mapped native code is unchanged between 2.1.55 and 2.1.59 — it is the Bun/JSC runtime. All behavioral changes are in the BunFS JS payload.

---

## Module Cross-Reference

### Module 01: Auth & Identity (`modules/01-auth-identity/report.md`)
**5 auth paths:** OAuth PKCE (browser), refresh token exchange, API key (`ANTHROPIC_API_KEY`), Claude.ai session cookie, enterprise OIDC.

Key flows: `authLogin (E59)` PKCE → `/oauth/authorize` → `/oauth/token`; `GRH(refreshToken)` → `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` env bootstrap.

**Cross-references:**
- → Module 06: auth events: `tengu_oauth_*`, `tengu_login_from_refresh_token`
- → Module 06: GrowthBook re-init on auth change (`D_H()`)
- → Module 10: Voice requires `Vq()` (OAuth session, not API key)
- → Module 03: trust dialog on first run includes auth context
- → Module 05: CCRClient uses auth headers from `B5().headers`

---

### Module 02: Model Routing & API (`modules/02-model-routing/report.md`)
**Request pipeline:** thinking config injection → messages API streaming → watchdog timers → retry loop (10 retries, exponential backoff) → context overflow → model fallback.

Key: Fast mode uses separate model variant; `coral_reef_opus` = Opus fast-mode alias; streaming watchdog: first-token 30s, inter-chunk 60s.

**Cross-references:**
- → Module 06: `tengu_max_tokens_reached`, `tengu_context_window_exceeded`, `tengu_api_*` events
- → Module 05: `kN()` runs the API stream in inProcessRunner loop
- → Module 03: tool result parsing checks permissions before each tool call
- → Module 01: `B5().headers` provides auth to API requests

---

### Module 03: Permission & Safety (`modules/03-permission-safety/report.md`)
**6 permission modes** — default, acceptEdits, dontAsk, plan, bypassPermissions. Rule sources in priority order from `policySettings` (enterprise) down to `projectSettings`. Hook system fires on PermissionRequest events.

Native layer: `checkVMEntryPermission()` (JSC-level, not user-facing); `CLAUDE_CODE_AGENT_RULE_` → native `FUN_03111620`.

**Cross-references:**
- → Module 04: MCP tools always return `{behavior: "passthrough"}` — defer to this system
- → Module 07: `FUN_03111620` reads `CLAUDE_CODE_AGENT_RULE_` env var, calls `parseAgentRule (FUN_02fec150)` parser
- → Module 06: `tengu_trust_dialog_accept`, `tengu_bypass_permissions_mode_dialog_*`
- → Module 05: `bypassPermissions` + `isBypassPermissionsModeAvailable` → auto-allow in plan mode

---

### Module 04: MCP & Tool Execution (`modules/04-mcp-tools/report.md`)
**5 transport types:** stdio, sse, http, claudeai-proxy, sdk. Tool names: `mcp__<server>__<tool>` (except sdk+`CLAUDE_AGENT_SDK_MCP_NO_PREFIX`). SSE reconnect: max 600s window, liveness 45s timeout.

Key: MCP is entirely JS-layer; no native MCP code exists in the mapped binary.

**Cross-references:**
- → Module 03: MCP tools defer permission to rule engine
- → Module 06: `tengu_mcp_server_connection_failed`, `tengu_mcp_tools_commands_loaded`
- → Module 05: CCRClient uses SSE transport variant (`CLAUDE_CODE_USE_CCR_V2`)

---

### Module 05: Worker & Session (`modules/05-worker-session/report.md`)
**Three worker concepts:**
1. CCRClient — cloud session manager (CLAUDE_CODE_WORKER_EPOCH, 20s heartbeat, 409→shutdown)
2. Bun WebWorker — native OS threads via pthread (FUN_046444b0 exit handler)
3. InProcessBackend — teammate agent loop (inProcessRunner)

Session: `--continue` finds latest, `--resume <id>` fuzzy matches, `--from-pr` links to PR.

**Cross-references:**
- → Module 07: Worker exit → FUN_046444b0 → JSC VM cleanup chain
- → Module 06: `cli_worker_lifecycle_initialized`, `cli_worker_epoch_mismatch`, `tengu_continue`
- → Module 03: plan mode + bypassPermissions in agent spawning
- → Module 04: CCRClient uses SSE or WebSocket transport from Module 04

---

### Module 06: Telemetry & Feature Flags (`modules/06-telemetry-flags/report.md`)
**Dual flag system:** GrowthBook (remote eval, api.anthropic.com, 6hr refresh) + Statsig (local gate cache). Resolution: `forcedFeatureValues` → GrowthBook in-memory → config cache → Statsig → default.

**New in 2.1.59:** `tengu_amber_quartz` (voice mode gate), `tengu_slate_ridge` (MCP experiment gate), `tengu_voice_*` events, `tengu_session_memory`, `tengu_scratch`.

**Cross-references:**
- → All modules: `c()` / `LA()` emit `tengu_*` events throughout the codebase
- → Module 01: GrowthBook attributes include `accountUUID`, `organizationUUID`, `email`
- → Module 10: `tengu_voice_toggled`, `tengu_voice_recording_started`

---

### Module 07: Native Runtime Internals (`modules/07-native-runtime/report.md`)
JSC GC (FUN_0485a3e0, 52K refs — most-called function), property hash table (FUN_048efce0, 24K refs). Largest function: FUN_05da1fd0 (818KB, likely JIT dispatch table).

**Key discovery:** `CLAUDE_CODE_AGENT_RULE_` is read in native code (FUN_03111620), not JS — the only `CLAUDE_CODE_*` env var in mapped native code.

**Cross-references:**
- → Module 03: `CLAUDE_CODE_AGENT_RULE_` bridges native and JS permission layers
- → Module 05: Worker exit handler (FUN_046444b0) → JSC context cleanup sequence
- → Module 09: file-index.node, ripgrep.node NAPI loaded via full NAPI surface

---

### Module 08: Plugin System (`modules/08-plugin-system/report.md`)
**Marketplace sources:** github, git, url, directory, file, npm. Enterprise policy: `strictKnownMarketplaces` (allowlist), `blockedMarketplaces` (blocklist), `hostPattern` matching.

Git clone: `--depth 1 --recurse-submodules --shallow-submodules`. Zip cache mode (`CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE`) for headless/CI. Official marketplace auto-install: exponential backoff (1hr → 7 days, max 10 attempts).

**Cross-references:**
- → Module 04: Plugins can declare `mcpServers` in manifest → loaded as MCP servers
- → Module 06: `tengu_plugin_installed`, `tengu_headless_plugin_install`, `tengu_marketplace_background_install`, `tengu_official_marketplace_auto_install`
- → Module 01: `CLAUDE_CODE_REMOTE` env var selects HTTPS vs SSH for github URLs

---

### Module 09: File Operations & Search (`modules/09-file-search/report.md`)
**Primary:** git ls-files (5s timeout, --recurse-submodules) with parallel untracked fetch.
**Fallback:** ripgrep (`--files --follow --hidden --glob !.git/`).
**Search:** Rust FileIndex NAPI → Fuse.js fallback (threshold 0.5, filename weight 2x path).
**Ignore:** `.ignore`, `.rgignore` files honored.

**Cross-references:**
- → Module 07: file-index.node loaded via NAPI surface (ripgrep.node also present)
- → Module 06: `tengu_file_suggestions_*` events
- → Module 03: `isBinaryOrGenerated (igD)` binary/generated file detection used in write permission checks

---

### Module 10: Voice & Audio (`modules/10-voice-audio/report.md`) — New in 2.1.59
**Audio backends:** native platform API → arecord (Linux ALSA) → SoX rec.
**Protocol:** PCM S16_LE 16kHz mono → WebSocket voice_stream → server-side STT → interim + final transcripts.
**Trigger:** Hold Space (5 spaces in 120ms window). Focus mode: auto-start on focus gain.
**11 languages supported.** Requires Claude.ai OAuth (not API key).

**Cross-references:**
- → Module 01: requires `Vq()` — Claude.ai OAuth session
- → Module 06: `tengu_voice_toggled`, `tengu_voice_recording_started`
- → Module 07: audio-capture.node loaded via NAPI

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code 2.1.59 Binary                    │
├──────────────────────────┬──────────────────────────────────────┤
│   Native (Bun/JSC)       │       JS Payload (BunFS cli.js)      │
│   ~103MB mapped          │       ~124MB, 11,832 lines           │
│                          │                                       │
│  JSC Engine:             │  ┌─────────────────────────────┐     │
│   GC (FUN_0485a3e0)      │  │  Auth & Identity (M01)      │     │
│   Hash (FUN_048efce0)    │  │  Model Routing  (M02)       │     │
│   JIT (FUN_054918f0)     │  │  Permissions    (M03)       │     │
│                          │  │  MCP/Tools      (M04)       │     │
│  NAPI modules:           │  │  Workers/Session(M05)       │     │
│   ripgrep.node    ──────────→ File Search     (M09)       │     │
│   file-index.node ──────────→ File Search     (M09)       │     │
│   color-diff.node        │  │  Telemetry/FF   (M06)       │     │
│   image-processor.node   │  │  Plugin System  (M08)       │     │
│   audio-capture.node ───────→ Voice/Audio     (M10)       │     │
│                          │  └─────────────────────────────┘     │
│  Env: CLAUDE_CODE_       │                                       │
│   AGENT_RULE_  (native!) │  External APIs:                      │
│                          │   api.anthropic.com (models + FF)     │
│                          │   claude.ai OAuth                     │
│                          │   voice_stream WebSocket              │
└──────────────────────────┴──────────────────────────────────────┘
```

---

## Changes in 2.1.59 vs Earlier Versions

### Confirmed New in 2.1.59
| Feature | Module | Evidence |
|---------|--------|---------|
| Voice/Audio system | M10 | audio-capture.node, VOICE_STREAM_BASE_URL, tengu_voice_* events |
| `tengu_amber_quartz` gate | M06 | Not in 2.1.41/2.1.42/2.1.50 string extracts |
| `tengu_slate_ridge` gate | M06 | Not in earlier versions |
| `tengu_session_memory` gate | M06 | New |
| `tengu_scratch` gate | M06 | New — scratchpad directory feature |
| `tengu_bridge_poll_interval_ms` | M06 | New |
| `tengu_login_from_refresh_token` | M06 | New |
| `tengu_worktree_detection` | M06 | New — worktree detection metrics |

### Native Code
Mapped native code is **identical** between 2.1.55 and 2.1.59. All version differences are JS-payload only.

---

## Key Env Vars — Master Reference

| Env Var | Module | Effect |
|---------|--------|--------|
| `ANTHROPIC_API_KEY` | M01 | Direct API key auth |
| `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` | M01 | Bootstrap OAuth session |
| `CLAUDE_CODE_ACCOUNT_UUID` | M01 | Pre-set account UUID |
| `CLAUDE_CODE_AGENT_RULE_` | M03/M07 | Native agent rule (parsed in native code) |
| `CLAUDE_CODE_WORKER_EPOCH` | M05 | CCRClient epoch (required integer) |
| `CLAUDE_CODE_USE_CCR_V2` | M05 | SSE-based CCR transport |
| `CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2` | M05 | HTTP POST ingress mode |
| `CLAUDE_AGENT_SDK_MCP_NO_PREFIX` | M04 | Skip mcp__ prefix for sdk transport |
| `MCP_CONNECTION_NONBLOCKING` | M04 | Don't block startup on MCP connect |
| `CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE` | M08 | Enable ZIP cache mode |
| `CLAUDE_CODE_PLUGIN_CACHE_DIR` | M08 | Override plugin cache directory |
| `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` | M08 | Git operation timeout (default 120s) |
| `CLAUDE_CODE_REMOTE` | M08 | Use HTTPS GitHub URLs (vs SSH) |
| `VOICE_STREAM_BASE_URL` | M10 | Override voice stream endpoint |
| `AUDIO_CAPTURE_NODE_PATH` | M10 | Override audio-capture.node path |
| `DISABLE_TELEMETRY` | M06 | Disable telemetry |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | M06 | Enable telemetry |
| `DO_NOT_TRACK` | M06 | Global telemetry disable |

---

## Resolved Questions (Cross-Module)

1. **`tengu_amber_quartz`** (M06): Gates **voice mode**. `YS$()` checks this flag; `Vq()` requires both OAuth account AND this flag. Voice is hidden when `Vq()` is false, disabled when `YS$()` is false.

2. **`tengu_slate_ridge`** (M06): Only used in the `experiment_gates` MCP notification. Communicated to connected MCP servers alongside `tengu_quiet_fern` and `tengu_penguins_enabled`. No direct client-side code path — exists for MCP server-side feature decisions.

3. **Voice stream endpoint** (M10): Direct WebSocket to `claude.ai` (not api.anthropic.com). URL derived from `CLAUDE_AI_AUTHORIZE_URL` origin with `https://` replaced by `wss://`. Overridable via `VOICE_STREAM_BASE_URL`. Requires OAuth because it connects to claude.ai directly.

4. **GrowthBook client key** (M06): `EFL = "sdk-zAZezfDKGoZuXXKe"`.

5. **OAuth scopes** (M01): `Xx = "user:inference"` (inference-only scope). Full set: `FL$ = ["user:profile", "user:inference", "user:sessions:claude_code", "user:mcp_servers"]`.

6. **Sampling config** (M06): Server-driven via `tengu_event_sampling_config` feature flag. Batch size 10,000, queue limit 200, buffer 8,192.

## Open Questions (Cross-Module)

1. **`CLAUDE_CODE_AGENT_RULE_`** (M03/M07): What does `parseAgentRule (FUN_02fec150)` parse from the rule string? This is native code — requires deeper Ghidra decompilation. Likely a compiled DSL for rule evaluation.

2. **`(JIT_dispatchTable?) (FUN_05da1fd0)` (818KB)** (M07): One ref-in suggests it's a static dispatch table, possibly the JSC bytecode dispatch table. Size consistent with opcode dispatch. Requires JSC source comparison.

3. **CCRClient epoch rotation** (M05): Server-side logic — the binary only reads `CLAUDE_CODE_WORKER_EPOCH` as a required integer. 409 response triggers immediate shutdown (strong consistency). What service generates epochs and when they rotate is not determinable from the client binary.

4. **Session memory** (`tengu_session_memory`) (M06): New gate in 2.1.59 — likely the "memory" feature for cross-session persistent notes. May be behind the gate and not yet fully active.
