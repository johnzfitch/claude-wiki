# Hook Events Status — 2.1.76

**Date**: 2026-03-15
**Finding**: No new hook events in 2.1.76 (still 21 events from 2.1.70)

---

## Complete Hook Event Inventory (2.1.76)

From source code array `SX6`:

```javascript
[
  "PreToolUse",
  "PostToolUse",
  "PostToolUse Failure",
  "Notification",
  "UserPromptSubmit",
  "SessionStart",
  "SessionEnd",
  "Stop",
  "SubagentStart",        // ← KEY for dynamic agent context
  "SubagentStop",
  "PreCompact",
  "PermissionRequest",
  "Setup",
  "TeammateIdle",         // ← Team system
  "TaskCompleted",        // ← Team system
  "Elicitation",          // ← Added in 2.1.70
  "ElicitationResult",    // ← Added in 2.1.70
  "ConfigChange",
  "WorktreeCreate",
  "WorktreeRemove",
  "InstructionsLoaded"    // ← Added in 2.1.70
]
```

**Total**: 21 events (same as 2.1.70)

---

## Events Supporting `additionalContext`

These hooks can inject dynamic context into the conversation:

1. ✅ **SubagentStart** — Agent spawns (PRIMARY for our use case)
2. ✅ **SessionStart** — Session begins
3. ✅ **UserPromptSubmit** — User sends message
4. ✅ **PostToolUse** — After tool executes
5. ✅ **PostToolUseFailure** — After tool fails
6. ✅ **Setup** — Repo maintenance
7. ✅ **Notification** — System notifications

---

## Critical Discovery: Hooks Solve Plugin Limitations

### Problem
Plugin agents can't have JavaScript `getSystemPrompt({ toolUseContext })` like built-in agents.

### Solution
Use `SubagentStart` hook with `additionalContext` to inject dynamic project state when agent spawns.

### Example Flow

1. **Plugin defines static agent**:
   ```markdown
   ---
   name: burn-architect
   ---
   You are a Burn expert. [static knowledge here]
   ```

2. **Hook injects dynamic context**:
   ```bash
   # .claude/hooks/inject-burn-context.sh
   #!/bin/bash
   INPUT=$(cat)
   AGENT=$(echo "$INPUT" | jq -r '.agent_type')

   if [[ "$AGENT" == "burn-architect" ]]; then
     BURN_VER=$(grep 'burn =' Cargo.toml | cut -d'"' -f2)
     jq -n --arg ctx "Burn $BURN_VER detected" '{
       hookSpecificOutput: {
         hookEventName: "SubagentStart",
         additionalContext: $ctx
       }
     }'
   fi
   ```

3. **Agent receives**:
   ```
   You are a Burn expert. [static knowledge]

   ---

   Burn 0.20.0 detected
   ```

This achieves the same result as `getSystemPrompt({ toolUseContext })` without requiring JavaScript!

---

## No New Hook Events in 2.1.76

Comparison with 2.1.70:
- **2.1.59**: 18 events
- **2.1.70**: 21 events (+3: Elicitation, ElicitationResult, InstructionsLoaded)
- **2.1.76**: 21 events (no additions)

**Conclusion**: The hook system is stable. The 2.1.70 additions were for:
- MCP elicitation handling
- Instructions file observability

These are complete for our Burn plugin use case.

---

## Recommended Hook Setup for Burn Plugin

### `manifest.json`

```json
{
  "name": "burn-dev-team",
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

### Hook Scripts

**`hooks/inject-burn-context.sh`**:
```bash
#!/bin/bash
INPUT=$(cat)
AGENT=$(echo "$INPUT" | jq -r '.agent_type')
CWD=$(echo "$INPUT" | jq -r '.cwd')

[[ ! "$AGENT" =~ ^burn- ]] && exit 0

BURN_VER=""
[[ -f "$CWD/Cargo.toml" ]] && BURN_VER=$(grep 'burn =' "$CWD/Cargo.toml" | cut -d'"' -f2)

BURN_FILES=$(find "$CWD" -name "*.rs" -exec grep -l "use burn::" {} \; 2>/dev/null | wc -l)

CONTEXT="**Project Detection**
- Burn Version: ${BURN_VER:-not detected}
- Files using Burn: $BURN_FILES"

jq -n --arg ctx "$CONTEXT" '{
  hookSpecificOutput: {
    hookEventName: "SubagentStart",
    additionalContext: $ctx
  }
}'
```

**`hooks/check-rust-code.sh`**:
```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path')

ERRORS=$(cargo check --message-format=short 2>&1 | grep "error\|warning" | head -10)

if [[ -n "$ERRORS" ]]; then
  CONTEXT="**Compiler Feedback**:
\`\`\`
$ERRORS
\`\`\`"

  jq -n --arg ctx "$CONTEXT" '{
    hookSpecificOutput: {
      hookEventName: "PostToolUse",
      additionalContext: $ctx
    }
  }'
fi
```

**`hooks/scan-project.sh`**:
```bash
#!/bin/bash
INPUT=$(cat)
CWD=$(echo "$INPUT" | jq -r '.cwd')

[[ ! -f "$CWD/Cargo.toml" ]] && exit 0

BACKEND=$(grep -E 'burn.*wgpu|burn.*cuda|burn.*ndarray' "$CWD/Cargo.toml" | head -1)
MODEL_FILES=$(find "$CWD" -name "*.rs" -exec grep -l "Module" {} \; | wc -l)

CONTEXT="**Burn Project Detected**
- Backend: ${BACKEND:-default}
- Model files: $MODEL_FILES"

jq -n --arg ctx "$CONTEXT" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: $ctx
  }
}'
```

---

## Final Architecture: Static + Dynamic + MCP

### Tier 1: Static Knowledge (Embedded in .md)
- Hot-path APIs (Tensor::zeros, Module patterns)
- Common pitfalls
- Design patterns
- ~10KB per agent
- **Always available, zero latency**

### Tier 2: Dynamic Context (Hooks)
- **SubagentStart**: Burn version, file count, dependencies
- **PostToolUse**: Compiler errors/warnings
- **SessionStart**: Initial project scan
- **Injected via `additionalContext`**
- **Sub-5s execution time**

### Tier 3: Complex Queries (MCP Tools)
- Database searches for rare APIs
- External documentation fetching
- Semantic search across examples
- **Called by agents when needed**

---

## Summary

**2.1.76 Status**: Hook system is complete and stable (21 events, same as 2.1.70).

**Key Discovery**: `SubagentStart` + `additionalContext` provides dynamic systemPrompt injection for plugin agents, solving the limitation of static .md files.

**Ready to implement**: All necessary hooks are available to build a fully dynamic Burn development team plugin.

---

**Related Documents**:
- `HOOKS_DYNAMIC_CONTEXT_INJECTION.md` — Full reference
- `HOOKS_SUMMARY_FOR_BURN_PLUGIN.md` — Quick implementation guide
- `PLUGIN_CAPABILITIES_REALITY_CHECK.md` — Plugin limitations
- `BURN_KB_ARCHITECTURE_VERIFIED.md` — Original (now superseded by hooks approach)
