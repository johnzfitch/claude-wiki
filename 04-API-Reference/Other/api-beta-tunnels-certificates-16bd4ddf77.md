---
title: "Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/tunnels/certificates"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:19Z"
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


Create Tunnel Certificate


Get Tunnel Certificate


List Tunnel Certificates


Archive Tunnel Certificate


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

Certificates




cURL

# Certificates

##### [Create Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

##### ModelsExpand Collapse 



BetaTunnelCertificate object { id, archived_at, created_at, 4 more }



A CA certificate attached to a tunnel.

id: string



Unique identifier for the certificate, prefixed with `tcrt_`.

[](#beta_tunnel_certificate.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_tunnel_certificate.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_tunnel_certificate.created_at)

expires_at: string



A timestamp in RFC 3339 format

[](#beta_tunnel_certificate.expires_at)

fingerprint: string



Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

[](#beta_tunnel_certificate.fingerprint)

tunnel_id: string



ID of the tunnel the certificate is registered against.

[](#beta_tunnel_certificate.tunnel_id)

type: "tunnel_certificate"



[](#beta_tunnel_certificate.type)
