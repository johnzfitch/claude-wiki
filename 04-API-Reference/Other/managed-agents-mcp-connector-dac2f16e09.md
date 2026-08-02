---
title: "MCP connector - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/mcp-connector"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:42:16Z"
tags: ["api", "mcp"]
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

MCP connector

Managed Agents/Define your agent

# MCP connector




Connect MCP servers to your agents for access to external tools and data sources.




Claude Managed Agents supports connecting [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers to your agents. This gives the agent access to external tools, data sources, and services through a standardized protocol.

MCP configuration is split across two steps:

1.  **Agent creation** declares which MCP servers the agent connects to, by name and URL.
2.  **Session creation** supplies authentication for those servers by referencing a pre-registered vault (see [Authenticate with vaults](/docs/en/managed-agents/vaults)).

This separation keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Declare MCP servers on the agent

Specify MCP servers in the `mcp_servers` array when creating an agent. Each server needs a `type`, a unique `name`, and a `url`. No authentication tokens are provided at this stage.

Each declared server also needs a matching `mcp_toolset` entry in the `tools` array. The toolset's `mcp_server_name` must match the server's `name`.

curl

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
AGENT_ID=$(ant beta:agents create \
  --name "GitHub Assistant" \
  --model '{id: claude-opus-5}' \
  --mcp-server '{type: url, name: github, url: "https://api.githubcopilot.com/mcp/"}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --raw-output)
```



The MCP toolset defaults to a permission policy of `always_ask`, which requires user approval before each tool call. See [permission policies](/docs/en/managed-agents/permission-policies) to configure this behavior.




`mcp_servers` field reference

Each entry in the `mcp_servers` array defines one connection.

| Field  | Description                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type` | Required. Must be `"url"`.                                                                                                                                                                                                                   |
| `name` | Required. A unique name for this server within the agent (1–255 characters). Used as the `mcp_server_name` in the `tools` array and surfaced on MCP tool events in the [session event stream](/docs/en/managed-agents/events-and-streaming). |
| `url`  | Required. The endpoint of the remote MCP server (up to 2,048 characters). See [Supported MCP server types](/docs/en/managed-agents/reference#supported-mcp-server-types) for transport requirements.                                         |

Constraints:

- An agent can declare up to 20 MCP servers. Server names must be unique within the array.
- Every `mcp_servers` entry must be referenced by an `mcp_toolset` in the `tools` array, and every `mcp_toolset` must reference a declared server. The API rejects agent definitions with unreferenced servers or dangling toolsets.




Configure which MCP tools are available

The `mcp_toolset` entry supports the same `default_config` and `configs` shape as the built-in agent toolset, applied to the tools the MCP server exposes. The `name` in each `configs` entry is the bare tool name as reported by the server.

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

See [configuring the toolset](/docs/en/managed-agents/tools#configuring-the-toolset) for the general `default_config` / `configs` pattern, and [MCP toolset permissions](/docs/en/managed-agents/permission-policies#mcp-toolset-permissions) for setting `permission_policy` on MCP tools and handling confirmation requests.




MCP tool output handling

When an MCP tool output exceeds 100,000 characters (about 25,000 tokens), it is automatically written to a file in the sandbox. The model receives a truncated preview with the file path and can read the full content from there.




Provide authentication at session creation

When starting a session, pass `vault_ids` to provide credentials for your MCP servers. Vaults are collections of credentials that you register once and reference by ID. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and manage credentials.

curl

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

Credentials are matched by URL, so the vault must contain a credential whose `mcp_server_url` refers to the same server as the `url` declared in `mcp_servers`. Both URLs are normalized before matching (scheme and host lowercased, default ports and trailing slashes stripped), so differences in host casing, a default port, or a trailing slash don't prevent a match; a different path, subdomain, or non-default port does. If none matches, the connection is attempted unauthenticated. See [Add a credential](/docs/en/managed-agents/vaults#add-a-credential) for the `static_bearer` and `mcp_oauth` credential types.




Handle connection and authentication failures

Session creation does not validate MCP connectivity or credentials. If an MCP server is unreachable or rejects the supplied credential, the session still starts and interaction remains possible. A [`session.error`](/docs/en/managed-agents/events-and-streaming) event is emitted with the `mcp_server_name` of the affected server and a `retry_status`:

| Error type                        | Meaning                                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mcp_connection_failed_error`     | The MCP server could not be reached (network error, timeout, or non-authentication HTTP failure).                                                                                                            |
| `mcp_authentication_failed_error` | Authentication with the MCP server failed: the server rejected the credential from the attached vault, required authentication when no matching credential was configured, or an OAuth token refresh failed. |

You can decide whether to block further interaction on this error, trigger a credential rotation, or let the session continue without the affected server's tools. The connection is retried on the next `session.status_idle` to `session.status_running` transition.




Next steps




Permission policies

Control when agent and MCP tools run.




Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.




Supported MCP server types

Transport requirements for remote MCP servers.
