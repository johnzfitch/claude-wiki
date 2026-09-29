---
title: "Credentials - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults/credentials"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:57Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fvaults%2Fcredentials)

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

# Credentials

##### [Create Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

##### Models



BetaManagedAgentsCredential object{ type: "vault_credential", id, archived_at, 6 more }



A credential stored in a vault. Sensitive fields are never returned in responses.



BetaManagedAgentsCredentialNetworkingParams = [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_unrestricted_credential_networking_params) or [BetaManagedAgentsLimitedCredentialNetworkingParams](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_limited_credential_networking_params)



One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object{ type: "unrestricted" }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"





BetaManagedAgentsLimitedCredentialNetworkingParams object{ type: "limited", allowed_hosts }



Substitute the secret only on requests to the listed hosts.

type: "limited"



allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



BetaManagedAgentsCredentialValidation object{ type: "vault_credential_validation", credential_id, has_refresh_token, 5 more }



Result of live-probing a credential against its configured MCP server.



BetaManagedAgentsCredentialValidationStatus = "valid" or "invalid" or "unknown"



Overall verdict of a credential validation probe.

One of the following:

"valid"



The credential successfully authenticated against its MCP server.

"invalid"



The probe reached the MCP server and was rejected, and a refresh (if attempted) did not recover it.

"unknown"



The probe could not determine validity — for example, a transport error or a successful refresh that was not re-probed.



BetaManagedAgentsDeletedCredential object{ type: "vault_credential_deleted", id }



Confirmation of a deleted credential.

type: "vault_credential_deleted"



id: string



Unique identifier of the deleted credential.



BetaManagedAgentsEnvironmentVariableAuthResponse object{ type: "environment_variable", injection_location, networking, secret_name }



Environment variable credential details. The secret value is never returned.



BetaManagedAgentsEnvironmentVariableCreateParams object{ type: "environment_variable", networking, secret_name, 2 more }



Parameters for creating an environment variable credential.



BetaManagedAgentsEnvironmentVariableUpdateParams object{ type: "environment_variable", injection_location, networking, secret_value }



Parameters for updating an environment variable credential. `secret_name` is immutable.



BetaManagedAgentsInjectionLocationParams object{ body, header }



Where in the outbound request the secret value may be substituted.

body: optional boolean



Substitute when the placeholder appears in the request body.

header: optional boolean



Substitute when the placeholder appears in a request header value.



BetaManagedAgentsInjectionLocationResponse object{ body, header }



Where in the outbound request the secret value is substituted.

body: boolean



Whether the placeholder is substituted in the request body.

header: boolean



Whether the placeholder is substituted in request header values.



BetaManagedAgentsInjectionLocationUpdateParams object{ body, header }



Updated injection location.

body: optional boolean



Substitute when the placeholder appears in the request body.

header: optional boolean



Substitute when the placeholder appears in a request header value.



BetaManagedAgentsLimitedCredentialNetworkingParams object{ type: "limited", allowed_hosts }



Substitute the secret only on requests to the listed hosts.

type: "limited"



allowed_hosts: array of string



Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



BetaManagedAgentsLimitedCredentialNetworkingResponse object{ type: "limited", allowed_hosts }



The secret is substituted only on requests to the listed hosts.

type: "limited"



allowed_hosts: array of string



Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

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

BetaManagedAgentsMCPOAuthCreateParams object{ type: "mcp_oauth", access_token, mcp_server_url, 2 more }



Parameters for creating an MCP OAuth credential.

type: "mcp_oauth"





access_token: string



OAuth access token.

minLength1

maxLength8192



mcp_server_url: string



URL of the MCP server this credential authenticates against.

minLength1

maxLength2047



expires_at: optional string or null



A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_params) { client_id, refresh_token, token_endpoint, 3 more } or null



Refresh token configuration, if the credential supports token refresh.



BetaManagedAgentsMCPOAuthRefreshParams object{ client_id, refresh_token, token_endpoint, 3 more }



OAuth refresh token parameters for creating a credential with refresh support.



BetaManagedAgentsMCPOAuthRefreshResponse object{ client_id, token_endpoint, token_endpoint_auth, 2 more }



OAuth refresh token configuration returned in credential responses.



BetaManagedAgentsMCPOAuthRefreshUpdateParams object{ refresh_token, scope, token_endpoint_auth }



