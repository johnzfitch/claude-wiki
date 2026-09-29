---
title: "Week 36 · August 31 – September 4, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w36"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-15T06:28:16Z"
tags: ["claude-code"]
---

# Week 36 · August 31 – September 4, 2026

Copy pageCopy page

Switch to Claude Fable 5.1, let computer use run in the background on Desktop, and watch Claude’s edits in a live /diff panel.

Copy pageCopy page

Releases [v2.1.251 → v2.1.261](/docs/en/changelog#2-1-251)4 features · August 31 – September 4

Claude Fable 5.1new model

Claude Fable 5.1 is available in Claude Code with a 1M-token context window, and the `fable` alias now selects it. In Claude apps gateway sessions, `fable` still selects Fable 5. If your gateway serves Fable 5.1, run `/model claude-fable-5-1`. Requires v2.1.257 or later.

Switch the current session to Fable 5.1 and save it as your default:

Claude Code

```python
> /model fable
```

On the Anthropic API, the picker lists Fable only once the server reports it available for your organization, but typing `/model fable` checks with the server directly.

[Work with Fable](/docs/en/model-config#work-with-fable)

Computer use runs in the background on DesktopDesktop

On macOS, computer use in the Claude Code Desktop app now works in the background: Claude sees and acts in the apps you’ve approved while you keep working. Background computer use is in beta on Pro and Max plans.

[Let Claude use your computer](/docs/en/desktop#let-claude-use-your-computer)

Live diff panel in fullscreen renderingv2.1.260

In fullscreen rendering, `/diff` now opens a panel beside the conversation instead of a viewer you have to close. The panel lists the changed files with their added and removed line counts and refreshes each time Claude edits a file or runs a shell command. Select lines in the panel with the mouse to attach them to your next prompt.

With fullscreen rendering on, inside a git repository, and in a terminal at least 110 columns wide, toggle the panel:

Claude Code

```python
> /diff
```

Run `/diff` again or click the `✕` in its header to close it.

[Diff panel](/docs/en/interactive-mode#diff-panel)

Find unused skills with /skill-doctorCLI

`/skill-doctor` shows what each of your skills costs in context and how often it gets used, so you can decide which ones to turn off. Every skill in the [skill listing](/docs/en/skills#skill-descriptions-are-cut-short) adds to your context on every turn, whether or not Claude ever uses it. Requires v2.1.252 or later and isn’t available in sessions that skip [feature-flag fetching](/docs/en/env-vars#features-that-need-feature-flag-fetching).

Run it in an interactive session to open the report in the `/plugin` manager’s **Stats** tab:

Claude Code

```python
> /skill-doctor
```

In non-interactive mode with `-p`, Claude Code prints the report as text instead.

[Find unused skills](/docs/en/skills#find-unused-skills)

Other wins

A [`PreModelSwitch`](/docs/en/hooks#premodelswitch) hook can block a model switch you request, and a [`PostModelSwitch`](/docs/en/hooks#postmodelswitch) hook can add context for Claude after the session’s model changes

[`/cost`](/docs/en/costs#prompt-cache-statistics) adds a `Prompt cache (main)` line: the share of input tokens served from cache, the cache misses, whether the cache is warm, and a likely cause for the last miss when Claude Code can name one. Status line scripts get a matching `prompt_cache` object

Organizations can list HTTP and SSE MCP servers under the [`managedMcpServers`](/docs/en/managed-mcp#provide-servers-through-managed-settings) managed setting to give them to every user, in addition to the servers that users add on their own

`/effort` and the `/model` picker now [save a separate effort level for each model](/docs/en/model-config#adjust-effort-level); press `s` instead of `Enter` to apply a level to the current session only

By default, the auto mode classifier [now also blocks](/docs/en/permission-modes#what-the-classifier-blocks-by-default) actions such as requesting credentials from the cloud instance-metadata endpoint or connecting to sibling containers that Claude didn’t start

In auto mode, Claude Code asks you before Claude [first reads a file outside your working directories](/docs/en/permission-modes#first-read-outside-the-working-directories), with an option to block such reads from then on

Raise [`bashOutputMaxChars`](/docs/en/settings-reference#bashoutputmaxchars) and [`taskOutputMaxChars`](/docs/en/settings-reference#taskoutputmaxchars), up to 128,000 characters, so Claude receives more of the output from a successful command or background task inline

The prompt’s [word-editing shortcuts follow readline](/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace) for everyone, and the `keybindingFlavor` setting no longer has any effect. `Ctrl+W` deletes back to the previous whitespace, and `Alt+B`, `Alt+F`, and `Alt+D` treat punctuation such as `/` and `.` as word breaks

If you set `defaultMode` to `“bypassPermissions”` in a project’s `.claude/settings.json` or `.claude/settings.local.json`, it [no longer takes effect](/docs/en/permission-modes#which-mode-a-session-starts-in) and the session starts in Manual mode; set `“bypassPermissions”` in user or managed settings instead, or pass `--permission-mode`

Seat-based Enterprise plans now [default to Opus 5](/docs/en/model-config#default-model-setting)

In the VS Code extension, click the model name at the bottom of the prompt box to [open the model picker](/docs/en/vs-code#use-the-prompt-box)

In the VS Code extension, select **Output styles** in the command menu’s Customize section to [pick an output style](/docs/en/vs-code#use-the-prompt-box), including your custom ones

[Full changelog for v2.1.251–v2.1.261 →](/docs/en/changelog#2-1-251)
