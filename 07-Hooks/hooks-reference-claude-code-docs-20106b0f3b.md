---
category: "07-Hooks"
fetched_at: "2026-02-28T11:22:25Z"
source_url: "https://code.claude.com/docs/en/hooks"
title: "Hooks reference - Claude Code Docs"
---

# Hooks reference


Reference for Claude Code hook events, configuration schema, JSON input/output formats, exit codes, async hooks, HTTP hooks, prompt hooks, and MCP tool hooks.


For a quickstart guide with examples, see [Automate workflows with hooks](/docs/en/hooks-guide).

Hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code’s lifecycle. Use this reference to look up event schemas, configuration options, JSON input/output formats, and advanced features like async hooks, HTTP hooks, and MCP tool hooks. If you’re setting up hooks for the first time, start with the [guide](/docs/en/hooks-guide) instead.

## 

[​](#hook-lifecycle)

Hook lifecycle

Hooks fire at specific points during a Claude Code session. When an event fires and a matcher matches, Claude Code passes JSON context about the event to your hook handler. For command hooks, input arrives on stdin. For HTTP hooks, it arrives as the POST request body. Your handler can then inspect the input, take action, and optionally return a decision. Some events fire once per session, while others fire repeatedly inside the agentic loop:

The table below summarizes when each event fires. The [Hook events](#hook-events) section documents the full input schema and decision control options for each one.

| Event | When it fires |
|:---|:---|
| `SessionStart` | When a session begins or resumes |
| `UserPromptSubmit` | When you submit a prompt, before Claude processes it |
| `PreToolUse` | Before a tool call executes. Can block it |
| `PermissionRequest` | When a permission dialog appears |
| `PostToolUse` | After a tool call succeeds |
| `PostToolUseFailure` | After a tool call fails |
| `Notification` | When Claude Code sends a notification |
| `SubagentStart` | When a subagent is spawned |
| `SubagentStop` | When a subagent finishes |
| `Stop` | When Claude finishes responding |
| `TeammateIdle` | When an [agent team](/docs/en/agent-teams) teammate is about to go idle |
| `TaskCompleted` | When a task is being marked as completed |
| `ConfigChange` | When a configuration file changes during a session |
| `WorktreeCreate` | When a worktree is being created via `--worktree` or `isolation: "worktree"`. Replaces default git behavior |
| `WorktreeRemove` | When a worktree is being removed, either at session exit or when a subagent finishes |
| `PreCompact` | Before context compaction |
| `SessionEnd` | When a session terminates |

### 

[​](#how-a-hook-resolves)

How a hook resolves

To see how these pieces fit together, consider this `PreToolUse` hook that blocks destructive shell commands. The hook runs `block-rm.sh` before every Bash tool call:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block-rm.sh"
          }
        ]
      }
    ]
  }
}
```

The script reads the JSON input from stdin, extracts the command, and returns a `permissionDecision` of `"deny"` if it contains `rm -rf`:

Report incorrect code

Copy


``` shiki
#!/bin/bash
# .claude/hooks/block-rm.sh
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0  # allow the command
fi
```

Now suppose Claude Code decides to run `Bash "rm -rf /tmp/build"`. Here’s what happens:

1

[](#)

Event fires

The `PreToolUse` event fires. Claude Code sends the tool input as JSON on stdin to the hook:

Report incorrect code

Copy


``` shiki
{ "tool_name": "Bash", "tool_input": { "command": "rm -rf /tmp/build" }, ... }
```

2

[](#)

Matcher checks

The matcher `"Bash"` matches the tool name, so `block-rm.sh` runs. If you omit the matcher or use `"*"`, the hook runs on every occurrence of the event. Hooks only skip when a matcher is defined and doesn’t match.

3

[](#)

Hook handler runs

The script extracts `"rm -rf /tmp/build"` from the input and finds `rm -rf`, so it prints a decision to stdout:

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook"
  }
}
```

If the command had been safe (like `npm test`), the script would hit `exit 0` instead, which tells Claude Code to allow the tool call with no further action.

4

