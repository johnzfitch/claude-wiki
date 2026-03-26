# Hooks: Dynamic Context Injection for Agents

**Date**: 2026-03-15
**Critical Discovery**: Hooks CAN inject dynamic context into agent systemPrompts via `additionalContext`!

---

## TL;DR: The Missing Piece

**Plugins CAN get dynamic systemPrompt behavior through hooks!**

While plugin agents can't have JavaScript `getSystemPrompt({ toolUseContext })` functions, they CAN use **hooks** to inject dynamic context at key lifecycle events:

1. **`SubagentStart`** — Inject context when agent spawns
2. **`UserPromptSubmit`** — Inject context on every user message
3. **`PostToolUse`** — Inject context after tool calls
4. **`SessionStart`** — Inject context at session startup

This solves the "no dynamic context" limitation we discovered!

---

## How `additionalContext` Works

### Hook Output Schema

All these hook events support `additionalContext` in their `hookSpecificOutput`:

```typescript
// From source code schema
type HookOutput = {
  hookSpecificOutput?: {
    hookEventName: "SubagentStart" | "SessionStart" | "UserPromptSubmit" | "PostToolUse" | ...
    additionalContext?: string  // ← This gets injected into conversation
    // ... other fields
  }
}
```

### Injection Mechanism

When a hook returns `additionalContext`, Claude Code:
1. Takes the string value
2. Injects it as a **system message** into the conversation
3. The model sees it as authoritative context for that turn

**Example**:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "**Project Context**: Burn 0.20.0 detected in Cargo.toml. 3 Burn files found: src/model.rs, src/training.rs, src/data.rs"
  }
}
```

Result: The agent receives this context in its system prompt for that session.

---

## Hook Events That Support Dynamic Context

### 1. `SubagentStart` — Agent Spawn Context Injection

**Fires**: When an agent is spawned (via Agent tool or teammate system)

**Input Schema**:
```json
{
  "hook_event_name": "SubagentStart",
  "session_id": "...",
  "transcript_path": "...",
  "cwd": "/project/path",
  "permission_mode": "...",
  "agent_id": "abc123",
  "agent_type": "burn-architect"  // ← Our agent name!
}
```

**Hook Output**:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "<dynamic context here>"
  }
}
```

**Use Case**: Inject project-specific context when a Burn agent spawns.

**Example Hook (Command)**:
```bash
#!/bin/bash
# .claude/hooks/inject-burn-context.sh

INPUT=$(cat)
AGENT_TYPE=$(echo "$INPUT" | jq -r '.agent_type')
CWD=$(echo "$INPUT" | jq -r '.cwd')

if [[ "$AGENT_TYPE" == "burn-architect" ]]; then
  # Detect Burn version
  if [[ -f "$CWD/Cargo.toml" ]]; then
    BURN_VERSION=$(grep 'burn =' "$CWD/Cargo.toml" | head -1 | sed 's/.*"\(.*\)".*/\1/')

    # Find Burn files
    BURN_FILES=$(find "$CWD" -name "*.rs" -exec grep -l "use burn::" {} \; 2>/dev/null | head -10)
    FILE_COUNT=$(echo "$BURN_FILES" | wc -l)

    # Build context
    CONTEXT="**Project Context - Burn Framework**

- Burn Version: $BURN_VERSION detected in Cargo.toml
- Burn Files Found: $FILE_COUNT files
$(echo "$BURN_FILES" | sed 's/^/  - /')

This project is using the Burn deep learning framework. Prioritize Burn-specific patterns and APIs."

    # Return with additionalContext
    jq -n \
      --arg ctx "$CONTEXT" \
      '{
        hookSpecificOutput: {
          hookEventName: "SubagentStart",
          additionalContext: $ctx
        }
      }'
  fi
fi
```

**Hook Config** (in plugin `manifest.json` or `~/.claude/settings.json`):
```json
{
  "hooks": {
    "SubagentStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/inject-burn-context.sh"
      }]
    }]
  }
}
```

**Result**: When `burn-architect` agent spawns, it receives:
```
You are the Burn architecture specialist...
[static systemPrompt from .md file]

---

**Project Context - Burn Framework**

- Burn Version: 0.20.0 detected in Cargo.toml
- Burn Files Found: 3 files
  - src/model.rs
  - src/training.rs
  - src/data.rs

This project is using the Burn deep learning framework...
```

### 2. `UserPromptSubmit` — Per-Turn Context Injection

**Fires**: Every time user submits a prompt

**Input Schema**:
```json
{
  "hook_event_name": "UserPromptSubmit",
  "session_id": "...",
  "transcript_path": "...",
  "cwd": "...",
  "permission_mode": "...",
  "prompt": "How do I implement a custom loss function?"  // ← User's message
}
```

