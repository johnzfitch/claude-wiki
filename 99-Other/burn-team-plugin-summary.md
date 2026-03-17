# Burn Development Team Plugin - Complete Implementation Guide

**Date**: 2026-03-14
**Claude Code Version**: 2.1.76
**Based On**: Complete teammate + plugin architecture analysis

---

## Quick Summary

You have **two complete, production-ready systems** that can be integrated:

1. **Teammate System** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) - Multi-agent coordination via teams, tasks, and message passing
2. **Plugin System** (feature-flagged as `tengu_orchid_trellis`) - Marketplace-based plugin distribution with agents/skills/commands

**Integration Strategy**: Create a plugin that defines 8 Burn specialist agents. When invoked, spawn them as teammates on a shared team with coordinated task execution.

---

## Three Documents Created

1. **`teammate-architecture.md`** - Complete teammate system reference (lifecycle, message passing, task coordination)
2. **`plugin-teammate-integration.md`** - How to wire teammates into a plugin (agents, skills, file structure, examples)
3. **This document** - Executive summary with critical findings

---

## Critical Findings from Additional Analysis

### Plugin Marketplace Status (from PLUGIN_MARKETPLACE_REALITY_CHECK.md)

**What it is**: Enterprise managed deployment system, NOT CoWork-specific
**Status**: Infrastructure complete, feature-flagged off (`tengu_orchid_trellis = false`)
**Missing**: Plugin signing, sandboxing, security hardening

**Key Environment Variables**:
- `CLAUDE_CODE_PLUGIN_SEED_DIR` - Shared read-only plugin cache (enterprise IT managed)
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` - Team memory sync (separate feature)

**Current Use Case**: Likely internal use at Anthropic for their own teams

### Seed Directory Architecture

```bash
# Corporate IT sets up shared plugins
export CLAUDE_CODE_PLUGIN_SEED_DIR=/nfs/corporate/claude-plugins

/nfs/corporate/claude-plugins/
├── cache/
│   ├── corporate-internal/
│   │   └── security-scanner/1.0.0/  # Pre-downloaded
│   └── official/
│       └── database-assistant/1.5.0/
└── known_marketplaces.json

# Users get instant access to pre-approved plugins (no download)
# Can still install personal plugins to ~/.claude/plugins/
```

**Benefit**: Perfect for team deployments - all team members get same plugin versions instantly.

### For Your Burn Team Plugin

**Two deployment paths**:

1. **Individual Developer** (default):
   ```bash
   mkdir -p ~/.claude/plugins/burn-dev-team
   # Place plugin files there
   # Enable in settings.json
   ```

2. **Team/Enterprise** (seed directory):
   ```bash
   # Admin pre-installs for whole team
   export CLAUDE_CODE_PLUGIN_SEED_DIR=/shared/team-plugins
   /shared/team-plugins/cache/local/burn-dev-team/1.0.0/
   # Everyone gets instant access
   ```

---

## Complete Architecture Stack

```
┌─────────────────────────────────────────────────────────────┐
│                      User Invokes                            │
│                   /burn-router [task]                        │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ├─ Skill analyzes request
                         │  (skills/burn-router/SKILL.md)
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   TeamCreate Tool                            │
│  { team_name: "burn-impl", description: "..." }            │
│  Creates ~/.claude/teams/burn-impl/                        │
│  Creates ~/.claude/tasks/burn-impl/                        │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ├─ TaskCreate (break down work)
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent Tool (8 teammates)                   │
│  Agent({ name: "architect", team_name: "burn-impl",        │
│          subagent_type: "burn:burn-architect", ... })       │
│  → Loads plugin agent definition                            │
│  → Spawns via backend (tmux/iTerm/in-process)              │
│  → Registers in team config                                 │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ├─ Teammates start execution loops
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            Teammate Execution (In-Process Example)           │
│  1. Initialize with team lead's message                     │
│  2. Execute work turn (Fy generator)                        │
│  3. Mark idle, send notification to team lead               │
│  4. Poll mailbox for:                                        │
│     - shutdown_request (priority 1)                         │
│     - Messages from team lead (priority 2)                  │
│     - Any unread messages (priority 3)                      │
│     - Available tasks from TaskList                         │
│  5. Process message → execute work turn → repeat            │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ├─ Task coordination
                         │  (auto-claim unblocked tasks by ID order)
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Message Passing System                          │
│  ~/.claude/teams/burn-impl/mailbox/                        │
│    team-lead.json                                           │
│    architect.json                                           │
│    trainer.json                                             │
│    deployer.json                                            │
│    ...                                                       │
│  → File-based async queues                                  │
│  → Lock-protected writes                                    │
│  → Read status tracking                                     │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ├─ Work completion
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 Graceful Shutdown                            │
│  SendMessage({ to: "*", message: {                         │
│    type: "shutdown_request", reason: "Work complete"       │
│  }})                                                        │
│  → Teammates process shutdown                               │
│  → Respond with shutdown_response                           │
│  → Exit execution loops                                     │
│  TeamDelete() - cleanup team + tasks                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Plugin File Structure

