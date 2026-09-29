---
title: "Vaults - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:51Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fvaults)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Create Vault


List Vaults


Get Vault


Update Vault


Delete Vault


Archive Vault

Credentials

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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)

# Vaults

##### [Create Vault](/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](/docs/en/api/http/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

##### Models



BetaManagedAgentsDeletedVault object{ type: "vault_deleted", id }



Confirmation of a deleted vault.

type: "vault_deleted"



id: string



Unique identifier of the deleted vault.



BetaManagedAgentsVault object{ type: "vault", id, archived_at, 4 more }



A vault that stores credentials for use by agents during sessions.

type: "vault"



id: string



Unique identifier for the vault.



archived_at: string or null



When the vault was archived. Null if not archived.

formatdate-time



created_at: string



A timestamp in RFC 3339 format

formatdate-time

display_name: string



Human-readable name for the vault.

metadata: map\[string\]



Arbitrary key-value metadata attached to the vault.



updated_at: string



A timestamp in RFC 3339 format

formatdate-time

#### Vaults[Credentials](/docs/en/api/http/beta/vaults/credentials)

##### [Create Credential](/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate
