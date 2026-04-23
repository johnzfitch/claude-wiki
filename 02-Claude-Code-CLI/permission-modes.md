---
title: "Choose a permission mode"
source_url: "https://code.claude.com/docs/en/permission-modes.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
tags: ["claude-code"]
---

# Choose a permission mode

Control whether Claude asks before editing files or running commands. Cycle modes with Shift+Tab in the CLI or use the mode selector in VS Code, Desktop, and claude.ai.

When Claude wants to edit a file, run a shell command, or make a network request, it pauses and asks you to approve the action. Permission modes control how often that pause happens.

## Available modes

| Mode                | What runs without asking                  | Best for                                |
| :------------------ | :---------------------------------------- | :-------------------------------------- |
| `default`           | Reads only                                | Getting started, sensitive work         |
| `acceptEdits`       | Reads and file edits                      | Iterating on code you're reviewing      |
| `plan`              | Reads only                                | Exploring a codebase before changing it |
| `auto`              | Everything, with background safety checks | Long tasks, reducing prompt fatigue     |
| `dontAsk`           | Only pre-approved tools                   | Locked-down CI and scripts              |
| `bypassPermissions` | Everything except protected paths         | Isolated containers and VMs only        |

Writes to protected paths are never auto-approved in any mode.

## Switch permission modes

### CLI

- **During a session**: press `Shift+Tab` to cycle `default` → `acceptEdits` → `plan`
- **At startup**: `claude --permission-mode plan`
- **As a default**: set `defaultMode` in settings

```json
{
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}
```

### VS Code

Click the mode indicator at the bottom of the prompt box.

| UI label           | Mode                |
| :----------------- | :------------------ |
| Ask before edits   | `default`           |
| Edit automatically | `acceptEdits`       |
| Plan mode          | `plan`              |
| Auto mode          | `auto`              |
| Bypass permissions | `bypassPermissions` |

### Desktop

Use the mode selector next to the send button.

### Web and mobile

Use the mode dropdown next to the prompt box on claude.ai/code.

## acceptEdits mode

Lets Claude create and edit files without prompting. Writes to protected paths and all non-edit actions still prompt. Status bar shows `⏵⏵ accept edits on`.

```bash
claude --permission-mode acceptEdits
```

## Plan mode

Claude researches and proposes changes without making them. Claude reads files and runs shell commands to explore, but does not edit your source.

Enter plan mode by pressing `Shift+Tab` or prefixing a single prompt with `/plan`.

When the plan is ready, Claude presents it and asks how to proceed:

- Approve and start in auto mode
- Approve and accept edits
- Approve and review each edit manually
- Keep planning with feedback
- Refine with Ultraplan for browser-based review

## Auto mode

> Auto mode requires Claude Code v2.1.83 or later.

Auto mode lets Claude execute without permission prompts. A separate classifier model reviews actions before they run.

**Requirements:**

- **Plan**: Team, Enterprise, or API (not Pro or Max)
- **Admin**: must enable in Claude Code admin settings
- **Model**: Claude Sonnet 4.6 or Opus 4.6
- **Provider**: Anthropic API only

```bash
claude --enable-auto-mode
```

### What the classifier blocks by default

**Blocked**: downloading and executing code (`curl | bash`), sending sensitive data externally, production deploys, mass deletion, granting permissions, modifying shared infrastructure, force push to main.

**Allowed**: local file operations, installing dependencies from lock files, reading `.env` and sending credentials to matching APIs, read-only HTTP, pushing to your branch.

### When auto mode falls back

If the classifier blocks an action 3 times consecutively or 20 times total, auto mode pauses and resumes prompting. Approving the prompted action resumes auto mode.

## dontAsk mode

Auto-denies every tool not explicitly allowed. Only `permissions.allow` rules can execute.

```bash
claude --permission-mode dontAsk
```

## bypassPermissions mode

Disables permission prompts and safety checks. Writes to protected paths are the only actions that still prompt. Only use in isolated environments (containers, VMs, devcontainers).

```bash
claude --permission-mode bypassPermissions
```

## Protected paths

Writes to these paths are never auto-approved:

**Directories**: `.git`, `.vscode`, `.idea`, `.husky`, `.claude` (except `.claude/commands`, `.claude/agents`, `.claude/skills`, `.claude/worktrees`)

**Files**: `.gitconfig`, `.gitmodules`, `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`, `.ripgreprc`, `.mcp.json`, `.claude.json`

## See Also

- [Permissions](/en/permissions) — allow, ask, deny rules
- [Hooks](../07-Hooks/hooks-reference-claude-code-docs.md) — custom permission logic
- [Ultraplan](ultraplan.md) — plan mode with browser-based review
- [Security](security-claude-code-docs.md)
- [Sandboxing](/en/sandboxing)