[](#)

Claude Code acts on the result

Claude Code reads the JSON decision, blocks the tool call, and shows Claude the reason.

The [Configuration](#configuration) section below documents the full schema, and each [hook event](#hook-events) section documents what input your command receives and what output it can return.

## 

[​](#configuration)

Configuration

Hooks are defined in JSON settings files. The configuration has three levels of nesting:

1.  Choose a [hook event](#hook-events) to respond to, like `PreToolUse` or `Stop`
2.  Add a [matcher group](#matcher-patterns) to filter when it fires, like “only for the Bash tool”
3.  Define one or more [hook handlers](#hook-handler-fields) to run when matched

See [How a hook resolves](#how-a-hook-resolves) above for a complete walkthrough with an annotated example.

This page uses specific terms for each level: **hook event** for the lifecycle point, **matcher group** for the filter, and **hook handler** for the shell command, HTTP endpoint, prompt, or agent that runs. “Hook” on its own refers to the general feature.

### 

[​](#hook-locations)

Hook locations

Where you define a hook determines its scope:

| Location | Scope | Shareable |
|:---|:---|:---|
| `~/.claude/settings.json` | All your projects | No, local to your machine |
| `.claude/settings.json` | Single project | Yes, can be committed to the repo |
| `.claude/settings.local.json` | Single project | No, gitignored |
| Managed policy settings | Organization-wide | Yes, admin-controlled |
| [Plugin](/docs/en/plugins) `hooks/hooks.json` | When plugin is enabled | Yes, bundled with the plugin |
| [Skill](/docs/en/skills) or [agent](/docs/en/sub-agents) frontmatter | While the component is active | Yes, defined in the component file |

For details on settings file resolution, see [settings](/docs/en/settings). Enterprise administrators can use `allowManagedHooksOnly` to block user, project, and plugin hooks. See [Hook configuration](/docs/en/settings#hook-configuration).

### 

[​](#matcher-patterns)

Matcher patterns

The `matcher` field is a regex string that filters when hooks fire. Use `"*"`, `""`, or omit `matcher` entirely to match all occurrences. Each event type matches on a different field:

| Event | What the matcher filters | Example matcher values |
|:---|:---|:---|
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest` | tool name | `Bash`, `Edit|Write`, `mcp__.*` |
| `SessionStart` | how the session started | `startup`, `resume`, `clear`, `compact` |
| `SessionEnd` | why the session ended | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other` |
| `Notification` | notification type | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` |
| `SubagentStart` | agent type | `Bash`, `Explore`, `Plan`, or custom agent names |
| `PreCompact` | what triggered compaction | `manual`, `auto` |
| `SubagentStop` | agent type | same values as `SubagentStart` |
| `ConfigChange` | configuration source | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| `UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove` | no matcher support | always fires on every occurrence |

The matcher is a regex, so `Edit|Write` matches either tool and `Notebook.*` matches any tool starting with Notebook. The matcher runs against a field from the [JSON input](#hook-input-and-output) that Claude Code sends to your hook on stdin. For tool events, that field is `tool_name`. Each [hook event](#hook-events) section lists the full set of matcher values and the input schema for that event. This example runs a linting script only when Claude writes or edits a file:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/lint-check.sh"
          }
        ]
      }
    ]
  }
}
```

`UserPromptSubmit`, `Stop`, `TeammateIdle`, `TaskCompleted`, `WorktreeCreate`, and `WorktreeRemove` don’t support matchers and always fire on every occurrence. If you add a `matcher` field to these events, it is silently ignored.

#### 

[​](#match-mcp-tools)

Match MCP tools

[MCP](/docs/en/mcp) server tools appear as regular tools in tool events (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`), so you can match them the same way you match any other tool name. MCP tools follow the naming pattern `mcp__<server>__<tool>`, for example:

- `mcp__memory__create_entities`: Memory server’s create entities tool
- `mcp__filesystem__read_file`: Filesystem server’s read file tool
- `mcp__github__search_repositories`: GitHub server’s search tool

Use regex patterns to target specific MCP tools or groups of tools:

- `mcp__memory__.*` matches all tools from the `memory` server
- `mcp__.*__write.*` matches any tool containing “write” from any server

This example logs all memory server operations and validates write operations from any MCP server:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Memory operation initiated' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/scripts/validate-mcp-write.py"
          }
        ]
      }
    ]
  }
}
```

### 

[​](#hook-handler-fields)

Hook handler fields

Each object in the inner `hooks` array is a hook handler: the shell command, HTTP endpoint, LLM prompt, or agent that runs when the matcher matches. There are four types:

- **[Command hooks](#command-hook-fields)** (`type: "command"`): run a shell command. Your script receives the event’s [JSON input](#hook-input-and-output) on stdin and communicates results back through exit codes and stdout.
- **[HTTP hooks](#http-hook-fields)** (`type: "http"`): send the event’s JSON input as an HTTP POST request to a URL. The endpoint communicates results back through the response body using the same [JSON output format](#json-output) as command hooks.
- **[Prompt hooks](#prompt-and-agent-hook-fields)** (`type: "prompt"`): send a prompt to a Claude model for single-turn evaluation. The model returns a yes/no decision as JSON. See [Prompt-based hooks](#prompt-based-hooks).
- **[Agent hooks](#prompt-and-agent-hook-fields)** (`type: "agent"`): spawn a subagent that can use tools like Read, Grep, and Glob to verify conditions before returning a decision. See [Agent-based hooks](#agent-based-hooks).

#### 

[​](#common-fields)

Common fields

These fields apply to all hook types:

| Field | Required | Description |
|:---|:---|:---|
| `type` | yes | `"command"`, `"http"`, `"prompt"`, or `"agent"` |
| `timeout` | no | Seconds before canceling. Defaults: 600 for command, 30 for prompt, 60 for agent |
| `statusMessage` | no | Custom spinner message displayed while the hook runs |
| `once` | no | If `true`, runs only once per session then is removed. Skills only, not agents. See [Hooks in skills and agents](#hooks-in-skills-and-agents) |

#### 

[​](#command-hook-fields)

Command hook fields

In addition to the [common fields](#common-fields), command hooks accept these fields:

| Field | Required | Description |
|:---|:---|:---|
| `command` | yes | Shell command to execute |
| `async` | no | If `true`, runs in the background without blocking. See [Run hooks in the background](#run-hooks-in-the-background) |

#### 

[​](#http-hook-fields)

HTTP hook fields

In addition to the [common fields](#common-fields), HTTP hooks accept these fields:

| Field | Required | Description |
|:---|:---|:---|
| `url` | yes | URL to send the POST request to |
| `headers` | no | Additional HTTP headers as key-value pairs. Values support environment variable interpolation using `$VAR_NAME` or `${VAR_NAME}` syntax. Only variables listed in `allowedEnvVars` are resolved |
| `allowedEnvVars` | no | List of environment variable names that may be interpolated into header values. References to unlisted variables are replaced with empty strings. Required for any env var interpolation to work |

Claude Code sends the hook’s [JSON input](#hook-input-and-output) as the POST request body with `Content-Type: application/json`. The response body uses the same [JSON output format](#json-output) as command hooks. Error handling differs from command hooks: non-2xx responses, connection failures, and timeouts all produce non-blocking errors that allow execution to continue. To block a tool call or deny a permission, return a 2xx response with a JSON body containing `decision: "block"` or a `hookSpecificOutput` with `permissionDecision: "deny"`. This example sends `PreToolUse` events to a local validation service, authenticating with a token from the `MY_TOKEN` environment variable:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "http",
            "url": "http://localhost:8080/hooks/pre-tool-use",
            "timeout": 30,
            "headers": {
              "Authorization": "Bearer $MY_TOKEN"
            },
            "allowedEnvVars": ["MY_TOKEN"]
          }
        ]
      }
    ]
  }
}
```

HTTP hooks must be configured by editing settings JSON directly. The `/hooks` interactive menu only supports adding command hooks.

#### 

[​](#prompt-and-agent-hook-fields)

Prompt and agent hook fields

In addition to the [common fields](#common-fields), prompt and agent hooks accept these fields:

| Field | Required | Description |
|:---|:---|:---|
| `prompt` | yes | Prompt text to send to the model. Use `$ARGUMENTS` as a placeholder for the hook input JSON |
| `model` | no | Model to use for evaluation. Defaults to a fast model |

All matching hooks run in parallel, and identical handlers are deduplicated automatically. Command hooks are deduplicated by command string, and HTTP hooks are deduplicated by URL. Handlers run in the current directory with Claude Code’s environment. The `$CLAUDE_CODE_REMOTE` environment variable is set to `"true"` in remote web environments and not set in the local CLI.

### 

[​](#reference-scripts-by-path)

Reference scripts by path

Use environment variables to reference hook scripts relative to the project or plugin root, regardless of the working directory when the hook runs:

- `$CLAUDE_PROJECT_DIR`: the project root. Wrap in quotes to handle paths with spaces.
- `${CLAUDE_PLUGIN_ROOT}`: the plugin’s root directory, for scripts bundled with a [plugin](/docs/en/plugins).

- Project scripts

- Plugin scripts

This example uses `$CLAUDE_PROJECT_DIR` to run a style checker from the project’s `.claude/hooks/` directory after any `Write` or `Edit` tool call:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-style.sh"
          }
        ]
      }
    ]
  }
}
```

Define plugin hooks in `hooks/hooks.json` with an optional top-level `description` field. When a plugin is enabled, its hooks merge with your user and project hooks.This example runs a formatting script bundled with the plugin:

Report incorrect code

Copy


``` shiki
{
  "description": "Automatic code formatting",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

See the [plugin components reference](/docs/en/plugins-reference#hooks) for details on creating plugin hooks.

### 

[​](#hooks-in-skills-and-agents)

Hooks in skills and agents

In addition to settings files and plugins, hooks can be defined directly in [skills](/docs/en/skills) and [subagents](/docs/en/sub-agents) using frontmatter. These hooks are scoped to the component’s lifecycle and only run when that component is active. All hook events are supported. For subagents, `Stop` hooks are automatically converted to `SubagentStop` since that is the event that fires when a subagent completes. Hooks use the same configuration format as settings-based hooks but are scoped to the component’s lifetime and cleaned up when it finishes. This skill defines a `PreToolUse` hook that runs a security validation script before each `Bash` command:

Report incorrect code

Copy


``` shiki
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
---
```

Agents use the same format in their YAML frontmatter.

### 

[​](#the-/hooks-menu)

The `/hooks` menu

Type `/hooks` in Claude Code to open the interactive hooks manager, where you can view, add, and delete hooks without editing settings files directly. For a step-by-step walkthrough, see [Set up your first hook](/docs/en/hooks-guide#set-up-your-first-hook) in the guide. Each hook in the menu is labeled with a bracket prefix indicating its source:

- `[User]`: from `~/.claude/settings.json`
- `[Project]`: from `.claude/settings.json`
- `[Local]`: from `.claude/settings.local.json`
- `[Plugin]`: from a plugin’s `hooks/hooks.json`, read-only

### 

[​](#disable-or-remove-hooks)

Disable or remove hooks

To remove a hook, delete its entry from the settings JSON file, or use the `/hooks` menu and select the hook to delete it. To temporarily disable all hooks without removing them, set `"disableAllHooks": true` in your settings file or use the toggle in the `/hooks` menu. There is no way to disable an individual hook while keeping it in the configuration. The `disableAllHooks` setting respects the managed settings hierarchy. If an administrator has configured hooks through managed policy settings, `disableAllHooks` set in user, project, or local settings cannot disable those managed hooks. Only `disableAllHooks` set at the managed settings level can disable managed hooks. Direct edits to hooks in settings files don’t take effect immediately. Claude Code captures a snapshot of hooks at startup and uses it throughout the session. This prevents malicious or accidental hook modifications from taking effect mid-session without your review. If hooks are modified externally, Claude Code warns you and requires review in the `/hooks` menu before changes apply.

## 

[​](#hook-input-and-output)

Hook input and output

Command hooks receive JSON data via stdin and communicate results through exit codes, stdout, and stderr. HTTP hooks receive the same JSON as the POST request body and communicate results through the HTTP response body. This section covers fields and behavior common to all events. Each event’s section under [Hook events](#hook-events) includes its specific input schema and decision control options.

### 

[​](#common-input-fields)

Common input fields

All hook events receive these fields as JSON, in addition to event-specific fields documented in each [hook event](#hook-events) section. For command hooks, this JSON arrives via stdin. For HTTP hooks, it arrives as the POST request body.

| Field | Description |
|:---|:---|
| `session_id` | Current session identifier |
| `transcript_path` | Path to conversation JSON |
| `cwd` | Current working directory when the hook is invoked |
| `permission_mode` | Current [permission mode](/docs/en/permissions#permission-modes): `"default"`, `"plan"`, `"acceptEdits"`, `"dontAsk"`, or `"bypassPermissions"` |
| `hook_event_name` | Name of the event that fired |

For example, a `PreToolUse` hook for a Bash command receives this on stdin:

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/home/user/.claude/projects/.../transcript.jsonl",
  "cwd": "/home/user/my-project",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test"
  }
}
```

The `tool_name` and `tool_input` fields are event-specific. Each [hook event](#hook-events) section documents the additional fields for that event.

### 

[​](#exit-code-output)

Exit code output

The exit code from your hook command tells Claude Code whether the action should proceed, be blocked, or be ignored. **Exit 0** means success. Claude Code parses stdout for [JSON output fields](#json-output). JSON output is only processed on exit 0. For most events, stdout is only shown in verbose mode (`Ctrl+O`). The exceptions are `UserPromptSubmit` and `SessionStart`, where stdout is added as context that Claude can see and act on. **Exit 2** means a blocking error. Claude Code ignores stdout and any JSON in it. Instead, stderr text is fed back to Claude as an error message. The effect depends on the event: `PreToolUse` blocks the tool call, `UserPromptSubmit` rejects the prompt, and so on. See [exit code 2 behavior](#exit-code-2-behavior-per-event) for the full list. **Any other exit code** is a non-blocking error. stderr is shown in verbose mode (`Ctrl+O`) and execution continues. For example, a hook command script that blocks dangerous Bash commands:

Report incorrect code

Copy


``` shiki
#!/bin/bash
# Reads JSON input from stdin, checks the command
command=$(jq -r '.tool_input.command' < /dev/stdin)

if [[ "$command" == rm* ]]; then
  echo "Blocked: rm commands are not allowed" >&2
  exit 2  # Blocking error: tool call is prevented
fi

exit 0  # Success: tool call proceeds
```

#### 

[​](#exit-code-2-behavior-per-event)

Exit code 2 behavior per event

Exit code 2 is the way a hook signals “stop, don’t do this.” The effect depends on the event, because some events represent actions that can be blocked (like a tool call that hasn’t happened yet) and others represent things that already happened or can’t be prevented.

| Hook event | Can block? | What happens on exit 2 |
|:---|:---|:---|
| `PreToolUse` | Yes | Blocks the tool call |
| `PermissionRequest` | Yes | Denies the permission |
| `UserPromptSubmit` | Yes | Blocks prompt processing and erases the prompt |
| `Stop` | Yes | Prevents Claude from stopping, continues the conversation |
| `SubagentStop` | Yes | Prevents the subagent from stopping |
| `TeammateIdle` | Yes | Prevents the teammate from going idle (teammate continues working) |
| `TaskCompleted` | Yes | Prevents the task from being marked as completed |
| `ConfigChange` | Yes | Blocks the configuration change from taking effect (except `policy_settings`) |
| `PostToolUse` | No | Shows stderr to Claude (tool already ran) |
| `PostToolUseFailure` | No | Shows stderr to Claude (tool already failed) |
| `Notification` | No | Shows stderr to user only |
| `SubagentStart` | No | Shows stderr to user only |
| `SessionStart` | No | Shows stderr to user only |
| `SessionEnd` | No | Shows stderr to user only |
| `PreCompact` | No | Shows stderr to user only |
| `WorktreeCreate` | Yes | Any non-zero exit code causes worktree creation to fail |
| `WorktreeRemove` | No | Failures are logged in debug mode only |

### 

[​](#http-response-handling)

HTTP response handling

HTTP hooks use HTTP status codes and response bodies instead of exit codes and stdout:

- **2xx with an empty body**: success, equivalent to exit code 0 with no output
- **2xx with a plain text body**: success, the text is added as context
- **2xx with a JSON body**: success, parsed using the same [JSON output](#json-output) schema as command hooks
- **Non-2xx status**: non-blocking error, execution continues
- **Connection failure or timeout**: non-blocking error, execution continues

Unlike command hooks, HTTP hooks cannot signal a blocking error through status codes alone. To block a tool call or deny a permission, return a 2xx response with a JSON body containing the appropriate decision fields.

### 

[​](#json-output)

JSON output

Exit codes let you allow or block, but JSON output gives you finer-grained control. Instead of exiting with code 2 to block, exit 0 and print a JSON object to stdout. Claude Code reads specific fields from that JSON to control behavior, including [decision control](#decision-control) for blocking, allowing, or escalating to the user.

You must choose one approach per hook, not both: either use exit codes alone for signaling, or exit 0 and print JSON for structured control. Claude Code only processes JSON on exit 0. If you exit 2, any JSON is ignored.

Your hook’s stdout must contain only the JSON object. If your shell profile prints text on startup, it can interfere with JSON parsing. See [JSON validation failed](/docs/en/hooks-guide#json-validation-failed) in the troubleshooting guide. The JSON object supports three kinds of fields:

- **Universal fields** like `continue` work across all events. These are listed in the table below.
- **Top-level `decision` and `reason`** are used by some events to block or provide feedback.
- **`hookSpecificOutput`** is a nested object for events that need richer control. It requires a `hookEventName` field set to the event name.

| Field | Default | Description |
|:---|:---|:---|
| `continue` | `true` | If `false`, Claude stops processing entirely after the hook runs. Takes precedence over any event-specific decision fields |
| `stopReason` | none | Message shown to the user when `continue` is `false`. Not shown to Claude |
| `suppressOutput` | `false` | If `true`, hides stdout from verbose mode output |
| `systemMessage` | none | Warning message shown to the user |

To stop Claude entirely regardless of event type:

Report incorrect code

Copy


``` shiki
{ "continue": false, "stopReason": "Build failed, fix errors before continuing" }
```

#### 

[​](#decision-control)

Decision control

Not every event supports blocking or controlling behavior through JSON. The events that do each use a different set of fields to express that decision. Use this table as a quick reference before writing a hook:

| Events | Decision pattern | Key fields |
|:---|:---|:---|
| UserPromptSubmit, PostToolUse, PostToolUseFailure, Stop, SubagentStop, ConfigChange | Top-level `decision` | `decision: "block"`, `reason` |
| TeammateIdle, TaskCompleted | Exit code only | Exit code 2 blocks the action, stderr is fed back as feedback |
| PreToolUse | `hookSpecificOutput` | `permissionDecision` (allow/deny/ask), `permissionDecisionReason` |
| PermissionRequest | `hookSpecificOutput` | `decision.behavior` (allow/deny) |
| WorktreeCreate | stdout path | Hook prints absolute path to created worktree. Non-zero exit fails creation |
| WorktreeRemove, Notification, SessionEnd, PreCompact | None | No decision control. Used for side effects like logging or cleanup |

Here are examples of each pattern in action:

- Top-level decision

- PreToolUse

- PermissionRequest

Used by `UserPromptSubmit`, `PostToolUse`, `PostToolUseFailure`, `Stop`, `SubagentStop`, and `ConfigChange`. The only value is `"block"`. To allow the action to proceed, omit `decision` from your JSON, or exit 0 without any JSON at all:

Report incorrect code

Copy


``` shiki
{
  "decision": "block",
  "reason": "Test suite must pass before proceeding"
}
```

Uses `hookSpecificOutput` for richer control: allow, deny, or escalate to the user. You can also modify tool input before it runs or inject additional context for Claude. See [PreToolUse decision control](#pretooluse-decision-control) for the full set of options.

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Database writes are not allowed"
  }
}
```

Uses `hookSpecificOutput` to allow or deny a permission request on behalf of the user. When allowing, you can also modify the tool’s input or apply permission rules so the user isn’t prompted again. See [PermissionRequest decision control](#permissionrequest-decision-control) for the full set of options.

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow",
      "updatedInput": {
        "command": "npm run lint"
      }
    }
  }
}
```

For extended examples including Bash command validation, prompt filtering, and auto-approval scripts, see [What you can automate](/docs/en/hooks-guide#what-you-can-automate) in the guide and the [Bash command validator reference implementation](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py).

## 

[​](#hook-events)

Hook events

Each event corresponds to a point in Claude Code’s lifecycle where hooks can run. The sections below are ordered to match the lifecycle: from session setup through the agentic loop to session end. Each section describes when the event fires, what matchers it supports, the JSON input it receives, and how to control behavior through output.

### 

[​](#sessionstart)

SessionStart

Runs when Claude Code starts a new session or resumes an existing session. Useful for loading development context like existing issues or recent changes to your codebase, or setting up environment variables. For static context that does not require a script, use [CLAUDE.md](/docs/en/memory) instead. SessionStart runs on every session, so keep these hooks fast. The matcher value corresponds to how the session was initiated:

| Matcher   | When it fires                          |
|:----------|:---------------------------------------|
| `startup` | New session                            |
| `resume`  | `--resume`, `--continue`, or `/resume` |
| `clear`   | `/clear`                               |
| `compact` | Auto or manual compaction              |

#### 

[​](#sessionstart-input)

SessionStart input

In addition to the [common input fields](#common-input-fields), SessionStart hooks receive `source`, `model`, and optionally `agent_type`. The `source` field indicates how the session started: `"startup"` for new sessions, `"resume"` for resumed sessions, `"clear"` after `/clear`, or `"compact"` after compaction. The `model` field contains the model identifier. If you start Claude Code with `claude --agent <name>`, an `agent_type` field contains the agent name.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "SessionStart",
  "source": "startup",
  "model": "claude-sonnet-4-6"
}
```

#### 

[​](#sessionstart-decision-control)

SessionStart decision control

Any text your hook script prints to stdout is added as context for Claude. In addition to the [JSON output fields](#json-output) available to all hooks, you can return these event-specific fields:

| Field | Description |
|:---|:---|
| `additionalContext` | String added to Claude’s context. Multiple hooks’ values are concatenated |

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "My additional context here"
  }
}
```

#### 

[​](#persist-environment-variables)

Persist environment variables

SessionStart hooks have access to the `CLAUDE_ENV_FILE` environment variable, which provides a file path where you can persist environment variables for subsequent Bash commands. To set individual environment variables, write `export` statements to `CLAUDE_ENV_FILE`. Use append (`>>`) to preserve variables set by other hooks:

Report incorrect code

Copy


``` shiki
#!/bin/bash

if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
  echo 'export DEBUG_LOG=true' >> "$CLAUDE_ENV_FILE"
  echo 'export PATH="$PATH:./node_modules/.bin"' >> "$CLAUDE_ENV_FILE"
fi

exit 0
```

To capture all environment changes from setup commands, compare the exported variables before and after:

Report incorrect code

Copy


``` shiki
#!/bin/bash

ENV_BEFORE=$(export -p | sort)

# Run your setup commands that modify the environment
source ~/.nvm/nvm.sh
nvm use 20

if [ -n "$CLAUDE_ENV_FILE" ]; then
  ENV_AFTER=$(export -p | sort)
  comm -13 <(echo "$ENV_BEFORE") <(echo "$ENV_AFTER") >> "$CLAUDE_ENV_FILE"
fi

exit 0
```

Any variables written to this file will be available in all subsequent Bash commands that Claude Code executes during the session.

`CLAUDE_ENV_FILE` is available for SessionStart hooks. Other hook types do not have access to this variable.

### 

[​](#userpromptsubmit)

UserPromptSubmit

Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts.

#### 

[​](#userpromptsubmit-input)

UserPromptSubmit input

In addition to the [common input fields](#common-input-fields), UserPromptSubmit hooks receive the `prompt` field containing the text the user submitted.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Write a function to calculate the factorial of a number"
}
```

#### 

[​](#userpromptsubmit-decision-control)

UserPromptSubmit decision control

`UserPromptSubmit` hooks can control whether a user prompt is processed and add context. All [JSON output fields](#json-output) are available. There are two ways to add context to the conversation on exit code 0:

- **Plain text stdout**: any non-JSON text written to stdout is added as context
- **JSON with `additionalContext`**: use the JSON format below for more control. The `additionalContext` field is added as context

Plain stdout is shown as hook output in the transcript. The `additionalContext` field is added more discretely. To block a prompt, return a JSON object with `decision` set to `"block"`:

| Field | Description |
|:---|:---|
| `decision` | `"block"` prevents the prompt from being processed and erases it from context. Omit to allow the prompt to proceed |
| `reason` | Shown to the user when `decision` is `"block"`. Not added to context |
| `additionalContext` | String added to Claude’s context |

Report incorrect code

Copy


``` shiki
{
  "decision": "block",
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "My additional context here"
  }
}
```

The JSON format isn’t required for simple use cases. To add context, you can print plain text to stdout with exit code 0. Use JSON when you need to block prompts or want more structured control.

### 

[​](#pretooluse)

PreToolUse

Runs after Claude creates tool parameters and before processing the tool call. Matches on tool name: `Bash`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Task`, `WebFetch`, `WebSearch`, and any [MCP tool names](#match-mcp-tools). Use [PreToolUse decision control](#pretooluse-decision-control) to allow, deny, or ask for permission to use the tool.

#### 

[​](#pretooluse-input)

PreToolUse input

In addition to the [common input fields](#common-input-fields), PreToolUse hooks receive `tool_name`, `tool_input`, and `tool_use_id`. The `tool_input` fields depend on the tool:

##### Bash

Executes shell commands.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `command` | string | `"npm test"` | The shell command to execute |
| `description` | string | `"Run test suite"` | Optional description of what the command does |
| `timeout` | number | `120000` | Optional timeout in milliseconds |
| `run_in_background` | boolean | `false` | Whether to run the command in background |

##### Write

Creates or overwrites a file.

| Field       | Type   | Example               | Description                        |
|:------------|:-------|:----------------------|:-----------------------------------|
| `file_path` | string | `"/path/to/file.txt"` | Absolute path to the file to write |
| `content`   | string | `"file content"`      | Content to write to the file       |

##### Edit

Replaces a string in an existing file.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `file_path` | string | `"/path/to/file.txt"` | Absolute path to the file to edit |
| `old_string` | string | `"original text"` | Text to find and replace |
| `new_string` | string | `"replacement text"` | Replacement text |
| `replace_all` | boolean | `false` | Whether to replace all occurrences |

##### Read

Reads file contents.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `file_path` | string | `"/path/to/file.txt"` | Absolute path to the file to read |
| `offset` | number | `10` | Optional line number to start reading from |
| `limit` | number | `50` | Optional number of lines to read |

##### Glob

Finds files matching a glob pattern.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `pattern` | string | `"**/*.ts"` | Glob pattern to match files against |
| `path` | string | `"/path/to/dir"` | Optional directory to search in. Defaults to current working directory |

##### Grep

Searches file contents with regular expressions.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `pattern` | string | `"TODO.*fix"` | Regular expression pattern to search for |
| `path` | string | `"/path/to/dir"` | Optional file or directory to search in |
| `glob` | string | `"*.ts"` | Optional glob pattern to filter files |
| `output_mode` | string | `"content"` | `"content"`, `"files_with_matches"`, or `"count"`. Defaults to `"files_with_matches"` |
| `-i` | boolean | `true` | Case insensitive search |
| `multiline` | boolean | `false` | Enable multiline matching |

##### WebFetch

Fetches and processes web content.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `url` | string | `"https://example.com/api"` | URL to fetch content from |
| `prompt` | string | `"Extract the API endpoints"` | Prompt to run on the fetched content |

##### WebSearch

Searches the web.

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `query` | string | `"react hooks best practices"` | Search query |
| `allowed_domains` | array | `["docs.example.com"]` | Optional: only include results from these domains |
| `blocked_domains` | array | `["spam.example.com"]` | Optional: exclude results from these domains |

##### Task

Spawns a [subagent](/docs/en/sub-agents).

| Field | Type | Example | Description |
|:---|:---|:---|:---|
| `prompt` | string | `"Find all API endpoints"` | The task for the agent to perform |
| `description` | string | `"Find API endpoints"` | Short description of the task |
| `subagent_type` | string | `"Explore"` | Type of specialized agent to use |
| `model` | string | `"sonnet"` | Optional model alias to override the default |

#### 

[​](#pretooluse-decision-control)

PreToolUse decision control

`PreToolUse` hooks can control whether a tool call proceeds. Unlike other hooks that use a top-level `decision` field, PreToolUse returns its decision inside a `hookSpecificOutput` object. This gives it richer control: three outcomes (allow, deny, or ask) plus the ability to modify tool input before execution.

| Field | Description |
|:---|:---|
| `permissionDecision` | `"allow"` bypasses the permission system, `"deny"` prevents the tool call, `"ask"` prompts the user to confirm |
| `permissionDecisionReason` | For `"allow"` and `"ask"`, shown to the user but not Claude. For `"deny"`, shown to Claude |
| `updatedInput` | Modifies the tool’s input parameters before execution. Combine with `"allow"` to auto-approve, or `"ask"` to show the modified input to the user |
| `additionalContext` | String added to Claude’s context before the tool executes |

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "My reason here",
    "updatedInput": {
      "field_to_modify": "new value"
    },
    "additionalContext": "Current environment: production. Proceed with caution."
  }
}
```

PreToolUse previously used top-level `decision` and `reason` fields, but these are deprecated for this event. Use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason` instead. The deprecated values `"approve"` and `"block"` map to `"allow"` and `"deny"` respectively. Other events like PostToolUse and Stop continue to use top-level `decision` and `reason` as their current format.

### 

[​](#permissionrequest)

PermissionRequest

Runs when the user is shown a permission dialog. Use [PermissionRequest decision control](#permissionrequest-decision-control) to allow or deny on behalf of the user. Matches on tool name, same values as PreToolUse.

#### 

[​](#permissionrequest-input)

PermissionRequest input

PermissionRequest hooks receive `tool_name` and `tool_input` fields like PreToolUse hooks, but without `tool_use_id`. An optional `permission_suggestions` array contains the “always allow” options the user would normally see in the permission dialog. The difference is when the hook fires: PermissionRequest hooks run when a permission dialog is about to be shown to the user, while PreToolUse hooks run before tool execution regardless of permission status.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "PermissionRequest",
  "tool_name": "Bash",
  "tool_input": {
    "command": "rm -rf node_modules",
    "description": "Remove node_modules directory"
  },
  "permission_suggestions": [
    { "type": "toolAlwaysAllow", "tool": "Bash" }
  ]
}
```

#### 

[​](#permissionrequest-decision-control)

PermissionRequest decision control

`PermissionRequest` hooks can allow or deny permission requests. In addition to the [JSON output fields](#json-output) available to all hooks, your hook script can return a `decision` object with these event-specific fields:

| Field | Description |
|:---|:---|
| `behavior` | `"allow"` grants the permission, `"deny"` denies it |
| `updatedInput` | For `"allow"` only: modifies the tool’s input parameters before execution |
| `updatedPermissions` | For `"allow"` only: applies permission rule updates, equivalent to the user selecting an “always allow” option |
| `message` | For `"deny"` only: tells Claude why the permission was denied |
| `interrupt` | For `"deny"` only: if `true`, stops Claude |

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow",
      "updatedInput": {
        "command": "npm run lint"
      }
    }
  }
}
```

### 

[​](#posttooluse)

PostToolUse

Runs immediately after a tool completes successfully. Matches on tool name, same values as PreToolUse.

#### 

[​](#posttooluse-input)

PostToolUse input

`PostToolUse` hooks fire after a tool has already executed successfully. The input includes both `tool_input`, the arguments sent to the tool, and `tool_response`, the result it returned. The exact schema for both depends on the tool.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_response": {
    "filePath": "/path/to/file.txt",
    "success": true
  },
  "tool_use_id": "toolu_01ABC123..."
}
```

#### 

[​](#posttooluse-decision-control)

PostToolUse decision control

`PostToolUse` hooks can provide feedback to Claude after tool execution. In addition to the [JSON output fields](#json-output) available to all hooks, your hook script can return these event-specific fields:

| Field | Description |
|:---|:---|
| `decision` | `"block"` prompts Claude with the `reason`. Omit to allow the action to proceed |
| `reason` | Explanation shown to Claude when `decision` is `"block"` |
| `additionalContext` | Additional context for Claude to consider |
| `updatedMCPToolOutput` | For [MCP tools](#match-mcp-tools) only: replaces the tool’s output with the provided value |

Report incorrect code

Copy


``` shiki
{
  "decision": "block",
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Additional information for Claude"
  }
}
```

### 

[​](#posttoolusefailure)

PostToolUseFailure

Runs when a tool execution fails. This event fires for tool calls that throw errors or return failure results. Use this to log failures, send alerts, or provide corrective feedback to Claude. Matches on tool name, same values as PreToolUse.

#### 

[​](#posttoolusefailure-input)

PostToolUseFailure input

PostToolUseFailure hooks receive the same `tool_name` and `tool_input` fields as PostToolUse, along with error information as top-level fields:

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "PostToolUseFailure",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test",
    "description": "Run test suite"
  },
  "tool_use_id": "toolu_01ABC123...",
  "error": "Command exited with non-zero status code 1",
  "is_interrupt": false
}
```

| Field | Description |
|:---|:---|
| `error` | String describing what went wrong |
| `is_interrupt` | Optional boolean indicating whether the failure was caused by user interruption |

#### 

[​](#posttoolusefailure-decision-control)

PostToolUseFailure decision control

`PostToolUseFailure` hooks can provide context to Claude after a tool failure. In addition to the [JSON output fields](#json-output) available to all hooks, your hook script can return these event-specific fields:

| Field | Description |
|:---|:---|
| `additionalContext` | Additional context for Claude to consider alongside the error |

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUseFailure",
    "additionalContext": "Additional information about the failure for Claude"
  }
}
```

### 

[​](#notification)

Notification

Runs when Claude Code sends notifications. Matches on notification type: `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`. Omit the matcher to run hooks for all notification types. Use separate matchers to run different handlers depending on the notification type. This configuration triggers a permission-specific alert script when Claude needs permission approval and a different notification when Claude has been idle:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/permission-alert.sh"
          }
        ]
      },
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/idle-notification.sh"
          }
        ]
      }
    ]
  }
}
```

#### 

[​](#notification-input)

Notification input

In addition to the [common input fields](#common-input-fields), Notification hooks receive `message` with the notification text, an optional `title`, and `notification_type` indicating which type fired.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "Notification",
  "message": "Claude needs your permission to use Bash",
  "title": "Permission needed",
  "notification_type": "permission_prompt"
}
```

Notification hooks cannot block or modify notifications. In addition to the [JSON output fields](#json-output) available to all hooks, you can return `additionalContext` to add context to the conversation:

| Field               | Description                      |
|:--------------------|:---------------------------------|
| `additionalContext` | String added to Claude’s context |

### 

[​](#subagentstart)

SubagentStart

Runs when a Claude Code subagent is spawned via the Task tool. Supports matchers to filter by agent type name (built-in agents like `Bash`, `Explore`, `Plan`, or custom agent names from `.claude/agents/`).

#### 

[​](#subagentstart-input)

SubagentStart input

In addition to the [common input fields](#common-input-fields), SubagentStart hooks receive `agent_id` with the unique identifier for the subagent and `agent_type` with the agent name (built-in agents like `"Bash"`, `"Explore"`, `"Plan"`, or custom agent names).

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "SubagentStart",
  "agent_id": "agent-abc123",
  "agent_type": "Explore"
}
```

SubagentStart hooks cannot block subagent creation, but they can inject context into the subagent. In addition to the [JSON output fields](#json-output) available to all hooks, you can return:

| Field               | Description                            |
|:--------------------|:---------------------------------------|
| `additionalContext` | String added to the subagent’s context |

Report incorrect code

Copy


``` shiki
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Follow security guidelines for this task"
  }
}
```

### 

[​](#subagentstop)

SubagentStop

Runs when a Claude Code subagent has finished responding. Matches on agent type, same values as SubagentStart.

#### 

[​](#subagentstop-input)

SubagentStop input

In addition to the [common input fields](#common-input-fields), SubagentStop hooks receive `stop_hook_active`, `agent_id`, `agent_type`, `agent_transcript_path`, and `last_assistant_message`. The `agent_type` field is the value used for matcher filtering. The `transcript_path` is the main session’s transcript, while `agent_transcript_path` is the subagent’s own transcript stored in a nested `subagents/` folder. The `last_assistant_message` field contains the text content of the subagent’s final response, so hooks can access it without parsing the transcript file.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../abc123.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "SubagentStop",
  "stop_hook_active": false,
  "agent_id": "def456",
  "agent_type": "Explore",
  "agent_transcript_path": "~/.claude/projects/.../abc123/subagents/agent-def456.jsonl",
  "last_assistant_message": "Analysis complete. Found 3 potential issues..."
}
```

SubagentStop hooks use the same decision control format as [Stop hooks](#stop-decision-control).

### 

[​](#stop)

Stop

Runs when the main Claude Code agent has finished responding. Does not run if the stoppage occurred due to a user interrupt.

#### 

[​](#stop-input)

Stop input

In addition to the [common input fields](#common-input-fields), Stop hooks receive `stop_hook_active` and `last_assistant_message`. The `stop_hook_active` field is `true` when Claude Code is already continuing as a result of a stop hook. Check this value or process the transcript to prevent Claude Code from running indefinitely. The `last_assistant_message` field contains the text content of Claude’s final response, so hooks can access it without parsing the transcript file.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "Stop",
  "stop_hook_active": true,
  "last_assistant_message": "I've completed the refactoring. Here's a summary..."
}
```

#### 

[​](#stop-decision-control)

Stop decision control

`Stop` and `SubagentStop` hooks can control whether Claude continues. In addition to the [JSON output fields](#json-output) available to all hooks, your hook script can return these event-specific fields:

| Field | Description |
|:---|:---|
| `decision` | `"block"` prevents Claude from stopping. Omit to allow Claude to stop |
| `reason` | Required when `decision` is `"block"`. Tells Claude why it should continue |

Report incorrect code

Copy


``` shiki
{
  "decision": "block",
  "reason": "Must be provided when Claude is blocked from stopping"
}
```

### 

[​](#teammateidle)

TeammateIdle

Runs when an [agent team](/docs/en/agent-teams) teammate is about to go idle after finishing its turn. Use this to enforce quality gates before a teammate stops working, such as requiring passing lint checks or verifying that output files exist. When a `TeammateIdle` hook exits with code 2, the teammate receives the stderr message as feedback and continues working instead of going idle. TeammateIdle hooks do not support matchers and fire on every occurrence.

#### 

[​](#teammateidle-input)

TeammateIdle input

In addition to the [common input fields](#common-input-fields), TeammateIdle hooks receive `teammate_name` and `team_name`.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "TeammateIdle",
  "teammate_name": "researcher",
  "team_name": "my-project"
}
```

| Field           | Description                                   |
|:----------------|:----------------------------------------------|
| `teammate_name` | Name of the teammate that is about to go idle |
| `team_name`     | Name of the team                              |

#### 

[​](#teammateidle-decision-control)

TeammateIdle decision control

TeammateIdle hooks use exit codes only, not JSON decision control. This example checks that a build artifact exists before allowing a teammate to go idle:

Report incorrect code

Copy


``` shiki
#!/bin/bash

if [ ! -f "./dist/output.js" ]; then
  echo "Build artifact missing. Run the build before stopping." >&2
  exit 2
fi

exit 0
```

### 

[​](#taskcompleted)

TaskCompleted

Runs when a task is being marked as completed. This fires in two situations: when any agent explicitly marks a task as completed through the TaskUpdate tool, or when an [agent team](/docs/en/agent-teams) teammate finishes its turn with in-progress tasks. Use this to enforce completion criteria like passing tests or lint checks before a task can close. When a `TaskCompleted` hook exits with code 2, the task is not marked as completed and the stderr message is fed back to the model as feedback. TaskCompleted hooks do not support matchers and fire on every occurrence.

#### 

[​](#taskcompleted-input)

TaskCompleted input

In addition to the [common input fields](#common-input-fields), TaskCompleted hooks receive `task_id`, `task_subject`, and optionally `task_description`, `teammate_name`, and `team_name`.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "TaskCompleted",
  "task_id": "task-001",
  "task_subject": "Implement user authentication",
  "task_description": "Add login and signup endpoints",
  "teammate_name": "implementer",
  "team_name": "my-project"
}
```

| Field | Description |
|:---|:---|
| `task_id` | Identifier of the task being completed |
| `task_subject` | Title of the task |
| `task_description` | Detailed description of the task. May be absent |
| `teammate_name` | Name of the teammate completing the task. May be absent |
| `team_name` | Name of the team. May be absent |

#### 

[​](#taskcompleted-decision-control)

TaskCompleted decision control

TaskCompleted hooks use exit codes only, not JSON decision control. This example runs tests and blocks task completion if they fail:

Report incorrect code

Copy


``` shiki
#!/bin/bash
INPUT=$(cat)
TASK_SUBJECT=$(echo "$INPUT" | jq -r '.task_subject')

# Run the test suite
if ! npm test 2>&1; then
  echo "Tests not passing. Fix failing tests before completing: $TASK_SUBJECT" >&2
  exit 2
fi

exit 0
```

### 

[​](#configchange)

ConfigChange

Runs when a configuration file changes during a session. Use this to audit settings changes, enforce security policies, or block unauthorized modifications to configuration files. ConfigChange hooks fire for changes to settings files, managed policy settings, and skill files. The `source` field in the input tells you which type of configuration changed, and the optional `file_path` field provides the path to the changed file. The matcher filters on the configuration source:

| Matcher            | When it fires                             |
|:-------------------|:------------------------------------------|
| `user_settings`    | `~/.claude/settings.json` changes         |
| `project_settings` | `.claude/settings.json` changes           |
| `local_settings`   | `.claude/settings.local.json` changes     |
| `policy_settings`  | Managed policy settings change            |
| `skills`           | A skill file in `.claude/skills/` changes |

This example logs all configuration changes for security auditing:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "ConfigChange": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/audit-config-change.sh"
          }
        ]
      }
    ]
  }
}
```

#### 

[​](#configchange-input)

ConfigChange input

In addition to the [common input fields](#common-input-fields), ConfigChange hooks receive `source` and optionally `file_path`. The `source` field indicates which configuration type changed, and `file_path` provides the path to the specific file that was modified.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "ConfigChange",
  "source": "project_settings",
  "file_path": "/Users/.../my-project/.claude/settings.json"
}
```

#### 

[​](#configchange-decision-control)

ConfigChange decision control

ConfigChange hooks can block configuration changes from taking effect. Use exit code 2 or a JSON `decision` to prevent the change. When blocked, the new settings are not applied to the running session.

| Field | Description |
|:---|:---|
| `decision` | `"block"` prevents the configuration change from being applied. Omit to allow the change |
| `reason` | Explanation shown to the user when `decision` is `"block"` |

Report incorrect code

Copy


``` shiki
{
  "decision": "block",
  "reason": "Configuration changes to project settings require admin approval"
}
```

`policy_settings` changes cannot be blocked. Hooks still fire for `policy_settings` sources, so you can use them for audit logging, but any blocking decision is ignored. This ensures enterprise-managed settings always take effect.

### 

[​](#worktreecreate)

WorktreeCreate

When you run `claude --worktree` or a [subagent uses `isolation: "worktree"`](/docs/en/sub-agents#choose-the-subagent-scope), Claude Code creates an isolated working copy using `git worktree`. If you configure a WorktreeCreate hook, it replaces the default git behavior, letting you use a different version control system like SVN, Perforce, or Mercurial. The hook must print the absolute path to the created worktree directory on stdout. Claude Code uses this path as the working directory for the isolated session. This example creates an SVN working copy and prints the path for Claude Code to use. Replace the repository URL with your own:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'NAME=$(jq -r .name); DIR=\"$HOME/.claude/worktrees/$NAME\"; svn checkout https://svn.example.com/repo/trunk \"$DIR\" >&2 && echo \"$DIR\"'"
          }
        ]
      }
    ]
  }
}
```

The hook reads the worktree `name` from the JSON input on stdin, checks out a fresh copy into a new directory, and prints the directory path. The `echo` on the last line is what Claude Code reads as the worktree path. Redirect any other output to stderr so it doesn’t interfere with the path.

#### 

[​](#worktreecreate-input)

WorktreeCreate input

In addition to the [common input fields](#common-input-fields), WorktreeCreate hooks receive the `name` field. This is a slug identifier for the new worktree, either specified by the user or auto-generated (for example, `bold-oak-a3f2`).

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "WorktreeCreate",
  "name": "feature-auth"
}
```

#### 

[​](#worktreecreate-output)

WorktreeCreate output

The hook must print the absolute path to the created worktree directory on stdout. If the hook fails or produces no output, worktree creation fails with an error. WorktreeCreate hooks do not use the standard allow/block decision model. Instead, the hook’s success or failure determines the outcome. Only `type: "command"` hooks are supported.

### 

[​](#worktreeremove)

WorktreeRemove

The cleanup counterpart to [WorktreeCreate](#worktreecreate). This hook fires when a worktree is being removed, either when you exit a `--worktree` session and choose to remove it, or when a subagent with `isolation: "worktree"` finishes. For git-based worktrees, Claude handles cleanup automatically with `git worktree remove`. If you configured a WorktreeCreate hook for a non-git version control system, pair it with a WorktreeRemove hook to handle cleanup. Without one, the worktree directory is left on disk. Claude Code passes the path that WorktreeCreate printed on stdout as `worktree_path` in the hook input. This example reads that path and removes the directory:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "WorktreeRemove": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'jq -r .worktree_path | xargs rm -rf'"
          }
        ]
      }
    ]
  }
}
```

#### 

[​](#worktreeremove-input)

WorktreeRemove input

In addition to the [common input fields](#common-input-fields), WorktreeRemove hooks receive the `worktree_path` field, which is the absolute path to the worktree being removed.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "WorktreeRemove",
  "worktree_path": "/Users/.../my-project/.claude/worktrees/feature-auth"
}
```

WorktreeRemove hooks have no decision control. They cannot block worktree removal but can perform cleanup tasks like removing version control state or archiving changes. Hook failures are logged in debug mode only. Only `type: "command"` hooks are supported.

### 

[​](#precompact)

PreCompact

Runs before Claude Code is about to run a compact operation. The matcher value indicates whether compaction was triggered manually or automatically:

| Matcher  | When it fires                                |
|:---------|:---------------------------------------------|
| `manual` | `/compact`                                   |
| `auto`   | Auto-compact when the context window is full |

#### 

[​](#precompact-input)

PreCompact input

In addition to the [common input fields](#common-input-fields), PreCompact hooks receive `trigger` and `custom_instructions`. For `manual`, `custom_instructions` contains what the user passes into `/compact`. For `auto`, `custom_instructions` is empty.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "PreCompact",
  "trigger": "manual",
  "custom_instructions": ""
}
```

### 

[​](#sessionend)

SessionEnd

Runs when a Claude Code session ends. Useful for cleanup tasks, logging session statistics, or saving session state. Supports matchers to filter by exit reason. The `reason` field in the hook input indicates why the session ended:

| Reason                        | Description                                |
|:------------------------------|:-------------------------------------------|
| `clear`                       | Session cleared with `/clear` command      |
| `logout`                      | User logged out                            |
| `prompt_input_exit`           | User exited while prompt input was visible |
| `bypass_permissions_disabled` | Bypass permissions mode was disabled       |
| `other`                       | Other exit reasons                         |

#### 

[​](#sessionend-input)

SessionEnd input

In addition to the [common input fields](#common-input-fields), SessionEnd hooks receive a `reason` field indicating why the session ended. See the [reason table](#sessionend) above for all values.

Report incorrect code

Copy


``` shiki
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}
```

SessionEnd hooks have no decision control. They cannot block session termination but can perform cleanup tasks.

## 

[​](#prompt-based-hooks)

Prompt-based hooks

In addition to Bash command hooks (`type: "command"`), Claude Code supports prompt-based hooks (`type: "prompt"`) that use an LLM to evaluate whether to allow or block an action, and agent hooks (`type: "agent"`) that spawn an agentic verifier with tool access. Not all events support every hook type. Events that support all three hook types (`command`, `prompt`, and `agent`):

- `PermissionRequest`
- `PostToolUse`
- `PostToolUseFailure`
- `PreToolUse`
- `Stop`
- `SubagentStop`
- `TaskCompleted`
- `UserPromptSubmit`

Events that only support `type: "command"` hooks:

- `ConfigChange`
- `Notification`
- `PreCompact`
- `SessionEnd`
- `SessionStart`
- `SubagentStart`
- `TeammateIdle`
- `WorktreeCreate`
- `WorktreeRemove`

### 

[​](#how-prompt-based-hooks-work)

How prompt-based hooks work

Instead of executing a Bash command, prompt-based hooks:

1.  Send the hook input and your prompt to a Claude model, Haiku by default
2.  The LLM responds with structured JSON containing a decision
3.  Claude Code processes the decision automatically

### 

[​](#prompt-hook-configuration)

Prompt hook configuration

Set `type` to `"prompt"` and provide a `prompt` string instead of a `command`. Use the `$ARGUMENTS` placeholder to inject the hook’s JSON input data into your prompt text. Claude Code sends the combined prompt and input to a fast Claude model, which returns a JSON decision. This `Stop` hook asks the LLM to evaluate whether all tasks are complete before allowing Claude to finish:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude should stop: $ARGUMENTS. Check if all tasks are complete."
          }
        ]
      }
    ]
  }
}
```

| Field | Required | Description |
|:---|:---|:---|
| `type` | yes | Must be `"prompt"` |
| `prompt` | yes | The prompt text to send to the LLM. Use `$ARGUMENTS` as a placeholder for the hook input JSON. If `$ARGUMENTS` is not present, input JSON is appended to the prompt |
| `model` | no | Model to use for evaluation. Defaults to a fast model |
| `timeout` | no | Timeout in seconds. Default: 30 |

### 

[​](#response-schema)

Response schema

The LLM must respond with JSON containing:

Report incorrect code

Copy


``` shiki
{
  "ok": true | false,
  "reason": "Explanation for the decision"
}
```

| Field    | Description                                                |
|:---------|:-----------------------------------------------------------|
| `ok`     | `true` allows the action, `false` prevents it              |
| `reason` | Required when `ok` is `false`. Explanation shown to Claude |

### 

[​](#example-multi-criteria-stop-hook)

Example: Multi-criteria Stop hook

This `Stop` hook uses a detailed prompt to check three conditions before allowing Claude to stop. If `"ok"` is `false`, Claude continues working with the provided reason as its next instruction. `SubagentStop` hooks use the same format to evaluate whether a [subagent](/docs/en/sub-agents) should stop:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "You are evaluating whether Claude should stop working. Context: $ARGUMENTS\n\nAnalyze the conversation and determine if:\n1. All user-requested tasks are complete\n2. Any errors need to be addressed\n3. Follow-up work is needed\n\nRespond with JSON: {\"ok\": true} to allow stopping, or {\"ok\": false, \"reason\": \"your explanation\"} to continue working.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## 

[​](#agent-based-hooks)

Agent-based hooks

Agent-based hooks (`type: "agent"`) are like prompt-based hooks but with multi-turn tool access. Instead of a single LLM call, an agent hook spawns a subagent that can read files, search code, and inspect the codebase to verify conditions. Agent hooks support the same events as prompt-based hooks.

### 

[​](#how-agent-hooks-work)

How agent hooks work

When an agent hook fires:

1.  Claude Code spawns a subagent with your prompt and the hook’s JSON input
2.  The subagent can use tools like Read, Grep, and Glob to investigate
3.  After up to 50 turns, the subagent returns a structured `{ "ok": true/false }` decision
4.  Claude Code processes the decision the same way as a prompt hook

Agent hooks are useful when verification requires inspecting actual files or test output, not just evaluating the hook input data alone.

### 

[​](#agent-hook-configuration)

Agent hook configuration

Set `type` to `"agent"` and provide a `prompt` string. The configuration fields are the same as [prompt hooks](#prompt-hook-configuration), with a longer default timeout:

| Field | Required | Description |
|:---|:---|:---|
| `type` | yes | Must be `"agent"` |
| `prompt` | yes | Prompt describing what to verify. Use `$ARGUMENTS` as a placeholder for the hook input JSON |
| `model` | no | Model to use. Defaults to a fast model |
| `timeout` | no | Timeout in seconds. Default: 60 |

The response schema is the same as prompt hooks: `{ "ok": true }` to allow or `{ "ok": false, "reason": "..." }` to block. This `Stop` hook verifies that all unit tests pass before allowing Claude to finish:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "agent",
            "prompt": "Verify that all unit tests pass. Run the test suite and check the results. $ARGUMENTS",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

## 

[​](#run-hooks-in-the-background)

Run hooks in the background

By default, hooks block Claude’s execution until they complete. For long-running tasks like deployments, test suites, or external API calls, set `"async": true` to run the hook in the background while Claude continues working. Async hooks cannot block or control Claude’s behavior: response fields like `decision`, `permissionDecision`, and `continue` have no effect, because the action they would have controlled has already completed.

### 

[​](#configure-an-async-hook)

Configure an async hook

Add `"async": true` to a command hook’s configuration to run it in the background without blocking Claude. This field is only available on `type: "command"` hooks. This hook runs a test script after every `Write` tool call. Claude continues working immediately while `run-tests.sh` executes for up to 120 seconds. When the script finishes, its output is delivered on the next conversation turn:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/run-tests.sh",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

The `timeout` field sets the maximum time in seconds for the background process. If not specified, async hooks use the same 10-minute default as sync hooks.

### 

[​](#how-async-hooks-execute)

How async hooks execute

When an async hook fires, Claude Code starts the hook process and immediately continues without waiting for it to finish. The hook receives the same JSON input via stdin as a synchronous hook. After the background process exits, if the hook produced a JSON response with a `systemMessage` or `additionalContext` field, that content is delivered to Claude as context on the next conversation turn.

### 

[​](#example-run-tests-after-file-changes)

Example: run tests after file changes

This hook starts a test suite in the background whenever Claude writes a file, then reports the results back to Claude when the tests finish. Save this script to `.claude/hooks/run-tests-async.sh` in your project and make it executable with `chmod +x`:

Report incorrect code

Copy


``` shiki
#!/bin/bash
# run-tests-async.sh

# Read hook input from stdin
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only run tests for source files
if [[ "$FILE_PATH" != *.ts && "$FILE_PATH" != *.js ]]; then
  exit 0
fi

# Run tests and report results via systemMessage
RESULT=$(npm test 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "{\"systemMessage\": \"Tests passed after editing $FILE_PATH\"}"
else
  echo "{\"systemMessage\": \"Tests failed after editing $FILE_PATH: $RESULT\"}"
fi
```

Then add this configuration to `.claude/settings.json` in your project root. The `async: true` flag lets Claude keep working while tests run:

Report incorrect code

Copy


``` shiki
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/run-tests-async.sh",
            "async": true,
            "timeout": 300
          }
        ]
      }
    ]
  }
}
```

### 

[​](#limitations)

Limitations

Async hooks have several constraints compared to synchronous hooks:

- Only `type: "command"` hooks support `async`. Prompt-based hooks cannot run asynchronously.
- Async hooks cannot block tool calls or return decisions. By the time the hook completes, the triggering action has already proceeded.
- Hook output is delivered on the next conversation turn. If the session is idle, the response waits until the next user interaction.
- Each execution creates a separate background process. There is no deduplication across multiple firings of the same async hook.

## 

[​](#security-considerations)

Security considerations

### 

[​](#disclaimer)

Disclaimer

Command hooks run with your system user’s full permissions.

Command hooks execute shell commands with your full user permissions. They can modify, delete, or access any files your user account can access. Review and test all hook commands before adding them to your configuration.

### 

[​](#security-best-practices)

Security best practices

Keep these practices in mind when writing hooks:

- **Validate and sanitize inputs**: never trust input data blindly
- **Always quote shell variables**: use `"$VAR"` not `$VAR`
- **Block path traversal**: check for `..` in file paths
- **Use absolute paths**: specify full paths for scripts, using `"$CLAUDE_PROJECT_DIR"` for the project root
- **Skip sensitive files**: avoid `.env`, `.git/`, keys, etc.

## 

[​](#debug-hooks)

Debug hooks

Run `claude --debug` to see hook execution details, including which hooks matched, their exit codes, and output. Toggle verbose mode with `Ctrl+O` to see hook progress in the transcript.

Report incorrect code

Copy


``` shiki
[DEBUG] Executing hooks for PostToolUse:Write
[DEBUG] Getting matching hook commands for PostToolUse with query: Write
[DEBUG] Found 1 hook matchers in settings
[DEBUG] Matched 1 hooks for query "Write"
[DEBUG] Found 1 hook commands to execute
[DEBUG] Executing hook command: <Your command> with timeout 600000ms
[DEBUG] Hook command completed with status 0: <Your stdout>
```

For troubleshooting common issues like hooks not firing, infinite Stop hook loops, or configuration errors, see [Limitations and troubleshooting](/docs/en/hooks-guide#limitations-and-troubleshooting) in the guide.
