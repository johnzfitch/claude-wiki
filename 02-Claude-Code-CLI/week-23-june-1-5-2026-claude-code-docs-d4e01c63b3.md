---
title: "Week 23 · June 1–5, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w23"
category: "02-Claude-Code-CLI"
fetched_at: "2026-08-02T05:38:28Z"
tags: ["claude-code"]
---

# Week 23 · June 1–5, 2026

Copy pageCopy page

Run auto mode on Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry, prompt before writing files that can run code in acceptEdits mode, list installed plugins with /plugin list, and require an approved version range for managed deployments.

Copy pageCopy page

Releases [v2.1.158 → v2.1.165](/docs/en/changelog#2-1-158)4 features · June 1–5

Auto mode on Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundryv2.1.158

Auto mode is now available on Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry for Opus 4.7 and Opus 4.8, replacing permission prompts with background safety checks on third-party providers. Opt in by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`.

Opt in on a third-party provider, then cycle to auto mode with Shift+Tab:

terminal

```python
export CLAUDE_CODE_ENABLE_AUTO_MODE=1
```

[Auto mode on third-party providers](/docs/en/permission-modes#enable-auto-mode-on-bedrock-agent-platform-or-foundry)

Safer automatic editsv2.1.160

Claude Code now prompts before writing files that can run code, even in `acceptEdits` mode. The protected set covers shell startup files such as `.zshenv` and `.bash_login`, git config under `~/.config/git/`, and build-tool configs such as `.npmrc`, `.bazelrc`, and `.pre-commit-config.yaml`. These writes are never auto-approved in any mode except `bypassPermissions`.

Work in acceptEdits mode; Claude now pauses before writing these files:

terminal

```python
claude --permission-mode acceptEdits
```

[Protected paths](/docs/en/permission-modes#protected-paths)

List installed plugins with /plugin listv2.1.163

The new `/plugin list` command prints your installed plugins inline, without opening the `/plugin` menu, and is also available as `claude plugin list` from the shell. In the interactive form, add `--enabled` or `--disabled` to show only plugins in that state.

List the plugins that are currently turned on:

Claude Code

```python
> /plugin list --enabled
```

[Plugin commands](/docs/en/plugins-reference#plugin-list)

Version requirements for managed deploymentsv2.1.163

Two managed settings, `requiredMinimumVersion` and `requiredMaximumVersion`, let your organization require an approved Claude Code version range. A client outside the range exits at startup and tells the user to update through the organization’s method. `claude update`, `claude install`, and `claude doctor` keep working so users can still recover.

Add a floor to your managed settings so older clients refuse to start:

managed-settings.json

```python
{
  "requiredMinimumVersion": "2.1.163"
}
```

[Decide what to enforce](/docs/en/admin-setup#decide-what-to-enforce)

Other wins

The trigger keyword for [dynamic workflows](/docs/en/workflows) changed from `workflow` to `ultracode`; asking for a workflow in your own words still works, and the keyword is highlighted in violet in the prompt

[Stop and SubagentStop hooks](/docs/en/hooks) can return `hookSpecificOutput.additionalContext` to give Claude feedback and keep the turn going instead of being treated as an error

`claude mcp` list, get, and add no longer print secrets: environment-variable references are not expanded, and credential headers and URL secrets are redacted

A failed Bash command in a parallel tool batch no longer cancels the others; each tool returns its own result independently

Editing a file no longer needs a separate Read first when you viewed it with a single-file `grep`, `egrep`, or `fgrep`

Clicking a command in the autocomplete menu now fills it into your prompt instead of running it immediately; press Enter to run

Listing `Grep` or `Glob` in `--tools` now provides the dedicated search tools on native builds with embedded search, instead of silently ignoring those names

`/effort` now confirms when your chosen level will persist as the default for new sessions

`OTEL_RESOURCE_ATTRIBUTES` values are now attached as labels on metric datapoints, so you can slice usage metrics by custom dimensions like team or repo

Windsurf is renamed to Devin Desktop in `/ide`, `/terminal-setup`, and `/scroll-speed`, following the editor’s rebrand

`/btw` gains a `c to copy` shortcut that copies the raw markdown answer to the clipboard

[Full changelog for v2.1.158–v2.1.165 →](/docs/en/changelog#2-1-158)
