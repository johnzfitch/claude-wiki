---
title: "Week 29 · July 13–17, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w29"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:45Z"
tags: ["claude-code"]
---

# Week 29 · July 13–17, 2026

Copy pageCopy page

Pull live data into published artifacts through MCP connectors, and use Claude Code with a screen reader in the new screen reader mode.

Copy pageCopy page

Releases [v2.1.207 → v2.1.212](changelog.md#2-1-207)2 features · July 13–17

Artifacts call your MCP connectorsweb

A published artifact can now call MCP connectors each time someone views it, so a dashboard shows live data and can take actions on demand rather than a snapshot from the session that built it. Each call runs through the viewing account’s own connections, and viewers approve access before the page’s first connector call. This week also adds public sharing links, editor roles for shared editing on Team and Enterprise plans, and artifacts created from Claude Tag sessions.

Name the connector and the data you want in your prompt:

Claude Code

```python
Build a dashboard artifact of open pull requests that pulls the live list through my GitHub connector when the page loads.
```

[Pull live data with MCP connectors](artifacts.md#pull-live-data-with-mcp-connectors)

Screen reader modeCLI

Screen reader mode replaces the visual terminal interface with plain, linear text: instead of boxes, spinners, and in-place redraws, Claude Code prints labeled lines that a screen reader such as VoiceOver or NVDA reads in order, so you can approve permissions and review output end to end. Turn it on per session with a flag, per shell with the `CLAUDE_AX_SCREEN_READER` environment variable, or everywhere with the `axScreenReader` setting.

Start a session in screen reader mode:

terminal

```python
claude --ax-screen-reader
```

[Turn on screen reader mode](accessibility.md#turn-on-screen-reader-mode)

Other wins

`/fork` now copies your conversation into a new background session with its own row in `claude agents` while you keep working; the in-session forked subagent it used to launch is now `/subtask`

[Auto mode](permission-modes.md#enable-auto-mode-on-bedrock-agent-platform-or-foundry) no longer needs the `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry; administrators can turn it off with `disableAutoMode`

MCP tool calls that run longer than two minutes now move to the background automatically so the session stays usable; tune or disable the threshold with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`

New `claude auto-mode reset` restores the default auto-mode configuration, and `--yes` skips the confirmation prompt

New [corporate launcher](../13-Enterprise-Admin/corporate-launcher.md) support: `CLAUDE_CODE_PROCESS_WRAPPER` or the `processWrapper` setting runs the processes Claude Code starts from its own binary, such as the background service and agent view sessions, through a required wrapper executable

`vimInsertModeRemaps` setting maps two-key insert-mode sequences such as `jj` to Escape in vim mode

`--forward-subagent-text` and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` include subagent text and thinking blocks in [stream-json output](headless.md)

Session-wide caps stop runaway loops: WebSearch calls and subagent spawns each default to 200, tunable with `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` and `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`

”Always allow” permission rules save at the repository root, so approvals granted in a git worktree persist across sessions and worktrees

Amazon Bedrock, Google Cloud’s Agent Platform, and Claude Platform on AWS now default to Claude Opus 4.8

The collapsed tool summary line shows a live elapsed-time counter, so long-running tool calls visibly tick instead of looking stuck

[Full changelog for v2.1.207–v2.1.212 →](changelog.md#2-1-207)
