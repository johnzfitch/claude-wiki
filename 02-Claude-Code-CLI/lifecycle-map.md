---
title: "Hook Lifecycle Map — Claude Code 2.1.59"
category: "02-Claude-Code-CLI"
tags: ["agents", "claude-code", "subagents"]
---

# Hook Lifecycle Map — Claude Code 2.1.59

Mapping every hook event to its position in the conversation/process lifecycle.

---

## 1. Full Process Lifetime

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PROCESS LIFETIME                                │
│                                                                     │
│  OS START                                                           │
│     │                                                               │
│     ▼                                                               │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  STARTUP PHASE  (main(), one-time)                           │   │
│  │                                                              │   │
│  │  1. setup()                                                  │   │
│  │       │                                                      │   │
│  │       ├── if --init flag:                                    │   │
│  │       │     [HOOK: Setup(trigger="init")]  ──────────────┐   │   │
│  │       │     [HOOK: SessionStart(source="startup")]       │   │   │
│  │       │     process.exit(0)                              │   │   │
│  │       │                                                  │   │   │
│  │       ├── if --maintenance flag:                         │   │   │
│  │       │     setupTrigger = "maintenance"                 │   │   │
│  │       │     (fired later in runHeadless)                 │   │   │
│  │       │                                                  │   │   │
│  │       └── normal interactive start:                      │   │   │
│  │             [HOOK: SessionStart(source="startup")]       │   │   │
│  │                                                          │   │   │
│  │  2. MCP servers connect                                  │   │   │
│  │  3. Plugins load                                         │   │   │
│  │  4. UI renders                                           │   │   │
│  └──────────────────────────────────────────────────────────┘   │   │
│     │                                                               │
│     ▼                                                               │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  SESSION (repeating turns — see Section 2)                   │   │
│  └──────────────────────────────────────────────────────────────┘   │
│     │                                                               │
│     │  background (any time):                                       │
│     │  ┌──────────────────────────────────────────────────────┐     │
│     │  │  [HOOK: ConfigChange]  ← file watcher fires          │     │
│     │  │  [HOOK: Notification]  ← permission/idle/auth events │     │
│     │  │  [HOOK: StatusLine]    ← periodic poll (continuous)  │     │
│     │  └──────────────────────────────────────────────────────┘     │
│     │                                                               │
│     ▼                                                               │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  SHUTDOWN  (SIGINT / SIGTERM / SIGHUP / /exit / /clear)      │   │
│  │                                                              │   │
│  │  tB(exitCode, reason, transcript)                            │   │
│  │    ├── await cleanup()                                       │   │
│  │    ├── [HOOK: SessionEnd(reason)]  ← last hook to run        │   │
│  │    │     reasons: clear | logout | prompt_input_exit | other │   │
│  │    └── process.exit()                                        │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Single Conversation Turn (Interactive REPL)

