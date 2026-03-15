---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-15T12:17:19Z"
source_url: "https://code.claude.com/docs/en/tools-reference"
title: "Tools reference - Claude Code Docs"
---

# Tools reference


Complete reference for the tools Claude Code can use, including permission requirements.


Claude Code has access to a set of tools that help it understand and modify your codebase. The tool names below are the exact strings you use in [permission rules](/docs/en/permissions#tool-specific-permission-rules), [subagent tool lists](/docs/en/sub-agents), and [hook matchers](/docs/en/hooks).

| Tool | Description | Permission Required |
|:---|:---|:---|
| `Agent` | Spawns a [subagent](/docs/en/sub-agents) with its own context window to handle a task | No |
| `AskUserQuestion` | Asks multiple-choice questions to gather requirements or clarify ambiguity | No |
| `Bash` | Executes shell commands in your environment. See [Bash tool behavior](#bash-tool-behavior) | Yes |
| `CronCreate` | Schedules a recurring or one-shot prompt within the current session (gone when Claude exits). See [scheduled tasks](/docs/en/scheduled-tasks) | No |
| `CronDelete` | Cancels a scheduled task by ID | No |
| `CronList` | Lists all scheduled tasks in the session | No |
| `Edit` | Makes targeted edits to specific files | Yes |
| `EnterPlanMode` | Switches to plan mode to design an approach before coding | No |
| `EnterWorktree` | Creates an isolated [git worktree](/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) and switches into it | No |
| `ExitPlanMode` | Presents a plan for approval and exits plan mode | Yes |
| `ExitWorktree` | Exits a worktree session and returns to the original directory | No |
| `Glob` | Finds files based on pattern matching | No |
| `Grep` | Searches for patterns in file contents | No |
| `ListMcpResourcesTool` | Lists resources exposed by connected [MCP servers](/docs/en/mcp) | No |
| `LSP` | Code intelligence via language servers. Reports type errors and warnings automatically after file edits. Also supports navigation operations: jump to definitions, find references, get type info, list symbols, find implementations, trace call hierarchies. Requires a [code intelligence plugin](/docs/en/discover-plugins#code-intelligence) and its language server binary | No |
| `NotebookEdit` | Modifies Jupyter notebook cells | Yes |
| `Read` | Reads the contents of files | No |
| `ReadMcpResourceTool` | Reads a specific MCP resource by URI | No |
| `Skill` | Executes a [skill](/docs/en/skills#control-who-invokes-a-skill) within the main conversation | Yes |
| `TaskCreate` | Creates a new task in the task list | No |
| `TaskGet` | Retrieves full details for a specific task | No |
| `TaskList` | Lists all tasks with their current status | No |
| `TaskOutput` | Retrieves output from a background task | No |
| `TaskStop` | Kills a running background task by ID | No |
| `TaskUpdate` | Updates task status, dependencies, details, or deletes tasks | No |
| `TodoWrite` | Manages the session task checklist. Available in non-interactive mode and the [Agent SDK](/docs/en/headless); interactive sessions use TaskCreate, TaskGet, TaskList, and TaskUpdate instead | No |
| `ToolSearch` | Searches for and loads deferred tools when [tool search](/docs/en/mcp#scale-with-mcp-tool-search) is enabled | No |
| `WebFetch` | Fetches content from a specified URL | Yes |
| `WebSearch` | Performs web searches | Yes |
| `Write` | Creates or overwrites files | Yes |

Permission rules can be configured using `/permissions` or in [permission settings](/docs/en/settings#available-settings). Also see [Tool-specific permission rules](/docs/en/permissions#tool-specific-permission-rules).

## 

[​](#bash-tool-behavior)

Bash tool behavior

The Bash tool runs each command in a separate process with the following persistence behavior:

- Working directory persists across commands. Set `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` to reset to the project directory after each command.
- Environment variables do not persist. An `export` in one command will not be available in the next.

Activate your virtualenv or conda environment before launching Claude Code. To make environment variables persist across Bash commands, set [`CLAUDE_ENV_FILE`](/docs/en/env-vars) to a shell script before launching Claude Code, or use a [SessionStart hook](/docs/en/hooks#persist-environment-variables) to populate it dynamically.

## 

[​](#see-also)

See also

- [Permissions](/docs/en/permissions): permission system, rule syntax, and tool-specific patterns
- [Subagents](/docs/en/sub-agents): configure tool access for subagents
- [Hooks](/docs/en/hooks-guide): run custom commands before or after tool execution
