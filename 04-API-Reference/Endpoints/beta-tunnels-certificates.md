---
title: "Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/tunnels/certificates"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:48Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Ftunnels%2Fcertificates)

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


Create Tunnel Certificate


Get Tunnel Certificate


List Tunnel Certificates


Archive Tunnel Certificate


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
3.  [Tunnels](http-beta-tunnels.md)

# Certificates

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

##### Models



BetaTunnelCertificate object{ type: "tunnel_certificate", id, archived_at, 4 more }



A CA certificate attached to a tunnel.

type: "tunnel_certificate"



id: string



Unique identifier for the certificate, prefixed with `tcrt_`.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

formatdate-time



created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires_at: string or null



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

formatdate-time

fingerprint: string



Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

tunnel_id: string



ID of the tunnel the certificate is registered against.
