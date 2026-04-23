---
title: "Claude Code CoWork Protocol Specification"
category: "02-Claude-Code-CLI"
tags: ["agents", "api", "claude-code", "cli", "oauth", "sdk"]
---

# Claude Code CoWork Protocol Specification

Reverse-engineered from claude binaries 2.1.74-2.1.75 (2026-03-11 to 2026-03-14).
Source: `2.1.75_bunfs_extracted/src/entrypoints/cli.js` (14,697 lines)

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Client Type Identification](#client-type-identification)
3. [OAuth Configuration](#oauth-configuration)
4. [CLI Spawning — Flags & Environment](#cli-spawning)
5. [stdin Protocol (Caller → CLI)](#stdin-protocol)
6. [stdout Protocol (CLI → Caller)](#stdout-protocol)
7. [Session JSONL Format](#session-jsonl-format)
8. [Sessions API](#sessions-api)
9. [WebSocket Subscription](#websocket-subscription)
10. [CoWork-Specific Behavior](#cowork-specific-behavior)
11. [Agent Teams (Teammate Mode)](#agent-teams)
12. [Session Resume Paths](#session-resume-paths)
13. [sdkUrl & Session Ingress Transport](#sdkurl-session-ingress-transport)
14. [Session Creation API](#session-creation-api)
15. [Bridge Orchestrator](#bridge-orchestrator)
16. [Remaining Unknowns](#remaining-unknowns)

---

## Architecture Overview

All three interfaces (CLI terminal, Claude Desktop, claude.ai web) run the **same `claude` binary**.
Differences are purely in:
- How the process is spawned (TTY vs child_process with piped stdio)
- Which env vars are set (entrypoint, auth mechanism, persistence flags)
- Whether stdin/stdout uses interactive Ink/React rendering vs stream-json protocol
- Whether persistence is local-only or dual-write to Sessions API

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Claude       │   │ Claude Code  │   │ claude.ai    │
│ Desktop      │   │ CLI          │   │ Web          │
│ (Electron)   │   │ (Terminal)   │   │ (Browser)    │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                   │
       │ ENTRYPOINT=      │ (unset→"cli")     │ ENVIRONMENT_KIND=
       │ "claude-desktop" │                   │ "bridge"
       │                  │                   │
       ▼                  ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ claude CLI   │   │ claude CLI   │   │  Bridge      │
│ (child proc) │   │ (direct)     │   │  (spawner)   │
│ stdin/stdout │   │ TTY I/O      │   │  Yz8()       │
│ stream-json  │   │ interactive  │   └──────┬───────┘
└──────┬───────┘   └──────┬───────┘          │
       │                  │           ┌──────▼───────┐
       │                  │           │ claude CLI   │
       │                  │           │ --print      │
       │                  │           │ stdin/stdout │
       │                  │           │ stream-json  │
       │                  │           └──────┬───────┘
       ▼                  ▼                  ▼
┌─────────────────────────────────────────────────┐
│              Anthropic API                      │
│         /v1/messages (Claude model)             │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              Sessions API                       │
│  /v1/sessions/<id>             (CRUD)           │
│  /v1/sessions/<id>/events      (event log)      │
│  /v1/sessions/ws/<id>/subscribe (WebSocket)     │
│  /v1/code/sessions/<id>/teleport-events         │
│  /v1/session_ingress/session/<id> (legacy)      │
└─────────────────────────────────────────────────┘
```

---

## Client Type Identification

Determined at startup from `CLAUDE_CODE_ENTRYPOINT`:

| CLAUDE_CODE_ENTRYPOINT | clientType      | Context                        |
|------------------------|-----------------|--------------------------------|
| `"sdk-cli"`            | `"sdk-cli"`     | Agent SDK invocation           |
| `"claude-vscode"`      | `"claude-vscode"` | VS Code extension            |
| `"local-agent"`        | `"local-agent"` | Desktop app local agent mode   |
| `"claude-desktop"`     | `"claude-desktop"` | Claude Desktop (Electron)   |
| `"remote"` (or token present) | `"remote"` | Remote / web session        |
| (unset)                | `"cli"`         | Bare terminal                  |

Additional identity in API User-Agent:
```
CLAUDE_AGENT_SDK_VERSION  → "agent-sdk/X.Y.Z"
CLAUDE_AGENT_SDK_CLIENT_APP → "client-app/<name>"
User-Agent: "claude-code/2.1.74 (sdk-cli, agent-sdk/1.0.0, client-app/myapp)"
```

When `CLAUDE_CODE_ENVIRONMENT_KIND=bridge`, session source is set to `"remote-control"`.

---

## OAuth Configuration

### Production Endpoints (s_L)

```
BASE_API_URL:            https://api.anthropic.com
CLAUDE_AI_AUTHORIZE_URL: https://claude.ai/oauth/authorize
CONSOLE_AUTHORIZE_URL:   https://platform.claude.com/oauth/authorize
TOKEN_URL:               https://platform.claude.com/v1/oauth/token
API_KEY_URL:             https://api.anthropic.com/api/oauth/claude_cli/create_api_key
ROLES_URL:               https://api.anthropic.com/api/oauth/claude_cli/roles
CONSOLE_SUCCESS_URL:     https://platform.claude.com/buy_credits?returnUrl=/oauth/code/success%3Fapp%3Dclaude-code
CLAUDEAI_SUCCESS_URL:    https://platform.claude.com/oauth/code/success?app=claude-code
MANUAL_REDIRECT_URL:     https://platform.claude.com/oauth/code/callback
CLIENT_ID:               9d1c250a-e61b-44d9-88ed-5944d1962f5e
MCP_PROXY_URL:           https://mcp-proxy.anthropic.com
MCP_PROXY_PATH:          /v1/mcp/{server_id}
```

Overridable via:
- `CLAUDE_CODE_CUSTOM_OAUTH_URL` — replaces all URLs with custom base
- `CLAUDE_CODE_OAUTH_CLIENT_ID` — replaces CLIENT_ID

### Scopes

```
Claude.ai flow (eH$):
  user:profile
  user:inference
  user:sessions:claude_code
  user:mcp_servers

Console flow (HML):
  org:create_api_key
  user:profile
```

### Token Exchange

```http
POST https://platform.claude.com/v1/oauth/token
Content-Type: application/json

{
  "grant_type": "authorization_code",
  "redirect_uri": "http://localhost:<port>/callback" | MANUAL_REDIRECT_URL,
  "client_id": "9d1c250a-e61b-44d9-88ed-5944d1962f5e",
  "code_verifier": "<PKCE_verifier>",
  "state": "<state>"
}
```

### Token Refresh

```http
POST https://platform.claude.com/v1/oauth/token
Content-Type: application/json

{
  "grant_type": "refresh_token",
  "refresh_token": "<token>",
  "client_id": "9d1c250a-e61b-44d9-88ed-5944d1962f5e",
  "scope": "user:profile user:inference user:sessions:claude_code user:mcp_servers"
}
```

Beta header for all Sessions API calls: `anthropic-beta: oauth-2025-04-20`

### Desktop App Auth

Desktop uses file descriptor auth instead of env vars:
```
CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR=<fd_number>
```
Token read from `/proc/self/fd/<N>` (inherited FD from parent Electron process).

---

## CLI Spawning

### Flags for Non-Interactive (Print) Mode

```bash
claude --print \
  --session-id <uuid> \
  --input-format stream-json \
  --output-format stream-json \
  --replay-user-messages \
  [--sdk-url <bridge_endpoint>] \
  [--verbose] \
  [--debug-file <path>] \
  [--permission-mode <mode>]
```

### Environment Variables Set by Bridge

```bash
CLAUDE_CODE_ENVIRONMENT_KIND=bridge        # identifies runtime context
CLAUDE_CODE_SESSION_ACCESS_TOKEN=<token>   # OAuth bearer for API
CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2=1  # enable remote persistence
CLAUDE_CODE_OAUTH_TOKEN=                   # explicitly cleared
CLAUDE_CODE_FORCE_SANDBOX=1               # if sandbox enabled
CLAUDE_CODE_USE_CCR_V2=1                  # if using CCR v2
CLAUDE_CODE_WORKER_EPOCH=<N>              # worker generation counter
```

### CoWork Tab Additional Vars

```bash
CLAUDE_CODE_IS_COWORK=1                   # eager flush at every turn
CLAUDE_CODE_USE_COWORK_PLUGINS=1          # cowork_plugins/ + cowork_settings.json
```

### All Relevant Environment Variables

| Variable | Purpose |
|----------|---------|
| `CLAUDE_CODE_ENTRYPOINT` | Client identity: sdk-cli, claude-vscode, local-agent, claude-desktop, remote |
| `CLAUDE_CODE_ENVIRONMENT_KIND` | Runtime context: bridge, byoc, anthropic_cloud |
| `CLAUDE_CODE_IS_COWORK` | Eager session flush at every turn boundary |
| `CLAUDE_CODE_USE_COWORK_PLUGINS` | Plugin dir → cowork_plugins/, settings → cowork_settings.json |
| `CLAUDE_CODE_SESSION_ACCESS_TOKEN` | OAuth token for Sessions API (refreshable via stdin) |
| `CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2` | Enable dual-write: local JSONL + remote Sessions API |
| `CLAUDE_CODE_USE_CCR_V2` | CCR v2 protocol |
| `CLAUDE_CODE_WORKER_EPOCH` | Worker generation counter for CCR v2 |
| `CLAUDE_CODE_FORCE_SANDBOX` | Force sandbox mode |
| `CLAUDE_CODE_EAGER_FLUSH` | Force eager session flush (same effect as IS_COWORK for flushing) |
| `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` | Override auto-memory directory (shared memory path) |
| `CLAUDE_CODE_REMOTE` | Remote mode flag |
| `CLAUDE_CODE_REMOTE_MEMORY_DIR` | Memory dir in remote mode |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Enable agent-teams feature |
| `CLAUDE_CODE_PLAN_MODE_REQUIRED` | Force plan-before-act for teammates |
| `CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR` | FD-based auth for Desktop app |
| `CLAUDE_AGENT_SDK_VERSION` | SDK version for User-Agent |
| `CLAUDE_AGENT_SDK_CLIENT_APP` | Client app name for User-Agent |
| `CLAUDE_CODE_CUSTOM_OAUTH_URL` | Override OAuth endpoints |
| `CLAUDE_CODE_OAUTH_CLIENT_ID` | Override OAuth client ID |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Disable auto-memory |
| `CLAUDE_CODE_SESSION_SOURCE` | Session source identifier |
| `CLAUDE_CODE_SIMPLE` | Disable skills, CLAUDE.md, file attachments |
| `CLAUDE_CODE_QUESTION_PREVIEW_FORMAT` | "markdown" or "html" |

---

## stdin Protocol

Each line is a JSON object terminated by `\n`. Parsed by `XoH.processLine()`.

### User Message

```json
{
  "type": "user",
  "message": { "content": "fix the auth bug in login.ts" },
  "parent_tool_use_id": null,
  "isSynthetic": false,
  "isReplay": false
}
```

### Keep-Alive

```json
{ "type": "keep_alive" }
```

### Environment Variable Update

```json
{
  "type": "update_environment_variables",
  "variables": {
    "CLAUDE_CODE_SESSION_ACCESS_TOKEN": "new-token-value"
  }
}
```

### Permission Response (Approve)

```json
{
  "type": "control_response",
  "response": {
    "request_id": "abc-123",
    "subtype": "success",
    "response": {
      "behavior": "allow",
      "updatedInput": {}
    }
  }
}
```

### Permission Response (Deny)

```json
{
  "type": "control_response",
  "response": {
    "request_id": "abc-123",
    "subtype": "success",
    "response": {
      "behavior": "deny"
    }
  }
}
```

### Permission Cancel

```json
{
  "type": "control_cancel_request",
  "request_id": "abc-123"
}
```

Note: `Nm$()` normalizes `requestId` → `request_id` for camelCase compat.

---

## stdout Protocol

Each line is a JSON object terminated by `\n`. Parsed by `fA_()`.

### Assistant Message

```json
{
  "type": "assistant",
  "message": {
    "content": [
      { "type": "text", "text": "I'll fix that..." },
      { "type": "tool_use", "id": "tu_123", "name": "Read",
        "input": { "file_path": "/src/login.ts" } }
    ]
  },
  "uuid": "msg-uuid",
  "session_id": "session-uuid"
}
```

### Permission Request

```json
{
  "type": "control_request",
  "request_id": "req-uuid",
  "request": {
    "subtype": "can_use_tool",
    "tool_name": "Bash",
    "tool_use_id": "tu_456",
    "input": { "command": "rm -rf /tmp/old" }
  }
}
```

### Result (Success)

```json
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 45230,
  "duration_api_ms": 38100,
  "num_turns": 7,
  "result": "Fixed the auth bug by...",
  "stop_reason": null,
  "session_id": "session-uuid",
  "total_cost_usd": 0.0342,
  "usage": {
    "input_tokens": 15420,
    "output_tokens": 3200,
    "cache_read_input_tokens": 8000,
    "cache_creation_input_tokens": 0
  },
  "modelUsage": {},
  "permission_denials": [],
  "fast_mode_state": {},
  "uuid": "result-uuid"
}
```

### Result Subtypes

| subtype | Meaning |
|---------|---------|
| `"success"` | Normal completion |
| `"error_max_turns"` | Hit max turns limit |
| `"error_max_budget_usd"` | Hit cost budget |
| `"error_during_execution"` | Runtime error |
| `"error_max_structured_output_retries"` | Structured output validation failed repeatedly |

---

## Session JSONL Format

### File Path

```
~/.claude/projects/<PI(projectRoot)>/<session-uuid>.jsonl
```

Where `PI()` hashes the absolute project path. Subagent sessions:
```
~/.claude/projects/<hash>/<parent-session-id>/subagents/agent-<agent-id>.jsonl
```

### Message Entry Shape

Each line is a JSON object. Messages pass the `RQ()` filter:
```js
RQ(H) = H.type === "user" || "assistant" || "attachment" || "system" || "progress"
```

```json
{
  "type": "user|assistant|system|progress|attachment",
  "uuid": "<crypto.randomUUID>",
  "timestamp": "2026-03-14T...",
  "message": { "role": "user|assistant", "content": "..." },

  "parentUuid": "<prev-msg-uuid> | null",
  "logicalParentUuid": "<uuid> | undefined",
  "isSidechain": false,
  "sessionId": "<session-uuid>",
  "version": "1",
  "cwd": "/path/to/project",
  "gitBranch": "main",
  "slug": "claude-sonnet-4-6",
  "userType": "external",

  "agentId": "<agent-uuid> | undefined",
  "agentName": "<name> | undefined",
  "teamName": "<team-name> | undefined",
  "promptId": "<prompt-uuid> | undefined",

  "isMeta": false,
  "toolUseResult": false,
  "isCompactSummary": false,
  "sourceToolAssistantUUID": "<uuid>"
}
```

System messages with `"subtype": "compact_boundary"` mark compaction points.

### Metadata Entries (Non-Message Lines)

```json
{"type":"custom-title","customTitle":"Fix auth bug","sessionId":"..."}
{"type":"ai-title","aiTitle":"Auth module refactor","sessionId":"..."}
{"type":"tag","tag":"bugfix","sessionId":"..."}
{"type":"summary","leafUuid":"...","summary":"..."}
{"type":"agent-name","agentName":"researcher","sessionId":"..."}
{"type":"agent-color","agentColor":"#ff6b6b","sessionId":"..."}
{"type":"agent-setting","agentSetting":"explorer","sessionId":"..."}
{"type":"mode","mode":"plan","sessionId":"..."}
{"type":"pr-link","prNumber":42,"prUrl":"...","prRepository":"...","sessionId":"...","timestamp":"..."}
{"type":"last-prompt","lastPrompt":"fix the auth bug","sessionId":"..."}
{"type":"file-history-snapshot","messageId":"...","snapshot":{}}
{"type":"queue-operation","operation":{}}
```

### Session File Writer

`dT(path, entry)` — synchronous append, mode 0600:
```js
fs.appendFileSync(path, JSON.stringify(entry) + "\n", { mode: 0o600 })
```

`Jq()` singleton manages batched writes (100ms flush interval), with eager flush
when `CLAUDE_CODE_IS_COWORK` or `CLAUDE_CODE_EAGER_FLUSH` is set.

---

## Sessions API

All calls require:
```http
Authorization: Bearer <accessToken>
anthropic-beta: ccr-byoc-2025-07-29
x-organization-uuid: <orgUUID>
```

### List Sessions

```http
GET https://api.anthropic.com/v1/sessions
```

Response: `{ data: [{ id, title, session_status, session_context, created_at, updated_at }] }`

### Get Session

```http
GET https://api.anthropic.com/v1/sessions/<session-id>
```

### Update Session Title

```http
PATCH https://api.anthropic.com/v1/sessions/<session-id>
Content-Type: application/json

{ "title": "New Title" }
```

### Post Events (Single Message)

```http
POST https://api.anthropic.com/v1/sessions/<session-id>/events
Content-Type: application/json

{
  "events": [{
    "uuid": "<uuid>",
    "session_id": "<session-id>",
    "type": "user",
    "parent_tool_use_id": null,
    "message": { "role": "user", "content": "message text" }
  }]
}
```

### Post Events (Batch)

Same endpoint, up to 100 events per batch (`kN$ = 100`).

### Fetch Teleport Events (Paginated)

```http
GET https://api.anthropic.com/v1/code/sessions/<session-id>/teleport-events
  ?limit=1000
  &cursor=<cursor>
```

### Legacy Ingress Fetch

```http
GET https://api.anthropic.com/v1/session_ingress/session/<session-id>
```

### Archive Session

```http
POST https://api.anthropic.com/v1/sessions/<session-id>/archive
```

---

## WebSocket Subscription

### Connection

```
wss://api.anthropic.com/v1/sessions/ws/<session-id>/subscribe
  ?organization_uuid=<orgUuid>

Headers:
  Authorization: Bearer <accessToken>
  anthropic-version: 2023-06-01
```

### Message Handling

Validator `fW6()` accepts any object with a string `type` field:
```js
function fW6(H) {
  if (typeof H !== "object" || H === null || !("type" in H)) return false;
  return typeof H.type === "string";
}
```

Events are forwarded to `callbacks.onMessage(parsedEvent)`.

Reconnection: up to `Abf` attempts with `AW6` ms delay.
Permanent close codes in `DW6` set prevent reconnection.
Ping interval: `LW6` ms.

### Control Messages (via WebSocket)

```json
{
  "type": "control_request",
  "request_id": "<uuid>",
  "request": {
    "subtype": "can_use_tool",
    "tool_name": "Bash",
    "tool_use_id": "...",
    "input": {}
  }
}
```

---

## CoWork-Specific Behavior

### Plugin Isolation

When `CLAUDE_CODE_USE_COWORK_PLUGINS=1` or `--cowork` flag:
- Plugin directory: `~/.claude/cowork_plugins/` (instead of `~/.claude/plugins/`)
- Settings file: `~/.claude/cowork_settings.json` (instead of `~/.claude/settings.json`)
- Function `ae6()` returns `"cowork_settings.json"` when `BkH()` or env var is truthy
- Function `L$_()` returns `"cowork_plugins"` instead of `"plugins"`

### Eager Flush

When `CLAUDE_CODE_IS_COWORK=1` or `CLAUDE_CODE_EAGER_FLUSH=1`:
- `RB()` (= `Jq().flush()`) called at every turn boundary
- `RB()` called at every result exit point (success, error_max_turns, etc.)
- Ensures remote Sessions API receives events in near-real-time

### Shared Memory (CoWork Teams)

`CLAUDE_COWORK_MEMORY_PATH_OVERRIDE=/path/to/shared/memory`
- Overrides the per-project memory directory
- All teammates in a CoWork session share the same MEMORY.md
- `mM$()` returns true when override is active
- `SHD()` reads the env var, `o3()` uses it as first priority

---

## Agent Teams

Agent Teams (teammate mode) is separate from CoWork. Enabled by:
```
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true  OR  --agent-teams flag
AND tengu_amber_flint feature flag = true
```

### Teammate Spawning (tmux mode)

The lead constructs a claude command:
```bash
cd /project && claude \
  --agent-id <uuid> \
  --agent-name <sanitized-name> \
  --team-name <team-name> \
  --agent-color <color> \
  --parent-session-id <lead-session-id> \
  [--plan-mode-required] \
  [--agent-type <type>]
```

### Teammate Modes

| Mode | Mechanism |
|------|-----------|
| `"tmux"` | Separate claude process in tmux pane |
| `"in-process"` | AsyncLocalStorage context in same Node process |
| `"auto"` | Chooses based on terminal (iTerm2 native panes → tmux → in-process) |

Configurable via settings `teammateMode` or `--teammate-mode <mode>`.

### Team State Storage

```
~/.claude/teams/<team-name>/config.json
~/.claude/tasks/<team-name>/
```

Config contains `members[]` with agentId, name, agentType, model, prompt, color,
planModeRequired, joinedAt, tmuxPaneId, cwd, subscriptions, backendType.

### SendMessage Tool Schema

Types: `message`, `broadcast`, `shutdown_request`, `shutdown_response`, `plan_approval_response`

```json
{"type":"message","recipient":"researcher","content":"...","summary":"Brief preview"}
{"type":"broadcast","content":"...","summary":"Critical announcement"}
{"type":"shutdown_request","recipient":"researcher","content":"Task complete"}
{"type":"shutdown_response","request_id":"abc","approve":true}
{"type":"plan_approval_response","request_id":"abc","recipient":"researcher","approve":true}
```

### Teammate System Prompt Addendum

```
# Agent Teammate Communication

IMPORTANT: You are running as an agent in a team. To communicate with anyone on your team:
- Use the SendMessage tool with type `message` to send messages to specific teammates
- Use the SendMessage tool with type `broadcast` sparingly for team-wide announcements

Just writing a response in text is not visible to others on your team
- you MUST use the SendMessage tool.

The user interacts primarily with the team lead. Your work is coordinated
through the task system and teammate messaging.
```

---

## Session Resume Paths

### Local Resume

| Flag | Mechanism |
|------|-----------|
| `--continue` | Loads most recent session via `FbA(0)` |
| `--resume <uuid>` | Loads `<uuid>.jsonl` via `eQH(sessionId)` |
| `--resume <search>` | Fuzzy matches title via `UB(query, {exact:true})` |
| `--fork-session` | Creates new session ID, copies messages |
| `--resume-session-at <msg-id>` | Truncates at message UUID |
| `--rewind-files <msg-id>` | Restores files to snapshot, exits |
| `--from-pr [number]` | Sessions linked to PR |

### Remote Resume

| Flag | Mechanism |
|------|-----------|
| `--teleport <id>` | `GET /v1/code/sessions/<id>/teleport-events` (paginated, 1000/page) |
| (fallback) | `GET /v1/session_ingress/session/<id>` |

### Session Loader Flow (ae())

1. Read JSONL → parse via `HqH()` → maps of messages, summaries, titles, tags, snapshots
2. Find leaf UUID (most recent non-sidechain message)
3. Walk `parentUuid` chain via `GrH()` to reconstruct conversation tree
4. Slice at `compact_boundary` via `Ly()` if present
5. Restore fileHistorySnapshots, attributionSnapshots, contentReplacements
6. Run `SessionStart:resume` hooks
7. Return `{messages, turnInterruptionState, agentSetting, ...}` to React app

### Hydration (Remote → Local)

`ZnA(sessionId, ingressUrl)`:
1. Fetch events from remote ingress URL
2. Write to local `<uuid>.jsonl`
3. Set remote ingress URL on session writer for future dual-write

---

## sdkUrl & Session Ingress Transport

**Gap 1 RESOLVED**: `--sdk-url` is NOT an HTTP endpoint. It is a **WebSocket URL** for
session ingress. The CLI opens a persistent WebSocket to it and pipes stream-json
bidirectionally.

### How sdkUrl Works

When `--sdk-url <url>` is passed, the CLI creates a `Yp$` transport (class extending `goH`):

```
┌────────────────────────────┐
│  Bridge Daemon (T38)       │
│  polls /work/poll          │
│  gets work_secret with     │
│  session_ingress_token     │
└─────────┬──────────────────┘
          │ spawns:
          │ claude --print --sdk-url <ws_url> --session-id <id> ...
          ▼
┌────────────────────────────┐          ┌──────────────────────────┐
│  CLI child process         │          │  Anthropic API           │
│  Yp$ class                 │◄──WS───►│  session_ingress/ws/<id> │
│  ├─ WebSocket transport    │          └──────────────────────────┘
│  │  (doH / FoH / mqH)     │
│  ├─ stdin ← WS messages   │
│  ├─ stdout → WS write()   │
│  └─ keep_alive interval   │
└────────────────────────────┘
```

### Transport Selection (`d08()`)

```
d08(url, headers, sessionId, refreshHeaders):
  if CLAUDE_CODE_USE_CCR_V2:
    → convert ws→http, append /worker/events/stream
    → return SSETransport (mqH)
  else if ws:// or wss://:
    if CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2:
      → return HybridTransport (FoH) — WebSocket + POST fallback
    else:
      → return WebSocketTransport (doH)
  else:
    → Error: unsupported protocol
```

### Session Ingress WebSocket URL

Built by `Wm$()`:
```
wss://{api_host}/v1/session_ingress/ws/{sessionId}
```
For localhost: `ws://` and `/v2/` path prefix.

### HybridTransport POST Fallback

`FoH` extends `doH` (WebSocketTransport), adding:
- Batched POST uploads to `{url}/session/{sessionId}/events` (URL transform via `L1_()`)
- Auth: `Authorization: Bearer {MJ()}` — uses `MJ()` (see session token section)
- Content-Type: `application/json`
- Body: `{ events: [...messages] }`
- Batch size: 500, queue size: 100k, retry with exponential backoff

### CCR v2 Path

When `CLAUDE_CODE_USE_CCR_V2=1`:
- Worker registration: `POST {api}/v1/code/sessions/{id}/worker/register`
- Stream: SSE at `{api}/v1/code/sessions/{id}/worker/events/stream`
- Internal events read/write via `QoH` (CCRClient)
- State reporting: permission_mode, tool activity, metadata

### Key Implication for Local Client

**sdkUrl is optional for local implementations.** When omitted, the CLI uses `goH` (local
stdin/stdout passthrough). The `Yp$` class is only needed when the CLI must talk to a
remote bridge over WebSocket. A local CoWork client can:
1. Spawn CLI with piped stdin/stdout (no `--sdk-url`)
2. Separately dual-write events via `POST /v1/sessions/{id}/events`
3. Subscribe to remote updates via WebSocket subscription

---

## Session Creation API

**Gap 2 RESOLVED**: Full `POST /v1/sessions` schema extracted.

### Create Session (Web/CLI Path)

```http
POST https://api.anthropic.com/v1/sessions
Authorization: Bearer <accessToken>
Content-Type: application/json
anthropic-version: 2023-06-01
anthropic-beta: ccr-byoc-2025-07-29
x-organization-uuid: <orgUUID>
```

Request Body:
```json
{
  "title": "Fix auth bug in login.ts",
  "events": [
    {
      "type": "event",
      "data": {
        "uuid": "<crypto.randomUUID()>",
        "session_id": "",
        "type": "user",
        "parent_tool_use_id": null,
        "message": {
          "role": "user",
          "content": "fix the auth bug in login.ts"
        }
      }
    }
  ],
  "session_context": {
    "sources": [
      {
        "type": "git_repository",
        "git_info": {
          "type": "github",
          "repo": "owner/repo"
        }
      }
    ],
    "outcomes": [
      {
        "type": "git_repository",
        "git_info": {
          "type": "github",
          "repo": "owner/repo",
          "branches": ["claude/task"]
        }
      }
    ],
    "model": "claude-sonnet-4-6"
  },
  "environment_id": "<environment-uuid>"
}
```

Response:
```json
{
  "id": "cse_abc123...",
  "title": "Fix auth bug in login.ts"
}
```

### Create Session (Bridge/Remote Control Path)

Same endpoint, but additional fields:

```json
{
  "title": "optional",
  "events": [],
  "session_context": {
    "sources": [{"type": "git_repository", "git_info": {...}}],
    "outcomes": [{"type": "git_repository", "git_info": {...}}],
    "model": "claude-sonnet-4-6"
  },
  "environment_id": "<environment-uuid>",
  "source": "remote-control",
  "permission_mode": "plan"
}
```

### Fetch Session Details

```http
GET https://api.anthropic.com/v1/sessions/<session-id>
```

Response includes `session_context.sources[]` with:
- `type: "git_repository"` — `url`, `git_info.type`, `git_info.repo`
- `type: "directory"` — path info

### List Code Sessions (with context)

```http
GET https://api.anthropic.com/v1/sessions
```

Response: `{ data: [{ id, title, session_status, session_context, created_at, updated_at }] }`

### Share Transcript

```http
POST https://api.anthropic.com/api/claude_code_shared_session_transcripts
Content-Type: application/json
User-Agent: claude-code/2.1.75

{
  "content": "<transcript>",
  "appearance_id": "<id>"
}
```

Response: `{ transcript_id: "..." }`

---

## WebSocket Event Types

**Gap 3 RESOLVED**: The WebSocket carries the **same stream-json protocol** as stdin/stdout.
All message types listed below are valid over both WebSocket and piped stdio.

### Full Message Type Taxonomy

Messages pass through `Lf_()` filter (passes everything except control_request/control_response)
and `QZH()` adapter:

| Type | Subtypes | Direction | Purpose |
|------|----------|-----------|---------|
| `user` | — | client→server | User message |
| `assistant` | — | server→client | Model response (text, tool_use) |
| `system` | `init`, `status`, `compact_boundary`, `informational` | server→client | System events |
| `result` | `success`, `error_max_turns`, `error_max_budget_usd`, `error_during_execution` | server→client | Turn completion |
| `tool_progress` | — | server→client | Long-running tool status |
| `stream_event` | — | server→client | Streaming delta (text, tool input) |
| `auth_status` | — | server→client | Auth state changes |
| `tool_use_summary` | — | server→client | Tool use digest |
| `rate_limit_event` | — | server→client | Rate limiting info |
| `control_request` | `can_use_tool`, `interrupt`, `hook_callback`, `elicitation`, `mcp_message`, `set_permission_mode` | bidirectional | Permission/control flow |
| `control_response` | `success`, `error` | bidirectional | Response to control_request |
| `control_cancel_request` | — | client→server | Cancel pending request |
| `keep_alive` | — | bidirectional | Connection heartbeat |
| `streamlined_text` | — | server→client | Streamlined text output |
| `streamlined_tool_use_summary` | — | server→client | Streamlined tool digest |
| `update_environment_variables` | — | client→server | Token refresh |

### system.init Event

Sent when session starts:
```json
{
  "type": "system",
  "subtype": "init",
  "slash_commands": ["commit", "compact", "help", ...],
  "timestamp": "..."
}
```

### stream_event Event

Real-time streaming deltas:
```json
{
  "type": "stream_event",
  "event": {
    "type": "content_block_delta",
    "delta": {"type": "text_delta", "text": "partial..."}
  }
}
```

### control_request Subtypes (Full)

| Subtype | Purpose | Fields |
|---------|---------|--------|
| `can_use_tool` | Permission check | `tool_name`, `input`, `tool_use_id`, `permission_suggestions`, `blocked_path`, `decision_reason`, `description`, `agent_id` |
| `interrupt` | Abort current operation | — |
| `hook_callback` | Execute hook | `callback_id`, `input`, `tool_use_id` |
| `elicitation` | MCP elicitation | `mcp_server_name`, `message`, `mode`, `url`, `elicitation_id`, `requested_schema` |
| `mcp_message` | MCP passthrough | `server_name`, `message` |
| `set_permission_mode` | Change permission level | `mode` |

---

## Session Token Architecture

**Gap 4 RESOLVED**: Complete token chain traced.

### Token Hierarchy

```
OAuth accessToken (long-lived, from PKCE flow)
  ├─ Used for: Sessions API CRUD, session listing, teleport, archive
  ├─ Stored: ~/.claude/.credentials.json
  └─ Header: Authorization: Bearer <accessToken>

session_ingress_token (session-scoped, from work secret)
  ├─ Used for: WebSocket ingress, event POST to session, bridge heartbeats
  ├─ Source: pollForWork response → work_secret (base64url JSON)
  └─ Header: Authorization: Bearer <session_ingress_token>
```

### MJ() — Session Token Getter

Priority chain:
1. `process.env.CLAUDE_CODE_SESSION_ACCESS_TOKEN` — highest priority
2. `CI1()` — reads from file descriptor via `CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR`
   - Reads `/proc/self/fd/<N>` (inherited from Desktop Electron parent)
   - Cached after first read

### fIH() — Auth Headers Builder

```js
// For sessionKey tokens (sk-ant-sid*)
{ Cookie: "sessionKey=<token>", "X-Organization-Uuid": "<orgUuid>" }

// For bearer tokens (everything else)
{ Authorization: "Bearer <token>" }
```

### Rw() — OAuth Headers Builder

Used for all Sessions API calls:
```js
{
  Authorization: "Bearer <accessToken>",
  "Content-Type": "application/json",
  "anthropic-version": "2023-06-01"
}
```

Plus per-request additions:
```
anthropic-beta: ccr-byoc-2025-07-29
x-organization-uuid: <orgUUID>
```

### Work Secret Structure

The `pollForWork` response includes a `secret` field. Decoded by `Em$()`:

```json
{
  "version": 1,
  "session_ingress_token": "string (required)",
  "api_base_url": "string (required)",
  "use_code_sessions": true
}
```

The `session_ingress_token` is:
- Passed to child process via `CLAUDE_CODE_SESSION_ACCESS_TOKEN` env var
- Used as `accessToken` parameter in bridge session spawn
- Refreshable via token rotation during long sessions
- Bridge updates running sessions via `updateAccessToken()` when new work arrives

### Token Refresh for Running Sessions

The bridge daemon can receive updated tokens for existing sessions:
```js
// In poll loop, when session already exists:
if (existingSession) {
  existingSession.updateAccessToken(workSecret.session_ingress_token);
  // Also schedules token rotation
}
```

---

## Bridge Orchestrator

**Gap 5 RESOLVED**: Full bridge lifecycle traced.

### Entry Point

The bridge is started via `claude remote-control` or `/remote-control` command, which
calls `T38()` — the main bridge poll loop.

### Bridge API Client

Created by `zm$()`, provides these endpoints:

```
┌─────────────────────────────────────────────────────────────────┐
│  Bridge API Surface                                             │
│                                                                 │
│  POST /v1/environments/bridge                                   │
│    → registerBridgeEnvironment(machineName, dir, branch,        │
│       gitRepoUrl, maxSessions, workerType, reuseEnvironmentId)  │
│    ← { environment_id: string }                                 │
│                                                                 │
│  GET  /v1/environments/{envId}/work/poll?ack=true               │
│    → pollForWork(environmentId, accessToken, abortSignal)       │
│    ← { id: workId, data: { type: "session"|"healthcheck",      │
│         id: sessionId }, secret: base64url_work_secret }        │
│    ← null (no work available)                                   │
│                                                                 │
│  POST /v1/environments/{envId}/work/{workId}/ack                │
│    → acknowledgeWork(environmentId, workId, accessToken)        │
│                                                                 │
│  POST /v1/environments/{envId}/work/{workId}/stop               │
│    → stopWork(environmentId, workId, force)                     │
│                                                                 │
│  POST /v1/environments/{envId}/work/{workId}/heartbeat          │
│    → heartbeatWork(environmentId, workId, accessToken)          │
│    ← { lease_extended: bool, state: string }                    │
│                                                                 │
│  POST /v1/environments/{envId}/bridge/reconnect                 │
│    → reconnectSession(environmentId, sessionId)                 │
│                                                                 │
│  DELETE /v1/environments/bridge/{envId}                         │
│    → deregisterEnvironment(environmentId)                       │
│                                                                 │
│  POST /v1/sessions/{id}/archive                                 │
│    → archiveSession(sessionId)                                  │
│                                                                 │
│  POST /v1/sessions/{id}/events                                  │
│    → sendPermissionResponseEvent(sessionId, event, token)       │
│                                                                 │
│  Beta header: anthropic-beta: environments-2025-11-01           │
└─────────────────────────────────────────────────────────────────┘
```

### Bridge Lifecycle (T38)

```
1. REGISTER
   POST /v1/environments/bridge
   Body: { machine_name, directory, branch, git_repo_url,
           max_sessions, metadata: { worker_type } }
   ← environment_id

2. POLL LOOP (infinite)
   GET /v1/environments/{envId}/work/poll?ack=true
   ← null → sleep(poll_interval), retry
   ← { data.type: "healthcheck" } → log, continue
   ← { data.type: "session", data.id: sessionId, secret: ... } → SPAWN

3. SPAWN SESSION
   a. Decode work secret: Em$(secret) → { session_ingress_token, api_base_url, ... }
   b. Build ingress URL: Wm$(api_base_url, sessionId)
      → wss://{host}/v1/session_ingress/ws/{sessionId}
   c. (Optional CCR v2) Register worker:
      POST {api}/v1/code/sessions/{id}/worker/register
   d. Spawn child:
      claude --print --sdk-url <ws_url> --session-id <id>
            --input-format stream-json --output-format stream-json
            --replay-user-messages [--verbose] [--debug-file <path>]
            [--permission-mode <mode>]
      Env: CLAUDE_CODE_SESSION_ACCESS_TOKEN=<ingress_token>
           CLAUDE_CODE_ENVIRONMENT_KIND=bridge
           CLAUDE_CODE_WORKER_EPOCH=<N>
           [CLAUDE_CODE_USE_CCR_V2=1]

4. SESSION MONITORING
   - Track active sessions in Map<sessionId, childProcess>
   - Heartbeat: POST /v1/environments/{envId}/work/{workId}/heartbeat
   - Timeout: configurable per session (sessionTimeoutMs)
   - Token rotation: update child tokens when new work arrives for same session

5. SESSION COMPLETE
   - Archive: POST /v1/sessions/{id}/archive
   - Worktree cleanup (if spawn mode = worktree)
   - Acknowledge work completion
   - Return to poll loop

6. DEREGISTER (on shutdown)
   DELETE /v1/environments/bridge/{envId}
```

### Spawn Modes

| Mode | Mechanism |
|------|-----------|
| `same-dir` | Child process in same directory |
| `worktree` | git worktree created per session |
| `session` | Isolated session directory |
| `single-session` | One session at a time, exit after completion |

### Capacity Management

- `maxSessions` configurable (passed during registration)
- At capacity: enters heartbeat mode (heartbeat_interval_ms)
- Multisession polling: `multisession_poll_interval_ms_at_capacity`
- Session count tracked and reported via status display

### Error Handling

`YE` (BridgeFatalError) class with status codes:
- 401: Authentication failed
- 403: Access denied / session expired
- 404: Not found (Remote Control may not be available)
- 410: Session expired
- 429: Rate limited (polling too frequently)

---

## Remaining Unknowns

The 5 original gaps are now resolved. Remaining minor unknowns:

1. **Exact event schemas for all stream_event subtypes** — the content_block_delta
   structure follows the Anthropic Messages API spec, but edge cases may exist.

2. **session_context full taxonomy** — `sources[]` and `outcomes[]` types beyond
   `git_repository` and `directory` are not fully enumerated.

3. **CCR v2 worker event stream format** — the SSE transport (`mqH`) uses a different
   wire format than the WebSocket path. Not fully traced.

4. **Bridge poll interval config** — `o$H()` returns configurable intervals
   (`poll_interval_ms_not_at_capacity`, `heartbeat_interval_ms`,
   `multisession_poll_interval_ms_at_capacity`, `session_keepalive_interval_ms`)
   but the defaults and server-side config source are unknown.

5. **Token rotation scheduling** — `Y38()` schedules periodic token refresh for
   bridge sessions but the exact interval logic is not fully traced.

These are implementation details, not blocking for a Linux CoWork client.

---

## Building a Linux CoWork Client

### Architecture Decision

Two viable approaches based on findings:

**Approach A: Local Pipe (Simplest)**
- Spawn CLI with piped stdin/stdout, no `--sdk-url`
- Dual-write events via `POST /v1/sessions/{id}/events`
- Subscribe via WebSocket for remote sync

**Approach B: Full Bridge (Production)**
- Register environment via bridge API
- Poll for work, get session_ingress_token
- Spawn CLI with `--sdk-url` pointing to session ingress WebSocket
- Full lifecycle management like claude.ai

### Implementation (Approach A)

```python
import subprocess, json, uuid, threading, time, webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlencode, parse_qs, urlparse
import hashlib, base64, secrets, requests

# ── 1. OAuth PKCE Login ──
CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
TOKEN_URL = "https://platform.claude.com/v1/oauth/token"
AUTHORIZE_URL = "https://claude.ai/oauth/authorize"
SCOPES = "user:profile user:inference user:sessions:claude_code user:mcp_servers"
BASE_API = "https://api.anthropic.com"
BETA_HEADER = "ccr-byoc-2025-07-29"

def pkce_pair():
    verifier = secrets.token_urlsafe(64)
    digest = hashlib.sha256(verifier.encode()).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    return verifier, challenge

def oauth_login():
    verifier, challenge = pkce_pair()
    state = secrets.token_urlsafe(32)
    port = 9876
    auth_code = [None]

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            qs = parse_qs(urlparse(self.path).query)
            if "code" in qs:
                auth_code[0] = qs["code"][0]
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Login successful. Return to terminal.")
            self.server.shutdown_request(self.request)
        def log_message(self, *a): pass

    server = HTTPServer(("127.0.0.1", port), Handler)
    redirect_uri = f"http://localhost:{port}/callback"
    url = f"{AUTHORIZE_URL}?" + urlencode({
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    })
    webbrowser.open(url)
    server.handle_request()

    resp = requests.post(TOKEN_URL, json={
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": redirect_uri,
        "code_verifier": verifier,
        "code": auth_code[0],
    })
    tokens = resp.json()
    return tokens["access_token"], tokens.get("refresh_token")

# ── 2. Session Management ──
def api_headers(token, org_uuid):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "anthropic-beta": BETA_HEADER,
        "x-organization-uuid": org_uuid,
    }

def create_session(token, org_uuid, title, initial_prompt=None, env_id=None):
    events = []
    if initial_prompt:
        events.append({
            "type": "event",
            "data": {
                "uuid": str(uuid.uuid4()),
                "session_id": "",
                "type": "user",
                "parent_tool_use_id": None,
                "message": {"role": "user", "content": initial_prompt}
            }
        })
    body = {
        "title": title,
        "events": events,
        "session_context": {"sources": [], "outcomes": [], "model": "claude-sonnet-4-6"},
    }
    if env_id:
        body["environment_id"] = env_id
    resp = requests.post(f"{BASE_API}/v1/sessions",
                         json=body, headers=api_headers(token, org_uuid))
    resp.raise_for_status()
    return resp.json()["id"]

def send_event(token, org_uuid, session_id, content, msg_uuid=None):
    body = {"events": [{
        "uuid": msg_uuid or str(uuid.uuid4()),
        "session_id": session_id,
        "type": "user",
        "parent_tool_use_id": None,
        "message": {"role": "user", "content": content}
    }]}
    resp = requests.post(f"{BASE_API}/v1/sessions/{session_id}/events",
                         json=body, headers=api_headers(token, org_uuid))
    return resp.status_code in (200, 201)

# ── 3. Spawn CLI ──
def spawn_cli(session_id, access_token):
    import os
    env = {
        **os.environ,
        "CLAUDE_CODE_SESSION_ACCESS_TOKEN": access_token,
        "CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2": "1",
        "CLAUDE_CODE_IS_COWORK": "1",
        "CLAUDE_CODE_USE_COWORK_PLUGINS": "1",
        "CLAUDE_CODE_ENVIRONMENT_KIND": "bridge",
        "CLAUDE_CODE_ENTRYPOINT": "claude-desktop",
    }
    return subprocess.Popen(
        ["claude", "--print",
         "--session-id", session_id,
         "--input-format", "stream-json",
         "--output-format", "stream-json",
         "--replay-user-messages"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )

# ── 4. Stream Protocol ──
def send_message(proc, content):
    msg = json.dumps({
        "type": "user",
        "message": {"content": content},
        "parent_tool_use_id": None,
    }) + "\n"
    proc.stdin.write(msg.encode())
    proc.stdin.flush()

def send_control_response(proc, request_id, behavior="allow", updated_input=None):
    resp = {
        "type": "control_response",
        "response": {
            "request_id": request_id,
            "subtype": "success",
            "response": {"behavior": behavior}
        }
    }
    if behavior == "allow" and updated_input:
        resp["response"]["response"]["updatedInput"] = updated_input
    proc.stdin.write((json.dumps(resp) + "\n").encode())
    proc.stdin.flush()

def refresh_token(proc, new_token):
    msg = json.dumps({
        "type": "update_environment_variables",
        "variables": {"CLAUDE_CODE_SESSION_ACCESS_TOKEN": new_token}
    }) + "\n"
    proc.stdin.write(msg.encode())
    proc.stdin.flush()

def read_events(proc, on_assistant, on_permission, on_result):
    for line in proc.stdout:
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = event.get("type")
        if t == "assistant":
            on_assistant(event)
        elif t == "control_request":
            on_permission(event)
        elif t == "result":
            on_result(event)
            if event.get("subtype") == "success":
                break
        elif t == "system" and event.get("subtype") == "init":
            pass  # Session initialized
        elif t == "keep_alive":
            pass  # Ignore heartbeats

# ── 5. Resume Session ──
# Option A: Local resume
#   claude --resume <session-uuid>
#
# Option B: Remote teleport
#   GET /v1/code/sessions/<id>/teleport-events?limit=1000&cursor=<cursor>
#
# Option C: WebSocket subscription for live sync
#   wss://api.anthropic.com/v1/sessions/ws/<id>/subscribe
#     ?organization_uuid=<orgUuid>
#   Headers: Authorization: Bearer <accessToken>
#            anthropic-version: 2023-06-01
```
