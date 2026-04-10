# Hook System — Claude Code 2.1.59

## Overview

Hooks are shell commands (or internal callbacks) that fire at specific lifecycle points in Claude Code. They can observe, block, modify, or augment Claude's behavior. Hooks receive JSON on stdin, may return JSON on stdout, and communicate outcome via exit codes.

Hooks are entirely JS-layer (cli.js). No native code is involved.

---

## Hook Event Types (18 total)

### Tool Events (have matcher on `tool_name`)

| Event | Fires | exit 0 | exit 2 | other |
|-------|-------|--------|--------|-------|
| `PreToolUse` | Before tool execution | silent | block tool call, show stderr to model | show stderr to user only |
| `PostToolUse` | After tool execution | show stdout in transcript (ctrl+o) | show stderr to model immediately | show stderr to user only |
| `PostToolUseFailure` | After tool execution fails | show stdout in transcript (ctrl+o) | show stderr to model immediately | show stderr to user only |
| `PermissionRequest` | Permission dialog displayed | use hook decision if provided | show stderr to user only | show stderr to user only |

### Session Lifecycle Events

| Event | Fires | Matcher field | exit 0 | exit 2 | other |
|-------|-------|--------------|--------|--------|-------|
| `SessionStart` | New session starts | `source`: startup/resume/clear/compact | show stdout to Claude | blocked (ignored) | show stderr to user only |
| `SessionEnd` | Session is ending | `reason`: clear/logout/prompt_input_exit/other | completes successfully | — | show stderr to user only |
| `Stop` | Claude concludes response | none | silent | show stderr to model, continue conversation | show stderr to user only |
| `Setup` | Repo init and maintenance | `trigger`: init/maintenance | show stdout to Claude | blocked (ignored) | show stderr to user only |
| `UserPromptSubmit` | User submits a prompt | none | show stdout to Claude | block processing, erase prompt, show stderr to user | show stderr to user only |
| `PreCompact` | Before conversation compaction | `trigger`: manual/auto | append stdout as compact instructions | block compaction | show stderr to user, continue |

### Subagent / Team Events

| Event | Fires | Matcher field | exit 0 | exit 2 | other |
|-------|-------|--------------|--------|--------|-------|
| `SubagentStart` | Task tool call starts | `agent_type` | show stdout to subagent | blocked (ignored) | show stderr to user only |
| `SubagentStop` | Subagent concludes response | `agent_type` | silent | show stderr to subagent, keep running | show stderr to user only |
| `TeammateIdle` | Teammate about to go idle | none | silent | show stderr to teammate, prevent idle | show stderr to user only |
| `TaskCompleted` | Task being marked completed | none | silent | show stderr to model, prevent task completion | show stderr to user only |

### Configuration Events

| Event | Fires | Matcher field | exit 0 | exit 2 | other |
|-------|-------|--------------|--------|--------|-------|
| `ConfigChange` | Config file changes during session | `source`: user_settings/project_settings/local_settings/policy_settings/skills | allow change | block change from being applied | show stderr to user only |

### Worktree Events (VCS-agnostic isolation)

| Event | Fires | exit 0 | other |
|-------|-------|--------|-------|
| `WorktreeCreate` | Create isolated worktree; stdout = absolute path to worktree dir | success | creation failed |
| `WorktreeRemove` | Remove previously created worktree | success | show stderr to user only |

### Notification Event

| Event | Fires | Matcher field | exit 0 | other |
|-------|-------|--------------|--------|-------|
| `Notification` | Notification sent | `notification_type`: permission_prompt/idle_prompt/auth_success/elicitation_dialog | silent | show stderr to user only |

---

## Hook Input Format

Every hook receives a JSON object on **stdin**. All events include a base set of fields, plus event-specific fields.

### Base Fields (all events)
```json
{
  "session_id": "<uuid>",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default|acceptEdits|dontAsk|bypassPermissions|plan"
}
```
Source: `yJ(permissionMode, sessionId)` in cli.js

### Event-Specific Fields

**PreToolUse:**
```json
{
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { ...tool arguments... },
  "tool_use_id": "<uuid>"
}
```

**PostToolUse:**
```json
{
  "hook_event_name": "PostToolUse",
  "tool_name": "Bash",
  "tool_input": { ...tool arguments... },
  "tool_response": { ...tool response... },
  "tool_use_id": "<uuid>"
}
```

**PostToolUseFailure:**
```json
{
  "hook_event_name": "PostToolUseFailure",
  "tool_name": "Bash",
  "tool_input": { ...tool arguments... },
  "tool_use_id": "<uuid>",
  "error": "error message",
  "error_type": "...",
  "is_interrupt": false,
  "is_timeout": false
}
```

**PermissionRequest:**
```json
{
  "hook_event_name": "PermissionRequest",
  "tool_name": "Bash",
  "tool_input": { ...tool arguments... },
  "tool_use_id": "<uuid>"
}
```

**UserPromptSubmit:**
```json
{
  "hook_event_name": "UserPromptSubmit",
  "prompt": "original user prompt text"
}
```

