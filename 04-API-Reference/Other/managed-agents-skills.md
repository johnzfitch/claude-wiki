---
title: "Skills - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/skills"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:43Z"
tags: ["agents", "api", "git", "github", "skills"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fskills)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)Define your agent

# Skills

Copy page



Attach pre-built or custom skills to an agent in Claude Managed Agents to give it reusable, filesystem-based expertise for domain-specific workflows.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Each skill you add incurs a modest cost on the session's context window, adding instructions and metadata that help the model use the skill. Learn more in the [Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md) overview.

Skills reach your agent in two ways: attach them through the agent's `skills` array, or [load them from a GitHub repository](#load-skills-from-a-github-repository) mounted on the session. Attached skills come in two types. All skills work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling (`pptx`, `xlsx`, `docx`, `pdf`).
- **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md) and [Skill authoring best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md). To upload a custom skill to your workspace, see [Create a custom skill](#create-a-custom-skill).

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

[`ant apply`](cli-sdks-libraries-cli-apply.md) uploads the `skills/pr-summary` directory, prints the new skill's ID, and records it in `claude-lock.json`. Commit `claude-lock.json` so the next `ant apply` uploads your edits as a new version instead of creating a second skill.

To list, retrieve, delete, and version custom skills, see [Managing custom skills](../Guides/build-with-claude-skills-guide.md#managing-custom-skills). For the full request and response schemas, see the [Create Skill API reference](../Endpoints/skills-create.md). Skill bundles upload directly to the Skills API rather than through the [Files API](../Guides/build-with-claude-files.md).

## Attach skills to an agent

Attach skills when creating an agent. Each [session](managed-agents-sessions.md) supports up to 500 skills, counted as the deduplicated set across every agent in the session (see [Multiagent orchestration](managed-agents-multiagent-orchestration.md)).

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

Skills can also live in your codebase. When a session mounts a repository through the [`github_repository` resource](managed-agents-github.md), the repository's root `.claude/skills` directory is scanned at session start, and each skill found there becomes available to the agent. No upload and no entry in the agent's `skills` array are required. The agent sees each discovered skill's name, description, and path in the sandbox, and reads the skill's `SKILL.md` when a task matches, including any scripts and resources the skill ships. Discovery relies on the agent's `read` tool from the [agent toolset](managed-agents-tools.md), which is enabled by default; an agent with `read` disabled doesn't load repository skills.



Repository skills are agent instructions, so a mounted repository is part of your agent's trust boundary. Anyone who can commit to the repository (a merged external pull request, a compromised dependency, a contributor) can add or change a skill, the platform loads it at session start without a review step, and session tools such as `bash` and `web_fetch` give those instructions real reach. Mount only repositories you trust, and review `.claude/skills` before mounting a repository that accepts outside contributions.



Repository skill discovery runs in cloud sandboxes. [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md) don't support GitHub repository resources.

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

Repository skills use the same `SKILL.md` format as the custom skills you upload. For the format and authoring guidance, see [Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md) and [Skill authoring best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md).

To load skills from a repository, create a session that mounts it. This is the same request shown in [Accessing GitHub](managed-agents-github.md#token-permissions); `mount_path` is optional and defaults to `/workspace/<repo-name>`:

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

For private repositories, the resource's `authorization_token` must have access to the repository. This is the same personal access token flow used for any repository mount; see [Accessing GitHub](managed-agents-github.md#token-permissions).

Discovered skills follow the checked-out state of the repository: the `checkout` branch or commit when the resource sets one, otherwise the repository's default branch. The scan runs once, when the session starts. Commits pushed mid-session are not picked up; to load updated skills, start a new session.

Repository skills work alongside skills attached through the agent's `skills` array. If a repository skill shares a name with an attached skill, or with a skill from another mounted repository, both are available; each is announced with its own path.

## Next steps



[Cloud environment setup](managed-agents-environments.md)

Customize cloud sandboxes for your sessions.



[Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md)

Learn how to use Agent Skills to extend Claude's capabilities through the API.



[Files API](../Guides/build-with-claude-files.md)

Upload files once and reference them across API requests.



[Get started with Agent Skills in the API](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.
