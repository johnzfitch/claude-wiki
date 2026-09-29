---
title: "Reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/reference"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:41Z"
tags: ["api", "mcp"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Freference)

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

[Managed Agents](managed-agents-overview.md)Reference

# Reference

Copy page



Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

This page collects reference material for Claude Managed Agents. For task-oriented guides, follow the links in each section. For the operations on the session resource, see [Session operations](managed-agents-session-operations.md).

## Event types

Persisted event type strings follow a `{domain}.{action}` naming convention; the stream-only event deltas (see the Event deltas tab) are the exception. See [Session event stream](managed-agents-events-and-streaming.md) for sending, streaming, and listing events. Webhook event types are listed separately in [Subscribe to webhooks](managed-agents-webhooks.md#supported-event-types), and some of their names differ from the stream's (for example, `session.status_idled` rather than `session.status_idle`).

User events

Agent events

Session events

Span events

System events

Event deltas

| Type                      | Description                                                                                                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `user.message`            | A user message with text, image, or document content.                                                                                                                                                                     |
| `user.interrupt`          | Stop the agent mid-execution.                                                                                                                                                                                             |
| `user.custom_tool_result` | Response to a custom tool call from the agent.                                                                                                                                                                            |
| `user.tool_confirmation`  | Approve or deny an agent or MCP tool call when a permission policy requires confirmation.                                                                                                                                 |
| `user.define_outcome`     | Define an [outcome](managed-agents-define-outcomes.md) for the agent to work toward.                                                                                                                                |
| `user.tool_result`        | For sessions with `self_hosted` [environments](managed-agents-self-hosted-sandboxes.md) only, your integration is responsible for providing `agent_toolset` results. The SDK helpers and CLI do this automatically. |

## Self-hosted worker

These are the `ant beta:worker` CLI flags for the pre-built worker that drives a `self_hosted` environment. See [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md) for setting up the environment, running a worker, and the SDK helper options.

| Flag                   | Description                                                                                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--environment-id`     | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`.                                                                                            |
| `--environment-key`    | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`.                                                                             |
| `--workdir`            | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory); the system default working directory is `/workspace`.     |
| `--on-work`            | Script to call for each claimed work item instead of running tools in-process. Receives session details as environment variables.                                        |
| `--unrestricted-paths` | Allow the file tools to read and write paths outside `--workdir`. The workdir check is a guardrail for the file tools only, not a sandbox; it does not constrain bash.   |
| `--max-idle`           | How long to wait after the session goes idle with an `end_turn` [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) before shutting down. Defaults to `60s`. |
| `--log-format`         | Log output format. Use `json` for structured log ingestion. Defaults to `text`.                                                                                          |

The CLI worker does not mount [memory stores](managed-agents-memory.md): a session that attaches one still runs, but the agent finds nothing at the store's `mount_path` and no changes sync back to the store. To use memory stores in sessions on a self-hosted environment, run the SDK worker instead; see [Use memory stores](managed-agents-self-hosted-sandboxes.md#use-memory-stores).

## Supported MCP server types

Claude Managed Agents connects to [remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md) that expose an HTTP endpoint, or to private MCP servers through [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md). The server should support the MCP protocol's streamable HTTP transport; servers that only support the deprecated SSE transport still work through an automatic fallback. See [MCP connector](managed-agents-mcp-connector.md) for declaring servers on an agent.

For more information on MCP and building MCP servers, see the [MCP documentation](https://modelcontextprotocol.io).

## Rate limits

Managed Agents endpoints are rate-limited per organization:

| Operation                                                     | Limit                     |
|---------------------------------------------------------------|---------------------------|
| Create endpoints (such as agents, sessions, and environments) | 300 requests per minute   |
| Read endpoints (such as retrieve, list, and stream)           | 1,200 requests per minute |

Organization-level [spend limits and usage-tier rate limits](../Endpoints/rate-limits.md) also apply.

## Branding guidelines

For partners integrating Claude Managed Agents, use of Claude branding is optional. When referencing Claude in your product:

**Allowed:**

- "Claude Agent" (preferred for dropdown menus)
- "Claude" (when within a menu already labeled "Agents")
- "{YourAgentName} Powered by Claude" (if you have an existing agent name)

**Not permitted:**

- "Claude Code" or "Claude Code Agent"
- "Claude Cowork" or "Claude Cowork Agent"
- Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code, Claude Cowork, or any other Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).
