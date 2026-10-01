---
title: "Automate actions with hooks - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/hooks-guide"
category: "07-Hooks"
fetched_at: "2026-09-30T06:30:35Z"
tags: ["claude-code", "hooks"]
---

## On this page

- [Set up your first hook](#set-up-your-first-hook)
- [What you can automate](#what-you-can-automate)
  - [Get notified when Claude needs input](#get-notified-when-claude-needs-input)
  - [Auto-format code after edits](#auto-format-code-after-edits)
  - [Block edits to protected files](#block-edits-to-protected-files)
  - [Re-inject context after compaction](#re-inject-context-after-compaction)
  - [Audit configuration changes](#audit-configuration-changes)
  - [Reload environment when directory or files change](#reload-environment-when-directory-or-files-change)
  - [Auto-approve specific permission prompts](#auto-approve-specific-permission-prompts)
- [How hooks work](#how-hooks-work)
  - [Combine results from multiple hooks](#combine-results-from-multiple-hooks)
  - [Read input and return output](#read-input-and-return-output)
  - [Hook input](#hook-input)
  - [Hook output](#hook-output)
  - [Structured JSON output](#structured-json-output)
  - [Filter hooks with matchers](#filter-hooks-with-matchers)
  - [Filter by tool name and arguments with the if field](#filter-by-tool-name-and-arguments-with-the-if-field)
  - [Configure hook location](#configure-hook-location)
- [Prompt-based hooks](#prompt-based-hooks)
- [Agent-based hooks](#agent-based-hooks)
- [HTTP hooks](#http-hooks)
- [Limitations and troubleshooting](#limitations-and-troubleshooting)
  - [Limitations](#limitations)
  - [Hooks and permission modes](#hooks-and-permission-modes)
  - [Hook not firing](#hook-not-firing)
  - [Hook error in output](#hook-error-in-output)
  - [/hooks shows no hooks configured](#%2Fhooks-shows-no-hooks-configured)
  - [Stop hook hits the block cap](#stop-hook-hits-the-block-cap)
  - [Hook JSON has no effect](#hook-json-has-no-effect)
  - [Debug techniques](#debug-techniques)
- [Learn more](#learn-more)

Automation

# Automate actions with hooks

Copy pageCopy page

Run shell commands automatically when Claude Code edits files, finishes tasks, or needs input. Format code, send notifications, validate commands, and enforce project rules.

Copy pageCopy page

Hooks are user-defined shell commands. Claude Code runs them at specific points in its lifecycle, which gives you deterministic control: certain actions always happen rather than relying on the LLM to choose to run them. Use hooks to enforce project rules, automate repetitive tasks, and integrate Claude Code with your existing tools. For decisions that require judgment rather than deterministic rules, you can also use [prompt-based hooks](#prompt-based-hooks) or [agent-based hooks](#agent-based-hooks) that use a Claude model to evaluate conditions. For other ways to extend Claude Code, see [skills](../08-Plugins-Skills/skills.md) for giving Claude additional instructions and executable commands, [subagents](../09-Agents-Patterns/sub-agents.md) for running tasks in isolated contexts, and [plugins](../08-Plugins-Skills/plugins.md) for packaging extensions to share across projects.

This guide covers common use cases and how to get started. For full event schemas, JSON input/output formats, and advanced features like async hooks and MCP tool hooks, see the [Hooks reference](hooks.md).


[​](#set-up-your-first-hook)

Set up your first hook

To create a hook, add a `hooks` block to a [settings file](#configure-hook-location). This walkthrough creates a desktop notification hook, so you get alerted whenever Claude is waiting for your input instead of watching the terminal.

1

Add the hook to your settings

Open `~/.claude/settings.json` and add a `Notification` hook. If the file doesn’t exist, create it. The example below uses `osascript` for macOS; see [Get notified when Claude needs input](#get-notified-when-claude-needs-input) for Linux and Windows commands.

```python
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

If your settings file already has a `hooks` key, add `Notification` as a sibling of the existing event keys rather than replacing the whole object. Each event name is a key inside the single `hooks` object:

```python
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [{ "type": "command", "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'" }]
      }
    ]
  }
}
```

You can also ask Claude to write the hook for you by describing what you want in the CLI.

2

Verify the configuration

Type `/hooks` to open the hooks browser. You’ll see a list of all available hook events, with a count next to each event that has hooks configured. Select `Notification` to confirm your new hook appears in the list. Selecting the hook shows its details: the event, matcher, type, source file, and command.

3

Test the hook

Press `Esc` to return to the CLI. Press `Shift+Tab` until the status bar shows `⏸ manual mode on`, ask Claude to do something that requires permission, then switch away from the terminal. You should receive a desktop notification.

The `/hooks` menu is read-only. To add, modify, or remove hooks, edit your settings JSON directly or ask Claude to make the change.


[​](#what-you-can-automate)

What you can automate

Hooks let you run code at key points in Claude Code’s lifecycle: format files after edits, block commands before they execute, send notifications when Claude needs input, inject context at session start, and more. For the full list of hook events, see the [Hooks reference](hooks.md#hook-lifecycle). Each example includes a ready-to-use configuration block that you add to a [settings file](#configure-hook-location). For a production example of hooks that run a separate model review and feed findings back into the session, see [how the `security-guidance` plugin integrates with Claude Code](../02-Claude-Code-CLI/security-guidance.md#how-the-plugin-integrates-with-claude-code).


[​](#get-notified-when-claude-needs-input)

Get notified when Claude needs input

Get a desktop notification whenever Claude finishes working and needs your input, so you can switch to other tasks without checking the terminal. This hook uses the `Notification` event, which Claude Code fires when Claude is waiting for input or permission. See [when each notification type fires](hooks.md#notification) for the exact timing. Each tab below uses the platform’s native notification command. Add this to `~/.claude/settings.json`:

- macOS

- Linux

- Windows (PowerShell)

```python
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

If no notification appears

`osascript` routes notifications through the built-in Script Editor app. If Script Editor doesn’t have notification permission, the command fails silently, and macOS won’t prompt you to grant it. Run this in Terminal once to make Script Editor appear in your notification settings:

```python
osascript -e 'display notification "test"'
```

Nothing will appear yet. Open **System Settings \> Notifications**, find **Script Editor** in the list, and turn on **Allow Notifications**. Run the command again to confirm the test notification appears.

```python
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Claude Code needs your attention'"
          }
        ]
      }
    ]
  }
}
```

If no notification appears

`notify-send` needs a desktop notification daemon, which headless servers, SSH sessions, and most containers don’t have. Test the command directly first:

```python
notify-send 'Claude Code' 'test'
```

If the command isn’t found, install the `libnotify-bin` package on Debian and Ubuntu, or your distribution’s equivalent.

```python
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude Code needs your attention', 'Claude Code')\""
          }
        ]
      }
    ]
  }
}
```

If no dialog appears

This command opens a dialog box rather than a notification in the corner of your screen, so the dialog can open behind your terminal window. Test the command directly in PowerShell first. If you run Claude Code inside WSL, `powershell.exe` must be available on your `PATH` through Windows interop.

The empty `matcher` fires on all notification types. To fire only on specific events, set it to one of these values:

| Matcher                      | Fires when                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `permission_prompt`          | Claude needs you to approve a tool use or a sandboxed command’s [network request](../02-Claude-Code-CLI/sandboxing.md#network-isolation), and the prompt has waited about six seconds                                                                                                                                                                                                                                                                                                      |
| `idle_prompt`                | Claude finished responding about 60 seconds ago and you haven’t typed since                                                                                                                                                                                                                                                                                                                                                                                                |
| `auth_success`               | Authentication completes                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `elicitation_dialog`         | An MCP server opens an elicitation form and you haven’t typed for about six seconds                                                                                                                                                                                                                                                                                                                                                                                        |
| `elicitation_url_dialog`     | An MCP server asks you to open a browser URL and you haven’t typed for about six seconds                                                                                                                                                                                                                                                                                                                                                                                   |
| `elicitation_complete`       | An MCP server reports that a [URL-mode elicitation](hooks.md#elicitation-input) is complete                                                                                                                                                                                                                                                                                                                                                                          |
| `elicitation_response`       | An MCP elicitation response is sent back to the server                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `agent_needs_input`          | A background session starts waiting on your input while [agent view](../09-Agents-Patterns/agent-view.md) is open. Also fires when a terminal session shows you an [agent team teammate’s terminal setup question](../09-Agents-Patterns/agent-teams.md#choose-a-display-mode) or auto mode’s notice about [classifier request charges](../17-Billing-Plans/auto-mode-classifier-billing.md) and you haven’t typed for about six seconds                                                                                 |
| `agent_completed`            | A background session finishes or fails. Fires only while [agent view](../09-Agents-Patterns/agent-view.md) is open                                                                                                                                                                                                                                                                                                                                                                         |
| `quota_auto_resume_fired`    | Claude Code continues your task after a claude.ai usage limit paused it: at the reset, or sooner when something you do in Claude Code during the wait, such as adding usage credits, upgrading your plan, or switching models, makes usage available again, with the [model-setting exception](../02-Claude-Code-CLI/interactive-mode.md#wait-for-a-usage-limit-to-reset)                                                                                                                  |
| `quota_auto_resume_stale`    | A claude.ai usage limit reset while your computer slept for more than about 30 minutes. Claude Code waits for you to press `Enter` instead of continuing. After a shorter sleep it continues and fires `quota_auto_resume_fired` instead                                                                                                                                                                                                                                   |
| `quota_auto_resume_disabled` | Claude Code ends its wait for a claude.ai usage limit without continuing your task: [`autoContinueAtUsageLimit`](../02-Claude-Code-CLI/settings-reference.md#autocontinueatusagelimit) turned off or the reset moved more than 24 hours away during a wait Claude Code started on its own, the continued task kept hitting the limit, or the continuation was blocked before it reached the model. Doesn’t fire when you press `Esc` or `Ctrl+C`, or pick **Don’t continue automatically** |

Claude Code times `permission_prompt` differently in a terminal and in Claude Desktop, the VS Code extension, and other hosts that answer permission requests through the Agent SDK. See [when each notification type fires](hooks.md#notification) for both timings. The `agent_needs_input` and `agent_completed` matchers require Claude Code v2.1.198 or later. The `quota_auto_resume_fired`, `quota_auto_resume_stale`, and `quota_auto_resume_disabled` matchers require Claude Code v2.1.234 or later. In terminal sessions, `permission_prompt` for a sandboxed command’s network request requires Claude Code v2.1.246 or later. `agent_needs_input` for a teammate’s terminal setup question requires Claude Code v2.1.248 or later. Type `/hooks` and select `Notification` to confirm the hook is registered. For the full event schema, see the [Notification reference](hooks.md#notification).


[​](#auto-format-code-after-edits)

Auto-format code after edits

Automatically run [Prettier](https://prettier.io/) on every file Claude edits, so formatting stays consistent without manual intervention. This hook uses the `PostToolUse` event with an `Edit|Write` matcher, so it runs only after file-editing tools. The command extracts the edited file path with [`jq`](https://jqlang.org/) and passes it to Prettier. Add this to `.claude/settings.json` in your project root:

```python
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

To test the hook, ask Claude to add a line with single-quoted strings to a JavaScript file, then open the file: with Prettier’s default settings, the hook rewrites them to double quotes. When the hook succeeds, Claude Code shows nothing in the conversation. To confirm the hook ran, check that the edited file is reformatted, or see [Debug techniques](#debug-techniques). To reformat a specific file however it changes, including when a `Bash` command rewrites it, use a [FileChanged](hooks.md#filechanged) hook instead.

The Bash examples on this page use `jq` for JSON parsing. Install it with `brew install jq` on macOS, `apt-get install jq` on Debian and Ubuntu, or see [`jq` downloads](https://jqlang.org/download/).


[​](#block-edits-to-protected-files)

Block edits to protected files

Prevent Claude from modifying sensitive files like `.env`, `package-lock.json`, or anything in `.git/`. Claude receives feedback explaining why the edit was blocked, so it can adjust its approach. This example uses a separate script file that the hook calls. The script checks the target file path against a list of protected patterns and exits with code 2 to block the edit.

1

Create the hook script

Save this to `.claude/hooks/protect-files.sh`:

```python
#!/bin/bash
# protect-files.sh

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Normalize Windows backslash separators so the patterns below match
FILE_PATH="${FILE_PATH//\\//}"

PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
    exit 2
  fi
done

exit 0
```

2

Make the script executable on macOS and Linux

Hook scripts must be executable for Claude Code to run them:

```python
chmod +x .claude/hooks/protect-files.sh
```

3

Register the hook

Add a `PreToolUse` hook to `.claude/settings.json` that runs the script before any `Edit` or `Write` tool call:

```python
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"
          }
        ]
      }
    ]
  }
}
```

4

Test the hook

Ask Claude to add a comment to your `.env` file. Claude Code blocks the edit before it runs and passes the script’s `Blocked:` message to Claude as feedback.


[​](#re-inject-context-after-compaction)

Re-inject context after compaction

When Claude’s context window fills up, compaction summarizes the conversation to free space. This can lose important details. Use a `SessionStart` hook with a `compact` matcher to re-inject critical context after every compaction. Claude Code adds plain text your command writes to stdout to Claude’s context. This example reminds Claude of project conventions and recent work. Add this to `.claude/settings.json` in your project root:

```python
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Reminder: use Bun, not npm. Run bun test before committing. Current sprint: auth refactor.'"
          }
        ]
      }
    ]
  }
}
```

You can replace the `echo` with any command that produces dynamic output, like `git log --oneline -5` to show recent commits. For injecting context on every session start, consider using [CLAUDE.md](../02-Claude-Code-CLI/memory.md) instead. For environment variables, see [`CLAUDE_ENV_FILE`](hooks.md#persist-environment-variables) in the reference.


[​](#audit-configuration-changes)

Audit configuration changes

Track when settings or skills files change during a session. The `ConfigChange` event fires when an external process or editor modifies a configuration file, so you can log changes for compliance or block unauthorized modifications. This example appends each change to an audit log. Add this to `~/.claude/settings.json`:

```python
{
  "hooks": {
    "ConfigChange": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "jq -c '{timestamp: now | todate, source: .source, file: .file_path}' >> ~/claude-config-audit.log"
          }
        ]
      }
    ]
  }
}
```

The matcher filters by configuration type: `user_settings`, `project_settings`, `local_settings`, `policy_settings`, or `skills`. To block a change from taking effect, exit with code 2 or return `{"decision": "block"}`. See the [ConfigChange reference](hooks.md#configchange) for the full input schema. To confirm the hook records changes, edit a settings file in another editor while a session is running, then open `~/claude-config-audit.log`: the hook appends one JSON line per change with the timestamp, source, and file path.


[​](#reload-environment-when-directory-or-files-change)

Reload environment when directory or files change

Some projects set different environment variables depending on which directory you are in. Tools like [direnv](https://direnv.net/) do this automatically in your shell, but Claude’s Bash tool doesn’t pick up those changes on its own. Pairing a `SessionStart` hook with a `CwdChanged` hook fixes this. `SessionStart` loads the variables for the directory you launch in, and `CwdChanged` reloads them each time Claude changes directory. Both write to `CLAUDE_ENV_FILE`, which Claude Code runs as a script preamble before each Bash command. Add this to `~/.claude/settings.json`:

```python
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "direnv export bash > \"$CLAUDE_ENV_FILE\""
          }
        ]
      }
    ],
    "CwdChanged": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "direnv export bash > \"$CLAUDE_ENV_FILE\""
          }
        ]
      }
    ]
  }
}
```

Run `direnv allow` once in each directory that has an `.envrc` so direnv is permitted to load it. If you use devbox or nix instead of direnv, the same pattern works with `devbox shellenv` or `devbox global shellenv` in place of `direnv export bash`. To react to specific files instead of every directory change, use `FileChanged` with a `matcher` listing the filenames to watch, separated by `|`. When building the watch list, Claude Code splits this value into literal filenames rather than evaluating it as a regex. See [FileChanged](hooks.md#filechanged) for how the same value also filters which hook groups run when a file changes. This example watches `.envrc` and `.env` in the working directory:

```python
{
  "hooks": {
    "FileChanged": [
      {
        "matcher": ".envrc|.env",
        "hooks": [
          {
            "type": "command",
            "command": "direnv export bash > \"$CLAUDE_ENV_FILE\""
          }
        ]
      }
    ]
  }
}
```

See the [CwdChanged](hooks.md#cwdchanged) and [FileChanged](hooks.md#filechanged) reference entries for input schemas, `watchPaths` output, and `CLAUDE_ENV_FILE` details.


[​](#auto-approve-specific-permission-prompts)

Auto-approve specific permission prompts

Skip the approval dialog for tool calls you always allow. This example auto-approves `ExitPlanMode`, the tool Claude calls when it finishes presenting a plan and asks to proceed, so you aren’t prompted every time a plan is ready. Unlike the exit-code examples above, auto-approval requires your hook to write a JSON decision to stdout. Claude Code runs `PermissionRequest` hooks when it’s about to ask you for permission, and if your hook returns `"behavior": "allow"`, Claude Code answers the request on your behalf. The matcher scopes the hook to `ExitPlanMode` only, so no other prompts are affected. Add this to `~/.claude/settings.json`:

```python
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "ExitPlanMode",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"hookSpecificOutput\": {\"hookEventName\": \"PermissionRequest\", \"decision\": {\"behavior\": \"allow\"}}}'"
          }
        ]
      }
    ]
  }
}
```

When the hook approves, Claude Code exits plan mode and restores whatever permission mode was active before you entered plan mode. The transcript shows “Allowed by PermissionRequest hook” where the dialog would have appeared. The hook path always keeps the current conversation: it can’t clear context and start a fresh implementation session the way the dialog can. To set a specific permission mode instead, your hook’s output can include an `updatedPermissions` array with a `setMode` entry. The `mode` value is any permission mode like `default`, `acceptEdits`, or `bypassPermissions`, and `destination: "session"` applies it for the current session only.

`bypassPermissions` only applies if you started the session with bypass mode already available: `--dangerously-skip-permissions`, `--permission-mode bypassPermissions`, `--allow-dangerously-skip-permissions`, or `permissions.defaultMode: "bypassPermissions"` in [user, `--settings`, or managed settings](../02-Claude-Code-CLI/settings-reference.md#permissions-defaultmode). It doesn’t apply if bypass mode is disabled by [`permissions.disableBypassPermissionsMode`](../02-Claude-Code-CLI/permissions.md#managed-settings), or if you started the session in [restricted mode](../02-Claude-Code-CLI/cli-reference.md#cli-flags).Claude Code never saves it as `defaultMode`.

To switch the session to `acceptEdits`, your hook writes this JSON to stdout:

```python
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow",
      "updatedPermissions": [
        { "type": "setMode", "mode": "acceptEdits", "destination": "session" }
      ]
    }
  }
}
```

Keep the matcher as narrow as possible. Matching on `.*` or leaving the matcher empty would auto-approve every tool permission prompt, including file writes and shell commands. See the [PermissionRequest reference](hooks.md#permissionrequest-decision-control) for the full set of decision fields.


[​](#how-hooks-work)

How hooks work

Claude Code fires hook events at specific points in its lifecycle. When an event fires, Claude Code runs all matching hooks in parallel; see [Hook handler fields](hooks.md#hook-handler-fields) for how duplicate handlers are treated. The table below shows each event and when it triggers:

| Event                 | When it fires                                                                                                                                                                                                                                         |
|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SessionStart`        | When a session begins or resumes                                                                                                                                                                                                                      |
| `Setup`               | When you start Claude Code with `--init-only`, or with `--init` or `--maintenance` in `-p` mode. For one-time preparation in CI or scripts                                                                                                            |
| `UserPromptSubmit`    | When you submit a prompt, before Claude processes it                                                                                                                                                                                                  |
| `UserPromptExpansion` | When a user-typed command expands into a prompt, before it reaches Claude. Can block the expansion                                                                                                                                                    |
| `PreToolUse`          | Before a tool call executes. Can block it                                                                                                                                                                                                             |
| `PermissionRequest`   | When a tool call needs a permission decision                                                                                                                                                                                                          |
| `PermissionDenied`    | When auto mode denies a tool call, including denials without a classifier verdict. Use JSON `hookSpecificOutput.retry: true` to tell the model it may retry the denied tool call. Claude Code ignores `retry` when the classifier produced no verdict |
| `PostToolUse`         | After a tool call succeeds                                                                                                                                                                                                                            |
| `PostToolUseFailure`  | After a tool call fails                                                                                                                                                                                                                               |
| `PostToolBatch`       | After a full batch of parallel tool calls resolves, before the next model call                                                                                                                                                                        |
| `Notification`        | When Claude Code sends a notification                                                                                                                                                                                                                 |
| `MessageDisplay`      | While assistant message text is displayed                                                                                                                                                                                                             |
| `SubagentStart`       | When a subagent is spawned                                                                                                                                                                                                                            |
| `SubagentStop`        | When a subagent finishes                                                                                                                                                                                                                              |
| `TaskCreated`         | When a task is being created via `TaskCreate`                                                                                                                                                                                                         |
| `TaskCompleted`       | When a task is being marked as completed                                                                                                                                                                                                              |
| `Stop`                | When Claude finishes responding                                                                                                                                                                                                                       |
| `StopFailure`         | When the turn ends due to an API error                                                                                                                                                                                                                |
| `TeammateIdle`        | When an [agent team](../09-Agents-Patterns/agent-teams.md) teammate is about to go idle                                                                                                                                                                               |
| `InstructionsLoaded`  | When a CLAUDE.md or `.claude/rules/*.md` file is loaded into context. Fires at session start and when files are lazily loaded during a session                                                                                                        |
| `ConfigChange`        | When a configuration file changes during a session                                                                                                                                                                                                    |
| `CwdChanged`          | When the working directory changes, for example when Claude executes a `cd` command. Useful for reactive environment management with tools like direnv                                                                                                |
| `DirectoryAdded`      | When a working directory is added mid-session via `/add-dir` or the SDK `register_repo_root` control request                                                                                                                                          |
| `FileChanged`         | When a watched file changes on disk. The `matcher` field specifies which filenames to watch                                                                                                                                                           |
| `WorktreeCreate`      | When a worktree is being created via `--worktree`, `isolation: "worktree"`, or for a background session. Replaces default git behavior                                                                                                                |
| `WorktreeRemove`      | When a worktree is being removed at session exit, when a subagent finishes, or when you delete a background session                                                                                                                                   |
| `PreCompact`          | Before context compaction                                                                                                                                                                                                                             |
| `PostCompact`         | After context compaction completes                                                                                                                                                                                                                    |
| `PreModelSwitch`      | Before Claude Code applies a model switch that you or a client requested. Can block the switch                                                                                                                                                        |
| `PostModelSwitch`     | After the session’s model changes, including changes Claude Code makes on its own, such as restoring the model when you resume a session                                                                                                              |
| `Elicitation`         | When an MCP server requests user input during a tool call                                                                                                                                                                                             |
| `ElicitationResult`   | After a user responds to an MCP elicitation, before the response is sent back to the server                                                                                                                                                           |
| `SessionEnd`          | When a session terminates                                                                                                                                                                                                                             |

Each hook has a `type` that determines how it runs. Most hooks use `"type": "command"`, which runs a shell command. Four other types are available:

- `"type": "http"`: POST event data to a URL. See [HTTP hooks](#http-hooks).
- `"type": "mcp_tool"`: call a tool on a configured MCP server. See [MCP tool hooks](hooks.md#mcp-tool-hook-fields).
- `"type": "prompt"`: single-turn LLM evaluation. See [Prompt-based hooks](#prompt-based-hooks).
- `"type": "agent"`: multi-turn verification with tool access. Agent hooks are experimental and may change. See [Agent-based hooks](#agent-based-hooks).


[​](#combine-results-from-multiple-hooks)

Combine results from multiple hooks

When multiple hooks match the same event, every hook’s command runs to completion before Claude Code merges the results. One hook returning `deny` doesn’t stop sibling hooks from executing. Don’t rely on one hook’s `deny` to suppress side effects in another hook. After all matching hooks finish, Claude Code combines their outputs. For `PreToolUse` permission decisions, the most restrictive answer applies, in the order `deny`, `defer`, `ask`, `allow`. Text from `additionalContext` is kept from every hook and passed to Claude together. The example below registers two `PreToolUse` hooks on `Bash`. The first appends every command to a log file and exits 0. The second runs a script that exits 2 to deny when the command contains `rm -rf`:

```python
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r .tool_input.command >> ~/.claude/bash.log"
          },
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-rm-rf.sh"
          }
        ]
      }
    ]
  }
}
```

When Claude tries to run `rm -rf /tmp/build`, both hooks execute in parallel. The logging hook writes the command to `~/.claude/bash.log` and exits 0, which reports no decision. The guardrail hook exits 2, which denies the tool call. The deny takes precedence, so Claude Code blocks the command and shows Claude the guardrail’s stderr. The log entry is still written because the logging hook already ran.


[​](#read-input-and-return-output)

Read input and return output

Hooks communicate with Claude Code through stdin, stdout, stderr, and exit codes. When an event fires, Claude Code passes event-specific data as JSON to your script’s stdin. Your script reads that data, does its work, and tells Claude Code what to do next via the exit code.


[​](#hook-input)

Hook input

Every event includes common fields like `session_id`, a unique ID for the session, and `cwd`, the working directory when the event fired, but each event type adds different data. When Claude runs a Bash command, a `PreToolUse` hook receives these fields on stdin:

- `hook_event_name`: the event that triggered the hook
- `tool_name`: the tool Claude is about to use
- `tool_input`: the arguments Claude passed to the tool. For Bash, its `command` field holds the shell command.

For example, the hook input for an `npm test` command looks like this:

```python
{
  "session_id": "abc123",
  "cwd": "/Users/sarah/myproject",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test"
  }
}
```

Your script can parse that JSON and act on any of those fields. `UserPromptSubmit` hooks get the `prompt` text instead, `SessionStart` hooks get a `source` of `startup`, `resume`, `clear`, `compact`, or `fork`, and so on. See [Common input fields](hooks.md#common-input-fields) in the reference for shared fields, and each event’s section for event-specific schemas.


[​](#hook-output)

Hook output

Your script tells Claude Code what to do next by writing to stdout or stderr and exiting with a specific code. The following `PreToolUse` hook blocks a command:

```python
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q "drop table"; then
  echo "Blocked: dropping tables is not allowed" >&2  # stderr becomes Claude's feedback
  exit 2                                               # exit 2 = block the action
fi

exit 0  # exit 0 = no decision; the normal permission flow applies
```

The exit code determines what happens next:

- **Exit 0**: your hook reports no objection through its exit code.
  - For a `PreToolUse` hook this doesn’t approve the tool call: the normal [permission flow](../02-Claude-Code-CLI/permissions.md) still applies.
  - For `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, and `PostModelSwitch` hooks, Claude Code adds stdout it [treats as plain text](hooks.md#exit-code-0) to Claude’s context.
- **Exit 2**: Claude Code blocks the action. Write a reason to stderr. Where it lands depends on the event: some events feed it to Claude as feedback so it can adjust, others show it to the user, and a few, such as `ConfigChange` and `Elicitation`, surface no message. Some events can’t be blocked: for `SessionStart` and others, exit 2 shows stderr to the user and execution continues. See [exit code 2 behavior per event](hooks.md#exit-code-2-behavior-per-event) for the full list.
- **Any other exit code**: for most events, the outcome depends on what your hook printed to stdout:
  - A parsed object that passes schema validation: Claude Code ignores the exit code, the JSON alone decides the outcome, and the hook isn’t reported as an error. The per-event exceptions, like `WorktreeCreate` failing on any nonzero exit, are listed in the reference’s [Exit code output](hooks.md#exit-code-output) section.
  - A parsed object that fails schema validation, or stdout that Claude Code [tries to parse as JSON](hooks.md#exit-code-0) but that isn’t valid JSON: a non-blocking error; the notice carries the validation or parse message.
  - Stdout that Claude Code [treats as plain text](hooks.md#exit-code-0), or empty stdout: the action proceeds as a non-blocking error. The transcript shows a `<hook name> hook error` notice, then the first line of stderr prefixed with `Failed with non-blocking status code:`. To capture the full stderr, enable [debug logging](hooks.md#debug-hooks) with `claude --debug` or by running `/debug` mid-session.


[​](#structured-json-output)

Structured JSON output

Exit codes only let you block or stay silent. For more control, exit 0 and print a JSON object to stdout instead.

Use exit 2 to block with a stderr message, or exit 0 with JSON for structured control. Choose one approach per hook. For what happens when you mix them, see [Exit code output](hooks.md#exit-code-output).

For example, a `PreToolUse` hook can deny a tool call and tell Claude why, or escalate it to the user for approval:

```python
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Use rg instead of grep for better performance"
  }
}
```

With `"deny"`, Claude Code cancels the tool call and feeds `permissionDecisionReason` back to Claude. On `PreToolUse`, Claude Code handles each `permissionDecision` value as follows:

- `"allow"`: skip the interactive permission prompt. Deny and ask rules, including enterprise managed deny lists, still apply, as do prompts for MCP tools marked [`requiresUserInteraction`](../06-MCP-Tools/General/mcp.md#require-approval-for-a-specific-tool) and for connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools) in sessions where that setting reaches Claude Code
- `"deny"`: cancel the tool call and send the reason to Claude
- `"ask"`: show the permission prompt to the user as normal

A fourth value, `"defer"`, is available in [non-interactive mode](../02-Claude-Code-CLI/headless.md) with the `-p` flag. It exits the process with the tool call preserved so an Agent SDK wrapper can collect input and resume. See [Defer a tool call for later](hooks.md#defer-a-tool-call-for-later) in the reference. A `PreModelSwitch` hook returns the same `permissionDecision` field: `"allow"` lets a model switch proceed, and `"deny"` cancels it. `"ask"` has you confirm the switch when you run `/model` in an interactive session; everywhere else, Claude Code treats `"ask"` as a refusal. See [PreModelSwitch decision control](hooks.md#premodelswitch-decision-control). Other events use different decision patterns. For example, `PostToolUse` and `Stop` hooks use a top-level `decision: "block"` field, while `PermissionRequest` uses `hookSpecificOutput.decision.behavior`. See the [summary table](hooks.md#decision-control) in the reference for a full breakdown by event. For `UserPromptSubmit` hooks, use `hookSpecificOutput.additionalContext` instead to inject text into Claude’s context. Nest `additionalContext` inside `hookSpecificOutput`; if you place it at the top level of the JSON, Claude Code silently ignores it. For example, this output adds the current branch state to every prompt:

```python
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Current branch: release-42. Deploy freeze until Friday."
  }
}
```

See [UserPromptSubmit decision control](hooks.md#userpromptsubmit-decision-control) for the full output shape, including blocking prompts and setting the session title. Hooks with `type: "prompt"` handle output differently: see [Prompt-based hooks](#prompt-based-hooks).


[​](#filter-hooks-with-matchers)

Filter hooks with matchers

Without a matcher, a hook fires on every occurrence of its event. Matchers let you narrow that down. For example, if you want to run a formatter only after file edits, not after every tool call, add a matcher to your `PostToolUse` hook:

```python
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "prettier --write ..." }
        ]
      }
    ]
  }
}
```

The `"Edit|Write"` matcher fires only when Claude uses the `Edit` or `Write` tool, not when it uses `Bash`, `Read`, or any other tool. A comma separates alternatives the same way, so `"Edit, Write"` is equivalent. See [Matcher patterns](hooks.md#matcher-patterns) for how plain names and regular expressions are evaluated.

Claude can also create or modify files by running shell commands. If your hook must see every file change, such as for compliance scanning or audit logging, add a [`Stop`](hooks.md#stop) hook that scans the working tree once per turn. For per-call coverage instead, also match `Bash|PowerShell` and have your script list modified and untracked files with `git status --porcelain`. The [PowerShell hook input section](hooks.md#powershell) explains why matching `Bash` alone is not enough. To run a hook when a specific file changes on disk, whatever wrote it, use a [FileChanged](hooks.md#filechanged) hook.

Each event type matches on a specific field:

| Event                                                                                                                                                           | What the matcher filters                                                                                                | Example matcher values                                                                                                                                                                                                                                                         |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`                                                                      | tool name                                                                                                               | `Bash`, `Edit|Write`, `mcp__.*`                                                                                                                                                                                                                                                |
| `SessionStart`                                                                                                                                                  | how the session started                                                                                                 | `startup`, `resume`, `clear`, `compact`, `fork`                                                                                                                                                                                                                                |
| `Setup`                                                                                                                                                         | which CLI flag triggered setup                                                                                          | `init`, `maintenance`                                                                                                                                                                                                                                                          |
| `SessionEnd`                                                                                                                                                    | why the session ended                                                                                                   | `clear`, `resume`, `logout`, `prompt_input_exit`, `other`                                                                                                                                                                                                                      |
| `Notification`                                                                                                                                                  | notification type                                                                                                       | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_url_dialog`, `elicitation_complete`, `elicitation_response`, `agent_needs_input`, `agent_completed`, `quota_auto_resume_fired`, `quota_auto_resume_stale`, `quota_auto_resume_disabled` |
| `SubagentStart`                                                                                                                                                 | agent type                                                                                                              | `general-purpose`, `Explore`, `Plan`, or custom agent names                                                                                                                                                                                                                    |
| `PreCompact`, `PostCompact`                                                                                                                                     | what triggered compaction                                                                                               | `manual`, `auto`                                                                                                                                                                                                                                                               |
| `PreModelSwitch`, `PostModelSwitch`                                                                                                                             | canonical name of the model the session switches to, as described under [PreModelSwitch](hooks.md#premodelswitch) | `claude-opus-5`, `claude-opus-4-6|claude-opus-5`, `.*opus.*`                                                                                                                                                                                                                   |
| `SubagentStop`                                                                                                                                                  | agent type                                                                                                              | same values as `SubagentStart`                                                                                                                                                                                                                                                 |
| `ConfigChange`                                                                                                                                                  | configuration source                                                                                                    | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`                                                                                                                                                                                             |
| `DirectoryAdded`                                                                                                                                                | how the directory was added                                                                                             | `slash_command`, `register_repo_root`                                                                                                                                                                                                                                          |
| `StopFailure`                                                                                                                                                   | error type                                                                                                              | `rate_limit`, `overloaded`, `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown`                                               |
| `InstructionsLoaded`                                                                                                                                            | load reason                                                                                                             | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact`                                                                                                                                                                                                   |
| `Elicitation`                                                                                                                                                   | MCP server name                                                                                                         | your configured MCP server names                                                                                                                                                                                                                                               |
| `ElicitationResult`                                                                                                                                             | MCP server name                                                                                                         | same values as `Elicitation`                                                                                                                                                                                                                                                   |
| `FileChanged`                                                                                                                                                   | literal filenames to watch (see [FileChanged](hooks.md#filechanged))                                              | `.envrc|.env`                                                                                                                                                                                                                                                                  |
| `UserPromptExpansion`                                                                                                                                           | command name                                                                                                            | your skill or command names                                                                                                                                                                                                                                                    |
| `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `CwdChanged`, `MessageDisplay` | no matcher support                                                                                                      | always fires on every occurrence                                                                                                                                                                                                                                               |

The tabs below show a few more matchers on different event types.

- Log every Bash command

- Match MCP tools

- Clean up on session end

Match only `Bash` tool calls and log each command to a file. The `PostToolUse` event fires after the command completes, so `tool_input.command` contains what ran. The hook receives the event data as JSON on stdin, and `jq -r '.tool_input.command'` extracts only the command string, which `>>` appends to the log file:

```python
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/command-log.txt"
          }
        ]
      }
    ]
  }
}
```

MCP tools use a different naming convention than built-in tools: `mcp__<server>__<tool>`, where `<server>` is the MCP server name and `<tool>` is the tool it provides. For example, `mcp__github__search_repositories` or `mcp__filesystem__read_file`. Tools from a [plugin-bundled server](../06-MCP-Tools/General/mcp.md#plugin-provided-mcp-servers) use a scoped server segment instead, such as `mcp__plugin_my-plugin_db__query`. Use a regex matcher to target all tools from a specific server, or match across servers with a pattern like `mcp__.*__write.*`. See [Match MCP tools](hooks.md#match-mcp-tools) in the reference for the full list of examples.The command below extracts the tool name from the hook’s JSON input with `jq` and writes it to stderr. Writing to stderr keeps stdout clean for JSON output and sends the message to the [debug log](hooks.md#debug-hooks):

```python
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__github__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"GitHub tool called: $(jq -r '.tool_name')\" >&2"
          }
        ]
      }
    ]
  }
}
```

The `SessionEnd` event supports matchers on the reason the session ended. This hook only fires on the `clear` reason, set when you run `/clear`, not on normal exits:

```python
{
  "hooks": {
    "SessionEnd": [
      {
        "matcher": "clear",
        "hooks": [
          {
            "type": "command",
            "command": "rm -f /tmp/claude-scratch-*.txt"
          }
        ]
      }
    ]
  }
}
```


[​](#filter-by-tool-name-and-arguments-with-the-if-field)

Filter by tool name and arguments with the `if` field

The `if` field uses [permission rule syntax](../02-Claude-Code-CLI/permissions.md) to filter hooks by tool name and arguments together, so the hook process only spawns when the tool call matches. This goes beyond `matcher`, which filters at the group level by tool name only. For example, this configuration runs a hook only when Claude uses `git` commands rather than all Bash commands:

```python
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(git *)",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-git-policy.sh"
          }
        ]
      }
    ]
  }
}
```

Whether your hook command runs depends on the shape of your `if` pattern and the Bash command Claude is invoking:

| `if` pattern       | Bash command           | Hook runs? | Why                                                                                                 |
|:-------------------|:-----------------------|:-----------|:----------------------------------------------------------------------------------------------------|
| `Bash(git *)`      | `git push`             | yes        | command name matches                                                                                |
| `Bash(git *)`      | `npm test && git push` | yes        | each subcommand is checked; `git push` matches                                                      |
| `Bash(git *)`      | `echo $(git log)`      | yes        | commands inside `$()` and backticks are checked; `git log` matches                                  |
| `Bash(git *)`      | `echo $(date)`         | no         | no subcommand matches `git *`                                                                       |
| `Bash(git push *)` | `echo $(date)`         | yes        | patterns that specify more than the command name run the hook anyway on `$()`, backticks, or `$VAR` |

When Claude Code can’t determine which commands the Bash input runs, it runs your hook regardless of the pattern. The [Bash matching table](hooks.md#bash-if-matching) covers the command shapes Claude Code can and can’t narrow by subcommand. Because the filter is best-effort, use the [permission system](../02-Claude-Code-CLI/permissions.md) rather than a hook to enforce a hard allow or deny. The `if` field accepts the same patterns as permission rules: `"Bash(git *)"`, `"Edit(*.ts)"`, and so on. To match multiple tool names, use separate handlers each with its own `if` value, or match at the `matcher` level where pipe alternation is supported. `if` only works on tool events: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, and `PermissionDenied`. Adding it to any other event prevents the hook from running.


[​](#configure-hook-location)

Configure hook location

Where you add a hook determines its scope:

| Location                                               | Scope                                                                                                                          | Shareable                                             |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------|
| `~/.claude/settings.json`                              | All your projects                                                                                                              | No, local to your machine                             |
| `.claude/settings.json`                                | Single project                                                                                                                 | Yes, can be committed to the repo                     |
| `.claude/settings.local.json`                          | Single project                                                                                                                 | No, gitignored when Claude Code saves a setting to it |
| Managed policy settings                                | Organization-wide                                                                                                              | Yes, admin-controlled                                 |
| [Plugin](../08-Plugins-Skills/plugins.md) `hooks/hooks.json` | When plugin is enabled                                                                                                         | Yes, bundled with the plugin                          |
| [Skill](../08-Plugins-Skills/skills.md) frontmatter                   | The rest of the session once the skill is invoked. See [Hooks in skills and agents](hooks.md#hooks-in-skills-and-agents) | Yes, defined in the skill file                        |
| [Subagent](../09-Agents-Patterns/sub-agents.md) frontmatter            | While that subagent is running                                                                                                 | Yes, defined in the subagent file                     |

Run [`/hooks`](hooks.md#the-%2Fhooks-menu) in Claude Code to browse all configured hooks grouped by event. To disable hooks, set `"disableAllHooks": true` in your settings file. Claude Code reads the value left after [settings precedence](hooks.md#disable-or-remove-hooks) applies, so a project’s settings file can override yours. Hooks configured in managed settings still run unless `disableAllHooks` is also set there. For the full reach of each level, see [`disableAllHooks`](../02-Claude-Code-CLI/settings-reference.md#disableallhooks). If you edit settings files directly while Claude Code is running, the file watcher normally picks up hook changes automatically.


[​](#prompt-based-hooks)

Prompt-based hooks

For decisions that require judgment rather than deterministic rules, use `type: "prompt"` hooks. Instead of running a shell command, Claude Code sends your prompt and the hook’s input data to a Claude model to make the decision. You can specify a different model with the `model` field if you need more capability. The model’s only job is to return its decision as JSON:

- `"ok": true`: the action proceeds
- `"ok": false`: what happens depends on the event:
  - `Stop` and `SubagentStop`: the `reason` is fed back to Claude so it keeps working, unless the response also sets `"impossible": true` to mark the condition as one that can never be satisfied, in which case Claude Code allows the stop and the turn ends
  - `PreToolUse`: the tool call is denied; by default the turn ends and the deny `reason` appears in the chat as a warning line. Set `continueOnBlock: true` on the hook to instead return the `reason` to Claude as the tool error, so it can adjust and continue. Before v2.1.210, the deny `reason` was returned to Claude as the tool error and the turn continued
  - `PostToolUse`: by default the turn ends and the `reason` appears in the chat as a warning line. Set `continueOnBlock: true` to feed the `reason` back to Claude and continue the turn instead
  - `PostToolBatch`, `UserPromptSubmit`, and `UserPromptExpansion`: the turn ends and the `reason` appears in the chat as a warning line

This example uses a `Stop` hook to ask the model whether all requested tasks are complete. If the model returns `"ok": false` because the condition isn’t met yet, Claude keeps working and uses the `reason` as its next instruction:

```python
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check if all tasks are complete. If not, respond with {\"ok\": false, \"reason\": \"what remains to be done\"}."
          }
        ]
      }
    ]
  }
}
```

For full configuration options, see [Prompt-based hooks](hooks.md#prompt-based-hooks) in the reference.


[​](#agent-based-hooks)

Agent-based hooks

Agent hooks are experimental. Behavior and configuration may change in future releases. For production workflows, prefer [command hooks](hooks.md#command-hook-fields).

When verification requires inspecting files or running commands, use `type: "agent"` hooks. Unlike prompt hooks, which make a single LLM call, agent hooks spawn a subagent that can read files, search code, and use other tools to verify conditions before returning a decision. Agent hooks use the `"ok"` / `"reason"` response format with a longer default timeout of 60 seconds and up to 50 tool-use turns. They don’t support the prompt-hook `impossible` field. On `ok: false`, Claude Code handles an agent hook the way it handles a prompt hook with `continueOnBlock: true` on the same event, so on `PreToolUse` and `PostToolUse` the turn continues; agent hooks have no `continueOnBlock` field. See [agent hook configuration](hooks.md#agent-hook-configuration) for the fields, including the `$ARGUMENTS` placeholder that Claude Code replaces with the hook’s JSON input. This example verifies that tests pass before allowing Claude to stop:

```python
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

Use prompt hooks when the hook input data alone is enough to make a decision. Use agent hooks when you need to verify something against the actual state of the codebase. For full configuration options, see [Agent-based hooks](hooks.md#agent-based-hooks) in the reference.


[​](#http-hooks)

HTTP hooks

Use `type: "http"` hooks to POST event data to an HTTP endpoint instead of running a shell command. The endpoint receives the same JSON that a command hook would receive on stdin, and returns results through the HTTP response body using the same JSON format. HTTP hooks are useful when you want a web server, cloud function, or external service to handle hook logic: for example, a shared audit service that logs tool use events across a team. This example posts every tool use to a local logging service:

```python
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "http",
            "url": "http://localhost:8080/hooks/tool-use",
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

The endpoint should return a JSON response body using the same [output format](hooks.md#json-output) as command hooks. To block a tool call, return a 2xx response with the appropriate `hookSpecificOutput` fields. HTTP status codes alone can’t block actions. Header values support environment variable interpolation using `$VAR_NAME` or `${VAR_NAME}` syntax. Only variables listed in the `allowedEnvVars` array are resolved; all other `$VAR` references remain empty. For full configuration options and response handling, see [HTTP hooks](hooks.md#http-hook-fields) in the reference.


[​](#limitations-and-troubleshooting)

Limitations and troubleshooting


[​](#limitations)

Limitations

Keep these constraints in mind when designing hooks:

- Command hooks communicate through stdout, stderr, and exit codes only. They can’t trigger `/` commands or tool calls. Text returned via `additionalContext` is injected as a [system reminder](../02-Claude-Code-CLI/glossary.md#system-reminder) that Claude reads as plain text. HTTP hooks communicate through the response body instead.
- Hook timeouts vary by type. Override per hook with the `timeout` field in seconds.
  - `command`, `http`, `mcp_tool`: 10 minutes. Claude Code lowers this default to 30 seconds for `UserPromptSubmit`, `PreModelSwitch`, and `PostModelSwitch` hooks, and to 10 seconds for `MessageDisplay`.
  - `prompt`: 30 seconds.
  - `agent`: 60 seconds.
  - [`SessionEnd`](hooks.md#sessionend) hooks of any type share a 1.5-second budget. If your settings set a longer per-hook `timeout`, Claude Code raises the budget to match, up to 60 seconds.
- `PostToolUse` hooks can’t undo actions since the tool has already executed.
- `PermissionRequest` hooks fire when Claude Code is about to ask you for permission.
  - In [non-interactive mode](../02-Claude-Code-CLI/headless.md) with the `-p` flag, that prompt only exists when the Agent SDK’s [`canUseTool` callback](../05-Agent-SDK/agent-sdk-permissions.md) supplies it. In plain `-p` runs or with `--permission-prompt-tool`, use `PreToolUse` hooks for automated permission decisions instead.
  - Background subagents can’t show a prompt in non-interactive mode. Claude Code still runs the hooks for their tool calls, and if no hook returns a decision, it denies the call. In an interactive session, background subagent prompts surface in your main session and the hooks fire as usual.
- `Stop` hooks fire whenever Claude finishes responding, not only at task completion. They don’t fire on user interrupts. API errors fire [StopFailure](hooks.md#stopfailure) instead.
- When multiple `PreToolUse` hooks return [`updatedInput`](hooks.md#pretooluse) to rewrite a tool’s arguments, the last one to finish takes effect. Since hooks run in parallel, the order is non-deterministic. Avoid having more than one hook modify the same tool’s input.


[​](#hooks-and-permission-modes)

Hooks and permission modes

`PreToolUse` hooks fire before any permission-mode check, in every [permission mode](../02-Claude-Code-CLI/permission-modes.md), including `dontAsk`. A hook that returns `permissionDecision: "deny"` blocks the tool even in `bypassPermissions` mode or with `--dangerously-skip-permissions`. This lets you enforce policy that users can’t bypass by changing their permission mode. The reverse is not true: a hook returning `"allow"` doesn’t bypass deny rules from settings, and it can’t suppress the prompt for MCP tools marked [`requiresUserInteraction`](../06-MCP-Tools/General/mcp.md#require-approval-for-a-specific-tool) or for connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools) in sessions where that setting reaches Claude Code. Hooks can tighten restrictions but not loosen them past what permission rules allow.


[​](#hook-not-firing)

Hook not firing

The hook is configured but never executes.

- Run `/hooks` and confirm the hook appears under the correct event
- Check that the matcher pattern matches the tool name exactly. Matchers are case-sensitive
- Verify you’re triggering the right event type: `PreToolUse` fires before tool execution, `PostToolUse` fires after. A `PermissionRequest` hook fires when Claude Code is about to ask you for permission; see the [limitations](#limitations) for the non-interactive cases


[​](#hook-error-in-output)

Hook error in output

You see a message like “PreToolUse hook error: …” in the transcript.

- Your script exited with a non-zero code unexpectedly. Test it manually by piping sample JSON:

  ``` shiki
  echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | ./my-hook.sh
  echo $?  # Check the exit code
  ```
- If you see “command not found”, use absolute paths or `${CLAUDE_PROJECT_DIR}` to reference scripts. To avoid shell quoting entirely, add `"args": []` to switch to [exec form](hooks.md#exec-form-and-shell-form), which spawns the script directly without a shell
- If you see “jq: command not found”, install `jq` or use Python/Node.js for JSON parsing
- If the notice shows a JSON validation message, your hook’s stdout parsed as JSON but failed schema validation. If it shows a JSON parse message, the stdout looked like a JSON object but wasn’t valid JSON. Both happen even on exit 0. To fix a parse failure, build the payload with a JSON encoder such as `jq` instead of string concatenation, so quotes and backslashes inside values are escaped. The reference’s [Exit code output](hooks.md#exit-code-output) section covers the exit-code and JSON combinations
- If the script isn’t running at all, make it executable: `chmod +x ./my-hook.sh`


[​](#/hooks-shows-no-hooks-configured)

`/hooks` shows no hooks configured

You edited a settings file but the hooks don’t appear in the menu.

- File edits are normally picked up automatically. If they haven’t appeared after a few seconds, the file watcher may have missed the change: restart your session to force a reload.
- Verify your JSON is valid: trailing commas and comments aren’t allowed
- Confirm the settings file is in the correct location: `.claude/settings.json` for project hooks, `~/.claude/settings.json` for global hooks


[​](#stop-hook-hits-the-block-cap)

Stop hook hits the block cap

Claude keeps working instead of stopping, then ends the turn with a warning that the Stop hook blocked too many consecutive times. Claude Code overrides a Stop hook after it blocks eight times in a row without progress. Your hook script needs to check whether it already triggered a continuation. Parse the `stop_hook_active` field from the JSON input and exit early if it’s `true`:

```python
#!/bin/bash
INPUT=$(cat)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0  # Allow Claude to stop
fi
# ... rest of your hook logic
```

If your hook legitimately needs more than eight iterations to converge, raise the cap with [`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`](../02-Claude-Code-CLI/env-vars.md).


[​](#hook-json-has-no-effect)

Hook JSON has no effect

Your hook prints valid JSON, but the decision doesn’t take effect and no error appears in the transcript. Check which cause applies:

- **Extra output before the JSON**: something else writes to stdout first, usually an unconditional `echo` in your shell profile, so the output no longer starts with `{` and Claude Code doesn’t parse it as JSON. The cause and fix follow this list.
- **A field at the wrong level**: compare each field’s placement against the [JSON output](hooks.md#json-output) format. For example, `permissionDecision` belongs inside `hookSpecificOutput`, not at the top level.

When Claude Code runs a shell-form command hook, one without `args`, it spawns `sh -c` on macOS and Linux, Git Bash on Windows, or PowerShell when Git Bash isn’t installed by default. This shell is non-interactive, but Git Bash and some configurations, such as `BASH_ENV` pointing at `~/.bashrc`, still source your profile. If that profile contains unconditional `echo` statements, the output gets prepended to your hook’s JSON:

```python
Shell ready on arm64
{"decision": "block", "reason": "Not allowed"}
```

The combined output no longer starts with `{`, so Claude Code treats all of stdout as plain text and ignores the JSON. On exit 0 nothing is reported in the transcript; the parse attempt is recorded only in the [debug log](hooks.md#debug-hooks). To fix this, wrap echo statements in your shell profile so they only run in interactive shells:

```python
# In ~/.zshrc or ~/.bashrc
if [[ $- == *i* ]]; then
  echo "Shell ready"
fi
```

The `$-` variable contains shell flags, and `i` means interactive. Hooks run in non-interactive shells, so the echo is skipped. When your hook returns `permissionDecision` or `additionalContext` at the top level instead of inside `hookSpecificOutput`, the JSON still parses, and Claude Code ignores the misplaced fields without reporting an error. To see which fields it ignored, start Claude Code with `claude --debug` and search the [debug log](hooks.md#debug-hooks) for `Hook JSON output had unrecognized keys`.


[​](#debug-techniques)

Debug techniques

Press `Ctrl+O` to open the transcript view to check the outcome of a hook run:

- **Successful run**: you see nothing, unless the hook’s JSON surfaces something, such as `systemMessage` or Stop hook feedback.
  - To confirm a hook ran, check for its effect, like a reformatted file, or turn on debug logging as described below and trigger the hook again
- **Blocking error**: on most events you see the hook’s feedback. When the hook’s JSON made a blocking decision, the feedback is the reason from that decision; otherwise it is the hook’s stderr. On a few events, such as `ConfigChange` and `Elicitation`, a block surfaces no message.
- **Non-blocking error**: the action proceeded, and you see a `<hook name> hook error` notice with a short explanation, such as the first line of stderr prefixed with `Failed with non-blocking status code:`, or a JSON validation or parse message.

Which exit-code and JSON combinations produce each outcome, including the per-event exceptions, is defined in the reference’s [Exit code output](hooks.md#exit-code-output) section. For full execution details including which hooks matched, their exit codes, stdout, and stderr, read the debug log. Start Claude Code with `claude --debug-file /tmp/claude.log` to write to a known path, then `tail -f /tmp/claude.log` in another terminal. If you started without that flag, run `/debug` mid-session to enable logging and find the log path.


[​](#learn-more)

Learn more

- [Hooks reference](hooks.md): full event schemas, JSON output format, async hooks, and MCP tool hooks
- [Security considerations](hooks.md#security-considerations): review before deploying hooks in shared or production environments
- [Bash command validator example](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py): complete reference implementation
