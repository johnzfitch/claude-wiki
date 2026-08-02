---
title: "Skills - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/skills"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:22Z"
tags: ["api", "skills"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Prototype in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

Self-hosted sandboxes

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

MCP tunnels

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[](/login)




Managed Agents

Agent Skills

Managed Agents/Define your agent

# Skills




Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.




Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Each skill you add incurs a modest cost on the session's context window, adding instructions and metadata that help the model use the skill. Learn more in the [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) overview.

You can attach two types of skill. Both work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling (`pptx`, `xlsx`, `docx`, `pdf`).
- **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](/docs/en/agents-and-tools/agent-skills/best-practices). To upload a custom skill to your workspace, see [Create a custom skill](#create-a-custom-skill).



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Create a custom skill

A custom skill is a directory containing a `SKILL.md` file plus any supporting files, uploaded to your workspace as a zip archive or as individual files. Creating the skill returns the `skill_*` ID you reference when attaching it to an agent. Anthropic pre-built skills are already available in every workspace and don't require this step. To use only pre-built skills, skip to [Attach skills to an agent](#attach-skills-to-an-agent).

When you call the Skills API directly with cURL, pass the `anthropic-beta: skills-2025-10-02` header explicitly. The CLI and SDKs send it automatically.

These examples omit the optional `display_title` field, so the skill's title is derived from `SKILL.md`. An explicitly passed `display_title` must be unique among the custom skills in your workspace.

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
ant beta:skills create \
  --file example_skill.zip
```

To list, retrieve, delete, and version custom skills, see [Managing custom skills](/docs/en/build-with-claude/skills-guide#managing-custom-skills). For the full request and response schemas, see the [Create Skill API reference](/docs/en/api/beta/skills/create). Skill bundles upload directly to the Skills API rather than through the [Files API](/docs/en/build-with-claude/files).




Attach skills to an agent

Attach skills when creating an agent. Each [session](/docs/en/managed-agents/sessions) supports up to 500 skills total, counted across every agent in the session (see [Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)).



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
ant beta:agents create <<'YAML'
name: Financial Analyst
model: claude-opus-5
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
    version: latest
YAML
```




Next steps




Cloud environment setup

Customize cloud sandboxes for your sessions.




Using Agent Skills with the API

Learn how to use Agent Skills to extend Claude's capabilities through the API.




Files API

Upload files once and reference them across API requests.




Get started with Agent Skills in the API

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.
