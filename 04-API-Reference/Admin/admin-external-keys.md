---
title: "External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/external_keys"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:35Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fexternal_keys)





SearchCtrlK

Include beta APIs

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


Create External Key


List External Keys


Get External Key


Update External Key


Delete External Key


Validate External Key

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


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Admin](http-admin.md)

# External Keys

##### [Create External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/create)

POST/v1/organizations/external_keys

##### [List External Keys](https://platform.claude.com/docs/en/api/http/admin/external_keys/list)

GET/v1/organizations/external_keys

##### [Get External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

##### [Update External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

##### Models



ExternalKeyCreateResponse object{ id, attachment, created_at, 5 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).



ExternalKeyRetrieveResponse object{ id, attachment, created_at, 5 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).



ExternalKeyUpdateResponse object{ id, attachment, created_at, 5 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).



ExternalKeyListResponse object{ id, attachment, created_at, 5 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).



ExternalKeyDeleteResponse object{ id, type }



id: string



ID of the deleted External Key.



type: "external_key_deleted"



defaultexternal_key_deleted



ExternalKeyValidateResponse object{ error, status, type }



Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says whether the key works.

error: string or null



Error message when status is `failure`. Null otherwise.



status: "failure" or "success"



`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"failure"



"success"





type: "external_key_validation"



defaultexternal_key_validation
