---
title: "Create Federation Issuer - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/issuers/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:35Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Ffederation%2Fissuers%2Fcreate)

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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces


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

Code


Completions


Create a Text Completion Deprecated

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/create).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers)

# Create Federation Issuer

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Register an OIDC issuer that Anthropic will trust for workload identity federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and takes one of three shapes selected by `type`: `discovery` (resolve keys through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS URL), or `inline` (provide a static key set). When `jwks.type` is `discovery` and no `discovery_base` is set, the issuer URL must be publicly reachable over HTTPS so Anthropic can fetch the discovery document; for `explicit_url` and `inline` modes the issuer URL is only matched as the JWT's `iss` claim and is not fetched.

##### Body



issuer_url: string



The `iss` claim value to match against.

minLength1



name: string



Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

minLength1

maxLength255

check_jti: optional boolean or null



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.



jwks: optional [JWKSDiscovery](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_discovery) or [JWKSExplicitURL](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_explicit_url) or [JWKSInline](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_inline)



How signing keys are obtained. Defaults to OIDC discovery.

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

max_jwt_lifetime_seconds: optional number or null



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

minimum1

maximum176400

##### Returns



FederationIssuer object{ type: "federation_issuer", id, archived_at, 12 more }



Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

Create Federation Issuer

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_url": "x",
          "name": "x"
        }'
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
