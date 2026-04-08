# Hooks & Agents Comparison: Your Setup vs Official Docs

## Summary

Your setup is **well beyond the documented examples**. You're using undocumented hook events and creating sophisticated agent ecosystems that the docs don't cover.

---

## Hook Events

| Event | Docs Status | Your Usage |
|-------|-------------|------------|
| `PreToolUse` | ✅ Documented | ✅ Token dump prevention, grep/find guards |
| `PostToolUse` | ✅ Documented | ✅ NixOS sync, notifications |
| `PermissionRequest` | ✅ Documented | ✅ Present but minimal |
| `Notification` | ✅ Documented | ✅ Desktop notifications, urgency mapping |
| `UserPromptSubmit` | ✅ Documented | ✅ Git/project context injection |
| `Stop` | ✅ Documented | ✅ Present |
| `SubagentStop` | ✅ Documented | ✅ Duration tracking, notifications |
| `SessionStart` | ✅ Documented | ✅ Environment validation, git status |
| `SessionEnd` | ✅ Documented | ✅ Present |
| `PreCompact` | ✅ Documented | ❌ Not using |
| **`SubagentStart`** | ❌ **NOT documented** | ✅ Model tracking, state files |
| **`read-guard`** | ❌ **NOT documented** | ✅ Bundled file blocking |
| **`skill-invoked`** | ❌ **NOT documented** | ✅ Present |
| **`plan-mode`** | ❌ **NOT documented** | ✅ Present |
| **`tool-error`** | ❌ **NOT documented** | ✅ Present |

### Key Finding: Undocumented Events

You're using at least 5 hook events that aren't in the official docs:
- `SubagentStart` - You extract `model`, `agent_id`, `run_in_background`, `resume`
- `read-guard` - Appears to be a separate hook type for Read tool
- `skill-invoked` - Triggered when skills are called
- `plan-mode` - Triggered during plan mode
- `tool-error` - Triggered on tool failures

**These should probably be reported as doc gaps, not bugs.**

---

## Hook Input: Documented vs Actual

### PreToolUse - Documented Schema

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/dir",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "..." },
  "tool_use_id": "toolu_01ABC123"
}
```

### PreToolUse - What You're Using

```bash
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
```

**Gap**: You're only using 2 fields. The docs show `session_id`, `cwd`, `permission_mode` are also available - could be useful for context-aware decisions.

### SubagentStart - What You're Extracting (Undocumented)

```bash
AGENT_ID=$(echo "$INPUT" | jq -r '.agent_id // "unknown"')
AGENT_NAME=$(echo "$INPUT" | jq -r '.agent_name // ""')
AGENT_TYPE=$(echo "$INPUT" | jq -r '.subagent_type // ""')
MODEL=$(echo "$INPUT" | jq -r '.model // ""')
BACKGROUND=$(echo "$INPUT" | jq -r '.run_in_background // false')
RESUME_ID=$(echo "$INPUT" | jq -r '.resume // ""')
```

**This is the data you want in PreToolUse** - it exists, just not passed to tool hooks.

---

## Agent Definitions

### Documented Pattern

```yaml
---
name: code-reviewer
description: Review code changes
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

### Your Pattern (Extended)

```yaml
---
name: architect
description: System design and high-level architecture...
tools: Bash, Glob, Grep, Read, Write
disallowedTools: Edit              # ← Not in docs
model: claude-opus-4-5-20251101    # ← Not in docs  
permissionMode: default            # ← Not in docs
color: magenta                     # ← Not in docs
hooks:
  PostToolUse:
    - matcher: "Write"
      hooks:
        - type: command
          command: "~/.claude/hooks/agents/validate-design-doc.sh"
---
```

**Undocumented agent frontmatter fields you're using:**
- `tools` - Whitelist specific tools
- `disallowedTools` - Blacklist tools
- `model` - Override model for subagent
- `permissionMode` - Permission handling
- `color` - UI display color

---

## Best Practices Alignment

### ✅ You're Doing Well

| Practice | Docs Recommendation | Your Implementation |
|----------|---------------------|---------------------|
| Quote variables | `"$VAR"` | ✅ Consistent |
| Graceful degradation | `|| true` | ✅ `notify-send ... \|\| true` |
| jq defaults | `// "default"` | ✅ Throughout |
| Path validation | Check `..` | ✅ In agent scripts |
| Log rotation | Keep manageable | ✅ `tail -500` in notification |
| Exit codes | 0=allow, 2=block | ✅ Correct usage |

### ⚠️ Gaps/Improvements

| Issue | Recommendation |
|-------|----------------|
| No `$CLAUDE_PROJECT_DIR` usage | Docs recommend for project-relative scripts |
| State files for subagent tracking | Fragile - see bug report |
| Verbose block messages | Could overwhelm subagent context |
| No timeout configs | Docs support per-hook timeouts |

---

## Agent Sophistication

Your agents go far beyond doc examples:

| Feature | Docs | Your Agents |
|---------|------|-------------|
| Turn budgets | ❌ | ✅ "Maximum: 10-12 turns" |
| Stopping criteria | ❌ | ✅ Explicit conditions |
| Output templates | ❌ | ✅ Markdown formats |
| Tool rationale | ❌ | ✅ Explains why each tool |
| Architecture checklists | ❌ | ✅ ASCII diagrams |
| Severity levels | ❌ | ✅ Critical/Warning/Suggestion |

---

## Recommendations

### 1. File Doc Gaps (Not Bugs)

These hook events work but aren't documented:
- `SubagentStart`
- `read-guard` (if it's a real hook event)
- `skill-invoked`
- `plan-mode`
- `tool-error`

### 2. Use Available Context

Your PreToolUse could use more fields:
```bash
CWD=$(echo "$INPUT" | jq -r '.cwd // empty')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')
```

### 3. Add Timeouts to settings.json

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/pre-tool-use",
        "timeout": 5
      }]
    }]
  }
}
```

### 4. Consider Prompt-Based Hooks

For Stop/SubagentStop, docs show LLM-evaluated hooks:
```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude should stop: $ARGUMENTS..."
}
```

Could replace some of your bash logic with context-aware LLM decisions.
