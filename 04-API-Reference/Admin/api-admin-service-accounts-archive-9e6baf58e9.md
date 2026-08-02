---
title: "Archive Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/service_accounts/archive"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:34Z"
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


Create Service Account


Get Service Account


List Service Accounts


Update Service Account


Archive Service Account

Workspaces

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

Archive




# Archive Service Account

POST/v1/organizations/service_accounts/{service_account_id}/archive

Archive a service account.

Idempotent; re-archiving returns the service account with its original `archived_at`. Rejected with 400 if any live (non-archived) federation rule still targets this service account, same as issuer archival; archive those rules first or change their target to another service account.

Requires an OAuth bearer or Console session; Admin API keys are not accepted.

##### Path ParametersExpand Collapse 

service_account_id: string



ID of the service account to archive.

[](#archive.service_account_id)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#archive.anthropic-beta)

##### ReturnsExpand Collapse 



ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }



Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).

id: string



Tagged ID of the service account.

[](#service_account.id)

archived_at: string



If set, this service account is archived.

[](#service_account.archived_at)

archived_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

[](#service_account.archived_by_actor_id)

created_at: string



When this service account was created.

[](#service_account.created_at)

created_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that created this service account.

[](#service_account.created_by_actor_id)

description: string



Optional free-text description.

[](#service_account.description)

name: string



Admin-chosen slug identifier.

[](#service_account.name)



organization_role: "admin" or "developer"



Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

One of the following:

"admin"



[](#service_account.organization_role%5B0%5D)

"developer"



[](#service_account.organization_role%5B1%5D)

[](#service_account.organization_role)

type: "service_account"



[](#service_account.type)

updated_at: string



When this service account was last updated.

[](#service_account.updated_at)

updated_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

[](#service_account.updated_by_actor_id)

[](#service_account)

Archive Service Account



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
