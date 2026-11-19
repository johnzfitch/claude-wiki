---
title: "Session operations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-operations"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:47Z"
tags: ["agents", "api"]
---

# Session operations

Copy page



Retrieve, list, update, archive, and delete Claude Managed Agents sessions.

Copy page



[Managed Agents](managed-agents-overview.md)

Beta

[Models](managed-agents-overview.md#feature-availability)  
- All models

[Cloud platforms](managed-agents-overview.md#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Beta header](managed-agents-overview.md#feature-availability)  
- 
  Copy`managed-agents-2026-04-01`

[Data handling](managed-agents-overview.md#feature-data-handling)  
ZDRNot ZDR eligibleHIPAANot HIPAA eligible

Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](managed-agents-sessions.md) for creating a session and sending it work.

## Session statuses

Sessions progress through these statuses. See [Start a session](managed-agents-sessions.md) for the session lifecycle.

| Status | Description |
|----|----|
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions created without `initial_events` start in `idle`. A session can be `idle` while a [workflow run](managed-agents-workflow-runs.md#while-a-run-is-open) is still open, so `idle` alone doesn’t mean that the work is done. See [Know when the work is done](managed-agents-workflow-runs.md#know-when-the-work-is-done). |
| `running` | Agent is actively executing. |
| `rescheduling` | Transient error occurred, retrying automatically. |
| `terminated` | Session has ended, either because of an unrecoverable error or because it was archived. A session that completes its work goes `idle`, not `terminated`. |

## Updating the agent configuration

You can update a session’s `agent.tools` and `agent.mcp_servers`, including permission policies and per-tool web settings such as [domain filters](managed-agents-tools-web-restrictions.md#change-the-lists-mid-session), mid-session without creating a new agent version. Updates are session-local and do not apply to the underlying agent. Updated `allowed_domains` and `blocked_domains` apply to the rest of the session.

Only the agent’s `tools` and `mcp_servers` can change after a session is created. To run a session with `model`, `system`, or `skills` values other than the agent’s, use [agent configuration overrides](managed-agents-sessions.md#override-agent-configuration-for-a-session) when you create the session. The agent’s model configuration, including its [`inference_geo`](manage-claude-data-residency.md) pin, also can’t change mid-session: set the pin when you save the agent, or set or clear it for a single session with a `model` override when you create it. The agent’s configured `system` field is fixed for the session’s lifetime. On models that support it, you can still append system-level guidance mid-session by sending a [`system.message` event](managed-agents-events-and-streaming.md#send-system-messages).

The semantics of a `tools` or `mcp_servers` update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. To update the agent while the session is running, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#interrupt-the-agent) by itself and wait for the session to become `idle`. If a [workflow run](managed-agents-workflow-runs.md#while-a-run-is-open) is open, whether it’s running or paused, the update returns a 400 error, even when the session is `idle`. An interrupt doesn’t end a run, so the update still fails after you interrupt the session. Send a `user.message` that [asks the agent to stop its runs](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open), or wait until every run has ended.

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
client.beta.sessions.update(
    session.id,
    agent={
        "tools": [
            {"type": "agent_toolset_20260401"},
            {"type": "mcp_toolset", "mcp_server_name": "linear"},
        ],
        "mcp_servers": [
            {"type": "url", "name": "linear", "url": "https://mcp.linear.app/sse"}
        ],
    },
)
```

## Updating the session budget

A session [created with a budget](managed-agents-sessions.md#set-a-session-budget) accepts two kinds of budget update: replacing the cap with a new `max_list_cost`, and removing it by passing `budget=None`. Both automatically resume work that paused when the session reached its cap. A replacement cap can be higher or lower than the current one, but it must be strictly greater than the session’s consumed list cost. Removal is one-way: a non-null `budget` is accepted only on a session that currently has one. You therefore can’t re-add a removed budget or add one to a session created without it. See [Session budgets](managed-agents-budgets.md#resume-a-session-at-its-budget) for request examples, the error behaviors, and what counts toward list cost.

## Retrieving a session

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
retrieved = client.beta.sessions.retrieve(session.id)
print(f"Status: {retrieved.status}")
```

## Listing sessions

Results from `GET /v1/sessions` are paginated. Use the `limit` query parameter to control the page size. Each response includes a `next_page` cursor; pass it as the `page` parameter on the next request to fetch the following page. `next_page` is `null` when there are no more results.

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you’re on the first page.

A `page` cursor is opaque and encodes the `order` of the request that produced it. The `order` query parameter sets the sort direction of the results, `asc` or `desc` by creation time; the default is `desc` (newest first). Reusing a cursor with a different `order` returns a 400 error, as does changing a `created_at` filter so that it excludes the cursor’s position. Other query parameters, including the remaining filters and `limit`, can change between paginated requests. For the pagination fields shared across list endpoints, see [Pagination](../Endpoints/overview.md#pagination).

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
# Set `limit` low so the results span more than one page.
first_page = client.beta.sessions.list(limit=1, agent_id=agent.id)
# `prev_page` is None on the first page; `next_page` is None on the last.
print(f"prev_page: {first_page.prev_page}")
print(f"next_page: {first_page.next_page}")

# Pass `next_page` back as `page` to fetch the next page.
second_page = client.beta.sessions.list(
    limit=1, agent_id=agent.id, page=first_page.next_page
)
for listed_session in second_page.data:
    print(f"{listed_session.id}: {listed_session.status}")

# Pass `prev_page` back as `page` to return to the previous page.
previous_page = client.beta.sessions.list(
    limit=1, agent_id=agent.id, page=second_page.prev_page
)
for listed_session in previous_page.data:
    print(f"{listed_session.id}: {listed_session.status}")
# For forward-only iteration, the page object is also directly iterable.
```

## Archiving a session

Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; to archive one, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#interrupt-the-agent) by itself and wait for the session to become `idle`. If a [workflow run](managed-agents-workflow-runs.md#while-a-run-is-open) is open, archiving might return a 400 error, even when the session is `idle`, or it might succeed and end the run. Before you archive, send a `user.message` that [asks the agent to stop its runs](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open), or wait until each run has ended. Then archive the session once it’s `idle`.

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
client.beta.sessions.archive(session.id)
```

## Deleting a session

Deleting a session is permanent. It deletes the session’s record, events, and associated sandbox. A `running` session cannot be deleted; to delete one, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#interrupt-the-agent) by itself and wait for the session to become `idle`. If a [workflow run](managed-agents-workflow-runs.md#while-a-run-is-open) is open, deleting might return a 400 error, even when the session is `idle`, or it might succeed. After a delete that succeeds, no `workflow_run` event reports the end of the session’s runs. Before you delete, send a `user.message` that [asks the agent to stop its runs](managed-agents-workflow-runs.md#interrupt-a-session-with-runs-open), or wait until each run has ended. Then delete the session once it’s `idle`.

Memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion. Files you uploaded through the Files API are also unaffected, but files the session itself produced are scoped to it and are permanently deleted along with its filesystem. Download anything you need to keep before deleting the session. An output file written at the end of the last turn can take a few seconds after the session goes idle to appear in the [session’s file list](managed-agents-files.md#listing-and-downloading-session-files), so check that the files you expect are listed first.

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
client.beta.sessions.delete(session.id)
```