**Use Case**: Inject fresh project state on every turn (files changed, new dependencies, etc.)

**Example**: Re-scan Cargo.toml on every message to catch new dependencies.

### 3. `PostToolUse` — Post-Tool Context Injection

**Fires**: After a tool executes successfully

**Input Schema**:
```json
{
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": { "file_path": "src/model.rs", "content": "..." },
  "tool_output": "File written successfully"
}
```

**Use Case**: After writing Rust code, inject compiler warnings/errors.

**Example**:
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [[ "$TOOL_NAME" == "Write" && "$FILE_PATH" == *.rs ]]; then
  # Run cargo check
  ERRORS=$(cargo check --message-format=short 2>&1 | grep "error\|warning" | head -20)

  if [[ -n "$ERRORS" ]]; then
    CONTEXT="**Compiler Feedback After Writing $FILE_PATH**:

\`\`\`
$ERRORS
\`\`\`

Please address these issues."

    jq -n --arg ctx "$CONTEXT" \
      '{hookSpecificOutput: {hookEventName: "PostToolUse", additionalContext: $ctx}}'
  fi
fi
```

### 4. `SessionStart` — Initial Session Context

**Fires**: At the beginning of a session

**Use Case**: One-time project detection and setup instructions.

---

## Complete Plugin Architecture with Hooks

### File Structure

```
burn-plugin/
├── manifest.json
├── agents/
│   ├── burn-architect.md        # Static knowledge + memory
│   ├── burn-trainer.md
│   └── ...
├── skills/
│   └── burn-router/
│       └── SKILL.md              # Routing decision tree
├── hooks/
│   ├── inject-burn-context.sh   # SubagentStart hook
│   ├── check-after-write.sh     # PostToolUse hook
│   └── scan-project.sh          # SessionStart hook
└── mcp-servers/
    └── burn-kb/
        └── server.py             # Optional: for complex queries
```

### Plugin `manifest.json`

```json
{
  "name": "burn-dev-team",
  "version": "1.0.0",
  "description": "Burn ML framework development team with dynamic context injection",

  "agents": "agents/",
  "skills": "skills/",

  "hooks": {
    "SubagentStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "hooks/inject-burn-context.sh",
        "timeout": 5
      }]
    }],

    "PostToolUse": [{
      "matcher": "tool_name == 'Write' && tool_input.file_path.endsWith('.rs')",
      "hooks": [{
        "type": "command",
        "command": "hooks/check-after-write.sh",
        "async": true
      }]
    }],

    "SessionStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "hooks/scan-project.sh",
        "timeout": 10
      }]
    }]
  }
}
```

### Agent Definition (Static + Dynamic via Hook)

```markdown
---
name: burn-architect
description: Burn architecture specialist — tensors, modules, autodiff
tools:
  - Read
  - Write
  - Grep
  - Glob
model: sonnet
memory: project
---

You are the Burn architecture specialist with deep expertise in:

## Core Tensor Operations (Hot Path - Always Available)

- `Tensor::zeros(shape)` — zero-initialized tensor
- `Tensor::ones(shape)` — one-initialized
- `Tensor::matmul(other)` — matrix multiplication
- `tensor.reshape(new_shape)` — view with new dimensions

## Module Design Patterns

### Record Pattern
```rust
#[derive(Module, Debug)]
pub struct LinearLayer<B: Backend> {
    weight: Param<Tensor<B, 2>>,
}
```

## Common Pitfalls

1. Shape mismatch on matmul
2. Missing `.inner()` on autodiff tensors
3. Backend type leakage

---

**Note**: When you spawn, a `SubagentStart` hook will inject current project context (Burn version, existing files, dependencies). Use this to tailor your responses to the user's actual setup.
```

**What happens**:
1. User spawns `burn-architect` agent
2. `SubagentStart` hook fires
3. Hook script reads `Cargo.toml`, scans for Burn files
4. Hook returns `additionalContext` with project state
5. Agent receives: static systemPrompt + dynamic project context
6. Agent has full awareness without needing `getSystemPrompt({ toolUseContext })`

---

## Hook Matcher Syntax

Hooks support **matcher expressions** to conditionally fire:

```json
{
  "matcher": "agent_type == 'burn-architect'",
  "hooks": [...]
}

{
  "matcher": "tool_name == 'Write' && tool_input.file_path.endsWith('.rs')",
  "hooks": [...]
}

{
  "matcher": "",  // Always fires
  "hooks": [...]
}
```

**Operators**: `==`, `!=`, `&&`, `||`, `startsWith()`, `endsWith()`, `includes()`

---

## Comparison: Built-In vs. Plugin (With Hooks)

