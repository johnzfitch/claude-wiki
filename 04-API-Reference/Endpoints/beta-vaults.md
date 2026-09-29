---
title: "Vaults - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:51Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fvaults)

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

# Vaults

##### [Create Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/archive)

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

#### Vaults[Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials)

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
