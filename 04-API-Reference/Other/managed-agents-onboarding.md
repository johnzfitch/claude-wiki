---
title: "Build in Console - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/onboarding"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:36:47Z"
tags: ["agents", "api", "testing"]
---

# Build in Console

Copy page



Create, test, and iterate on agents visually in the Claude Console, then run them from your code with the API.

Copy page



Console agent builder

Feature of  
[Managed Agents](managed-agents-overview.md)

[Status](#availability-feature-support)  
Beta

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailable

[Beta header](#feature-beta-headers)  
- `managed-agents-2026-04-01`
  

[Data handling](#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

The [Claude Console](https://platform.claude.com/workspaces/default/agent-quickstart) provides a visual interface for creating and configuring agents. It lets you iterate on configuration interactively before writing code.

## How to build an agent

The [visual interface](https://platform.claude.com/workspaces/default/agent-quickstart) in the Claude Console walks you through each field of an agent definition:

- **Model and system prompt:** Pick a model and write the system prompt in a full-width editor.
- **MCP servers:** Add remote MCP servers by URL and authenticate your agent to take action on your behalf.
- **Tools:** Extend your agent’s capabilities using a pre-built agent toolset and MCP tools.
- **Skills:** Attach Anthropic or custom skills from your organization’s library.

As you configure, Console shows the equivalent API request so you can copy it into your code once you’re satisfied.

## Testing an agent

Console includes an inline session runner. After configuring your agent, you can start a test session directly, send messages, and watch the event stream without leaving the page. This is the fastest way to check that your system prompt and tool selection produce the behavior you expect.

## From Console to your code base

Once your agent works as expected:

1.  Copy the agent ID and [environment ID](managed-agents-environments.md) from Console.
2.  Reference them in your code when [creating sessions](managed-agents-sessions.md):

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
session = client.beta.sessions.create(
    agent="agent_01J8XkN5uT3vHpLqRfWdY2",
    environment_id="env_01K2mPsT7hNwR4jXuLvCqD8",
    title="My first session",
)
```

## Availability

Console agent builder is in beta on every model.

### API support

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `managed-agents-2026-04-01`
  

### Data handling

[Data handling overview](manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/agents`
- `/v1/sessions`
- `/v1/environments`

Zero data retentionNot eligible

Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including Self-hosted sandboxes.

HIPAANot eligible

Applies to all Managed Agents sub-features, including Self-hosted sandboxes.