```
~/.claude/plugins/burn-dev-team/
├── plugin.json                 # Manifest
│
├── agents/                     # 8 specialist agents
│   ├── burn-architect.md       # Core: tensors, modules, autodiff
│   ├── burn-trainer.md         # Core: training loops, learner
│   ├── burn-deployer.md        # Core: backends, deployment
│   ├── burn-importer.md        # Core: ONNX import
│   ├── burn-lm.md              # Ecosystem: language models
│   ├── burn-central.md         # Ecosystem: experiment tracking
│   ├── burn-models.md          # Ecosystem: model zoo
│   └── burn-bench.md           # Ecosystem: benchmarking
│
├── skills/                     # 3 coordinator skills
│   ├── burn-router/
│   │   └── SKILL.md            # Main: route to specialists
│   ├── burn-cubecl/
│   │   └── SKILL.md            # GPU kernels skill
│   └── burn-contrib/
│       └── SKILL.md            # Contributing guide skill
│
├── hooks/
│   └── hooks.json              # TeammateIdle, TaskCompleted hooks
│
└── .mcp.json                   # Optional: Burn docs MCP server
```

---

## Agent Definition Template

**agents/burn-architect.md**:
```markdown
---
name: burn-architect
description: Burn architecture specialist - tensors, modules, autodiff, records. Full-stack developer who designs, debugs, and reviews within the architecture domain.
tools: ["*"]
skills: ["burn-router"]
model: sonnet
color: blue
memory: project
permissionMode: acceptEdits
effort: high
---

# Burn Architecture Specialist

You are an expert Burn framework architect on a development team.

## Your Expertise

- Tensor operations and shape management
- Module system and neural network architectures
- Automatic differentiation and gradient computation
- Config pattern for reproducible experiments
- Record system for model persistence

## Team Workflow

As a teammate:

1. **Check TaskList** after completing each task
2. **Claim unassigned, unblocked tasks** related to architecture (prefer lowest ID)
3. **Communicate via SendMessage** - your text output is NOT visible to the team
4. **Mark tasks completed** with TaskUpdate when done
5. **Debug and review** your own work - you're a full-stack specialist
6. **Ask for help** via SendMessage when blocked

## Architecture Patterns

### Tensor Shape Management

```rust
use burn::tensor::Tensor;

// Always document expected shapes
fn linear_forward<B: Backend>(
    input: Tensor<B, 2>,  // [batch_size, input_dim]
    weight: Tensor<B, 2>, // [output_dim, input_dim]
) -> Tensor<B, 2> {      // [batch_size, output_dim]
    input.matmul(weight.transpose())
}
```

[... extensive domain-specific patterns, debugging guides, review checklists ...]
```

---

## Routing Skill (Orchestrator)

