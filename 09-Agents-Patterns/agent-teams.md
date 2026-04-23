---
title: "Orchestrate teams of Claude Code sessions"
source_url: "https://code.claude.com/docs/en/agent-teams.md"
category: "09-Agents-Patterns"
fetched_at: "2026-04-08"
tags: ["agents", "claude-code"]
---

# Orchestrate teams of Claude Code sessions

Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management.

> **Warning:** Agent teams are experimental and disabled by default. Enable them by adding `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to your settings.json or environment. Agent teams have known limitations around session resumption, task coordination, and shutdown behavior.

Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other.

Unlike subagents, which run within a single session and can only report back to the main agent, you can also interact with individual teammates directly without going through the lead.

> Agent teams require Claude Code v2.1.32 or later. Check your version with `claude --version`.

## When to use agent teams

Agent teams are most effective for tasks where parallel exploration adds real value:

- **Research and review**: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other's findings
- **New modules or features**: teammates can each own a separate piece without stepping on each other
- **Debugging with competing hypotheses**: teammates test different theories in parallel and converge on the answer faster
- **Cross-layer coordination**: changes that span frontend, backend, and tests, each owned by a different teammate

Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.

### Compare with subagents

Both agent teams and subagents let you parallelize work, but they operate differently. Choose based on whether your workers need to communicate with each other:

|                   | Subagents                                        | Agent teams                                         |
| :---------------- | :----------------------------------------------- | :-------------------------------------------------- |
| **Context**       | Own context window; results return to the caller | Own context window; fully independent               |
| **Communication** | Report results back to the main agent only       | Teammates message each other directly               |
| **Coordination**  | Main agent manages all work                      | Shared task list with self-coordination             |
| **Best for**      | Focused tasks where only the result matters      | Complex work requiring discussion and collaboration |
| **Token cost**    | Lower: results summarized back to main context   | Higher: each teammate is a separate Claude instance |

Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

## Enable agent teams

Agent teams are disabled by default. Enable them by setting the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable to `1`, either in your shell environment or through settings.json:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## Start your first agent team

After enabling agent teams, tell Claude to create an agent team and describe the task and the team structure you want in natural language. Claude creates the team, spawns teammates, and coordinates work based on your prompt.

This example works well because the three roles are independent and can explore the problem without waiting on each other:

```
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

From there, Claude creates a team with a shared task list, spawns teammates for each perspective, has them explore the problem, synthesizes findings, and attempts to clean up the team when finished.

The lead's terminal lists all teammates and what they're working on. Use Shift+Down to cycle through teammates and message them directly. After the last teammate, Shift+Down wraps back to the lead.

## Control your agent team

Tell the lead what you want in natural language. It handles team coordination, task assignment, and delegation based on your instructions.

### Choose a display mode

Agent teams support two display modes:

- **In-process**: all teammates run inside your main terminal. Use Shift+Down to cycle through teammates and type to message them directly. Works in any terminal, no extra setup required.
- **Split panes**: each teammate gets its own pane. You can see everyone's output at once and click into a pane to interact directly. Requires tmux, or iTerm2.

The default is `"auto"`, which uses split panes if you're already running inside a tmux session, and in-process otherwise. The `"tmux"` setting enables split-pane mode and auto-detects whether to use tmux or iTerm2 based on your terminal. To override, set `teammateMode` in your global config at `~/.claude.json`:

```json
{
  "teammateMode": "in-process"
}
```

To force in-process mode for a single session, pass it as a flag:

```bash
claude --teammate-mode in-process
```

### Specify teammates and models

Claude decides the number of teammates to spawn based on your task, or you can specify exactly what you want:

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### Require plan approval for teammates

For complex or risky tasks, you can require teammates to plan before implementing. The teammate works in read-only plan mode until the lead approves their approach:

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

When a teammate finishes planning, it sends a plan approval request to the lead. The lead reviews the plan and either approves it or rejects it with feedback. If rejected, the teammate stays in plan mode, revises based on the feedback, and resubmits. Once approved, the teammate exits plan mode and begins implementation.

### Talk to teammates directly

Each teammate is a full, independent Claude Code session. You can message any teammate directly to give additional instructions, ask follow-up questions, or redirect their approach.

- **In-process mode**: use Shift+Down to cycle through teammates, then type to send them a message. Press Enter to view a teammate's session, then Escape to interrupt their current turn. Press Ctrl+T to toggle the task list.
- **Split-pane mode**: click into a teammate's pane to interact with their session directly.

