# Hooks Summary for Burn Development Team Plugin

**Date**: 2026-03-15
**Purpose**: Quick reference for implementing dynamic context injection via hooks

---

## The Solution to Plugin Limitations

**Problem**: Plugin agents can't have JavaScript `getSystemPrompt({ toolUseContext })` functions.

**Solution**: Use **hooks with `additionalContext`** to inject dynamic content at key lifecycle events.

---

## Critical Hook Events for Our Use Case

### 1. `SubagentStart` — PRIMARY INJECTION POINT

**Fires**: When ANY agent spawns (teammates, subagents, plugin agents)

**Perfect for**: Injecting project-specific context when a Burn agent starts.

**Input Fields**:
```json
{
  "hook_event_name": "SubagentStart",
  "agent_id": "abc123",
  "agent_type": "burn-architect",  // ← Filter on this!
  "cwd": "/project/path",
  "permission_mode": "..."
}
```

**Hook Output** (bash script example):
```bash
#!/bin/bash
INPUT=$(cat)
AGENT=$(echo "$INPUT" | jq -r '.agent_type')
CWD=$(echo "$INPUT" | jq -r '.cwd')

# Only inject for Burn agents
if [[ ! "$AGENT" =~ ^burn- ]]; then
  exit 0
fi

# Detect Burn version
BURN_VER=""
if [[ -f "$CWD/Cargo.toml" ]]; then
  BURN_VER=$(grep 'burn =' "$CWD/Cargo.toml" | head -1 | cut -d'"' -f2)
fi

# Find Burn files
BURN_FILES=$(find "$CWD" -name "*.rs" -exec grep -l "use burn::" {} \; 2>/dev/null | wc -l)

# Build context
CONTEXT="**Project Detection**
- Burn Version: ${BURN_VER:-not detected}
- Files using Burn: $BURN_FILES
- Working Directory: $CWD"

# Return JSON with additionalContext
jq -n --arg ctx "$CONTEXT" '{
  hookSpecificOutput: {
    hookEventName: "SubagentStart",
    additionalContext: $ctx
  }
}'
```

**Result**: Agent receives static systemPrompt + dynamic project context.

---

### 2. `PostToolUse` — POST-ACTION FEEDBACK

**Fires**: After tools execute successfully

**Perfect for**: Providing compiler feedback after writing Rust code.

**Input Fields**:
```json
{
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "src/model.rs",
    "content": "..."
  },
  "tool_output": "File written"
}
```

**Example Use**: Run `cargo check` after writing .rs files, inject errors/warnings.

---

### 3. `UserPromptSubmit` — PER-TURN REFRESH

**Fires**: Every time user submits a message

**Perfect for**: Re-scanning project state on demand.

**Input Fields**:
```json
{
  "hook_event_name": "UserPromptSubmit",
  "prompt": "User's message here"
}
```

**Example Use**: Check for new dependencies in Cargo.toml on every turn.

---

### 4. `SessionStart` — INITIAL SETUP

**Fires**: At session start

**Perfect for**: One-time expensive scans (full codebase indexing).

---

## Plugin Manifest Hook Configuration

```json
{
  "name": "burn-dev-team",
  "version": "1.0.0",

  "agents": "agents/",
  "skills": "skills/",

  "hooks": {
    "SubagentStart": [{
      "matcher": "agent_type.startsWith('burn-')",
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
        "command": "hooks/check-rust-code.sh",
        "async": true
      }]
    }]
  }
}
```

---

## Complete Hook List (2.1.70+)

All hooks that support `additionalContext`:

| Hook Event | Fires When | additionalContext Support | Use Case |
|------------|------------|---------------------------|----------|
| **SubagentStart** | Agent spawns | ✅ Yes | **Primary injection point** |
| **SessionStart** | Session begins | ✅ Yes | Initial project scan |
| **UserPromptSubmit** | User sends message | ✅ Yes | Per-turn refresh |
| **PostToolUse** | Tool completes | ✅ Yes | Post-action feedback |
| **PostToolUseFailure** | Tool fails | ✅ Yes | Error context |
| **Setup** | Repo maintenance | ✅ Yes | Git hooks, linting |
| PreToolUse | Before tool runs | ❌ No | Permission only |
| Stop | Claude finishes | ❌ No | Observational |
| SessionEnd | Session ends | ❌ No | Cleanup |
| PreCompact | Before compaction | ❌ No | Compact instructions |