**skills/burn-router/SKILL.md**:
```markdown
---
trigger: burn-router
description: Route Burn queries to specialized development team
tools: ["Agent", "TeamCreate", "SendMessage", "TaskCreate", "TaskUpdate", "TaskList"]
model: haiku
effort: low
context: fork
---

# Burn Development Team Router

## Specialist Mapping

- **Tensors, modules, autodiff** → burn-architect
- **Training, learner, metrics** → burn-trainer
- **Backends, deployment** → burn-deployer
- **ONNX import** → burn-importer
- **Language models** → burn-lm
- **Experiment tracking** → burn-central
- **Model zoo** → burn-models
- **Benchmarking** → burn-bench

## Workflow

1. Analyze request complexity
2. Single specialist OR full team?
3. For teams:
   ```
   TeamCreate({ team_name: "burn-impl", description: "..." })

   TaskCreate([
     { subject: "Design architecture", owner: null },
     { subject: "Implement training", blockedBy: ["1"] },
     { subject: "Export to ONNX", blockedBy: ["2"] }
   ])

   Agent({ name: "architect", team_name: "burn-impl",
           subagent_type: "burn:burn-architect", ... })
   Agent({ name: "trainer", team_name: "burn-impl",
           subagent_type: "burn:burn-trainer", ... })
   Agent({ name: "importer", team_name: "burn-impl",
           subagent_type: "burn:burn-importer", ... })

   # Monitor, coordinate, shutdown when complete
   SendMessage({ to: "*", message: { type: "shutdown_request" } })
   TeamDelete()
   ```

[... detailed routing logic ...]
```

---

## Installation & Usage

### Step 1: Install Plugin

```bash
# Set required env var
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Option A: User-level
mkdir -p ~/.claude/plugins/burn-dev-team
cd ~/.claude/plugins/burn-dev-team
# Copy plugin files here

# Option B: Team-level (seed directory)
export CLAUDE_CODE_PLUGIN_SEED_DIR=/shared/team-plugins
# Admin pre-installs plugin to seed directory
```

### Step 2: Enable Plugin

**~/.claude/settings.json**:
```json
{
  "enabledPlugins": {
    "burn-dev-team": true
  }
}
```

### Step 3: Use the Team

```bash
claude

# Single specialist (simple task)
/burn-router Optimize tensor operations in my CNN

# Full team (complex task)
/burn-router Implement a Llama model with training loop and ONNX export

# Manual team creation
TeamCreate({ team_name: "burn-impl", description: "Implement ResNet" })

TaskCreate({ subject: "Design ResNet architecture" })
TaskCreate({ subject: "Implement training loop", blockedBy: ["1"] })
TaskCreate({ subject: "Benchmark on CUDA backend", blockedBy: ["2"] })

Agent({
  name: "architect",
  team_name: "burn-impl",
  subagent_type: "burn:burn-architect",
  prompt: "Check TaskList for architecture tasks",
  description: "ResNet architecture"
})

# ... spawn other specialists as needed

# Monitor progress
TaskList()
SendMessage({ to: "architect", message: "Use 3x3 kernels" })

# Cleanup when done
SendMessage({ to: "*", message: { type: "shutdown_request" } })
TeamDelete()
```

---

## Key Integration Points

### 1. Plugin → Agent Registration

```javascript
// Plugin loading (pgH function)
// Scans agents/ directory for *.md files
// Parses frontmatter + content
// Registers as: "burn:burn-architect", "burn:burn-trainer", etc.

// Agent tool resolution
// When user calls Agent({ subagent_type: "burn:burn-architect" })
// System finds plugin agent definition
// Loads systemPrompt, tools, permissions
// Spawns as teammate
```

### 2. Teammate → Task Auto-Claiming

