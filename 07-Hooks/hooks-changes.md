---
title: "Hook System Changes: 2.1.59 → 2.1.70"
category: "07-Hooks"
tags: ["hooks", "security"]
---

# Hook System Changes: 2.1.59 → 2.1.70

## Overview of Changes

| Category | 2.1.59 | 2.1.70 | Delta |
|----------|--------|--------|-------|
| Hook event types | 18 | 21 | **+3** |
| Command hook fields | `command, timeout, statusMessage, once, async` | + `asyncRewake` | +1 |
| HTTP hook security | URL+header+env filtering | + DNS SSRF blocking + policy allowlists + sandbox proxy | Major hardening |
| HTTP hook policy controls | none | `allowedHttpHookUrls`, `httpHookAllowedEnvVars` | +2 |
| SessionEnd reasons | 4 | 5 | +1 |

No hook events were removed.

---

## 1. New Hook Events

```
   Hook Event Registry: 2.1.59 → 2.1.70
   ┌───────────────────────────────────────────────────────────────────────┐
   │  EXISTING (18)                                                        │
   │  PreToolUse  PostToolUse  PostToolUseFailure  PermissionRequest       │
   │  SessionStart  SessionEnd  Stop                                       │
   │  SubagentStart  SubagentStop  TeammateIdle  TaskCompleted             │
   │  Setup  PreCompact  UserPromptSubmit                                  │
   │  ConfigChange  Notification  WorktreeCreate  WorktreeRemove           │
   ├───────────────────────────────────────────────────────────────────────┤
   │  NEW (3) ← 2.1.70                                                     │
   │  ┌─────────────────┐  ┌───────────────────┐  ┌────────────────────┐  │
   │  │  Elicitation    │  │ ElicitationResult  │  │ InstructionsLoaded │  │
   │  └─────────────────┘  └───────────────────┘  └────────────────────┘  │
   └───────────────────────────────────────────────────────────────────────┘
```

---

### 1a. `Elicitation` — MCP Server Input Request Interception

Fires when an MCP server sends an elicitation request (asking the user to fill a form
or visit a URL). The hook fires **before** the dialog is shown to the user.

```
   Elicitation Flow (2.1.70)
   ┌──────────────┐   elicitation   ┌──────────────────┐
   │  MCP Server  │────────────────►│  Claude Code CLI │
   └──────────────┘                 └────────┬─────────┘
                                             │ fire BEFORE showing dialog
                                             ▼
                                    ┌─────────────────────────────────────┐
                                    │        Elicitation Hook             │
                                    │  receives:                          │
                                    │   hook_event_name: "Elicitation"    │
                                    │   mcp_server_name: "my-mcp"         │
                                    │   message: "Please provide..."      │
                                    │   mode: "form" | "url"              │
                                    │   url: "https://..." (url mode)     │
                                    │   elicitation_id: "<uuid>"          │
                                    │   requested_schema: { field: ... }  │
                                    └──────────────┬──────────────────────┘
                                                   │
                    ┌──────────────────────────────┼──────────────────────┐
                    │                              │                      │
                    ▼                              ▼                      ▼
           hook returns nothing          action: "accept"        action: "decline"
                    │                    content: { ... }               │
                    │                              │                      │
                    ▼                              ▼                      ▼
           show dialog to user         auto-fill & submit         block dialog
                                       (no user interaction)     "Elicitation
                                                                  denied by hook"
```

**Input schema:**
```json
{
  "hook_event_name": "Elicitation",
  "session_id": "...",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "...",
  "mcp_server_name": "my-server",
  "message": "Please enter your API key",
  "mode": "form",
  "elicitation_id": "<uuid>",
  "requested_schema": { "api_key": { "type": "string" } }
}
```

**hookSpecificOutput:**
```json
{
  "hookEventName": "Elicitation",
  "action": "accept" | "decline" | "cancel",
  "content": { "field_name": "value" }
}
```

