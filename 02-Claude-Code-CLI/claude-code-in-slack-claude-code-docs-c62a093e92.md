---
title: "Claude Code in Slack - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/slack"
category: "02-Claude-Code-CLI"
fetched_at: "2026-08-02T05:36:31Z"
tags: ["claude-code", "slack"]
---

## On this page

- [Use cases](#use-cases)
- [Prerequisites](#prerequisites)
- [Setting up Claude Code in Slack](#setting-up-claude-code-in-slack)
- [How it works](#how-it-works)
  - [Automatic detection](#automatic-detection)
  - [Context gathering](#context-gathering)
  - [Session flow](#session-flow)
- [User interface elements](#user-interface-elements)
  - [App Home](#app-home)
  - [Message actions](#message-actions)
  - [Repository selection](#repository-selection)
- [Access and permissions](#access-and-permissions)
  - [User-level access](#user-level-access)
  - [Workspace-level access](#workspace-level-access)
  - [Channel-based access control](#channel-based-access-control)
- [What’s accessible where](#what%E2%80%99s-accessible-where)
- [Best practices](#best-practices)
  - [Writing effective requests](#writing-effective-requests)
  - [When to use Slack vs. web](#when-to-use-slack-vs-web)
- [Troubleshooting](#troubleshooting)
  - [”Claude Code is not enabled for your account”](#%E2%80%9Dclaude-code-is-not-enabled-for-your-account%E2%80%9D)
  - [Sessions not starting](#sessions-not-starting)
  - [Sessions from a Claude Tag channel fail to start](#sessions-from-a-claude-tag-channel-fail-to-start)
  - [Repository not showing](#repository-not-showing)
  - [Wrong repository selected](#wrong-repository-selected)
  - [Authentication errors](#authentication-errors)
  - [Session expiration](#session-expiration)
- [Current limitations](#current-limitations)
- [Related resources](#related-resources)

Platforms and integrations

# Claude Code in Slack

Copy pageCopy page

Delegate coding tasks directly from your Slack workspace. Anthropic is retiring this earlier version for Team and Enterprise workspaces in favor of Claude Tag; it remains the setup path on Pro and Max plans.

Copy pageCopy page

This page documents the earlier Claude Code in Slack, which runs each session under an individual user’s account.

- **Team and Enterprise plans:** Anthropic is retiring this version in favor of [Claude Tag](https://claude.com/docs/claude-tag/overview), which runs @Claude as your organization’s shared identity with admin-configured access. Your existing Slack app and @Claude handle stay, and your Anthropic account team can tell you the cutover date. Set up Claude Tag for a new workspace; to move one that already uses this version, see [Migrate from the earlier Claude in Slack](https://claude.com/docs/claude-tag/admins/migrate-from-earlier).
- **Pro and Max plans:** Claude Tag isn’t available on individual plans, so this page remains the setup path.

Claude Code in Slack brings the power of Claude Code directly into your Slack workspace. When you mention `@Claude` with a coding task, Claude automatically detects the intent and creates a Claude Code session on the web, allowing you to delegate development work without leaving your team conversations. This integration is built on the existing Claude for Slack app but adds intelligent routing to Claude Code on the web for coding-related requests. Each session runs under your own Claude account, using your connected repositories and your plan limits.


[​](#use-cases)

Use cases

- **Bug investigation and fixes**: Ask Claude to investigate and fix bugs as soon as they’re reported in Slack channels.
- **Quick code reviews and modifications**: Have Claude implement small features or refactor code based on team feedback.
- **Collaborative debugging**: When team discussions provide crucial context (e.g., error reproductions or user reports), Claude can use that information to inform its debugging approach.
- **Parallel task execution**: Kick off coding tasks in Slack while you continue other work, receiving notifications when complete.


[​](#prerequisites)

Prerequisites

Before using Claude Code in Slack, ensure you have the following:

| Requirement            | Details                                                                                           |
|:-----------------------|:--------------------------------------------------------------------------------------------------|
| Claude Plan            | Pro, Max, Team, or Enterprise with Claude Code access (premium seats or Chat + Claude Code seats) |
| Claude Code on the web | Access to [Claude Code on the web](/docs/en/claude-code-on-the-web) must be enabled               |
| GitHub Account         | Connected to Claude Code on the web with at least one repository authenticated                    |
| Slack Authentication   | Your Slack account linked to your Claude account via the Claude app                               |


[​](#setting-up-claude-code-in-slack)

Setting up Claude Code in Slack

1

Install the Claude App in Slack

A workspace administrator must install the Claude app from the Slack App Marketplace. Visit the [Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4) and click “Add to Slack” to begin the installation process.

2

Connect your Claude account

After the app is installed, authenticate your individual Claude account:

1.  Open the Claude app in Slack by clicking on “Claude” in your Apps section
2.  Navigate to the App Home tab
3.  Click “Connect” to link your Slack account with your Claude account
4.  Complete the authentication flow in your browser

3

Configure Claude Code on the web

Ensure your Claude Code on the web is properly configured:

- Visit [claude.ai/code](https://claude.ai/code) and sign in with the same account you connected to Slack
- Connect your GitHub account if not already connected
- Authenticate at least one repository that you want Claude to work with

4

Choose your routing mode

After connecting your accounts, configure how Claude handles your messages in Slack. Navigate to the Claude App Home in Slack to find the **Routing Mode** setting.

| Mode            | Behavior                                                                                                                                                                                                                                 |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Code only**   | Claude routes all @mentions to Claude Code sessions. Best for teams using Claude in Slack exclusively for development tasks.                                                                                                             |
| **Code + Chat** | Claude analyzes each message and intelligently routes between Claude Code (for coding tasks) and Claude Chat (for writing, analysis, and general questions). Best for teams who want a single @Claude entry point for all types of work. |

In Code + Chat mode, if Claude routes a message to Chat but you wanted a coding session, you can click “Retry as Code” to create a Claude Code session instead. Similarly, if it’s routed to Code but you wanted a Chat session, you can choose that option in that thread.

5

Add Claude to channels

Claude is not automatically added to any channels after installation. To use Claude in a channel, invite it by typing `/invite @Claude` in that channel. Claude can only respond to @mentions in channels where it has been added.


[​](#how-it-works)

How it works


[​](#automatic-detection)

Automatic detection

When you mention @Claude in a Slack channel or thread, Claude automatically analyzes your message to determine if it’s a coding task. If Claude detects coding intent, it will route your request to Claude Code on the web instead of responding as a regular chat assistant. You can also explicitly tell Claude to handle a request as a coding task, even if it doesn’t automatically detect it.

Claude Code in Slack only works in channels (public or private). It does not work in direct messages (DMs).


[​](#context-gathering)

Context gathering

**From threads**: When you @mention Claude in a thread, it gathers context from all messages in that thread to understand the full conversation. **From channels**: When mentioned directly in a channel, Claude looks at recent channel messages for relevant context. This context helps Claude understand the problem, select the appropriate repository, and inform its approach to the task.

When @Claude is invoked in Slack, Claude is given access to the conversation context to better understand your request. Claude may follow directions from other messages in the context, so users should make sure to only use Claude in trusted Slack conversations.


[​](#session-flow)

Session flow

1.  **Initiation**: You @mention Claude with a coding request
2.  **Detection**: Claude analyzes your message and detects coding intent
3.  **Session creation**: A new Claude Code session is created on claude.ai/code
4.  **Progress updates**: Claude posts status updates to your Slack thread as work progresses
5.  **Completion**: When finished, Claude @mentions you with a summary and action buttons
6.  **Review**: Click “View Session” to see the full transcript, or “Create PR” to open a pull request


[​](#user-interface-elements)

User interface elements


[​](#app-home)

App Home

The App Home tab shows your connection status and allows you to connect or disconnect your Claude account from Slack.


[​](#message-actions)

Message actions

- **View Session**: Opens the full Claude Code session in your browser where you can see all work performed, continue the session, or make additional requests.
- **Create PR**: Creates a pull request directly from the session’s changes.
- **Retry as Code**: If Claude initially responds as a chat assistant but you wanted a coding session, click this button to retry the request as a Claude Code task.
- **Change Repo**: Allows you to select a different repository if Claude chose incorrectly.


[​](#repository-selection)

Repository selection

Claude automatically selects a repository based on context from your Slack conversation. If multiple repositories could apply, Claude may display a dropdown allowing you to choose the correct one.


[​](#access-and-permissions)

Access and permissions


[​](#user-level-access)

User-level access

| Access Type          | Requirement                                                     |
|:---------------------|:----------------------------------------------------------------|
| Claude Code Sessions | Each user runs sessions under their own Claude account          |
| Usage & Rate Limits  | Sessions count against the individual user’s plan limits        |
| Repository Access    | Users can only access repositories they’ve personally connected |
| Session History      | Sessions appear in your Claude Code history on claude.ai/code   |


[​](#workspace-level-access)

Workspace-level access

Slack workspace administrators control whether the Claude app is available in their workspace:

| Control                      | Description                                                                                                       |
|:-----------------------------|:------------------------------------------------------------------------------------------------------------------|
| App installation             | Workspace admins decide whether to install the Claude app from the Slack App Marketplace                          |
| Enterprise Grid distribution | For Enterprise Grid organizations, organization admins can control which workspaces have access to the Claude app |
| App removal                  | Removing the app from a workspace immediately revokes access for all users in that workspace                      |


[​](#channel-based-access-control)

Channel-based access control

Claude is not automatically added to any channels after installation. Users must explicitly invite Claude to channels where they want to use it:

- **Invite required**: Type `/invite @Claude` in any channel to add Claude to that channel
- **Channel membership controls access**: Claude can only respond to @mentions in channels where it has been added
- **Access gating through channels**: Admins can control who uses Claude Code by managing which channels Claude is invited to and who has access to those channels
- **Private channel support**: Claude works in both public and private channels, giving teams flexibility in controlling visibility

This channel-based model allows teams to restrict Claude Code usage to specific channels, providing an additional layer of access control beyond workspace-level permissions.


[​](#what’s-accessible-where)

What’s accessible where

**In Slack**: You’ll see status updates, completion summaries, and action buttons. The full transcript is preserved and always accessible. **On the web**: The complete Claude Code session with full conversation history, all code changes, file operations, and the ability to continue the session or create pull requests. For Enterprise and Team accounts, sessions created from Claude in Slack are automatically visible to the organization. See [Claude Code on the Web sharing](/docs/en/claude-code-on-the-web#share-sessions) for more details.


[​](#best-practices)

Best practices


[​](#writing-effective-requests)

Writing effective requests

- **Be specific**: Include file names, function names, or error messages when relevant.
- **Provide context**: Mention the repository or project if it’s not clear from the conversation.
- **Define success**: Explain what “done” looks like—should Claude write tests? Update documentation? Create a PR?
- **Use threads**: Reply in threads when discussing bugs or features so Claude can gather the full context.


[​](#when-to-use-slack-vs-web)

When to use Slack vs. web

**Use Slack when**: Context already exists in a Slack discussion, you want to kick off a task asynchronously, or you’re collaborating with teammates who need visibility. **Use the web directly when**: You need to upload files, want real-time interaction during development, or are working on longer, more complex tasks.


[​](#troubleshooting)

Troubleshooting


[​](#”claude-code-is-not-enabled-for-your-account”)

”Claude Code is not enabled for your account”

This error means your Claude account has no cloud environment yet, not that an admin needs to enable anything. Sign in at [claude.ai/code](https://claude.ai/code) once with the same account you connected to Slack. The first visit creates your default cloud environment, and the error clears on your next mention. Each user must do this individually.


[​](#sessions-not-starting)

Sessions not starting

1.  Verify your Claude account is connected in the Claude App Home
2.  Check that you have Claude Code on the web access enabled
3.  Ensure you have at least one GitHub repository connected to Claude Code


[​](#sessions-from-a-claude-tag-channel-fail-to-start)

Sessions from a Claude Tag channel fail to start

This entry applies to workspaces using [Claude Tag](https://claude.com/docs/claude-tag/overview), where Claude works in channels as your organization’s shared identity, not as any member’s account. If you created the channel’s cloud environment at [claude.ai/code](https://claude.ai/code), it belongs to your personal account, and Claude can’t start channel sessions in a personal environment. Claude Code fails the session immediately, and retrying doesn’t help. If you’re an Owner or admin, recreate the environment as an [organization-shared environment](/docs/en/cloud-environments#organization-shared-environments) from the **Cloud environments** page in [admin settings](https://claude.ai/admin-settings). You can apply it in two ways:

- Set it as the organization default at [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code).
- [Set it on the channel](https://claude.com/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one) in the Claude Tag admin settings.

If you’re not an Owner or admin, send this entry to one.


[​](#repository-not-showing)

Repository not showing

1.  Connect the repository in Claude Code on the web at [claude.ai/code](https://claude.ai/code)
2.  Verify your GitHub permissions for that repository
3.  Try disconnecting and reconnecting your GitHub account


[​](#wrong-repository-selected)

Wrong repository selected

1.  Click the “Change Repo” button to select a different repository
2.  Include the repository name in your request for more accurate selection


[​](#authentication-errors)

Authentication errors

1.  Disconnect and reconnect your Claude account in the App Home
2.  Ensure you’re signed into the correct Claude account in your browser
3.  Check that your Claude plan includes Claude Code access


[​](#session-expiration)

Session expiration

1.  Sessions remain accessible in your Claude Code history on the web
2.  You can continue or reference past sessions from [claude.ai/code](https://claude.ai/code)


[​](#current-limitations)

Current limitations

- **GitHub only**: Currently supports repositories on GitHub.
- **One PR at a time**: Each session can create one pull request.
- **Rate limits apply**: Sessions use your individual Claude plan’s rate limits.
- **Web access required**: Users must have Claude Code on the web access; those without it will only get standard Claude chat responses.


[​](#related-resources)

Related resources

## Claude Code on the web

Learn more about Claude Code on the web

## Claude for Slack

General Claude for Slack documentation

## Claude Tag

Organization-managed @Claude in Slack with admin-configured access

## Slack App Marketplace

Install the Claude app from the Slack Marketplace

## Claude Help Center

Get additional support