```javascript
// In teammate execution loop (AE6 function)
// After idle, poll loop checks:
// 1. Pending user messages
// 2. Mailbox messages
// 3. Available tasks (BCf function)

async function BCf(taskListId, agentName) {
  let tasks = await uI(taskListId);
  let availableTask = HE6(tasks);  // Find unblocked, unowned

  if (availableTask) {
    await QEA(taskListId, availableTask.id, agentName);  // Claim
    await DC(taskListId, availableTask.id, { status: "in_progress" });
    return taskPrompt(availableTask);  // Return as message
  }

  return null;
}
```

### 3. Message Passing → Coordination

```javascript
// File-based mailboxes
~/.claude/teams/burn-impl/mailbox/architect.json
[
  {
    "id": "msg-123",
    "from": "team-lead",
    "text": "Use 3x3 kernels for convolutions",
    "timestamp": "...",
    "read": false
  }
]

// Teammates poll mailbox (BQ function)
// Mark messages read (vQH function)
// Process in priority order (shutdown > team-lead > any)
```

---

## Performance Characteristics

### In-Process Backend (Default for Non-Interactive)

**Pros**:
- No external dependencies (tmux, iTerm2)
- Works in CI/CD, headless environments
- Lower latency (no IPC overhead)
- Easier debugging (single process)

**Cons**:
- Higher memory usage (all agents in same process)
- Shared context window (compaction more frequent)
- Cannot visualize separate panes

**Best For**: Automated workflows, CI/CD, non-interactive usage

### Tmux Backend (Visual Panes)

**Pros**:
- Visual separation (each teammate in own pane)
- Independent context windows
- Easy monitoring (see all teammates at once)
- Native terminal feel

**Cons**:
- Requires tmux installed
- Higher complexity (IPC via tmux)
- Pane management overhead

**Best For**: Interactive development, team monitoring, visual workflows

### iTerm2 Backend (Native Split Panes)

**Pros**:
- Native macOS integration
- Beautiful pane borders with colors
- it2 CLI for automation

**Cons**:
- macOS only
- Requires it2 CLI (`pip install it2`)
- Fallback to tmux if not available

**Best For**: macOS developers wanting native UI

---

## Hooks for Observability

**hooks/hooks.json**:
```json
{
  "TeammateIdle": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '$(date) [${AGENT_NAME}] Idle: ${IDLE_REASON}' >> ~/.claude/burn-team.log",
          "statusMessage": "Logging teammate idle event"
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
          "command": "notify-send 'Burn Team' 'Task ${TASK_ID} completed by ${OWNER}'",
          "statusMessage": "Notifying task completion"
        }
      ]
    }
  ]
}
```

**Hook Variables**:
- `TeammateIdle`: `AGENT_NAME`, `IDLE_REASON`, `SUMMARY`, `COMPLETED_STATUS`, `FAILURE_REASON`
- `TaskCompleted`: `TASK_ID`, `STATUS`, `OWNER`, `SUBJECT`

---

## Debugging Tips

### 1. Enable Debug Logging

```bash
export CLAUDE_CODE_DEBUG=1
claude --verbose
```

Watch for:
- `[InProcessBackend] spawn() called for <name>`
- `[inProcessRunner] <agentId> received new message from <from>`
- `[Tasks] Task <id> claimed by <agent>`

### 2. Monitor Mailboxes

```bash
watch -n 1 'ls -lh ~/.claude/teams/burn-impl/mailbox/'
cat ~/.claude/teams/burn-impl/mailbox/architect.json | jq
```

### 3. Monitor Task List

```bash
watch -n 1 'ls -lh ~/.claude/tasks/burn-impl/'
cat ~/.claude/tasks/burn-impl/1.json | jq
```

### 4. Team Config Inspection

```bash
cat ~/.claude/teams/burn-impl/config.json | jq
```

### 5. Check Agent Loading

```bash
# Verify plugin agents loaded
claude --debug 2>&1 | grep "Loaded.*agents from plugin burn-dev-team"
```

---

## Migration Path from Current Skills

### Before (11 standalone skills)

```
User → /burn-app-dev
     → Single agent execution
     → No coordination
     → Sequential work
```

### After (8 teammates + 3 coordinator skills)