| Feature | Built-In Agent | Plugin Agent (Static) | Plugin Agent (With Hooks) |
|---------|---------------|----------------------|---------------------------|
| **Static knowledge** | ✅ Embedded in JS | ✅ Embedded in .md | ✅ Embedded in .md |
| **Dynamic context injection** | ✅ `getSystemPrompt({ toolUseContext })` | ❌ Not possible | ✅ Via `SubagentStart` hook |
| **Project awareness** | ✅ Can read `toolUseContext` | ❌ No access | ✅ Hook scans filesystem |
| **Burn version detection** | ✅ Can check Cargo.toml | ❌ Static | ✅ Hook reads Cargo.toml |
| **Existing file listing** | ✅ Can access file state | ❌ Static | ✅ Hook scans with `find` |
| **Post-action feedback** | ✅ Can inject after tools | ❌ Static | ✅ `PostToolUse` hook |
| **Per-turn updates** | ✅ Can rebuild context | ❌ Static | ✅ `UserPromptSubmit` hook |
| **Requires binary modification** | ❌ Yes | ✅ No | ✅ No |

---

## Advanced Hook Patterns

### Pattern 1: Agent-Specific Context

Only inject for specific agents:

```bash
#!/bin/bash
INPUT=$(cat)
AGENT_TYPE=$(echo "$INPUT" | jq -r '.agent_type')

case "$AGENT_TYPE" in
  burn-architect)
    CONTEXT="Focus on tensor operations and module design"
    ;;
  burn-trainer)
    CONTEXT="Focus on Learner API and training loops"
    ;;
  burn-deployer)
    CONTEXT="Focus on backend selection and optimization"
    ;;
  *)
    exit 0  # No context for other agents
    ;;
esac

jq -n --arg ctx "$CONTEXT" \
  '{hookSpecificOutput: {hookEventName: "SubagentStart", additionalContext: $ctx}}'
```

### Pattern 2: Cached Context (Performance)

Cache expensive operations:

```bash
#!/bin/bash
CACHE_FILE="/tmp/burn-project-context.cache"
CACHE_TTL=300  # 5 minutes

if [[ -f "$CACHE_FILE" ]]; then
  AGE=$(($(date +%s) - $(stat -c %Y "$CACHE_FILE" 2>/dev/null || stat -f %m "$CACHE_FILE")))
  if [[ $AGE -lt $CACHE_TTL ]]; then
    cat "$CACHE_FILE"
    exit 0
  fi
fi

# Generate fresh context
CONTEXT="..."  # ... scan project

# Cache and return
jq -n --arg ctx "$CONTEXT" \
  '{hookSpecificOutput: {hookEventName: "SubagentStart", additionalContext: $ctx}}' \
  | tee "$CACHE_FILE"
```

### Pattern 3: HTTP Hook for Remote Context

For enterprise deployments with centralized knowledge:

```json
{
  "hooks": {
    "SubagentStart": [{
      "matcher": "agent_type.startsWith('burn-')",
      "hooks": [{
        "type": "http",
        "url": "https://internal.company.com/burn-context",
        "headers": {
          "Authorization": "Bearer $BURN_CONTEXT_TOKEN"
        },
        "timeout": 5
      }]
    }]
  }
}
```

Server responds:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "**Company Standards**: Use Burn 0.20.0. Approved backends: WGPU, CUDA. Code review required for custom operations."
  }
}
```

---

## New Hook Events in 2.1.76 (To Check)

Based on the pattern of additions in 2.1.70 (Elicitation, ElicitationResult, InstructionsLoaded), there may be new events in 2.1.76. Need to check:

1. **Team-related hooks** (TeamCreate, TeamDelete, TeammateMessage?)
2. **Task system hooks** (TaskCreate, TaskUpdate, TaskClaim?)
3. **Plugin lifecycle hooks** (PluginLoaded, PluginEnabled?)
4. **MCP connection hooks** (MCPServerConnected, MCPServerDisconnected?)

Let me search 2.1.76 source for new hook events...

---

## Conclusion: Plugins + Hooks = Dynamic Agents!

**The full picture**:

### Tier 1: Static Agent Knowledge (Markdown)
- Hot-path APIs and patterns embedded in agent `.md` files
- Always available, zero latency
- ~10KB per agent

### Tier 2: Dynamic Context Injection (Hooks)
- `SubagentStart` hook injects project state when agent spawns
- `PostToolUse` hook injects feedback after actions
- `UserPromptSubmit` hook refreshes context on demand
- Agents get runtime awareness without `getSystemPrompt({ toolUseContext })`

### Tier 3: Complex Queries (MCP Tools)
- For database queries, semantic search, external APIs
- Agents call tools when needed
- Scales to millions of docs

**This solves the "plugin limitation" we discovered!**

Plugins CAN have dynamic behavior — not via JavaScript functions, but via **hooks that inject `additionalContext`** at the right lifecycle events.

**Next**: Check 2.1.76 for new hook events that might enable even more dynamic behavior.