```
┌──────────────────────────────────────────────────────────────────────┐
│  CONVERSATION TURN                                                   │
│                                                                      │
│  USER INPUT                                                          │
│     │                                                                │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  UserPromptSubmit                                           │     │
│  │    stdin: { hook_event_name, prompt, ...base }              │     │
│  │                                                             │     │
│  │    exit 0  → stdout shown to Claude as context              │     │
│  │    exit 2  → BLOCK: erase prompt, show stderr to user       │     │──→ back to input
│  │    other   → show stderr to user, continue                  │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │  (if not blocked)                                              │
│     ▼                                                                │
│  ┌──────────────────────────────┐                                    │
│  │  MODEL STREAMING (API call)  │                                    │
│  │  Messages API → token stream │                                    │
│  └──────────────────────────────┘                                    │
│     │                                                                │
│     ├── if model emits tool_use blocks (may repeat N times):         │
│     │                                                                │
│     │   ┌────────────────────────────────────────────────────────┐   │
│     │   │  TOOL CALL CYCLE  (see Section 3)                      │   │
│     │   └────────────────────────────────────────────────────────┘   │
│     │     ↑                                                          │
│     │     └── loop: tool results injected, model called again        │
│     │                                                                │
│     ├── if model emits stop_reason = "end_turn":                     │
│     │                                                                │
│     │   ┌────────────────────────────────────────────────────────┐   │
│     │   │  Stop                                                  │   │
│     │   │    stdin: { hook_event_name, ...base }                 │   │
│     │   │    (last assistant message available in messages[])    │   │
│     │   │                                                        │   │
│     │   │    exit 0  → silent, Claude done                       │   │
│     │   │    exit 2  → reinject stderr to model, continue loop   │───→ back to API
│     │   │    other   → show stderr to user only                  │   │
│     │   └────────────────────────────────────────────────────────┘   │
│     │                                                                │
│     ▼                                                                │
│  RESPONSE RENDERED TO USER                                           │
│     │                                                                │
│     └─────────────────────────────────────────────────────────────   │
│                                             (next user input)        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 3. Tool Call Cycle (within a turn)

```
┌──────────────────────────────────────────────────────────────────────┐
│  TOOL CALL CYCLE                                                     │
│                                                                      │
│  Model emits tool_use { name, id, input }                            │
│     │                                                                │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  PreToolUse                                                 │     │
│  │    stdin: { tool_name, tool_input, tool_use_id, ...base }   │     │
│  │                                                             │     │
│  │    exit 0  → silent, continue                               │     │
│  │    exit 2  → BLOCK tool: show stderr to model               │──→ tool result = blocked error
│  │    other   → show stderr to user, continue                  │     │
│  │                                                             │     │
│  │    JSON output options:                                     │     │
│  │      permissionDecision: allow|deny|ask                     │     │
│  │      updatedInput: {...}  ← modify tool args                │     │
│  │      additionalContext: "..."  ← inject to Claude context   │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │  (if not blocked)                                              │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  Permission check                                           │     │
│  │  (if tool requires user approval)                           │     │
│  │                                                             │     │
│  │  ┌─────────────────────────────────────────────────────┐    │     │
│  │  │  PermissionRequest                                  │    │     │
│  │  │    stdin: { tool_name, tool_input, tool_use_id,     │    │     │
│  │  │             permission_suggestions, ...base }       │    │     │
│  │  │                                                     │    │     │
│  │  │    JSON hookSpecificOutput:                         │    │     │
│  │  │      decision.behavior: allow → skip dialog         │    │     │
│  │  │      decision.behavior: deny  → reject              │    │     │
│  │  │      decision.updatedInput    → modify args         │    │     │
│  │  │      decision.updatedPermissions → write rules      │    │     │
│  │  │                                                     │    │     │
│  │  │    Also fires:                                      │    │     │
│  │  │    [HOOK: Notification(notification_type=           │    │     │
│  │  │              "permission_prompt")]  ← parallel      │    │     │
│  │  └─────────────────────────────────────────────────────┘    │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │                                                                │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  TOOL EXECUTES                                              │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │                                                                │
│     ├── on SUCCESS:                                                  │
│     │   ┌─────────────────────────────────────────────────────────┐  │
│     │   │  PostToolUse                                            │  │
│     │   │    stdin: { tool_name, tool_input, tool_response,       │  │
│     │   │             tool_use_id, ...base }                      │  │
│     │   │                                                         │  │
│     │   │    exit 0  → stdout shown in transcript (ctrl+o)        │  │
│     │   │    exit 2  → show stderr to model immediately           │  │
│     │   │    other   → show stderr to user only                   │  │
│     │   │                                                         │  │
│     │   │    JSON output options:                                 │  │
│     │   │      additionalContext   ← inject to Claude context     │  │
│     │   │      updatedMCPToolOutput ← replace MCP response        │  │
│     │   └─────────────────────────────────────────────────────────┘  │
│     │                                                                │
│     └── on FAILURE / ERROR:                                          │
│         ┌─────────────────────────────────────────────────────────┐  │
│         │  PostToolUseFailure                                     │  │
│         │    stdin: { tool_name, tool_input, tool_use_id,         │  │
│         │             error, error_type, is_interrupt,            │  │
│         │             is_timeout, ...base }                       │  │
│         │                                                         │  │
│         │    exit 0  → stdout shown in transcript (ctrl+o)        │  │
│         │    exit 2  → show stderr to model immediately           │  │
│         │    other   → show stderr to user only                   │  │
│         └─────────────────────────────────────────────────────────┘  │
│                                                                      │
│  Tool result injected into messages → model called again             │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 4. Subagent (Task Tool) Lifecycle