**SessionStart:**
```json
{
  "hook_event_name": "SessionStart",
  "source": "startup|resume|clear|compact"
}
```

**SessionEnd:**
```json
{
  "hook_event_name": "SessionEnd",
  "reason": "clear|logout|prompt_input_exit|other"
}
```

**Stop:**
```json
{
  "hook_event_name": "Stop"
}
```
(base fields only)

**SubagentStart:**
```json
{
  "hook_event_name": "SubagentStart",
  "agent_id": "<uuid>",
  "agent_type": "general-purpose|explore|..."
}
```

**SubagentStop:**
```json
{
  "hook_event_name": "SubagentStop",
  "agent_id": "<uuid>",
  "agent_type": "...",
  "agent_transcript_path": "/path/to/agent/transcript.jsonl"
}
```

**Setup:**
```json
{
  "hook_event_name": "Setup",
  "trigger": "init|maintenance"
}
```

**PreCompact:**
```json
{
  "hook_event_name": "PreCompact",
  "trigger": "manual|auto",
  ...compaction details...
}
```

**TeammateIdle:**
```json
{
  "hook_event_name": "TeammateIdle",
  "teammate_name": "researcher",
  "team_name": "my-team"
}
```

**TaskCompleted:**
```json
{
  "hook_event_name": "TaskCompleted",
  "task_id": "1",
  "task_subject": "Fix bug",
  "task_description": "...",
  "teammate_name": "coder",
  "team_name": "my-team"
}
```

**ConfigChange:**
```json
{
  "hook_event_name": "ConfigChange",
  "source": "user_settings|project_settings|local_settings|policy_settings|skills",
  "file_path": "/path/to/settings.json"
}
```

**Notification:**
```json
{
  "hook_event_name": "Notification",
  "message": "notification text",
  "title": "notification title",
  "notification_type": "permission_prompt|idle_prompt|auth_success|elicitation_dialog"
}
```

**WorktreeCreate:**
```json
{
  "hook_event_name": "WorktreeCreate",
  "name": "suggested-worktree-slug"
}
```

**WorktreeRemove:**
```json
{
  "hook_event_name": "WorktreeRemove",
  "worktree_path": "/absolute/path/to/worktree"
}
```

**Env vars injected into hook process:**
```
CLAUDE_PROJECT_DIR     = V$() (project cwd)
CLAUDE_PLUGIN_ROOT     = plugin root (if hook comes from a plugin)
CLAUDE_ENV_FILE        = path to env file (SessionStart + Setup only)
```

---

## Hook Output JSON Schema

Hooks may write JSON to stdout to communicate structured results back. Parsed via Zod:

```typescript
// Async signal (immediate exit → background process):
{ async: true, asyncTimeout?: number }

// Normal output:
{
  continue?: boolean            // false = stop Claude after hook (default: true)
  suppressOutput?: boolean      // true = hide stdout from transcript
  stopReason?: string           // message shown when continue=false
  decision?: "approve" | "block"  // legacy permission (deprecated)
  reason?: string               // explanation for decision
  systemMessage?: string        // warning message shown to user

  hookSpecificOutput?: {
    // For PreToolUse:
    hookEventName: "PreToolUse"
    permissionDecision?: "allow" | "deny" | "ask"
    permissionDecisionReason?: string
    updatedInput?: Record<string, unknown>   // modify tool's input before execution
    additionalContext?: string               // context injected as Claude's context

    // For PostToolUse:
    hookEventName: "PostToolUse"
    additionalContext?: string
    updatedMCPToolOutput?: unknown   // replace MCP tool's output in conversation

    // For PostToolUseFailure | UserPromptSubmit | SessionStart | Setup | SubagentStart | Notification:
    hookEventName: "..."
    additionalContext?: string

    // For PermissionRequest:
    hookEventName: "PermissionRequest"
    decision: {
      behavior: "allow"
      updatedInput?: Record<string, unknown>
      updatedPermissions?: PermissionChange[]
    } | {
      behavior: "deny"
      message?: string
      interrupt?: boolean
    }
  }
}
```

### Exit Code Semantics (summary)
```
exit 0 → success; stdout handling depends on event (silent / show to Claude / show in transcript)
exit 2 → blocking; stderr handling depends on event (block tool / block prompt / inject to model)
other  → non-blocking error; stderr shown to user only, execution continues
```

---

## Hook Types

The hook config object has a `type` field. User-configurable types:

### `"command"` — Shell Command
```json
{
  "type": "command",
  "command": "python3 ~/hooks/my_hook.py",
  "timeout": 30
}
```
- Most common type
- Spawned as child process with input JSON on stdin
- `timeout`: seconds before SIGTERM (default: 600s / 10 minutes)
- `CLAUDE_CODE_SHELL_PREFIX` env var → prepend prefix to command (e.g., `sudo -u hookuser`)
- Windows: `.sh` commands auto-prefixed with `bash`