---

## Recommended Architecture

### Tier 1: Static Knowledge (Agent .md Files)
- Hot-path APIs (Tensor::zeros, Module patterns)
- Common pitfalls
- Design patterns
- ~10KB per agent

### Tier 2: Dynamic Context (Hooks)
- **SubagentStart**: Project state (Burn version, files)
- **PostToolUse**: Compiler feedback
- **UserPromptSubmit**: Dependency changes
- Injected via `additionalContext`

### Tier 3: Complex Queries (MCP Tools)
- Database searches
- External APIs
- Rare/obscure docs
- Agents call when needed

---

## Example: Complete Burn Architect Agent

**File**: `agents/burn-architect.md`

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

You are the Burn architecture specialist.

## Core Tensor Operations

- `Tensor::zeros(shape)` — zero-initialized
- `Tensor::ones(shape)` — one-initialized
- `Tensor::matmul(other)` — matrix multiplication

## Module Patterns

```rust
#[derive(Module)]
pub struct MyModel<B: Backend> {
    linear: Linear<B>,
}
```

## Common Pitfalls

1. Shape mismatch on matmul
2. Missing `.inner()` on autodiff
3. Backend type leakage

---

**Dynamic Context Note**: When you spawn, a hook will inject the current project's Burn version and file count. Use this to give specific advice.
```

**Hook**: `hooks/inject-burn-context.sh` (shown above)

**Result**: Agent knows about project without needing JavaScript!

---

## Performance Considerations

### Hook Execution Time
- **Target**: < 5 seconds for SubagentStart
- **Cache**: Expensive scans (store in /tmp with TTL)
- **Async**: Use `async: true` for slow operations

### Caching Pattern

```bash
CACHE="/tmp/burn-context-$CWD_HASH.json"
if [[ -f "$CACHE" ]]; then
  AGE=$(($(date +%s) - $(stat -c %Y "$CACHE")))
  if [[ $AGE -lt 300 ]]; then  # 5 min TTL
    cat "$CACHE"
    exit 0
  fi
fi

# Generate fresh context
CONTEXT="..."
echo "$CONTEXT" | tee "$CACHE"
```

---

## Testing Hooks

### Manual Test

```bash
# Create test input
cat > /tmp/test-hook-input.json << 'EOF'
{
  "hook_event_name": "SubagentStart",
  "agent_type": "burn-architect",
  "cwd": "/path/to/burn/project"
}
EOF

# Run hook
cat /tmp/test-hook-input.json | hooks/inject-burn-context.sh | jq
```

### Expected Output

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "**Project Detection**\n- Burn Version: 0.20.0\n- Files using Burn: 5\n- Working Directory: /path/to/burn/project"
  }
}
```

---

## Common Patterns

### Pattern 1: Agent-Specific Context

```bash
case "$AGENT_TYPE" in
  burn-architect)
    CONTEXT="Focus on tensor ops and module design"
    ;;
  burn-trainer)
    CONTEXT="Focus on Learner API and training"
    ;;
  burn-deployer)
    CONTEXT="Focus on backends and optimization"
    ;;
esac
```

### Pattern 2: Environment Detection

```bash
if [[ -f "Cargo.toml" ]]; then
  CONTEXT="Rust project with Cargo"
elif [[ -f "package.json" ]]; then
  CONTEXT="Node.js project"
fi
```

### Pattern 3: Error Detection

```bash
ERRORS=$(cargo check 2>&1 | grep "error")
if [[ -n "$ERRORS" ]]; then
  CONTEXT="**Compiler Errors Detected:**\n$ERRORS"
fi
```

---

## Limitations & Workarounds

### Limitation 1: No Access to Conversation History
**Workaround**: Read transcript file (path provided in hook input)

### Limitation 2: No Access to Model State
**Workaround**: Use session-scoped files to track state

### Limitation 3: Synchronous Execution
**Workaround**: Use `async: true` for long operations, cache results

---

## Next Steps

1. ✅ Create hook scripts in `hooks/` directory
2. ✅ Add hook config to `manifest.json`
3. ✅ Test hooks with sample input
4. ✅ Verify `additionalContext` appears in agent systemPrompt
5. ⬜ Check 2.1.76 for new hook events (in progress)

---

**Created**: `/home/zack/claude-binary/HOOKS_DYNAMIC_CONTEXT_INJECTION.md` (full reference)
**This file**: Quick reference for implementation
