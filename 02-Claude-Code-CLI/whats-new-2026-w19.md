---
title: "Week 19 · May 4–8, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w19"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-30T06:32:01Z"
tags: ["claude-code"]
---

# Week 19 · May 4–8, 2026

Copy pageCopy page

Load plugins from .zip archives and URLs, search command history across every project with Ctrl+R, branch new worktrees from local HEAD or the remote default, and block actions unconditionally with auto mode hard deny rules.

Copy pageCopy page

Releases [v2.1.128 → v2.1.136](changelog.md#2-1-128)2 features · May 4–8

Plugins from .zip archives and URLs

`--plugin-dir` now accepts a `.zip` plugin archive in addition to a directory, and the new `--plugin-url` flag fetches a plugin archive from a URL for the current session. Useful for trying a plugin before adding it to a marketplace, or for shipping internal plugins from an artifact store.

Load a plugin straight from a URL:

terminal

```python
claude --plugin-url https://example.com/my-plugin.zip
```

[Plugins guide](../08-Plugins-Skills/plugins.md)

History search across all your projectsv2.1.129

`Ctrl+R` reverse-search now defaults to all prompts across every project, restoring the behavior from before v2.1.124. Press `Ctrl+S` while searching to narrow back to the current project or session. Handy when you remember a command you ran in another repo last week and don’t want to go digging for it.

[Interactive mode: command history](interactive-mode.md#command-history)

Other wins

New `worktree.baseRef` setting (`fresh` \| `head`) controls whether `--worktree`, the `EnterWorktree` tool, and agent-isolation worktrees branch from the remote default branch or local `HEAD`; the default `fresh` keeps unpushed commits out of new worktrees

New `settings.autoMode.hard_deny` rules block matching actions unconditionally in auto mode, regardless of allow exceptions, for actions that should never run automatically even when broader allow rules apply

Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read `$CLAUDE_EFFORT`

`CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` opts out of the fullscreen alternate-screen renderer and keeps the conversation in the terminal’s native scrollback

`CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` lets Homebrew or WinGet installations run the upgrade in the background and prompt to restart

`CLAUDE_CODE_SESSION_ID` is now in the Bash tool subprocess environment, matching the `session_id` passed to hooks

`/mcp` now shows the tool count for connected servers and flags servers that connected with 0 tools

`--channels` now works with console (API key) authentication

Subprocesses such as Bash, hooks, MCP, and LSP no longer inherit `OTEL_*` environment variables, so OTEL-instrumented apps run via the Bash tool no longer pick up the CLI’s own OTLP endpoint

Sub-agent progress summaries now hit the prompt cache, cutting `cache_creation` token cost by roughly 3x

Several OAuth and credential reliability fixes: parallel sessions no longer dead-end at 401 after a refresh-token race, MCP OAuth refresh tokens are no longer lost when multiple servers refresh concurrently, and a rare login loop from a concurrent credential write is fixed

New `parentSettingsBehavior` admin key lets admins opt SDK `managedSettings` into the policy merge

[Full changelog for v2.1.128–v2.1.136 →](changelog.md#2-1-128)