### `"prompt"` — Model-Based Condition Evaluator (`processPromptHook (jDB)`, L6208)
```json
{
  "type": "prompt",
  "prompt": "Check that all tests pass",
  "timeout": 60,
  "model": "claude-haiku-4-5-20251001"
}
```
Queries a **separate model instance** to evaluate a condition. Single-turn, no agent loop.

**Implementation — `jDB(H, $, A, L, I, D, B, f)`:**

| Param | Meaning |
|-------|---------|
| `H` | Hook config (`.prompt`, `.timeout`, `.model`) |
| `$` | Hook name (string) |
| `A` | Hook event name |
| `L` | Template variables for prompt expansion |
| `I` | Abort signal |
| `D` | toolUseContext (parent context) |
| `B` | Fork context messages (conversation history, optional) |
| `f` | Tool use ID (or auto-generated UUID) |

**Flow:**
1. **Expand prompt template**: `sR$(H.prompt, L)` -> `X6H()` (variable substitution)
2. **Build messages**: If fork context provided, append; otherwise just the expanded prompt
3. **Set timeout**: `H.timeout * 1000` milliseconds, default **30 seconds**
4. **Query model** via `queryModelForHook (Mu)`:
   - System prompt: `"You are evaluating a hook in Claude Code."`
   - Output format: JSON schema `{ok: boolean, reason?: string}`
   - Thinking: **disabled** (no chain-of-thought overhead)
   - Model: `H.model ?? Y5()` — see Model Selection below
   - **mcpTools: `[]`** — prompt hooks get NO MCP tools
   - **tools: `D.options.tools`** — parent's built-in tools (unlikely used with JSON output)
   - isNonInteractiveSession: `true`
5. **Parse response**: Extract text content, parse as JSON, validate against `hookResultSchema (FnH)` schema
6. **Decision**:
   - `{ok: true}` -> outcome `"success"`
   - `{ok: false, reason: "..."}` -> outcome `"blocking"` (prevents action, reason surfaced)
   - JSON parse failure -> `"non_blocking_error"` (action proceeds with warning)
   - Timeout/abort -> `"cancelled"`

### `"agent"` — Full Agent with Tool Access (`processAgentHook (RDB)`, L6212)
```json
{
  "type": "agent",
  "prompt": ["Verify that {file} has no lint errors"],
  "timeout": 120,
  "model": "claude-haiku-4-5-20251001"
}
```
Spawns a **full multi-turn agent** that can read files, run searches, and verify conditions.
The most powerful hook type.

**Implementation — `RDB(H, $, A, L, I, D, B, f)`:**

Same parameter signature as `processPromptHook (jDB)`.

**Flow:**
1. **Get transcript path**: `Jy(agentId)` or `_X()` — resolves to the conversation JSONL file
2. **Construct tool set**:
   ```javascript
   let z = [
     ...D.options.tools                    // Parent's built-in tools
       .filter(not StructuredOutput)       // Remove existing StructuredOutput
       .filter(not n3H),                   // Remove: TaskOutput, ExitPlanMode,
                                           //   EnterPlanMode, Task, AskUserQuestion, TaskStop
     xDB()                                 // Add: StructuredOutput verifier tool
   ];
   ```
3. **System prompt**:
   ```
   You are verifying a stop condition in Claude Code. Your task is to verify
   that the agent completed the given plan. The conversation transcript is
   available at: <transcript_path>

   Use the available tools to inspect the codebase and verify the condition.
   Use as few steps as possible - be efficient and direct.

   When done, return your result using the StructuredOutput tool with:
   - ok: true if the condition is met
   - ok: false with reason if the condition is not met
   ```
4. **Permission override**: Mode set to `dontAsk` with session allow rule `Read(/<transcript_path>)`
5. **Execute agent loop** via `agentLoop (uN)`:
   - Max turns: **50** (hardcoded)
   - Thinking: **disabled**
   - isNonInteractiveSession: `true`
   - **mcpTools: NOT passed** (no MCP tool access)
6. **Force tool call**: `enforceToolCall (eR$)` → `v2$()` enforces StructuredOutput call
   - Enforcement timeout: **5000ms**
   - System message: "You MUST call the StructuredOutput tool to complete this request."
7. **Result handling**:
   - StructuredOutput `{ok: true}` -> `"success"`
   - StructuredOutput `{ok: false, reason}` -> `"blocking"`
   - 50 turns without output -> `"cancelled"` + telemetry `tengu_agent_stop_hook_max_turns`
   - No structured output -> `"cancelled"` + telemetry `tengu_agent_stop_hook_error`
   - Exception -> `"non_blocking_error"`

**StructuredOutput verifier tool** (`createStopVerifierTool (xDB)`, L6208):
```javascript
xDB() = {
  name: "StructuredOutput",
  inputSchema: {
    ok: boolean,           // Whether the condition was met
    reason?: string        // Reason if not met
  },
  prompt: "Use this tool to return your verification result.
           You MUST call this tool exactly once at the end of your response."
}
```