### Assign and claim tasks

The shared task list coordinates work across the team. The lead creates tasks and teammates work through them. Tasks have three states: pending, in progress, and completed. Tasks can also depend on other tasks.

The lead can assign tasks explicitly, or teammates can self-claim:

- **Lead assigns**: tell the lead which task to give to which teammate
- **Self-claim**: after finishing a task, a teammate picks up the next unassigned, unblocked task on its own

Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously.

### Shut down teammates

To gracefully end a teammate's session:

```
Ask the researcher teammate to shut down
```

The lead sends a shutdown request. The teammate can approve, exiting gracefully, or reject with an explanation.

### Clean up the team

When you're done, ask the lead to clean up:

```
Clean up the team
```

This removes the shared team resources. When the lead runs cleanup, it checks for active teammates and fails if any are still running, so shut them down first.

### Enforce quality gates with hooks

Use hooks to enforce rules when teammates finish work or tasks are created or completed:

- `TeammateIdle`: runs when a teammate is about to go idle. Exit with code 2 to send feedback and keep the teammate working.
- `TaskCreated`: runs when a task is being created. Exit with code 2 to prevent creation and send feedback.
- `TaskCompleted`: runs when a task is being marked complete. Exit with code 2 to prevent completion and send feedback.

## How agent teams work

### Architecture

An agent team consists of:

| Component     | Role                                                                                       |
| :------------ | :----------------------------------------------------------------------------------------- |
| **Team lead** | The main Claude Code session that creates the team, spawns teammates, and coordinates work |
| **Teammates** | Separate Claude Code instances that each work on assigned tasks                            |
| **Task list** | Shared list of work items that teammates claim and complete                                |
| **Mailbox**   | Messaging system for communication between agents                                          |

Teams and tasks are stored locally:

- **Team config**: `~/.claude/teams/{team-name}/config.json`
- **Task list**: `~/.claude/tasks/{team-name}/`

### Use subagent definitions for teammates

When spawning a teammate, you can reference a subagent type from any subagent scope: project, user, plugin, or CLI-defined. This lets you define a role once, such as a security-reviewer or test-runner, and reuse it both as a delegated subagent and as an agent team teammate.

```
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

### Permissions

Teammates start with the lead's permission settings. If the lead runs with `--dangerously-skip-permissions`, all teammates do too.

### Context and communication

Each teammate has its own context window. When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills.

**How teammates share information:**

- **Automatic message delivery**: when teammates send messages, they're delivered automatically to recipients
- **Idle notifications**: when a teammate finishes and stops, they automatically notify the lead
- **Shared task list**: all agents can see task status and claim available work

**Teammate messaging:**

- **message**: send a message to one specific teammate
- **broadcast**: send to all teammates simultaneously

### Token usage

Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates.

## Use case examples

### Run a parallel code review

```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

### Investigate with competing hypotheses

```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

## Best practices

### Give teammates enough context

Include task-specific details in the spawn prompt:

```
Spawn a security reviewer teammate with the prompt: "Review the authentication module
at src/auth/ for security vulnerabilities. Focus on token handling, session
management, and input validation."
```

### Choose an appropriate team size

Start with 3-5 teammates for most workflows. Having 5-6 tasks per teammate keeps everyone productive without excessive context switching.

### Size tasks appropriately

- **Too small**: coordination overhead exceeds the benefit
- **Too large**: teammates work too long without check-ins
- **Just right**: self-contained units that produce a clear deliverable

### Avoid file conflicts

Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.

## Limitations

- **No session resumption with in-process teammates**: `/resume` and `/rewind` do not restore in-process teammates
- **Task status can lag**: teammates sometimes fail to mark tasks as completed
- **Shutdown can be slow**: teammates finish their current request before shutting down
- **One team per session**: clean up the current team before starting a new one
- **No nested teams**: teammates cannot spawn their own teams
- **Lead is fixed**: the session that creates the team is the lead for its lifetime
- **Permissions set at spawn**: all teammates start with the lead's permission mode
- **Split panes require tmux or iTerm2**: not supported in VS Code's integrated terminal, Windows Terminal, or Ghostty

## See Also

- [Subagents](/en/sub-agents)
- [Git worktrees](/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)
