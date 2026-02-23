---
category: "09-Agents-Patterns"
fetched_at: "2026-02-23T00:45:36Z"
source_url: "https://code.claude.com/docs/en/sub-agents"
title: "Subagents - Claude Code Docs"
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

Create custom subagents

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

- [Built-in subagents](#built-in-subagents)
- [Quickstart: create your first subagent](#quickstart-create-your-first-subagent)
- [Configure subagents](#configure-subagents)
- [Use the /agents command](#use-the-%2Fagents-command)
- [Choose the subagent scope](#choose-the-subagent-scope)
- [Write subagent files](#write-subagent-files)
- [Supported frontmatter fields](#supported-frontmatter-fields)
- [Choose a model](#choose-a-model)
- [Control subagent capabilities](#control-subagent-capabilities)
- [Available tools](#available-tools)
- [Restrict which subagents can be spawned](#restrict-which-subagents-can-be-spawned)
- [Permission modes](#permission-modes)
- [Preload skills into subagents](#preload-skills-into-subagents)
- [Enable persistent memory](#enable-persistent-memory)
- [Conditional rules with hooks](#conditional-rules-with-hooks)
- [Disable specific subagents](#disable-specific-subagents)
- [Define hooks for subagents](#define-hooks-for-subagents)
- [Hooks in subagent frontmatter](#hooks-in-subagent-frontmatter)
- [Project-level hooks for subagent events](#project-level-hooks-for-subagent-events)
- [Work with subagents](#work-with-subagents)
- [Understand automatic delegation](#understand-automatic-delegation)
- [Run subagents in foreground or background](#run-subagents-in-foreground-or-background)
- [Common patterns](#common-patterns)
- [Isolate high-volume operations](#isolate-high-volume-operations)
- [Run parallel research](#run-parallel-research)
- [Chain subagents](#chain-subagents)
- [Choose between subagents and main conversation](#choose-between-subagents-and-main-conversation)
- [Manage subagent context](#manage-subagent-context)
- [Resume subagents](#resume-subagents)
- [Auto-compaction](#auto-compaction)
- [Example subagents](#example-subagents)
- [Code reviewer](#code-reviewer)
- [Debugger](#debugger)
- [Data scientist](#data-scientist)
- [Database query validator](#database-query-validator)
- [Next steps](#next-steps)

Build with Claude Code

# Create custom subagents

Copy page

Create and use specialized AI subagents in Claude Code for task-specific workflows and improved context management.

Copy page

Subagents are specialized AI assistants that handle specific types of tasks. Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. When Claude encounters a task that matches a subagent’s description, it delegates to that subagent, which works independently and returns results.

If you need multiple agents working in parallel and communicating with each other, see [agent teams](/docs/en/agent-teams) instead. Subagents work within a single session; agent teams coordinate across separate sessions.

Subagents help you:

- **Preserve context** by keeping exploration and implementation out of your main conversation
- **Enforce constraints** by limiting which tools a subagent can use
- **Reuse configurations** across projects with user-level subagents
- **Specialize behavior** with focused system prompts for specific domains
- **Control costs** by routing tasks to faster, cheaper models like Haiku

Claude uses each subagent’s description to decide when to delegate tasks. When you create a subagent, write a clear description so Claude knows when to use it. Claude Code includes several built-in subagents like **Explore**, **Plan**, and **general-purpose**. You can also create custom subagents to handle specific tasks. This page covers the [built-in subagents](#built-in-subagents), [how to create your own](#quickstart-create-your-first-subagent), [full configuration options](#configure-subagents), [patterns for working with subagents](#work-with-subagents), and [example subagents](#example-subagents).

## 

[​](#built-in-subagents)

Built-in subagents

Claude Code includes built-in subagents that Claude automatically uses when appropriate. Each inherits the parent conversation’s permissions with additional tool restrictions.

- Explore

- Plan

- General-purpose

- Other

A fast, read-only agent optimized for searching and analyzing codebases.

- **Model**: Haiku (fast, low-latency)
- **Tools**: Read-only tools (denied access to Write and Edit tools)
- **Purpose**: File discovery, code search, codebase exploration

Claude delegates to Explore when it needs to search or understand a codebase without making changes. This keeps exploration results out of your main conversation context.When invoking Explore, Claude specifies a thoroughness level: **quick** for targeted lookups, **medium** for balanced exploration, or **very thorough** for comprehensive analysis.

A research agent used during [plan mode](/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis) to gather context before presenting a plan.

- **Model**: Inherits from main conversation
- **Tools**: Read-only tools (denied access to Write and Edit tools)
- **Purpose**: Codebase research for planning

When you’re in plan mode and Claude needs to understand your codebase, it delegates research to the Plan subagent. This prevents infinite nesting (subagents cannot spawn other subagents) while still gathering necessary context.

A capable agent for complex, multi-step tasks that require both exploration and action.

- **Model**: Inherits from main conversation
- **Tools**: All tools
- **Purpose**: Complex research, multi-step operations, code modifications

Claude delegates to general-purpose when the task requires both exploration and modification, complex reasoning to interpret results, or multiple dependent steps.

Claude Code includes additional helper agents for specific tasks. These are typically invoked automatically, so you don’t need to use them directly.

| Agent | Model | When Claude uses it |
|:---|:---|:---|
| Bash | Inherits | Running terminal commands in a separate context |
| statusline-setup | Sonnet | When you run `/statusline` to configure your status line |
| Claude Code Guide | Haiku | When you ask questions about Claude Code features |

Beyond these built-in subagents, you can create your own with custom prompts, tool restrictions, permission modes, hooks, and skills. The following sections show how to get started and customize subagents.

## 

[​](#quickstart-create-your-first-subagent)

Quickstart: create your first subagent

Subagents are defined in Markdown files with YAML frontmatter. You can [create them manually](#write-subagent-files) or use the `/agents` command. This walkthrough guides you through creating a user-level subagent with the `/agent` command. The subagent reviews code and suggests improvements for the codebase.

1

[](#)

Open the subagents interface

In Claude Code, run:

Report incorrect code

Copy

Ask AI

``` shiki
/agents
```

2

[](#)

Create a new user-level agent

Select **Create new agent**, then choose **User-level**. This saves the subagent to `~/.claude/agents/` so it’s available in all your projects.

3

[](#)

Generate with Claude

Select **Generate with Claude**. When prompted, describe the subagent:

Report incorrect code

Copy

Ask AI

``` shiki
A code improvement agent that scans files and suggests improvements
for readability, performance, and best practices. It should explain
each issue, show the current code, and provide an improved version.
```

Claude generates the system prompt and configuration. Press `e` to open it in your editor if you want to customize it.

4

[](#)

Select tools

For a read-only reviewer, deselect everything except **Read-only tools**. If you keep all tools selected, the subagent inherits all tools available to the main conversation.

5

[](#)

Select model

Choose which model the subagent uses. For this example agent, select **Sonnet**, which balances capability and speed for analyzing code patterns.

6

[](#)

Choose a color

Pick a background color for the subagent. This helps you identify which subagent is running in the UI.

7

[](#)

Save and try it out

Save the subagent. It’s available immediately (no restart needed). Try it:

Report incorrect code

Copy

Ask AI

``` shiki
Use the code-improver agent to suggest improvements in this project
```

Claude delegates to your new subagent, which scans the codebase and returns improvement suggestions.

You now have a subagent you can use in any project on your machine to analyze codebases and suggest improvements. You can also create subagents manually as Markdown files, define them via CLI flags, or distribute them through plugins. The following sections cover all configuration options.

## 

[​](#configure-subagents)

Configure subagents

### 

[​](#use-the-/agents-command)

Use the /agents command

The `/agents` command provides an interactive interface for managing subagents. Run `/agents` to:

- View all available subagents (built-in, user, project, and plugin)
- Create new subagents with guided setup or Claude generation
- Edit existing subagent configuration and tool access
- Delete custom subagents
- See which subagents are active when duplicates exist

This is the recommended way to create and manage subagents. For manual creation or automation, you can also add subagent files directly. To list all configured subagents from the command line without starting an interactive session, run `claude agents`. This shows agents grouped by source and indicates which are overridden by higher-priority definitions.

### 

[​](#choose-the-subagent-scope)

Choose the subagent scope

Subagents are Markdown files with YAML frontmatter. Store them in different locations depending on scope. When multiple subagents share the same name, the higher-priority location wins.

| Location | Scope | Priority | How to create |
|:---|:---|:---|:---|
| `--agents` CLI flag | Current session | 1 (highest) | Pass JSON when launching Claude Code |
| `.claude/agents/` | Current project | 2 | Interactive or manual |
| `~/.claude/agents/` | All your projects | 3 | Interactive or manual |
| Plugin’s `agents/` directory | Where plugin is enabled | 4 (lowest) | Installed with [plugins](/docs/en/plugins) |

**Project subagents** (`.claude/agents/`) are ideal for subagents specific to a codebase. Check them into version control so your team can use and improve them collaboratively. **User subagents** (`~/.claude/agents/`) are personal subagents available in all your projects. **CLI-defined subagents** are passed as JSON when launching Claude Code. They exist only for that session and aren’t saved to disk, making them useful for quick testing or automation scripts:

Report incorrect code

Copy

Ask AI

``` shiki
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

The `--agents` flag accepts JSON with the same [frontmatter](#supported-frontmatter-fields) fields as file-based subagents: `description`, `prompt`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `skills`, and `memory`. Use `prompt` for the system prompt, equivalent to the markdown body in file-based subagents. See the [CLI reference](/docs/en/cli-reference#agents-flag-format) for the full JSON format. **Plugin subagents** come from [plugins](/docs/en/plugins) you’ve installed. They appear in `/agents` alongside your custom subagents. See the [plugin components reference](/docs/en/plugins-reference#agents) for details on creating plugin subagents.

### 

[​](#write-subagent-files)

Write subagent files

Subagent files use YAML frontmatter for configuration, followed by the system prompt in Markdown:

Subagents are loaded at session start. If you create a subagent by manually adding a file, restart your session or use `/agents` to load it immediately.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

The frontmatter defines the subagent’s metadata and configuration. The body becomes the system prompt that guides the subagent’s behavior. Subagents receive only this system prompt (plus basic environment details like working directory), not the full Claude Code system prompt.

#### 

[​](#supported-frontmatter-fields)

Supported frontmatter fields

The following fields can be used in the YAML frontmatter. Only `name` and `description` are required.

| Field | Required | Description |
|:---|:---|:---|
| `name` | Yes | Unique identifier using lowercase letters and hyphens |
| `description` | Yes | When Claude should delegate to this subagent |
| `tools` | No | [Tools](#available-tools) the subagent can use. Inherits all tools if omitted |
| `disallowedTools` | No | Tools to deny, removed from inherited or specified list |
| `model` | No | [Model](#choose-a-model) to use: `sonnet`, `opus`, `haiku`, or `inherit`. Defaults to `inherit` |
| `permissionMode` | No | [Permission mode](#permission-modes): `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, or `plan` |
| `maxTurns` | No | Maximum number of agentic turns before the subagent stops |
| `skills` | No | [Skills](/docs/en/skills) to load into the subagent’s context at startup. The full skill content is injected, not just made available for invocation. Subagents don’t inherit skills from the parent conversation |
| `mcpServers` | No | [MCP servers](/docs/en/mcp) available to this subagent. Each entry is either a server name referencing an already-configured server (e.g., `"slack"`) or an inline definition with the server name as key and a full [MCP server config](/docs/en/mcp#configure-mcp-servers) as value |
| `hooks` | No | [Lifecycle hooks](#define-hooks-for-subagents) scoped to this subagent |
| `memory` | No | [Persistent memory scope](#enable-persistent-memory): `user`, `project`, or `local`. Enables cross-session learning |
| `background` | No | Set to `true` to always run this subagent as a [background task](#run-subagents-in-foreground-or-background). Default: `false` |
| `isolation` | No | Set to `worktree` to run the subagent in a temporary [git worktree](/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees), giving it an isolated copy of the repository. The worktree is automatically cleaned up if the subagent makes no changes |

### 

[​](#choose-a-model)

Choose a model

The `model` field controls which [AI model](/docs/en/model-config) the subagent uses:

- **Model alias**: Use one of the available aliases: `sonnet`, `opus`, or `haiku`
- **inherit**: Use the same model as the main conversation
- **Omitted**: If not specified, defaults to `inherit` (uses the same model as the main conversation)

### 

[​](#control-subagent-capabilities)

Control subagent capabilities

You can control what subagents can do through tool access, permission modes, and conditional rules.

#### 

[​](#available-tools)

Available tools

Subagents can use any of Claude Code’s [internal tools](/docs/en/settings#tools-available-to-claude). By default, subagents inherit all tools from the main conversation, including MCP tools. To restrict tools, use the `tools` field (allowlist) or `disallowedTools` field (denylist):

Report incorrect code

Copy

Ask AI

``` shiki
---
name: safe-researcher
description: Research agent with restricted capabilities
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
---
```

#### 

[​](#restrict-which-subagents-can-be-spawned)

Restrict which subagents can be spawned

When an agent runs as the main thread with `claude --agent`, it can spawn subagents using the Task tool. To restrict which subagent types it can spawn, use `Task(agent_type)` syntax in the `tools` field:

Report incorrect code

Copy

Ask AI

``` shiki
---
name: coordinator
description: Coordinates work across specialized agents
tools: Task(worker, researcher), Read, Bash
---
```

This is an allowlist: only the `worker` and `researcher` subagents can be spawned. If the agent tries to spawn any other type, the request fails and the agent sees only the allowed types in its prompt. To block specific agents while allowing all others, use [`permissions.deny`](#disable-specific-subagents) instead. To allow spawning any subagent without restrictions, use `Task` without parentheses:

Report incorrect code

Copy

Ask AI

``` shiki
tools: Task, Read, Bash
```

If `Task` is omitted from the `tools` list entirely, the agent cannot spawn any subagents. This restriction only applies to agents running as the main thread with `claude --agent`. Subagents cannot spawn other subagents, so `Task(agent_type)` has no effect in subagent definitions.

#### 

[​](#permission-modes)

Permission modes

The `permissionMode` field controls how the subagent handles permission prompts. Subagents inherit the permission context from the main conversation but can override the mode.

| Mode | Behavior |
|:---|:---|
| `default` | Standard permission checking with prompts |
| `acceptEdits` | Auto-accept file edits |
| `dontAsk` | Auto-deny permission prompts (explicitly allowed tools still work) |
| `bypassPermissions` | Skip all permission checks |
| `plan` | Plan mode (read-only exploration) |

Use `bypassPermissions` with caution. It skips all permission checks, allowing the subagent to execute any operation without approval.

If the parent uses `bypassPermissions`, this takes precedence and cannot be overridden.

#### 

[​](#preload-skills-into-subagents)

Preload skills into subagents

Use the `skills` field to inject skill content into a subagent’s context at startup. This gives the subagent domain knowledge without requiring it to discover and load skills during execution.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: api-developer
description: Implement API endpoints following team conventions
skills:
  - api-conventions
  - error-handling-patterns
---

Implement API endpoints. Follow the conventions and patterns from the preloaded skills.
```

The full content of each skill is injected into the subagent’s context, not just made available for invocation. Subagents don’t inherit skills from the parent conversation; you must list them explicitly.

This is the inverse of [running a skill in a subagent](/docs/en/skills#run-skills-in-a-subagent). With `skills` in a subagent, the subagent controls the system prompt and loads skill content. With `context: fork` in a skill, the skill content is injected into the agent you specify. Both use the same underlying system.

#### 

[​](#enable-persistent-memory)

Enable persistent memory

The `memory` field gives the subagent a persistent directory that survives across conversations. The subagent uses this directory to build up knowledge over time, such as codebase patterns, debugging insights, and architectural decisions.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: code-reviewer
description: Reviews code for quality and best practices
memory: user
---

You are a code reviewer. As you review code, update your agent memory with
patterns, conventions, and recurring issues you discover.
```

Choose a scope based on how broadly the memory should apply:

| Scope | Location | Use when |
|:---|:---|:---|
| `user` | `~/.claude/agent-memory/<name-of-agent>/` | the subagent should remember learnings across all projects |
| `project` | `.claude/agent-memory/<name-of-agent>/` | the subagent’s knowledge is project-specific and shareable via version control |
| `local` | `.claude/agent-memory-local/<name-of-agent>/` | the subagent’s knowledge is project-specific but should not be checked into version control |

When memory is enabled:

- The subagent’s system prompt includes instructions for reading and writing to the memory directory.
- The subagent’s system prompt also includes the first 200 lines of `MEMORY.md` in the memory directory, with instructions to curate `MEMORY.md` if it exceeds 200 lines.
- Read, Write, and Edit tools are automatically enabled so the subagent can manage its memory files.

##### Persistent memory tips

- `user` is the recommended default scope. Use `project` or `local` when the subagent’s knowledge is only relevant to a specific codebase.
- Ask the subagent to consult its memory before starting work: “Review this PR, and check your memory for patterns you’ve seen before.”
- Ask the subagent to update its memory after completing a task: “Now that you’re done, save what you learned to your memory.” Over time, this builds a knowledge base that makes the subagent more effective.
- Include memory instructions directly in the subagent’s markdown file so it proactively maintains its own knowledge base:
  Report incorrect code

  Copy

  Ask AI

  ``` shiki
  Update your agent memory as you discover codepaths, patterns, library
  locations, and key architectural decisions. This builds up institutional
  knowledge across conversations. Write concise notes about what you found
  and where.
  ```

#### 

[​](#conditional-rules-with-hooks)

Conditional rules with hooks

For more dynamic control over tool usage, use `PreToolUse` hooks to validate operations before they execute. This is useful when you need to allow some operations of a tool while blocking others. This example creates a subagent that only allows read-only database queries. The `PreToolUse` hook runs the script specified in `command` before each Bash command executes:

Report incorrect code

Copy

Ask AI

``` shiki
---
name: db-reader
description: Execute read-only database queries
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---
```

Claude Code [passes hook input as JSON](/docs/en/hooks#pretooluse-input) via stdin to hook commands. The validation script reads this JSON, extracts the Bash command, and [exits with code 2](/docs/en/hooks#exit-code-2-behavior-per-event) to block write operations:

Report incorrect code

Copy

Ask AI

``` shiki
#!/bin/bash
# ./scripts/validate-readonly-query.sh

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Block SQL write operations (case-insensitive)
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' > /dev/null; then
  echo "Blocked: Only SELECT queries are allowed" >&2
  exit 2
fi

exit 0
```

See [Hook input](/docs/en/hooks#pretooluse-input) for the complete input schema and [exit codes](/docs/en/hooks#exit-code-output) for how exit codes affect behavior.

#### 

[​](#disable-specific-subagents)

Disable specific subagents

You can prevent Claude from using specific subagents by adding them to the `deny` array in your [settings](/docs/en/settings#permission-settings). Use the format `Task(subagent-name)` where `subagent-name` matches the subagent’s name field.

Report incorrect code

Copy

Ask AI

``` shiki
{
  "permissions": {
    "deny": ["Task(Explore)", "Task(my-custom-agent)"]
  }
}
```

This works for both built-in and custom subagents. You can also use the `--disallowedTools` CLI flag:

Report incorrect code

Copy

Ask AI

``` shiki
claude --disallowedTools "Task(Explore)"
```

See [Permissions documentation](/docs/en/permissions#tool-specific-permission-rules) for more details on permission rules.

### 

[​](#define-hooks-for-subagents)

Define hooks for subagents

Subagents can define [hooks](/docs/en/hooks) that run during the subagent’s lifecycle. There are two ways to configure hooks:

1.  **In the subagent’s frontmatter**: Define hooks that run only while that subagent is active
2.  **In `settings.json`**: Define hooks that run in the main session when subagents start or stop

#### 

[​](#hooks-in-subagent-frontmatter)

Hooks in subagent frontmatter

Define hooks directly in the subagent’s markdown file. These hooks only run while that specific subagent is active and are cleaned up when it finishes. All [hook events](/docs/en/hooks#hook-events) are supported. The most common events for subagents are:

| Event | Matcher input | When it fires |
|:---|:---|:---|
| `PreToolUse` | Tool name | Before the subagent uses a tool |
| `PostToolUse` | Tool name | After the subagent uses a tool |
| `Stop` | (none) | When the subagent finishes (converted to `SubagentStop` at runtime) |

This example validates Bash commands with the `PreToolUse` hook and runs a linter after file edits with `PostToolUse`:

Report incorrect code

Copy

Ask AI

``` shiki
---
name: code-reviewer
description: Review code changes with automatic linting
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh $TOOL_INPUT"
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

`Stop` hooks in frontmatter are automatically converted to `SubagentStop` events.

#### 

[​](#project-level-hooks-for-subagent-events)

Project-level hooks for subagent events

Configure hooks in `settings.json` that respond to subagent lifecycle events in the main session.

| Event           | Matcher input   | When it fires                    |
|:----------------|:----------------|:---------------------------------|
| `SubagentStart` | Agent type name | When a subagent begins execution |
| `SubagentStop`  | Agent type name | When a subagent completes        |

Both events support matchers to target specific agent types by name. This example runs a setup script only when the `db-agent` subagent starts, and a cleanup script when any subagent stops:

Report incorrect code

Copy

Ask AI

``` shiki
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "db-agent",
        "hooks": [
          { "type": "command", "command": "./scripts/setup-db-connection.sh" }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          { "type": "command", "command": "./scripts/cleanup-db-connection.sh" }
        ]
      }
    ]
  }
}
```

See [Hooks](/docs/en/hooks) for the complete hook configuration format.

## 

[​](#work-with-subagents)

Work with subagents

### 

[​](#understand-automatic-delegation)

Understand automatic delegation

Claude automatically delegates tasks based on the task description in your request, the `description` field in subagent configurations, and current context. To encourage proactive delegation, include phrases like “use proactively” in your subagent’s description field. You can also request a specific subagent explicitly:

Report incorrect code

Copy

Ask AI

``` shiki
Use the test-runner subagent to fix failing tests
Have the code-reviewer subagent look at my recent changes
```

### 

[​](#run-subagents-in-foreground-or-background)

Run subagents in foreground or background

Subagents can run in the foreground (blocking) or background (concurrent):

- **Foreground subagents** block the main conversation until complete. Permission prompts and clarifying questions (like [`AskUserQuestion`](/docs/en/settings#tools-available-to-claude)) are passed through to you.
- **Background subagents** run concurrently while you continue working. Before launching, Claude Code prompts for any tool permissions the subagent will need, ensuring it has the necessary approvals upfront. Once running, the subagent inherits these permissions and auto-denies anything not pre-approved. If a background subagent needs to ask clarifying questions, that tool call fails but the subagent continues. MCP tools are not available in background subagents.

If a background subagent fails due to missing permissions, you can [resume it](#resume-subagents) in the foreground to retry with interactive prompts. Claude decides whether to run subagents in the foreground or background based on the task. You can also:

- Ask Claude to “run this in the background”
- Press **Ctrl+B** to background a running task

To disable all background task functionality, set the `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to `1`. See [Environment variables](/docs/en/settings#environment-variables).

### 

[​](#common-patterns)

Common patterns

#### 

[​](#isolate-high-volume-operations)

Isolate high-volume operations

One of the most effective uses for subagents is isolating operations that produce large amounts of output. Running tests, fetching documentation, or processing log files can consume significant context. By delegating these to a subagent, the verbose output stays in the subagent’s context while only the relevant summary returns to your main conversation.

Report incorrect code

Copy

Ask AI

``` shiki
Use a subagent to run the test suite and report only the failing tests with their error messages
```

#### 

[​](#run-parallel-research)

Run parallel research

For independent investigations, spawn multiple subagents to work simultaneously:

Report incorrect code

Copy

Ask AI

``` shiki
Research the authentication, database, and API modules in parallel using separate subagents
```

Each subagent explores its area independently, then Claude synthesizes the findings. This works best when the research paths don’t depend on each other.

When subagents complete, their results return to your main conversation. Running many subagents that each return detailed results can consume significant context.

For tasks that need sustained parallelism or exceed your context window, [agent teams](/docs/en/agent-teams) give each worker its own independent context.

#### 

[​](#chain-subagents)

Chain subagents

For multi-step workflows, ask Claude to use subagents in sequence. Each subagent completes its task and returns results to Claude, which then passes relevant context to the next subagent.

Report incorrect code

Copy

Ask AI

``` shiki
Use the code-reviewer subagent to find performance issues, then use the optimizer subagent to fix them
```

### 

[​](#choose-between-subagents-and-main-conversation)

Choose between subagents and main conversation

Use the **main conversation** when:

- The task needs frequent back-and-forth or iterative refinement
- Multiple phases share significant context (planning → implementation → testing)
- You’re making a quick, targeted change
- Latency matters. Subagents start fresh and may need time to gather context

Use **subagents** when:

- The task produces verbose output you don’t need in your main context
- You want to enforce specific tool restrictions or permissions
- The work is self-contained and can return a summary

Consider [Skills](/docs/en/skills) instead when you want reusable prompts or workflows that run in the main conversation context rather than isolated subagent context.

Subagents cannot spawn other subagents. If your workflow requires nested delegation, use [Skills](/docs/en/skills) or [chain subagents](#chain-subagents) from the main conversation.

### 

[​](#manage-subagent-context)

Manage subagent context

#### 

[​](#resume-subagents)

Resume subagents

Each subagent invocation creates a new instance with fresh context. To continue an existing subagent’s work instead of starting over, ask Claude to resume it. Resumed subagents retain their full conversation history, including all previous tool calls, results, and reasoning. The subagent picks up exactly where it stopped rather than starting fresh. When a subagent completes, Claude receives its agent ID. To resume a subagent, ask Claude to continue the previous work:

Report incorrect code

Copy

Ask AI

``` shiki
Use the code-reviewer subagent to review the authentication module
[Agent completes]

Continue that code review and now analyze the authorization logic
[Claude resumes the subagent with full context from previous conversation]
```

You can also ask Claude for the agent ID if you want to reference it explicitly, or find IDs in the transcript files at `~/.claude/projects/{project}/{sessionId}/subagents/`. Each transcript is stored as `agent-{agentId}.jsonl`. Subagent transcripts persist independently of the main conversation:

- **Main conversation compaction**: When the main conversation compacts, subagent transcripts are unaffected. They’re stored in separate files.
- **Session persistence**: Subagent transcripts persist within their session. You can [resume a subagent](#resume-subagents) after restarting Claude Code by resuming the same session.
- **Automatic cleanup**: Transcripts are cleaned up based on the `cleanupPeriodDays` setting (default: 30 days).

#### 

[​](#auto-compaction)

Auto-compaction

Subagents support automatic compaction using the same logic as the main conversation. By default, auto-compaction triggers at approximately 95% capacity. To trigger compaction earlier, set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` to a lower percentage (for example, `50`). See [environment variables](/docs/en/settings#environment-variables) for details. Compaction events are logged in subagent transcript files:

Report incorrect code

Copy

Ask AI

``` shiki
{
  "type": "system",
  "subtype": "compact_boundary",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 167189
  }
}
```

The `preTokens` value shows how many tokens were used before compaction occurred.

## 

[​](#example-subagents)

Example subagents

These examples demonstrate effective patterns for building subagents. Use them as starting points, or generate a customized version with Claude.

**Best practices:**

- **Design focused subagents:** each subagent should excel at one specific task
- **Write detailed descriptions:** Claude uses the description to decide when to delegate
- **Limit tool access:** grant only necessary permissions for security and focus
- **Check into version control:** share project subagents with your team

### 

[​](#code-reviewer)

Code reviewer

A read-only subagent that reviews code without modifying it. This example shows how to design a focused subagent with limited tool access (no Edit or Write) and a detailed prompt that specifies exactly what to look for and how to format output.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is clear and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

### 

[​](#debugger)

Debugger

A subagent that can both analyze and fix issues. Unlike the code reviewer, this one includes Edit because fixing bugs requires modifying code. The prompt provides a clear workflow from diagnosis to verification.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not the symptoms.
```

### 

[​](#data-scientist)

Data scientist

A domain-specific subagent for data analysis work. This example shows how to create subagents for specialized workflows outside of typical coding tasks. It explicitly sets `model: sonnet` for more capable analysis.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
model: sonnet
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```

### 

[​](#database-query-validator)

Database query validator

A subagent that allows Bash access but validates commands to permit only read-only SQL queries. This example shows how to use `PreToolUse` hooks for conditional validation when you need finer control than the `tools` field provides.

Report incorrect code

Copy

Ask AI

``` shiki
---
name: db-reader
description: Execute read-only database queries. Use when analyzing data or generating reports.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

You are a database analyst with read-only access. Execute SELECT queries to answer questions about the data.

When asked to analyze data:
1. Identify which tables contain the relevant data
2. Write efficient SELECT queries with appropriate filters
3. Present results clearly with context

You cannot modify data. If asked to INSERT, UPDATE, DELETE, or modify schema, explain that you only have read access.
```

Claude Code [passes hook input as JSON](/docs/en/hooks#pretooluse-input) via stdin to hook commands. The validation script reads this JSON, extracts the command being executed, and checks it against a list of SQL write operations. If a write operation is detected, the script [exits with code 2](/docs/en/hooks#exit-code-2-behavior-per-event) to block execution and returns an error message to Claude via stderr. Create the validation script anywhere in your project. The path must match the `command` field in your hook configuration:

Report incorrect code

Copy

Ask AI

``` shiki
#!/bin/bash
# Blocks SQL write operations, allows SELECT queries

# Read JSON input from stdin
INPUT=$(cat)

# Extract the command field from tool_input using jq
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [ -z "$COMMAND" ]; then
  exit 0
fi

# Block write operations (case-insensitive)
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|REPLACE|MERGE)\b' > /dev/null; then
  echo "Blocked: Write operations not allowed. Use SELECT queries only." >&2
  exit 2
fi

exit 0
```

Make the script executable:

Report incorrect code

Copy

Ask AI

``` shiki
chmod +x ./scripts/validate-readonly-query.sh
```

The hook receives JSON via stdin with the Bash command in `tool_input.command`. Exit code 2 blocks the operation and feeds the error message back to Claude. See [Hooks](/docs/en/hooks#exit-code-output) for details on exit codes and [Hook input](/docs/en/hooks#pretooluse-input) for the complete input schema.

## 

[​](#next-steps)

Next steps

Now that you understand subagents, explore these related features:

- [Distribute subagents with plugins](/docs/en/plugins) to share subagents across teams or projects
- [Run Claude Code programmatically](/docs/en/headless) with the Agent SDK for CI/CD and automation
- [Use MCP servers](/docs/en/mcp) to give subagents access to external tools and data

Was this page helpful?

Yes

No

[Run agent teams](/docs/en/agent-teams)

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
