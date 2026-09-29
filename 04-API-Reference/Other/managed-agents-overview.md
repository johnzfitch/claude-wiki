---
title: "Claude Managed Agents overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:50Z"
tags: ["agents", "api"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Foverview)

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

Managed AgentsFirst steps

# Claude Managed Agents overview

Copy page



Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.

Copy page



Managed Agents

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Anthropic offers two ways to build with Claude, each suited to different use cases:

|                | Messages API                                | Claude Managed Agents                                                     |
|----------------|---------------------------------------------|---------------------------------------------------------------------------|
| **What it is** | Direct model prompting access               | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for**   | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work                                  |

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and run code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations for high-quality, efficient agent outputs. To build your own agent loop with direct model access instead, see [Using the Messages API](../Guides/build-with-claude-working-with-messages.md).



Claude Managed Agents is also available on Claude Platform on AWS, with some differences in feature availability and session behavior. See [Claude Managed Agents](../Guides/build-with-claude-claude-platform-on-aws.md#claude-managed-agents) in the Claude Platform on AWS guide.



[Quickstart](managed-agents-quickstart.md)

Create your first agent session



[Start a session](managed-agents-sessions.md)

Create a session and send your first event



[Reference](managed-agents-reference.md)

Event types, rate limits, CLI flags, and other lookup tables

## Core concepts

Claude Managed Agents is built around four concepts:

| Concept         | Description                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Agent**       | The model, system prompt, tools, MCP servers, and skills                                                                      |
| **Environment** | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure |
| **Session**     | A running agent instance within an environment, performing a specific task and generating outputs                             |
| **Events**      | Messages exchanged between your application and the agent (user turns, tool results, status updates)                          |

## How it works

1.  1

    ### Create an agent

    Define the model, system prompt, tools, MCP servers, and skills. Create the agent once and reference it by ID across sessions.

2.  2

    ### Create an environment

    Configure where the agent runs: a cloud sandbox, or a [self-hosted sandbox](managed-agents-self-hosted-sandboxes.md) on your own infrastructure.

3.  3

    ### Start a session

    Launch a session that references your agent and environment configuration.

4.  4

    ### Send events and stream responses

    Send user messages as events. Claude autonomously runs tools and streams back results through server-sent events (SSE). Event history is persisted server-side and can be fetched in full.

5.  5

    ### Steer or interrupt

    Send additional user events to guide the agent mid-execution, or interrupt it to change direction.

## When to use Claude Managed Agents

Claude Managed Agents is best for workloads that need:

- **Long-running execution:** Tasks that run for minutes or hours with multiple tool calls
- **Cloud infrastructure:** Secure sandboxes with pre-installed packages and network access
- **Self-hosted execution:** Sandboxes on infrastructure you control for compliance or data-residency requirements
- **Minimal infrastructure:** No need to build your own agent loop, sandbox, or tool execution layer
- **Stateful sessions:** Persistent filesystems and conversation history across multiple interactions
- **Scheduled execution:** Recurring agent runs on a cron schedule through [scheduled deployments](managed-agents-scheduled-deployments.md)

## Supported tools

Claude Managed Agents gives Claude access to a set of built-in tools:

- **Bash:** Run shell commands in the sandbox
- **File operations:** Read, write, edit, glob, and grep files in the sandbox
- **Web search and fetch:** Search the web and retrieve content from URLs, optionally restricted to an allowlist or blocklist of domains
- **MCP servers:** Connect to external tool providers

See [Tools](managed-agents-tools.md) for the full list and configuration options.

## Beta access



Claude Managed Agents is in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically. Behaviors may be refined between releases to improve outputs.

To get started, you need:

1.  A [Claude API key](usage-limits.md)
2.  The `managed-agents-2026-04-01` beta header on all requests
3.  Access to Claude Managed Agents (enabled by default for all API accounts)

Within the beta, [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) and [dreaming](managed-agents-dreams.md) are in a more limited research preview. [Request access](https://claude.com/form/claude-managed-agents) to enable them.

Claude Managed Agents is stateful by design: sessions are long-running, resume cleanly after pauses, and store conversation history, sandbox state, and outputs server-side. Because of this, Managed Agents is not currently eligible for [Zero Data Retention](manage-claude-api-and-data-retention.md#zero-data-retention-zdr-scope) or HIPAA Business Associate Agreement (BAA) coverage. You retain control over this data: you can [delete sessions](managed-agents-session-operations.md#deleting-a-session), and separately delete any [files](../Guides/build-with-claude-files.md#delete-a-file) you uploaded, at any time through the API. For eligibility across all features, see [API and data retention](manage-claude-api-and-data-retention.md#feature-eligibility).

See [Rate limits](managed-agents-reference.md#rate-limits) and [Branding guidelines](managed-agents-reference.md#branding-guidelines) in the reference.
