---
title: "Vaults - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:23Z"
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


Create Vault


List Vaults


Get Vault


Update Vault


Delete Vault


Archive Vault

Credentials

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

Vaults




cURL

# Vaults

##### [Create Vault](/docs/en/api/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](/docs/en/api/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](/docs/en/api/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](/docs/en/api/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](/docs/en/api/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](/docs/en/api/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

##### ModelsExpand Collapse 



BetaManagedAgentsDeletedVault object { id, type }



Confirmation of a deleted vault.

id: string



Unique identifier of the deleted vault.

[](#beta_managed_agents_deleted_vault.id)

type: "vault_deleted"



[](#beta_managed_agents_deleted_vault.type)

[](#beta_managed_agents_deleted_vault)



BetaManagedAgentsVault object { id, archived_at, created_at, 4 more }



A vault that stores credentials for use by agents during sessions.

id: string



Unique identifier for the vault.

[](#beta_managed_agents_vault.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_vault.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_vault.created_at)

display_name: string



Human-readable name for the vault.

[](#beta_managed_agents_vault.display_name)

metadata: map\[string\]



Arbitrary key-value metadata attached to the vault.

[](#beta_managed_agents_vault.metadata)

type: "vault"



[](#beta_managed_agents_vault.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_vault.updated_at)

[](#beta_managed_agents_vault)

#### VaultsCredentials

##### [Create Credential](/docs/en/api/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](/docs/en/api/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](/docs/en/api/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](/docs/en/api/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](/docs/en/api/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](/docs/en/api/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](/docs/en/api/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate
