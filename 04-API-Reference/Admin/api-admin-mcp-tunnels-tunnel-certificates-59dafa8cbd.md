---
title: "Tunnel Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:35Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fmcp_tunnels%2Ftunnel_certificates)

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


Create Tunnel Certificate


Get Tunnel Certificate


List Tunnel Certificates


Archive Tunnel Certificate


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
3.  [MCP Tunnels](/docs/en/api/http/admin/mcp_tunnels)

# Tunnel Certificates

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

##### Models



TunnelCertificateCreateResponse object{ id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

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

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel_id: string



ID of the Tunnel this certificate is registered against.



type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel_certificate



TunnelCertificateRetrieveResponse object{ id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

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

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel_id: string



ID of the Tunnel this certificate is registered against.



type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel_certificate



TunnelCertificateListResponse object{ id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

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

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel_id: string



ID of the Tunnel this certificate is registered against.



type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel_certificate



TunnelCertificateArchiveResponse object{ id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

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

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel_id: string



ID of the Tunnel this certificate is registered against.



type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.