### `"callback"` — Internal JS Callback (not user-configurable)
Used by plugins and internal systems. Takes `(input, hookId, signal, hookIndex)` args.
Internal callbacks with `hook.internal === true` are filtered from telemetry counts (`isInternalCallback (dDB)`).

### `"function"` — Internal JS Function (not user-configurable, REPL only)
Stop hooks only. Takes `(messages, signal)` → `boolean` (true=continue).

### `"http"` — HTTP POST Endpoint
```json
{
  "type": "http",
  "url": "http://localhost:8080/hook"
}
```
Sends hook input as HTTP POST body, parses JSON response.
**Note:** HTTP hooks are **blocked for `SessionStart` and `Setup` events** because the session
may not be fully initialized. Log message: `"Skipping HTTP hook — HTTP hooks are not supported for SessionStart/Setup"`.

### Model Selection for Prompt/Agent Hooks

Both `processPromptHook (jDB)` and `processAgentHook (RDB)` use the same model resolution:

```javascript
function Y5() {
  return process.env.ANTHROPIC_SMALL_FAST_MODEL || _nH()
}
function _nH() {
  return process.env.ANTHROPIC_DEFAULT_HAIKU_MODEL || a9().haiku45
}
```

**Default: Haiku 4.5** — the cheapest and fastest model available.

Override priority:
1. Per-hook `model` field (highest)
2. `ANTHROPIC_SMALL_FAST_MODEL` env var
3. `ANTHROPIC_DEFAULT_HAIKU_MODEL` env var
4. Hardcoded `haiku45` constant (lowest)

The hook model's decision is **authoritative** — there is no appeal to the main model.
If Haiku blocks an action, Opus cannot override it.

---

## Async Hook Mechanism

Hooks can signal they want to run in the background (non-blocking):

**Method 1: Config-based async**
```json
{
  "type": "command",
  "command": "my_slow_hook.sh",
  "async": true,
  "asyncTimeout": 60000
}
```
Hook process is backgrounded immediately after stdin is written.

**Method 2: Output-based async**
When hook stdout starts with `{"async": true, ...}` before output buffer has `}`, the process is backgrounded:
```
→ Hook starts, writes {"async": true, "asyncTimeout": 30000} to stdout
→ CC detects this, backgrounds the process (ID: `async_hook_<pid>`)
→ CC continues without waiting for hook completion
```

Implementation:
```javascript
// p = true once stdout buffer has first "}"
// If async detected: bDB({processId, hookId, ...}) → backgrounds
// bDB uses $ID() to track the process
```

---

## Matcher Logic (`hj9(toolName, matcher)`)

Matchers are used by PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, SubagentStart, SubagentStop, Notification, SessionStart, PreCompact, Setup, ConfigChange.

```javascript
function hj9(name, matcher) {
  if (!matcher || matcher === "*") return true    // match all

  if (/^[a-zA-Z0-9_|]+$/.test(matcher)) {
    // Simple string(s)
    if (matcher.includes("|"))
      return matcher.split("|").map(E2).includes(name)  // pipe-separated
    return name === E2(matcher)                          // exact match
  }

  // Regex mode
  try {
    let re = new RegExp(matcher)
    if (re.test(name)) return true
    for (let alias of xHI(name)) if (re.test(alias)) return true
    return false
  } catch {
    // Invalid regex → false + log warning
    return false
  }
}
```

Matcher examples:
```
"*"          → all tools
"Bash"       → only Bash
"Write|Edit" → Write or Edit
"Web.*"      → any tool starting with Web (regex)
"Glob"       → only Glob
```

`E2()` normalizes tool name casing. `xHI(name)` returns tool aliases.

---

## Hook Configuration Structure

