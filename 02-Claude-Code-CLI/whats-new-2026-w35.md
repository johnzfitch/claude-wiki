---
title: "Week 35 · August 24–28, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w35"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-15T06:28:45Z"
tags: ["claude-code"]
---

# Week 35 · August 24–28, 2026

Copy pageCopy page

Resume terminal sessions in the Claude Code Desktop app, review feedback reports that Claude drafts for you, and start a session in restricted mode.

Copy pageCopy page

Releases [v2.1.240 → v2.1.250](changelog.md#2-1-240)3 features · August 24–28

Resume terminal sessions in the Desktop appDesktop

Type `/resume` in the Claude Code Desktop prompt box to pick up any session you started from the CLI and continue it in the app with the full conversation and context intact. Search your sessions by title, folder, or branch, and preview where you left off before you resume.

In a Desktop session, run the command to list your terminal sessions:

Claude Code

```python
> /resume
```

Select a session and press `Enter`. The conversation opens in the app where you left off.

[Move between the CLI and Desktop](../16-Mobile-Desktop/desktop.md#coming-from-the-cli)

Claude-drafted feedbackCLI

When a tool keeps failing, Claude can’t help with a request, or you point out a mistake, Claude now drafts a feedback report for you with the `SendFeedback` tool. A card above your prompt shows the draft, and you can review, send, or dismiss it from there. Nothing reaches Anthropic until you send it. Requires v2.1.238 or later.

Run `/feedback` with no argument to open your queue of drafts from every session:

Claude Code

```python
> /feedback
```

Select a draft, then edit, send, or discard it. To turn drafting off, set **Claude-drafted feedback** to `off` in `/config`.

[SendFeedback tool behavior](tools-reference.md#sendfeedback-tool-behavior)

Restricted modev2.1.248

Restricted mode starts Claude Code without the built-in tools that run commands or code. Use it when an evaluation harness drives `claude` on a shared machine. Start it with `--restricted` or set `CLAUDE_CODE_RESTRICTED=1`. Claude Code also removes `WebFetch`, confines the file tools to the working directories, loads only managed settings and `--settings`, and refuses the `bypassPermissions` permission mode.

Run a non-interactive query without the command-running tools:

terminal

```python
claude --restricted -p "review src/ for SQL injection risks"
```

To give Claude one of the removed tools back, list it in `--tools` together with the other built-in tools you want, for example `--tools "Bash,Read,Edit"`. `--tools` is an allowlist, and its `default` preset doesn’t restore the removed tools.

[CLI flags](cli-reference.md#cli-flags)

Other wins

Set the new [`modelPicker`](settings-reference.md#modelpicker) setting to extend or replace the `/model` picker’s built-in list with your own ordered, labeled entries, including Amazon Bedrock or Google Cloud’s Agent Platform model IDs

Set [`promptCacheTtl`](prompt-caching.md#choose-the-ttl-yourself) to `1h` to keep a one-hour prompt cache on the main conversation when you use an API key or a cloud provider; `subagentPromptCacheTtl` sets the TTL for subagents and all other requests outside the main conversation

On Pro, Max, Team, and Enterprise plans, [`/usage`](../17-Billing-Plans/costs.md#plan-usage-breakdown) adds a Loops breakdown: run count, total tokens, tokens per run, and last run for the `/loop` and scheduled tasks that used the most tokens

Organizations on contracted rates can set the [`modelPricing`](../17-Billing-Plans/costs.md#report-spend-at-your-contracted-rates) managed setting so `/usage`, the status line, and OpenTelemetry report cost at those rates instead of list price

`/login` offers **Sign in with your Console account** under the **Anthropic Console account** option, so members of Console organizations that don’t allow API keys can sign in without creating one

Run `/permissions` and open the new [**Auto mode** tab](auto-mode-config.md#edit-rules-from-permissions) to view and edit auto mode classifier rules without opening a settings file

When auto mode is available, Bash permission prompts in the Manual and `acceptEdits` permission modes offer a [**Yes, and switch to auto mode**](permission-modes.md#switch-permission-modes) option; select it to approve the command and switch the session to auto mode

After you [move a session with `/cd`](permissions.md#move-the-session-to-another-directory), the new directory’s project settings, hooks, `.mcp.json` servers, skills, and subagents take effect immediately instead of on the next `--resume`

In non-interactive sessions, including `-p` runs, Agent SDK runs, and cloud sessions, Claude Code [continues a response](errors.md#the-response-above-may-be-incomplete) that a server error, dropped connection, or stall cut off mid-stream, when the partial response contains text and no tool calls

A subagent that stops at its `maxTurns` limit returns its output marked as partial, with a hint that Claude can [continue it with `SendMessage`](../09-Agents-Patterns/sub-agents.md#resume-subagents), instead of appearing finished

On Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry, sessions on the same machine can now [message each other](cross-session-messaging.md#availability), `/loop` can [choose its own interval](scheduled-tasks.md#let-claude-choose-the-interval), and `/model` and `/effort` apply immediately instead of after the turn ends

The native installer and auto-updater download a zstd-compressed build, about 75 MB instead of 340 MB on Linux x64, and native builds load code on demand, using roughly 40 to 70 MB less memory per session

[Full changelog for v2.1.240–v2.1.250 →](changelog.md#2-1-240)
