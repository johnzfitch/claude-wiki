---
title: "Week 34 · August 17–21, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w34"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:46Z"
tags: ["claude-code"]
---

# Week 34 · August 17–21, 2026

Copy pageCopy page

Draft editable UI artboards with the /design skill, set the Concise output style, and start a Claude Code session on your machine from your phone.

Copy pageCopy page

Releases [v2.1.234 → v2.1.239](/docs/en/changelog#2-1-234)3 features · August 17–21

/designresearch preview

The `/design` skill brings Claude Design’s artboard workflow into the CLI and Claude Code Desktop, built on artifacts. Run it with a brief and Claude publishes a canvas of editable artboards for your UI. Pick one, tweak it, then have Claude implement it. Available on Pro, Max, Team, and Enterprise. Requires v2.1.234 or later.

Describe what you want designed and let Claude draft the options:

Claude Code

```python
> /design redesign the composer based on what people actually use it for
```

Claude prints a link to the published canvas. Open it, pick an artboard, and tell Claude which option to implement.

[Where artifacts are available](/docs/en/artifacts#availability)

Concise output stylev2.1.237

Concise is a new built-in output style. Claude leads with the result and skips preamble and narration, while doing the work as thoroughly as in the Default style. When you ask for an explanation or more detail, Claude answers in full. Error reports, security warnings, and confirmations for destructive actions keep their complete content.

Turn it on under **Output style** in `/config`, or set it in your settings file:

~/.claude/settings.json

```python
{
  "outputStyle": "Concise"
}
```

Run `/clear` or start a new session, and Claude’s replies lead with the result.

[Built-in output styles](/docs/en/output-styles#built-in-output-styles)

Start a session on your machine from your phonemobile

Any machine running `claude remote-control` now shows up as a device card at the top of the Code tab in the Claude app. Remote Control is also out of research preview.

Start Remote Control on the machine you want to reach, then open the Code tab on your phone:

terminal

```python
claude remote-control
```

Your machine appears as a device card at the top of the Code tab. Tap it to pick a directory and start a session there.

[Start a Remote Control session](/docs/en/remote-control#start-a-remote-control-session)

Other wins

Claude Code now continues your session automatically when a claude.ai usage limit resets; turn it off from the **Continue automatically at usage limit** row in `/config`

The optional [`spellcheck` setting](/docs/en/interactive-mode#check-spelling-as-you-type) underlines misspelled words in the prompt input as you type, using your installed `aspell`, `hunspell`, or `ispell`

On a branch with an open GitLab merge request, with the `glab` CLI authenticated through `glab auth login`, the footer shows an [`MR !N` badge](/docs/en/interactive-mode#gitlab-merge-requests) colored by whether the merge request is a draft, open, or mergeable

Change the effort level from your phone or claude.ai/code and it [applies to the session on your machine](/docs/en/remote-control#what-connected-devices-see); Remote Control sessions hosted by Desktop or VS Code also show connected devices the session’s current permission mode

You can open [`/permissions`](/docs/en/permissions#manage-permissions) or run `/add-dir <path>` while Claude is working; permission rule changes apply to the rest of the current turn

When background tasks keep a [`/goal`](/docs/en/goal#background-work-defers-evaluation) waiting, Claude checks in on them after 30 minutes instead of waiting indefinitely and keeps checking in, at longer intervals while the session sits idle; set `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` to opt out

Your own prompts now render markdown in the transcript, with highlighted code blocks, inline code, and lists, the same way replies do

The new [`ANTHROPIC_DEFAULT_MODEL`](/docs/en/model-config#set-a-default-model-for-new-sessions) environment variable sets the model new sessions start on; a `/model` pick still overrides it and persists across restarts

With the `notify_when_idle` input on `SendMessage`, Claude can ask another Claude Code session on the same machine to [send one notice when it next goes idle](/docs/en/cross-session-messaging#get-a-notice-when-another-session-goes-idle)

Set [`keybindingFlavor`](/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace) to `“readline”` to make `Ctrl+W` in the prompt delete back to the previous whitespace, as Bash does, instead of stopping at punctuation such as `/`

On native Windows, your Claude Code sessions can now [message each other](/docs/en/cross-session-messaging#availability) with `SendMessage` and find each other with `ListAgents`, as on macOS and Linux

Self-hosted runners accept `--defer-shutdown-max-min`, which [keeps serving attached sessions](/docs/en/self-hosted-environments-deploy#defer-the-drain-past-the-first-signal) for a set number of minutes after SIGTERM

Self-hosted runners accept `--proxy-authorization-command` or `--proxy-authorization-file` to supply a fresh `Proxy-Authorization` header for [egress proxies that require one](/docs/en/self-hosted-environments-deploy#authenticate-to-an-egress-proxy)

[Full changelog for v2.1.234–v2.1.239 →](/docs/en/changelog#2-1-234)