```
┌──────────────────────────────────────────────────────────────────────┐
│  SUBAGENT LIFECYCLE  (Task tool call)                                │
│                                                                      │
│  Main agent calls Task tool                                          │
│     │                                                                │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  SubagentStart                                              │     │
│  │    stdin: { agent_id, agent_type, ...base }                 │     │
│  │    matcher: agent_type                                      │     │
│  │                                                             │     │
│  │    exit 0  → stdout shown to subagent as initial context    │     │
│  │    exit 2  → blocking (ignored, subagent starts anyway)     │     │
│  │    other   → show stderr to user only                       │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │                                                                │
│     ▼                                                                │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │  SUBAGENT RUNS its own conversation loop                     │    │
│  │  (same turn cycle as Section 2, same tool cycle as Section 3)│    │
│  │  SubagentStart fires for nested subagents recursively        │    │
│  └──────────────────────────────────────────────────────────────┘    │
│     │                                                                │
│     ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────┐     │
│  │  SubagentStop                                               │     │
│  │    stdin: { agent_id, agent_type,                           │     │
│  │             agent_transcript_path, ...base }                │     │
│  │    matcher: agent_type                                      │     │
│  │                                                             │     │
│  │    exit 0  → silent                                         │     │
│  │    exit 2  → show stderr to subagent, subagent continues    │──→ back to subagent loop
│  │    other   → show stderr to user only                       │     │
│  └─────────────────────────────────────────────────────────────┘     │
│     │                                                                │
│     ▼                                                                │
│  Task tool result returned to main agent                             │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Team / Multi-Agent Events

```
┌──────────────────────────────────────────────────────────────────────┐
│  TEAM EVENTS  (TeamCreate, multi-agent sessions)                     │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  TeammateIdle                                                  │  │
│  │    Fires: when a teammate's turn ends (goes idle)              │  │
│  │    stdin: { teammate_name, team_name, ...base }                │  │
│  │                                                                │  │
│  │    exit 0  → silent (teammate goes idle normally)              │  │
│  │    exit 2  → show stderr to teammate, PREVENT idle             │──→ teammate stays active
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  TaskCompleted                                                 │  │
│  │    Fires: when TaskUpdate sets status="completed"              │  │
│  │    stdin: { task_id, task_subject, task_description,           │  │
│  │             teammate_name, team_name, ...base }                │  │
│  │                                                                │  │
│  │    exit 0  → silent, task marked completed                     │  │
│  │    exit 2  → show stderr to model, PREVENT task completion     │──→ task stays in_progress
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 6. Session-Level Events (not per-turn)

