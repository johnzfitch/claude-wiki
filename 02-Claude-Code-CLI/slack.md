---
source_url: "https://code.claude.com/docs/en/slack.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Claude Code in Slack

Delegate coding tasks directly from your Slack workspace. When you mention `@Claude` with a coding task, Claude automatically detects the intent and creates a Claude Code session on the web.

## Use cases

- **Bug investigation and fixes**: investigate and fix bugs as soon as they're reported
- **Quick code reviews and modifications**: implement small features or refactor code
- **Collaborative debugging**: use team discussion context for debugging
- **Parallel task execution**: kick off coding tasks while you continue other work

## Prerequisites

| Requirement            | Details                                                       |
| :--------------------- | :------------------------------------------------------------ |
| Claude Plan            | Pro, Max, Team, or Enterprise with Claude Code access         |
| Claude Code on the web | Must be enabled                                               |
| GitHub Account         | Connected with at least one repository authenticated          |
| Slack Authentication   | Slack account linked to Claude account via the Claude app     |

## Setup

1. **Install the Claude App in Slack**: Workspace admin installs from the Slack App Marketplace
2. **Connect your Claude account**: Open Claude app in Slack → App Home → Click "Connect"
3. **Configure Claude Code on the web**: Visit claude.ai/code and connect your GitHub account
4. **Choose routing mode**:
   - **Code only**: all @mentions go to Claude Code sessions
   - **Code + Chat**: Claude intelligently routes between Code and Chat
5. **Add Claude to channels**: type `/invite @Claude` in desired channels

## How it works

1. **Initiation**: @mention Claude with a coding request
2. **Detection**: Claude analyzes and detects coding intent
3. **Session creation**: New Claude Code session created on claude.ai/code
4. **Progress updates**: Status updates posted to Slack thread
5. **Completion**: Claude @mentions you with summary and action buttons
6. **Review**: Click "View Session" for full transcript, or "Create PR"

### Context gathering

- **From threads**: gathers context from all messages in the thread
- **From channels**: looks at recent channel messages for relevant context

## Message actions

- **View Session**: opens full session in browser
- **Create PR**: creates a pull request from session changes
- **Retry as Code**: retry as Claude Code task if initially routed to Chat
- **Change Repo**: select a different repository

## Access and permissions

### User-level

- Each user runs sessions under their own Claude account
- Sessions count against individual plan limits
- Users can only access personally connected repositories
- Sessions appear in Claude Code history on claude.ai/code

### Channel-based access control

- Claude is not added to channels automatically
- Invite required: `/invite @Claude`
- Works in both public and private channels
- Admins control access by managing which channels Claude is invited to

## Best practices

- **Be specific**: include file names, function names, or error messages
- **Provide context**: mention the repository if not clear
- **Define success**: explain what "done" looks like
- **Use threads**: reply in threads for full context gathering

## Limitations

- **GitHub only**: currently supports GitHub repositories
- **One PR at a time**: each session creates one pull request
- **Rate limits apply**: uses your individual plan's limits
- **Web access required**: users must have Claude Code on the web access
- **Channels only**: does not work in DMs

## See Also

- [Claude Code on the web](/en/claude-code-on-the-web)
- [Claude for Slack](https://claude.com/claude-and-slack)
