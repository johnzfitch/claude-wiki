---
title: "Validate Credential - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:25Z"
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


Create Vault


List Vaults


Get Vault


Update Vault


Delete Vault


Archive Vault

Credentials


Create Credential


List Credentials


Get Credential


Update Credential


Delete Credential


Archive Credential


Validate Credential

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

Mcp oauth validate




cURL

# Validate Credential

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

Validate Credential

##### Path ParametersExpand Collapse 

vault_id: string



[](#mcp_oauth_validate.vault_id)

credential_id: string



[](#mcp_oauth_validate.credential_id)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#mcp_oauth_validate.betas)

##### ReturnsExpand Collapse 



BetaManagedAgentsCredentialValidation object { credential_id, has_refresh_token, mcp_probe, 5 more }



Result of live-probing a credential against its configured MCP server.

credential_id: string



Unique identifier of the credential that was validated.

[](#beta_managed_agents_credential_validation.credential_id)

has_refresh_token: boolean



Whether the credential has a refresh token configured.

[](#beta_managed_agents_credential_validation.has_refresh_token)



mcp_probe: [BetaManagedAgentsMCPProbe](/docs/en/api/beta/vaults/credentials#beta_managed_agents_mcp_probe) { http_response, method }



The failing step of an MCP validation probe.



http_response: [BetaManagedAgentsRefreshHTTPResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code }



An HTTP response captured during a credential validation probe.

body: string



Response body. May be truncated and has sensitive values scrubbed.

[](#beta_managed_agents_mcp_probe.http_response%20%2B%20(resource)%20beta.vaults.credentials.body)

body_truncated: boolean



Whether `body` was truncated.

[](#beta_managed_agents_mcp_probe.http_response%20%2B%20(resource)%20beta.vaults.credentials.body_truncated)

content_type: string



Value of the `Content-Type` response header.

[](#beta_managed_agents_mcp_probe.http_response%20%2B%20(resource)%20beta.vaults.credentials.content_type)

status_code: number



HTTP status code.

[](#beta_managed_agents_mcp_probe.http_response%20%2B%20(resource)%20beta.vaults.credentials.status_code)

[](#beta_managed_agents_credential_validation.mcp_probe%20%2B%20(resource)%20beta.vaults.credentials.http_response)

method: string



The MCP method that failed (for example `initialize` or `tools/list`).

[](#beta_managed_agents_credential_validation.mcp_probe%20%2B%20(resource)%20beta.vaults.credentials.method)

[](#beta_managed_agents_credential_validation.mcp_probe)



refresh: [BetaManagedAgentsRefreshObject](/docs/en/api/beta/vaults/credentials#beta_managed_agents_refresh_object) { http_response, status }



Outcome of a refresh-token exchange attempted during credential validation.



http_response: [BetaManagedAgentsRefreshHTTPResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code }



An HTTP response captured during a credential validation probe.

body: string



Response body. May be truncated and has sensitive values scrubbed.

[](#beta_managed_agents_refresh_object.http_response%20%2B%20(resource)%20beta.vaults.credentials.body)

body_truncated: boolean



Whether `body` was truncated.

[](#beta_managed_agents_refresh_object.http_response%20%2B%20(resource)%20beta.vaults.credentials.body_truncated)

content_type: string



Value of the `Content-Type` response header.

[](#beta_managed_agents_refresh_object.http_response%20%2B%20(resource)%20beta.vaults.credentials.content_type)

status_code: number



HTTP status code.

[](#beta_managed_agents_refresh_object.http_response%20%2B%20(resource)%20beta.vaults.credentials.status_code)

[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.http_response)



status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"



Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"



[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.status%5B0%5D)

"failed"



[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.status%5B1%5D)

"connect_error"



[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.status%5B2%5D)

"no_refresh_token"



[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.status%5B3%5D)

[](#beta_managed_agents_credential_validation.refresh%20%2B%20(resource)%20beta.vaults.credentials.status)

[](#beta_managed_agents_credential_validation.refresh)



status: [BetaManagedAgentsCredentialValidationStatus](/docs/en/api/beta/vaults/credentials#beta_managed_agents_credential_validation_status)



Overall verdict of a credential validation probe.

One of the following:

"valid"



[](#beta_managed_agents_credential_validation.status%20%2B%20(resource)%20beta.vaults.credentials%5B0%5D)

"invalid"



[](#beta_managed_agents_credential_validation.status%20%2B%20(resource)%20beta.vaults.credentials%5B1%5D)

"unknown"



[](#beta_managed_agents_credential_validation.status%20%2B%20(resource)%20beta.vaults.credentials%5B2%5D)

[](#beta_managed_agents_credential_validation.status)

type: "vault_credential_validation"



[](#beta_managed_agents_credential_validation.type)

validated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_credential_validation.validated_at)

vault_id: string



Identifier of the vault containing the credential.

[](#beta_managed_agents_credential_validation.vault_id)

[](#beta_managed_agents_credential_validation)

Validate Credential

cURL



```python
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/mcp_oauth_validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

##### Returns Examples

Response 200



```python
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