**Outcome semantics:**
| Hook returns | Effect |
|---|---|
| Nothing / no hookSpecificOutput | Dialog shown to user normally |
| `action: "accept"` + `content` | Auto-submits with provided content; dialog skipped |
| `action: "decline"` | Sends decline to MCP server; blocking error: `"Elicitation denied by hook"` |
| `action: "cancel"` | Sends cancel to MCP server |
| Hook exits 2 (blocking) | `"Elicitation blocked by hook"` |

---

### 1b. `ElicitationResult` — MCP Server Input Response Interception

Fires **after** the user responds to an elicitation dialog (or a hook auto-responded),
but **before** the result is sent back to the MCP server. Allows a hook to override
or filter the user's response.

```
   ElicitationResult Flow (2.1.70)
   ┌──────────┐         ┌──────────────────┐
   │   User   │─ fills ►│  Elicitation UI   │
   └──────────┘         └────────┬─────────┘
                                  │ user submits (accept/decline/cancel)
                                  ▼
                         ┌────────────────────────────────────────────┐
                         │         ElicitationResult Hook             │
                         │  receives:                                 │
                         │   hook_event_name: "ElicitationResult"     │
                         │   mcp_server_name: "my-mcp"                │
                         │   elicitation_id: "<uuid>"                 │
                         │   mode: "form" | "url"                     │
                         │   action: "accept" | "decline" | "cancel"  │
                         │   content: { field: value, ... }           │
                         └─────────────────┬──────────────────────────┘
                                           │
                   ┌───────────────────────┼─────────────────────────┐
                   │                       │                         │
                   ▼                       ▼                         ▼
          hook returns nothing    override action/content    action: "decline"
                   │                       │                         │
                   ▼                       ▼                         ▼
          original result sent    modified result sent       "Elicitation result
          to MCP server           to MCP server               blocked by hook"
```

**Input schema:**
```json
{
  "hook_event_name": "ElicitationResult",
  "mcp_server_name": "my-server",
  "elicitation_id": "<uuid>",
  "mode": "form",
  "action": "accept",
  "content": { "api_key": "user-entered-value" }
}
```

**hookSpecificOutput:** same shape as `Elicitation` — `action` + `content`.

---

### 1c. `InstructionsLoaded` — Memory/CLAUDE.md File Load Observer

Fires each time Claude Code loads a CLAUDE.md or memory file. This is a
**purely observational** event — no hookSpecificOutput is supported. Used for
auditing, logging, or reacting to which instructions are active.

```
   InstructionsLoaded Trigger Points (2.1.70)
   ┌────────────────────────────────────────────────────────────────────┐
   │  load_reason: "session_start"                                      │
   │    └─► fires for each memory file loaded at startup                │
   │                                                                    │
   │  load_reason: "nested_traversal"                                   │
   │    └─► CLAUDE.md discovered while traversing directories           │
   │                                                                    │
   │  load_reason: "path_glob_match"                                    │
   │    └─► file matched a glob pattern in a parent CLAUDE.md           │
   │                                                                    │
   │  load_reason: "include"                                            │
   │    └─► explicit @include directive in a CLAUDE.md                  │
   └────────────────────────────────────────────────────────────────────┘

   memory_type values:
   ┌──────────┬────────────────────────────────────────────────────────┐
   │  "User"  │ ~/.claude/CLAUDE.md (global user instructions)         │
   │ "Project"│ .claude/CLAUDE.md or project root CLAUDE.md            │
   │  "Local" │ .claude/CLAUDE.local.md (gitignored local overrides)   │
   │"Managed" │ Enterprise-managed instructions from policy settings   │
   └──────────┴────────────────────────────────────────────────────────┘
```

**Input schema:**
```json
{
  "hook_event_name": "InstructionsLoaded",
  "session_id": "...",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "...",
  "file_path": "/home/user/.claude/CLAUDE.md",
  "memory_type": "User",
  "load_reason": "session_start",
  "globs": ["*.py", "src/**"],
  "trigger_file_path": "/project/CLAUDE.md",
  "parent_file_path": "/project/CLAUDE.md"
}
```

`globs`, `trigger_file_path`, `parent_file_path` are optional (present for nested/include loads).

---

