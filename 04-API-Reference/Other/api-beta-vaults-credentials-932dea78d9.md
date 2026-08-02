---
title: "Credentials - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults/credentials"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:24Z"
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

Credentials




cURL

# Credentials

##### [Create Credential](/docs/en/api/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](/docs/en/api/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](/docs/en/api/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](/docs/en/api/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](/docs/en/api/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](/docs/en/api/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](/docs/en/api/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

##### ModelsExpand Collapse 



BetaManagedAgentsCredential object { id, archived_at, auth, 6 more }



A credential stored in a vault. Sensitive fields are never returned in responses.

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

[](#beta_managed_agents_credential)



BetaManagedAgentsCredentialNetworkingParams = [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_unrestricted_credential_networking_params) { type } or [BetaManagedAgentsLimitedCredentialNetworkingParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_limited_credential_networking_params) { allowed_hosts, type }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



[](#beta_managed_agents_unrestricted_credential_networking_params.type)

[](#beta_managed_agents_unrestricted_credential_networking_params)



BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }



Substitute the secret only on requests to the listed hosts.

allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

[](#beta_managed_agents_limited_credential_networking_params.allowed_hosts)

type: "limited"



[](#beta_managed_agents_limited_credential_networking_params.type)

[](#beta_managed_agents_limited_credential_networking_params)

[](#beta_managed_agents_credential_networking_params)

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



BetaManagedAgentsCredentialValidationStatus = "valid" or "invalid" or "unknown"



Overall verdict of a credential validation probe.

One of the following:

"valid"



[](#beta_managed_agents_credential_validation_status%5B0%5D)

"invalid"



[](#beta_managed_agents_credential_validation_status%5B1%5D)

"unknown"



[](#beta_managed_agents_credential_validation_status%5B2%5D)

[](#beta_managed_agents_credential_validation_status)



BetaManagedAgentsDeletedCredential object { id, type }



Confirmation of a deleted credential.

id: string



Unique identifier of the deleted credential.

[](#beta_managed_agents_deleted_credential.id)

type: "vault_credential_deleted"



[](#beta_managed_agents_deleted_credential.type)

[](#beta_managed_agents_deleted_credential)

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



BetaManagedAgentsEnvironmentVariableCreateParams object { networking, secret_name, secret_value, 2 more }



Parameters for creating an environment variable credential.



networking: [BetaManagedAgentsCredentialNetworkingParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_credential_networking_params)



Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



[](#beta_managed_agents_environment_variable_create_params.networking%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_environment_variable_create_params.networking%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }



Substitute the secret only on requests to the listed hosts.

allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

[](#beta_managed_agents_environment_variable_create_params.networking%20%2B%20(resource)%20beta.vaults.credentials.allowed_hosts)

type: "limited"



[](#beta_managed_agents_environment_variable_create_params.networking%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_environment_variable_create_params.networking%20%2B%20(resource)%20beta.vaults.credentials)

[](#beta_managed_agents_environment_variable_create_params.networking)

secret_name: string



Name of the environment variable. Immutable after create.

[](#beta_managed_agents_environment_variable_create_params.secret_name)

secret_value: string



Secret value. Write-only; never returned in responses.

[](#beta_managed_agents_environment_variable_create_params.secret_value)

type: "environment_variable"



[](#beta_managed_agents_environment_variable_create_params.type)



injection_location: optional [BetaManagedAgentsInjectionLocationParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_injection_location_params) { body, header }



Where in the outbound request the secret value may be substituted.

body: optional boolean



Substitute when the placeholder appears in the request body.

[](#beta_managed_agents_environment_variable_create_params.injection_location%20%2B%20(resource)%20beta.vaults.credentials.body)

header: optional boolean



Substitute when the placeholder appears in a request header value.

[](#beta_managed_agents_environment_variable_create_params.injection_location%20%2B%20(resource)%20beta.vaults.credentials.header)

[](#beta_managed_agents_environment_variable_create_params.injection_location)

[](#beta_managed_agents_environment_variable_create_params)



BetaManagedAgentsEnvironmentVariableUpdateParams object { type, injection_location, networking, secret_value }



Parameters for updating an environment variable credential. `secret_name` is immutable.

type: "environment_variable"



[](#beta_managed_agents_environment_variable_update_params.type)



injection_location: optional [BetaManagedAgentsInjectionLocationUpdateParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_injection_location_update_params) { body, header }



Updated injection location.

body: optional boolean



Substitute when the placeholder appears in the request body.

[](#beta_managed_agents_environment_variable_update_params.injection_location%20%2B%20(resource)%20beta.vaults.credentials.body)

header: optional boolean



Substitute when the placeholder appears in a request header value.

[](#beta_managed_agents_environment_variable_update_params.injection_location%20%2B%20(resource)%20beta.vaults.credentials.header)

[](#beta_managed_agents_environment_variable_update_params.injection_location)



networking: optional [BetaManagedAgentsCredentialNetworkingParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_credential_networking_params)



Updated networking scope. Full replacement.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



[](#beta_managed_agents_environment_variable_update_params.networking%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_environment_variable_update_params.networking%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }



Substitute the secret only on requests to the listed hosts.

allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

[](#beta_managed_agents_environment_variable_update_params.networking%20%2B%20(resource)%20beta.vaults.credentials.allowed_hosts)

type: "limited"



[](#beta_managed_agents_environment_variable_update_params.networking%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_environment_variable_update_params.networking%20%2B%20(resource)%20beta.vaults.credentials)

[](#beta_managed_agents_environment_variable_update_params.networking)

secret_value: optional string



Updated secret value.

[](#beta_managed_agents_environment_variable_update_params.secret_value)

[](#beta_managed_agents_environment_variable_update_params)



BetaManagedAgentsInjectionLocationParams object { body, header }



Where in the outbound request the secret value may be substituted.

body: optional boolean



Substitute when the placeholder appears in the request body.

[](#beta_managed_agents_injection_location_params.body)

header: optional boolean



Substitute when the placeholder appears in a request header value.

[](#beta_managed_agents_injection_location_params.header)

[](#beta_managed_agents_injection_location_params)



BetaManagedAgentsInjectionLocationResponse object { body, header }



Where in the outbound request the secret value is substituted.

body: boolean



Whether the placeholder is substituted in the request body.

[](#beta_managed_agents_injection_location_response.body)

header: boolean



Whether the placeholder is substituted in request header values.

[](#beta_managed_agents_injection_location_response.header)

[](#beta_managed_agents_injection_location_response)



BetaManagedAgentsInjectionLocationUpdateParams object { body, header }



Updated injection location.

body: optional boolean



Substitute when the placeholder appears in the request body.

[](#beta_managed_agents_injection_location_update_params.body)

header: optional boolean



Substitute when the placeholder appears in a request header value.

[](#beta_managed_agents_injection_location_update_params.header)

[](#beta_managed_agents_injection_location_update_params)



BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type }



Substitute the secret only on requests to the listed hosts.

allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

[](#beta_managed_agents_limited_credential_networking_params.allowed_hosts)

type: "limited"



[](#beta_managed_agents_limited_credential_networking_params.type)

[](#beta_managed_agents_limited_credential_networking_params)

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

BetaManagedAgentsMCPOAuthCreateParams object { access_token, mcp_server_url, type, 2 more }



Parameters for creating an MCP OAuth credential.

access_token: string



OAuth access token.

[](#beta_managed_agents_mcp_oauth_create_params.access_token)

mcp_server_url: string



URL of the MCP server this credential authenticates against.

[](#beta_managed_agents_mcp_oauth_create_params.mcp_server_url)

type: "mcp_oauth"



[](#beta_managed_agents_mcp_oauth_create_params.type)

expires_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_mcp_oauth_create_params.expires_at)



refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_params) { client_id, refresh_token, token_endpoint, 3 more }



OAuth refresh token parameters for creating a credential with refresh support.

client_id: string



OAuth client ID.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_id)

refresh_token: string



OAuth refresh token.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.refresh_token)

token_endpoint: string



Token endpoint URL used to refresh the access token.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.token_endpoint)



token_endpoint_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_none_param) { type } or [BetaManagedAgentsTokenEndpointAuthBasicParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_basic_param) { client_secret, type } or [BetaManagedAgentsTokenEndpointAuthPostParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_post_param) { client_secret, type }



Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneParam object { type }



Token endpoint requires no client authentication.

type: "none"



[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }



Token endpoint uses HTTP Basic authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_secret)

type: "client_secret_basic"



[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }



Token endpoint uses POST body authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_secret)

type: "client_secret_post"



[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials)

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.token_endpoint_auth)

resource: optional string



OAuth resource indicator.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.resource)

scope: optional string



OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_create_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.scope)

[](#beta_managed_agents_mcp_oauth_create_params.refresh)

[](#beta_managed_agents_mcp_oauth_create_params)



BetaManagedAgentsMCPOAuthRefreshParams object { client_id, refresh_token, token_endpoint, 3 more }



OAuth refresh token parameters for creating a credential with refresh support.

client_id: string



OAuth client ID.

[](#beta_managed_agents_mcp_oauth_refresh_params.client_id)

refresh_token: string



OAuth refresh token.

[](#beta_managed_agents_mcp_oauth_refresh_params.refresh_token)

token_endpoint: string



Token endpoint URL used to refresh the access token.

[](#beta_managed_agents_mcp_oauth_refresh_params.token_endpoint)



token_endpoint_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_none_param) { type } or [BetaManagedAgentsTokenEndpointAuthBasicParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_basic_param) { client_secret, type } or [BetaManagedAgentsTokenEndpointAuthPostParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_post_param) { client_secret, type }



Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneParam object { type }



Token endpoint requires no client authentication.

type: "none"



[](#beta_managed_agents_token_endpoint_auth_none_param.type)

[](#beta_managed_agents_token_endpoint_auth_none_param)



BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }



Token endpoint uses HTTP Basic authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_basic_param.client_secret)

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_param.type)

[](#beta_managed_agents_token_endpoint_auth_basic_param)



BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }



Token endpoint uses POST body authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_post_param.client_secret)

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_param.type)

[](#beta_managed_agents_token_endpoint_auth_post_param)

[](#beta_managed_agents_mcp_oauth_refresh_params.token_endpoint_auth)

resource: optional string



OAuth resource indicator.

[](#beta_managed_agents_mcp_oauth_refresh_params.resource)

scope: optional string



OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_refresh_params.scope)

[](#beta_managed_agents_mcp_oauth_refresh_params)



BetaManagedAgentsMCPOAuthRefreshResponse object { client_id, token_endpoint, token_endpoint_auth, 2 more }



OAuth refresh token configuration returned in credential responses.

client_id: string



OAuth client ID.

[](#beta_managed_agents_mcp_oauth_refresh_response.client_id)

token_endpoint: string



Token endpoint URL used to refresh the access token.

[](#beta_managed_agents_mcp_oauth_refresh_response.token_endpoint)

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

[](#beta_managed_agents_token_endpoint_auth_none_response.type)

[](#beta_managed_agents_token_endpoint_auth_none_response)



BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }



Token endpoint uses HTTP Basic authentication with client credentials.

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_response.type)

[](#beta_managed_agents_token_endpoint_auth_basic_response)



BetaManagedAgentsTokenEndpointAuthPostResponse object { type }



Token endpoint uses POST body authentication with client credentials.

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_response.type)

[](#beta_managed_agents_token_endpoint_auth_post_response)

[](#beta_managed_agents_mcp_oauth_refresh_response.token_endpoint_auth)

resource: optional string



OAuth resource indicator.

[](#beta_managed_agents_mcp_oauth_refresh_response.resource)

scope: optional string



OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_refresh_response.scope)

[](#beta_managed_agents_mcp_oauth_refresh_response)



BetaManagedAgentsMCPOAuthRefreshUpdateParams object { refresh_token, scope, token_endpoint_auth }



Parameters for updating OAuth refresh token configuration.

refresh_token: optional string



Updated OAuth refresh token.

[](#beta_managed_agents_mcp_oauth_refresh_update_params.refresh_token)

scope: optional string



Updated OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_refresh_update_params.scope)



token_endpoint_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_basic_update_param) { type, client_secret } or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_post_update_param) { type, client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_update_param.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_basic_update_param.client_secret)

[](#beta_managed_agents_token_endpoint_auth_basic_update_param)



BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }



Updated POST body authentication parameters for the token endpoint.

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_update_param.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_post_update_param.client_secret)

[](#beta_managed_agents_token_endpoint_auth_post_update_param)

[](#beta_managed_agents_mcp_oauth_refresh_update_params.token_endpoint_auth)

[](#beta_managed_agents_mcp_oauth_refresh_update_params)



BetaManagedAgentsMCPOAuthUpdateParams object { type, access_token, expires_at, refresh }



Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp_oauth"



[](#beta_managed_agents_mcp_oauth_update_params.type)

access_token: optional string



Updated OAuth access token.

[](#beta_managed_agents_mcp_oauth_update_params.access_token)

expires_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_mcp_oauth_update_params.expires_at)



refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](/docs/en/api/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_update_params) { refresh_token, scope, token_endpoint_auth }



Parameters for updating OAuth refresh token configuration.

refresh_token: optional string



Updated OAuth refresh token.

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.refresh_token)

scope: optional string



Updated OAuth scope for the refresh request.

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.scope)



token_endpoint_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_basic_update_param) { type, client_secret } or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](/docs/en/api/beta/vaults/credentials#beta_managed_agents_token_endpoint_auth_post_update_param) { type, client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

type: "client_secret_basic"



[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_secret)

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials)



BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }



Updated POST body authentication parameters for the token endpoint.

type: "client_secret_post"



[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.client_secret)

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials)

[](#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20(resource)%20beta.vaults.credentials.token_endpoint_auth)

[](#beta_managed_agents_mcp_oauth_update_params.refresh)

[](#beta_managed_agents_mcp_oauth_update_params)



BetaManagedAgentsMCPProbe object { http_response, method }

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

[](#beta_managed_agents_mcp_probe.http_response)

method: string



The MCP method that failed (for example `initialize` or `tools/list`).

[](#beta_managed_agents_mcp_probe.method)

[](#beta_managed_agents_mcp_probe)



BetaManagedAgentsRefreshHTTPResponse object { body, body_truncated, content_type, status_code }



An HTTP response captured during a credential validation probe.

body: string



Response body. May be truncated and has sensitive values scrubbed.

[](#beta_managed_agents_refresh_http_response.body)

body_truncated: boolean



Whether `body` was truncated.

[](#beta_managed_agents_refresh_http_response.body_truncated)

content_type: string



Value of the `Content-Type` response header.

[](#beta_managed_agents_refresh_http_response.content_type)

status_code: number



HTTP status code.

[](#beta_managed_agents_refresh_http_response.status_code)

[](#beta_managed_agents_refresh_http_response)



BetaManagedAgentsRefreshObject object { http_response, status }

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

[](#beta_managed_agents_refresh_object.http_response)



status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"



Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"



[](#beta_managed_agents_refresh_object.status%5B0%5D)

"failed"



[](#beta_managed_agents_refresh_object.status%5B1%5D)

"connect_error"



[](#beta_managed_agents_refresh_object.status%5B2%5D)

"no_refresh_token"



[](#beta_managed_agents_refresh_object.status%5B3%5D)

[](#beta_managed_agents_refresh_object.status)

[](#beta_managed_agents_refresh_object)

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

BetaManagedAgentsStaticBearerCreateParams object { token, mcp_server_url, type }



Parameters for creating a static bearer token credential.

token: string



Static bearer token value.

[](#beta_managed_agents_static_bearer_create_params.token)

mcp_server_url: string



URL of the MCP server this credential authenticates against.

[](#beta_managed_agents_static_bearer_create_params.mcp_server_url)

type: "static_bearer"



[](#beta_managed_agents_static_bearer_create_params.type)

[](#beta_managed_agents_static_bearer_create_params)



BetaManagedAgentsStaticBearerUpdateParams object { type, token }



Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static_bearer"



[](#beta_managed_agents_static_bearer_update_params.type)

token: optional string



Updated static bearer token value.

[](#beta_managed_agents_static_bearer_update_params.token)

[](#beta_managed_agents_static_bearer_update_params)



BetaManagedAgentsTokenEndpointAuthBasicParam object { client_secret, type }



Token endpoint uses HTTP Basic authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_basic_param.client_secret)

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_param.type)

[](#beta_managed_agents_token_endpoint_auth_basic_param)



BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }



Token endpoint uses HTTP Basic authentication with client credentials.

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_response.type)

[](#beta_managed_agents_token_endpoint_auth_basic_response)



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

type: "client_secret_basic"



[](#beta_managed_agents_token_endpoint_auth_basic_update_param.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_basic_update_param.client_secret)

[](#beta_managed_agents_token_endpoint_auth_basic_update_param)



BetaManagedAgentsTokenEndpointAuthNoneParam object { type }



Token endpoint requires no client authentication.

type: "none"



[](#beta_managed_agents_token_endpoint_auth_none_param.type)

[](#beta_managed_agents_token_endpoint_auth_none_param)



BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }



Token endpoint requires no client authentication.

type: "none"



[](#beta_managed_agents_token_endpoint_auth_none_response.type)

[](#beta_managed_agents_token_endpoint_auth_none_response)



BetaManagedAgentsTokenEndpointAuthPostParam object { client_secret, type }



Token endpoint uses POST body authentication with client credentials.

client_secret: string



OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_post_param.client_secret)

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_param.type)

[](#beta_managed_agents_token_endpoint_auth_post_param)



BetaManagedAgentsTokenEndpointAuthPostResponse object { type }



Token endpoint uses POST body authentication with client credentials.

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_response.type)

[](#beta_managed_agents_token_endpoint_auth_post_response)



BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret }



Updated POST body authentication parameters for the token endpoint.

type: "client_secret_post"



[](#beta_managed_agents_token_endpoint_auth_post_update_param.type)

client_secret: optional string



Updated OAuth client secret.

[](#beta_managed_agents_token_endpoint_auth_post_update_param.client_secret)

[](#beta_managed_agents_token_endpoint_auth_post_update_param)



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



[](#beta_managed_agents_unrestricted_credential_networking_params.type)

[](#beta_managed_agents_unrestricted_credential_networking_params)



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }



The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"



[](#beta_managed_agents_unrestricted_credential_networking_response.type)

[](#beta_managed_agents_unrestricted_credential_networking_response)