Parameters for updating OAuth refresh token configuration.



BetaManagedAgentsMCPOAuthUpdateParams object{ type: "mcp_oauth", access_token, expires_at, refresh }



Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp_oauth"





access_token: optional string or null



Updated OAuth access token.

minLength1

maxLength8192



expires_at: optional string or null



A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_mcp_oauth_refresh_update_params) { refresh_token, scope, token_endpoint_auth } or null



Updated refresh token configuration.



BetaManagedAgentsMCPProbe object{ http_response, method }



The failing step of an MCP validation probe.



http_response: [BetaManagedAgentsRefreshHTTPResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code } or null



The captured HTTP error response. Null when no HTTP response was received (timeout, DNS, TLS).

body: string



Response body. May be truncated and has sensitive values scrubbed.

body_truncated: boolean



Whether `body` was truncated.

content_type: string



Value of the `Content-Type` response header.



status_code: number



HTTP status code.

formatint32

method: string



The MCP method that failed (for example `initialize` or `tools/list`).



BetaManagedAgentsRefreshHTTPResponse object{ body, body_truncated, content_type, status_code }



An HTTP response captured during a credential validation probe.

body: string



Response body. May be truncated and has sensitive values scrubbed.

body_truncated: boolean



Whether `body` was truncated.

content_type: string



Value of the `Content-Type` response header.



status_code: number



HTTP status code.

formatint32



BetaManagedAgentsRefreshObject object{ http_response, status }



Outcome of a refresh-token exchange attempted during credential validation.



http_response: [BetaManagedAgentsRefreshHTTPResponse](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code } or null



The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

body: string



Response body. May be truncated and has sensitive values scrubbed.

body_truncated: boolean



Whether `body` was truncated.

content_type: string



Value of the `Content-Type` response header.



status_code: number



HTTP status code.

formatint32



status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"



Outcome of the refresh attempt.

One of the following:

"succeeded"



The token endpoint returned a new access token.

"failed"



The token endpoint returned an error response. See `http_response` for detail.

"connect_error"



The token endpoint could not be reached (DNS, TLS, or connection error).

"no_refresh_token"



No refresh token is stored for the credential, so no exchange was attempted.

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

BetaManagedAgentsStaticBearerCreateParams object{ type: "static_bearer", token, mcp_server_url }



Parameters for creating a static bearer token credential.

type: "static_bearer"





token: string



Static bearer token value.

minLength1

maxLength8192



mcp_server_url: string



URL of the MCP server this credential authenticates against.

minLength1

maxLength2047



BetaManagedAgentsStaticBearerUpdateParams object{ type: "static_bearer", token }



Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static_bearer"





token: optional string or null



Updated static bearer token value.

minLength1

maxLength8192



BetaManagedAgentsTokenEndpointAuthBasicParam object{ type: "client_secret_basic", client_secret }



Token endpoint uses HTTP Basic authentication with client credentials.

type: "client_secret_basic"





client_secret: string



OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsTokenEndpointAuthBasicResponse object{ type: "client_secret_basic" }



Token endpoint uses HTTP Basic authentication with client credentials.

type: "client_secret_basic"





BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object{ type: "client_secret_basic", client_secret }



Updated HTTP Basic authentication parameters for the token endpoint.

type: "client_secret_basic"





client_secret: optional string or null



Updated OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsTokenEndpointAuthNoneParam object{ type: "none" }



Token endpoint requires no client authentication.

type: "none"





BetaManagedAgentsTokenEndpointAuthNoneResponse object{ type: "none" }



Token endpoint requires no client authentication.

type: "none"





BetaManagedAgentsTokenEndpointAuthPostParam object{ type: "client_secret_post", client_secret }



Token endpoint uses POST body authentication with client credentials.

type: "client_secret_post"





client_secret: string



OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsTokenEndpointAuthPostResponse object{ type: "client_secret_post" }



Token endpoint uses POST body authentication with client credentials.

type: "client_secret_post"





BetaManagedAgentsTokenEndpointAuthPostUpdateParam object{ type: "client_secret_post", client_secret }



Updated POST body authentication parameters for the token endpoint.

type: "client_secret_post"





client_secret: optional string or null



Updated OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object{ type: "unrestricted" }



Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"





BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object{ type: "unrestricted" }



The secret is substituted on any host the session's Environment network policy permits egress to.