### Settings JSON format
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/hooks/pre_tool.py",
            "timeout": 30
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write \"$CLAUDE_PROJECT_DIR\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude finished'"
          }
        ]
      }
    ]
  }
}
```

### Settings Sources (priority order, lowest → highest)
```
localSettings     → .claude/settings.local.json
projectSettings   → .claude/settings.json
userSettings      → ~/.claude/settings.json
policySettings    → MDM / managed-settings.json / registry
```

Higher priority overrides lower. Policy settings hooks run alongside user hooks unless `allowManagedHooksOnly` is set.

### Policy Controls
```json
// In policySettings (managed-settings.json):
{
  "disableAllHooks": true,          // all hooks skipped globally
  "allowManagedHooksOnly": true     // only policySettings hooks run;
                                    // user-defined hooks from all other sources blocked
}
```

When `disableAllHooks=true`:
- No hook commands execute
- StatusLine is not displayed
- Tool operations proceed without hook validation

---

## MCP Tool Isolation in Hooks

Hooks have **no access to MCP tools** in any execution type:

| Hook Type | MCP Access? | Evidence |
|-----------|-------------|---------|
| `command` (shell) | No | Shell subprocess; no MCP client connection |
| `prompt` (`processPromptHook (jDB)`) | No | `mcpTools: []` explicitly passed to `queryModelForHook (Mu)` |
| `agent` (`processAgentHook (RDB)`) | No | `mcpTools` not in options; tools from `D.options.tools` only |
| `http` | No | HTTP POST to external URL; no tool execution context |
| `callback`/`function` | No | Internal code; no MCP client available |

However, hooks **can intercept and transform MCP tool I/O**:

**Input modification** (PreToolUse):
- `hookSpecificOutput.updatedInput` replaces the tool's input parameters
- Works for both built-in tools and MCP tools
- The modified input is what gets executed

**Output replacement** (PostToolUse):
- `hookSpecificOutput.updatedMCPToolOutput` replaces the MCP tool's result
- Gate: `uZ($)` verifies the tool has `$.isMcp === true`
- Only applies to MCP tools (built-in tool outputs cannot be replaced)
- The original output is **not preserved** — it's silently replaced
- Log: `"Hook replaced MCP tool output"`

So while hooks cannot *call* MCP tools, they can *intercept, modify inputs to, and replace outputs from* all MCP tool invocations.

---

## Hook Pipeline Deep Dive (`hookExecutionPipeline (ay)` generator, L6227)

The main hook execution is an async generator function `hookExecutionPipeline (ay)`. All event-specific
executor functions (e.g., `executePreToolHooks (wkA)`, `executePostToolHooks (ZkA)`, `executeStopHooks (ykA)`) call into this pipeline.

### Pipeline Architecture

```
ay({hookInput, toolUseID, matchQuery, signal, timeoutMs, toolUseContext, messages})
  |
  +-- Guard checks (any true -> return immediately):
  |     XnH()        -> hooks globally disabled?
  |     CLAUDE_CODE_SIMPLE env var set?
  |     $v$()        -> workspace trust not accepted?
  |
  +-- ncA() -> Find matching hooks
  |     |
  |     +-- bj9() -> Collect all registered hooks:
  |     |     1. nR$()  -> User settings hooks (always loaded)
  |     |     2. mZH()  -> Managed/enterprise policy hooks (always loaded)
  |     |     3. h2$()  -> Plugin hooks (SKIPPED if managed-only mode)
  |     |     4. g0D()  -> Skill hooks (SKIPPED if managed-only mode)
  |     |
  |     +-- Filter by matcher: hj9(query, matcher)
  |     +-- Deduplicate by command/prompt/url (Map keyed on identifier)
  |     +-- Split by type: command[], prompt[], agent[], http[], callback[], function[]
  |     +-- Merge all types into execution list
  |
  +-- Telemetry: tengu_run_hook
  |
  +-- For each matched hook, yield progress events:
  |     {type: "hook_progress", hookName, hookEvent, hookType}
  |
  +-- Execute hooks (varies by type):
  |     command  -> Av$() shell subprocess
  |     prompt   -> jDB() model query
  |     agent    -> RDB() agent loop
  |     http     -> HTTP POST
  |     callback -> direct call
  |     function -> direct call
  |
  +-- Process results from each hook:
  |     additionalContexts[]     -> injected into conversation
  |     updatedMCPToolOutput     -> replaces MCP tool result (PostToolUse only)
  |     permissionBehavior       -> deny > ask > allow (strictest wins across all hooks)
  |     decision: approve/block  -> PreToolUse gate (legacy path)
  |     continue: false          -> stops the conversation
  |     systemMessage            -> warning shown to user
  |     stopReason               -> message when continue=false
  |
  +-- Yield result events:
        hook_success | hook_blocking_error | hook_non_blocking_error |
        hook_cancelled | hook_system_message | hook_additional_context |
        hook_stopped_continuation
```

### Hook Source Merging (`collectAllHooks (bj9)`, L6227)

The `collectAllHooks (bj9)` function builds the complete hook registry from all sources:

```javascript
function bj9(appState, sessionId) {
  let hooks = {};

  // 1. User settings hooks — always loaded
  let userHooks = nR$();
  if (userHooks)
    for (let [event, matchers] of Object.entries(userHooks))
      hooks[event] = matchers.map(m => ({matcher: m.matcher, hooks: m.hooks}));

  // 2. Managed/policy hooks — always loaded
  let managedOnly = qj();  // Is managed-only mode active?
  let policyHooks = mZH();
  if (policyHooks)
    for (let [event, matchers] of Object.entries(policyHooks)) {
      if (!hooks[event]) hooks[event] = [];
      for (let m of matchers) {
        if (managedOnly && "pluginRoot" in m) continue;  // Skip plugin hooks in managed mode
        hooks[event].push(m);
      }
    }

  // 3 & 4. Plugin + Skill hooks — ONLY if not managed-only
  if (!managedOnly && appState !== undefined) {
    let pluginHooks = h2$(appState, sessionId);
    // ... merge plugin hooks
    let skillHooks = g0D(appState, sessionId);
    // ... merge skill hooks
  }

  return hooks;
}
```

**Managed-only mode** (`qj()` returns true): Only enterprise policy hooks and user settings
hooks execute. All plugin hooks and skill hooks are silently dropped. This is the
`allowManagedHooksOnly` policy setting.

### Permission Decision Aggregation

When multiple hooks return permission decisions, the **strictest decision wins**:

```
deny > ask > allow
```

If any hook returns `deny`, the final decision is `deny` regardless of what other hooks say.
This applies to both the `permissionBehavior` field (from `hookSpecificOutput`)
and the legacy `decision` field (approve/block).

---

## Execution Flow (Shell Command)

```
executePreToolHooks(toolName, toolUseId, toolInput, ...) → yields attachments
  ↓
