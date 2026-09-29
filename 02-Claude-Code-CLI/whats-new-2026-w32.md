---
title: "Week 32 · August 3–7, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w32"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-25T06:29:48Z"
tags: ["claude-code"]
---

# Week 32 · August 3–7, 2026

Copy pageCopy page

Claude Code sessions message each other, self-hosted environments run cloud sessions on your infrastructure, and auto mode becomes the default permission mode.

Copy pageCopy page

Releases [v2.1.220 → v2.1.224](changelog.md#2-1-220)3 features · August 3–7

Cross-session messagingv2.1.224

Your Claude Code sessions can now message each other. Claude discovers your other sessions with the `ListAgents` tool and sends with `SendMessage`, either when you ask it to or on its own, such as after a change in one session affects what another is working on. A message is text Claude writes for the other session, never your conversation history or files. Available on macOS and Linux. Requires v2.1.224 or later.

With two sessions open on the same machine, ask one of them to pass something along:

Claude Code

```python
Tell the session working on the payments API that users.name is now users.display_name
```

The other session shows a `Message from` row once Claude has read the message; press `Ctrl+O` to expand it. To see which sessions Claude can reach, run `/list-agents`.

[Message another session](cross-session-messaging.md#message-another-session)

Self-hosted environmentsv2.1.224

Self-hosted environments run Claude Code cloud sessions on your organization’s own infrastructure, in public beta on Team and Enterprise plans. Run `claude self-hosted-runner` on your machines or containers to turn them into runners. When someone picks your environment while starting a session from claude.ai, the mobile or desktop apps, or `claude --cloud`, that session runs inside your network, with access to your internal services. An Owner turns on **Allow self-hosted environments** in [admin settings](https://claude.ai/admin-settings/cloud-environments) first.

Signed in as an Owner, run the guided setup, which walks you through creating the environment and starts a runner:

terminal

```python
claude self-hosted-runner setup
```

The environment shows **Healthy** in admin settings once the runner registers.

[Self-hosted environments quickstart](../13-Enterprise-Admin/self-hosted-environments-quickstart.md#set-up-an-environment-and-runner)

Auto mode becomes the defaultCLI

Starting August 14, auto mode is the default permission mode for new sessions on Pro, Max, and Team plans. If you set a default mode yourself, it stays in place unless you accept the one-time switch prompt, and a default your organization manages doesn’t change. You can still switch modes at any time. Already in effect on those plans: the classifier calls auto mode makes no longer count toward your usage limits.

To start every session in auto mode before the switch, set it as your default in your user settings:

~/.claude/settings.json

```python
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

New sessions then show `auto mode on` in the status bar.

[Auto mode requirements and controls](permission-modes.md#eliminate-prompts-with-auto-mode)

Other wins

The VS Code extension gets [Focus view](../03-IDE-Integrations/vs-code.md#extension-settings), which hides tool activity behind one expandable row per turn; toggle it from the command menu or with `Ctrl+Alt+F` (`Ctrl+Option+F` on Mac)

Sandbox credential files accept [`mode: “mask”`](sandboxing.md#mask-credential-files) on Linux and WSL2, so sandboxed commands read a sentinel copy while the sandbox proxy substitutes the real value on egress; credential masking also gains `extract`, JWT-aware `decode`, and AWS SigV4 re-signing options

Marketplaces can distribute a plugin as a [zip archive](../08-Plugins-Skills/plugins-marketplace-reference.md#archive-plugin-source) with the new `archive` source, downloaded over HTTPS with an optional SHA-256 pin, so installs work without git or npm

`/review` is now an alias of [`/code-review`](code-review.md#review-a-diff-locally), and `/code-review` with no effort level reuses the level you typed last

A session you copy with [`/fork`](../09-Agents-Patterns/agent-view.md#copy-the-session-with-%2Ffork) now makes its code changes in a worktree of its own instead of the original session’s checkout

Plugins you install from [`/plugin`](../08-Plugins-Skills/discover-plugins.md#install-a-plugin) activate in the current session when it’s safe to do so; the install summary reports `Plugin is now active.` or tells you to run `/reload-plugins`

[Background sessions](../09-Agents-Patterns/agent-view.md#how-file-edits-are-isolated) that changed code in a worktree now commit and push before finishing, open a draft pull request only when the task calls for one, and follow the git instructions in your `CLAUDE.md`

The 200-subagent-per-session cap is removed, so long-running sessions no longer refuse new subagents; the [concurrency](../09-Agents-Patterns/sub-agents.md#concurrent-subagent-limit) and depth limits still apply

A repository’s checked-in settings can no longer turn on [Remote Control auto-connect](remote-control.md#enable-remote-control-for-all-sessions); set `remoteControlAtStartup` in your user or managed settings instead, and project and local settings can only turn it off

[Worktree isolation](worktrees.md#how-claude-code-enforces-isolation) now blocks not only file edits but also Bash commands and git redirects that reach the main checkout, in every session type and in the session’s subagents

A Bash command can no longer hide part of itself from permission checks, and tab or invisible-Unicode padding no longer hides part of a command from the approval dialog

PreToolUse auto-allow hooks no longer bypass tool restrictions in Claude Code’s internal side tasks such as summaries and compaction

The [Ultraplan](ultraplan.md) research preview is removed, including the `/ultraplan` command and the `ultraplan` keyword; use plan mode or Claude Code on the web instead

[Full changelog for v2.1.220–v2.1.224 →](changelog.md#2-1-220)
