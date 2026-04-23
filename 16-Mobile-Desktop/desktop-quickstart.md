---
title: "Get started with the desktop app"
source_url: "https://code.claude.com/docs/en/desktop-quickstart.md"
category: "16-Mobile-Desktop"
fetched_at: "2026-04-08"
tags: ["cli", "desktop"]
---

# Get started with the desktop app

Install Claude Code on desktop and start your first coding session.

The desktop app gives you Claude Code with a graphical interface: visual diff review, live app preview, GitHub PR monitoring with auto-merge, parallel sessions with Git worktree isolation, scheduled tasks, and the ability to run tasks remotely. No terminal required.

## Downloads

- **macOS**: Universal build for Intel and Apple Silicon
- **Windows**: x64 and ARM64 installers
- Linux is not currently supported.

> Claude Code requires a Pro, Max, Team, or Enterprise subscription.

The desktop app has three tabs:

- **Chat**: General conversation with no file access, similar to claude.ai
- **Cowork**: An autonomous background agent that works on tasks in a cloud VM with its own environment
- **Code**: An interactive coding assistant with direct access to your local files

## Install

1. **Install and sign in**: Download Claude for your platform and run the installer. Launch and sign in with your Anthropic account.
2. **Open the Code tab**: Click the Code tab at the top center. If it prompts you to upgrade, you need a paid plan.

The desktop app includes Claude Code. You don't need to install Node.js or the CLI separately. To use `claude` from the terminal, install the CLI separately.

## Start your first session

1. **Choose an environment and folder**: Select **Local** to run Claude on your machine. Click **Select folder** and choose your project directory. You can also select **Remote** (Anthropic cloud) or **SSH** (remote machine).

2. **Choose a model**: Select from the dropdown next to the send button. You cannot change the model after the session starts.

3. **Tell Claude what to do**:
   - `Find a TODO comment and fix it`
   - `Add tests for the main function`
   - `Create a CLAUDE.md with instructions for this codebase`

4. **Review and accept changes**: By default, Claude proposes changes and waits for your approval before applying them. You'll see diff views showing exactly what will change, with Accept/Reject buttons.

## Now what?

- **Interrupt and steer**: Click the stop button or type your correction at any point
- **Give Claude more context**: Type `@filename` to pull a specific file, attach images and PDFs, or drag and drop files
- **Use skills**: Type `/` or click **+** → **Slash commands** to browse commands and skills
- **Review changes**: Click `+12 -1` indicators to open the diff view. Click **Review code** to have Claude evaluate diffs
- **Adjust permissions**: Ask permissions (default) requires approval before every edit. Auto accept edits auto-accepts file edits. Plan mode lets Claude map out an approach without touching files
- **Add plugins**: Click **+** → **Plugins** to browse and install plugins
- **Preview your app**: Click **Preview** to run your dev server in the desktop
- **Track pull requests**: After opening a PR, Claude monitors CI and can auto-fix failures or merge
- **Schedule tasks**: Set up scheduled tasks for recurring work (daily code review, dependency audit)
- **Scale up**: Open parallel sessions, send work to the cloud, or continue in another surface

## Coming from the CLI?

Desktop runs the same engine as the CLI with a graphical interface. You can run both simultaneously on the same project, and they share configuration (CLAUDE.md files, MCP servers, hooks, skills, and settings).

## See Also

- [Use Claude Code Desktop](desktop.md)
- [Troubleshooting](/en/desktop#troubleshooting)
- [Best practices](/en/best-practices)
- [Common workflows](/en/common-workflows)
