---
title: "List Federation Issuers - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/federation/issuers/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-28T06:33:15Z"
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

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Ffederation%2Fissuers%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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

Issuers


Create Federation Issuer


List Federation Issuers


Get Federation Issuer


Update Federation Issuer


Archive Federation Issuer

Rules

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Federation](https://platform.claude.com/docs/en/api/http/beta/organization/federation)
5.  [Issuers](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers)

# List Federation Issuers

GET/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

##### Query parameters



include_archived: optional boolean



Include archived resources. Defaults to false.

defaultfalse



limit: optional number



Number of results per page.

default20

minimum1

maximum100

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/http-beta.md#anthropic_beta)

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

##### Returns



data: array of [BetaFederationIssuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers#beta_federation_issuer) { type: "federation_issuer", id, archived_at, 12 more }





type: "federation_issuer"



defaultfederation_issuer

id: string



Tagged ID of the federation issuer.



archived_at: string or null



If set, all rules referencing this issuer reject token exchange.

formatdate-time

archived_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

check_jti: boolean



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.



created_at: string



When this issuer was created.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

issuer_url: string



The `iss` claim value. Incoming JWTs must match exactly.



jwks: [BetaJWKSDiscovery](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers#beta_jwks_discovery) or [BetaJWKSExplicitURL](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers#beta_jwks_explicit_url) or [BetaJWKSInline](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers#beta_jwks_inline)



How signing keys are obtained for signature verification.

One of the following:



BetaJWKSDiscovery object{ type: "discovery", ca_cert_pem, discovery_base }



JWKS via the issuer's OIDC discovery document.

type: "discovery"





ca_cert_pem: optional string or null



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192

discovery_base: optional string or null



Set when the discovery URL differs from `issuer_url`.



BetaJWKSExplicitURL object{ type: "explicit_url", url, ca_cert_pem }



JWKS fetched from a fixed endpoint.

type: "explicit_url"





url: string



JWKS endpoint.

minLength1



ca_cert_pem: optional string or null



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192



BetaJWKSInline object{ type: "inline", keys }



JWKS supplied directly; no network fetch.

type: "inline"





keys: array of map\[unknown\]



Inline JWK objects.

minItems1



jwks_polling_disabled_at: string or null



If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

formatdate-time

max_jwt_lifetime_seconds: number



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

name: string



Admin-chosen slug identifier.



poll_status: [BetaFederationIssuerPollStatus](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers#beta_federation_issuer_poll_status) { consecutive_failures, last_fetched_at, next_poll_at } or null



Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

consecutive_failures: number



Consecutive fetch failures since the last success.



last_fetched_at: string or null



When the last successful fetch completed.

formatdate-time



next_poll_at: string or null



When the next fetch is scheduled. Null if paused.

formatdate-time



updated_at: string



When this issuer was last updated.

formatdate-time

updated_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

next_page: string or null



Opaque cursor for the next page, or null if no more results.

List Federation Issuers

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
