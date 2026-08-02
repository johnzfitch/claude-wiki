---
title: "Create Tunnel Certificate - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:04Z"
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

Create




# Create Tunnel Certificate

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Register a public CA certificate for the tunnel.

Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. The PEM body must contain exactly one X.509 certificate and no private-key material. A tunnel holds at most two non-archived certificates.

##### Path ParametersExpand Collapse 

tunnel_id: string



ID of the Tunnel.

[](#create.tunnel_id)

##### Header ParametersExpand Collapse 

"anthropic-beta": array of "mcp-tunnels-2026-05-19"



Required for all Tunnel endpoints.

[](#create.anthropic-beta)

##### Body ParametersJSONExpand Collapse 

ca_certificate_pem: string



PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material.

[](#create.ca_certificate_pem)

##### ReturnsExpand Collapse 

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

Create Tunnel Certificate



```python
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\\n...illustrative placeholder, not a real certificate...\\n-----END CERTIFICATE-----\\n"
        }'
```

Response 200



```python
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
