---
title: "Skills - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/skills"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:43Z"
tags: ["agents", "api", "git", "github", "skills"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fskills)





SearchCtrlK

First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Build in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

[Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes)

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Session budgets](/docs/en/managed-agents/budgets)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[Console](/)

[Managed Agents](/docs/en/managed-agents/overview)Define your agent

# Skills

Copy page



Attach pre-built or custom skills to an agent in Claude Managed Agents to give it reusable, filesystem-based expertise for domain-specific workflows.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Each skill you add incurs a modest cost on the session's context window, adding instructions and metadata that help the model use the skill. Learn more in the [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) overview.

Skills reach your agent in two ways: attach them through the agent's `skills` array, or [load them from a GitHub repository](#load-skills-from-a-github-repository) mounted on the session. Attached skills come in two types. All skills work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling (`pptx`, `xlsx`, `docx`, `pdf`).
- **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](/docs/en/agents-and-tools/agent-skills/best-practices). To upload a custom skill to your workspace, see [Create a custom skill](#create-a-custom-skill).

## Create a custom skill

A custom skill is a directory containing a `SKILL.md` file plus any supporting files, uploaded to your workspace as a zip archive or as individual files. Creating the skill returns the `skill_*` ID you reference when attaching it to an agent. Anthropic pre-built skills are already available in every workspace and don't require this step. To use only pre-built skills, skip to [Attach skills to an agent](#attach-skills-to-an-agent).

These examples omit the optional `display_name` field, so the skill's display name is derived from the `name` field in `SKILL.md`. An explicit `display_name` can be up to 255 characters and doesn't need to be unique within your workspace.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant apply skills/pr-summary
```

skills/pr-summary/SKILL.md





```python
---
name: pr-summary
description: Summarize a pull request's changes and risks in the team's review format.
---

# PR summary

List what changed, why, and anything a reviewer should look at closely, in three short sections.
```

[`ant apply`](/docs/en/cli-sdks-libraries/cli/apply) uploads the `skills/pr-summary` directory, prints the new skill's ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` uploads your edits as a new version instead of creating a second skill.

To list, retrieve, delete, and version custom skills, see [Managing custom skills](/docs/en/build-with-claude/skills-guide#managing-custom-skills). For the full request and response schemas, see the [Create Skill API reference](/docs/en/api/skills/create). Skill bundles upload directly to the Skills API rather than through the [Files API](/docs/en/build-with-claude/files).

## Attach skills to an agent

Attach skills when creating an agent. Each [session](/docs/en/managed-agents/sessions) supports up to 500 skills, counted as the deduplicated set across every agent in the session (see [Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)).



Mounting more skills increases the time it takes for the session's sandbox to start. Attach only the skills each agent needs for its task.

Each entry in the `skills` array uses the following fields:

| Field      | Description                                                                                                                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`     | Either `anthropic` for pre-built skills or `custom` for workspace-authored skills.                                                                                                                        |
| `skill_id` | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation (see [Create a custom skill](#create-a-custom-skill)). |
| `version`  | Pin to a specific version or use `latest`. Optional. Defaults to `latest` when omitted. Applies to both Anthropic and custom skills.                                                                      |

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
ant apply agent.md
```

agent.md





```python
---
name: Financial Analyst
model: claude-opus-5-5
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
    version: latest
---

You are a financial analysis agent.
```

## Load skills from a GitHub repository

Skills can also live in your codebase. When a session mounts a repository through the [`github_repository` resource](/docs/en/managed-agents/github), the repository's root `.claude/skills` directory is scanned at session start, and each skill found there becomes available to the agent. No upload and no entry in the agent's `skills` array are required. The agent sees each discovered skill's name, description, and path in the sandbox, and reads the skill's `SKILL.md` when a task matches, including any scripts and resources the skill ships. Discovery relies on the agent's `read` tool from the [agent toolset](/docs/en/managed-agents/tools), which is enabled by default; an agent with `read` disabled doesn't load repository skills.



Repository skills are agent instructions, so a mounted repository is part of your agent's trust boundary. Anyone who can commit to the repository (a merged external pull request, a compromised dependency, a contributor) can add or change a skill, the platform loads it at session start without a review step, and session tools such as `bash` and `web_fetch` give those instructions real reach. Mount only repositories you trust, and review `.claude/skills` before mounting a repository that accepts outside contributions.



Repository skill discovery runs in cloud sandboxes. [Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes) don't support GitHub repository resources.

Discovery finds skills at exactly `.claude/skills/<skill-name>/SKILL.md`, one directory level deep at the repository root:

- `your-repo/`
  - `.claude/`
    - `skills/`
      - `code-review/`
        - `SKILL.md`
      - `release-process/`
        - `SKILL.md`
        - `scripts/`
          - `run_checks.sh`
  - `src/`

Locations that don't match this layout aren't discovered at session start:

- `.claude/skills/SKILL.md`: a `SKILL.md` with no skill directory around it
- `.claude/skills/tools/code-review/SKILL.md`: nested more than one directory level deep
- `skills/code-review/SKILL.md`: a `skills` directory outside `.claude`

A `.claude/skills` directory elsewhere in the repository, such as inside a package subdirectory, isn't announced at session start; those skills can still surface when the agent reads files under that subtree.

Repository skills use the same `SKILL.md` format as the custom skills you upload. For the format and authoring guidance, see [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](/docs/en/agents-and-tools/agent-skills/best-practices).

To load skills from a repository, create a session that mounts it. This is the same request shown in [Accessing GitHub](/docs/en/managed-agents/github#token-permissions); `mount_path` is optional and defaults to `/workspace/<repo-name>`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
        },
    ],
)
```

For private repositories, the resource's `authorization_token` must have access to the repository. This is the same personal access token flow used for any repository mount; see [Accessing GitHub](/docs/en/managed-agents/github#token-permissions).

Discovered skills follow the checked-out state of the repository: the `checkout` branch or commit when the resource sets one, otherwise the repository's default branch. The scan runs once, when the session starts. Commits pushed mid-session are not picked up; to load updated skills, start a new session.

Repository skills work alongside skills attached through the agent's `skills` array. If a repository skill shares a name with an attached skill, or with a skill from another mounted repository, both are available; each is announced with its own path.

## Next steps



[Cloud environment setup](/docs/en/managed-agents/environments)

Customize cloud sandboxes for your sessions.



[Using Agent Skills with the API](/docs/en/build-with-claude/skills-guide)

Learn how to use Agent Skills to extend Claude's capabilities through the API.



[Files API](/docs/en/build-with-claude/files)

Upload files once and reference them across API requests.



[Get started with Agent Skills in the API](/docs/en/agents-and-tools/agent-skills/quickstart)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.