```
┌──────────────────────────────────────────────────────────────────────┐
│  SESSION EVENTS                                                      │
│                                                                      │
│  SessionStart                                                        │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    matcher: source                                             │  │
│  │    source values:                                              │  │
│  │                                                                │  │
│  │      "startup"   → fresh `claude` invocation (interactive)     │  │
│  │      "resume"    → --resume or --continue                      │  │
│  │      "clear"     → /clear slash command                        │  │
│  │      "compact"   → post-compaction restart                     │  │
│  │                                                                │  │
│  │    exit 0  → stdout shown to Claude (as initial context)       │  │
│  │    exit 2  → blocked (ignored for SessionStart)                │  │
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  SessionEnd                                                          │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    matcher: reason                                             │  │
│  │    reason values:                                              │  │
│  │                                                                │  │
│  │      "clear"            → /clear command                       │  │
│  │      "logout"           → /logout command                      │  │
│  │      "prompt_input_exit"→ user typed /exit at prompt           │  │
│  │      "other"            → SIGINT/SIGTERM/SIGHUP/crash          │  │
│  │                                                                │  │
│  │    Called inside tB() (graceful shutdown) BEFORE process.exit  │  │
│  │    5s hard timeout on total shutdown; hook has this window     │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  Setup                                                               │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    matcher: trigger                                            │  │
│  │    trigger values:                                             │  │
│  │                                                                │  │
│  │      "init"        → claude --init  (one-time repo init)       │  │
│  │      "maintenance" → claude --maintenance (headless only)      │  │
│  │                                                                │  │
│  │    Called with forceSyncExecution=true                         │  │
│  │    CLAUDE_ENV_FILE injected into hook env                      │  │
│  │    exit 0  → stdout shown to Claude                            │  │
│  │    exit 2  → blocked (ignored for Setup)                       │  │
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  PreCompact                                                          │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    matcher: trigger                                            │  │
│  │    trigger values:                                             │  │
│  │                                                                │  │
│  │      "manual" → /compact slash command                         │  │
│  │      "auto"   → context window approaching limit               │  │
│  │                                                                │  │
│  │    exit 0  → stdout appended as CUSTOM COMPACT INSTRUCTIONS    │  │
│  │    exit 2  → BLOCK compaction entirely                         │  │
│  │    other   → show stderr to user, compact anyway               │  │
│  └────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 7. Background / Continuous Events

```
┌──────────────────────────────────────────────────────────────────────┐
│  BACKGROUND EVENTS  (not tied to turns)                              │
│                                                                      │
│  ConfigChange                                                        │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    Trigger: chokidar file watcher detects settings file change │  │
│  │    matcher: source                                             │  │
│  │    source values:                                              │  │
│  │      user_settings, project_settings, local_settings,          │  │
│  │      policy_settings, skills                                   │  │
│  │                                                                │  │
│  │    Fires asynchronously while session is running               │  │
│  │    MDM settings polled every 30min as fallback                 │  │
│  │                                                                │  │
│  │    exit 0  → allow the change to apply                         │  │
│  │    exit 2  → BLOCK change from being applied to session        │  │
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  Notification                                                        │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    matcher: notification_type                                  │  │
│  │    notification_type values:                                   │  │
│  │      "permission_prompt" → tool permission dialog shown        │  │
│  │      "idle_prompt"       → CC went idle (awaiting input)       │  │
│  │      "auth_success"      → OAuth login completed               │  │
│  │      "elicitation_dialog"→ elicitation UI shown                │  │
│  │                                                                │  │
│  │    Runs via JCH() (outside-REPL executor, non-blocking)        │  │
│  │    exit 0  → silent                                            │  │
│  │    other   → show stderr to user only                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  StatusLine  (not a hook event per se — special command)             │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    Config: { statusLine: { type: "command", command: "..." } } │  │
│  │    Polled continuously during session (periodic, 5s timeout)   │  │
│  │    stdout rendered in terminal status bar at bottom            │  │
│  │    Skipped if disableAllHooks=true                             │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  WorktreeCreate / WorktreeRemove  (VCS-agnostic isolation)           │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │    WorktreeCreate: fired by EnterWorktree tool                 │  │
│  │      stdin: { name: "suggested-slug", ...base }                │  │
│  │      stdout MUST be the absolute worktree path                 │  │
│  │      exit 0  → worktree created, path taken from stdout        │  │
│  │      other   → error, worktree creation fails                  │  │
│  │                                                                │  │
│  │    WorktreeRemove: when worktree is cleaned up                 │  │
│  │      stdin: { worktree_path: "/abs/path", ...base }            │  │
│  │      exit 0  → success                                         │  │
│  │      other   → show stderr to user only                        │  │
│  └────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 8. Complete Turn Timeline (annotated)

