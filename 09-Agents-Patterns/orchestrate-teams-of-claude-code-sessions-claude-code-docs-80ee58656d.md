---
category: "09-Agents-Patterns"
fetched_at: "2026-02-23T00:45:37Z"
source_url: "https://code.claude.com/docs/en/agent-teams"
title: "Orchestrate teams of Claude Code sessions - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Build with Claude Code

Orchestrate teams of Claude Code sessions

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Build with Claude Code

- [](/docs/en/sub-agents)
  Create custom subagents
- [](/docs/en/agent-teams)
  Run agent teams
- [](/docs/en/plugins)
  Create plugins
- [](/docs/en/discover-plugins)
  Discover and install prebuilt plugins
- [](/docs/en/skills)
  Extend Claude with skills
- [](/docs/en/output-styles)
  Output styles
- [](/docs/en/hooks-guide)
  Automate with hooks
- [](/docs/en/headless)
  Programmatic usage
- [](/docs/en/mcp)
  Model Context Protocol (MCP)
- [](/docs/en/troubleshooting)
  Troubleshooting

On this page

- [When to use agent teams](#when-to-use-agent-teams)
- [Compare with subagents](#compare-with-subagents)
- [Enable agent teams](#enable-agent-teams)
- [Start your first agent team](#start-your-first-agent-team)
- [Control your agent team](#control-your-agent-team)
- [Choose a display mode](#choose-a-display-mode)
- [Specify teammates and models](#specify-teammates-and-models)
- [Require plan approval for teammates](#require-plan-approval-for-teammates)
- [Talk to teammates directly](#talk-to-teammates-directly)
- [Assign and claim tasks](#assign-and-claim-tasks)
- [Shut down teammates](#shut-down-teammates)
- [Clean up the team](#clean-up-the-team)
- [Enforce quality gates with hooks](#enforce-quality-gates-with-hooks)
- [How agent teams work](#how-agent-teams-work)
- [How Claude starts agent teams](#how-claude-starts-agent-teams)
- [Architecture](#architecture)
- [Permissions](#permissions)
- [Context and communication](#context-and-communication)
- [Token usage](#token-usage)
- [Use case examples](#use-case-examples)
- [Run a parallel code review](#run-a-parallel-code-review)
- [Investigate with competing hypotheses](#investigate-with-competing-hypotheses)
- [Best practices](#best-practices)
- [Give teammates enough context](#give-teammates-enough-context)
- [Size tasks appropriately](#size-tasks-appropriately)
- [Wait for teammates to finish](#wait-for-teammates-to-finish)
- [Start with research and review](#start-with-research-and-review)
- [Avoid file conflicts](#avoid-file-conflicts)
- [Monitor and steer](#monitor-and-steer)
- [Troubleshooting](#troubleshooting)
- [Teammates not appearing](#teammates-not-appearing)
- [Too many permission prompts](#too-many-permission-prompts)
- [Teammates stopping on errors](#teammates-stopping-on-errors)
- [Lead shuts down before work is done](#lead-shuts-down-before-work-is-done)
- [Orphaned tmux sessions](#orphaned-tmux-sessions)
- [Limitations](#limitations)
- [Next steps](#next-steps)

Build with Claude Code

# Orchestrate teams of Claude Code sessions

Copy page

Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management.

Copy page

Agent teams are experimental and disabled by default. Enable them by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to your [settings.json](/docs/en/settings) or environment. Agent teams have [known limitations](#limitations) around session resumption, task coordination, and shutdown behavior.

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other. Unlike [subagents](/docs/en/sub-agents), which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead. This page covers:

- [When to use agent teams](#when-to-use-agent-teams), including best use cases and how they compare with subagents
- [Starting a team](#start-your-first-agent-team)
- [Controlling teammates](#control-your-agent-team), including display modes, task assignment, and delegation
- [Best practices for parallel work](#best-practices)

## 

[​](#when-to-use-agent-teams)

When to use agent teams

Agent teams are most effective for tasks where parallel exploration adds real value. See [use case examples](#use-case-examples) for full scenarios. The strongest use cases are:

- **Research and review**: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other’s findings
- **New modules or features**: teammates can each own a separate piece without stepping on each other
- **Debugging with competing hypotheses**: teammates test different theories in parallel and converge on the answer faster
- **Cross-layer coordination**: changes that span frontend, backend, and tests, each owned by a different teammate

Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or [subagents](/docs/en/sub-agents) are more effective.

### 

[​](#compare-with-subagents)

Compare with subagents

Both agent teams and [subagents](/docs/en/sub-agents) let you parallelize work, but they operate differently. Choose based on whether your workers need to communicate with each other:

|  | Subagents | Agent teams |
|:---|:---|:---|
| **Context** | Own context window; results return to the caller | Own context window; fully independent |
| **Communication** | Report results back to the main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

## 

[​](#enable-agent-teams)

Enable agent teams

Agent teams are disabled by default. Enable them by setting the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable to `1`, either in your shell environment or through [settings.json](/docs/en/settings):

settings.json

Report incorrect code

Copy

Ask AI

``` shiki
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## 

[​](#start-your-first-agent-team)

Start your first agent team

After enabling agent teams, tell Claude to create an agent team and describe the task and the team structure you want in natural language. Claude creates the team, spawns teammates, and coordinates work based on your prompt. This example works well because the three roles are independent and can explore the problem without waiting on each other:

Report incorrect code

Copy

Ask AI

``` shiki
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

From there, Claude creates a team with a [shared task list](/docs/en/interactive-mode#task-list), spawns teammates for each perspective, has them explore the problem, synthesizes findings, and attempts to [clean up the team](#clean-up-the-team) when finished. The lead’s terminal lists all teammates and what they’re working on. Use Shift+Down to cycle through teammates and message them directly. After the last teammate, Shift+Down wraps back to the lead. If you want each teammate in its own split pane, see [Choose a display mode](#choose-a-display-mode).

## 

[​](#control-your-agent-team)

Control your agent team

Tell the lead what you want in natural language. It handles team coordination, task assignment, and delegation based on your instructions.

### 

[​](#choose-a-display-mode)

Choose a display mode

Agent teams support two display modes:

- **In-process**: all teammates run inside your main terminal. Use Shift+Down to cycle through teammates and type to message them directly. Works in any terminal, no extra setup required.
- **Split panes**: each teammate gets its own pane. You can see everyone’s output at once and click into a pane to interact directly. Requires tmux, or iTerm2.

`tmux` has known limitations on certain operating systems and traditionally works best on macOS. Using `tmux -CC` in iTerm2 is the suggested entrypoint into `tmux`.

The default is `"auto"`, which uses split panes if you’re already running inside a tmux session, and in-process otherwise. The `"tmux"` setting enables split-pane mode and auto-detects whether to use tmux or iTerm2 based on your terminal. To override, set `teammateMode` in your [settings.json](/docs/en/settings):

Report incorrect code

Copy

Ask AI

``` shiki
{
  "teammateMode": "in-process"
}
```

To force in-process mode for a single session, pass it as a flag:

Report incorrect code

Copy

Ask AI

``` shiki
claude --teammate-mode in-process
```

Split-pane mode requires either [tmux](https://github.com/tmux/tmux/wiki) or iTerm2 with the [`it2` CLI](https://github.com/mkusaka/it2). To install manually:

- **tmux**: install through your system’s package manager. See the [tmux wiki](https://github.com/tmux/tmux/wiki/Installing) for platform-specific instructions.
- **iTerm2**: install the [`it2` CLI](https://github.com/mkusaka/it2), then enable the Python API in **iTerm2 → Settings → General → Magic → Enable Python API**.

### 

[​](#specify-teammates-and-models)

Specify teammates and models

Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want:

Report incorrect code

Copy

Ask AI

``` shiki
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### 

[​](#require-plan-approval-for-teammates)

Require plan approval for teammates

For complex or risky tasks, you can require teammates to plan before implementing. The teammate works in read-only plan mode until the lead approves their approach:

Report incorrect code

Copy

Ask AI

``` shiki
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

When a teammate finishes planning, it sends a plan approval request to the lead. The lead reviews the plan and either approves it or rejects it with feedback. If rejected, the teammate stays in plan mode, revises based on the feedback, and resubmits. Once approved, the teammate exits plan mode and begins implementation. The lead makes approval decisions autonomously. To influence the lead’s judgment, give it criteria in your prompt, such as “only approve plans that include test coverage” or “reject plans that modify the database schema.”

### 

[​](#talk-to-teammates-directly)

Talk to teammates directly

Each teammate is a full, independent Claude Code session. You can message any teammate directly to give additional instructions, ask follow-up questions, or redirect their approach.

- **In-process mode**: use Shift+Down to cycle through teammates, then type to send them a message. Press Enter to view a teammate’s session, then Escape to interrupt their current turn. Press Ctrl+T to toggle the task list.
- **Split-pane mode**: click into a teammate’s pane to interact with their session directly. Each teammate has a full view of their own terminal.

### 

[​](#assign-and-claim-tasks)

Assign and claim tasks

The shared task list coordinates work across the team. The lead creates tasks and teammates work through them. Tasks have three states: pending, in progress, and completed. Tasks can also depend on other tasks: a pending task with unresolved dependencies cannot be claimed until those dependencies are completed. The lead can assign tasks explicitly, or teammates can self-claim:

- **Lead assigns**: tell the lead which task to give to which teammate
- **Self-claim**: after finishing a task, a teammate picks up the next unassigned, unblocked task on its own

Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously.

### 

[​](#shut-down-teammates)

Shut down teammates

To gracefully end a teammate’s session:

Report incorrect code

Copy

Ask AI

``` shiki
Ask the researcher teammate to shut down
```

The lead sends a shutdown request. The teammate can approve, exiting gracefully, or reject with an explanation.

### 

[​](#clean-up-the-team)

Clean up the team

When you’re done, ask the lead to clean up:

Report incorrect code

Copy

Ask AI

``` shiki
Clean up the team
```

This removes the shared team resources. When the lead runs cleanup, it checks for active teammates and fails if any are still running, so shut them down first.

Always use the lead to clean up. Teammates should not run cleanup because their team context may not resolve correctly, potentially leaving resources in an inconsistent state.

### 

[​](#enforce-quality-gates-with-hooks)

Enforce quality gates with hooks

Use [hooks](/docs/en/hooks) to enforce rules when teammates finish work or tasks complete:

- [`TeammateIdle`](/docs/en/hooks#teammateidle): runs when a teammate is about to go idle. Exit with code 2 to send feedback and keep the teammate working.
- [`TaskCompleted`](/docs/en/hooks#taskcompleted): runs when a task is being marked complete. Exit with code 2 to prevent completion and send feedback.

## 

[​](#how-agent-teams-work)

How agent teams work

This section covers the architecture and mechanics behind agent teams. If you want to start using them, see [Control your agent team](#control-your-agent-team) above.

### 

[​](#how-claude-starts-agent-teams)

How Claude starts agent teams

There are two ways agent teams get started:

- **You request a team**: give Claude a task that benefits from parallel work and explicitly ask for an agent team. Claude creates one based on your instructions.
- **Claude proposes a team**: if Claude determines your task would benefit from parallel work, it may suggest creating a team. You confirm before it proceeds.

In both cases, you stay in control. Claude won’t create a team without your approval.

### 

[​](#architecture)

Architecture

An agent team consists of:

| Component | Role |
|:---|:---|
| **Team lead** | The main Claude Code session that creates the team, spawns teammates, and coordinates work |
| **Teammates** | Separate Claude Code instances that each work on assigned tasks |
| **Task list** | Shared list of work items that teammates claim and complete |
| **Mailbox** | Messaging system for communication between agents |

See [Choose a display mode](#choose-a-display-mode) for display configuration options. Teammate messages arrive at the lead automatically. The system manages task dependencies automatically. When a teammate completes a task that other tasks depend on, blocked tasks unblock without manual intervention. Teams and tasks are stored locally:

- **Team config**: `~/.claude/teams/{team-name}/config.json`
- **Task list**: `~/.claude/tasks/{team-name}/`

The team config contains a `members` array with each teammate’s name, agent ID, and agent type. Teammates can read this file to discover other team members.

### 

[​](#permissions)

Permissions

Teammates start with the lead’s permission settings. If the lead runs with `--dangerously-skip-permissions`, all teammates do too. After spawning, you can change individual teammate modes, but you can’t set per-teammate modes at spawn time.

### 

[​](#context-and-communication)

Context and communication

Each teammate has its own context window. When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills. It also receives the spawn prompt from the lead. The lead’s conversation history does not carry over. **How teammates share information:**

- **Automatic message delivery**: when teammates send messages, they’re delivered automatically to recipients. The lead doesn’t need to poll for updates.
- **Idle notifications**: when a teammate finishes and stops, they automatically notify the lead.
- **Shared task list**: all agents can see task status and claim available work.

**Teammate messaging:**

- **message**: send a message to one specific teammate
- **broadcast**: send to all teammates simultaneously. Use sparingly, as costs scale with team size.

### 

[​](#token-usage)

Token usage

Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates. For research, review, and new feature work, the extra tokens are usually worthwhile. For routine tasks, a single session is more cost-effective. See [agent team token costs](/docs/en/costs#agent-team-token-costs) for usage guidance.

## 

[​](#use-case-examples)

Use case examples

These examples show how agent teams handle tasks where parallel exploration adds value.

### 

[​](#run-a-parallel-code-review)

Run a parallel code review

A single reviewer tends to gravitate toward one type of issue at a time. Splitting review criteria into independent domains means security, performance, and test coverage all get thorough attention simultaneously. The prompt assigns each teammate a distinct lens so they don’t overlap:

Report incorrect code

Copy

Ask AI

``` shiki
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

Each reviewer works from the same PR but applies a different filter. The lead synthesizes findings across all three after they finish.

### 

[​](#investigate-with-competing-hypotheses)

Investigate with competing hypotheses

When the root cause is unclear, a single agent tends to find one plausible explanation and stop looking. The prompt fights this by making teammates explicitly adversarial: each one’s job is not only to investigate its own theory but to challenge the others’.

Report incorrect code

Copy

Ask AI

``` shiki
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

The debate structure is the key mechanism here. Sequential investigation suffers from anchoring: once one theory is explored, subsequent investigation is biased toward it. With multiple independent investigators actively trying to disprove each other, the theory that survives is much more likely to be the actual root cause.

## 

[​](#best-practices)

Best practices

### 

[​](#give-teammates-enough-context)

Give teammates enough context

Teammates load project context automatically, including CLAUDE.md, MCP servers, and skills, but they don’t inherit the lead’s conversation history. See [Context and communication](#context-and-communication) for details. Include task-specific details in the spawn prompt:

Report incorrect code

Copy

Ask AI

``` shiki
Spawn a security reviewer teammate with the prompt: "Review the authentication module
at src/auth/ for security vulnerabilities. Focus on token handling, session
management, and input validation. The app uses JWT tokens stored in
httpOnly cookies. Report any issues with severity ratings."
```

### 

[​](#size-tasks-appropriately)

Size tasks appropriately

- **Too small**: coordination overhead exceeds the benefit
- **Too large**: teammates work too long without check-ins, increasing risk of wasted effort
- **Just right**: self-contained units that produce a clear deliverable, such as a function, a test file, or a review

The lead breaks work into tasks and assigns them to teammates automatically. If it isn’t creating enough tasks, ask it to split the work into smaller pieces. Having 5-6 tasks per teammate keeps everyone productive and lets the lead reassign work if someone gets stuck.

### 

[​](#wait-for-teammates-to-finish)

Wait for teammates to finish

Sometimes the lead starts implementing tasks itself instead of waiting for teammates. If you notice this:

Report incorrect code

Copy

Ask AI

``` shiki
Wait for your teammates to complete their tasks before proceeding
```

### 

[​](#start-with-research-and-review)

Start with research and review

If you’re new to agent teams, start with tasks that have clear boundaries and don’t require writing code: reviewing a PR, researching a library, or investigating a bug. These tasks show the value of parallel exploration without the coordination challenges that come with parallel implementation.

### 

[​](#avoid-file-conflicts)

Avoid file conflicts

Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.

### 

[​](#monitor-and-steer)

Monitor and steer

Check in on teammates’ progress, redirect approaches that aren’t working, and synthesize findings as they come in. Letting a team run unattended for too long increases the risk of wasted effort.

## 

[​](#troubleshooting)

Troubleshooting

### 

[​](#teammates-not-appearing)

Teammates not appearing

If teammates aren’t appearing after you ask Claude to create a team:

- In in-process mode, teammates may already be running but not visible. Press Shift+Down to cycle through active teammates.
- Check that the task you gave Claude was complex enough to warrant a team. Claude decides whether to spawn teammates based on the task.
- If you explicitly requested split panes, ensure tmux is installed and available in your PATH:
  Report incorrect code

  Copy

  Ask AI

  ``` shiki
  which tmux
  ```
- For iTerm2, verify the `it2` CLI is installed and the Python API is enabled in iTerm2 preferences.

### 

[​](#too-many-permission-prompts)

Too many permission prompts

Teammate permission requests bubble up to the lead, which can create friction. Pre-approve common operations in your [permission settings](/docs/en/permissions) before spawning teammates to reduce interruptions.

### 

[​](#teammates-stopping-on-errors)

Teammates stopping on errors

Teammates may stop after encountering errors instead of recovering. Check their output using Shift+Down in in-process mode or by clicking the pane in split mode, then either:

- Give them additional instructions directly
- Spawn a replacement teammate to continue the work

### 

[​](#lead-shuts-down-before-work-is-done)

Lead shuts down before work is done

The lead may decide the team is finished before all tasks are actually complete. If this happens, tell it to keep going. You can also tell the lead to wait for teammates to finish before proceeding if it starts doing work instead of delegating.

### 

[​](#orphaned-tmux-sessions)

Orphaned tmux sessions

If a tmux session persists after the team ends, it may not have been fully cleaned up. List sessions and kill the one created by the team:

Report incorrect code

Copy

Ask AI

``` shiki
tmux ls
tmux kill-session -t <session-name>
```

## 

[​](#limitations)

Limitations

Agent teams are experimental. Current limitations to be aware of:

- **No session resumption with in-process teammates**: `/resume` and `/rewind` do not restore in-process teammates. After resuming a session, the lead may attempt to message teammates that no longer exist. If this happens, tell the lead to spawn new teammates.
- **Task status can lag**: teammates sometimes fail to mark tasks as completed, which blocks dependent tasks. If a task appears stuck, check whether the work is actually done and update the task status manually or tell the lead to nudge the teammate.
- **Shutdown can be slow**: teammates finish their current request or tool call before shutting down, which can take time.
- **One team per session**: a lead can only manage one team at a time. Clean up the current team before starting a new one.
- **No nested teams**: teammates cannot spawn their own teams or teammates. Only the lead can manage the team.
- **Lead is fixed**: the session that creates the team is the lead for its lifetime. You can’t promote a teammate to lead or transfer leadership.
- **Permissions set at spawn**: all teammates start with the lead’s permission mode. You can change individual teammate modes after spawning, but you can’t set per-teammate modes at spawn time.
- **Split panes require tmux or iTerm2**: the default in-process mode works in any terminal. Split-pane mode isn’t supported in VS Code’s integrated terminal, Windows Terminal, or Ghostty.

**`CLAUDE.md` works normally**: teammates read `CLAUDE.md` files from their working directory. Use this to provide project-specific guidance to all teammates.

## 

[​](#next-steps)

Next steps

Explore related approaches for parallel work and delegation:

- **Lightweight delegation**: [subagents](/docs/en/sub-agents) spawn helper agents for research or verification within your session, better for tasks that don’t need inter-agent coordination
- **Manual parallel sessions**: [Git worktrees](/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) let you run multiple Claude Code sessions yourself without automated team coordination
- **Compare approaches**: see the [subagent vs agent team](/docs/en/features-overview#compare-similar-features) comparison for a side-by-side breakdown

Was this page helpful?

Yes

No

[Create custom subagents](/docs/en/sub-agents)[Create plugins](/docs/en/plugins)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
