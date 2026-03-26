# Claude Code Hooks - Configuration Reference

## Hook Configuration Format

Claude Code uses a matcher-based array format for hooks:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/hook"
          }
        ]
      }
    ]
  }
}
```

---

## Available Hook Events

| Event | When | Use Case |
|-------|------|----------|
| `PreToolUse` | Before tool execution | Security validation, cost tracking |
| `PostToolUse` | After successful tool execution | Auto-backup, sync, notifications |
| `PostToolUseFailure` | After tool failure | Error logging, notifications |
| `UserPromptSubmit` | When user submits prompt | Context enhancement, TODO detection |
| `SessionStart` | Session initialization | Environment validation, logging |
| `SessionEnd` | Session termination | Cleanup, final logging |
| `Notification` | On notifications | Custom notification handling |
| `Stop` | On stop events | Cleanup |
| `SubagentStart` | When subagent starts | Subagent tracking |
| `SubagentStop` | When subagent stops | Subagent cleanup |
| `PreCompact` | Before compacting | Pre-compact processing |
| `PermissionRequest` | On permission requests | Custom permission handling |

---

## Using Matchers

Matchers filter when hooks run. Use `"*"` to match all tools.

**Match all tools:**

```json
{
  "matcher": "*",
  "hooks": [...]
}
```

**Match specific tools:**

```json
{
  "matcher": {
    "tools": ["Bash"]
  },
  "hooks": [...]
}
```

**Match file patterns:**

```json
{
  "matcher": {
    "filePatterns": ["*.js", "*.ts"]
  },
  "hooks": [...]
}
```

**Combined matchers:**

```json
{
  "matcher": {
    "tools": ["Edit", "Write"],
    "filePatterns": ["*.nix"]
  },
  "hooks": [...]
}
```

---

## Multiple Hooks Per Event

You can have multiple hooks for the same event with different matchers:

```json
{
  "PostToolUse": [
    {
      "matcher": {
        "tools": ["Bash"]
      },
      "hooks": [
        {
          "type": "command",
          "command": "/home/zack/.claude/hooks/bash-logger"
        }
      ]
    },
    {
      "matcher": {
        "tools": ["Edit"]
      },
      "hooks": [
        {
          "type": "command",
          "command": "/home/zack/.claude/hooks/edit-backup"
        }
      ]
    }
  ]
}
```

---

## Hook Input (stdin JSON)

Hooks receive JSON via stdin with context about the event.

**PreToolUse / PostToolUse:**

```json
{
  "tool_name": "Bash",
  "tool_input": { "command": "ls -la" },
  "tool_use_id": "toolu_xxx"
}
```

**PostToolUseFailure:**

```json
{
  "tool_name": "Bash",
  "tool_input": { "command": "invalid" },
  "error": "command not found"
}
```

**UserPromptSubmit:**

```json
{
  "prompt": "fix the bug"
}
```

**SessionStart:**

```json
{
  "session_id": "xxx-xxx-xxx"
}
```

---

## Hook Output

Hooks can output JSON to modify behavior:

**Block tool execution (PreToolUse):**

```json
{
  "decision": "block",
  "reason": "Cannot modify sensitive file"
}
```

**Add context (UserPromptSubmit):**

```json
{
  "additionalContext": "[Branch: main] [3 uncommitted files]"
}
```

---

## Current Configuration

Your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/zack/.claude/hooks/pre-tool-use"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/zack/.claude/hooks/post-tool-use"
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/zack/.claude/hooks/tool-error"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/home/zack/.claude/hooks/user-prompt-submit"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/home/zack/.claude/hooks/session-start"
          }
        ]
      }
    ]
  }
}
```

---

## Testing

```bash
# Start session (triggers SessionStart)
claude

# Run command (triggers PreToolUse + PostToolUse)
# Then type: ls -la

# Check logs
cat ~/.claude/session-log.txt
cat ~/.claude/errors.log
cat ~/.claude/tool-usage.csv
```

---

## Documentation

Official docs: https://code.claude.com/docs/en/hooks
