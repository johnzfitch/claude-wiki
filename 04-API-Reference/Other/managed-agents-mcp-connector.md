---
title: "MCP connector - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/mcp-connector"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["agents", "api", "authentication", "mcp"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fmcp-connector)

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

[Managed Agents](managed-agents-overview.md)Define your agent

# MCP connector

Copy page



Connect MCP servers to your agents for access to external tools and data sources.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Claude Managed Agents supports connecting [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers to your agents. This gives the agent access to external tools, data sources, and services through a standardized protocol.

MCP configuration is split across two steps:

1.  **Agent creation** declares which MCP servers the agent connects to, by name and URL.
2.  **Session creation** supplies authentication for those servers by referencing a pre-registered vault (see [Authenticate with vaults](managed-agents-vaults.md)).

This separation keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.

## Declare MCP servers on the agent

Specify MCP servers in the `mcp_servers` array when creating an agent. Each server needs a `type`, a unique `name`, and a `url`. No authentication tokens are provided at this stage.

Each declared server also needs a matching `mcp_toolset` entry in the `tools` array. The toolset's `mcp_server_name` must match the server's `name`.

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
ant apply github-assistant.md
```

github-assistant.md





```python
---
name: GitHub Assistant
model: claude-opus-5-5
mcp_servers:
  - type: url
    name: github
    url: https://api.githubcopilot.com/mcp/
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
---
```



The MCP toolset defaults to a permission policy of `always_ask`, which requires user approval before each tool call. See [permission policies](managed-agents-permission-policies.md) to configure this behavior.

### `mcp_servers` field reference

Each entry in the `mcp_servers` array defines one connection.

| Field  | Description                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type` | Required. Must be `"url"`.                                                                                                                                                                                                                   |
| `name` | Required. A unique name for this server within the agent (1–255 characters). Used as the `mcp_server_name` in the `tools` array and surfaced on MCP tool events in the [session event stream](managed-agents-events-and-streaming.md). |
| `url`  | Required. The endpoint of the remote MCP server (up to 2,048 characters). See [Supported MCP server types](managed-agents-reference.md#supported-mcp-server-types) for transport requirements.                                         |

Constraints:

- An agent can declare up to 20 MCP servers. Server names must be unique within the array.
- Every `mcp_servers` entry must be referenced by an `mcp_toolset` in the `tools` array, and every `mcp_toolset` must reference a declared server. The API rejects agent definitions with unreferenced servers or dangling toolsets.

## Configure which MCP tools are available

The `mcp_toolset` entry supports a `default_config` object and a `configs` array, applied to the tools the MCP server exposes. Each `configs` entry accepts only `name`, `enabled`, and `permission_policy`. Unlike entries in the built-in agent toolset, MCP tool entries do not take a `type` field, and the [web settings](managed-agents-tools.md#restrict-web-search-and-web-fetch-domains) available on `web_search` and `web_fetch` do not apply to MCP tools. The `name` in each `configs` entry is the bare tool name as reported by the server.

By default all tools exposed by the MCP server are enabled. To enable only specific tools, set `default_config.enabled` to `false` and explicitly enable the tools you want:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "get_issue", "enabled": true },
    { "name": "list_issues", "enabled": true },
    { "name": "add_issue_comment", "enabled": true }
  ]
}
```



This pattern is useful when a server exposes many tools but the agent only needs a few, or when you want tools added by the server operator to stay off until you review them.

To disable specific tools while keeping the rest enabled, omit `default_config` and set `enabled: false` on individual entries:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "configs": [{ "name": "delete_repository", "enabled": false }]
}
```



See [configuring the toolset](managed-agents-tools.md#configuring-the-toolset) for the general `default_config` / `configs` pattern, and [MCP toolset permissions](managed-agents-permission-policies.md#mcp-toolset-permissions) for setting `permission_policy` on MCP tools and handling confirmation requests.

### MCP tool output handling

When an MCP tool output exceeds 100,000 characters (about 25,000 tokens), it is automatically written to a file in the sandbox. The model receives a truncated preview with the file path and can read the full content from there.

## Provide authentication at session creation

When starting a session, pass `vault_ids` to provide credentials for your MCP servers. Vaults are collections of credentials that you register once and reference by ID. See [Authenticate with vaults](managed-agents-vaults.md) for how to create vaults and manage credentials.

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
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
```

Credentials are matched by URL, so the vault must contain a credential whose `mcp_server_url` refers to the same server as the `url` declared in `mcp_servers`. Both URLs are normalized before matching (scheme and host lowercased, default ports and trailing slashes stripped), so differences in host casing, a default port, or a trailing slash don't prevent a match; a different path, subdomain, or non-default port does. If none matches, the connection is attempted unauthenticated. See [Add a credential](managed-agents-vaults.md#add-a-credential) for the `static_bearer` and `mcp_oauth` credential types.

### Handle connection and authentication failures

Session creation does not validate MCP connectivity or credentials. If an MCP server is unreachable or rejects the supplied credential, the session still starts and interaction remains possible. A [`session.error`](managed-agents-events-and-streaming.md) event is emitted with the `mcp_server_name` of the affected server and a `retry_status`:

| Error type                        | Meaning                                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mcp_connection_failed_error`     | The MCP server could not be reached (network error, timeout, or non-authentication HTTP failure).                                                                                                            |
| `mcp_authentication_failed_error` | Authentication with the MCP server failed: the server rejected the credential from the attached vault, required authentication when no matching credential was configured, or an OAuth token refresh failed. |

You can decide whether to block further interaction on this error, trigger a credential rotation, or let the session continue without the affected server's tools. The connection is retried on the next `session.status_idle` to `session.status_running` transition.

## Next steps



[Permission policies](managed-agents-permission-policies.md)

Control when agent and MCP tools run.



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.



[Supported MCP server types](managed-agents-reference.md#supported-mcp-server-types)

Transport requirements for remote MCP servers.
