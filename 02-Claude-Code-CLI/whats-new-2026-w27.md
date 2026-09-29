---
title: "Week 27 · June 29 – July 3, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w27"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:57Z"
tags: ["claude-code"]
---

# Week 27 · June 29 – July 3, 2026

Copy pageCopy page

Claude Sonnet 5 becomes the default model, Claude in Chrome reaches general availability, subagents run in the background by default, Claude Desktop arrives on Linux in beta, and /radio tunes into Claude FM.

Copy pageCopy page

Releases [v2.1.195 → v2.1.201](changelog.md#2-1-195)5 features · June 29 – July 3

Claude Sonnet 5new model

Sonnet 5 is the new default model for Pro, Team Standard, and Enterprise subscription seats: top-tier coding and tool use at Sonnet pricing, with a native 1M-token context window and adaptive thinking on by default. API pricing is promotional at \$2/\$10 per MTok through August 31. Requires v2.1.197 or later.

Switch to Sonnet 5 by name, or pick it from the model picker:

Claude Code

```python
> /model claude-sonnet-5
```

[Model configuration](model-config.md#available-models)

Claude in Chrome is generally availablev2.1.198

The Chrome integration is out of preview for everyone on a direct Anthropic plan. Claude Code drives your browser through the Claude in Chrome extension: it opens tabs, clicks through pages, fills forms, reads console logs, and shares your login state, so it can test the app it builds without you switching contexts.

[Use Claude Code with Chrome](../03-IDE-Integrations/chrome.md)

Subagents run in the background by defaultv2.1.198

Claude now keeps working while subagents run and picks up their results when they finish, instead of pausing the conversation to wait. Claude still runs a subagent in the foreground when it needs the result before continuing, and background subagents surface every permission prompt in your main session. Pin a subagent’s behavior with the `background` frontmatter field.

[Run subagents in foreground or background](../09-Agents-Patterns/sub-agents.md#run-subagents-in-foreground-or-background)

Claude Desktop on LinuxDesktop

The Claude desktop app is now available on Ubuntu 22.04+ and Debian 12+ in beta, on x86_64 and arm64. You get the same Chat, Cowork, and Claude Code experience as macOS and Windows: parallel sessions, visual diff review, an integrated terminal and editor, and live app preview. Installs from Anthropic’s apt repository, so updates arrive through regular package updates.

[Claude Desktop on Linux](../16-Mobile-Desktop/desktop-linux.md)

/radioCLI

Claude FM is on the air. `/radio` opens the lo-fi radio stream in your browser for something to code to, and prints the stream URL when no browser is available. Not available on Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry.

Tune in from any session:

Claude Code

```python
> /radio
```

[All commands](commands.md#all-commands)

Other wins

[Artifacts](artifacts.md) are now generally available and included on Pro and Max plans, joining Team and Enterprise

Admins can set an [organization default model](model-config.md#organization-default-model) in the org console; it shows as “Org default” in `/model` when you haven’t picked a model yourself

Stacked skill invocations like `/skill-a /skill-b do XYZ` now load all leading skills (up to 5), not only the first

`AskUserQuestion` dialogs no longer auto-continue by default; opt into an idle timeout via `/config`

The “default” permission mode is now named “Manual” across the CLI, `--help`, VS Code, and JetBrains; `--permission-mode manual` is accepted alongside `default`

New `/dataviz` skill gives chart and dashboard design guidance, with a runnable color-palette validator

The built-in Explore agent now inherits the main session’s model (capped at Opus) instead of running on Haiku

Background agents launched from `claude agents` now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask

Hook matchers with hyphenated identifiers like `code-reviewer` now exact-match instead of substring-matching; use `mcp__brave-search__.*` to match all tools from a hyphenated MCP server

Transient server rate-limit errors unrelated to your usage limit are now retried automatically with backoff for subscribers instead of failing the turn

The streaming idle watchdog is now on by default for all providers: it aborts and retries when a response stream produces no events for 5 minutes (`CLAUDE_ENABLE_STREAM_WATCHDOG=0` to disable)

[Full changelog for v2.1.195–v2.1.201 →](changelog.md#2-1-195)