## 2. HTTP Hook — Major Security Hardening

2.1.59 had a basic HTTP hook type. 2.1.70 adds a multi-layer security architecture around it.

```
   HTTP Hook Security Layers (2.1.70)
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                     HTTP Hook Execution Pipeline                        │
   │                                                                         │
   │  Hook Config:                                                           │
   │  { type: "http", url: "...", headers: {...}, timeout: N,                │
   │    allowedEnvVars: [...] }                                              │
   │                          │                                              │
   │                          ▼                                              │
   │  ┌────────────────  LAYER 1: URL Allowlist ─────────────────────────┐   │
   │  │  policy: allowedHttpHookUrls (enterprise setting)                │   │
   │  │                                                                  │   │
   │  │  if allowedHttpHookUrls is set:                                  │   │
   │  │    hook.url must match at least one pattern                      │   │
   │  │    patterns support * wildcard                                   │   │
   │  │    e.g.: "https://hooks.example.com/*"                           │   │
   │  │                                                                  │   │
   │  │  BLOCKED ──────────────────────────────────────► log + return    │   │
   │  │  ALLOWED ──────────────────────────────────────► Layer 2         │   │
   │  └──────────────────────────────────────────────────────────────────┘   │
   │                          │                                              │
   │                          ▼                                              │
   │  ┌──────────────── LAYER 2: Header Env Var Gating  ─────────────────┐   │
   │  │  hook.allowedEnvVars ∩ policy.httpHookAllowedEnvVars             │   │
   │  │                                                                  │   │
   │  │  Double-gate: a var must appear in BOTH lists to be injected     │   │
   │  │  Prevents leaking $AWS_SECRET_KEY even if hook asks for it       │   │
   │  │                                                                  │   │
   │  │  Header value syntax: "Bearer $MY_TOKEN" or "${MY_TOKEN}"        │   │
   │  │  Unallowed vars → replaced with "" + warning log                 │   │
   │  │  CRLF/null stripped from interpolated values (injection guard)   │   │
   │  └──────────────────────────────────────────────────────────────────┘   │
   │                          │                                              │
   │                          ▼                                              │
   │  ┌──────────────── LAYER 3: Network Path Decision ─────────────────┐    │
   │  │                                                                 │    │
   │  │  SandboxManager enabled?                                        │    │
   │  │    YES ─► route via sandbox proxy (host: 127.0.0.1, port: P)    │    │
   │  │           skip DNS check (sandbox controls network)             │    │
   │  │           log: "via sandbox proxy :P"                           │    │
   │  │                                                                 │    │
   │  │  Env-var proxy (HTTP_PROXY etc.) configured?                    │    │
   │  │    YES ─► route via proxy, skip DNS check                       │    │
   │  │           log: "via env-var proxy"                              │    │
   │  │                                                                 │    │
   │  │  Neither ──────────────────────────────────────► Layer 4        │    │
   │  └─────────────────────────────────────────────────────────────────┘    │
   │                          │                                              │
   │                          ▼                                              │
   │  ┌──────────────── LAYER 4: DNS + SSRF Protection ─────────────────┐    │
   │  │  (only for direct connections, no proxy)                        │    │
   │  │                                                                 │    │
   │  │  Hostname IP?      YES ─► check directly (no DNS needed)        │    │
   │  │  Hostname domain?  dns.lookup(host, {all: true})                │    │
   │  │                                                                 │    │
   │  │  For each resolved address:                                     │    │
   │  │  ┌────────────────────────────────────────────────────────────┐ │    │
   │  │  │  IPv4 BLOCKED:                                             │ │    │
   │  │  │    10.0.0.0/8    (private)                                 │ │    │
   │  │  │    172.16.0.0/12 (private)                                 │ │    │
   │  │  │    192.168.0.0/16(private)                                 │ │    │
   │  │  │    169.254.0.0/16(link-local/APIPA)                        │ │    │
   │  │  │    100.64.0.0/10 (Carrier-grade NAT, RFC 6598)             │ │    │
   │  │  │    0.x.x.x       (this network)                            │ │    │
   │  │  │  IPv6 BLOCKED:                                             │ │    │
   │  │  │    fc00::/7      (Unique Local Addresses)                  │ │    │
   │  │  │    fe80::/10     (link-local)                              │ │    │
   │  │  │    ::            (all-zeros)                               │ │    │
   │  │  │  ALLOWED (loopback):                                       │ │    │
   │  │  │    127.0.0.1     (IPv4 loopback — local dev OK)            │ │    │
   │  │  │    ::1           (IPv6 loopback — local dev OK)            │ │    │
   │  │  └────────────────────────────────────────────────────────────┘ │    │
   │  │                                                                 │    │
   │  │  ANY address is private ──► ERR_HTTP_HOOK_BLOCKED_ADDRESS       │    │
   │  │  ALL addresses pass    ──► proceed to HTTP POST                 │    │
   │  └─────────────────────────────────────────────────────────────────┘    │
   │                          │                                              │
   │                          ▼                                              │
   │  ┌──────────────── HTTP POST  ──────────────────────────────────────┐   │
   │  │  axios.post(url, body, {                                         │   │
   │  │    headers: { "Content-Type": "application/json", ...merged },   │   │
   │  │    timeout: hook.timeout * 1000 (default: 600000ms),             │   │
   │  │    responseType: "text",                                         │   │
   │  │    validateStatus: () => true,  // don't throw on 4xx/5xx        │   │
   │  │    maxRedirects: 0,              // no redirect following        │   │
   │  │    proxy: sandboxProxy || false,                                 │   │
   │  │    lookup: (no proxy) ? NO8 : undefined  // custom DNS resolver  │   │
   │  │  })                                                              │   │
   │  │                                                                  │   │
   │  │  ok = status 200–299                                             │   │
   │  │  body = response text (parsed as JSON by hook pipeline)          │   │
   │  └──────────────────────────────────────────────────────────────────┘   │
   └─────────────────────────────────────────────────────────────────────────┘
```

