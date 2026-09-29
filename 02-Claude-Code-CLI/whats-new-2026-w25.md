---
title: "Week 25 · June 15–19, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w25"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:45Z"
tags: ["claude-code"]
---

# Week 25 · June 15–19, 2026

Copy pageCopy page

Publish a live, shareable page from your session with Artifacts, match tool parameters in deny and ask rules, and set any setting from the prompt with /config.

Copy pageCopy page

Releases [v2.1.178 → v2.1.183](changelog.md#2-1-178)3 features · June 15–19

Artifacts

An artifact is a live, interactive page that Claude Code publishes from your session to a private URL on claude.ai, and it updates in place as the session keeps working. Ask for one when terminal text is the wrong medium, such as a PR walkthrough with the diff annotated inline or a dashboard built from session data. Artifacts are in beta on Team and Enterprise plans.

Ask Claude for a page, then approve the publish prompt:

Claude Code

```python
Make an artifact that walks through this PR with the diff annotated inline.
```

[Create an artifact](artifacts.md#create-an-artifact)

Match by input parameterv2.1.178

Deny and ask permission rules can now match a tool’s input parameters with the `Tool(param:value)` syntax. For example, `Agent(model:opus)` matches subagent spawns that request the Opus model tier. The value accepts `*` as a wildcard, so `Agent(isolation:*)` matches any explicit isolation value.

Add a parameter rule to the deny list in `settings.json`:

.claude/settings.json

```python
{
  "permissions": {
    "deny": ["Agent(model:opus)"]
  }
}
```

[Match by input parameter](permissions.md#match-by-input-parameter)

Set any setting from the promptv2.1.181

Pass `key=value` to `/config` to change a setting directly without opening the Settings interface. The syntax also works in non-interactive mode with the `-p` flag and from Remote Control.

Set the `thinking` setting from the prompt:

Claude Code

```python
/config thinking=false
```

[Commands reference](commands.md#all-commands)

Other wins

Auto mode now blocks destructive git commands (`git reset --hard`, `git clean -fd`, `git stash drop`) when you didn’t ask to discard local work, and blocks `terraform destroy` unless you asked for the specific stack

Set the new `attribution.sessionUrl` setting to `false` to omit the claude.ai session link from commits and PRs in web and Remote Control sessions

In the `/config` interface, Enter and Space both change the selected setting, and Esc now saves and closes instead of reverting

New `sandbox.allowAppleEvents` opt-in setting lets sandboxed commands send Apple Events on macOS

Point `CLAUDE_CLIENT_PRESENCE_FILE` at a marker file to suppress mobile push notifications while you’re at the machine

Long paragraphs now stream line by line instead of waiting for the first line break

API connection drops mid-thinking now retry automatically instead of showing “Connection closed while thinking”

With `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` set, every session has one implicit team, so you spawn teammates directly with the Agent tool’s `name` parameter

Skills in nested `.claude/skills` directories load when working on files there; on a name clash the nested skill appears as `<dir>:<name>` so both stay available

Fixed prompt caching not reading on a custom `ANTHROPIC_BASE_URL` and on Microsoft Foundry

Fixed Write and Edit producing zero-byte or truncated files on network drives and cloud-synced folders

[Full changelog for v2.1.178–v2.1.183 →](changelog.md#2-1-178)
