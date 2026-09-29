---
title: "Week 33 · August 10–14, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w33"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-25T06:29:14Z"
tags: ["claude-code"]
---

# Week 33 · August 10–14, 2026

Copy pageCopy page

Claude Code Desktop auto-continues after a usage limit resets, fork mode turns on by default, and GitLab merge requests and marketplaces join GitHub.

Copy pageCopy page

Releases [v2.1.225 → v2.1.233](/docs/en/changelog#2-1-225)3 features · August 10–14

Auto-continue after a usage limit on DesktopDesktop

When you hit your session limit in the Code tab of Claude Code Desktop, the limit card now offers an **Auto-continue when limits reset** checkbox. Check it, and the Desktop app retries the interrupted turn after the reset. The card shows the retry time. The weekly-limit card doesn’t offer it.

The next time a session-limit card appears, check **Auto-continue when limits reset** and leave the session open. The card shows `Auto-resuming at` followed by the reset time, and the turn picks up on its own once the limit resets.

[What to do when you hit a usage limit](/docs/en/errors#youve-hit-your-session-limit)

Fork mode on by defaultv2.1.232

Fork mode is now on by default in interactive sessions. Claude can request the `fork` subagent type, which inherits the full conversation and prompt cache instead of starting fresh, so you don’t have to re-explain the context for a side task. Subagents Claude spawns in interactive sessions, apart from the ones an agent-team teammate spawns, also run in the background by default.

Start a fork yourself with a task that needs everything you’ve discussed so far:

Claude Code

```python
> /subtask draft unit tests for the parser changes so far
```

The fork appears in the panel below your prompt and its result arrives in your conversation when it finishes. To turn fork mode off, set `CLAUDE_CODE_FORK_SUBAGENT=0`.

[Turn fork mode on or off](/docs/en/sub-agents#turn-fork-mode-on-or-off)

GitLab merge requests and marketplacesv2.1.232

Plugin marketplaces clone bare `gitlab.com` URLs, including nested subgroups. On v2.1.233 or later, pass a GitLab merge request URL to `—worktree` to branch from it, and the `claude agents` view labels sessions linked to a merge request as `!N`. Claude Code also redacts GitLab token families such as `glpat-` and `glrt-`, and protects the `glab` CLI’s config store the same way it protects `gh`.

Start a session in a worktree branched from a merge request:

terminal

```python
claude --worktree https://gitlab.com/group/project/-/merge_requests/42
```

When `origin` is on gitlab.com, Claude Code fetches `merge-requests/42/head` and opens the session on that branch in its own worktree.

[Branch a worktree from a pull or merge request](/docs/en/worktrees#branch-from-a-pull-request)

Other wins

Type `@` in the prompt to [mention another Claude session](/docs/en/cross-session-messaging#message-another-session) by name, and Claude messages it directly with `SendMessage`; a bare name that matches exactly one live session now delivers without a confirmation step

Interactive sessions on one machine keep [unique names](/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach): if you start or rename a session with a name another live session already uses, Claude Code gives yours a `name-word-word` variant and tells you

Plugin marketplaces accept [`command` sources](/docs/en/plugins/marketplace-reference#command-plugin-source): a local command prints the plugin directory, which Claude Code re-resolves each session and applies without a restart

On Linux and WSL, set [`CLAUDE_CODE_TOOL_MEMORY_LIMIT`](/docs/en/tools-reference#memory-limit-on-linux-and-wsl) to a size such as `4G` to cap the memory Bash and PowerShell tool commands can use

The task-tracking tools, such as `TaskCreate`, `TaskUpdate`, and `TodoWrite`, are [no longer available on Opus 4.8, Sonnet 5, Fable 5, Mythos 5, and later models in those families](/docs/en/tools-reference#task-tool-availability); set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` to re-enable them

[`/code-review`](/docs/en/code-review#review-a-diff-locally) at high, xhigh, and max effort now runs in a background agent like the other levels

[`/plugin install plugin@marketplace`](/docs/en/plugins/install#install-a-plugin) refreshes the marketplace first, so newly published plugins install without a manual marketplace update

Settings accept [`additionalMarketplaces` and `allowedMarketplaces`](/docs/en/settings-reference#marketplace-key-aliases) as aliases for `extraKnownMarketplaces` and `strictKnownMarketplaces`

On newer models, Claude can [overwrite an existing file with the Write tool](/docs/en/tools-reference#write-tool-behavior) without reading it first this session, matching the Edit tool’s rules; older models require the read

The VS Code extension can [organize the sessions list into groups](/docs/en/vs-code#organize-sessions-into-groups): right-click to create, rename, or delete a group, and Cmd/Ctrl- or Shift-click to move several sessions at once

If your organization routes Claude Code through a [Claude apps gateway with spend limits](/docs/en/claude-apps-gateway-spend-limits), Claude Code shows the limit period, its reset time, and the operator’s message when you reach the limit

[Full changelog for v2.1.225–v2.1.233 →](/docs/en/changelog#2-1-225)
