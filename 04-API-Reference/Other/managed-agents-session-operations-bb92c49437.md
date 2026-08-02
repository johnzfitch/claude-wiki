---
title: "Session operations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/session-operations"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:42:18Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Prototype in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

Self-hosted sandboxes

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

MCP tunnels

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[](/login)




Managed Agents

Session operations

Managed Agents/Delegate work to your agent

# Session operations




Retrieve, list, update, archive, and delete Claude Managed Agents sessions.




Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](/docs/en/managed-agents/sessions) for creating a session and sending it work.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Session statuses

Sessions progress through these statuses. See [Start a session](/docs/en/managed-agents/sessions) for the session lifecycle.

| Status         | Description                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `idle`         | Agent is waiting for input, including user messages or tool confirmations. Sessions created without `initial_events` start in `idle`. |
| `running`      | Agent is actively executing.                                                                                                          |
| `rescheduling` | Transient error occurred, retrying automatically.                                                                                     |
| `terminated`   | Session has ended, either because of an unrecoverable error or on completion.                                                         |




Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.

Only the agent's `tools` and `mcp_servers` can change after a session is created. To run a session with `model`, `system`, or `skills` values other than the agent's, use [agent configuration overrides](/docs/en/managed-agents/sessions#override-agent-configuration-for-a-session) when you create the session. The agent's configured `system` field is fixed for the session's lifetime. On models that support it, you can still append system-level guidance mid-session by sending a [`system.message` event](/docs/en/managed-agents/events-and-streaming#sending-system-messages).

The semantics of a `tools` or `mcp_servers` update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. [Interrupt](/docs/en/managed-agents/events-and-streaming#integrating-events) the session if you need to update the agent while it's running.

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
ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML
```




Retrieving a session

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
ant beta:sessions retrieve --session-id "$SESSION_ID"
```




Listing sessions

Results from `GET /v1/sessions` are paginated. Use the `limit` query parameter to control the page size. Each response includes a `next_page` cursor; pass it as the `page` parameter on the next request to fetch the following page. `next_page` is `null` when there are no more results.

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you're on the first page.

A `page` cursor is opaque and encodes the `order` of the request that produced it. The `order` query parameter sets the sort direction of the results, `asc` or `desc` by creation time; the default is `desc` (newest first). Reusing a cursor with a different `order` returns a 400 error; other query parameters, including filters and `limit`, can change between paginated requests. For the pagination fields shared across list endpoints, see [Pagination](/docs/en/api/overview#pagination).

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
# --format raw returns one page envelope with its prev_page and next_page
# cursors; the default output auto-paginates and emits only the sessions.
cursors=$(ant beta:sessions list \
  --agent-id "$AGENT_ID" \
  --limit 1 \
  --format raw \
  --transform '{prev_page,next_page}')
printf '%s\n' "$cursors"

# Pass the next_page cursor back as --page to fetch the next page.
NEXT_PAGE=$(jq -r '.next_page' <<< "$cursors")
ant beta:sessions list \
  --agent-id "$AGENT_ID" \
  --limit 1 \
  --page "$NEXT_PAGE" \
  --format raw \
  --transform '{prev_page,next_page}'
# Pass that response's prev_page as --page to go back the same way.
```




Archiving a session

Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; send an [interrupt event](/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to archive it immediately.

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
ant beta:sessions archive \
  --session-id "$SESSION_ID"
```




Deleting a session

Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; send an [interrupt event](/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to delete it immediately.

Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.

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
ant beta:sessions delete \
  --session-id "$SESSION_ID"
```