### Policy Settings (Enterprise)

Two new policy-level controls restrict HTTP hook network reach globally:

```json
// In managed-settings.json (policySettings):
{
  "allowedHttpHookUrls": [
    "https://hooks.company.internal/*",
    "https://monitoring.example.com/webhook"
  ],
  "httpHookAllowedEnvVars": [
    "HOOK_AUTH_TOKEN",
    "DEPLOYMENT_ENV"
  ]
}
```

```
   Policy Layering for HTTP Hooks
   ┌─────────────────────────────────────────────────────────────────┐
   │                    Settings Priority                            │
   │  localSettings     ──── hook.allowedEnvVars: ["A","B","C"]      │
   │  projectSettings   ──── hook.allowedEnvVars: ["A","B"]          │
   │  userSettings      ──────────────────────────────────────────── │
   │  policySettings    ──── httpHookAllowedEnvVars: ["A","D"]       │
   │                                                                 │
   │  Effective allowed vars = hook.allowedEnvVars                   │
   │                         ∩ policy.httpHookAllowedEnvVars         │
   │                         = ["A"]  (only A is in both)            │
   │                                                                 │
   │  Similarly:                                                     │
   │  hook.url must match allowedHttpHookUrls (if set by policy)     │
   └─────────────────────────────────────────────────────────────────┘
```

---

## 3. New Command Hook Field: `asyncRewake`

2.1.59 had `async` (fire-and-forget background). 2.1.70 adds `asyncRewake`.

