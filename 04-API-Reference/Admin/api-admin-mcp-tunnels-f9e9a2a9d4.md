---
title: "MCP Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:03Z"
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


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

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


Get Tunnel


List Tunnels


Reveal Tunnel Token


Rotate Tunnel Token


Archive Tunnel

Tunnel Certificates


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Mcp tunnels




# MCP Tunnels

##### [Get Tunnel](/docs/en/api/admin/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

##### [List Tunnels](/docs/en/api/admin/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](/docs/en/api/admin/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](/docs/en/api/admin/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

##### [Archive Tunnel](/docs/en/api/admin/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

##### ModelsExpand Collapse 



MCPTunnelRetrieveResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel.

[](#mcp_tunnel_retrieve_response.id)

archived_at: string



RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.

[](#mcp_tunnel_retrieve_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the Tunnel was created.

[](#mcp_tunnel_retrieve_response.created_at)

display_name: string



Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

[](#mcp_tunnel_retrieve_response.display_name)

domain: string



Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.

[](#mcp_tunnel_retrieve_response.domain)

type: "tunnel"



Object type. Always `tunnel` for Tunnels.

[](#mcp_tunnel_retrieve_response.type)

workspace_id: string



ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.

[](#mcp_tunnel_retrieve_response.workspace_id)

[](#mcp_tunnel_retrieve_response)



MCPTunnelListResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel.

[](#mcp_tunnel_list_response.id)

archived_at: string



RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.

[](#mcp_tunnel_list_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the Tunnel was created.

[](#mcp_tunnel_list_response.created_at)

display_name: string



Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

[](#mcp_tunnel_list_response.display_name)

domain: string



Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.

[](#mcp_tunnel_list_response.domain)

type: "tunnel"



Object type. Always `tunnel` for Tunnels.

[](#mcp_tunnel_list_response.type)

workspace_id: string



ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.

[](#mcp_tunnel_list_response.workspace_id)

[](#mcp_tunnel_list_response)



MCPTunnelRevealTokenResponse object { id, tunnel_token, type }



id: string



Stable identifier for the current token value. Changes when the token is rotated.

[](#mcp_tunnel_reveal_token_response.id)

tunnel_token: string



The tunnel's connection token.

[](#mcp_tunnel_reveal_token_response.tunnel_token)

type: "tunnel_token"



Object type. Always `tunnel_token` for Tunnel Tokens.

[](#mcp_tunnel_reveal_token_response.type)

[](#mcp_tunnel_reveal_token_response)



MCPTunnelRotateTokenResponse object { id, tunnel_token, type }



id: string



Stable identifier for the current token value. Changes when the token is rotated.

[](#mcp_tunnel_rotate_token_response.id)

tunnel_token: string



The tunnel's connection token.

[](#mcp_tunnel_rotate_token_response.tunnel_token)

type: "tunnel_token"



Object type. Always `tunnel_token` for Tunnel Tokens.

[](#mcp_tunnel_rotate_token_response.type)

[](#mcp_tunnel_rotate_token_response)



MCPTunnelArchiveResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel.

[](#mcp_tunnel_archive_response.id)

archived_at: string



RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.

[](#mcp_tunnel_archive_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the Tunnel was created.

[](#mcp_tunnel_archive_response.created_at)

display_name: string



Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

[](#mcp_tunnel_archive_response.display_name)

domain: string



Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.

[](#mcp_tunnel_archive_response.domain)

type: "tunnel"



Object type. Always `tunnel` for Tunnels.

[](#mcp_tunnel_archive_response.type)

workspace_id: string



ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.

[](#mcp_tunnel_archive_response.workspace_id)

[](#mcp_tunnel_archive_response)

#### MCP TunnelsTunnel Certificates

##### [Create Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
