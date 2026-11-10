---
title: "Inspect sessions and track usage - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-observability"
category: "04-API-Reference/Other"
fetched_at: "2026-11-06T06:33:51Z"
tags: ["api"]
---

# Inspect sessions and track usage

Copy page



Inspect a session in the Claude Console, read its token usage and list cost, and debug unexpected agent behavior.

Copy page



Session viewer

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

Use the session viewer in the Claude Console to inspect what an agent did in a session, without writing any code. Use the session’s `usage` totals to see what that work consumed. To see a session’s turns, model requests, and tool uses in your observability platform, set up [OpenTelemetry tracing](manage-claude-opentelemetry.md).

## Inspect a session in the Console

The session viewer is only accessible to Developers and Admins. To open it, go to the [Sessions](playground.md) page (`platform.claude.com/sessions`) in the Claude Console. The list shows every session in the workspace with its status, agent, token usage, cost, creator, and creation time. Select a session to open it.

The session viewer shows:

- **Timeline minimap:** A zoomable overview of the session’s activity over time, with one lane for each thread in [multiagent](managed-agents-multiagent-orchestration.md) sessions. Select a lane to view that thread, or select a mark to jump to its event.
- **Transcript:** The conversation grouped by model request, including thinking, tool calls with their inputs and results, and message text as it streams. You can filter the events and copy or download them as JSON.
- **Inspector:** A resizable side panel with details about the session, in five tabs.

| Inspector tab | What it shows |
|----|----|
| **Session** | The session’s details and metadata, its cumulative cost over time, and spend against the session’s [budget](managed-agents-budgets.md) when one is set. |
| **Events** | Every raw event on the current thread, in the order the server sent it. Select an event to see its JSON. A message that streamed while the page was open also has a **Deltas** view of its [event deltas](managed-agents-event-deltas.md). |
| **Tools** | The tools the session’s agents are configured with, along with call counts, failures, and median duration. Select a tool to see its calls and jump to one in the transcript. |
| **Resources** | Mounted [files](managed-agents-files.md), [repositories](managed-agents-github.md), and [memory stores](managed-agents-memory.md) at their container paths, including the memories in each store and the changes this session made to them. Also lists files the agent wrote to `/mnt/session/outputs` and the [skills](managed-agents-skills.md) attached to the session’s agents. |
| **Threads** | Every thread with its status, context size, and cost. Select a thread to view its details, such as the agent, model, context usage, and cost. |

Append `?event={event_id}` to a session URL to open the session at a specific event.

With `ant beta:sessions connect`, you can open the same viewer from the `ant` CLI or follow the session in your terminal. See [Connect to a Managed Agents session from your terminal](cli-sdks-libraries-cli-sessions-connect.md).

## Track usage

The session object includes a `usage` field with the session’s cumulative usage: token counts, server tool use, active time, and the tracked list cost. Fetch the session after it goes idle to read the latest totals.

```python
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

| Field | Description |
|----|----|
| `input_tokens` | Uncached input tokens across all model calls in the session. |
| `output_tokens` | Total output tokens across all model calls in the session. |
| `cache_read_input_tokens` | Tokens read from the prompt cache. |
| `cache_creation` | Cache-creation tokens, broken down by cache lifetime (`ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`). |
| `list_cost` | The session’s cumulative consumption priced at public list rates, as a whole number of cents in a string, with a currency code. |
| `active_seconds` | The cumulative time during which the session had at least one thread running. Overlapping activity from concurrent threads is counted once. The session’s runtime cost is priced on this duration. |
| `server_tool_use` | Counts of server-executed tool requests, for pricing. Web search requests are priced into list cost per request. Web fetch requests carry no per-request charge and aren’t metered, so `web_fetch_requests` reads `0`. |

Cache entries use a 5-minute TTL by default, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.

The session’s `stats` object has its own `active_seconds`, which sums each thread’s own active time instead of counting overlapping activity once.

### Per-thread usage

Each [session thread](managed-agents-session-threads.md)’s own `usage` carries `list_cost` and `active_seconds` too. Per-thread figures are rounded independently and exclude the session’s running-time cost, so they don’t sum exactly to the session’s `list_cost`. The session figure is the authoritative one.

### Read usage from the stream

You don’t have to poll the session to observe these totals. The `session.usage` event carries the same cumulative snapshot on the session stream and in the event history. The snapshot holds the `usage` object, plus the session’s `budget` if the session has one.

The event is emitted on idle transitions rather than on a timer:

- The session emits one immediately before it goes idle, whatever the stop reason.
- The session emits one when a thread pauses at a [session budget](managed-agents-budgets.md).

### Enforce a spend limit

To enforce a spend limit, set a session budget rather than polling usage and stopping the session yourself. The platform prices the session’s consumption continuously, and pauses each thread before its next model request once the list cost reaches the cap. See [When a session reaches its budget](managed-agents-budgets.md#when-a-session-reaches-its-budget) for what that looks like on the stream.

### Find session usage across your organization

Session usage counts toward your organization’s totals on the [Usage](playground.md) page (`platform.claude.com/usage`) and the [Cost](playground.md) page (`platform.claude.com/cost`) in the Claude Console. To see token usage by agent, set **Group by** to **Agent** on the **Usage** page.

To see session usage by agent or by session, use the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) and group by `agent_id` or `session_id`. Session usage also appears in the [usage report](../Admin/beta-organization-usage-report-retrieve-messages.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. from the legacy [Usage and Cost API](manage-claude-usage-cost-api.md). To see which account it’s reported under, group that report by one of these fields:

- **`account_id`:** The member who started the session. This covers sessions started in the Console or with a [personal key](manage-claude-authentication.md#key-types) scoped to a single workspace.
- **`service_account_id`:** An Anthropic-managed service account (`svac_...`). This covers sessions started with a workspace key or by a [deployment](managed-agents-scheduled-deployments.md). For this usage, `api_key_id` and `account_id` are `null`.

Anthropic creates one of these service accounts in each workspace where sessions run. It isn’t listed with the service accounts that you create, and the Admin API’s service account endpoints don’t return it. On the **Usage** page, the **Account** filter lists it by its ID. When you set **Group by** to **API key**, its usage is labeled **Managed Agents**.

To see who started a session, check the **Created by** column on the [Sessions](playground.md) page.

## Debugging tips

- **Check session events:** The session reports errors through [`session.error`](managed-agents-reference.md#event-types) events.
- **Review tool results:** Tool failures often explain unexpected agent behavior. The Inspector’s **Tools** tab shows each tool’s failures.
- **Use system prompts:** Add logging instructions to the system prompt so the agent summarizes what it did and what it found.
- **Troubleshoot previews:** If a stream that opts in to event deltas doesn’t behave as you expect, see [Troubleshoot previews](managed-agents-event-deltas.md#troubleshoot-previews).

## Next steps



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session while it runs.

[Session budgets](managed-agents-budgets.md)

Cap a session’s spend with a hard dollar budget enforced at public list rates.

## Availability

Session viewer is in beta on every model.

### API support

Usage

Always on

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
