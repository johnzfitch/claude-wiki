# Claude Code Teammate/Team System Architecture

**Version**: 2.1.76
**Date**: 2026-03-14
**Purpose**: Complete reference for implementing teammate/team functionality in plugins

---

## Table of Contents

1. [Overview](#overview)
2. [Environment Variables](#environment-variables)
3. [CLI Flags](#cli-flags)
4. [Backend Architecture](#backend-architecture)
5. [Team Lifecycle](#team-lifecycle)
6. [Teammate Lifecycle](#teammate-lifecycle)
7. [Message Passing System](#message-passing-system)
8. [Task System Integration](#task-system-integration)
9. [Agent Tool Schema](#agent-tool-schema)
10. [TeamCreate Tool Schema](#teamcreate-tool-schema)
11. [SendMessage Tool Schema](#sendmessage-tool-schema)
12. [System Prompts](#system-prompts)
13. [Hooks](#hooks)
14. [File System Layout](#file-system-layout)
15. [Implementation Checklist](#implementation-checklist)

---

## Overview

The teammate/team system enables coordinated multi-agent workflows. The team lead (main session) spawns teammates that work in parallel, communicate via message passing, and coordinate through a shared task list.

### Key Concepts

- **Team Lead**: The main Claude Code session that creates and coordinates the team
- **Teammate**: A spawned agent running in a separate process (tmux pane, iTerm pane, or in-process)
- **Team Name**: Unique identifier for the team, used for task list and message routing
- **Message Queue**: File-based mailbox system for inter-agent communication
- **Task List**: Shared task tracking at `~/.claude/tasks/{team-name}/`
- **Team Config**: Configuration file at `~/.claude/teams/{team-name}/config.json`

### Execution Modes

| Mode | Description | When Used |
|------|-------------|-----------|
| `tmux` | Teammates spawn in tmux panes | Inside tmux session, or --teammate-mode=tmux |
| `iterm2` | Teammates spawn in iTerm2 split panes | Inside iTerm2 with it2 CLI installed |
| `in-process` | Teammates run in same process | Non-interactive sessions, or --teammate-mode=in-process |
| `auto` (default) | Selects tmux if inside tmux, else in-process | Adaptive to environment |

---

## Environment Variables

### `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`

**Required**: Must be set to `1` or `true` to enable team functionality.

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Without this, the TeamCreate, SendMessage, and team-related Agent parameters are unavailable.

### `CLAUDE_CODE_TEAMMATE_COMMAND`

**Purpose**: Override the command used to spawn teammate processes.

**Default**: Auto-detected from `process.execPath` or `process.argv[1]`.

**Usage**:
```bash
export CLAUDE_CODE_TEAMMATE_COMMAND="/path/to/custom-claude"
```

**Implementation**:
```javascript
function QCf() {
  if (process.env[W2H]) return process.env[W2H];
  return sM() ? process.execPath : process.argv[1];
}
```

### Environment Variables Passed to Teammates

When spawning teammates, these environment variables are preserved:

```javascript
const ME6 = [
  "CLAUDE_CODE_USE_BEDROCK",
  "CLAUDE_CODE_USE_VERTEX",
  "CLAUDE_CODE_USE_FOUNDRY",
  "ANTHROPIC_BASE_URL",
  "CLAUDE_CONFIG_DIR",
];
```

**Spawn Environment Template**:
```bash
CLAUDECODE=1 \
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 \
${preserved_vars} \
claude ${flags}
```
**Found variables of some sort?**
CLAUDE_CODE_TEAMMATE_COMMAND
TEAMMATE_SYSTEM_PROMPT_ADDENDUM

---

## CLI Flags

### `--teammate-mode <mode>`

**Values**: `auto` | `tmux` | `in-process`
**Default**: Captured from config at startup, stored in snapshot
**Purpose**: Force a specific teammate execution backend

**Example**:
```bash
claude --teammate-mode tmux
claude --teammate-mode in-process
```

**Snapshot Mechanism**:
```javascript
// Captured once at session start
function cCf() {
  if (AlH)  // CLI override takes precedence
    cMH = AlH;
  else
    cMH = O$().teammateMode ?? "auto";
}

// Retrieved throughout session
function LlH() {
  if (cMH === null)
    cCf();
  return cMH ?? "auto";
}
```

### Teammate Spawn Flags (auto-generated)

When spawning teammates, the following flags are auto-constructed:

```javascript
function lCf(H) {
  let $ = [];

  // Plan mode requirement
  if (H.planModeRequired) {
    // No flag needed - handled via message passing
  }

  // Permission mode
  else if (L === "bypassPermissions" || PLH())
    $.push("--dangerously-skip-permissions");
  else if (L === "acceptEdits")
    $.push("--permission-mode acceptEdits");

  // Model inheritance
  let D = eh();
  if (D) $.push(`--model ${zf([D])}`);

  // Settings file
  let f = Li();
  if (f) $.push(`--settings ${zf([f])}`);

  // Plugin directories
  let _ = qLH();
  for (let q of _) $.push(`--plugin-dir ${zf([q])}`);

  // Teammate mode
  let M = LlH();
  $.push(`--teammate-mode ${M}`);

  // Chrome mode
  let K = jvH();
  if (K === true) $.push("--chrome");
  else if (K === false) $.push("--no-chrome");

  return $.join(" ");
}
```

---

## Backend Architecture

### Backend Selection Logic

```javascript
async function XHH() {
  let insideTmux = await Wu();
  let inITerm2 = jHH();

  if (insideTmux) {
    // Inside tmux session - use tmux backend
    return { backend: new TmuxBackend(), isNative: true };
  }

  if (inITerm2) {
    if (!userPrefersTmux()) {
      let hasIt2 = await $lH();  // Check for it2 CLI
      if (hasIt2) {
        // iTerm2 with it2 CLI - native split panes
        return { backend: new ITermBackend(), isNative: true };
      }
    }

    let hasTmux = await IHH();
    if (hasTmux) {
      // iTerm2 fallback to tmux (recommend it2 installation)
      return { backend: new TmuxBackend(), isNative: false, needsIt2Setup: true };
    }

    throw Error("iTerm2 detected but it2 CLI not installed. Install it2 with: pip install it2");
  }

  // Not in tmux or iTerm2
  let hasTmux = await IHH();
  if (hasTmux) {
    return { backend: new TmuxBackend(), isNative: false };
  }

  throw Error("No pane backend available. Install tmux.");
}
```

### Backend Interfaces

All backends implement:

```typescript
interface TeammateBackend {
  type: "tmux" | "iterm2" | "in-process";
  displayName: string;
  supportsHideShow: boolean;

  isAvailable(): Promise<boolean>;
  isRunningInside(): Promise<boolean>;

  spawn(params: SpawnParams): Promise<SpawnResult>;
  sendMessage(agentId: string, message: Message): Promise<void>;
  terminate(agentId: string, reason: string): Promise<boolean>;
  kill(agentId: string): Promise<boolean>;
  isActive(agentId: string): Promise<boolean>;
}

interface SpawnParams {
  name: string;
  teamName: string;
  prompt: string;
  color: string;
  planModeRequired: boolean;
  model?: string;
  systemPrompt?: string;
  systemPromptMode?: "replace" | "append";
  permissions?: string[];
  allowPermissionPrompts?: boolean;
}

interface SpawnResult {
  success: boolean;
  agentId: string;
  taskId?: string;
  abortController?: AbortController;
  error?: string;
}
```

### TmuxBackend

**Pane Management**:
```javascript
class TmuxBackend {
  async createTeammatePaneWithLeader(name, color) {
    // Leader is in current window
    let currentPane = await this.getCurrentPaneId();
    let paneCount = await this.getCurrentWindowPaneCount();

    if (paneCount === 1) {
      // First teammate - split horizontally
      let paneId = await splitPane(currentPane, "-h", "-l", "70%");
    } else {
      // Subsequent teammates - balanced alternating splits
      let panes = await listPanes();
      let targetPane = selectBalancedPane(panes);
      let orientation = (panes.length % 2 === 1) ? "-v" : "-h";
      let paneId = await splitPane(targetPane, orientation);
    }

    await this.setPaneBorderColor(paneId, color);
    await this.setPaneTitle(paneId, name, color);
    await this.rebalancePanesWithLeader(window);

    return { paneId, isFirstTeammate };
  }

  async rebalancePanesWithLeader(window) {
    await selectLayout(window, "main-vertical");
    let leaderPane = getPanes()[0];
    await resizePane(leaderPane, "-x", "30%");
  }
}
```

### ITermBackend

**iTerm2 Split Pane Support**:
- Requires `it2` CLI tool (`pip install it2`)
- Uses iTerm2 Python API for native split panes
- Fallback to tmux if it2 unavailable

**Verification**:
```javascript
async function lbA() {
  // Verify it2 can communicate with iTerm2
  let result = await qA("it2", ["--version"]);
  if (result.code !== 0) {
    return { success: false, error: "it2 command failed" };
  }

  // Test iTerm2 Python API connection
  // (actual verification happens in it2 CLI)

  return { success: true };
}
```

### InProcessBackend

**In-Process Execution**:
```javascript
class InProcessBackend {
  type = "in-process";

  async spawn(params) {
    // Creates task in same process
    let result = await JJH({
      name: params.name,
      teamName: params.teamName,
      prompt: params.prompt,
      color: params.color,
      planModeRequired: params.planModeRequired,
    }, this.context);

    if (result.success) {
      // Start async execution
      tV$({
        identity: {
          agentId: result.agentId,
          agentName: params.name,
          teamName: params.teamName,
          color: params.color,
          planModeRequired: params.planModeRequired,
          parentSessionId: result.teammateContext.parentSessionId,
        },
        taskId: result.taskId,
        prompt: params.prompt,
        teammateContext: result.teammateContext,
        toolUseContext: { ...this.context, messages: [] },
        abortController: result.abortController,
        model: params.model,
        systemPrompt: params.systemPrompt,
        systemPromptMode: params.systemPromptMode,
        allowedTools: params.permissions,
        allowPermissionPrompts: params.allowPermissionPrompts,
      });
    }

    return result;
  }

  async sendMessage(agentId, message) {
    let { agentName, teamName } = RdH(agentId);
    await F6(agentName, {
      text: message.text,
      from: message.from,
      color: message.color,
      timestamp: message.timestamp ?? new Date().toISOString(),
    }, teamName);
  }

  async terminate(agentId, reason) {
    let task = pB(agentId, this.context.getAppState().tasks);
    if (!task) return false;
    if (task.shutdownRequested) return true;

    let requestId = `shutdown-${agentId}-${Date.now()}`;
    let shutdownMsg = Z2H({ requestId, from: "team-lead", reason });

    await F6(task.identity.agentName, {
      from: "team-lead",
      text: JSON.stringify(shutdownMsg),
      timestamp: new Date().toISOString(),
    }, task.identity.teamName);

    GVA(task.id, this.context.setAppState);  // Mark shutdown requested
    return true;
  }
}
```

---

## Team Lifecycle

### 1. Team Creation (TeamCreate)

**Tool Call**:
```json
{
  "team_name": "burn-ml-dev",
  "description": "Burn ML development team",
  "agent_type": "team-lead"
}
```

**Implementation**:
```javascript
async function call({ team_name, description, agent_type }, context) {
  let { setAppState, getAppState } = context;
  let state = getAppState();

  // Check for existing team
  if (state.teamContext?.teamName) {
    throw Error(`Already leading team "${teamName}". Use TeamDelete first.`);
  }

  let teamName = By6(team_name);  // Sanitize
  let leadAgentId = Lv("team-lead", teamName);  // team-lead@team-name
  let leadAgentType = agent_type || "team-lead";
  let model = w1(state.mainLoopModel);

  // Create team directory and config
  let teamDir = Dlf(teamName);  // ~/.claude/teams/{team-name}
  let configPath = path.join(teamDir, "config.json");

  let config = {
    name: teamName,
    description,
    createdAt: Date.now(),
    leadAgentId,
    leadSessionId: y$(),  // Current session ID
    members: [{
      agentId: leadAgentId,
      name: "team-lead",
      agentType: leadAgentType,
      model,
      joinedAt: Date.now(),
      tmuxPaneId: "",
      cwd: G$(),
      subscriptions: []
    }]
  };

  await my6(teamName, config);  // Write config file
  XVA(teamName);  // Register team

  // Create task list directory
  let taskListId = _UA(teamName);
  await aX$(taskListId);  // mkdir ~/.claude/tasks/{team-name}
  qrD(taskListId);  // Set as active task list

  // Update session state
  setAppState((state) => ({
    ...state,
    teamContext: {
      teamName,
      teamFilePath: configPath,
      leadAgentId,
      teammates: {
        [leadAgentId]: {
          name: "team-lead",
          agentType: leadAgentType,
          color: nQ(leadAgentId),
          tmuxSessionName: "",
          tmuxPaneId: "",
          cwd: G$(),
          spawnedAt: Date.now()
        }
      }
    }
  }));

  return {
    data: {
      team_name: teamName,
      team_file_path: configPath,
      lead_agent_id: leadAgentId
    }
  };
}
```

### 2. Team Deletion (TeamDelete)

**Tool Call**:
```json
{}  // No parameters - uses current team context
```

**Implementation**:
```javascript
async function call({}, context) {
  let { setAppState, getAppState } = context;
  let state = getAppState();

  if (!state.teamContext) {
    throw Error("No active team to delete");
  }

  let teamName = state.teamContext.teamName;

  // Check for active teammates
  let hasActiveTeammates = Object.values(state.tasks).some(task =>
    task.type === "in_process_teammate" && task.status === "running"
  );

  if (hasActiveTeammates) {
    throw Error("Cannot delete team with active teammates. Terminate teammates first.");
  }

  // Remove team directory
  let teamDir = Dlf(teamName);
  await rm(teamDir, { recursive: true });

  // Remove task directory
  let taskDir = QV(teamName);
  await rm(taskDir, { recursive: true });

  // Clear team context
  setAppState((state) => ({
    ...state,
    teamContext: null
  }));

  PrD();  // Clear task list override

  return {
    data: {
      success: true,
      team_name: teamName,
      message: `Team "${teamName}" deleted`
    }
  };
}
```

---

## Teammate Lifecycle

### 1. Spawning a Teammate

**Agent Tool Call (with team parameters)**:
```json
{
  "name": "researcher",
  "team_name": "burn-ml-dev",
  "prompt": "Research latest Burn framework features",
  "description": "Research Burn features",
  "subagent_type": "general-purpose",
  "mode": "acceptEdits"
}
```

**Spawn Flow**:
```javascript
async function yuf({ name, prompt, description, team_name, plan_mode_required, model, agent_type }, context) {
  let teamName = team_name || r1();  // Current team or explicit

  if (!teamName) {
    throw Error("team_name required when spawning teammates");
  }

  // Validate: teammates can't spawn teammates (flat roster)
  if (fM() && teamName && name) {
    throw Error("Teammates cannot spawn other teammates. Omit 'name' parameter for subagent.");
  }

  // Get or detect backend
  let backend = await XE6(true);  // true = prefer in-process if available

  // Spawn via backend
  let result = await backend.spawn({
    name,
    teamName,
    prompt,
    color: agentDef?.color || nQ(name),
    planModeRequired: plan_mode_required,
    model,
    systemPrompt: agentDef?.getSystemPrompt(),
    systemPromptMode: "append",
    permissions: agentDef?.tools || ["*"],
    allowPermissionPrompts: true,
  });

  if (!result.success) {
    return { data: { error: result.error } };
  }

  // Register agent name -> agentId mapping
  context.setAppState((state) => {
    let registry = new Map(state.agentNameRegistry);
    registry.set(name, SP(result.agentId));
    return { ...state, agentNameRegistry: registry };
  });

  return {
    data: {
      status: "teammate_spawned",
      agentId: result.agentId,
      name,
      team_name: teamName,
      prompt
    }
  };
}
```

### 2. Teammate Main Loop (In-Process)

**Execution Pattern**:
```javascript
async function LE6(params) {
  let { identity, taskId, prompt, teammateContext, toolUseContext, abortController } = params;

  // Set teammate context for this async execution
  await QX$(teammateContext, async () => {

    // Initialize with team lead's message
    let initialMessage = UbA("team-lead", prompt);
    let messages = [U$({ content: initialMessage })];

    // Main work loop
    while (!abortController.signal.aborted) {

      // Execute agent turn
      let turnMessages = [];
      for await (let msg of Fy({
        agentDefinition,
        promptMessages: messages,
        toolUseContext,
        canUseTool,
        isAsync: true,
        forkContextMessages: compactedHistory,
        querySource: "agent:custom",
        override: { abortController },
        model,
        preserveToolUseResults: true,
        availableTools: toolUseContext.options.tools,
        allowedTools: permissions,
      })) {
        if (abortController.signal.aborted) break;

        turnMessages.push(msg);
        messages.push(msg);

        // Update task progress
        updateTaskProgress(taskId, msg);
      }

      // Mark idle
      setTaskIdle(taskId);

      // Send idle notification
      await mCf(identity.agentName, identity.color, identity.teamName, {
        idleReason: "available",
        summary: RQH(turnMessages)
      });

      // Wait for next work
      let nextWork = await AE6(identity, abortController, taskId, getAppState, setAppState, parentSessionId);

      switch (nextWork.type) {
        case "shutdown_request":
          // Inject shutdown message into conversation
          let shutdownMsg = UbA(nextWork.request.from, nextWork.originalMessage);
          messages.push(U$({ content: shutdownMsg }));
          break;

        case "new_message":
          // Inject new message into conversation
          if (nextWork.from === "user") {
            messages.push(U$({ content: nextWork.message }));
          } else {
            let teammateMsg = UbA(nextWork.from, nextWork.message, nextWork.color, nextWork.summary);
            messages.push(U$({ content: teammateMsg }));
          }
          break;

        case "aborted":
          return;  // Exit loop
      }
    }
  });
}
```

### 3. Waiting for Messages (Polling Loop)

**Message Queue Polling**:
```javascript
async function AE6(identity, abortController, taskId, getAppState, setAppState, parentSessionId) {
  let pollCount = 0;

  while (!abortController.signal.aborted) {

    // Check for pending user messages (queued via SendMessage to non-running agent)
    let task = getAppState().tasks[taskId];
    if (task?.type === "in_process_teammate" && task.pendingUserMessages.length > 0) {
      let message = task.pendingUserMessages[0];
      setAppState((state) => {
        let task = state.tasks[taskId];
        return {
          ...state,
          tasks: {
            ...state.tasks,
            [taskId]: {
              ...task,
              pendingUserMessages: task.pendingUserMessages.slice(1)
            }
          }
        };
      });
      return { type: "new_message", message, from: "user" };
    }

    if (pollCount > 0) await sleep(500);
    pollCount++;

    // Check mailbox
    let mailbox = await BQ(identity.agentName, identity.teamName);

    // Priority 1: Shutdown requests (always first)
    for (let i = 0; i < mailbox.length; i++) {
      let msg = mailbox[i];
      if (!msg.read) {
        let shutdownReq = fHH(msg.text);  // Parse shutdown_request JSON
        if (shutdownReq) {
          await vQH(identity.agentName, identity.teamName, i);  // Mark read
          return {
            type: "shutdown_request",
            request: shutdownReq,
            originalMessage: msg.text
          };
        }
      }
    }

    // Priority 2: Messages from team lead
    let leaderMsgIdx = mailbox.findIndex(msg => !msg.read && msg.from === "team-lead");

    // Priority 3: Any unread message
    if (leaderMsgIdx === -1) {
      leaderMsgIdx = mailbox.findIndex(msg => !msg.read);
    }

    if (leaderMsgIdx !== -1) {
      let msg = mailbox[leaderMsgIdx];
      await vQH(identity.agentName, identity.teamName, leaderMsgIdx);  // Mark read
      return {
        type: "new_message",
        message: msg.text,
        from: msg.from,
        color: msg.color,
        summary: msg.summary
      };
    }

    // Check for available tasks
    let taskPrompt = await BCf(parentSessionId, identity.agentName);
    if (taskPrompt) {
      return { type: "new_message", message: taskPrompt, from: "task-list" };
    }
  }

  return { type: "aborted" };
}
```

**Task Auto-Claiming**:
```javascript
async function BCf(taskListId, agentName) {
  try {
    let tasks = await uI(taskListId);
    let availableTask = HE6(tasks);  // Find unblocked, unowned task

    if (!availableTask) return null;

    // Claim task
    let result = await QEA(taskListId, availableTask.id, agentName);
    if (!result.success) return null;

    // Mark in-progress
    await DC(taskListId, availableTask.id, { status: "in_progress" });

    // Return prompt
    return $E6(availableTask);  // "Complete task #N: subject\n\ndescription"
  } catch (error) {
    return null;
  }
}

function HE6(tasks) {
  let pendingIds = new Set(
    tasks.filter(t => t.status !== "completed").map(t => t.id)
  );

  return tasks.find(t => {
    if (t.status !== "pending") return false;
    if (t.owner) return false;  // Already claimed
    // Unblocked = all blockedBy tasks are completed
    return t.blockedBy.every(id => !pendingIds.has(id));
  });
}
```

### 4. Idle Notifications

**Idle Notification Structure**:
```javascript
async function mCf(agentName, color, teamName, metadata) {
  let notification = VQH(agentName, metadata);
  await s26(agentName, JSON.stringify(notification), color, teamName);
}

function VQH(agentName, metadata) {
  return {
    type: "idle_notification",
    agent_name: agentName,
    idle_reason: metadata.idleReason,  // "available" | "interrupted" | "failed"
    summary: metadata.summary,  // Last work summary
    completed_status: metadata.completedStatus,  // "completed" | "failed"
    failure_reason: metadata.failureReason,
    timestamp: new Date().toISOString()
  };
}
```

**Sent to team lead via**:
```javascript
async function s26(agentName, messageText, color, teamName) {
  await F6("team-lead", {
    from: agentName,
    text: messageText,
    timestamp: new Date().toISOString(),
    color
  }, teamName);
}
```

### 5. Graceful Shutdown

**Shutdown Request**:
```javascript
// Via SendMessage tool
{
  "to": "researcher",
  "message": {
    "type": "shutdown_request",
    "reason": "Work complete"
  }
}
```

**Shutdown Flow**:
1. Team lead calls `SendMessage` with `shutdown_request`
2. Message written to teammate's mailbox
3. Teammate's poll loop prioritizes shutdown messages
4. Shutdown message injected into conversation:
   ```
   Message from team-lead:
   {"type": "shutdown_request", "requestId": "shutdown-...", "from": "team-lead", "reason": "Work complete"}
   ```
5. Teammate processes shutdown, responds with `shutdown_response`:
   ```json
   {
     "type": "shutdown_response",
     "request_id": "shutdown-...",
     "approve": true
   }
   ```
6. Teammate exits main loop, marks task completed

---

## Message Passing System

### Mailbox File Structure

**Location**: `~/.claude/teams/{team-name}/mailbox/{agent-name}.json`

**Schema**:
```json
[
  {
    "id": "msg-1234567890-abc",
    "from": "team-lead",
    "text": "Start working on task #1",
    "color": "#3b82f6",
    "summary": "Assign task #1",
    "timestamp": "2026-03-14T12:34:56.789Z",
    "read": false
  },
  {
    "id": "msg-1234567891-def",
    "from": "researcher",
    "text": "Starting research on Burn features",
    "color": "#10b981",
    "timestamp": "2026-03-14T12:35:01.234Z",
    "read": true
  }
]
```

### Message Queue Operations

**Send Message (F6)**:
```javascript
async function F6(recipientName, message, teamName) {
  let mailboxPath = getMailboxPath(teamName, recipientName);

  // Lock mailbox file
  let lock = await acquireLock(mailboxPath);

  try {
    // Read existing messages
    let messages = [];
    try {
      let content = await readFile(mailboxPath, "utf-8");
      messages = JSON.parse(content);
    } catch (e) {
      // File doesn't exist yet
    }

    // Append new message
    let newMessage = {
      id: generateMessageId(),
      from: message.from,
      text: message.text,
      color: message.color,
      summary: message.summary,
      timestamp: message.timestamp,
      read: false
    };

    messages.push(newMessage);

    // Write back
    await writeFile(mailboxPath, JSON.stringify(messages, null, 2));

  } finally {
    await lock.release();
  }
}
```

**Read Mailbox (BQ)**:
```javascript
async function BQ(agentName, teamName) {
  let mailboxPath = getMailboxPath(teamName, agentName);

  try {
    let content = await readFile(mailboxPath, "utf-8");
    return JSON.parse(content);
  } catch (e) {
    if (e.code === "ENOENT") return [];
    throw e;
  }
}
```

**Mark Message Read (vQH)**:
```javascript
async function vQH(agentName, teamName, messageIndex) {
  let mailboxPath = getMailboxPath(teamName, agentName);
  let lock = await acquireLock(mailboxPath);

  try {
    let messages = JSON.parse(await readFile(mailboxPath, "utf-8"));

    if (messageIndex < messages.length) {
      messages[messageIndex].read = true;
      await writeFile(mailboxPath, JSON.stringify(messages, null, 2));
    }
  } finally {
    await lock.release();
  }
}
```

### Message Formatting

**Teammate Message Format** (UbA):
```javascript
function UbA(from, text, color, summary) {
  let header = `Message from ${from}`;
  if (summary) header += ` (${summary})`;
  header += `:`;

  return `${header}\n${text}`;
}

// Example output:
// Message from researcher (Research complete):
// I've analyzed the latest Burn 0.20 features. Here's what I found...
```

---

## Task System Integration

### Task List Location

**Directory**: `~/.claude/tasks/{team-name}/`
**Files**: `{task-id}.json` (e.g., `1.json`, `2.json`)

### Task Schema

```typescript
interface Task {
  id: string;
  subject: string;
  description?: string;
  status: "pending" | "in_progress" | "completed";
  owner?: string;  // Agent name who claimed it
  blockedBy: string[];  // Task IDs that must complete first
  blocks: string[];  // Task IDs blocked by this
  createdAt: number;
  updatedAt: number;
  completedAt?: number;
}
```

### Task Operations

**Create Task**:
```javascript
async function tX$(taskListId, task) {
  let lock = await acquireLock(taskListId);
  try {
    let nextId = await mB1(taskListId);  // Get max task ID
    let newId = String(nextId + 1);
    let taskPath = epH(taskListId, newId);

    let taskData = {
      id: newId,
      ...task,
      createdAt: Date.now(),
      updatedAt: Date.now()
    };

    await writeFile(taskPath, JSON.stringify(taskData, null, 2));
    fs();  // Trigger task list watchers

    return newId;
  } finally {
    await lock.release();
  }
}
```

**Update Task**:
```javascript
async function DC(taskListId, taskId, updates) {
  let task = await am(taskListId, taskId);  // Read current
  if (!task) return null;

  let updated = {
    ...task,
    ...updates,
    id: taskId,  // Ensure ID doesn't change
    updatedAt: Date.now()
  };

  if (updates.status === "completed" && !task.completedAt) {
    updated.completedAt = Date.now();
  }

  let taskPath = epH(taskListId, taskId);
  await writeFile(taskPath, JSON.stringify(updated, null, 2));
  fs();  // Trigger watchers

  return updated;
}
```

**List Tasks**:
```javascript
async function uI(taskListId) {
  let taskDir = QV(taskListId);
  let files = await readdir(taskDir);

  let tasks = [];
  for (let file of files) {
    if (!file.endsWith(".json")) continue;
    if (file.startsWith(".")) continue;

    let taskId = file.replace(".json", "");
    let task = await am(taskListId, taskId);
    if (task) tasks.push(task);
  }

  return tasks.sort((a, b) => parseInt(a.id) - parseInt(b.id));
}
```

### Task Tool Integration

**TaskCreate, TaskUpdate, TaskList tools** automatically use:
```javascript
function R2() {
  // Explicit override
  if (process.env.CLAUDE_CODE_TASK_LIST_ID) {
    return process.env.CLAUDE_CODE_TASK_LIST_ID;
  }

  // In-process teammate context
  let teammateCtx = IY();
  if (teammateCtx) return teammateCtx.teamName;

  // Current team context
  return r1() || tpH || y$();
}
```

This ensures teammates and team lead share the same task list.

---

## Agent Tool Schema

**Input Schema (with teammate parameters)**:
```typescript
{
  // Standard agent params
  description: string,  // "Research Burn features"
  prompt: string,       // "Analyze latest Burn 0.20 features"
  subagent_type?: string,  // "general-purpose"
  model?: "sonnet" | "opus" | "haiku",
  resume?: string,      // Agent ID to resume
  run_in_background?: boolean,

  // Teammate-specific params (when EXPERIMENTAL_AGENT_TEAMS=1)
  name?: string,        // "researcher" - makes it a teammate
  team_name?: string,   // "burn-ml-dev" - which team to join
  mode?: "plan" | "acceptEdits" | "default",  // Permission mode

  // Isolation (not typically used with teammates)
  isolation?: "worktree",
  cwd?: string
}
```

**Output Schema**:
```typescript
{
  // For teammates
  status: "teammate_spawned",
  agentId: string,  // "researcher@burn-ml-dev"
  name: string,     // "researcher"
  team_name: string,  // "burn-ml-dev"
  prompt: string
}

// OR for async background agents
{
  status: "async_launched",
  agentId: string,
  description: string,
  prompt: string,
  outputFile: string,
  canReadOutputFile: boolean
}

// OR for completed sync agents
{
  status: "completed",
  agentId: string,
  prompt: string,
  content: Array<{ type: "text", text: string }>,
  totalToolUseCount: number,
  totalDurationMs: number,
  totalTokens: number,
  usage: {...}
}
```

**Teammate Detection Logic**:
```javascript
// Is this a teammate spawn?
let isTeammateSpawn = !!(team_name && name);

if (isTeammateSpawn) {
  // Validate: teammates can't spawn teammates
  if (fM()) {
    throw Error("Teammates cannot spawn other teammates. Omit 'name' for subagent.");
  }

  // Spawn via backend
  return await yuf({ name, prompt, team_name, ... }, context);
}
```

---

## TeamCreate Tool Schema

**Input Schema**:
```typescript
{
  team_name: string,     // "burn-ml-dev" (required)
  description?: string,  // "Burn ML development team"
  agent_type?: string    // "team-lead" (defaults to "team-lead")
}
```

**Output Schema**:
```typescript
{
  team_name: string,       // "burn-ml-dev"
  team_file_path: string,  // "/home/user/.claude/teams/burn-ml-dev/config.json"
  lead_agent_id: string    // "team-lead@burn-ml-dev"
}
```

**Validation**:
- `team_name` cannot be empty
- Cannot create team if already leading a team
- Team name is sanitized: `team_name.replace(/[^a-zA-Z0-9]/g, "-").toLowerCase()`

---

## SendMessage Tool Schema

**Input Schema**:
```typescript
{
  to: string,  // Recipient name or "*" for broadcast
  message: string | ProtocolMessage,
  summary?: string  // Required for string messages, shown in UI
}

type ProtocolMessage =
  | { type: "shutdown_request", reason?: string }
  | { type: "shutdown_response", request_id: string, approve: boolean, reason?: string }
  | { type: "plan_approval_response", request_id: string, approve: boolean, feedback?: string };
```

**Examples**:

Plain text message:
```json
{
  "to": "researcher",
  "message": "Start working on task #1",
  "summary": "Assign task #1"
}
```

Broadcast:
```json
{
  "to": "*",
  "message": "Critical blocking issue - stop all work",
  "summary": "Critical issue found"
}
```

Shutdown request:
```json
{
  "to": "researcher",
  "message": {
    "type": "shutdown_request",
    "reason": "Work complete"
  }
}
```

Shutdown response (teammate to team-lead):
```json
{
  "to": "team-lead",
  "message": {
    "type": "shutdown_response",
    "request_id": "shutdown-researcher@burn-ml-dev-1234567890",
    "approve": true
  }
}
```

**Validation**:
- `to` cannot be empty
- `to` cannot contain "@" (one team per session)
- `summary` required for string messages
- Structured messages cannot be broadcast (`to: "*"`)
- `shutdown_response` must go to "team-lead"
- Rejecting shutdown requires `reason`

**Output Schema**:
```typescript
{
  success: boolean,
  message?: string  // Status or error message
}
```

---

## System Prompts

### TEAMMATE_SYSTEM_PROMPT_ADDENDUM

**Added to in-process teammates only**:

```markdown
# Agent Teammate Communication

IMPORTANT: You are running as an agent in a team. To communicate with anyone on your team:
- Use the SendMessage tool with `to: "<name>"` to send messages to specific teammates
- Use the SendMessage tool with `to: "*"` sparingly for team-wide broadcasts

Just writing a response in text is not visible to others on your team - you MUST use the SendMessage tool.

The user interacts primarily with the team lead. Your work is coordinated through the task system and teammate messaging.
```

**Injection Point**:
```javascript
async function LE6(params) {
  let systemPromptParts = [
    ...await cX(toolUseContext.options.tools, model, undefined, mcpClients),
    xbA  // TEAMMATE_SYSTEM_PROMPT_ADDENDUM
  ];

  if (agentDefinition) {
    let customPrompt = agentDefinition.getSystemPrompt();
    if (customPrompt) {
      systemPromptParts.push(`\n# Custom Agent Instructions\n${customPrompt}`);
    }
  }

  let systemPrompt = systemPromptParts.join("\n");

  // Use systemPrompt for execution...
}
```

### Team Lead Prompt Additions

**Agent Tool Prompt** (includes team instructions):

```markdown
# TeamCreate

## When to Use

Use this tool proactively whenever:
- The user explicitly asks to use a team, swarm, or group of agents
- The user mentions wanting agents to work together, coordinate, or collaborate
- A task is complex enough that it would benefit from parallel work by multiple agents

When in doubt about whether a task warrants a team, prefer spawning a team.

## Choosing Agent Types for Teammates

When spawning teammates via the Agent tool, choose the `subagent_type` based on what tools the agent needs for its task:

- **Read-only agents** (e.g., Explore, Plan) cannot edit or write files. Only assign them research, search, or planning tasks.
- **Full-capability agents** (e.g., general-purpose) have access to all tools including file editing, writing, and bash.
- **Custom agents** defined in `.claude/agents/` may have their own tool restrictions.

Always review the agent type descriptions and their available tools before selecting a `subagent_type`.

## Team Workflow

1. **Create a team** with TeamCreate - this creates both the team and its task list
2. **Create tasks** using the Task tools (TaskCreate, TaskList, etc.)
3. **Spawn teammates** using the Agent tool with `team_name` and `name` parameters
4. **Assign tasks** using TaskUpdate with `owner` to give tasks to idle teammates
5. **Teammates work on assigned tasks** and mark them completed via TaskUpdate
6. **Teammates go idle between turns** - Be patient! Don't comment on their idleness until it impacts work.
7. **Shutdown your team** - gracefully shut down teammates via SendMessage with `message: {type: "shutdown_request"}`

## Task List Coordination

Teams share a task list at `~/.claude/tasks/{team-name}/`.

Teammates should:
1. Check TaskList periodically, especially after completing each task
2. Claim unassigned, unblocked tasks with TaskUpdate (set `owner` to your name)
3. **Prefer tasks in ID order** (lowest ID first) when multiple available
4. Create new tasks with TaskCreate when identifying additional work
5. Mark tasks completed with TaskUpdate when done, then check for next work
6. If all available tasks are blocked, notify the team lead or help resolve blocking tasks

**IMPORTANT**:
- Do not use terminal tools to view your team's activity; always send messages
- Your team cannot hear you if you don't use SendMessage
- Do NOT send structured JSON like `{"type":"idle",...}` manually - the system sends these automatically
- Use TaskUpdate to mark tasks completed
- The system automatically sends idle notifications when teammates stop
```

---

## Hooks

### New Hook Events (2.1.70+)

**TeammateIdle**:
```typescript
{
  type: "TeammateIdle",
  agentName: string,
  idleReason: "available" | "interrupted" | "failed",
  summary?: string,
  completedStatus?: "completed" | "failed",
  failureReason?: string
}
```

**TaskCompleted**:
```typescript
{
  type: "TaskCompleted",
  taskId: string,
  status: "completed" | "failed",
  owner?: string
}
```

**Elicitation** / **ElicitationResult**:
```typescript
{
  type: "Elicitation",
  prompt: string,
  agentName?: string
}

{
  type: "ElicitationResult",
  response: string,
  agentName?: string
}
```

### Hook Configuration

**settings.json**:
```json
{
  "hooks": {
    "TeammateIdle": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Teammate ${AGENT_NAME} is idle: ${IDLE_REASON}'"
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Task ${TASK_ID} completed by ${OWNER}'"
          }
        ]
      }
    ]
  }
}
```

---

## File System Layout

```
~/.claude/
├── teams/
│   └── {team-name}/
│       ├── config.json          # Team configuration
│       └── mailbox/
│           ├── team-lead.json   # Team lead's mailbox
│           ├── researcher.json  # Researcher's mailbox
│           └── tester.json      # Tester's mailbox
│
└── tasks/
    └── {team-name}/
        ├── .next-id             # Next task ID counter
        ├── 1.json               # Task #1
        ├── 2.json               # Task #2
        └── 3.json               # Task #3
```

### Team Config Schema

**`~/.claude/teams/{team-name}/config.json`**:
```json
{
  "name": "burn-ml-dev",
  "description": "Burn ML development team",
  "createdAt": 1710432000000,
  "leadAgentId": "team-lead@burn-ml-dev",
  "leadSessionId": "session-abc123",
  "members": [
    {
      "agentId": "team-lead@burn-ml-dev",
      "name": "team-lead",
      "agentType": "team-lead",
      "model": "claude-sonnet-4-6",
      "joinedAt": 1710432000000,
      "tmuxPaneId": "",
      "cwd": "/home/user/project",
      "subscriptions": []
    },
    {
      "agentId": "researcher@burn-ml-dev",
      "name": "researcher",
      "agentType": "general-purpose",
      "model": "claude-sonnet-4-6",
      "joinedAt": 1710432060000,
      "tmuxPaneId": "%42",
      "cwd": "/home/user/project",
      "subscriptions": []
    }
  ]
}
```

---

## Implementation Checklist

### For Plugin Authors Implementing Teammate Functionality

#### 1. Environment Setup
- [ ] Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in plugin environment
- [ ] Optionally set `CLAUDE_CODE_TEAMMATE_COMMAND` for custom spawn command
- [ ] Preserve required env vars when spawning (`CLAUDE_CODE_USE_*`, `ANTHROPIC_BASE_URL`, etc.)

#### 2. Backend Selection
- [ ] Implement backend detection logic (`XHH()`)
- [ ] Support at least one backend (tmux, iTerm2, or in-process)
- [ ] Handle `--teammate-mode` CLI flag
- [ ] Capture teammate mode at session start (snapshot pattern)

#### 3. Team Management
- [ ] Implement `TeamCreate` tool
  - Create team directory: `~/.claude/teams/{team-name}/`
  - Write config.json with team metadata
  - Create task list directory: `~/.claude/tasks/{team-name}/`
  - Update session state with `teamContext`
- [ ] Implement `TeamDelete` tool
  - Validate no active teammates
  - Remove team and task directories
  - Clear session `teamContext`

#### 4. Teammate Spawning
- [ ] Extend `Agent` tool with teammate parameters:
  - `name` (teammate identifier)
  - `team_name` (which team to join)
  - `mode` (permission mode)
- [ ] Implement spawn via selected backend
- [ ] Register agent name → agentId mapping
- [ ] Handle teammate-specific system prompt injection

#### 5. Message Passing
- [ ] Implement `SendMessage` tool
  - Support direct messages (`to: "name"`)
  - Support broadcast (`to: "*"`)
  - Support protocol messages (shutdown, plan approval)
- [ ] Implement mailbox file I/O:
  - `F6()` - send message
  - `BQ()` - read mailbox
  - `vQH()` - mark message read
- [ ] Implement message queue polling (`AE6()`)
- [ ] Handle shutdown request/response protocol

#### 6. Task Integration
- [ ] Use shared task list based on team context (`R2()`)
- [ ] Implement task auto-claiming for idle teammates (`BCf()`)
- [ ] Prioritize tasks by ID (lowest first)
- [ ] Check for unblocked tasks

#### 7. Idle Notifications
- [ ] Send idle notifications after each work cycle (`mCf()`)
- [ ] Include idle reason, summary, completion status
- [ ] Send to team lead's mailbox

#### 8. Lifecycle Management
- [ ] Implement teammate main loop (`LE6()`)
- [ ] Handle graceful shutdown via shutdown_request
- [ ] Clean up task state on completion/failure
- [ ] Handle abort signals properly

#### 9. Hooks
- [ ] Trigger `TeammateIdle` hook after idle notification
- [ ] Trigger `TaskCompleted` hook after task marked done
- [ ] Support hook configuration in settings.json

#### 10. Testing
- [ ] Test tmux backend (if supported)
- [ ] Test in-process backend
- [ ] Test message passing between teammates
- [ ] Test task claiming and completion
- [ ] Test graceful shutdown flow
- [ ] Test error handling (teammate crashes, network issues)

---

## Example: Burn ML Development Team

### Setup

```javascript
// 1. Create team
await TeamCreate({
  team_name: "burn-ml-dev",
  description: "Burn ML framework development team",
  agent_type: "burn-architect"
});

// 2. Create tasks
await TaskCreate({
  subject: "Research Burn 0.20 features",
  description: "Analyze latest Burn release notes and API changes",
  status: "pending"
});

await TaskCreate({
  subject: "Implement training loop",
  description: "Create trainer using new Learner API",
  status: "pending",
  blockedBy: ["1"]  // Blocked by research task
});

await TaskCreate({
  subject: "Write tests",
  description: "Add unit tests for training loop",
  status: "pending",
  blockedBy: ["2"]  // Blocked by implementation
});

// 3. Spawn teammates
await Agent({
  name: "researcher",
  team_name: "burn-ml-dev",
  subagent_type: "general-purpose",
  prompt: "You are a Burn framework researcher. Check TaskList for work.",
  description: "Research Burn features"
});

await Agent({
  name: "implementer",
  team_name: "burn-ml-dev",
  subagent_type: "general-purpose",
  prompt: "You are a Burn implementer. Check TaskList for work.",
  description: "Implement training code"
});

await Agent({
  name: "tester",
  team_name: "burn-ml-dev",
  subagent_type: "general-purpose",
  prompt: "You are a test engineer. Check TaskList for work.",
  description: "Write tests"
});
```

### Workflow

1. **Researcher** starts, checks TaskList, claims task #1
2. **Researcher** completes research, marks task #1 completed
3. **Implementer** (now unblocked) claims task #2
4. **Implementer** sends message: `SendMessage({ to: "researcher", message: "What API should I use for optimizer?" })`
5. **Researcher** responds with details
6. **Implementer** completes task #2
7. **Tester** (now unblocked) claims task #3
8. **Tester** completes tests, marks task #3 completed
9. **Team lead** sends shutdown to all:
   ```javascript
   await SendMessage({ to: "*", message: { type: "shutdown_request", reason: "All tasks complete" } });
   ```
10. Teammates acknowledge and shut down
11. **Team lead** calls `TeamDelete({})`

---

## Summary

The teammate system is a sophisticated multi-agent coordination framework built on:

1. **Backend abstraction**: tmux, iTerm2, or in-process execution
2. **File-based messaging**: Mailbox JSON files for async communication
3. **Shared task lists**: Coordinated work tracking
4. **Lifecycle management**: Spawn → Work → Idle → Shutdown cycles
5. **System prompt injection**: Teammates know they're in a team context
6. **Hook integration**: Monitor teammate activity

To implement in a plugin, focus on:
- Backend selection and spawning
- Message queue I/O
- Task list integration
- Idle notification sending
- Shutdown protocol handling

This architecture enables truly parallel multi-agent workflows where agents coordinate through messages and shared task lists, just like human development teams.
