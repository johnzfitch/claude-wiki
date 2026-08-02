---
title: "List Credentials - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults/credentials/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:25Z"
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

List




cURL

# List Credentials

GET/v1/vaults/{vault_id}/credentials

List Credentials

##### Path ParametersExpand Collapse 

vault_id: string



[](#list.vault_id)

##### Query ParametersExpand Collapse 

include_archived: optional boolean



Whether to include archived credentials in the results.

[](#list.include_archived)

limit: optional number



Maximum number of credentials to return per page. Defaults to 20, maximum 100.

[](#list.limit)

page: optional string



Opaque pagination token from a previous `list_credentials` response.

[](#list.page)

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

[](#list.betas)

##### ReturnsExpand Collapse 



data: optional array of [BetaManagedAgentsCredential](/docs/en/api/beta/vaults/credentials#beta_managed_agents_credential) { id, archived_at, auth, 6 more }



List of credentials.

id: string



Unique identifier for the credential.

[](#beta_managed_agents_credential.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_credential.archived_at)



auth: [BetaManagedAgentsMCPOAuthAuthResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_mcp_oauth_auth_response) { mcp_server_url, type, expires_at, refresh } or [BetaManagedAgentsStaticBearerAuthResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_static_bearer_auth_response) { mcp_server_url, type } or [BetaManagedAgentsEnvironmentVariableAuthResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_environment_variable_auth_response) { injection_location, networking, secret_name, type }



Authentication details for a credential.

One of the following:



BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }



OAuth credential details for an MCP server.

mcp_server_url: string



URL of the MCP server this credential authenticates against.

[](#beta_managed_agents_mcp_oauth_auth_response.mcp_server_url)

type: "mcp_oauth"



[](#beta_managed_agents_mcp_oauth_auth_response.type)

expires_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_mcp_oauth_auth_response.expires_at)



refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_response) { client_id, token_endpoint, token_endpoint_auth, 2 more }



OAuth refresh token configuration returned in credential responses.

client_id: string



OAuth client ID.

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_id)

token_endpoint: string



Token endpoint URL used to refresh the access token.

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.token_endpoint)



token_endpoint_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_none_response) { type } or [BetaManagedAgentsTokenEndpointAuthBasicResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_basic_response) { type } or [BetaManagedAgentsTokenEndpointAuthPostResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_post_response) { type }



Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }



Token endpoint requires no client authentication.

type: "none"



[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }



Token endpoint uses HTTP Basic authentication with client credentials.

type: "client_secret_basic"



[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsTokenEndpointAuthPostResponse object { type }



Token endpoint uses POST body authentication with client credentials.

type: "client_secret_post"



[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials)

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.token_endpoint_auth)

resource: optional string



OAuth resource indicator.

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.resource)

scope: optional string



OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20(resource)%20beta.vaults.credentials.scope)

[](#beta_managed_agents_mcp_oauth_auth_response.refresh)

[](#beta_managed_agents_mcp_oauth_auth_response)



BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }



Static bearer token credential details for an MCP server.

mcp_server_url: string



URL of the MCP server this credential authenticates against.

[](#beta_managed_agents_static_bearer_auth_response.mcp_server_url)

type: "static_bearer"



[](#beta_managed_agents_static_bearer_auth_response.type)

[](#beta_managed_agents_static_bearer_auth_response)



BetaManagedAgentsEnvironmentVariableAuthResponse object { injection_location, networking, secret_name, type }



Environment variable credential details. The secret value is never returned.



injection_location: [BetaManagedAgentsInjectionLocationResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_injection_location_response) { body, header }



Where in the outbound request the secret value is substituted.

body: boolean



Whether the placeholder is substituted in the request body.

[](#beta_managed_agents_environment_variable_auth_response.injection_location%20%2B%20(resource)%20beta.vaults.credentials.body)

header: boolean



Whether the placeholder is substituted in request header values.

[](#beta_managed_agents_environment_variable_auth_response.injection_location%20%2B%20(resource)%20beta.vaults.credentials.header)

[](#beta_managed_agents_environment_variable_auth_response.injection_location)



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_unrestricted_credential_networking_response) { type } or [BetaManagedAgentsLimitedCredentialNetworkingResponse](/docs/en/api/beta/vaults/credentials#beta_managed_agents_limited_credential_networking_response) { allowed_hosts, type }



Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }



The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"



[](#beta_managed_agents_unrestricted_credential_networking_response.type)

[](#beta_managed_agents_unrestricted_credential_networking_response)



BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }



The secret is substituted only on requests to the listed hosts.

allowed_hosts: array of string



Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

[](#beta_managed_agents_limited_credential_networking_response.allowed_hosts)

type: "limited"



[](#beta_managed_agents_limited_credential_networking_response.type)

[](#beta_managed_agents_limited_credential_networking_response)

[](#beta_managed_agents_environment_variable_auth_response.networking)

secret_name: string



Name of the environment variable.

[](#beta_managed_agents_environment_variable_auth_response.secret_name)

type: "environment_variable"



[](#beta_managed_agents_environment_variable_auth_response.type)

[](#beta_managed_agents_environment_variable_auth_response)

[](#beta_managed_agents_credential.auth)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_credential.created_at)

metadata: map\[string\]



Arbitrary key-value metadata attached to the credential.

[](#beta_managed_agents_credential.metadata)

type: "vault_credential"



[](#beta_managed_agents_credential.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_credential.updated_at)

vault_id: string



Identifier of the vault this credential belongs to.

[](#beta_managed_agents_credential.vault_id)

display_name: optional string



Human-readable name for the credential.

[](#beta_managed_agents_credential.display_name)

[](#list)

next_page: optional string



Pagination token for the next page, or null if no more results.

[](#list)

List Credentials

cURL



```python
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
