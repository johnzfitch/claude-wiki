---
title: "Claude Code on mobile - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/mobile"
category: "16-Mobile-Desktop"
fetched_at: "2026-09-26T06:38:01Z"
tags: ["claude-code", "desktop", "mobile"]
---

## On this page

- [Get the app](#get-the-app)
- [Work from your phone](#work-from-your-phone)
  - [Start and monitor cloud sessions](#start-and-monitor-cloud-sessions)
  - [Continue a local session with Remote Control](#continue-a-local-session-with-remote-control)
  - [Get push notifications](#get-push-notifications)
- [Limitations](#limitations)
- [Related resources](#related-resources)

Platforms and integrations

# Claude Code on mobile

Copy pageCopy page

Start, monitor, and steer Claude Code tasks from your phone with the Claude app for iOS and Android.

Copy pageCopy page

The Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) is a client for Claude Code sessions rather than a place where code runs. From your phone you reach [cloud sessions](#start-and-monitor-cloud-sessions) and [projects](../02-Claude-Code-CLI/claude-projects.md) in the cloud, a session running on your own machine through [Remote Control](#continue-a-local-session-with-remote-control), or the Desktop app through [Dispatch](desktop.md#sessions-from-dispatch).

Claude Code doesn’t have a separate mobile app: cloud sessions and Remote Control both live in the **Code** tab in the Claude app, and Dispatch is a task you message in the app.


[​](#get-the-app)

Get the app

1

Download the Claude app

Install the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) or [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude). On an iPad, install the same iOS app.

Run `/mobile` in a Claude Code session to show a QR code for [claude.ai/mobile](https://claude.ai/mobile), which opens the right app store for your phone. `/ios` and `/android` do the same thing.

2

Sign in

Sign in with the same claude.ai account and organization you use for Claude Code. Cloud sessions and Remote Control require a claude.ai account, so they aren’t reachable with an Anthropic Console API key or from a third-party provider such as Amazon Bedrock.

3

Open the Code tab

Tap **Code** in the app’s navigation to reach your sessions, or open [claude.ai/code/new](https://claude.ai/code/new) on your phone to start a new Code session in the app. If you don’t see the Code tab, your plan or organization may not include these features; see [availability by subscription plan](../02-Claude-Code-CLI/feature-availability.md#availability-by-subscription-plan).


[​](#work-from-your-phone)

Work from your phone

From the app you can start cloud sessions, open a project, drive a Claude Code session running on your computer, or message Dispatch a task. The app is the same for each; they differ in where the work happens.

| Feature                                             | What you connect to                                                               | When to use                                                                                                                                                 |
|:----------------------------------------------------|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cloud sessions](../02-Claude-Code-CLI/claude-code-on-the-web.md)   | A session on cloud infrastructure, Anthropic-managed by default                   | Your repository is on GitHub and the task should keep running after you put your phone away. See the [cloud quickstart](../02-Claude-Code-CLI/web-quickstart.md) to set up. |
| [Projects](../02-Claude-Code-CLI/claude-projects.md)                | A conversation where Claude coordinates parallel threads of work and reports back | You have a stream of related work rather than one task and want to see which threads finished or need you.                                                  |
| [Remote Control](../02-Claude-Code-CLI/remote-control.md)           | A Claude Code session running on your computer                                    | The work needs your local filesystem, tools, or MCP servers.                                                                                                |
| [Dispatch](desktop.md#sessions-from-dispatch) | The Desktop app on your computer                                                  | You want to message a task and let Dispatch decide how to run it. Requires a Pro or Max plan.                                                               |

If your computer will be off, use cloud sessions or a project, which run in the cloud and continue with your laptop closed. Remote Control and Dispatch drive your own machine, so it needs to stay on with Claude Code or the Desktop app running. If your machine sleeps during a Remote Control session, Claude Code reconnects when the machine comes back online. For a fuller comparison, see [work when you are away from your terminal](../02-Claude-Code-CLI/platforms.md#work-when-you-are-away-from-your-terminal). Cloud sessions and Remote Control run from the **Code** tab. For Dispatch, which you message as a task in the app, see [sessions from Dispatch](desktop.md#sessions-from-dispatch).


[​](#start-and-monitor-cloud-sessions)

Start and monitor cloud sessions

Cloud sessions run tasks on cloud infrastructure, Anthropic-managed by default, so a session continues after you put your phone away. From the Code tab, select a repository and branch, describe the task, and submit it. Sessions persist across devices: a task you start on your laptop is ready to review from your phone, and one you start from your phone is waiting when you’re back at your desk. Open a session in the app to check progress, answer Claude’s questions, or steer it in a new direction. You can also tell Claude to [watch a pull request](../02-Claude-Code-CLI/claude-code-on-the-web.md#auto-fix-pull-requests) and fix CI failures or review comments as they arrive. To connect GitHub and set up your environment, follow the [cloud quickstart](../02-Claude-Code-CLI/web-quickstart.md), and see [Use Claude Code in the cloud](../02-Claude-Code-CLI/claude-code-on-the-web.md) for everything cloud sessions can do.


[​](#continue-a-local-session-with-remote-control)

Continue a local session with Remote Control

Remote Control connects the Claude app to a Claude Code session running on your machine, so code execution and filesystem access stay local while you drive the session from your phone. Start the session on your computer with `claude remote-control`, or run `/remote-control` in a session that’s already open. Then scan the QR code the terminal can display, or open the Claude app, tap **Code**, and pick the session from the list. See [connect from another device](../02-Claude-Code-CLI/remote-control.md#connect-from-another-device) for each option. When you add an attachment in the Claude app, it reaches the local session too:

- **Photos**: Claude sees attached photos directly as part of your message. Claude Code also saves each photo under `~/.claude/uploads/` and tells Claude the saved file path, so Claude can copy the image into files it creates.
- **Other files**: Claude Code downloads them to your machine and passes them to Claude as `@` file references.

For requirements, invocation modes, and troubleshooting, see the [Remote Control overview](../02-Claude-Code-CLI/remote-control.md).


[​](#get-push-notifications)

Get push notifications

When Remote Control is active, Claude can send push notifications to your phone, typically when a long-running task finishes or when it needs a decision from you. You can also ask for one in your prompt, such as `notify me when the tests finish`. See [mobile push notifications](../02-Claude-Code-CLI/remote-control.md#mobile-push-notifications) for the two `/config` toggles and delivery troubleshooting. Dispatch sends its own notification when a Code session it spawned finishes or needs your approval, described in [sessions from Dispatch](desktop.md#sessions-from-dispatch).


[​](#limitations)

Limitations

The mobile client covers most of what a session needs, with a few limitations:

- **Local-only commands**: commands that only run in the terminal interface, such as `/plugin` and `/resume`, don’t work from the app. The [Remote Control limitations](../02-Claude-Code-CLI/remote-control.md#limitations) list the commands that do work from mobile and how their behavior differs.
- **Permission modes**: cloud sessions offer Accept edits, Plan, and Auto in the mode dropdown, and Remote Control sessions offer Manual, Accept edits, and Plan. You can’t select Bypass permissions from the app in either case, and you can’t select Auto for a Remote Control session. See [switch permission modes](../02-Claude-Code-CLI/permission-modes.md#switch-permission-modes).
- **Dispatch plans**: Dispatch requires a Pro or Max plan and isn’t available on Team or Enterprise.


[​](#related-resources)

Related resources

- [Platforms and integrations](../02-Claude-Code-CLI/platforms.md): compare every surface Claude Code runs on
- [Use Claude Code in the cloud](../02-Claude-Code-CLI/claude-code-on-the-web.md): how cloud sessions run and how to move work to and from your terminal
- [Configure cloud environments](../02-Claude-Code-CLI/cloud-environments.md): network access levels, environment variables, and setup scripts for cloud sessions
- [Remote Control](../02-Claude-Code-CLI/remote-control.md): continue a local session from any device
- [Sessions from Dispatch](desktop.md#sessions-from-dispatch): how Dispatch tasks become Code sessions in the Desktop app
- [Channels](../02-Claude-Code-CLI/channels.md): ask Claude something from your phone via Telegram, Discord, or iMessage while the work runs on your machine
- [Claude Code in Slack](../14-Connectors/slack.md): delegate coding tasks from your Slack workspace by mentioning `@Claude`