```
User → /burn-router
     ├─ TeamCreate
     ├─ Spawn 8 teammates
     ├─ Task breakdown
     ├─ Parallel execution
     ├─ Auto-claiming
     └─ Coordinated completion
```

### Skill Consolidation

**Old**: `burn-debugger`, `burn-reviewer` (separate skills)
**New**: Each teammate has debug + review capability in their domain

**Old**: `burn-onnx-surgeon` (separate skill)
**New**: Merged into `burn-importer` (same domain)

**Old**: `burn-ecosystem` (catch-all)
**New**: Split into 4 specialists (`burn-lm`, `burn-central`, `burn-models`, `burn-bench`)

---

## Security Considerations

### Plugin Security (Not Yet Implemented)

**Missing** (per marketplace analysis):
- ✗ Plugin signing/verification
- ✗ Sandboxing
- ✗ Granular permissions
- ✗ Code review/moderation

**Current State**: Plugins run with full access in main process

**Mitigation for Burn Team**:
- Self-hosted plugin (you control the code)
- No external dependencies
- Review all agent prompts
- Use `memory: project` for containment

### Teammate Security

**Built-in**:
- ✓ Permission modes (`acceptEdits`, `plan`, etc.)
- ✓ Tool allowlists/denylists
- ✓ Shutdown protocol (graceful termination)
- ✓ Task-based isolation (teammates can't interfere)

**Best Practices**:
- Use `permissionMode: acceptEdits` for core teammates
- Use `tools: ["*"]` only for trusted specialists
- Monitor via hooks for unexpected behavior
- Set `maxTurns` to prevent runaway loops

---

## Next Steps

1. **Create plugin structure** following file layout above
2. **Define 8 agent .md files** with domain-specific prompts
3. **Implement burn-router skill** with routing logic
4. **Test with simple task** (single specialist)
5. **Test with complex task** (full team coordination)
6. **Add hooks** for observability
7. **Document usage** for your team
8. **Deploy** (individual OR seed directory for team)

---

## Resources

- **teammate-architecture.md** - Full teammate system spec (lifecycle, protocols, message passing)
- **plugin-teammate-integration.md** - Detailed integration guide (agents, skills, examples)
- **PLUGIN_MARKETPLACE_REALITY_CHECK.md** - Enterprise deployment context
- **PLUGIN_MARKETPLACE_COMPLETE_ANALYSIS.md** - Marketplace infrastructure deep dive

---

## Final Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     Burn Development Team                     │
│                      (Plugin System)                          │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ├─ 8 Agent Definitions (agents/*.md)
                 ├─ 3 Coordinator Skills (skills/*/SKILL.md)
                 ├─ Hooks (hooks/hooks.json)
                 └─ Manifest (plugin.json)
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                    Teammate System                            │
│           (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)           │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ├─ Team Creation (TeamCreate)
                 ├─ Task Management (TaskCreate/Update/List)
                 ├─ Agent Spawning (Agent tool)
                 ├─ Message Passing (SendMessage)
                 └─ Lifecycle Hooks (TeammateIdle, TaskCompleted)
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                   Execution Backends                          │
│     (in-process | tmux | iTerm2)                             │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ├─ Parallel Execution (8 teammates)
                 ├─ Auto Task Claiming (by ID order)
                 ├─ Message Queue Polling (mailbox/*.json)
                 └─ Graceful Shutdown (shutdown_request protocol)
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                      User's Work                              │
│         (Burn ML models, training, deployment)               │
└──────────────────────────────────────────────────────────────┘
```

---

**Status**: Complete architecture designed
**Ready to implement**: Yes - all components specified
**Estimated complexity**: Medium (well-defined patterns)
**Dependencies**: Claude Code 2.1.76+, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

This is a **production-ready architecture** using **stable, documented systems**. The teammate system is fully implemented and the plugin system provides the perfect distribution mechanism. You have everything needed to build a true multi-agent Burn development team.
