---
title: "List Credentials - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults/credentials/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:58Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fvaults%2Fcredentials%2Flist)

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


Create Vault


List Vaults


Get Vault


Update Vault


Delete Vault


Archive Vault

Credentials


Create Credential


List Credentials


Get Credential


Update Credential


Delete Credential


Archive Credential


Validate Credential

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
3.  [Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults)
4.  [Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials)

# List Credentials

GET/v1/vaults/{vault_id}/credentials

List Credentials

##### Path parameters

vault_id: string



Identifier of the vault to list credentials for.

##### Query parameters

include_archived: optional boolean



Whether to include archived credentials in the results.



limit: optional number



Maximum number of credentials to return per page. Defaults to 20, maximum 100.

formatint32

page: optional string



Opaque pagination token from a previous `list_credentials` response.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:

"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: optional array of [BetaManagedAgentsCredential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_credential) { type: "vault_credential", id, archived_at, 6 more }



List of credentials.

type: "vault_credential"



id: string



Unique identifier for the credential.



archived_at: string or null



When the credential was archived. Null if not archived.

formatdate-time



auth: [BetaManagedAgentsMCPOAuthAuthResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_mcp_oauth_auth_response) or [BetaManagedAgentsStaticBearerAuthResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_static_bearer_auth_response) or [BetaManagedAgentsEnvironmentVariableAuthResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_environment_variable_auth_response)



Authentication configuration for this credential.

One of the following:



BetaManagedAgentsMCPOAuthAuthResponse object{ type: "mcp_oauth", mcp_server_url, expires_at, refresh }



OAuth credential details for an MCP server.

type: "mcp_oauth"



mcp_server_url: string



URL of the MCP server this credential authenticates against.



expires_at: optional string or null



A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_response) { client_id, token_endpoint, token_endpoint_auth, 2 more } or null



Refresh token configuration, if the credential supports token refresh.



BetaManagedAgentsStaticBearerAuthResponse object{ type: "static_bearer", mcp_server_url }



Static bearer token credential details for an MCP server.

type: "static_bearer"



mcp_server_url: string



URL of the MCP server this credential authenticates against.



BetaManagedAgentsEnvironmentVariableAuthResponse object{ type: "environment_variable", injection_location, networking, secret_name }



Environment variable credential details. The secret value is never returned.



created_at: string



A timestamp in RFC 3339 format

formatdate-time

metadata: map\[string\]



Arbitrary key-value metadata attached to the credential.



updated_at: string



A timestamp in RFC 3339 format

formatdate-time

vault_id: string



Identifier of the vault this credential belongs to.

display_name: optional string or null



Human-readable name for the credential.

next_page: optional string or null



Pagination token for the next page, or null if no more results.

List Credentials

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
