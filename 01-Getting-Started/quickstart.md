---
title: "Quickstart - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/quickstart"
category: "01-Getting-Started"
fetched_at: "2026-10-08T06:25:00Z"
tags: ["claude-code", "getting-started"]
---

## On this page

- [Before you begin](#before-you-begin)
- [Step 1: Install Claude Code](#step-1-install-claude-code)
- [Step 2: Start your first session](#step-2-start-your-first-session)
- [Step 3: Ask your first question](#step-3-ask-your-first-question)
- [Step 4: Make your first code change](#step-4-make-your-first-code-change)
- [Step 5: Use Git with Claude Code](#step-5-use-git-with-claude-code)
- [Step 6: Fix a bug or add a feature](#step-6-fix-a-bug-or-add-a-feature)
- [Step 7: Test out other common workflows](#step-7-test-out-other-common-workflows)
- [Essential commands](#essential-commands)
  - [Shell commands](#shell-commands)
  - [Session commands](#session-commands)
- [Pro tips for beginners](#pro-tips-for-beginners)
- [What’s next?](#what%E2%80%99s-next)
- [Getting help](#getting-help)

Getting started

# Quickstart

Copy pageCopy page

Install Claude Code in your terminal, sign in, and use the CLI to explore your codebase and make your first code change.

Copy pageCopy page

This quickstart covers Claude Code in your terminal: installing the CLI, signing in from your first session, and using it for common development tasks in your own project.


[​](#before-you-begin)

Before you begin

Make sure you have:

- A terminal or command prompt open
- A code project to work with
- A [Claude subscription](../17-Billing-Plans/pricing.md) (Pro, Max, Team, or Enterprise), [Claude Console](../04-API-Reference/Other/playground.md) account, or access through a [supported cloud provider](../02-Claude-Code-CLI/third-party-integrations.md)

These cases are covered on other pages:

- **Never used a terminal before**: start with the [terminal guide](../02-Claude-Code-CLI/terminal-guide.md)
- **Want Claude Code somewhere other than the terminal**: Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](../16-Mobile-Desktop/desktop.md), in [VS Code](../03-IDE-Integrations/vs-code.md) and [JetBrains IDEs](../03-IDE-Integrations/jetbrains.md), in [Slack](../14-Connectors/slack.md), and in CI/CD with [GitHub Actions](../02-Claude-Code-CLI/github-actions.md) and [GitLab](../02-Claude-Code-CLI/gitlab-ci-cd.md). See [all interfaces](../02-Claude-Code-CLI/code-home.md#use-claude-code-everywhere).


[​](#step-1-install-claude-code)

Step 1: Install Claude Code

To install Claude Code, open a terminal and run the command for your system. If you haven’t used a terminal before, the [terminal guide](../02-Claude-Code-CLI/terminal-guide.md) shows how to open one and paste the command.

- Native Install (Recommended)

- Homebrew

- WinGet

**macOS, Linux, WSL:**

```python
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows, your prompt shows `PS C:\` when you’re in PowerShell and `C:\` without the `PS` when you’re in CMD.**Windows PowerShell:**

```python
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```python
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

The install command shows no progress while it downloads Claude Code. When the installer finishes, open a new terminal window and run `claude --version`. A working installation prints a version number. If your shell says `claude` isn’t found or isn’t recognized, the install directory isn’t on your PATH yet: see [Fix your PATH](../02-Claude-Code-CLI/troubleshoot-install.md#command-not-found-claude-after-installation).If you see `The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you’re in CMD, not PowerShell.If the install command fails with `syntax error near unexpected token '<'`, a `403`, or any other error, see [Troubleshoot installation](../02-Claude-Code-CLI/troubleshoot-install.md#find-your-error) to match the error to a fix and for alternative install methods.[Git for Windows](https://git-scm.com/downloads/win) is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.

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

You can also install with [apt, dnf, or apk](setup.md#install-with-linux-package-managers) on Debian, Fedora, RHEL, and Alpine. To confirm the installation worked, run:

```python
claude --version
```

The command prints a version number followed by `(Claude Code)`.


[​](#step-2-start-your-first-session)

Step 2: Start your first session

Open your terminal in any project directory and start Claude Code:

```python
cd /path/to/your/project
claude
```

Replace `/path/to/your/project` with the path to the project you want to work on. Claude Code prompts you to log in on first use. For Claude subscription or Console accounts, follow the prompts to complete authentication in your browser. If you’ve set the `ANTHROPIC_API_KEY` environment variable and you approve the key when Claude Code asks whether to use it, Claude Code skips the login prompt. You can log in using any of these account types:

- [Claude Pro, Max, Team, or Enterprise](../17-Billing-Plans/pricing.md) (recommended)
- [Claude Console](../04-API-Reference/Other/playground.md) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
- [Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry](../02-Claude-Code-CLI/third-party-integrations.md) (enterprise cloud providers)
- A self-hosted [Claude apps gateway](../13-Enterprise-Admin/claude-apps-gateway.md), if your organization runs one: your admin pre-configures the gateway URL, and `/login` opens directly on the **Cloud gateway** screen for you to sign in with corporate SSO

Once logged in, your credentials are stored and you won’t need to log in again. Learn more in [Credential Management](../02-Claude-Code-CLI/authentication.md#credential-management). The Claude Code prompt appears with the version, current model, and working directory shown above it. Type `/help` for available commands or `/resume` to continue a previous conversation. To switch accounts later or re-authenticate, type `/login` inside the running session.


[​](#step-3-ask-your-first-question)

Step 3: Ask your first question

Try one of these commands:

```python
what does this project do?
```

Claude will analyze your files and provide a summary. You can also ask more specific questions:

```python
what technologies does this project use?
```

```python
where is the main entry point?
```

```python
explain the folder structure
```

You can also ask Claude about its own capabilities:

```python
what can Claude Code do?
```

```python
how do I create custom skills in Claude Code?
```

```python
can Claude Code work with Docker?
```

Claude Code reads your project files as needed. You don’t have to manually add context.


[​](#step-4-make-your-first-code-change)

Step 4: Make your first code change

Try a small task:

```python
add a hello world function to the main file
```

Claude Code finds the appropriate file and shows you the change. If it asks before making the change, select **Yes** to approve. The session’s [permission mode](../02-Claude-Code-CLI/permission-modes.md) sets which actions Claude can take without asking you first. Press `Shift+Tab` at any time to switch the permission mode of the session you’re in.


[​](#step-5-use-git-with-claude-code)

Step 5: Use Git with Claude Code

Claude Code makes Git operations conversational:

```python
what files have I changed?
```

```python
commit my changes with a descriptive message
```

You can also prompt for more complex Git operations:

```python
create a new branch called feature/quickstart
```

```python
show me the last 5 commits
```

```python
help me resolve merge conflicts
```


[​](#step-6-fix-a-bug-or-add-a-feature)

Step 6: Fix a bug or add a feature

Describe what you want in natural language:

```python
add input validation to the user registration form
```

Or fix existing issues:

```python
there's a bug where users can submit empty forms - fix it
```


[​](#step-7-test-out-other-common-workflows)

Step 7: Test out other common workflows

Try a few more prompts. You can ask Claude to refactor code, write tests, update documentation, or review your changes:

```python
refactor the authentication module to use async/await instead of callbacks
```

```python
write unit tests for the calculator functions
```

```python
update the README with installation instructions
```

```python
review my changes and suggest improvements
```

Talk to Claude like you would a helpful colleague. Describe what you want to achieve, and it will help you get there.


[​](#essential-commands)

Essential commands

Here are the most important commands for daily use, grouped by where you run them.


[​](#shell-commands)

Shell commands

Run these from your terminal to start or resume Claude Code.

| Command             | What it does                                           | Example                             |
|---------------------|--------------------------------------------------------|-------------------------------------|
| `claude`            | Start interactive mode                                 | `claude`                            |
| `claude "task"`     | Start interactive mode with an initial prompt          | `claude "fix the build error"`      |
| `claude -p "query"` | Run one-off query, then exit                           | `claude -p "explain this function"` |
| `claude -c`         | Continue most recent conversation in current directory | `claude -c`                         |
| `claude -r`         | Resume a previous conversation                         | `claude -r`                         |

See the [CLI reference](../02-Claude-Code-CLI/cli-reference.md) for the complete list of shell commands.


[​](#session-commands)

Session commands

Run these inside Claude Code after it starts.

| Command                 | What it does               | Example  |
|-------------------------|----------------------------|----------|
| `/clear`                | Clear conversation history | `/clear` |
| `/help`                 | Show available commands    | `/help`  |
| `/exit` or Ctrl+D twice | Exit Claude Code           | `/exit`  |

See the [commands reference](../02-Claude-Code-CLI/commands.md) for the complete list of session commands.


[​](#pro-tips-for-beginners)

Pro tips for beginners

For more, see [best practices](../02-Claude-Code-CLI/best-practices.md) and [common workflows](../02-Claude-Code-CLI/common-workflows.md).

Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:

```python
1. create a new database table for user profiles
2. create an API endpoint to get and update user profiles
3. build a webpage that allows users to see and edit their information
```

Let Claude explore first

Before making changes, let Claude understand your code:

```python
analyze the database schema
```

```python
build a dashboard showing products that are most frequently returned by our UK customers
```

Save time with shortcuts

- Type `/` to see the commands and skills available to you
- Use Tab for command completion
- Press ↑ for command history
- Press `Shift+Tab` to cycle permission modes


[​](#what’s-next)

What’s next?

Now that you’ve learned the basics, explore more advanced features:

- [How Claude Code works](../02-Claude-Code-CLI/how-claude-code-works.md): understand the agentic loop, built-in tools, and how Claude Code interacts with your project
- [Best practices](../02-Claude-Code-CLI/best-practices.md): get better results with effective prompting and project setup
- [Common workflows](../02-Claude-Code-CLI/common-workflows.md): step-by-step guides for common tasks
- [Extend Claude Code](../02-Claude-Code-CLI/features-overview.md): customize with CLAUDE.md, skills, hooks, MCP, and more

See [advanced setup](setup.md) for installation options, manual updates, or uninstallation instructions.


[​](#getting-help)

Getting help

- **In Claude Code**: type `/help` or ask a “how do I” question
- **Documentation**: browse the other guides on this site
- **Courses**: take [Claude Code 101](https://academy.claude.com/courses/claude-code-101) and other free self-paced courses on [Claude Academy](https://academy.claude.com/)
- **Community**: join the [Discord server](https://www.anthropic.com/discord) for tips and support