yJ() → build base hook input
  ↓
ncA(appState, sessionId, "PreToolUse", hookInput) → getMatchingHooks
  ↓
For each matched hook:
  Av$(hook, event, hookName, inputJSON, signal, hookId, index, pluginRoot)
    ↓
    Resolve command (CLAUDE_CODE_SHELL_PREFIX, Windows .sh → bash)
    Set env: CLAUDE_PROJECT_DIR, CLAUDE_PLUGIN_ROOT, CLAUDE_ENV_FILE
    Spawn subprocess: shell=true, windowsHide=true, cwd=project dir
    Write inputJSON to stdin
    ↓
    Monitor stdout (check for async signal)
    Wait for: stdin write | stdout | stderr | process close
    ↓
    On exit:
      Parse stdout JSON (if any) via mDB() / vj9()
      Build result via pDB()
      Return {outcome, message, blocked, ...}
  ↓
Collect results → yield attachment messages
```

### Attachment Messages (transcript entries)
Each hook execution adds to the transcript as attachment records:

```typescript
type HookAttachment =
  | { type: "hook_success", hookName, toolUseID, hookEvent, content, stdout, stderr, exitCode }
  | { type: "hook_blocking_error", hookName, toolUseID, hookEvent, blockingError }
  | { type: "hook_non_blocking_error", hookName, toolUseID, hookEvent, stderr, stdout, exitCode }
  | { type: "hook_error_during_execution", hookName, toolUseID, hookEvent, content }
  | { type: "hook_cancelled", hookName, toolUseID, hookEvent }
  | { type: "hook_system_message", hookName, toolUseID, hookEvent, systemMessage }
  | { type: "hook_additional_context", hookName, toolUseID, hookEvent, additionalContext }
  | { type: "hook_stopped_continuation", hookName, toolUseID, hookEvent }
