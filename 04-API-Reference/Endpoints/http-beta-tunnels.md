---
title: "Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/tunnels"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:39:20Z"
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

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Ftunnels)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


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


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)

# Tunnels

##### [Create Tunnel](http-beta-tunnels-create.md)

POST/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel](http-beta-tunnels-retrieve.md)

GET/v1/tunnels/{tunnel_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnels](http-beta-tunnels-list.md)

GET/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel](http-beta-tunnels-archive.md)

POST/v1/tunnels/{tunnel_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Reveal Tunnel Token](http-beta-tunnels-reveal-token.md)

POST/v1/tunnels/{tunnel_id}/reveal_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Rotate Tunnel Token](http-beta-tunnels-rotate-token.md)

POST/v1/tunnels/{tunnel_id}/rotate_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### Models



BetaTunnel object{ type: "tunnel", id, archived_at, 3 more }



An MCP tunnel.

type: "tunnel"



id: string



Unique identifier for the tunnel, prefixed with `tnl_`.



archived_at: string or null



RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

formatdate-time



created_at: string



RFC 3339 datetime string indicating when the tunnel was created.

formatdate-time

display_name: string or null



Human-readable name for the tunnel (1-255 characters). Null if unset.

domain: string



Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.



BetaTunnelToken object{ type: "tunnel_token", id, tunnel_token }



A tunnel's connector token.

type: "tunnel_token"



id: string



Stable identifier for the current token value. Changes when the token is rotated.

tunnel_token: string



The connector token used to run the tunnel. Treat as a credential.

#### Tunnels[Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.
