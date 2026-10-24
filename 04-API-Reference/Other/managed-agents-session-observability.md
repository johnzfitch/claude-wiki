---
title: "Inspect sessions and track usage - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-observability"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:29:45Z"
tags: ["api"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsession-observability)

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

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Inspect sessions and track usage

Copy page



Inspect a session in the Claude Console, read its token usage and list cost, and debug unexpected agent behavior.

Copy page



Use the session viewer in the Claude Console to inspect what an agent did in a session, without writing any code. Use the session's `usage` totals to see what that work consumed.

## Inspect a session in the Console

The session viewer is only accessible to Developers and Admins. To open it, go to the [Sessions](playground.md) page (`platform.claude.com/sessions`) in the Claude Console. The list shows every session in the workspace with its status, agent, token usage, cost, and creation time. Select a session to open it.

The session viewer shows:

- **Timeline minimap:** A zoomable overview of the session's activity over time, with one lane for each thread in [multiagent](managed-agents-multiagent-orchestration.md) sessions. Select a lane to view that thread, or select a mark to jump to its event.
- **Transcript:** The conversation grouped by model request, including thinking, tool calls with their inputs and results, and message text as it streams. You can filter the events and copy or download them as JSON.
- **Inspector:** A resizable side panel with details about the session, in five tabs.

| Inspector tab | What it shows                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Session**   | The session's details and metadata, its cumulative cost over time, and spend against the session's [budget](managed-agents-budgets.md) when one is set.                                                                                                                                                                                                                                               |
| **Events**    | Every raw event on the current thread, in the order the server sent it. Select an event to see its JSON. A message that streamed while the page was open also has a **Deltas** view of its [event deltas](managed-agents-event-deltas.md).                                                                                                                                                            |
| **Tools**     | The tools the session's agents are configured with, along with call counts, failures, and median duration. Select a tool to see its calls and jump to one in the transcript.                                                                                                                                                                                                                                |
| **Resources** | Mounted [files](managed-agents-files.md), [repositories](managed-agents-github.md), and [memory stores](managed-agents-memory.md) at their container paths, including the memories in each store and the changes this session made to them. Also lists files the agent wrote to `/mnt/session/outputs` and the [skills](managed-agents-skills.md) attached to the session's agents. |
| **Threads**   | Every thread with its status, context size, and cost. Select a thread to view its details, such as the agent, model, context usage, and cost.                                                                                                                                                                                                                                                               |

Append `?event={event_id}` to a session URL to open the session at a specific event.

With `ant beta:sessions connect`, you can open the same viewer from the `ant` CLI or follow the session in your terminal. See [Connect to a Managed Agents session from your terminal](cli-sdks-libraries-cli-sessions-connect.md).

## Track usage

The session object includes a `usage` field with the session's cumulative usage: token counts, server tool use, active time, and the tracked list cost. Fetch the session after it goes idle to read the latest totals.

``` block
{
  "id": "sesn_01...",
  "status": "idle",
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 3200,
    "cache_read_input_tokens": 20000,
    "cache_creation": {
      "ephemeral_5m_input_tokens": 2000,
      "ephemeral_1h_input_tokens": 0
    },
    "list_cost": {
      "amount": "187",
      "currency": "USD"
    },
    "active_seconds": 342.5,
    "server_tool_use": {
      "web_search_requests": 3,
      "web_fetch_requests": 0
    }
  }
}
```



| Field                     | Description                                                                                                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `input_tokens`            | Uncached input tokens across all model calls in the session.                                                                                                                                                           |
| `output_tokens`           | Total output tokens across all model calls in the session.                                                                                                                                                             |
| `cache_read_input_tokens` | Tokens read from the prompt cache.                                                                                                                                                                                     |
| `cache_creation`          | Cache-creation tokens, broken down by cache lifetime (`ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`).                                                                                                    |
| `list_cost`               | The session's cumulative consumption priced at public list rates, as a whole number of cents in a string, with a currency code.                                                                                        |
| `active_seconds`          | The cumulative time during which the session had at least one thread running. Overlapping activity from concurrent threads is counted once. The session's runtime cost is priced on this duration.                     |
| `server_tool_use`         | Counts of server-executed tool requests, for pricing. Web search requests are priced into list cost per request. Web fetch requests carry no per-request charge and aren't metered, so `web_fetch_requests` reads `0`. |

Cache entries use a 5-minute TTL by default, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.

The session's `stats` object has its own `active_seconds`, which sums each thread's own active time instead of counting overlapping activity once.

### Per-thread usage

Each [session thread](managed-agents-session-threads.md)'s own `usage` carries `list_cost` and `active_seconds` too. Per-thread figures are rounded independently and exclude the session's running-time cost, so they don't sum exactly to the session's `list_cost`. The session figure is the authoritative one.

### Read usage from the stream

You don't have to poll the session to observe these totals. The `session.usage` event carries the same cumulative snapshot on the session stream and in the event history. The snapshot holds the `usage` object, plus the session's `budget` if the session has one.

The event is emitted on idle transitions rather than on a timer:

- The session emits one immediately before it goes idle, whatever the stop reason.
- The session emits one when a thread pauses at a [session budget](managed-agents-budgets.md).

### Enforce a spend limit

To enforce a spend limit, set a session budget rather than polling usage and stopping the session yourself. The platform prices the session's consumption continuously, and pauses each thread before its next model request once the list cost reaches the cap. See [When a session reaches its budget](managed-agents-budgets.md#when-a-session-reaches-its-budget) for what that looks like on the stream.

## Debugging tips

- **Check session events:** The session reports errors through [`session.error`](managed-agents-reference.md#event-types) events.
- **Review tool results:** Tool failures often explain unexpected agent behavior. The Inspector's **Tools** tab shows each tool's failures.
- **Use system prompts:** Add logging instructions to the system prompt so the agent summarizes what it did and what it found.
- **Troubleshoot previews:** If a stream that opts in to event deltas doesn't behave as you expect, see [Troubleshoot previews](managed-agents-event-deltas.md#troubleshoot-previews).

## Next steps



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session while it runs.

[Session budgets](managed-agents-budgets.md)

Cap a session's spend with a hard dollar budget enforced at public list rates.
