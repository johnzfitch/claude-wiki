---
title: "Session operations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-operations"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fsession-operations)

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

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

# Session operations

Copy page



Retrieve, list, update, archive, and delete Claude Managed Agents sessions.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](managed-agents-sessions.md) for creating a session and sending it work.

## Session statuses

Sessions progress through these statuses. See [Start a session](managed-agents-sessions.md) for the session lifecycle.

| Status         | Description                                                                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `idle`         | Agent is waiting for input, including user messages or tool confirmations. Sessions created without `initial_events` start in `idle`.                   |
| `running`      | Agent is actively executing.                                                                                                                            |
| `rescheduling` | Transient error occurred, retrying automatically.                                                                                                       |
| `terminated`   | Session has ended, either because of an unrecoverable error or because it was archived. A session that finishes its work goes `idle`, not `terminated`. |

## Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies and per-tool web settings such as [domain filters](managed-agents-tools.md#restrict-web-search-and-web-fetch-domains), mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent. Updated `allowed_domains` and `blocked_domains` apply to the rest of the session.

Only the agent's `tools` and `mcp_servers` can change after a session is created. To run a session with `model`, `system`, or `skills` values other than the agent's, use [agent configuration overrides](managed-agents-sessions.md#override-agent-configuration-for-a-session) when you create the session. The agent's model configuration, including its [`inference_geo`](../Guides/build-with-claude-data-residency.md) pin, also can't change mid-session: set the pin when you save the agent, or set or clear it for a single session with a `model` override when you create it. The agent's configured `system` field is fixed for the session's lifetime. On models that support it, you can still append system-level guidance mid-session by sending a [`system.message` event](managed-agents-events-and-streaming.md#sending-system-messages).

The semantics of a `tools` or `mcp_servers` update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. To update the agent while the session is running, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#integrating-events) by itself and wait for the session to become `idle`.

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

A session [created with a budget](managed-agents-sessions.md#set-a-session-budget) accepts two kinds of budget update: replacing the cap with a new `max_list_cost`, and removing it by setting `budget` to `null`. Both automatically resume work that paused when the session reached its cap. A replacement cap can be higher or lower than the current one, but it must be strictly greater than the session's consumed list cost, and removal is one-way: a non-null `budget` is accepted only on a session that currently has one, so you can't re-add a removed budget or add one to a session created without it. See [Session budgets](managed-agents-budgets.md#resume-a-session-at-its-budget) for request examples, the error behaviors, and what counts toward list cost.

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



```python
retrieved = client.beta.sessions.retrieve(session.id)
print(f"Status: {retrieved.status}")
```

## Listing sessions

Results from `GET /v1/sessions` are paginated. Use the `limit` query parameter to control the page size. Each response includes a `next_page` cursor; pass it as the `page` parameter on the next request to fetch the following page. `next_page` is `null` when there are no more results.

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you're on the first page.

A `page` cursor is opaque and encodes the `order` of the request that produced it. The `order` query parameter sets the sort direction of the results, `asc` or `desc` by creation time; the default is `desc` (newest first). Reusing a cursor with a different `order` returns a 400 error, as does changing a `created_at` filter so that it excludes the cursor's position. Other query parameters, including the remaining filters and `limit`, can change between paginated requests. For the pagination fields shared across list endpoints, see [Pagination](../Endpoints/overview.md#pagination).

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

Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; to archive one, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#integrating-events) by itself and wait for the session to become `idle`.

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
client.beta.sessions.archive(session.id)
```

## Deleting a session

Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; to delete one, send a [`user.interrupt` event](managed-agents-events-and-streaming.md#integrating-events) by itself and wait for the session to become `idle`.

Memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion. Files you uploaded through the Files API are also unaffected, but files the session itself produced are scoped to it and are permanently deleted along with its filesystem. Download anything you need to keep before deleting the session. An output file written at the end of the last turn can take a few seconds after the session goes idle to appear in the [session's file list](managed-agents-files.md#listing-and-downloading-session-files), so check that the files you expect are listed first.

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
client.beta.sessions.delete(session.id)
```
