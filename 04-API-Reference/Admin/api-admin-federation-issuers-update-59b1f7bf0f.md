---
title: "Update Federation Issuer - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_issuers/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:59Z"
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


Create Federation Issuer


Get Federation Issuer


List Federation Issuers


Update Federation Issuer


Archive Federation Issuer

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

Update




# Update Federation Issuer

POST/v1/organizations/federation_issuers/{federation_issuer_id}

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside `workspace:developer` or `workspace:inference` requires a Console session. Requires an OAuth bearer or Console session; Admin API keys are not accepted.

##### Path ParametersExpand Collapse 

federation_issuer_id: string



ID of the federation issuer to update.

[](#update.federation_issuer_id)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#update.anthropic-beta)

##### Body ParametersJSONExpand Collapse 

check_jti: optional boolean



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

[](#update.check_jti)

issuer_url: optional string



Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

[](#update.issuer_url)



jwks: optional object { type, ca_cert_pem, discovery_base } or object { type, url, ca_cert_pem } or object { keys, type }



Replaces the entire JWKS configuration.

One of the following:



Discovery object { type, ca_cert_pem, discovery_base }



JWKS via the issuer's OIDC discovery document.

type: "discovery"



[](#update.jwks%5B0%5D.type)

ca_cert_pem: optional string



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

[](#update.jwks%5B0%5D.ca_cert_pem)

discovery_base: optional string



Set when the discovery URL differs from `issuer_url`.

[](#update.jwks%5B0%5D.discovery_base)

[](#update.jwks%5B0%5D)



ExplicitURL object { type, url, ca_cert_pem }



JWKS fetched from a fixed endpoint.

type: "explicit_url"



[](#update.jwks%5B1%5D.type)

url: string



JWKS endpoint.

[](#update.jwks%5B1%5D.url)

ca_cert_pem: optional string



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

[](#update.jwks%5B1%5D.ca_cert_pem)

[](#update.jwks%5B1%5D)



Inline object { keys, type }



JWKS supplied directly; no network fetch.

keys: array of map\[unknown\]



Inline JWK objects.

[](#update.jwks%5B2%5D.keys)

type: "inline"



[](#update.jwks%5B2%5D.type)

[](#update.jwks%5B2%5D)

[](#update.jwks)

jwks_polling_disabled: optional boolean



Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

[](#update.jwks_polling_disabled)

max_jwt_lifetime_seconds: optional number



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

[](#update.max_jwt_lifetime_seconds)

name: optional string



Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

[](#update.name)

##### ReturnsExpand Collapse 



FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }



Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

id: string



Tagged ID of the federation issuer.

[](#federation_issuer.id)

archived_at: string



If set, all rules referencing this issuer reject token exchange.

[](#federation_issuer.archived_at)

archived_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

[](#federation_issuer.archived_by_actor_id)

check_jti: boolean



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

[](#federation_issuer.check_jti)

created_at: string



When this issuer was created.

[](#federation_issuer.created_at)

created_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

[](#federation_issuer.created_by_actor_id)

issuer_url: string



The `iss` claim value. Incoming JWTs must match exactly.

[](#federation_issuer.issuer_url)



jwks: object { type, ca_cert_pem, discovery_base } or object { type, url, ca_cert_pem } or object { keys, type }



How signing keys are obtained for signature verification.

One of the following:



Discovery object { type, ca_cert_pem, discovery_base }



JWKS via the issuer's OIDC discovery document.

type: "discovery"



[](#federation_issuer.jwks%5B0%5D.type)

ca_cert_pem: optional string



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

[](#federation_issuer.jwks%5B0%5D.ca_cert_pem)

discovery_base: optional string



Set when the discovery URL differs from `issuer_url`.

[](#federation_issuer.jwks%5B0%5D.discovery_base)

[](#federation_issuer.jwks%5B0%5D)



ExplicitURL object { type, url, ca_cert_pem }



JWKS fetched from a fixed endpoint.

type: "explicit_url"



[](#federation_issuer.jwks%5B1%5D.type)

url: string



JWKS endpoint.

[](#federation_issuer.jwks%5B1%5D.url)

ca_cert_pem: optional string



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

[](#federation_issuer.jwks%5B1%5D.ca_cert_pem)

[](#federation_issuer.jwks%5B1%5D)



Inline object { keys, type }



JWKS supplied directly; no network fetch.

keys: array of map\[unknown\]



Inline JWK objects.

[](#federation_issuer.jwks%5B2%5D.keys)

type: "inline"



[](#federation_issuer.jwks%5B2%5D.type)

[](#federation_issuer.jwks%5B2%5D)

[](#federation_issuer.jwks)

jwks_polling_disabled_at: string



If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

[](#federation_issuer.jwks_polling_disabled_at)

max_jwt_lifetime_seconds: number



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

[](#federation_issuer.max_jwt_lifetime_seconds)

name: string



Admin-chosen slug identifier.

[](#federation_issuer.name)



poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }



Status of automatic JWKS polling for a federation issuer.

Anthropic periodically fetches the issuer's signing keys in the background. These fields summarize the most recent fetches so the health of the JWKS endpoint can be monitored.

consecutive_failures: number



Consecutive fetch failures since the last success.

[](#federation_issuer.poll_status.consecutive_failures)

last_fetched_at: string



When the last successful fetch completed.

[](#federation_issuer.poll_status.last_fetched_at)

next_poll_at: string



When the next fetch is scheduled. Null if paused.

[](#federation_issuer.poll_status.next_poll_at)

[](#federation_issuer.poll_status)

type: "federation_issuer"



[](#federation_issuer.type)

updated_at: string



When this issuer was last updated.

[](#federation_issuer.updated_at)

updated_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

[](#federation_issuer.updated_by_actor_id)

[](#federation_issuer)

Update Federation Issuer



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

Response 200



```python
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
```

##### Returns Examples

Response 200



```python
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
