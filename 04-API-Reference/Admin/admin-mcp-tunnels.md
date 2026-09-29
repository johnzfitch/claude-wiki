---
title: "MCP Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:40Z"
tags: ["api", "mcp"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fmcp_tunnels)

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

# MCP Tunnels

##### [Get Tunnel](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

##### [List Tunnels](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

##### [Archive Tunnel](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

##### Models



MCPTunnelRetrieveResponse object{ id, archived_at, created_at, 4 more }



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



MCPTunnelListResponse object{ id, archived_at, created_at, 4 more }



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



MCPTunnelArchiveResponse object{ id, archived_at, created_at, 4 more }



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



MCPTunnelRevealTokenResponse object{ id, tunnel_token, type }



id: string



Stable identifier for the current token value. Changes when the token is rotated.

tunnel_token: string



The tunnel's connection token.



type: "tunnel_token"



Object type. Always `tunnel_token` for Tunnel Tokens.

defaulttunnel_token



MCPTunnelRotateTokenResponse object{ id, tunnel_token, type }



id: string



Stable identifier for the current token value. Changes when the token is rotated.

tunnel_token: string



The tunnel's connection token.



type: "tunnel_token"



Object type. Always `tunnel_token` for Tunnel Tokens.

defaulttunnel_token

#### MCP Tunnels[Tunnel Certificates](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
