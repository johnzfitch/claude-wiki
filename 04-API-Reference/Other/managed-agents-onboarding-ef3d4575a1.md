---
title: "Build in Console - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/onboarding"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["agents", "api", "testing"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fonboarding)

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

[Managed Agents](/docs/en/managed-agents/overview)First steps

# Build in Console

Copy page



Create, test, and iterate on agents visually in Console, then run them from your code with the API.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

[Console](https://platform.claude.com/workspaces/default/agent-quickstart/) provides a visual interface for creating and configuring agents. It lets you iterate on configuration interactively before writing code.

## How to build an agent

The [visual interface](https://platform.claude.com/workspaces/default/agent-quickstart/) walks you through each field of an agent definition:

- **Model and system prompt:** Pick a model and write the system prompt in a full-width editor.
- **MCP servers:** Add remote MCP servers by URL and authenticate your agent to take action on your behalf.
- **Tools:** Extend your agent's capabilities using a pre-built agent toolset and MCP tools.
- **Skills:** Attach Anthropic or custom skills from your organization's library.

As you configure, Console shows the equivalent API request so you can copy it into your code once you're satisfied.

## Testing an agent

Console includes an inline session runner. After configuring your agent, you can start a test session directly, send messages, and watch the event stream without leaving the page. This is the fastest way to check that your system prompt and tool selection produce the behavior you expect.

## From Console to your codebase

Once your agent works as expected:

1.  Copy the agent ID and [environment ID](/docs/en/managed-agents/environments) from Console.
2.  Reference them in your code when [creating sessions](/docs/en/managed-agents/sessions):

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
    agent="agent_01J8XkN5uT3vHpLqRfWdY2",
    environment_id="env_01K2mPsT7hNwR4jXuLvCqD8",
    title="My first session",
)
```
