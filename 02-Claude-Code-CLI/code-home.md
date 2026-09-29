---
title: "Overview - Claude Code Docs"
source_url: "https://code.claude.com/docs"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-29T06:29:26Z"
tags: ["claude-code"]
---

## On this page

- [Get started](#get-started)
- [What you can do](#what-you-can-do)
- [Use Claude Code everywhere](#use-claude-code-everywhere)
- [Next steps](#next-steps)

Getting started

# Overview

Copy pageCopy page

Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.

Copy pageCopy page

Claude Code is an AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks. It understands your entire codebase and can work across multiple files and tools to get things done.


[​](#get-started)

Get started

Claude Code runs on several surfaces: the terminal, IDE extensions, a desktop app, and the web. Choose one from the tabs below to get started. Most surfaces require a [Claude subscription](../17-Billing-Plans/pricing.md) or [Anthropic Console](../04-API-Reference/Other/usage-limits.md) account. The Terminal CLI, VS Code, and JetBrains also support [third-party providers](third-party-integrations.md).

- Terminal

- VS Code

- Desktop app

- Web

- JetBrains

The full-featured CLI for working with Claude Code directly in your terminal. Edit files, run commands, and manage your entire project from the command line.To install Claude Code, open a terminal and run the command for your system. If you haven’t used a terminal before, the [terminal guide](terminal-guide.md) shows how to open one and paste the command.

- Native Install (Recommended)

- Homebrew

- WinGet

**macOS, Linux, WSL:**

```python
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```python
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```python
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

When the installer finishes, open a new terminal window and run `claude --version`. A working installation prints a version number. If your shell says `claude` isn’t found or isn’t recognized, the install directory isn’t on your PATH yet: see [Fix your PATH](troubleshoot-install.md#command-not-found-claude-after-installation).If you see `The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you’re in CMD, not PowerShell. Your prompt shows `PS C:\` when you’re in PowerShell and `C:\` without the `PS` when you’re in CMD.If the install command fails with `syntax error near unexpected token '<'`, a `403`, or another curl error, see [Troubleshoot installation](troubleshoot-install.md#find-your-error) to match the error to a fix and for alternative install methods.[Git for Windows](https://git-scm.com/downloads/win) is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.

Native installations automatically update in the background to keep you on the latest version.

```python
brew install --cask claude-code
```

Homebrew offers two casks. `claude-code` tracks the stable release channel, which is typically about a week behind and skips releases with major regressions. `claude-code@latest` tracks the latest channel and receives new versions as soon as they ship.

Homebrew installations do not auto-update. Run `brew upgrade claude-code` or `brew upgrade claude-code@latest`, depending on which cask you installed, to get the latest features and security fixes.

```python
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

You can also install with [apt, dnf, or apk](../01-Getting-Started/setup.md#install-with-linux-package-managers) on Debian, Fedora, RHEL, and Alpine.Then start Claude Code in any project. Replace `your-project` with the path to a project directory on your machine:

```python
cd your-project
claude
```

You’ll be prompted to log in on first use. If you’ve set the `ANTHROPIC_API_KEY` environment variable, Claude Code skips the login prompt and asks you to approve the key instead. That’s it! [Continue with the Quickstart →](../01-Getting-Started/quickstart.md)

See [advanced setup](../01-Getting-Started/setup.md) for installation options, manual updates, or uninstallation instructions. Visit [installation troubleshooting](troubleshoot-install.md) if you hit issues.

The VS Code extension provides inline diffs, @-mentions, plan review, and conversation history directly in your editor.

- [Install for VS Code](vscode:extension/anthropic.claude-code)
- [Install for Cursor](cursor:extension/anthropic.claude-code)

Or search for “Claude Code” in the Extensions view (`Cmd+Shift+X` on Mac, `Ctrl+Shift+X` on Windows/Linux). After installing, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`), type “Claude Code”, and select **Open in New Tab**.[Get started with VS Code →](../03-IDE-Integrations/vs-code.md#get-started)

A standalone app for running Claude Code outside your IDE or terminal. Review diffs visually, run multiple sessions side by side, schedule recurring tasks, and start cloud sessions.Download and install:

- [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs) (Intel and Apple Silicon)
- [Windows](https://claude.ai/api/desktop/win32/x64/setup/latest/redirect?utm_source=claude_code&utm_medium=docs) (x64)
- [Windows ARM64](https://claude.ai/api/desktop/win32/arm64/setup/latest/redirect?utm_source=claude_code&utm_medium=docs)
- On Ubuntu or Debian, where the app is in beta, install it with apt by following the [Linux install instructions](../16-Mobile-Desktop/desktop-linux.md)

After installing, launch Claude, sign in, and click the **Code** tab to start coding. The app includes Claude Code, so you don’t need to install the CLI separately. A [paid subscription](../17-Billing-Plans/pricing.md) is required.[Learn more about the desktop app →](../16-Mobile-Desktop/desktop-quickstart.md)

Run Claude Code in your browser with no local setup. Kick off long-running tasks and check back when they’re done, work on repos you don’t have locally, or run multiple tasks in parallel. For a longer body of work, create a [project](claude-projects.md) and let Claude coordinate the parallel sessions for you. Available on desktop browsers and [the Claude app for iOS and Android](../16-Mobile-Desktop/mobile.md).Start coding at [claude.ai/code](https://claude.ai/code).[Get started →](web-quickstart.md)

A plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with interactive diff viewing and selection context sharing.Install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains Marketplace and restart your IDE. The plugin requires the Claude Code CLI, installed separately; see the [JetBrains setup steps](../03-IDE-Integrations/jetbrains.md#installation).[Get started with JetBrains →](../03-IDE-Integrations/jetbrains.md)


[​](#what-you-can-do)

What you can do

Here are some of the ways you can use Claude Code:

Automate the work you keep putting off

Claude Code handles the tedious tasks that eat up your day: writing tests for untested code, fixing lint errors across a project, resolving merge conflicts, updating dependencies, and writing release notes.

```python
claude "write tests for the auth module, run them, and fix any failures"
```

Build features and fix bugs

Describe what you want in plain language. Claude Code plans the approach, writes the code across multiple files, and verifies it works.For bugs, paste an error message or describe the symptom. Claude Code traces the issue through your codebase, identifies the root cause, and implements a fix. See [common workflows](common-workflows.md) for more examples.

Create commits and pull requests

Claude Code works directly with git. It stages changes, writes commit messages, creates branches, and opens pull requests.

```python
claude "commit my changes with a descriptive message"
```

In CI, you can automate code review and issue triage with [GitHub Actions](github-actions.md) or [GitLab CI/CD](gitlab-ci-cd.md).

Connect your tools with MCP

The [Model Context Protocol (MCP)](../06-MCP-Tools/General/mcp.md) is an open standard for connecting AI tools to external data sources. With MCP, Claude Code can read your design docs in Google Drive, update tickets in Jira, pull data from Slack, or use your own custom tooling. The [MCP quickstart](../06-MCP-Tools/General/mcp-quickstart.md) connects your first server end to end.

Customize with instructions, skills, and hooks

[`CLAUDE.md`](memory.md) is a markdown file you add to your project root that Claude Code reads at the start of every session. Use it to set coding standards, architecture decisions, preferred libraries, and review checklists. If your repository already has an `AGENTS.md` for other coding agents, Claude Code [can read that](memory.md#agents-md) on its own or alongside `CLAUDE.md`. Claude also builds [auto memory](memory.md#auto-memory) as it works, saving learnings across sessions without you writing anything.Create [skills](../08-Plugins-Skills/skills.md) to package repeatable workflows your team can share, like `/review-pr` or `/deploy-staging`.[Hooks](../07-Hooks/hooks.md) let you run shell commands before or after Claude Code actions, like auto-formatting after every file edit or running lint before a commit.

Run agents in parallel and build custom agents

Spawn [multiple Claude Code agents](../09-Agents-Patterns/sub-agents.md) that work on different parts of a task simultaneously. A lead agent coordinates the work, assigns subtasks, and merges results.To run several full sessions in parallel and watch them from one screen, use [background agents](../09-Agents-Patterns/agent-view.md). For fully custom workflows, the [Agent SDK](../05-Agent-SDK/agent-sdk-overview.md) lets you build your own agents powered by Claude Code’s tools and capabilities, with full control over orchestration, tool access, and permissions.

Pipe, script, and automate with the CLI

Claude Code is composable and follows the Unix philosophy. Pipe logs into it, run it in CI, or chain it with other tools:

```python
# Analyze recent log output
tail -200 app.log | claude -p "Slack me if you see any anomalies"

# Automate translations in CI
claude -p "translate new strings into French and raise a PR for review"

# Bulk operations across files
git diff main --name-only | claude -p "review these changed files for security issues"
```

See the [CLI reference](cli-reference.md) for the full set of commands and flags.

Schedule recurring tasks

Run Claude on a schedule to automate work that repeats: morning PR reviews, overnight CI failure analysis, weekly dependency audits, or syncing docs after PRs merge.

- [Routines](web-scheduled-tasks.md) run in the cloud, so they keep running even when your computer is off. They can also trigger on API calls or GitHub events. Create them from the web, the Desktop app, or by running `/schedule` in the CLI.
- [Desktop scheduled tasks](../16-Mobile-Desktop/desktop-scheduled-tasks.md) run on your machine, with direct access to your local files and tools
- [`/loop`](scheduled-tasks.md) repeats a prompt within a CLI session for quick polling

Work from anywhere

Sessions aren’t tied to a single surface. Move work between them as your context changes:

- Step away from your desk and keep working from your phone or any browser with [Remote Control](remote-control.md)
- Message [Dispatch](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch) a task from your phone and open the Desktop session it creates
- Start a long-running task on the [web](claude-code-on-the-web.md) or the [Claude mobile app](../16-Mobile-Desktop/mobile.md), then pull it into your terminal with `claude --teleport`. Teleport requires a claude.ai subscription.
- Run `/desktop` to continue your current terminal session in the [Desktop app](../16-Mobile-Desktop/desktop.md), where you can review diffs visually. The `/desktop` handoff requires a claude.ai subscription. Available on macOS and x64 Windows.
- Route tasks from team chat: mention `@Claude` in [Slack](../14-Connectors/slack.md) with a bug report and get a pull request back


[​](#use-claude-code-everywhere)

Use Claude Code everywhere

Each [surface](glossary.md#surface) connects to the same underlying Claude Code engine, so your repo’s CLAUDE.md files, settings, and MCP servers work across all of them. Beyond the [Terminal](../01-Getting-Started/quickstart.md), [VS Code](../03-IDE-Integrations/vs-code.md), [JetBrains](../03-IDE-Integrations/jetbrains.md), [Desktop](../16-Mobile-Desktop/desktop.md), and [Web](claude-code-on-the-web.md) surfaces above, Claude Code integrates with CI/CD, chat, and browser workflows:

| What I want to do                                                               | Best option                                                                                                               |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Continue a local session from my phone or another device                        | [Remote Control](remote-control.md)                                                                                 |
| Push events from Telegram, Discord, iMessage, or my own webhooks into a session | [Channels](channels.md)                                                                                             |
| Start a task locally, continue on mobile                                        | [`claude --cloud`](claude-code-on-the-web.md#from-terminal-to-cloud), then the [Claude mobile app](../16-Mobile-Desktop/mobile.md) |
| Run Claude on a recurring schedule                                              | [Routines](web-scheduled-tasks.md) or [Desktop scheduled tasks](../16-Mobile-Desktop/desktop-scheduled-tasks.md)                              |
| Automate PR reviews and issue triage                                            | [GitHub Actions](github-actions.md) or [GitLab CI/CD](gitlab-ci-cd.md)                                        |
| Get automatic code review on every PR                                           | [GitHub Code Review](code-review.md)                                                                                |
| Route bug reports from Slack to pull requests                                   | [Slack](../14-Connectors/slack.md)                                                                                                   |
| Debug live web applications                                                     | [Chrome](../03-IDE-Integrations/chrome.md)                                                                                                 |
| Build custom agents for your own workflows                                      | [Agent SDK](../05-Agent-SDK/agent-sdk-overview.md)                                                                                  |


[​](#next-steps)

Next steps

Once you’ve installed Claude Code, these guides help you go deeper.

- [Quickstart](../01-Getting-Started/quickstart.md): walk through your first real task, from exploring a codebase to committing a fix
- [Store instructions and memories](memory.md): give Claude persistent instructions with CLAUDE.md files and auto memory
- [Common workflows](common-workflows.md) and [best practices](best-practices.md): patterns for getting the most out of Claude Code
- [Claude Academy](https://academy.claude.com/): free self-paced courses, including [Claude Code 101](https://academy.claude.com/courses/claude-code-101) and [Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)
- [A harness for every task](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code): how the Claude Code team uses [dynamic workflows](workflows.md) to orchestrate many subagents at once
- [Settings](settings.md): customize Claude Code for your workflow
- [Troubleshooting](troubleshooting.md): solutions for common issues
- [code.claude.com](../15-Claude-AI-Features/claude-com-product-claude-code.md): demos, pricing, and product details