```
   Command Hook Async Modes (2.1.70)
   ┌─────────────────────────────────────────────────────────────────────┐
   │  async: false (default)                                             │
   │  ┌──────────┐  stdin  ┌──────────────┐  wait  ┌──────────────────┐  │
   │  │  Claude  │────────►│  Hook Proc   │───────►│  Claude resumes  │  │
   │  └──────────┘         └──────────────┘        └──────────────────┘  │
   │                                                                     │
   ├─────────────────────────────────────────────────────────────────────┤
   │  async: true                                                        │
   │  ┌──────────┐  stdin  ┌──────────────┐                              │
   │  │  Claude  │────────►│  Hook Proc   │ (background, not awaited)    │
   │  └────┬─────┘         └──────────────┘                              │
   │       │ resumes immediately                                         │
   │       ▼                                                             │
   │  (hook outcome ignored)                                             │
   │                                                                     │
   ├─────────────────────────────────────────────────────────────────────┤
   │  asyncRewake: true  ← NEW IN 2.1.70                                 │
   │  ┌──────────┐  stdin  ┌──────────────┐                              │
   │  │  Claude  │────────►│  Hook Proc   │ (background)                 │
   │  └────┬─────┘         └──────┬───────┘                              │
   │       │ resumes immediately  │                                      │
   │       ▼                      │ exit code 0  ──► silently done       │
   │  (continues work)            │                                      │
   │                              │ exit code 2  ──► WAKE MODEL          │
   │                              │               inject blocking error  │
   │                              │               into conversation      │
   │                              └──────────────────────────────────────│
   └─────────────────────────────────────────────────────────────────────┘
```

**Config:**
```json
{
  "type": "command",
  "command": "my_async_validator.sh",
  "asyncRewake": true
}
```

Use case: a hook that watches background CI results and interrupts Claude only if
tests fail, without blocking the main conversation turn while tests run.

---

## 4. SessionEnd — New Reason

```
   SessionEnd.reason values:
   ┌──────────────────────────────────────────────────────────────────┐
   │  2.1.59:                                                         │
   │    "clear"                  user ran /clear                      │
   │    "logout"                 user logged out                      │
   │    "prompt_input_exit"      user exited at prompt                │
   │    "other"                  catch-all                            │
   │                                                                  │
   │  2.1.70 adds:                                                    │
   │    "bypass_permissions_disabled"   ← NEW                         │
   │      bypassPermissions mode was active and has been disabled;    │
   │      session terminates to enforce the mode change               │
   └──────────────────────────────────────────────────────────────────┘
```

---

## 5. Complete Event Inventory (2.1.70)

```
   Hook Events by Subsystem (21 total, 2.1.70)
   ┌────O──────────────────────────────────────────────────────────────────┐
   │  TOOL EXECUTION                                                       │
   │    PreToolUse  ──── before tool runs; can block or modify input       │
   │    PostToolUse ──── after tool runs; can inject context or mod output │
   │    PostToolUseFailure ── after tool error; can inject context         │
   │    PermissionRequest  ── on permission dialog; can approve/deny       │
   ├────S──────────────────────────────────────────────────────────────────┤
   │  SESSION LIFECYCLE                                                    │
   │    SessionStart  ── on session start; blocked for HTTP hooks          │
   │    SessionEnd    ── on session end                                    │
   │    Stop          ── when Claude finishes a response turn              │
   │    Setup         ── on repo init/maintenance; blocked for HTTP hooks  │
   │    UserPromptSubmit ── when user submits prompt; can block/modify     │
   │    PreCompact    ── before compaction; can inject compact instructions│
   ├────M──────────────────────────────────────────────────────────────────┤
   │  MEMORY / INSTRUCTIONS  ← partially new                               │
   │    InstructionsLoaded  ── [NEW] when CLAUDE.md / memory file loads    │
   ├────P──────────────────────────────────────────────────────────────────┤ 
   │  MCP / ELICITATION  ← entirely new                                    │
   │    Elicitation        ── [NEW] MCP server requests user input         │
   │    ElicitationResult  ── [NEW] after user responds to elicitation     │
   ├────B──────────────────────────────────────────────────────────────────┤
   │  SUBAGENT / TEAM                                                      │
   │    SubagentStart  ── when Task tool creates a subagent                │
   │    SubagentStop   ── when subagent finishes; can inject error         │ 
   │    TeammateIdle   ── teammate about to go idle; can prevent           │
   │    TaskCompleted  ── task being marked done; can prevent              │
   ├────N──────────────────────────────────────────────────────────────────┤
   │  CONFIGURATION                                                        │
   │    ConfigChange  ── config file changes live; can block apply         │ 
   ├────R──────────────────────────────────────────────────────────────────┤
   │  WORKTREE                                                             │
   │    WorktreeCreate  ── hook creates the worktree; stdout = path        │
   │    WorktreeRemove  ── hook removes the worktree                       │
   ├────T──────────────────────────────────────────────────────────────────┤
   │  NOTIFICATION                                                         │
   │    Notification  ── permission_prompt/idle_prompt/auth_success/etc    │
   └───────────────────────────────────────────────────────────────────────┘
```

