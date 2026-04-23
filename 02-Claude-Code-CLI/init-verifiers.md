---
title: "`/init-verifiers` -- Automated Verifier Skill Scaffolding"
category: "02-Claude-Code-CLI"
tags: ["agents", "authentication", "claude-code"]
---

# `/init-verifiers` -- Automated Verifier Skill Scaffolding

Bundled skill that creates `.claude/skills/verifier-*/SKILL.md` files so the **Verify
agent** can automatically test code changes after each edit cycle.

Explicitly avoids unit tests and typechecking ("already handled by the standard build/test
workflow"). Focuses only on **functional verification**: web UI, CLI, and API.

---

## 5-Phase Wizard

### Phase 1: Auto-Detection

Scans the project structure for distinct application areas. Looks at `package.json`,
`Cargo.toml`, `pyproject.toml`, `go.mod` in subdirectories. Classifies each into:

| Detected Type | Suggested Verifier |
|---------------|-------------------|
| Web app (React, Next.js, Vue) | Playwright-based |
| CLI tool | Tmux-based |
| API service (Express, FastAPI) | HTTP/curl-based |

Also checks for existing E2E tools (Playwright, Cypress) and MCP browser automation
configs in `.mcp.json` (Playwright MCP, Chrome DevTools MCP, Claude Chrome Extension).

### Phase 2: Verification Tool Setup

For web apps without browser automation detected, uses `AskUserQuestion` to offer:

| Option | What Happens |
|--------|-------------|
| **Playwright** (recommended) | `npm install -D @playwright/test && npx playwright install` |
| **Chrome DevTools MCP** | Configures MCP server entry in `.mcp.json` |
| **Claude Chrome Extension** | Uses `mcp__claude-in-chrome__*` tools (requires extension) |
| **None** | Falls back to HTTP-only checks |

For CLI tools: checks for `asciinema` and `tmux` availability.
For APIs: checks for `curl` / `httpie` (usually pre-installed).

### Phase 3: Interactive Q&A

Asks project-specific questions via `AskUserQuestion`:

**Verifier naming convention:**
- Single project: `verifier-playwright`, `verifier-cli`, `verifier-api`
- Multi-project: `verifier-frontend-playwright`, `verifier-backend-api`
- Name MUST contain "verifier" for auto-discovery by the Verify agent

**Per-type questions:**

| Type | Questions Asked |
|------|---------------|
| Web app | Dev server command, URL, ready signal text |
| CLI | Entry point command, asciinema recording preference |
| API | Server command, base URL |

**Authentication (web + API):**
- Whether login is required (none / required / partial)
- Login method: form-based, API key, OAuth/SSO
- Test credentials (suggests env vars like `$TEST_USER`, `$TEST_PASSWORD`)
- Post-login indicator: URL redirect, element appears, cookie set

### Phase 4: Generate Skill File

Writes to `.claude/skills/<verifier-name>/SKILL.md` with YAML frontmatter:

```markdown
---
name: <verifier-name>
description: <description based on type>
allowed-tools:
  # Per-type tool permissions (see below)
---

# <Verifier Title>

You are a verification executor. You receive a verification plan
and execute it EXACTLY as written.

## Project Context
<from auto-detection>

## Setup Instructions
<how to start services>

## Authentication
<login steps if needed, or omitted>

## Reporting
<PASS/FAIL format per step>

## Cleanup
<stop servers, close browsers>
```

**Allowed tools per verifier type:**

```
verifier-playwright:
  - Bash(npm:*)
  - Bash(yarn:*)
  - Bash(pnpm:*)
  - Bash(bun:*)
  - mcp__playwright__*
  - Read, Glob, Grep

verifier-cli:
  - Tmux
  - Bash(asciinema:*)
  - Read, Glob, Grep

verifier-api:
  - Bash(curl:*)
  - Bash(http:*)
  - Bash(npm:*)
  - Bash(yarn:*)
  - Read, Glob, Grep
```

### Phase 5: Confirm Creation

Reports to user:
1. Where each skill was created (always `.claude/skills/`)
2. Auto-discovery rule: folder name must contain "verifier" (case-insensitive)
3. Skills are editable and `/init-verifiers` can be re-run for more areas

---

## The Verify Agent

A separate bundled skill (~3000 chars) that consumes the verifier skills created above.
Registered via `XW()` with `name: "verify"`.

### Verify Agent Workflow

```
git status / git diff
       |
       v
Discover verifier skills (folder name contains "verifier")
       |
       v
Match changed files -> appropriate verifier (by description)
       |
       v
Create verification plan at ~/.claude/plans/<slug>.md
       |
       v
Trigger each verifier skill via Skill tool (sequentially)
       |
       v
Report PASS/FAIL inline
```

### Verification Plan Format

Plans are written to `~/.claude/plans/<slug>.md`:

```markdown
# Verification Plan

## Metadata
- **Verifier Skills**: <list>
- **Project Type**: <e.g., React web app>
- **Created**: <timestamp>
- **Change Summary**: <brief>

## Files Being Verified
- src/components/Button.tsx -> verifier-playwright
- src/routes/users.ts -> verifier-api

## Preconditions
## Setup Steps
## Verification Steps (each with Action, Expected, Success Criteria)
## Cleanup Steps
## Success Criteria

## Execution Rules
- Execute EXACTLY as written
- Report PASS or FAIL per step
- Stop immediately on first FAIL
- Do NOT skip, modify, or add steps
```

### Plan Reuse

If a pre-existing plan is passed to the Verify agent, it compares the plan's "Files Being
Verified" and "Change Summary" against current `git diff`. If they still match, the plan is
reused as-is. If changes have diverged, a fresh plan is created.

### When No Verifiers Exist

The Verify agent refuses to proceed and suggests running `/init-verifiers`:

> "No verifier skills found. Run `/init-verifiers` to create one."

---

## Relationship to Other Systems

- **Skills system** (report.md): init-verifiers is a `type: "prompt"` bundled skill with
  `source: "builtin"`. The Verify agent is registered via `XW()` (registerSkill).
- **Hooks** (hooks/report.md): Verifiers could be triggered by hooks, but the current
  implementation uses direct Skill tool invocation.
- **Permission system** (03-permission-safety): Each verifier type has restricted
  `allowed-tools` to limit blast radius (e.g., playwright verifiers can't run arbitrary
  bash, only `npm:*` prefixed commands).
- **TodoWrite**: The init-verifiers prompt explicitly instructs "Use the TodoWrite tool to
  track your progress through this multi-step task."
