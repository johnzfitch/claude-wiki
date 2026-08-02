---
title: "Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/tunnels"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:15Z"
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

Tunnels




cURL

# Tunnels

##### [Create Tunnel](/docs/en/api/beta/tunnels/create)

POST/v1/tunnels

##### [Get Tunnel](/docs/en/api/beta/tunnels/retrieve)

GET/v1/tunnels/{tunnel_id}

##### [List Tunnels](/docs/en/api/beta/tunnels/list)

GET/v1/tunnels

##### [Archive Tunnel](/docs/en/api/beta/tunnels/archive)

POST/v1/tunnels/{tunnel_id}/archive

##### [Reveal Tunnel Token](/docs/en/api/beta/tunnels/reveal_token)

POST/v1/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](/docs/en/api/beta/tunnels/rotate_token)

POST/v1/tunnels/{tunnel_id}/rotate_token

##### ModelsExpand Collapse 



BetaTunnel object { id, archived_at, created_at, 3 more }



An MCP tunnel.

id: string



Unique identifier for the tunnel, prefixed with `tnl_`.

[](#beta_tunnel.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_tunnel.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_tunnel.created_at)

display_name: string



Human-readable name for the tunnel (1-255 characters). Null if unset.

[](#beta_tunnel.display_name)

domain: string



Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

[](#beta_tunnel.domain)

type: "tunnel"



[](#beta_tunnel.type)

[](#beta_tunnel)



BetaTunnelToken object { id, tunnel_token, type }



A tunnel's connector token.

id: string



Stable identifier for the current token value. Changes when the token is rotated.

[](#beta_tunnel_token.id)

tunnel_token: string



The connector token used to run the tunnel. Treat as a credential.

[](#beta_tunnel_token.tunnel_token)

type: "tunnel_token"



[](#beta_tunnel_token.type)

[](#beta_tunnel_token)

#### TunnelsCertificates

##### [Create Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