---

## 6. Elicitation Hook Architecture in Context

```
   MCP Elicitation Lifecycle with Hooks (2.1.70)
   ┌──────────────────────────────────────────────────────────────────────┐
   │                                                                      │
   │  ┌────────────┐  1. elicitation request   ┌───────────────────────┐  │
   │  │ MCP Server │──────────────────────────►│   Claude Code Core    │  │
   │  └────────────┘                            └──────────┬───────────┘  │
   │                                                       │              │
   │                                            2. fire Elicitation hook  │
   │                                                       ▼              │
   │                                            ┌──────────────────────┐  │
   │                                            │  Elicitation Hook(s) │  │
   │                                            └──────────┬───────────┘  │
   │                                                       │              │
   │           ┌───────────────────────────────────────────┤              │
   │           │ action: none     │ action: "accept"       │ "decline"    │
   │           │                  │ content: {...}         │              │
   │           ▼                  ▼                        ▼              │
   │  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────────┐ │
   │  │  Show dialog    │  │  Skip dialog     │  │  Block elicitation   │ │
   │  │  to user        │  │  Auto-accept     │  │  Return decline      │ │
   │  └────────┬────────┘  │  with content    │  │  to MCP server       │ │
   │           │           └─────────┬────────┘  └──────────────────────┘ │
   │    3. user fills                │                                    │
   │    and submits                  │                                    │
   │           │                     │                                    │
   │           └─────────────────────┘                                    │
   │                       │                                              │
   │              4. fire ElicitationResult hook                          │
   │                       ▼                                              │
   │            ┌────────────────────────────────┐                        │
   │            │    ElicitationResult Hook(s)   │                        │
   │            └──────────────────┬─────────────┘                        │
   │                               │                                      │
   │           ┌───────────────────┼────────────────────┐                 │
   │           │ no override       │ override action    │ "decline"       │
   │           ▼                   ▼ + content          ▼                 │
   │  ┌─────────────────┐  ┌───────────────┐  ┌─────────────────────────┐ │
   │  │  Send original  │  │  Send hook's  │  │  Send decline to MCP    │ │
   │  │  result to MCP  │  │  result to    │  │  "Elicitation result    │ │
   │  │  server         │  │  MCP server   │  │   blocked by hook"      │ │
   │  └─────────────────┘  └───────────────┘  └─────────────────────────┘ │
   │           │                   │                                      │
   │           └───────────────────┘                                      │
   │                       │                                              │
   │                       ▼                                              │
   │  ┌────────────┐  5. receives result   ┌──────────────────────────┐   │
   │  │ MCP Server │◄──────────────────────│   Claude Code Core       │   │
   │  └────────────┘                       └──────────────────────────┘   │
   └──────────────────────────────────────────────────────────────────────┘
```

---

## 7. InstructionsLoaded — Load Reason Taxonomy

