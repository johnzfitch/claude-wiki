---
title: "Platforms and integrations"
source_url: "https://code.claude.com/docs/en/platforms.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["claude-code"]
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Platforms and integrations

> Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.

Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working. This page helps you pick the right platform for your workflow and connect the tools you already use.

## Where to run Claude Code

Choose a platform based on how you like to work and where your project lives.

| Platform                          | Best for                                                                                           | What you get                                                                                                                                                                              |
| :-------------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CLI](../01-Getting-Started/quickstart-claude-code-docs-a21b84bdea.md)             | Terminal workflows, scripting, remote servers                                                      | Full feature set, [Agent SDK](headless-b99e3140ec.md), [computer use](computer-use-427032da98.md) on macOS (Pro and Max), third-party providers                                                               |
| [Desktop](../16-Mobile-Desktop/desktop.md)            | Visual review, parallel sessions, managed setup                                                    | Diff viewer, app preview, [computer use](/en/desktop#let-claude-use-your-computer) and [Dispatch](/en/desktop#sessions-from-dispatch) on Pro and Max                                      |
| [VS Code](../03-IDE-Integrations/use-claude-code-in-vs-code-claude-code-docs-29143b6fee.md)            | Working inside VS Code without switching to a terminal                                             | Inline diffs, integrated terminal, file context                                                                                                                                           |
| [JetBrains](../03-IDE-Integrations/jetbrains-4cf6bd8c22.md)        | Working inside IntelliJ, PyCharm, WebStorm, or other JetBrains IDEs                                | Diff viewer, selection sharing, terminal session                                                                                                                                          |
| [Web](claude-code-on-the-web-69d53821d4.md) | Long-running tasks that don't need much steering, or work that should continue when you're offline | Anthropic-managed cloud, continues after you disconnect                                                                                                                                   |
| Mobile                            | Starting and monitoring tasks while away from your computer                                        | Cloud sessions from the Claude app for iOS and Android, [Remote Control](continue-local-sessions-from-any-device-with-remote-control-claude-code-docs-c1c03fd914.md) for local sessions, [Dispatch](/en/desktop#sessions-from-dispatch) to Desktop on Pro and Max |

The CLI is the most complete surface for terminal-native work: scripting, third-party providers, and the Agent SDK are CLI-only. Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration. The web runs in Anthropic's cloud, so tasks keep going after you disconnect. Mobile is a thin client into those same cloud sessions or into a local session via Remote Control, and can send tasks to Desktop with Dispatch.

You can mix surfaces on the same project. Configuration, project memory, and MCP servers are shared across the local surfaces.

## Connect your tools

Integrations let Claude work with services outside your codebase.

| Integration                          | What it does                                       | Use it for                                                       |
| :----------------------------------- | :------------------------------------------------- | :--------------------------------------------------------------- |
| [Chrome](../03-IDE-Integrations/use-claude-code-with-chrome-beta-claude-code-docs-4f2f5a5a96.md)                 | Controls your browser with your logged-in sessions | Testing web apps, filling forms, automating sites without an API |
| [GitHub Actions](claude-code-github-actions-claude-code-docs-0d633fbd8a.md) | Runs Claude in your CI pipeline                    | Automated PR reviews, issue triage, scheduled maintenance        |
| [GitLab CI/CD](claude-code-gitlab-ci-cd-claude-code-docs-fbcd915fee.md)     | Same as GitHub Actions for GitLab                  | CI-driven automation on GitLab                                   |
| [Code Review](code-review-09694cae75.md)       | Reviews every PR automatically                     | Catching bugs before human review                                |
| [Slack](../14-Connectors/claude-code-in-slack-claude-code-docs-c62a093e92.md)                   | Responds to `@Claude` mentions in your channels    | Turning bug reports into pull requests from team chat            |

For integrations not listed here, [MCP servers](../06-MCP-Tools/mcp-208e742686.md) and [connectors](/en/desktop#connect-external-tools) let you connect almost anything: Linear, Notion, Google Drive, or your own internal APIs.

## Work when you are away from your terminal

Claude Code offers several ways to work when you're not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.

|                                                | Trigger                                                                                        | Claude runs on                                                                               | Setup                                                                                                                                | Best for                                                      |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| [Dispatch](/en/desktop#sessions-from-dispatch) | Message a task from the Claude mobile app                                                      | Your machine (Desktop)                                                                       | [Pair the mobile app with Desktop](https://support.claude.com/en/articles/13947068)                                                  | Delegating work while you're away, minimal setup              |
| [Remote Control](continue-local-sessions-from-any-device-with-remote-control-claude-code-docs-c1c03fd914.md)           | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app | Your machine (CLI or VS Code)                                                                | Run `claude remote-control`                                                                                                          | Steering in-progress work from another device                 |
| [Channels](channels-00374ea787.md)                       | Push events from a chat app like Telegram or Discord, or your own server                       | Your machine (CLI)                                                                           | [Install a channel plugin](/en/channels#quickstart) or [build your own](channels-reference-claude-code-docs-67a0bbe41f.md)                                      | Reacting to external events like CI failures or chat messages |
| [Slack](../14-Connectors/claude-code-in-slack-claude-code-docs-c62a093e92.md)                             | Mention `@Claude` in a team channel                                                            | Anthropic cloud                                                                              | [Install the Slack app](/en/slack#setting-up-claude-code-in-slack) with [Claude Code on the web](claude-code-on-the-web-69d53821d4.md) enabled | PRs and reviews from team chat                                |
| [Scheduled tasks](run-prompts-on-a-schedule-claude-code-docs.md)         | Set a schedule                                                                                 | [CLI](run-prompts-on-a-schedule-claude-code-docs.md), [Desktop](../16-Mobile-Desktop/desktop-scheduled-tasks.md), or [cloud](routines-3111c7bd3a.md) | Pick a frequency                                                                                                                     | Recurring automation like daily reviews                       |

If you're not sure where to start, [install the CLI](../01-Getting-Started/quickstart-claude-code-docs-a21b84bdea.md) and run it in a project directory. If you'd rather not use a terminal, [Desktop](../16-Mobile-Desktop/desktop-quickstart.md) gives you the same engine with a graphical interface.

## Related resources

### Platforms

* [CLI quickstart](../01-Getting-Started/quickstart-claude-code-docs-a21b84bdea.md): install and run your first command in the terminal
* [Desktop](../16-Mobile-Desktop/desktop.md): visual diff review, parallel sessions, computer use, and Dispatch
* [VS Code](../03-IDE-Integrations/use-claude-code-in-vs-code-claude-code-docs-29143b6fee.md): the Claude Code extension inside your editor
* [JetBrains](../03-IDE-Integrations/jetbrains-4cf6bd8c22.md): the extension for IntelliJ, PyCharm, and other JetBrains IDEs
* [Claude Code on the web](claude-code-on-the-web-69d53821d4.md): cloud sessions that keep running when you disconnect
* Mobile: the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for starting and monitoring tasks while away from your computer

### Integrations

* [Chrome](../03-IDE-Integrations/use-claude-code-with-chrome-beta-claude-code-docs-4f2f5a5a96.md): automate browser tasks with your logged-in sessions
* [Computer use](computer-use-427032da98.md): let Claude open apps and control your screen on macOS
* [GitHub Actions](claude-code-github-actions-claude-code-docs-0d633fbd8a.md): run Claude in your CI pipeline
* [GitLab CI/CD](claude-code-gitlab-ci-cd-claude-code-docs-fbcd915fee.md): the same for GitLab
* [Code Review](code-review-09694cae75.md): automatic review on every pull request
* [Slack](../14-Connectors/claude-code-in-slack-claude-code-docs-c62a093e92.md): send tasks from team chat, get PRs back

### Remote access

* [Dispatch](/en/desktop#sessions-from-dispatch): message a task from your phone and it can spawn a Desktop session
* [Remote Control](continue-local-sessions-from-any-device-with-remote-control-claude-code-docs-c1c03fd914.md): drive a running session from your phone or browser
* [Channels](channels-00374ea787.md): push events from chat apps or your own servers into a session
* [Scheduled tasks](run-prompts-on-a-schedule-claude-code-docs.md): run prompts on a recurring schedule