```
TIME
│
│  [PROCESS START]
│    │
│    ├─── Setup("init"|"maintenance")          ← only if --init/--maintenance
│    └─── SessionStart("startup"|"resume")     ← every session open
│
│  [TURN 1 begins]
│    │
│    ├─── UserPromptSubmit                      ← user hits enter
│    │         ↳ blocked? → show error, loop back
│    │
│    ├─── [MODEL API CALL 1]
│    │    │
│    │    ├─── tool_use emitted
│    │    │    ├── PreToolUse                   ← before execution
│    │    │    │       ↳ blocked? → inject error to model
│    │    │    │       ↳ updatedInput? → modify args
│    │    │    │
│    │    │    ├── PermissionRequest            ← if approval needed
│    │    │    │   + Notification("permission_prompt")
│    │    │    │
│    │    │    ├── [TOOL EXECUTES]
│    │    │    │
│    │    │    └── PostToolUse                  ← on success
│    │    │        PostToolUseFailure           ← on error
│    │    │
│    │    ├─── tool_use emitted (N more tools, same cycle)
│    │    │    ...
│    │    │
│    │    └─── stop_reason = "end_turn"
│    │         └── Stop                         ← after each model response
│    │                 ↳ exit 2? → reinject, API called again
│    │
│  [TURN 1 ends — response displayed]
│
│  [TURN 2 begins]
│    ├─── UserPromptSubmit
│    ...
│
│  [at any time during session]
│    ├─── ConfigChange                          ← settings file changed on disk
│    ├─── Notification                          ← idle/auth/elicitation events
│    └─── StatusLine                            ← polled continuously
│
│  [Task tool call — spawns subagent]
│    ├─── SubagentStart                         ← on spawn
│    │    └─── [SUBAGENT runs its own turn loop]
│    │         └─── SubagentStop               ← when subagent concludes
│    └─── Task tool result returned to parent
│
│  [Team multi-agent]
│    ├─── TeammateIdle                          ← teammate turn ends
│    └─── TaskCompleted                         ← TaskUpdate(status=completed)
│
│  [/compact or auto-compact]
│    └─── PreCompact                            ← before compaction
│         └─── SessionStart("compact")          ← after compaction restarts
│
│  [/clear]
│    └─── SessionEnd("clear")                   ← before clearing
│         └─── SessionStart("clear")            ← after clear
│
│  [PROCESS END]
│    └─── SessionEnd("other"|"logout"|"prompt_input_exit")
```

---

## 9. Hook Execution Contexts

Two execution paths exist in the code:

```
┌──────────────────────────────────────────────────────────────────────┐
│  REPL CONTEXT  (ay() generator — interactive & subagent loops)       │
│                                                                      │
│  Hooks:  PreToolUse, PostToolUse, PostToolUseFailure,                │
│          PermissionRequest, UserPromptSubmit, Stop, SubagentStop,    │
│          TeammateIdle, TaskCompleted, PreCompact                     │
│                                                                      │
│  Features available:                                                 │
│    - Yields progress/attachment messages to transcript               │
│    - Supports "prompt" and "agent" hook types (Stop only)            │
│    - Supports "function" hook type (Stop only)                       │
│    - additionalContext injected into Claude's messages               │
│    - updatedMCPToolOutput replaces MCP response in messages          │
│    - permissionBehavior controls tool approval                       │
│    - updatedInput modifies tool arguments                            │
│    - Runs hooks in parallel (wN$), collects all results              │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  OUTSIDE-REPL CONTEXT  (JCH() — non-interactive, background)         │
│                                                                      │
│  Hooks:  SessionStart, SessionEnd, Setup, SubagentStart,             │
│          Notification, ConfigChange, WorktreeCreate, WorktreeRemove, │
│          TeammateIdle (also runs outside REPL in some paths)         │
│                                                                      │
│  Limitations:                                                        │
│    - "prompt" and "agent" hook types NOT supported                   │
│    - "function" hook type causes error if reached                    │
│    - Returns flat array of results (not async generator)             │
│    - ConfigChange: policy_settings results always non-blocking       │
│    - Simpler result structure: { command, succeeded, output, blocked}│
└──────────────────────────────────────────────────────────────────────┘
```

---

## 10. Hook Firing Order within a Single Tool Call

