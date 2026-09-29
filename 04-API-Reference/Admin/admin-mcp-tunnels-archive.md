---
title: "Archive Tunnel - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:43:03Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fmcp_tunnels%2Farchive)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Get Tunnel


List Tunnels


Reveal Tunnel Token


Rotate Tunnel Token


Archive Tunnel

Tunnel Certificates


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)
3.  [MCP Tunnels](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels)

# Archive Tunnel

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Archive a tunnel. Archival is irreversible.

Every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

##### Path parameters

tunnel_id: string



ID of the Tunnel.

##### Headers

"anthropic-beta": array of "mcp-tunnels-2026-05-19"



Required for all Tunnel endpoints.

##### Returns

id: string



ID of the Tunnel.



archived_at: string or null



RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.

formatdate-time



created_at: string



RFC 3339 datetime string indicating when the Tunnel was created.

formatdate-time

display_name: string or null



Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string



Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.



type: "tunnel"



Object type. Always `tunnel` for Tunnels.

defaulttunnel

workspace_id: string or null



ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.

Archive Tunnel

cURL



```python
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

Response 200



```python
{
  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