```

---

## Key Function Map

**133 hook-related functions identified.** Key functions listed below.

### Core Pipeline (L6227-6240)

| Function | Name | Role |
|----------|------|------|
| `hookExecutionPipeline (ay)` | `hookExecutionPipeline` | Main async generator — runs all hooks for an event |
| `getMatchingHooks (ncA)` | `getMatchingHooks` | Finds hooks matching event+matcher, deduplicates |
| `collectAllHooks (bj9)` | `collectAllHooks` | Merges hooks from all sources (user, policy, plugins, skills) |
| `createBaseHookInput (yJ)` | `createBaseHookInput` | Builds base JSON input for all hooks |
| `executeShellHook (Av$)` | *(internal)* | Shell command spawn + lifecycle |
| `parseHookOutput (pDB)` | *(internal)* | Parse JSON output -> hook result fields |
| `validateHookOutput (mDB)` | *(internal)* | Validate hook output against schema |
| `matchHookPattern (hj9)` | *(internal)* | Matcher logic (exact, pipe-separated, regex) |

### Hook Type Handlers

| Function | Type | Role |
|----------|------|------|
| `processPromptHook (jDB)` | `prompt` | Single-turn model query to evaluate condition (L6208) |
| `processAgentHook (RDB)` | `agent` | Multi-turn agent with tools to verify condition (L6212) |
| `createStopVerifierTool (xDB)` | *(tool)* | Creates StructuredOutput verifier tool for agent hooks |
| `expandHookPrompt (sR$)` | *(util)* | Expand hook prompt template variables (`X6H` wrapper) |
| `enforceToolCall (eR$)` | *(util)* | Force agent to call StructuredOutput (5s timeout) |
| `combineAbortSignals (kq)` | *(util)* | Combine parent + timeout abort signals |
| `getDefaultSmallModel (Y5)` | *(util)* | Default hook model: `ANTHROPIC_SMALL_FAST_MODEL` or Haiku 4.5 |
| `queryModelForHook (Mu)` | *(util)* | Single-turn model query function (used by prompt hooks) |
| `agentLoop (uN)` | *(util)* | Multi-turn agent loop function (used by agent hooks) |
| `createHookMessage (WB)` | *(util)* | Create hook result message for conversation transcript |

### Hook Schemas

| Symbol | Schema | Role |
|--------|--------|------|
| `hookResultSchema (FnH)` | `{ok: boolean, reason?: string}` | Hook verifier result (Zod) |
| `hookOutputSchema (yj9)` | Full hook output | Sync hook output schema (continue, decision, etc.) |
| `asyncHookSchema (jj9)` | `{async: true, asyncTimeout?: number}` | Async hook signal |
| `hookConfigUnion (oR$)` | Union of `yj9 \| jj9` | Combined hook config union |

### Event-Specific Executors

| Function | Name | Event |
|----------|------|-------|
| `executePreToolHooks (wkA)` | `executePreToolHooks` | PreToolUse |
| `executePostToolHooks (ZkA)` | `executePostToolHooks` | PostToolUse |
| `executePostToolUseFailureHooks (qkA)` | `executePostToolUseFailureHooks` | PostToolUseFailure |
| `executeStopHooks (ykA)` | `executeStopHooks` | Stop |
| `executeUserPromptSubmitHooks (acA)` | `executeUserPromptSubmitHooks` | UserPromptSubmit |
| `executeTeammateIdleHooks (RkA)` | `executeTeammateIdleHooks` | TeammateIdle |
| `executeTaskCompletedHooks (XlH)` | `executeTaskCompletedHooks` | TaskCompleted |
| `executeSessionStartHooks (zqA)` | `executeSessionStartHooks` | SessionStart |
| `executeSessionEndHooks (VuA)` | `executeSessionEndHooks` | SessionEnd |
| `executeSetupHooks (NqA)` | `executeSetupHooks` | Setup |
| `executeSubagentStartHooks (RyA)` | `executeSubagentStartHooks` | SubagentStart |
| `executePreCompactHooks (f2$)` | `executePreCompactHooks` | PreCompact |
| `executePermissionRequestHooks (oEH)` | `executePermissionRequestHooks` | PermissionRequest |
| `executeNotificationHooks (ENA)` | `executeNotificationHooks` | Notification |
| `executeConfigChangeHooks (XCH)` | `executeConfigChangeHooks` | ConfigChange |
| `executeWorktreeCreateHook (ZO$)` | `executeWorktreeCreateHook` | WorktreeCreate |
| `executeWorktreeRemoveHook (qO$)` | `executeWorktreeRemoveHook` | WorktreeRemove |

### Other

| Function | Name | Role |
|----------|------|------|
| `executeHooksOutsideREPL (JCH)` | `executeHooksOutsideREPL` | Hook execution outside REPL (headless) |
| `executeStatusLineCommand (ocA)` | `executeStatusLineCommand` | StatusLine display command |
| `executeFileSuggestionCommand (JuA)` | `executeFileSuggestionCommand` | Custom file suggestion provider |
| `hasWorktreeCreateHook (wO$)` | `hasWorktreeCreateHook` | Check if WorktreeCreate hook exists |
| `hasBlockingResult (UCH)` | `hasBlockingResult` | True if any hook result is blocking |
| `countHookTypes (lDB)` | `countHookTypes` | Count hooks by type for telemetry |
| `countPluginHooks (cDB)` | `countPluginHooks` | Count hooks by plugin ID for telemetry |
| `isInternalCallback (dDB)` | `isInternalCallback` | Filter internal callbacks from telemetry counts |
| `getHookIdentifier (zX)` | `getHookIdentifier` | Human-readable hook identifier for logging |

---

## Special Commands

### StatusLine (`executeStatusLineCommand (ocA)`)
Executes a configured status line command and displays its stdout in the terminal status bar. Configured via:
```json
{ "statusLineCommand": "my_status_script.sh" }
```
Fired periodically to update the status display. Subject to `disableAllHooks`.

### File Suggestion Command (`executeFileSuggestionCommand (JuA)`)
When `fileSuggestion.type === "command"` in settings, hooks can provide custom file completion suggestions. Replaces built-in git ls-files + ripgrep provider.

---

## Security Notes from Source

From the UI add-hook screen:
> "Hooks execute shell commands with your full user permissions. Only use hooks from trusted sources."

Warning conditions shown to user when adding hooks:
- **Relative path warning**: "Using a relative path for the executable may be insecure. Consider using an absolute path instead."
- **sudo warning**: "Using sudo in hooks can be dangerous and may expose your system to security risks."

Workspace trust check: `$v$()` → hooks skip execution if workspace trust hasn't been accepted.

---

## Telemetry Events

| Event | Payload |
|-------|---------|
| `tengu_run_hook` | `{hookName, numCommands, hookTypeCounts, pluginHookCounts}` |
| `tengu_repl_hook_finished` | `{hookName, numCommands, numSuccess, numBlocking, numNonBlockingError, numCancelled, totalDurationMs}` |
| `tengu_hook_created` | `{event, source, has_matcher}` |
| `tengu_hook_deleted` | `{event, source, has_matcher}` |
| `tengu_agent_stop_hook_success` | `{durationMs, turnCount}` |
| `tengu_agent_stop_hook_error` | `{durationMs, turnCount?, errorType}` |
| `tengu_agent_stop_hook_max_turns` | `{durationMs, turnCount}` |

---

## Common Patterns (from embedded docs)

### Auto-format after writes
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{ "type": "command", "command": "prettier --write \"$(jq -r '.tool_input.file_path' <<<\"$HOOK_INPUT\")\"" }]
    }]
  }
}
```

