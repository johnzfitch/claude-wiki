---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:10Z"
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


Add Workspace To Service Account


List Workspaces For Service Account


Remove Workspace From Service Account

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

Workspaces




# Workspaces

##### [Add Workspace To Service Account](/docs/en/api/admin/service_accounts/workspaces/create)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [List Workspaces For Service Account](/docs/en/api/admin/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [Remove Workspace From Service Account](/docs/en/api/admin/service_accounts/workspaces/delete)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

##### ModelsExpand Collapse 



WorkspaceCreateResponse object { created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

[](#workspace_create_response.created_by_actor_id)

implicit: boolean



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

[](#workspace_create_response.implicit)

service_account_id: string



Tagged service account ID (`svac_...`).

[](#workspace_create_response.service_account_id)

type: "service_account_workspace_member"



[](#workspace_create_response.type)

workspace_id: string



Tagged workspace ID (`wrkspc_...`).

[](#workspace_create_response.workspace_id)



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



[](#workspace_create_response.workspace_role%5B0%5D)

"workspace_billing"



[](#workspace_create_response.workspace_role%5B1%5D)

"workspace_developer"



[](#workspace_create_response.workspace_role%5B2%5D)

"workspace_restricted_developer"



[](#workspace_create_response.workspace_role%5B3%5D)

"workspace_user"



[](#workspace_create_response.workspace_role%5B4%5D)

[](#workspace_create_response.workspace_role)

[](#workspace_create_response)



WorkspaceListResponse object { created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

[](#workspace_list_response.created_by_actor_id)

implicit: boolean



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

[](#workspace_list_response.implicit)

service_account_id: string



Tagged service account ID (`svac_...`).

[](#workspace_list_response.service_account_id)

type: "service_account_workspace_member"



[](#workspace_list_response.type)

workspace_id: string



Tagged workspace ID (`wrkspc_...`).

[](#workspace_list_response.workspace_id)



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



[](#workspace_list_response.workspace_role%5B0%5D)

"workspace_billing"



[](#workspace_list_response.workspace_role%5B1%5D)

"workspace_developer"



[](#workspace_list_response.workspace_role%5B2%5D)

"workspace_restricted_developer"



[](#workspace_list_response.workspace_role%5B3%5D)

"workspace_user"



[](#workspace_list_response.workspace_role%5B4%5D)

[](#workspace_list_response.workspace_role)

[](#workspace_list_response)



WorkspaceDeleteResponse object { service_account_id, type, workspace_id }



service_account_id: string



Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

[](#workspace_delete_response.service_account_id)

type: "service_account_workspace_member_deleted"



[](#workspace_delete_response.type)

workspace_id: string



Tagged workspace ID (`wrkspc_...`) named in the delete request.

[](#workspace_delete_response.workspace_id)

[](#workspace_delete_response)
