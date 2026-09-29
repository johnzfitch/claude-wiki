---
title: "Claude Managed Agents overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:50Z"
tags: ["agents", "api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Foverview)

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

Managed AgentsFirst steps

# Claude Managed Agents overview

Copy page



Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.

Copy page



Managed Agents

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

Anthropic offers two ways to build with Claude, each suited to different use cases:

|                | Messages API                                | Claude Managed Agents                                                     |
|----------------|---------------------------------------------|---------------------------------------------------------------------------|
| **What it is** | Direct model prompting access               | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for**   | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work                                  |

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and run code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations for high-quality, efficient agent outputs. To build your own agent loop with direct model access instead, see [Using the Messages API](/docs/en/build-with-claude/working-with-messages).



Claude Managed Agents is also available on Claude Platform on AWS, with some differences in feature availability and session behavior. See [Claude Managed Agents](/docs/en/build-with-claude/claude-platform-on-aws#claude-managed-agents) in the Claude Platform on AWS guide.



[Quickstart](/docs/en/managed-agents/quickstart)

Create your first agent session



[Start a session](/docs/en/managed-agents/sessions)

Create a session and send your first event



[Reference](/docs/en/managed-agents/reference)

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

    Configure where the agent runs: a cloud sandbox, or a [self-hosted sandbox](/docs/en/managed-agents/self-hosted-sandboxes) on your own infrastructure.

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
- **Scheduled execution:** Recurring agent runs on a cron schedule through [scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

## Supported tools

Claude Managed Agents gives Claude access to a set of built-in tools:

- **Bash:** Run shell commands in the sandbox
- **File operations:** Read, write, edit, glob, and grep files in the sandbox
- **Web search and fetch:** Search the web and retrieve content from URLs, optionally restricted to an allowlist or blocklist of domains
- **MCP servers:** Connect to external tool providers

See [Tools](/docs/en/managed-agents/tools) for the full list and configuration options.

## Beta access



Claude Managed Agents is in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically. Behaviors may be refined between releases to improve outputs.

To get started, you need:

1.  A [Claude API key](/settings/keys)
2.  The `managed-agents-2026-04-01` beta header on all requests
3.  Access to Claude Managed Agents (enabled by default for all API accounts)

Within the beta, [MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview) and [dreaming](/docs/en/managed-agents/dreams) are in a more limited research preview. [Request access](https://claude.com/form/claude-managed-agents) to enable them.

Claude Managed Agents is stateful by design: sessions are long-running, resume cleanly after pauses, and store conversation history, sandbox state, and outputs server-side. Because of this, Managed Agents is not currently eligible for [Zero Data Retention](/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope) or HIPAA Business Associate Agreement (BAA) coverage. You retain control over this data: you can [delete sessions](/docs/en/managed-agents/session-operations#deleting-a-session), and separately delete any [files](/docs/en/build-with-claude/files#delete-a-file) you uploaded, at any time through the API. For eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

See [Rate limits](/docs/en/managed-agents/reference#rate-limits) and [Branding guidelines](/docs/en/managed-agents/reference#branding-guidelines) in the reference.
