---
title: "Tunnel Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:37:50Z"
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


Get Tunnel


List Tunnels


Reveal Tunnel Token


Rotate Tunnel Token


Archive Tunnel

Tunnel Certificates


Create Tunnel Certificate


Get Tunnel Certificate


List Tunnel Certificates


Archive Tunnel Certificate


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

Tunnel certificates




# Tunnel Certificates

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

##### ModelsExpand Collapse 



TunnelCertificateCreateResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.

[](#tunnel_certificate_create_response.id)

archived_at: string



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

[](#tunnel_certificate_create_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

[](#tunnel_certificate_create_response.created_at)

expires_at: string



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

[](#tunnel_certificate_create_response.expires_at)

fingerprint: string



The certificate's SHA-256 fingerprint, as a lowercase hex string.

[](#tunnel_certificate_create_response.fingerprint)

tunnel_id: string



ID of the Tunnel this certificate is registered against.

[](#tunnel_certificate_create_response.tunnel_id)

type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

[](#tunnel_certificate_create_response.type)

[](#tunnel_certificate_create_response)



TunnelCertificateRetrieveResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.

[](#tunnel_certificate_retrieve_response.id)

archived_at: string



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

[](#tunnel_certificate_retrieve_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

[](#tunnel_certificate_retrieve_response.created_at)

expires_at: string



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

[](#tunnel_certificate_retrieve_response.expires_at)

fingerprint: string



The certificate's SHA-256 fingerprint, as a lowercase hex string.

[](#tunnel_certificate_retrieve_response.fingerprint)

tunnel_id: string



ID of the Tunnel this certificate is registered against.

[](#tunnel_certificate_retrieve_response.tunnel_id)

type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

[](#tunnel_certificate_retrieve_response.type)

[](#tunnel_certificate_retrieve_response)



TunnelCertificateListResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.

[](#tunnel_certificate_list_response.id)

archived_at: string



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

[](#tunnel_certificate_list_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

[](#tunnel_certificate_list_response.created_at)

expires_at: string



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

[](#tunnel_certificate_list_response.expires_at)

fingerprint: string



The certificate's SHA-256 fingerprint, as a lowercase hex string.

[](#tunnel_certificate_list_response.fingerprint)

tunnel_id: string



ID of the Tunnel this certificate is registered against.

[](#tunnel_certificate_list_response.tunnel_id)

type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

[](#tunnel_certificate_list_response.type)

[](#tunnel_certificate_list_response)



TunnelCertificateArchiveResponse object { id, archived_at, created_at, 4 more }



id: string



ID of the Tunnel Certificate.

[](#tunnel_certificate_archive_response.id)

archived_at: string



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

[](#tunnel_certificate_archive_response.archived_at)

created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

[](#tunnel_certificate_archive_response.created_at)

expires_at: string



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

[](#tunnel_certificate_archive_response.expires_at)

fingerprint: string



The certificate's SHA-256 fingerprint, as a lowercase hex string.

[](#tunnel_certificate_archive_response.fingerprint)

tunnel_id: string



ID of the Tunnel this certificate is registered against.

[](#tunnel_certificate_archive_response.tunnel_id)

type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

[](#tunnel_certificate_archive_response.type)

[](#tunnel_certificate_archive_response)
