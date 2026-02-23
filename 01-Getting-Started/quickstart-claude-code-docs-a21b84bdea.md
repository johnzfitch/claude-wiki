---
category: "01-Getting-Started"
fetched_at: "2026-02-23T00:45:40Z"
source_url: "https://code.claude.com/docs/en/quickstart"
title: "Quickstart - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Getting started

Quickstart

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Getting started

- [](/docs/en/overview)
  Overview
- [](/docs/en/quickstart)
  Quickstart
- [](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
  Changelog

##### Core concepts

- [](/docs/en/how-claude-code-works)
  How Claude Code works
- [](/docs/en/features-overview)
  Extend Claude Code
- [](/docs/en/common-workflows)
  Common workflows
- [](/docs/en/best-practices)
  Best practices

##### Platforms and integrations

- [](/docs/en/claude-code-on-the-web)
  Claude Code on the web

- Claude Code on desktop

- [](/docs/en/chrome)
  Chrome extension (beta)

- [](/docs/en/vs-code)
  Visual Studio Code

- [](/docs/en/jetbrains)
  JetBrains IDEs

- [](/docs/en/github-actions)
  GitHub Actions

- [](/docs/en/gitlab-ci-cd)
  GitLab CI/CD

- [](/docs/en/slack)
  Claude Code in Slack

On this page

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

Copy page

Welcome to Claude Code!

Copy page

This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.

## 

[​](#before-you-begin)

Before you begin

Make sure you have:

- A terminal or command prompt open
- A code project to work with
- A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise), [Claude Console](https://console.anthropic.com/) account, or access through a [supported cloud provider](/docs/en/third-party-integrations)

This guide covers the terminal CLI. Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](/docs/en/desktop), in [VS Code](/docs/en/vs-code) and [JetBrains IDEs](/docs/en/jetbrains), in [Slack](/docs/en/slack), and in CI/CD with [GitHub Actions](/docs/en/github-actions) and [GitLab](/docs/en/gitlab-ci-cd). See [all interfaces](/docs/en/overview#use-claude-code-everywhere).

## 

[​](#step-1-install-claude-code)

Step 1: Install Claude Code

To install Claude Code, use one of the following methods:

- Native Install (Recommended)

- Homebrew

- WinGet

**macOS, Linux, WSL:**

Report incorrect code

Copy

Ask AI

``` shiki
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Report incorrect code

Copy

Ask AI

``` shiki
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Report incorrect code

Copy

Ask AI

``` shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

Report incorrect code

Copy

Ask AI

``` shiki
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

Report incorrect code

Copy

Ask AI

``` shiki
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

## 

[​](#step-2-log-in-to-your-account)

Step 2: Log in to your account

Claude Code requires an account to use. When you start an interactive session with the `claude` command, you’ll need to log in:

Report incorrect code

Copy

Ask AI

``` shiki
claude
# You'll be prompted to log in on first use
```

Report incorrect code

Copy

Ask AI

``` shiki
/login
# Follow the prompts to log in with your account
```

You can log in using any of these account types:

- [Claude Pro, Max, Teams, or Enterprise](https://claude.com/pricing) (recommended)
- [Claude Console](https://console.anthropic.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
- [Amazon Bedrock, Google Vertex AI, or Microsoft Foundry](/docs/en/third-party-integrations) (enterprise cloud providers)

Once logged in, your credentials are stored and you won’t need to log in again. To switch accounts later, use the `/login` command.

## 

[​](#step-3-start-your-first-session)

Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:

Report incorrect code

Copy

Ask AI

``` shiki
cd /path/to/your/project
claude
```

You’ll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type `/help` for available commands or `/resume` to continue a previous conversation.

After logging in (Step 2), your credentials are stored on your system. Learn more in [Credential Management](/docs/en/authentication#credential-management).

## 

[​](#step-4-ask-your-first-question)

Step 4: Ask your first question

Let’s start with understanding your codebase. Try one of these commands:

Report incorrect code

Copy

Ask AI

``` shiki
what does this project do?
```

Claude will analyze your files and provide a summary. You can also ask more specific questions:

Report incorrect code

Copy

Ask AI

``` shiki
what technologies does this project use?
```

Report incorrect code

Copy

Ask AI

``` shiki
where is the main entry point?
```

Report incorrect code

Copy

Ask AI

``` shiki
explain the folder structure
```

You can also ask Claude about its own capabilities:

Report incorrect code

Copy

Ask AI

``` shiki
what can Claude Code do?
```

Report incorrect code

Copy

Ask AI

``` shiki
how do I create custom skills in Claude Code?
```

Report incorrect code

Copy

Ask AI

``` shiki
can Claude Code work with Docker?
```

Claude Code reads your files as needed - you don’t have to manually add context. Claude also has access to its own documentation and can answer questions about its features and capabilities.

## 

[​](#step-5-make-your-first-code-change)

Step 5: Make your first code change

Now let’s make Claude Code do some actual coding. Try a simple task:

Report incorrect code

Copy

Ask AI

``` shiki
add a hello world function to the main file
```

Claude Code will:

1.  Find the appropriate file
2.  Show you the proposed changes
3.  Ask for your approval
4.  Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.

## 

[​](#step-6-use-git-with-claude-code)

Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:

Report incorrect code

Copy

Ask AI

``` shiki
what files have I changed?
```

Report incorrect code

Copy

Ask AI

``` shiki
commit my changes with a descriptive message
```

You can also prompt for more complex Git operations:

Report incorrect code

Copy

Ask AI

``` shiki
create a new branch called feature/quickstart
```

Report incorrect code

Copy

Ask AI

``` shiki
show me the last 5 commits
```

Report incorrect code

Copy

Ask AI

``` shiki
help me resolve merge conflicts
```

## 

[​](#step-7-fix-a-bug-or-add-a-feature)

Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation. Describe what you want in natural language:

Report incorrect code

Copy

Ask AI

``` shiki
add input validation to the user registration form
```

Or fix existing issues:

Report incorrect code

Copy

Ask AI

``` shiki
there's a bug where users can submit empty forms - fix it
```

Claude Code will:

- Locate the relevant code
- Understand the context
- Implement a solution
- Run tests if available

## 

[​](#step-8-test-out-other-common-workflows)

Step 8: Test out other common workflows

There are a number of ways to work with Claude: **Refactor code**

Report incorrect code

Copy

Ask AI

``` shiki
refactor the authentication module to use async/await instead of callbacks
```

**Write tests**

Report incorrect code

Copy

Ask AI

``` shiki
write unit tests for the calculator functions
```

**Update documentation**

Report incorrect code

Copy

Ask AI

``` shiki
update the README with installation instructions
```

**Code review**

Report incorrect code

Copy

Ask AI

``` shiki
review my changes and suggest improvements
```

**Remember**: Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.

## 

[​](#essential-commands)

Essential commands

Here are the most important commands for daily use:

| Command | What it does | Example |
|----|----|----|
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `claude commit` | Create a Git commit | `claude commit` |
| `/clear` | Clear conversation history | `/clear` |
| `/help` | Show available commands | `/help` |
| `exit` or Ctrl+C | Exit Claude Code | `exit` |

See the [CLI reference](/docs/en/cli-reference) for a complete list of commands.

## 

[​](#pro-tips-for-beginners)

Pro tips for beginners

For more, see [best practices](/docs/en/best-practices) and [common workflows](/docs/en/common-workflows).

Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

Use step-by-step instructions

Break complex tasks into steps:

Report incorrect code

Copy

Ask AI

``` shiki
1. create a new database table for user profiles
2. create an API endpoint to get and update user profiles
3. build a webpage that allows users to see and edit their information
```

Let Claude explore first

Before making changes, let Claude understand your code:

Report incorrect code

Copy

Ask AI

``` shiki
analyze the database schema
```

Report incorrect code

Copy

Ask AI

``` shiki
build a dashboard showing products that are most frequently returned by our UK customers
```

Save time with shortcuts

- Press `?` to see all available keyboard shortcuts
- Use Tab for command completion
- Press ↑ for command history
- Type `/` to see all commands and skills

## 

[​](#what’s-next)

What’s next?

Now that you’ve learned the basics, explore more advanced features:

[](/docs/en/how-claude-code-works)

## How Claude Code works

Understand the agentic loop, built-in tools, and how Claude Code interacts with your project

[](/docs/en/best-practices)

## Best practices

Get better results with effective prompting and project setup

[](/docs/en/common-workflows)

## Common workflows

Step-by-step guides for common tasks

[](/docs/en/features-overview)

## Extend Claude Code

Customize with CLAUDE.md, skills, hooks, MCP, and more

## 

[​](#getting-help)

Getting help

- **In Claude Code**: Type `/help` or ask “how do I…”
- **Documentation**: You’re here! Browse other guides
- **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support

Was this page helpful?

Yes

No

[Overview](/docs/en/overview)[Changelog](/docs/en/changelog)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
