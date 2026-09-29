---
title: "MCP Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:40Z"
tags: ["api", "mcp"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fmcp_tunnels)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Admin](/docs/en/api/http/admin)

# MCP Tunnels

##### [Get Tunnel](/docs/en/api/http/admin/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

##### [List Tunnels](/docs/en/api/http/admin/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](/docs/en/api/http/admin/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](/docs/en/api/http/admin/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

##### [Archive Tunnel](/docs/en/api/http/admin/mcp_tunnels/archive)

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

#### MCP Tunnels[Tunnel Certificates](/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