### Log bash commands
```bash
jq -r '"$(date) - \(.tool_input.command)"' >> ~/.claude/bash-command-log.txt
```

### Block dangerous patterns (PreToolUse, exit 2)
```bash
#!/bin/bash
INPUT=$(cat)
CMD=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
if echo "$CMD" | grep -q "rm -rf /"; then
  echo "Blocked: rm -rf /" >&2; exit 2
fi
```

### Inject additional context (PostToolUse)
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Remember to run tests after file changes."
  }
}
```

---

## Open Questions

1. **Agent hook turn distribution**: The 50-turn max is hardcoded. What's the typical turn count for stop condition verification in practice? (Telemetry fields exist but distribution data is not accessible. Requires Anthropic's internal telemetry data.)

---

## Resolved Questions (from safety analysis deep dive)

### Q1: Plugin hooks loading
Plugin manifests declare hooks via the `hooks` key. Plugin hooks are loaded via `h2$()` in `collectAllHooks (bj9)`. In managed-only mode (`qj()` / `allowManagedHooksOnly`), all plugin hooks are **silently skipped** — the `"pluginRoot" in E` check filters them out. Skill hooks via `g0D()` are similarly filtered.

### Q2: Hook model selection
Prompt and agent hooks use `getDefaultSmallModel (Y5)` which defaults to **Haiku 4.5** (cheapest model). Override via per-hook `model` field, `ANTHROPIC_SMALL_FAST_MODEL` env var, or `ANTHROPIC_DEFAULT_HAIKU_MODEL` env var. The hook model's decision is **authoritative** — the main model cannot override a hook's block decision.

### Q3: HTTP hooks status
HTTP hooks ARE implemented (not just a placeholder). They send hook input as HTTP POST body and parse JSON response. However, they are **blocked for `SessionStart` and `Setup` events** with the message: `"Skipping HTTP hook — HTTP hooks are not supported for {event}"`.

### Q31: `CLAUDE_ENV_FILE` format and usage
Points to a file containing shell environment variable assignments (plain text). Read at `SessionStart` and `Setup` via `readFile()`. The content is loaded and pushed into the hook environment. Also scans a directory (via `gAI()`) for additional env files matching a pattern. Used for environment bootstrapping — lets users provide env vars that hooks need without polluting the main shell environment.

### Q32: `CLAUDE_CODE_SHELL_PREFIX` scope
Applies broadly, **NOT just hooks**. It wraps commands in three contexts:
1. Hook shell commands via `executeShellHook (Av$)`
2. Bash tool commands
3. MCP server stdio process spawning

Uses `BG$(prefix, command)` to wrap. Intended for sandboxing wrappers like `firejail`, `sudo -u`, etc.

### Q33: `xHI(name)` — Tool alias mapping
Iterates the `OHI` alias map and returns all keys that map to a given tool variable. Example: for `_m` (TaskStop), returns `["KillShell"]`; for `Ym` (TaskOutput), returns `["AgentOutputTool", "BashOutputTool"]`. This affects hook regex matching — a PreToolUse hook matcher regex may match tool aliases the user doesn't expect.

### Q34: `updatedPermissions` abuse prevention
The `aEA()` function restricts which destinations accept persisted permissions: **only** `localSettings`, `userSettings`, or `projectSettings`. The `c1I()` persistence function also checks `lSH()` (a managed/locked settings check — if managed settings are locked, persistence is blocked). Additionally, the permission change schema (`bZA`) constrains format via Zod validation (must be `addRules` or `replaceRules` with proper rule format).

**However**, a compromised plugin hook CAN grant permissions via this path if managed mode is not enabled. The safeguard is: **policy hooks take precedence** (deny always wins over allow from other sources), and `allowManagedHooksOnly` in policy settings restricts which hooks run at all.

### Q35: MCP output replacement audit trail
The ONLY audit is the debug log line: `T(\`Hook ${E} (${getHookIdentifier(hook)}) replaced MCP tool output\`)`. The original MCP output is **NOT preserved** in the conversation transcript — it's overwritten in-place. There is no separate audit log or backup of pre-replacement output.

**Security note**: This means a malicious hook can silently alter MCP tool responses without leaving a forensic trail in the transcript. Only debug logs record the modification.

### Q36: Hook source trust model
The `mcA()` function controls hook source loading:
- If `policySettings.disableAllHooks === true`: returns `{}` (ALL hooks disabled)
- If `policySettings.allowManagedHooksOnly === true`: returns ONLY `policySettings.hooks` (user hooks excluded)
- If user settings has `disableAllHooks === true`: returns only policy hooks
- Otherwise: returns user settings hooks (from `xL().hooks`)

**In managed mode** (`allowManagedHooksOnly`), user hooks are NOT loaded — only policy hooks. A compromised `~/.claude/settings.json` cannot inject hooks when managed mode is active.
