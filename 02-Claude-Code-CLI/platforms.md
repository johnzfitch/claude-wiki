---
title: "Platforms and integrations - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/platforms"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-26T06:38:02Z"
tags: ["claude-code"]
---

## On this page

- [Where to run Claude Code](#where-to-run-claude-code)
- [Connect your tools](#connect-your-tools)
- [Work when you are away from your terminal](#work-when-you-are-away-from-your-terminal)
- [Related resources](#related-resources)
  - [Platforms](#platforms)
  - [Integrations](#integrations)
  - [Remote access](#remote-access)

Platforms and integrations

# Platforms and integrations

Copy pageCopy page

Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.

Copy pageCopy page

Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working. This page helps you pick the right platform for your workflow and connect the tools you already use.


[​](#where-to-run-claude-code)

Where to run Claude Code

Choose a platform based on how you like to work and where your project lives.

| Platform                               | Best for                                                                                           | What you get                                                                                                                                                                                        |
|:---------------------------------------|:---------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CLI](../01-Getting-Started/quickstart.md)             | Terminal workflows, scripting, remote servers                                                      | Full feature set, [Agent SDK](headless.md), [computer use](computer-use.md) on macOS (Pro and Max), third-party providers                                                               |
| [Desktop](../16-Mobile-Desktop/desktop.md)            | Visual review, parallel sessions, managed setup                                                    | Diff viewer, app preview, [computer use](../16-Mobile-Desktop/desktop.md#let-claude-use-your-computer) and [Dispatch](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch) on Pro and Max                                      |
| [VS Code](../03-IDE-Integrations/vs-code.md)            | Working inside VS Code without switching to a terminal                                             | Inline diffs, integrated terminal, file context                                                                                                                                                     |
| [JetBrains](../03-IDE-Integrations/jetbrains.md)        | Working inside IntelliJ, PyCharm, WebStorm, or other JetBrains IDEs                                | Diff viewer, selection sharing, terminal session                                                                                                                                                    |
| [Web](claude-code-on-the-web.md) | Long-running tasks that don’t need much steering, or work that should continue when you’re offline | Cloud, Anthropic-managed by default; continues after you disconnect                                                                                                                                 |
| [Mobile](../16-Mobile-Desktop/mobile.md)              | Starting and monitoring tasks while away from your computer                                        | Cloud sessions from the Claude app for iOS and Android, [Remote Control](remote-control.md) for local sessions, [Dispatch](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch) to Desktop on Pro and Max |

The CLI is the most complete surface for terminal-native work: scripting and the Agent SDK are CLI-only. Third-party providers also work in [VS Code](../03-IDE-Integrations/vs-code.md#use-third-party-providers) and in [JetBrains](feature-availability.md#features-available-on-every-provider), which runs the CLI in your IDE’s terminal. Enterprise [Desktop](../16-Mobile-Desktop/desktop.md) deployments support Google Cloud’s Agent Platform, and Desktop supports [gateway providers](../13-Enterprise-Admin/llm-gateway-connect.md#desktop-app); for Amazon Bedrock or Microsoft Foundry, use the CLI or an IDE extension, or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview), which runs the Code tab on those providers. Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration. The web runs in the cloud, so tasks keep going after you disconnect. Mobile is a thin client into those same cloud sessions or into a local session via Remote Control, and can send tasks to Desktop with Dispatch. You can mix surfaces on the same project. Configuration, project memory, and MCP servers are shared across the local surfaces.


[​](#connect-your-tools)

Connect your tools

Integrations let Claude work with services outside your codebase.

| Integration                                      | What it does                                                                       | Use it for                                                                          |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [Chrome](../03-IDE-Integrations/chrome.md)                        | Controls your browser with your logged-in sessions                                 | Testing web apps, filling forms, automating sites without an API                    |
| [GitHub Actions](github-actions.md)        | Runs Claude in your CI pipeline                                                    | Automated PR reviews, issue triage, scheduled maintenance                           |
| [GitLab CI/CD](gitlab-ci-cd.md)            | Same as GitHub Actions for GitLab                                                  | CI-driven automation on GitLab                                                      |
| [Code Review](code-review.md)              | Reviews every PR automatically                                                     | Catching bugs before human review                                                   |
| [Slack](../14-Connectors/slack.md)                          | Responds to `@Claude` mentions in your channels                                    | Turning bug reports into pull requests from team chat                               |
| [Claude Tag](https://claude.com/docs/claude-tag) | Runs `@Claude` as your organization’s shared identity with admin-configured access | Shared team access on Team and Enterprise plans, instead of per-user Slack sessions |

For integrations not listed here, [MCP servers](../06-MCP-Tools/General/mcp.md) and [connectors](../16-Mobile-Desktop/desktop.md#connect-external-tools) let you connect almost anything: Linear, Notion, Google Drive, or your own internal APIs.


[​](#work-when-you-are-away-from-your-terminal)

Work when you are away from your terminal

Claude Code offers several ways to work when you’re not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.

|                                                               | Trigger                                                                                           | Claude runs on                                                                                              | Setup                                                                                                                                          | Best for                                                      |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|
| [Dispatch](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch)           | Message a task from the Claude mobile app                                                         | Your machine (Desktop)                                                                                      | [Pair the mobile app with Desktop](https://code.claude.com/docs/99-Other/assign-tasks-from-anywhere-in-claude-cowork-claude-help-center-6bf98a1bec.md)                                                            | Delegating work while you’re away, minimal setup              |
| [Remote Control](remote-control.md)                     | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app    | Your machine (CLI, Desktop, or VS Code)                                                                     | Run [`claude remote-control` or `/remote-control`](remote-control.md#start-a-remote-control-session)                                     | Steering in-progress work from another device                 |
| [Channels](channels.md)                                 | Push events from a chat app like Telegram or Discord, or your own server                          | Your machine (CLI)                                                                                          | [Install a channel plugin](channels.md#quickstart) or [build your own](channels-reference.md)                                      | Reacting to external events like CI failures or chat messages |
| [Slack](../14-Connectors/slack.md)                                       | Mention `@Claude` in a team channel                                                               | Anthropic cloud                                                                                             | [Install the Slack app](../14-Connectors/slack.md#setting-up-claude-code-in-slack) with [Claude Code on the web](claude-code-on-the-web.md) enabled | PRs and reviews from team chat                                |
| [Self-hosted environments](../13-Enterprise-Admin/self-hosted-environments.md) | Start a [cloud session](claude-code-on-the-web.md) and pick your organization’s environment | Your organization’s infrastructure                                                                          | [Deploy runners](../13-Enterprise-Admin/self-hosted-environments-quickstart.md), on Team and Enterprise plans                                                   | Cloud sessions that must run inside your network              |
| [Scheduled tasks](scheduled-tasks.md)                   | Set a schedule                                                                                    | [CLI](scheduled-tasks.md), [Desktop](../16-Mobile-Desktop/desktop-scheduled-tasks.md), or [cloud](web-scheduled-tasks.md) | Pick a frequency                                                                                                                               | Recurring automation like daily reviews                       |

If you’re not sure where to start, [install the CLI](../01-Getting-Started/quickstart.md) and run it in a project directory. If you’d rather not use a terminal, [Desktop](../16-Mobile-Desktop/desktop-quickstart.md) gives you the same engine with a graphical interface.


[​](#related-resources)

Related resources


[​](#platforms)

Platforms

- [CLI quickstart](../01-Getting-Started/quickstart.md): install and run your first command in the terminal
- [Desktop](../16-Mobile-Desktop/desktop.md): visual diff review, parallel sessions, computer use, and Dispatch
- [VS Code](../03-IDE-Integrations/vs-code.md): the Claude Code extension inside your editor
- [JetBrains](../03-IDE-Integrations/jetbrains.md): the extension for IntelliJ, PyCharm, and other JetBrains IDEs
- [Web](claude-code-on-the-web.md): cloud sessions from your browser at claude.ai/code that keep running when you disconnect
- [Projects](claude-projects.md): one conversation where Claude coordinates many cloud sessions for a body of work and reports back
- [Mobile](../16-Mobile-Desktop/mobile.md): the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for starting and monitoring tasks while away from your computer


[​](#integrations)

Integrations

- [Chrome](../03-IDE-Integrations/chrome.md): automate browser tasks with your logged-in sessions
- [Computer use](computer-use.md): let Claude open apps and control your screen on macOS
- [GitHub Actions](github-actions.md): run Claude in your CI pipeline
- [GitLab CI/CD](gitlab-ci-cd.md): the same for GitLab
- [Code Review](code-review.md): automatic review on every pull request
- [Slack](../14-Connectors/slack.md): send tasks from team chat, get PRs back
- [Claude Tag](https://claude.com/docs/claude-tag): run `@Claude` as your organization’s shared identity on Team and Enterprise plans


[​](#remote-access)

Remote access

- [Dispatch](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch): message a task from your phone and it can spawn a Desktop session
- [Remote Control](remote-control.md): drive a running session from your phone or browser
- [Channels](channels.md): push events from chat apps or your own servers into a session
- [Scheduled tasks](scheduled-tasks.md): run prompts on a recurring schedule
