---
title: "Week 20 · May 11–15, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w20"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-16T06:24:15Z"
tags: ["claude-code"]
---

# Week 20 · May 11–15, 2026

Copy pageCopy page

Manage every Claude Code session from one screen with agent view, keep Claude working toward a goal until a condition holds, and run fast mode on Opus 4.7 by default.

Copy pageCopy page

Releases [v2.1.139 → v2.1.142](/docs/en/changelog#2-1-139)3 features · May 11–15

Agent viewresearch preview

`claude agents` opens one screen for every Claude Code session: what’s running, what’s blocked on your input, and what’s done. Dispatch a bug fix, a pull request review, and a flaky-test investigation as three rows, keep working in another window, and step in only when a row needs you. Attach to any row to drop into its full conversation, then press `←` to return to the list. Each background session keeps running without a terminal attached.

Open the dashboard from your shell:

terminal

```python
claude agents
```

[Agent view](/docs/en/agent-view)

/goalv2.1.139

Set a completion condition and Claude keeps working toward it across turns without you prompting each step. After every turn, a fast model checks whether the condition holds; if not, Claude starts another turn instead of handing control back. Useful for substantial work with a verifiable end state, like migrating a module until every call site compiles and tests pass. The goal clears once the condition is met, and works in interactive, `-p`, and Remote Control.

Set a goal and let Claude run until it holds:

Claude Code

```python
> /goal all tests in test/auth pass and the lint step is clean
```

[Goals](/docs/en/goal)

Fast mode on Opus 4.7research preview

`/fast` now runs on Opus 4.7 by default instead of Opus 4.6. Fast mode is a high-speed Opus configuration: the same model quality at about 2.5x the speed for a higher per-token cost, useful for rapid iteration and live debugging. Pricing is unchanged at \$30/\$150 per MTok, the same as Opus 4.6 fast mode. To pin fast mode to Opus 4.6, set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`.

Toggle fast mode, now running on Opus 4.7:

Claude Code

```python
> /fast
```

[Fast mode on Opus 4.7](/docs/en/fast-mode#understand-the-cost-tradeoff)

Other wins

`claude agents` gained dispatch flags (`—add-dir`, `—settings`, `—mcp-config`, `—plugin-dir`, `—permission-mode`, `—model`, `—effort`, `—dangerously-skip-permissions`) to configure background sessions, and `claude agents —cwd <path>` scopes the session list to a directory

New hook `args: string[]` exec form spawns the command directly without a shell, so path placeholders never need quoting

New `continueOnBlock` config option for `PostToolUse` hooks feeds the hook’s rejection reason back to Claude and continues the turn instead of ending it

New `terminalSequence` field in hook JSON output lets hooks emit desktop notifications, window titles, and bells without a controlling terminal

The Rewind menu added “Summarize up to here” to compress earlier context while keeping recent turns intact

Remote Control, `/schedule`, claude.ai MCP connectors, and notification preferences are now disabled when `ANTHROPIC_API_KEY`, `apiKeyHelper`, or `ANTHROPIC_AUTH_TOKEN` is set, even alongside a claude.ai login; unset the API key to use these features

MCP stdio servers now receive `CLAUDE_PROJECT_DIR` in their environment, matching hooks, and plugin configs can reference `$CLAUDE_PROJECT_DIR` in commands

`claude plugin details <name>` shows a plugin’s component inventory and projected per-session token cost, and the `/plugin` details pane now also lists the LSP servers a plugin provides

Plugins with a root-level `SKILL.md` and no `skills/` subdirectory are now surfaced as a skill

`/feedback` can now include recent sessions from the last 24 hours or 7 days for issues spanning more than the current session

Agent tool `subagent_type` now matches case- and separator-insensitively, so `“Code Reviewer”` resolves to `code-reviewer`

[Full changelog for v2.1.139–v2.1.142 →](/docs/en/changelog#2-1-139)