```
   CLAUDE.md / Memory File Loading Graph
   ┌──────────────────────────────────────────────────────────────────────┐
   │                                                                      │
   │  Session start                                                       │
   │  ┌────────────────────────────────────────────────────────────────┐  │
   │  │ load_reason: "session_start"                                   │  │
   │  │   → ~/.claude/CLAUDE.md    (memory_type: "User")               │  │
   │  │   → .claude/CLAUDE.md      (memory_type: "Project")            │  │
   │  │   → .claude/CLAUDE.local.md(memory_type: "Local")              │  │
   │  │   → [managed paths]        (memory_type: "Managed")            │  │
   │  └────────────────────────────────────────────────────────────────┘  │
   │                                                                      │
   │  Directory traversal (ascending to project root)                     │
   │  ┌───────────────────────────────────────────────────────────────┐   │
   │  │ load_reason: "nested_traversal"                               │   │
   │  │   → /project/src/CLAUDE.md discovered while walking up        │   │
   │  └───────────────────────────────────────────────────────────────┘   │
   │                                                                      │
   │  Glob pattern match (from a parent CLAUDE.md)                        │
   │  ┌───────────────────────────────────────────────────────────────┐   │
   │  │ load_reason: "path_glob_match"                                │   │
   │  │   globs: ["src/**", "*.py"]                                   │   │
   │  │   trigger_file_path: /project/CLAUDE.md                       │   │
   │  │   → current file matches one of the globs → load the file     │   │
   │  └───────────────────────────────────────────────────────────────┘   │
   │                                                                      │
   │  Explicit include (from a parent CLAUDE.md)                          │
   │  ┌───────────────────────────────────────────────────────────────┐   │
   │  │ load_reason: "include"                                        │   │
   │  │   parent_file_path: /project/CLAUDE.md                        │   │
   │  │   → explicit @path/to/file.md reference                       │   │
   │  └───────────────────────────────────────────────────────────────┘   │
   └──────────────────────────────────────────────────────────────────────┘
```

---

## 8. Summary of All Changes

```
   Diff Summary: 2.1.59 → 2.1.70 Hook System
   ┌────────────────────────────────────────────────────────────────────┐
   │  NEW EVENTS                                                        │
   │  ┌──────────────────────────────────────────────────────────────┐  │
   │  │  Elicitation        intercept MCP server data requests       │  │
   │  │  ElicitationResult  intercept user responses to MCP server   │  │
   │  │  InstructionsLoaded observe memory/CLAUDE.md file loading    │  │
   │  └──────────────────────────────────────────────────────────────┘  │
   │                                                                    │
   │  NEW COMMAND HOOK FIELD                                            │
   │  ┌──────────────────────────────────────────────────────────────┐  │
   │  │  asyncRewake: true    background + model wakeup on exit 2    │  │
   │  └──────────────────────────────────────────────────────────────┘  │
   │                                                                    │
   │  HTTP HOOK HARDENING                                               │
   │  ┌──────────────────────────────────────────────────────────────┐  │
   │  │  allowedHttpHookUrls    URL allowlist (wildcard patterns)    │  │
   │  │  httpHookAllowedEnvVars env var allowlist (intersects hook)  │  │
   │  │  DNS SSRF protection    private IPs blocked via dns.lookup   │  │
   │  │    loopback allowed     127.0.0.1, ::1 pass through          │  │
   │  │    ERR_HTTP_HOOK_BLOCKED_ADDRESS  error code for blocked IPs │  │
   │  │  sandbox proxy routing  routes via SandboxManager proxy port │  │
   │  │  maxRedirects: 0        redirect-based SSRF impossible       │  │
   │  └──────────────────────────────────────────────────────────────┘  │
   │                                                                    │
   │  SESSION END REASON                                                │
   │  ┌──────────────────────────────────────────────────────────────┐  │
   │  │  "bypass_permissions_disabled"   bypassPermissions turned off│  │
   │  └──────────────────────────────────────────────────────────────┘  │
   │                                                                    │
   │  UNCHANGED (confirmed same in both versions)                       │
   │  ┌──────────────────────────────────────────────────────────────┐  │
   │  │  Stop, SubagentStop:  last_assistant_message field (same)    │  │
   │  │  SessionStart:        agent_type, model fields (same)        │  │
   │  │  HTTP hooks:          headers, allowedEnvVars per-hook (same)│  │
   │  │  command hooks:       once, statusMessage (same)             │  │
   │  │  PermissionRequest:   permission_suggestions (same)          │  │
   │  │  all 18 prior events: exit code semantics unchanged          │  │
   │  └──────────────────────────────────────────────────────────────┘  │
   └────────────────────────────────────────────────────────────────────┘
```

---

*Source: JS payload diff 2.1.59 → 2.1.70, extracted from BunFS cli.js*
*Analysis date: 2026-03-06*