```
Tool call received from model
         │
         ▼
┌──────────────────┐     blocked?
│   PreToolUse     │──────────────→ [inject blocking error as tool result]
│   (all hooks,    │                 model sees error, may retry or stop
│    parallel)     │
└──────────────────┘
         │
         │  updatedInput? → replace tool.input
         │  additionalContext? → prepend to next model message
         │  permissionDecision "deny"? → same as blocked
         │  permissionDecision "allow"? → skip permission dialog
         ▼
┌──────────────────┐
│PermissionRequest │     decision.behavior="deny"?
│ (if needed)      │──────────────→ [tool rejected, inject denial message]
│                  │
│ + Notification   │     decision.behavior="allow"?
│  ("permission_   │──────────────→ [skip dialog, run tool]
│   prompt")       │
└──────────────────┘
         │
         ▼
┌──────────────────┐
│  TOOL RUNS       │
└──────────────────┘
         │
    ┌────┴─────┐
    │          │
    ▼          ▼
┌────────┐  ┌──────────────────┐
│Success │  │ Failure/Error    │
│        │  │                  │
│PostTool│  │PostToolUseFailure│
│Use     │  │                  │
│        │  │ exit 2 → inject  │
│exit 2→ │  │ stderr to model  │
│inject  │  │                  │
│to model│  └──────────────────┘
└────────┘
         │
         │  updatedMCPToolOutput? → replace tool response in messages
         │  additionalContext? → prepend to next model message
         ▼
  [tool result injected into messages → model called again]
```

---

## 11. Special Case: Stop Hook Continuation Loop

The Stop hook is the only event that can force Claude to keep responding:

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  Claude sends stop_reason="end_turn"                                 │
│         │                                                            │
│         ▼                                                            │
│  ┌─────────────────────┐                                             │
│  │    Stop hook runs   │                                             │
│  │  (all hooks, REPL)  │                                             │
│  └─────────────────────┘                                             │
│         │                                                            │
│    ┌────┴──────────────────────────────────┐                         │
│    │                                       │                         │
│    ▼                                       ▼                         │
│  exit 0                                  exit 2                      │
│  (done)                         stderr injected as new               │
│                                 user message                         │
│                                         │                            │
│                                         ▼                            │
│                               Model API called again                 │
│                               [turn continues...]                    │
│                                         │                            │
│                               Claude responds again                  │
│                                         │                            │
│                               Stop hook runs again                   │
│                                         │                            │
│                               (loop until exit 0 or max_turns)       │
│                                                                      │
│  For "prompt" type Stop hooks:                                       │
│    → spawns sub-Claude with Read tool                                │
│    → evaluates condition against transcript                          │
│    → {ok: true} = pass (same as exit 0)                              │
│    → {ok: false} = fail (same as exit 2, injects reason)             │
│    → max 50 sub-turns, 30s timeout                                   │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Summary Table

| Hook | When in lifecycle | Blocks? | Can modify? | REPL only? |
|------|------------------|---------|-------------|------------|
| `Setup` | Before first turn (--init/--maintenance) | No | context only | No |
| `SessionStart` | Session opens | No | context only | No |
| `UserPromptSubmit` | Before each user prompt → model | Yes (erase prompt) | context only | Yes |
| `PreToolUse` | Before each tool runs | Yes | tool input | Yes |
| `PermissionRequest` | At tool permission dialog | Yes (deny) | tool input, rules | Yes |
| `PostToolUse` | After tool succeeds | No (exit 2 = inject) | MCP output | Yes |
| `PostToolUseFailure` | After tool errors | No (exit 2 = inject) | No | Yes |
| `Stop` | After each model end_turn | No (exit 2 = continue) | No | Yes |
| `SubagentStart` | Task tool spawns agent | No | context to agent | No |
| `SubagentStop` | Subagent concludes | Yes (exit 2 = continue) | No | Yes |
| `PreCompact` | Before /compact or auto-compact | Yes | compact instructions | Yes |
| `SessionEnd` | Process shutdown | No | No | No |
| `TeammateIdle` | Teammate turn ends | Yes (prevent idle) | No | Mixed |
| `TaskCompleted` | Task marked complete | Yes (prevent complete) | No | Yes |
| `ConfigChange` | Settings file changed on disk | Yes (block apply) | No | No |
| `Notification` | Notification events | No | No | No |
| `WorktreeCreate` | EnterWorktree tool | Yes (by failing) | stdout = path | No |
| `WorktreeRemove` | Worktree cleanup | No | No | No |
| `StatusLine` | Continuous poll | N/A | N/A | No |
