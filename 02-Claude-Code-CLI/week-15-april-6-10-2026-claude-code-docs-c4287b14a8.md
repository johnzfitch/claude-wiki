---
title: "Week 15 · April 6–10, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w15"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:56Z"
tags: ["claude-code"]
---

# Week 15 · April 6–10, 2026

Copy pageCopy page

Ultraplan cloud planning, the Monitor tool with self-pacing /loop, /team-onboarding for packaging your setup, and /autofix-pr from your terminal.

Copy pageCopy page

Releases [v2.1.92 → v2.1.101](/docs/en/changelog#2-1-92)4 features · April 6–10

Ultraplanresearch preview

Kick off plan mode in the cloud from your terminal, then review the result in your browser. Claude drafts the plan in a Claude Code on the web session while your terminal stays free; when it’s ready you comment on individual sections, ask for revisions, and choose to execute remotely or send it back to your CLI. As of v2.1.101 the first run auto-creates a default cloud environment, so there’s no web setup step before you can try it.

Run the command, or just include the keyword in any prompt:

Claude Code

```python
/ultraplan migrate the auth service from sessions to JWTs
```

[Ultraplan guide](/docs/en/ultraplan)

Monitor toolv2.1.98

A new built-in tool that spawns a background watcher and streams its events into the conversation: each event lands as a new transcript message that Claude reacts to immediately. Tail a training run, babysit a PR’s CI, or auto-fix a dev server crash the moment it happens, all without a Bash sleep loop holding the turn open.

Ask Claude to watch something while you keep working:

Claude Code

```python
Tail server.log in the background and tell me the moment a 5xx shows up
```

This pairs with `/loop`, which now self-paces: omit the interval and Claude schedules the next tick based on the task, or reaches for the Monitor tool to skip polling altogether.

Claude Code

```python
/loop check CI on my PR
```

[Monitor tool reference](/docs/en/tools-reference#monitor-tool)

/autofix-prCLI

PR auto-fix landed on the web in Week 13. Now you can turn it on without leaving your terminal: `/autofix-pr` infers the open PR for your current branch and enables auto-fix for it on Claude Code on the web in one step. Push your branch, run the command, walk away; Claude watches CI and review comments and pushes fixes until it’s green.

Run it from the PR’s branch:

Claude Code

```python
/autofix-pr
```

[Auto-fix pull requests](/docs/en/claude-code-on-the-web#auto-fix-pull-requests)

/team-onboardingv2.1.101

Generates a teammate ramp-up guide from your local Claude Code usage. Run it in a project you know well and hand the output to a new teammate so they can replay your setup instead of starting from defaults.

Run it from a project you’ve spent real time in:

Claude Code

```python
/team-onboarding
```

[Commands reference](/docs/en/commands)

Other wins

Focus view: press `Ctrl+O` in flicker-free mode to collapse the view to your last prompt, a one-line tool summary with diffstats, and Claude’s final response

Guided [Amazon Bedrock](/docs/en/amazon-bedrock) and [Google Cloud’s Agent Platform](/docs/en/google-vertex-ai) setup wizards on the login screen: pick “3rd-party platform” for step-by-step auth, region, credential check, and model pinning

`/agents` gets a tabbed layout: a Running tab shows live subagents with a `● N running` count, plus Run agent and View running instance actions in the Library tab

Default effort level is now `high` for API-key, Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, Team, and Enterprise users (control with `/effort`)

`/cost` shows a per-model and cache-hit breakdown for subscription users

`/release-notes` is now an interactive version picker

Status line: new `refreshInterval` setting re-runs the command every N seconds, and `workspace.git_worktree` in the JSON input

`CLAUDE_CODE_PERFORCE_MODE`: Edit/Write fail on read-only files with a `p4 edit` hint instead of silently overwriting

OS CA certificate store is now trusted by default, so enterprise TLS proxies work without extra setup (`CLAUDE_CODE_CERT_STORE=bundled` to opt out)

Amazon Bedrock powered by Mantle: set `CLAUDE_CODE_USE_MANTLE=1`

Hardened Bash tool permissions: backslash-escaped flags, env-var prefixes, `/dev/tcp` redirects, and compound commands now prompt correctly

`UserPromptSubmit` hooks can set the session title via `hookSpecificOutput.sessionTitle`

[Full changelog for v2.1.92–v2.1.101 →](/docs/en/changelog#2-1-92)
