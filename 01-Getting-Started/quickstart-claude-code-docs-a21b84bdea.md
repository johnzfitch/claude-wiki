---
title: "Quickstart - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/quickstart"
category: "01-Getting-Started"
fetched_at: "2026-08-02T05:37:59Z"
tags: ["claude-code"]
---

## On this page

- [Before you begin](#before-you-begin)
- [Step 1: Install Claude Code](#step-1-install-claude-code)
- [Step 2: Log in to your account](#step-2-log-in-to-your-account)
- [Step 3: Start your first session](#step-3-start-your-first-session)
- [Step 4: Ask your first question](#step-4-ask-your-first-question)
- [Step 5: Make your first code change](#step-5-make-your-first-code-change)
- [Step 6: Use Git with Claude Code](#step-6-use-git-with-claude-code)
- [Step 7: Fix a bug or add a feature](#step-7-fix-a-bug-or-add-a-feature)
- [Step 8: Test out other common workflows](#step-8-test-out-other-common-workflows)
- [Essential commands](#essential-commands)
- [Pro tips for beginners](#pro-tips-for-beginners)
- [What’s next?](#what%E2%80%99s-next)
- [Getting help](#getting-help)

Getting started

# Quickstart

Copy pageCopy page

Welcome to Claude Code!

Copy pageCopy page

This quickstart guide will have you using AI-powered coding assistance in a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.


[​](#before-you-begin)

Before you begin

Make sure you have:

- A terminal or command prompt open
  - If you’ve never used the terminal before, check out the [terminal guide](/docs/en/terminal-guide)
- A code project to work with
- A [Claude subscription](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_prereq) (Pro, Max, Team, or Enterprise), [Claude Console](https://console.anthropic.com/) account, or access through a [supported cloud provider](/docs/en/third-party-integrations)

This guide covers the terminal CLI. Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](/docs/en/desktop), in [VS Code](/docs/en/vs-code) and [JetBrains IDEs](/docs/en/jetbrains), in [Slack](/docs/en/slack), and in CI/CD with [GitHub Actions](/docs/en/github-actions) and [GitLab](/docs/en/gitlab-ci-cd). See [all interfaces](/docs/en/overview#use-claude-code-everywhere).


[​](#step-1-install-claude-code)

Step 1: Install Claude Code

To install Claude Code, use one of the following methods:

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

If you see `The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you’re in CMD, not PowerShell. Your prompt shows `PS C:\` when you’re in PowerShell and `C:\` without the `PS` when you’re in CMD.If the install command fails with `syntax error near unexpected token '<'`, a `403`, or another curl error, see [Troubleshoot installation](/docs/en/troubleshoot-install#find-your-error) to match the error to a fix and for alternative install methods.[Git for Windows](https://git-scm.com/downloads/win) is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.

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

You can also install with [apt, dnf, or apk](/docs/en/setup#install-with-linux-package-managers) on Debian, Fedora, RHEL, and Alpine. To confirm the installation worked, run:

```python
claude --version
```

The command prints a version number followed by `(Claude Code)`.


[​](#step-2-log-in-to-your-account)

Step 2: Log in to your account

Claude Code requires an account to use. Start an interactive session with the `claude` command and you’ll be prompted to log in on first use:

```python
claude
```

For Claude subscription or Console accounts, follow the prompts to complete authentication in your browser. If you’ve set the `ANTHROPIC_API_KEY` environment variable, Claude Code skips the login prompt and asks you to approve the key instead. To switch accounts later or re-authenticate, type `/login` inside the running session:

```python
/login
```

You can log in using any of these account types:

- [Claude Pro, Max, Team, or Enterprise](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_login) (recommended)
- [Claude Console](https://console.anthropic.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
- [Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry](/docs/en/third-party-integrations) (enterprise cloud providers)
- A self-hosted [Claude apps gateway](/docs/en/claude-apps-gateway), if your organization runs one: your admin pre-configures the gateway URL, and `/login` opens directly on the **Cloud gateway** screen for you to sign in with corporate SSO

Once logged in, your credentials are stored and you won’t need to log in again.


[​](#step-3-start-your-first-session)

Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

```python
cd /path/to/your/project
claude
```

Replace `/path/to/your/project` with the path to the project you want to work on. You’ll see the Claude Code prompt with the version, current model, and working directory shown above it. Type `/help` for available commands or `/resume` to continue a previous conversation.

After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](/docs/en/authentication#credential-management).


[​](#step-4-ask-your-first-question)

Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:

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


[​](#step-5-make-your-first-code-change)

Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:

```python
add a hello world function to the main file
```

Claude Code will:

1.  Find the appropriate file
2.  Show you the proposed changes
3.  Ask for your approval before changing files, depending on your permission mode
4.  Make the edit

Whether Claude Code asks before changing files depends on your [permission mode](/docs/en/permission-modes). In default mode, Claude asks for approval before each change. Press `Shift+Tab` to cycle through modes: `acceptEdits` auto-approves file edits, and `plan` lets Claude propose changes without editing. Some accounts also have an `auto` mode that runs a background safety check and blocks risky actions, returning to prompts only after repeated blocks.


[​](#step-6-use-git-with-claude-code)

Step 6: Use Git with Claude Code

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


[​](#step-7-fix-a-bug-or-add-a-feature)

Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation. Describe what you want in natural language:

```python
add input validation to the user registration form
```

Or fix existing issues:

```python
there's a bug where users can submit empty forms - fix it
```

Claude Code will:

- Locate the relevant code
- Understand the context
- Implement a solution
- Run tests if available


[​](#step-8-test-out-other-common-workflows)

Step 8: Test out other common workflows

There are a number of ways to work with Claude: **Refactor code**

```python
refactor the authentication module to use async/await instead of callbacks
```

**Write tests**

```python
write unit tests for the calculator functions
```

**Update documentation**

```python
update the README with installation instructions
```

**Code review**

```python
review my changes and suggest improvements
```

Talk to Claude like you would a helpful colleague. Describe what you want to achieve, and it will help you get there.


[​](#essential-commands)

Essential commands

Here are the most important commands for daily use. Shell commands run from your terminal to start or resume Claude Code. Session commands run inside Claude Code after it starts. **Shell commands**

| Command             | What it does                                           | Example                             |
|---------------------|--------------------------------------------------------|-------------------------------------|
| `claude`            | Start interactive mode                                 | `claude`                            |
| `claude "task"`     | Run a one-time task                                    | `claude "fix the build error"`      |
| `claude -p "query"` | Run one-off query, then exit                           | `claude -p "explain this function"` |
| `claude -c`         | Continue most recent conversation in current directory | `claude -c`                         |
| `claude -r`         | Resume a previous conversation                         | `claude -r`                         |

**Session commands**

| Command                 | What it does               | Example  |
|-------------------------|----------------------------|----------|
| `/clear`                | Clear conversation history | `/clear` |
| `/help`                 | Show available commands    | `/help`  |
| `/exit` or Ctrl+D twice | Exit Claude Code           | `/exit`  |

See the [CLI reference](/docs/en/cli-reference) for the complete list of shell commands and the [commands reference](/docs/en/commands) for the complete list of session commands.


[​](#pro-tips-for-beginners)

Pro tips for beginners

For more, see [best practices](/docs/en/best-practices) and [common workflows](/docs/en/common-workflows).

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

- Type `/` to see all commands and skills
- Use Tab for command completion
- Press ↑ for command history
- Press `Shift+Tab` to cycle permission modes


[​](#what’s-next)

What’s next?

Now that you’ve learned the basics, explore more advanced features:

## How Claude Code works

Understand the agentic loop, built-in tools, and how Claude Code interacts with your project

## Best practices

Get better results with effective prompting and project setup

## Common workflows

Step-by-step guides for common tasks

## Extend Claude Code

Customize with CLAUDE.md, skills, hooks, MCP, and more


[​](#getting-help)

Getting help

- **In Claude Code**: Type `/help` or ask “how do I…”
- **Documentation**: You’re here! Browse other guides
- **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support
