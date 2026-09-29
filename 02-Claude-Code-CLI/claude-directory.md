---
title: "Explore the .claude directory - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/claude-directory"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-26T06:38:04Z"
tags: ["claude-code"]
---

# Explore the .claude directory

Copy pageCopy page

Where Claude Code reads CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules, and auto memory. Explore the .claude directory in your project and ~/.claude in your home directory.

Copy pageCopy page

Claude Code reads instructions, settings, skills, subagents, and memory from your project directory and from `~/.claude` in your home directory. Commit project files to git to share them with your team; files in `~/.claude` are personal configuration that applies across all your projects. On Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`. If you set [`CLAUDE_CONFIG_DIR`](env-vars.md), every `~/.claude` path on this page lives under that directory instead. Most users only edit `CLAUDE.md` and `settings.json`. If your repository already has an `AGENTS.md` for other coding agents, Claude Code [can read that](memory.md#agents-md) on its own or alongside `CLAUDE.md`. The rest of the directory is optional: add skills, rules, or subagents as you need them.


[​](#explore-the-directory)

Explore the directory

Click files in the tree to see what each one does, when it loads, and an example.


[​](#what’s-not-shown)

What’s not shown

The explorer covers files you author and edit. A few related files live elsewhere:

| File                    | Location                                   | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `managed-settings.json` | System-level, varies by OS                 | Enterprise-enforced settings that you can’t override, apart from [narrow exceptions](settings.md#security-keys-where-the-stricter-value-applies). See [where to save the file](../13-Enterprise-Admin/managed-settings.md#deploy-a-managed-settings-file) and [which managed source Claude Code uses](../13-Enterprise-Admin/managed-settings.md#precedence-within-the-managed-tier).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `CLAUDE.local.md`       | Project root                               | Your private preferences for this project, loaded alongside CLAUDE.md. Create it manually and add it to `.gitignore`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `AGENTS.md`             | Project root, `.claude/`, or any directory | Project instructions you write for AI coding agents. Claude Code can [load it](memory.md#agents-md) on its own or alongside `CLAUDE.md`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Installed plugins       | `~/.claude/plugins`                        | Cloned marketplaces, installed plugin versions, the `installed_plugins.json` install record, and per-plugin data, managed by `claude plugin` commands. Plugins [synced from your claude.ai account](../08-Plugins-Skills/plugins-loading.md#synced-plugins) download into `~/.claude/plugins/synced/`. For a plugin installed from a marketplace [`command` source](../08-Plugins-Skills/plugins-marketplace-reference.md#command-plugin-source) in link mode, Claude Code stores links here instead of a copy, and the plugin’s files stay in the directory the command prints. A `command` source requires Claude Code v2.1.229 or later. A plugin listed by relative path in a local-directory marketplace also [loads in place](../08-Plugins-Skills/plugins-loading.md#find-plugins-on-disk) from its source directory rather than from a cache copy. See [plugin caching](../08-Plugins-Skills/plugins-loading.md#find-plugins-on-disk) for how orphaned versions are cleaned up. |

`~/.claude` also holds data Claude Code writes as you work: transcripts, prompt history, file snapshots, caches, and logs. See [application data](#application-data) below.


[​](#choose-the-right-file)

Choose the right file

Different kinds of customization live in different files. Use this table to find where a change belongs.

| You want to                                        | Edit                                     | Scope             | Reference                                                    |
|:---------------------------------------------------|:-----------------------------------------|:------------------|:-------------------------------------------------------------|
| Give Claude project context and conventions        | `CLAUDE.md`                              | project or global | [Memory](memory.md)                                    |
| Allow or block specific tool calls                 | `settings.json` `permissions` or `hooks` | project or global | [Permissions](permissions.md), [Hooks](../07-Hooks/hooks.md) |
| Run a script before or after tool calls            | `settings.json` `hooks`                  | project or global | [Hooks](../07-Hooks/hooks.md)                                      |
| Set environment variables for the session          | `settings.json` `env`                    | project or global | [Settings](settings-reference.md#all-settings)         |
| Keep personal overrides out of git                 | `settings.local.json`                    | project only      | [Settings scopes](settings.md#where-settings-live)     |
| Add a prompt or capability you invoke with `/name` | `skills/<name>/SKILL.md`                 | project or global | [Skills](../08-Plugins-Skills/skills.md)                                    |
| Define a specialized subagent with its own tools   | `agents/*.md`                            | project or global | [Subagents](../09-Agents-Patterns/sub-agents.md)                             |
| Orchestrate many subagents from a script           | `workflows/*.js`                         | project or global | [Dynamic workflows](workflows.md)                      |
| Connect external tools over MCP                    | `.mcp.json`                              | project only      | [MCP](../06-MCP-Tools/General/mcp.md)                                          |
| Change how Claude formats responses                | `output-styles/*.md`                     | project or global | [Output styles](output-styles.md)                      |


[​](#file-reference)

File reference

This table lists every file the explorer covers. Project-scope files live in your repo under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`). Global-scope files live in `~/.claude/` and apply across all projects.

Several things can override what you put in these files:

- [Managed settings](../13-Enterprise-Admin/server-managed-settings.md) deployed by your organization take precedence over everything, apart from the [exceptions under Settings precedence](settings.md#exceptions-to-managed-settings-precedence)
- CLI flags like `--permission-mode` or `--settings` override `settings.json` for that session
- Some environment variables take precedence over their equivalent setting, but this varies: check the [environment variables reference](env-vars.md) for each one

See [settings precedence](settings.md#settings-precedence) for the full order.

Click a filename to open that node in the explorer above.

| File                                                | Scope              | Commit | What it does                                                                                                  | Reference                                                            |
|-----------------------------------------------------|--------------------|--------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [`CLAUDE.md`](#ce-claude-md)                        | Project and global | ✓      | Instructions loaded every session                                                                             | [Memory](memory.md)                                            |
| [`rules/*.md`](#ce-rules)                           | Project and global | ✓      | Topic-scoped instructions, optionally path-gated                                                              | [Rules](memory.md#organize-rules-with-claude/rules/)           |
| [`settings.json`](#ce-settings-json)                | Project and global | ✓      | Permissions, hooks, env vars, model defaults                                                                  | [Settings](settings.md)                                        |
| [`settings.local.json`](#ce-settings-local-json)    | Project only       |        | Your personal overrides, gitignored when Claude Code saves a setting to it                                    | [Settings scopes](settings.md#where-settings-live)             |
| [`.mcp.json`](#ce-mcp-json)                         | Project only       | ✓      | Team-shared MCP servers                                                                                       | [MCP scopes](../06-MCP-Tools/General/mcp.md#mcp-installation-scopes)                   |
| [`.worktreeinclude`](#ce-worktreeinclude)           | Project only       | ✓      | Gitignored files to copy into new worktrees                                                                   | [Worktrees](worktrees.md#copy-gitignored-files-into-worktrees) |
| [`skills/<name>/SKILL.md`](#ce-skills)              | Project and global | ✓      | Reusable prompts invoked with `/name` or auto-invoked                                                         | [Skills](../08-Plugins-Skills/skills.md)                                            |
| [`commands/*.md`](#ce-commands)                     | Project and global | ✓      | Single-file prompts; same mechanism as skills                                                                 | [Skills](../08-Plugins-Skills/skills.md)                                            |
| [`output-styles/*.md`](#ce-output-styles)           | Project and global | ✓      | Custom instruction sets that adjust how Claude works                                                          | [Output styles](output-styles.md)                              |
| [`agents/*.md`](#ce-agents)                         | Project and global | ✓      | Subagent definitions with their own prompt and tools                                                          | [Subagents](../09-Agents-Patterns/sub-agents.md)                                     |
| [`workflows/*.js`](#ce-workflows)                   | Project and global | ✓      | Dynamic workflow scripts written by Claude and saved from `/workflows`; each file becomes a `/<name>` command | [Dynamic workflows](workflows.md)                              |
| [`agent-memory/<name>/`](#ce-agent-memory)          | Project and global | ✓      | Persistent memory for subagents                                                                               | [Persistent memory](../09-Agents-Patterns/sub-agents.md#enable-persistent-memory)    |
| [`~/.claude.json`](#ce-claude-json)                 | Global only        |        | App state, OAuth, UI toggles, personal MCP servers                                                            | [Global config](settings-reference.md#global-config-settings)  |
| [`projects/<project>/memory/`](#ce-global-projects) | Global only        |        | Auto memory: Claude’s notes to itself across sessions                                                         | [Auto memory](memory.md#auto-memory)                           |
| [`keybindings.json`](#ce-keybindings)               | Global only        |        | Custom keyboard shortcuts                                                                                     | [Keybindings](keybindings.md)                                  |
| [`themes/*.json`](#ce-themes)                       | Global only        |        | Custom color themes                                                                                           | [Custom themes](terminal-config.md#create-a-custom-theme)      |


[​](#frontmatter-fields-by-file)

Frontmatter fields by file

Skills, command files, subagents, output styles, and rules read their configuration from YAML [frontmatter](glossary.md#frontmatter) at the top of the file, and each accepts its own set of fields. This table lists the field names for each file and links to the reference that describes them.

| File                     | Frontmatter fields                                                                                                                                                                                                                                                            | Reference                                                                |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `skills/<name>/SKILL.md` | `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility` | [Skill frontmatter](../08-Plugins-Skills/skills.md#frontmatter-reference)               |
| `commands/*.md`          | The skill fields except `name` and `paths`                                                                                                                                                                                                                                    | [Skill frontmatter](../08-Plugins-Skills/skills.md#frontmatter-reference)               |
| `agents/*.md`            | `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`, `initialPrompt`, `omitClaudeMd`, `experimental`                                            | [Subagent frontmatter](../09-Agents-Patterns/sub-agents.md#supported-frontmatter-fields) |
| `output-styles/*.md`     | `name`, `description`, `keep-coding-instructions`, `force-for-plugin`                                                                                                                                                                                                         | [Output style frontmatter](output-styles.md#frontmatter)           |
| `rules/*.md`             | `paths`                                                                                                                                                                                                                                                                       | [Rule frontmatter](memory.md#rules-frontmatter-reference)          |

Agents shipped in a [plugin](../08-Plugins-Skills/plugins-components.md#agents) honor a subset of the subagent fields.


[​](#troubleshoot-configuration)

Troubleshoot configuration

If a setting, hook, or file isn’t taking effect, see [Debug your configuration](debug-your-config.md) for the inspection commands and a symptom-first lookup table.


[​](#application-data)

Application data

Beyond the config you author, `~/.claude` holds data Claude Code writes during sessions. These files are plaintext. Anything that passes through a tool is written to a transcript on disk: file contents, command output, pasted text.


[​](#cleaned-up-automatically)

Cleaned up automatically

Claude Code deletes the files in the paths below once they’re older than [`cleanupPeriodDays`](settings-reference.md#cleanupperioddays), as long as it can safely determine the retention period. The default is 30 days and the minimum is 1; setting `0` fails with a validation error. The same age cutoff applies to automatic removal of [orphaned worktrees](worktrees.md#clean-up-subagent-and-background-session-worktrees).

| Path under `~/.claude/`                                                                                                         | Contents                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `projects/<project>/<session>.jsonl`                                                                                            | Full conversation transcript: every message, tool call, and tool result                                                                                                                                                                                                                                                                      |
| `projects/<project>/<session>.orphaned-<timestamp>-<suffix>.jsonl`, `projects/<project>/<session>.jsonl.superseded-<timestamp>` | A previous transcript for the session that Claude Code set aside instead of overwriting or deleting it. It doesn’t appear in the session picker                                                                                                                                                                                              |
| `projects/<project>/<session>/subagents/`                                                                                       | [Subagent](../09-Agents-Patterns/sub-agents.md) conversation transcripts, removed with the parent session transcript when it ages out                                                                                                                                                                                                                        |
| `projects/<project>/<session>/tool-results/`                                                                                    | Large tool outputs spilled to separate files, and full-size copies of [images that MCP tools return](../06-MCP-Tools/General/mcp.md#images-in-tool-results)                                                                                                                                                                                                    |
| `file-history/<session>/`                                                                                                       | Pre-edit snapshots of files Claude changed, used for [checkpoint restore](checkpointing.md). Holds snapshots for the 100 most recent checkpoints; snapshot files that no retained checkpoint references are deleted, except each file’s first snapshot                                                                                 |
| `plans/`                                                                                                                        | Plan files written during [plan mode](permission-modes.md#analyze-before-you-edit-with-plan-mode)                                                                                                                                                                                                                                      |
| `debug/`                                                                                                                        | Per-session debug logs, written while debug logging is on, such as when you start with [`--debug`](cli-reference.md#cli-flags) or run `/debug`                                                                                                                                                                                         |
| `paste-cache/`                                                                                                                  | Contents of large pastes                                                                                                                                                                                                                                                                                                                     |
| `image-cache/<session>/`                                                                                                        | Attached images saved by Claude Code v2.1.274 and earlier. Later versions save pasted and attached images outside `~/.claude`, in an `images/` directory for each session under the temp directory that [`CLAUDE_CODE_TMPDIR`](env-vars.md) controls. The sweep removes other sessions’ leftover directories here, whatever their age. |
| `uploads/<session>/`                                                                                                            | Files you attach from the web or mobile app, and photos you attach from the mobile app, when messaging a [Remote Control](remote-control.md) session. An attachment to a [cloud session](claude-code-on-the-web.md) is saved in that session’s own cloud environment instead, not on your machine.                               |
| `session-env/`                                                                                                                  | Per-session environment metadata                                                                                                                                                                                                                                                                                                             |
| `tasks/`                                                                                                                        | Task lists written by the task tools, one directory per list                                                                                                                                                                                                                                                                                 |
| `shell-snapshots/`                                                                                                              | Aliases, functions, and shell options captured at startup and applied by the [Bash tool](tools-reference.md#bash-tool-behavior) to each command. Removed on clean exit. The sweep clears any left after a crash.                                                                                                                       |
| `backups/`                                                                                                                      | Earlier versions of `~/.claude.json`, copied when Claude Code rewrites the file. Claude Code keeps the five newest, plus a copy of any version it couldn’t parse.                                                                                                                                                                            |
| `feedback-bundles/`                                                                                                             | Redacted transcript archives written by `/feedback` on third-party providers or when no Anthropic credentials are configured, for sending to your Anthropic account team                                                                                                                                                                     |
| `feedback/drafts/`                                                                                                              | Queued [Claude-drafted feedback](tools-reference.md#sendfeedback-tool-behavior) awaiting your review in `/feedback`. Swept after `cleanupPeriodDays` or 30 days, whichever is shorter. When the queue is at its 10-draft limit, Claude Code deletes the oldest draft to make room.                                                     |
| `usage-data/`                                                                                                                   | `report.html` and timestamped report copies written by [`/insights`](../17-Billing-Plans/costs.md#analyze-your-usage-patterns), plus cached per-session analysis data used to build them                                                                                                                                                                   |
| `skills/.trash/`, `plugins/.trash/`                                                                                             | [Skills](../08-Plugins-Skills/skills.md#how-synced-skills-behave) and [plugins](../08-Plugins-Skills/plugins-loading.md#synced-plugins) that the claude.ai sync removed, such as after you turn one off on claude.ai or stop syncing. The files stay here so you can recover them until the sweep deletes them                                                             |
| `todos/`, `statsig/`, `logs/`                                                                                                   | Legacy directories from older versions. No longer written. The sweep removes their contents and then the empty directory.                                                                                                                                                                                                                    |

Session files in `sessions/`, auto memory, and Claude Desktop and Cowork transcripts each follow their own retention rule:

- **`sessions/`**: holds one small file per running session, used to detect concurrent sessions and crashes. It isn’t part of the age-based sweep: Claude Code removes each file when its session exits and clears crash leftovers on the next launch.
- **Auto memory**: the sweep doesn’t delete the memory files in a project’s [auto memory](memory.md#auto-memory) directory, `projects/<project>/memory/`. Claude Code removes that directory only if it has been empty for the whole retention period. Before v2.1.228, the sweep treated folders inside the memory directory as session data and could delete old files beneath it.
- **Claude Desktop and Cowork transcripts**: Claude Code keeps the transcript of a session you started or most recently continued in Claude Desktop or Cowork at any age. To give these transcripts an age limit, set [`desktopSessionCleanupPeriodDays`](settings-reference.md#desktopsessioncleanupperioddays). When [managed settings](../13-Enterprise-Admin/managed-settings.md) set `cleanupPeriodDays`, Claude Code deletes these transcripts after that period instead. Requires Claude Code v2.1.248 or later; earlier versions delete them after `cleanupPeriodDays`.

Claude Code skips the age-based sweep in these cases:

- **Bare mode**: when you run `claude -p` with [`--bare`](headless.md#start-faster-with-bare-mode), Claude Code doesn’t run the sweep in that session.
- **Paused sweep**: if Claude Code can’t safely determine the retention period, it pauses the retention cleanup sweep; the [`retention_sweep` event](../13-Enterprise-Admin/monitoring-usage.md#retention-sweep-event) lists each configuration that pauses it. When the cause is a settings file that can’t be read or parsed, or settings errors with `cleanupPeriodDays` or `desktopSessionCleanupPeriodDays` explicitly set, Claude Code also shows a warning in `/status` until you fix the settings errors. When [managed settings](../13-Enterprise-Admin/server-managed-settings.md) provide `cleanupPeriodDays`, Claude Code runs the sweep at the managed value in either case.


[​](#session-scratchpad-directory)

Session scratchpad directory

The scratchpad is a per-session directory that Claude Code gives Claude for temporary files: intermediate results, helper scripts, and drafts that don’t belong in your project. When Claude says it saved something “to the scratchpad”, the file is there. Claude uses it instead of `/tmp`, and can create, edit, and read files in it without a permission prompt. The scratchpad lives under Claude Code’s temp directory rather than `~/.claude`. Find the current session’s path for your platform:

- **macOS**: `/private/tmp/claude-<uid>/<project>/<session-id>/scratchpad/`
- **Linux**: `/tmp/claude-<uid>/<project>/<session-id>/scratchpad/`, or the same shape under `$TMPDIR` when your system sets one
- **Windows**: `%TEMP%\claude\<project>\<session-id>\scratchpad\`

`<project>` is your working directory path with every character other than letters and digits replaced by `-`, such as `-Users-you-my-project`. If you set [`CLAUDE_CODE_TMPDIR`](env-vars.md), the tree moves under that directory instead. Hooks receive the current session’s path as [`scratchpad_dir`](../07-Hooks/hooks.md#common-input-fields). Scratchpad files last as long as the session’s transcript: the [retention sweep](#cleaned-up-automatically) deletes the directory when it deletes the transcript, and [`claude project purge`](#clear-local-data) doesn’t touch the temp directory. Because the directory sits under the system temp location, your operating system can also clear it, such as on restart. To keep something Claude wrote there, ask Claude to move it into your project. A session has a scratchpad only when all of these hold:

- You’re signed in with a claude.ai account rather than an API key
- The session uses the Anthropic API, not Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry
- [`enableArtifact`](settings-reference.md#enableartifact) isn’t set to `false`


[​](#kept-until-you-delete-them)

Kept until you delete them

The retention cleanup sweep doesn’t remove the paths below. Claude Code keeps them until you delete them, apart from the two caches it deletes when you log out.

| Path under `~/.claude/` | Contents                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `history.jsonl`         | Every prompt you’ve typed, with timestamp and project path. Used for up-arrow recall, `Ctrl+R` history search, and `!` shell-command completion.                                                                                                                                                                                                                            |
| `stats-cache.json`      | Aggregated token and cost counts shown by `/usage`                                                                                                                                                                                                                                                                                                                          |
| `remote-settings.json`  | Cached copy of [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md) for your organization, or `{}` when your organization has configured none. Only present when the session [fetches them](../13-Enterprise-Admin/server-managed-settings.md#platform-availability). Claude Code checks for updates at startup and hourly during a session. Claude Code deletes it when you log out. |
| `cache/changelog.md`    | Cached copy of the Claude Code changelog, shown by `/release-notes`. Refreshed in the background.                                                                                                                                                                                                                                                                           |
| `policy-limits.json`    | Cached feature policy settings for your organization. Only present for some account types. Refreshed automatically. A `policy-limits.json.stamp.json` sidecar records which account or API key the cache belongs to. Claude Code deletes both files when you log out.                                                                                                       |

Other files appear depending on which features you use. Caches and lock files are safe to delete. Keep these state files:

- `.credentials.json`: your [login credentials](../13-Enterprise-Admin/iam.md#credential-management)
- `agent-memory/`: [subagent memory](../09-Agents-Patterns/sub-agents.md#enable-persistent-memory)
- `jobs/` and `daemon/`: [background session](../09-Agents-Patterns/agent-view.md#where-state-is-stored) state


[​](#plaintext-storage)

Plaintext storage

Transcripts and history are not encrypted at rest. OS file permissions are the only protection. If a tool reads a `.env` file or a command prints a credential, that value is written to `projects/<project>/<session>.jsonl`. To reduce exposure:

- Lower `cleanupPeriodDays` to shorten how long Claude Code keeps transcripts
- Set [`desktopSessionCleanupPeriodDays`](settings-reference.md#desktopsessioncleanupperioddays) to give Claude Desktop and Cowork transcripts an age limit too
- Set the [`CLAUDE_CODE_SKIP_PROMPT_HISTORY`](env-vars.md) environment variable to skip writing transcripts and prompt history in any mode. In non-interactive mode, you can instead pass `--no-session-persistence` alongside `-p`, or set `persistSession: false` in the TypeScript Agent SDK; the Python SDK has no equivalent option.
- Use [permission rules](permissions.md) to deny reads of credential files


[​](#clear-local-data)

Clear local data

Run `claude project purge` to delete the state Claude Code holds for one project. It deletes:

- Transcripts and auto memory under `projects/`
- Per-session `tasks/`, `debug/`, and `file-history/` entries
- Matching prompt lines in `history.jsonl`
- The project’s entry in `~/.claude.json`

Images you pasted or attached in the project’s sessions and each session’s [scratchpad](#session-scratchpad-directory) are stored under Claude Code’s temp directory rather than `~/.claude`, so the purge doesn’t remove them. The [retention sweep](#cleaned-up-automatically) still deletes the images once they’re older than `cleanupPeriodDays`; a purged session’s scratchpad stays until you delete it or your operating system clears the temp directory. The command prints the full deletion plan and asks for confirmation before removing anything. The examples below use `~/work/my-repo` as a placeholder. Replace it with the path to your project. If no state matches the path, the command prints an error and exits with status 1. Preview the plan without deleting anything:

```python
claude project purge ~/work/my-repo --dry-run
```

The plan lists each matching item and why it is included:

```python
Purge plan for /home/user/work/my-repo:

  dir:    /home/user/.claude/projects/-home-user-work-my-repo
           project transcripts (.jsonl) and memory/
  config: projects["/home/user/work/my-repo"]
           project entry in ~/.claude.json (trust, history, MCP servers)
  filter: /home/user/.claude/history.jsonl
           12 prompt(s) typed in this project

shell-snapshots/ are not project-scoped and will not be touched
backups/ may still contain this project entry in old .claude.json snapshots (/home/user/.claude/backups); at most 5 are kept and they rotate out automatically
Dry run: 3 item(s) would be deleted.
```

Delete with a single confirmation prompt:

```python
claude project purge ~/work/my-repo
```

The command prints the same plan, then asks `Delete 3 item(s) for /home/user/work/my-repo? This cannot be undone. [y/N]` and deletes only if you answer `y`. Omit the path to pick a project from an interactive list. Skip the confirmation prompt for use in scripts:

```python
claude project purge ~/work/my-repo --yes
```

Pass `--all` instead of a path to purge state for every project at once, which deletes `history.jsonl` outright rather than filtering it. Pass `-i` to step through the deletion plan one item at a time. The command leaves `shell-snapshots/` and `backups/` alone because those are not project-scoped, and warns about them in the plan output. You can also delete any of the application-data paths above by hand, apart from the [state files to keep](#state-files-to-keep). New sessions are unaffected. The table below shows what you lose for past sessions.

| Delete                                                                                                               | You lose                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `~/.claude/projects/`                                                                                                | Resume, continue, and rewind for past sessions, and auto memory for every project                                                                                      |
| `~/.claude/history.jsonl`                                                                                            | Up-arrow prompt recall, `Ctrl+R` history search, and `!` shell-command completion                                                                                      |
| `~/.claude/paste-cache/`                                                                                             | Pasted text in recalled prompts; see [paste large content](terminal-config.md#paste-large-content)                                                               |
| `~/.claude/uploads/`                                                                                                 | Attachments that past [Remote Control](remote-control.md) sessions refer to by path                                                                              |
| `~/.claude/file-history/`                                                                                            | Checkpoint restore for past sessions                                                                                                                                   |
| `~/.claude/stats-cache.json`                                                                                         | Historical totals shown by `/usage`                                                                                                                                    |
| `~/.claude/usage-data/`                                                                                              | Past [`/insights`](../17-Billing-Plans/costs.md#analyze-your-usage-patterns) reports and the cached analysis data used to build them                                                 |
| `~/.claude/feedback-bundles/`                                                                                        | Feedback and bug-report archives you haven’t yet sent to your Anthropic account team                                                                                   |
| `~/.claude/feedback/drafts/`                                                                                         | [Claude-drafted feedback](tools-reference.md#sendfeedback-tool-behavior) you haven’t sent                                                                        |
| `~/.claude/remote-settings.json`                                                                                     | Nothing. Re-fetched on next launch.                                                                                                                                    |
| `~/.claude/cache/changelog.md`                                                                                       | Nothing. Refreshed in the background.                                                                                                                                  |
| `~/.claude/policy-limits.json`                                                                                       | Nothing. Refreshed automatically.                                                                                                                                      |
| `~/.claude/tasks/`                                                                                                   | Task lists that a resumed session would pick up                                                                                                                        |
| `~/.claude/skills/.trash/`, `~/.claude/plugins/.trash/`                                                              | The chance to recover [synced skills](../08-Plugins-Skills/skills.md#how-synced-skills-behave) and [synced plugins](../08-Plugins-Skills/plugins-loading.md#synced-plugins) that Claude Code removed |
| `~/.claude/debug/`, `~/.claude/plans/`, `~/.claude/session-env/`, `~/.claude/shell-snapshots/`, `~/.claude/backups/` | Nothing user-facing                                                                                                                                                    |
| `~/.claude/todos/`, `~/.claude/statsig/`, `~/.claude/logs/`, `~/.claude/image-cache/`                                | Nothing. Legacy directories not written by current versions.                                                                                                           |

Don’t delete `~/.claude.json`, `~/.claude/settings.json`, or `~/.claude/plugins/`: those hold your auth, preferences, and installed plugins.


[​](#related-resources)

Related resources

- [Manage Claude’s memory](memory.md): write and organize CLAUDE.md, rules, and auto memory
- [Configure settings](settings.md): set permissions, hooks, environment variables, and model defaults
- [Create skills](../08-Plugins-Skills/skills.md): build reusable prompts and workflows
- [Configure subagents](../09-Agents-Patterns/sub-agents.md): define specialized agents with their own context
