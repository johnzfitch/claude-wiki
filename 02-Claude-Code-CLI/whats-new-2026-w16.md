---
title: "Week 16 · April 13–17, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w16"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-30T06:31:00Z"
tags: ["claude-code"]
---

# Week 16 · April 13–17, 2026

Copy pageCopy page

Claude Opus 4.7 with the new xhigh effort level, Routines on Claude Code on the web, mobile push notifications that ping your phone when Claude needs you, a /usage breakdown that shows what’s driving your limits, and native binaries replacing the bundled JavaScript.

Copy pageCopy page

Releases [v2.1.105 → v2.1.113](changelog.md#2-1-105)5 features · April 13–17

Claude Opus 4.7new model

Anthropic’s strongest coding model yet is now the default on Max and Team Premium, and available everywhere else from `/model`. It adds a new `xhigh` effort level that sits between `high` and `max`: best results for most coding and agentic tasks, applied as the default the first time you switch to 4.7. `/effort` now opens an interactive arrow-key slider when you call it without arguments, so you can dial intelligence against speed without remembering the level names.

Switch model and effort in one go:

Claude Code

```python
> /model opus
> /effort xhigh
```

[Model config: effort levels](model-config.md#adjust-effort-level)

Routinesweb

Templated cloud agents that fire on a schedule, a GitHub event, or an API call. Define a routine once on Claude Code on the web with a prompt, the repos it can touch, and the connectors it needs, then let PR-opened, release-published, or your own webhook trigger it without your machine running. The trigger picker now covers GitHub events with optional filters and gives every routine a tokened `/fire` endpoint for external systems.

Create one from the web UI, or scaffold from your terminal:

Claude Code

```python
> /schedule daily PR review at 9am
```

[Routines guide](web-scheduled-tasks.md)

/usage breakdownCLI

More visibility into where your Claude Code usage goes. `/usage` now shows what’s driving your limits: parallel sessions, subagents, cache misses, and long context, each with a percentage of your last 24 hours and a tip to optimize it. Press `d` or `w` to switch between day and week views.

Run it any time:

Claude Code

```python
> /usage
```

[Commands reference](commands.md)

Mobile push notificationsmobile

With [Remote Control](remote-control.md) connected, Claude can send a push notification to your phone when a long task finishes or it needs a decision to keep going. Turn it on with “Push when Claude decides” in `/config`, or ask for one in your prompt. Useful when you kick off a long agent run and want to step away from the terminal.

Ask Claude to ping you when it’s done:

Claude Code

```python
> notify me when the tests pass
```

[Remote Control: mobile push notifications](remote-control.md#mobile-push-notifications)

Native binariesv2.1.113

The `claude` CLI now spawns a native per-platform binary instead of bundled JavaScript, so the installed `claude` command no longer invokes Node. The npm package pulls the right binary in through an optional dependency such as `@anthropic-ai/claude-code-darwin-arm64`, so your install command doesn’t change. The standalone installer already shipped this binary; npm now matches it.

Upgrade and check what you’re running:

```python
claude update
claude --version
```

[Setup guide](../01-Getting-Started/setup.md)

Other wins

New [`/ultrareview`](ultrareview.md): comprehensive code review in the cloud using parallel multi-agent analysis and an adversarial critique pass. Run it bare to review your current branch, or `/ultrareview <PR#>` for a specific PR

[Auto mode](permission-modes.md#eliminate-prompts-with-auto-mode) is now available for Max subscribers on Opus 4.7, and the `--enable-auto-mode` flag is no longer required

[Session recap](interactive-mode.md#session-recap) shows a one-line summary of what happened while you were away; run `/recap` on demand or turn it off from `/config`

New `/tui` command and `tui` setting switch between classic and flicker-free rendering mid-conversation; focus view moved from `Ctrl+O` to its own `/focus` command

Plugins can ship background watchers via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke

”Auto (match terminal)” option in `/theme` follows your terminal’s dark/light mode

`/fewer-permission-prompts` scans your transcripts for common read-only Bash and MCP calls and proposes an allowlist for `.claude/settings.json`

Claude can now discover and run built-in commands like `/init`, `/review`, and `/security-review` via the Skill tool

`PreCompact` hooks can block compaction by exiting with code 2 or returning `“decision”:“block”`

`ENABLE_PROMPT_CACHING_1H` opts API key, Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry users into 1-hour prompt cache TTL

`sandbox.network.deniedDomains` setting carves specific domains out of a broader `allowedDomains` wildcard

`/undo` is now an alias for `/rewind`, and `/proactive` is an alias for `/loop`

Hardened Bash permissions: deny rules now match through `env`/`sudo`/`watch` wrappers, and `Bash(find:*)` allow rules no longer auto-approve `-exec` or `-delete`

[Full changelog for v2.1.105–v2.1.113 →](changelog.md#2-1-105)
