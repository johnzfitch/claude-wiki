---
title: "Reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/reference"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:37:59Z"
tags: ["api", "mcp"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Freference)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

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

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Reference

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Reference

Copy page



Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.

Copy page



This page collects reference material for Claude Managed Agents. For task-oriented guides, follow the links in each section. For the operations on the session resource, see [Session operations](managed-agents-session-operations.md).

## Event types

Persisted event type strings follow a `{domain}.{action}` naming convention; the stream-only event deltas (see the Event deltas tab) are the exception. See [Session event stream](managed-agents-events-and-streaming.md) for sending, streaming, and listing events. Webhook event types are listed separately in [Subscribe to webhooks](managed-agents-webhooks.md#supported-event-types), and some of their names differ from the stream's (for example, `session.status_idled` rather than `session.status_idle`).

User events

Agent events

Session events

Span events

System events

Event deltas

User events

| Type                      | Description                                                                                                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `user.message`            | A user message with text, image, or document content.                                                                                                                                                                     |
| `user.interrupt`          | Stop the agent mid-execution. It ends no [workflow run](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open).                                                                                        |
| `user.custom_tool_result` | Response to a custom tool call from the agent.                                                                                                                                                                            |
| `user.tool_confirmation`  | Approve or deny an agent or MCP tool call when a permission policy requires confirmation.                                                                                                                                 |
| `user.define_outcome`     | Define an [outcome](managed-agents-define-outcomes.md) for the agent to work toward.                                                                                                                                |
| `user.tool_result`        | For sessions with `self_hosted` [environments](managed-agents-self-hosted-sandboxes.md) only, your integration is responsible for providing `agent_toolset` results. The SDK helpers and CLI do this automatically. |

Agent events

| Type                             | Description                                                                                                                                                                                                                                                         |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `agent.message`                  | Agent response content blocks.                                                                                                                                                                                                                                      |
| `agent.thinking`                 | Signals the agent is making forward progress through extended thinking. This is a progress signal only and does not carry the thinking content.                                                                                                                     |
| `agent.tool_use`                 | Agent invokes a pre-built agent tool (bash, file operations, and so on). Carries `evaluated_permission` and, usually, `evaluation` (see [how each call was evaluated](managed-agents-permission-policies.md#see-how-each-call-was-evaluated)).                |
| `agent.tool_result`              | Result of a pre-built agent tool execution.                                                                                                                                                                                                                         |
| `agent.mcp_tool_use`             | Agent invokes an MCP server tool. Carries `evaluated_permission` and, usually, `evaluation` (see [how each call was evaluated](managed-agents-permission-policies.md#see-how-each-call-was-evaluated)).                                                       |
| `agent.mcp_tool_result`          | Result of an MCP tool execution.                                                                                                                                                                                                                                    |
| `agent.custom_tool_use`          | Agent invokes one of your custom tools. Respond with a `user.custom_tool_result` event.                                                                                                                                                                             |
| `agent.thread_context_compacted` | Conversation history was compacted to fit the context window.                                                                                                                                                                                                       |
| `agent.thread_message_received`  | In a [multiagent](managed-agents-multiagent-orchestration.md) session, a message from another thread arrived on the thread whose stream carries this event; on the primary thread, an agent sent a report or question to the agent that the session runs.     |
| `agent.thread_message_sent`      | In a [multiagent](managed-agents-multiagent-orchestration.md) session, the thread whose stream carries this event sent a message to another thread; on the primary thread, the agent that the session runs sent a task or follow-up message to another agent. |

Message content in these events can include a `redacted` content block, `{"type": "redacted"}`: a placeholder for content withheld by Anthropic model policy. The block carries no other fields. Redacted blocks appear only in content the platform emits; a user event that includes one is rejected with a 400 error.

Session events

| Type                                | Description                                                                                                                                                                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `session.status_running`            | Agent is actively processing.                                                                                                                                                                                                                          |
| `session.status_idle`               | Agent finished its current task and is waiting for input. Includes a `stop_reason` indicating why the agent stopped.                                                                                                                                   |
| `session.status_rescheduled`        | A transient error occurred and the session is retrying automatically.                                                                                                                                                                                  |
| `session.status_terminated`         | Session ended, either because of an unrecoverable error or because it was archived.                                                                                                                                                                    |
| `session.deleted`                   | Session was deleted. Terminates any active event stream; no further events are emitted for this session.                                                                                                                                               |
| `session.updated`                   | Session update request changed at least one field. Includes only the fields that changed. Updates apply on the next turn.                                                                                                                              |
| `session.error`                     | An error occurred during processing. Includes a typed `error` object with a `retry_status`.                                                                                                                                                            |
| `session.usage`                     | Snapshot of the session's cumulative usage and tracked list cost. Carries the session's usage totals and, if the session has one, its [budget](managed-agents-budgets.md).                                                                       |
| `session.thread_created`            | A [multiagent](managed-agents-multiagent-orchestration.md) thread was created. It includes `workflow_run_id`: the run's ID for a [workflow run](managed-agents-workflow-runs.md#a-runs-threads)'s thread, and `None` for any other thread. |
| `session.thread_status_running`     | A session thread began executing. Every session emits this for its primary thread; in [multiagent](managed-agents-multiagent-orchestration.md) sessions, child-thread transitions are also cross-posted to the primary stream.                   |
| `session.thread_status_idle`        | A session thread finished its turn and is awaiting input. Includes `stop_reason`.                                                                                                                                                                      |
| `session.thread_status_rescheduled` | A session thread hit a transient error and is retrying automatically.                                                                                                                                                                                  |
| `session.thread_status_terminated`  | A session thread terminated and accepts no further input, for example because it was archived or hit an unrecoverable error. An advisor thread also terminates when its consultation ends. The server archives a workflow run's threads itself.        |

In a session whose agent has [dynamic workflows](managed-agents-multiagent-orchestration.md#dynamic-workflows) turned on, these `workflow_run.*` events arrive on the session's stream:

| Type                          | Description                                                                                                                                                                                                                                                                                                                        |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `workflow_run.created`        | A workflow run was created. Includes `workflow_run_id`, the run's `name` and `description`, and `phases`, the phases declared for the run. A status event follows, though after an interrupt it might not.                                                                                                                         |
| `workflow_run.status_running` | A workflow run is running. Sent when the run starts to execute, which can be a while after `workflow_run.created`, and again when it resumes after a pause at the budget. A resume after an interrupt might not send it. A run that is idle from the start might get `workflow_run.status_idle` first. Includes `workflow_run_id`. |
| `workflow_run.status_idle`    | A workflow run went idle: it was paused, for example at the session's budget. A pause after an interrupt might not send it. Includes `workflow_run_id`.                                                                                                                                                                            |
| `workflow_run.status_ended`   | A workflow run ended. Includes `workflow_run_id` and `result`, whose `type` says how the run ended.                                                                                                                                                                                                                                |
| `workflow_run.error`          | An error of a workflow run, or a start that the server refused. A run that ends in error gets it, with the same error, before its `workflow_run.status_ended`. Includes `error` and `workflow_run_id`, which is `None` when no run was created.                                                                                    |
| `workflow_run.phase_started`  | A workflow run entered one of its phases. Includes `workflow_run_id` and `workflow_run_phase_id`.                                                                                                                                                                                                                                  |
| `workflow_run.phase_ended`    | A workflow run left a phase. Includes `workflow_run_id`, `workflow_run_phase_id`, and `phase_started_id`.                                                                                                                                                                                                                          |

Span events

Span events are observability markers that wrap activity for timing and usage tracking.

| Type                              | Description                                                                                                                                                                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `span.model_request_start`        | A model inference call has started.                                                                                                                                                                                           |
| `span.model_request_end`          | A model inference call has completed. Includes `model_usage` with token counts.                                                                                                                                               |
| `span.outcome_evaluation_start`   | [Outcome](managed-agents-define-outcomes.md) evaluation has started.                                                                                                                                                    |
| `span.outcome_evaluation_ongoing` | Heartbeat during an ongoing [outcome](managed-agents-define-outcomes.md) evaluation.                                                                                                                                    |
| `span.outcome_evaluation_end`     | An [outcome](managed-agents-define-outcomes.md) evaluation cycle has completed. A `needs_revision` result means another cycle follows; `satisfied`, `max_iterations_reached`, `failed`, and `interrupted` are terminal. |

System events

| Type             | Description                                                                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `system.message` | Append privileged system-level context that applies to the accompanying turn and all subsequent turns. For the models that accept it, see [Supported models](managed-agents-events-and-streaming.md#supported-models). On an unsupported primary model the event is rejected with `model_does_not_support_mid_conversation_system`. |

Event deltas

Event deltas are stream-only preview events. They are emitted on stream connections (session-level or per-thread) that opt in with the `event_deltas` parameter, and they are never persisted to the session's event history. See [Preview responses with event deltas](managed-agents-event-deltas.md) for opting in, accumulating, and reconciling them.

| Type          | Description                                                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------|
| `event_start` | A previewed event has started generating. Carries the upcoming event's `type` and `id`. Stream-only and never persisted. |
| `event_delta` | Incremental content for a previewed event, identified by `event_id`. Stream-only and never persisted.                    |

## Self-hosted worker

See [Self-hosted worker reference](managed-agents-self-hosted-sandboxes-reference.md) for the `ant beta:worker` CLI flags, environment variables, filesystem paths, and SDK helper options of the pre-built workers that drive a `self_hosted` environment.

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
