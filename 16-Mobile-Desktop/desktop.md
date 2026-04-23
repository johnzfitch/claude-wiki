---
title: "Use Claude Code Desktop"
source_url: "https://code.claude.com/docs/en/desktop.md"
category: "16-Mobile-Desktop"
fetched_at: "2026-04-08"
tags: ["claude-code", "cli", "desktop"]
---

# Use Claude Code Desktop

Get more out of Claude Code Desktop: computer use, Dispatch sessions from your phone, parallel sessions with Git isolation, visual diff review, app previews, PR monitoring, connectors, and enterprise configuration.

The Code tab within the Claude Desktop app lets you use Claude Code through a graphical interface instead of the terminal.

## Key capabilities

- **Visual diff review** with inline comments
- **Live app preview** with dev servers
- **Computer use** to open apps and control your screen on macOS and Windows
- **GitHub PR monitoring** with auto-fix and auto-merge
- **Parallel sessions** with automatic Git worktree isolation
- **Dispatch** integration: send a task from your phone, get a session here
- **Scheduled tasks** that run Claude on a recurring schedule
- **Connectors** for GitHub, Slack, Linear, and more
- Local, SSH, and cloud environments

## Start a session

Configure four things in the prompt area before sending your first message:

1. **Environment**: Local, Remote, or SSH
2. **Folder**: the project directory Claude will work in
3. **Model**: Opus, Sonnet, or Haiku (cannot change after session starts)
4. **Permission mode**: controls what Claude can do without asking

## Work with code

### Add files and context to prompts

- Type `@filename` to pull a specific file into conversation
- Attach images and PDFs using the attachment button
- Drag and drop files into the prompt

### Review changes with diff view

After Claude edits files, a `+12 -1` indicator appears. Click it to open the diff view:
- Review modifications file by file
- Comment on specific lines (Claude reads comments and revises)
- Click **Review code** for Claude to self-evaluate diffs

### Choose a permission mode

| Mode             | What it does                              |
| :--------------- | :---------------------------------------- |
| Ask permissions  | Default. Claude asks before every edit    |
| Auto accept      | Auto-accepts file edits                   |
| Plan mode        | Claude plans without editing              |
| Auto mode        | Everything runs with safety checks        |
| Bypass           | No permission prompts (containers only)   |

### Preview your app

Click **Preview** dropdown to run your dev server in the desktop. Claude can view the running app, test endpoints, inspect logs, and iterate.

## Let Claude use your computer

Computer use is available on macOS and Windows (Pro and Max plans). Enable in **Settings > General** under Desktop app.

Claude can open apps, click, type, and see your screen. Each app requires per-session approval.

## Monitor pull request status

After opening a PR, Claude monitors CI check results. You can enable:
- **Auto-fix**: Claude automatically fixes CI failures
- **Auto-merge**: Claude merges the PR once all checks pass

## Manage sessions

### Work in parallel with sessions

Open parallel sessions from the sidebar. Each session can use its own Git worktree for isolation.

### Run long-running tasks remotely

Send work to Anthropic's cloud so it continues even if you close the app. Remote sessions work against a fresh clone of your repository.

### Continue in another surface

Transfer a session to the web, CLI, or mobile app to continue working elsewhere.

## Extend Claude Code

### Install plugins

Click **+** → **Plugins** to browse and install plugins that add skills, agents, MCP servers, and more.

### Connect external tools

Use connectors for GitHub, Slack, Linear, and more. Available in **Settings > Connectors**.

### Sessions from Dispatch

Pair the Claude mobile app with Desktop. When you message a task from your phone, Desktop spawns a session to handle it.

## SSH sessions

Connect to remote machines over SSH. Claude Code must be installed on the remote machine.

## Environment configuration

### Enterprise settings

Admins can configure:
- Allowed models and permission modes
- MCP server allowlists
- Network and proxy settings
- Feature flags

## Coming from the CLI

Desktop runs the same engine as the CLI with a graphical interface. They share configuration (CLAUDE.md, MCP servers, hooks, skills, settings).

Key differences:
- Desktop adds diff viewer, app preview, computer use (Windows), Dispatch
- CLI has Agent SDK, third-party providers, headless mode
- Both can run simultaneously on the same project

## Troubleshooting

### 403 or authentication errors

Sign out and sign back in. Check your subscription is active.

### Code tab not appearing

Ensure you have a Pro, Max, Team, or Enterprise subscription.

### Session hangs or stops responding

Try creating a new session. If persistent, restart the desktop app.

## See Also

- [Get started with Desktop](desktop-quickstart.md)
- [Desktop scheduled tasks](desktop-scheduled-tasks.md)
- [Permission modes](../02-Claude-Code-CLI/permission-modes.md)
- [Best practices](/en/best-practices)
