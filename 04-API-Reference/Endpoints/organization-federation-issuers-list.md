---
title: "List Federation Issuers - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/issuers/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:25:32Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Ffederation%2Fissuers%2Flist)





SearchCtrlK

Include beta APIs

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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers)

# List Federation Issuers

Copy page



cURL

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

"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [FederationIssuer](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#federation_issuer) { type: "federation_issuer", id, archived_at, 12 more }

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

jwks: [JWKSDiscovery](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_discovery) or [JWKSExplicitURL](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_explicit_url) or [JWKSInline](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_inline)



How signing keys are obtained for signature verification.

One of the following:



JWKSDiscovery object{ type: "discovery", ca_cert_pem, discovery_base }

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

JWKSExplicitURL object{ type: "explicit_url", url, ca_cert_pem }

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

JWKSInline object{ type: "inline", keys }

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

poll_status: [FederationIssuerPollStatus](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#federation_issuer_poll_status) { consecutive_failures, last_fetched_at, next_poll_at } or null

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
