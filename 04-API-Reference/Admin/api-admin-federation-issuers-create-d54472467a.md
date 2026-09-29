---
title: "Create Federation Issuer - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_issuers/create"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:43:00Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Ffederation_issuers%2Fcreate)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings


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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

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


Create Federation Issuer


Get Federation Issuer


List Federation Issuers


Update Federation Issuer


Archive Federation Issuer

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Admin](/docs/en/api/http/admin)
3.  [Federation Issuers](/docs/en/api/http/admin/federation_issuers)

# Create Federation Issuer

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Register an OIDC issuer that Anthropic will trust for workload identity federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and takes one of three shapes selected by `type`: `discovery` (resolve keys through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS URL), or `inline` (provide a static key set). When `jwks.type` is `discovery` and no `discovery_base` is set, the issuer URL must be publicly reachable over HTTPS so Anthropic can fetch the discovery document; for `explicit_url` and `inline` modes the issuer URL is only matched as the JWT's `iss` claim and is not fetched.

##### Headers



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

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

maxLength255

minLength1

check_jti: optional boolean or null



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.



jwks: optional object{ type, ca_cert_pem, discovery_base } or object{ type, url, ca_cert_pem } or object{ keys, type }



How signing keys are obtained. Defaults to OIDC discovery.

One of the following:



Discovery object{ type, ca_cert_pem, discovery_base }

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

ExplicitURL object{ type, url, ca_cert_pem }

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

Inline object{ keys, type }



JWKS supplied directly; no network fetch.



keys: array of map\[unknown\]



Inline JWK objects.

minItems1

type: "inline"





max_jwt_lifetime_seconds: optional number or null



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

maximum176400

exclusiveMinimum0

##### Returns



FederationIssuer object{ id, archived_at, archived_by_actor_id, 12 more }



Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

Create Federation Issuer

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
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
