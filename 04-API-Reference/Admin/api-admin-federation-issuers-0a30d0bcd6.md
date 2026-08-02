---
title: "Federation Issuers - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_issuers"
category: "04-API-Reference/Admin"
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

Federation issuers




# Federation Issuers

##### [Create Federation Issuer](/docs/en/api/admin/federation_issuers/create)

POST/v1/organizations/federation_issuers

##### [Get Federation Issuer](/docs/en/api/admin/federation_issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

##### [List Federation Issuers](/docs/en/api/admin/federation_issuers/list)

GET/v1/organizations/federation_issuers

##### [Update Federation Issuer](/docs/en/api/admin/federation_issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

##### [Archive Federation Issuer](/docs/en/api/admin/federation_issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

##### ModelsExpand Collapse 

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
