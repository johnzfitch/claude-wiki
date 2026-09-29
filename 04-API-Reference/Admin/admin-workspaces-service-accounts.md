---
title: "Service Accounts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:15Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fworkspaces%2Fservice_accounts)

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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits

Service Accounts


Create Service Account Workspace Member


Get Service Account Workspace Member


List Service Account Workspace Members


Update Service Account Workspace Member


Delete Service Account Workspace Member

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
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/admin/workspaces)

# Service Accounts

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/create)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### Models



ServiceAccountCreateResponse object{ created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string or null



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service_account_id: string



Tagged service account ID (`svac_...`).



type: "service_account_workspace_member"



defaultservice_account_workspace_member

workspace_id: string



Tagged workspace ID (`wrkspc_...`).



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



"workspace_billing"



"workspace_developer"



"workspace_restricted_developer"



"workspace_user"





ServiceAccountRetrieveResponse object{ created_by_actor_id, implicit, service_account_id, 3 more }





ServiceAccountUpdateResponse object{ created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string or null



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service_account_id: string



Tagged service account ID (`svac_...`).



type: "service_account_workspace_member"



defaultservice_account_workspace_member

workspace_id: string



Tagged workspace ID (`wrkspc_...`).



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



"workspace_billing"



"workspace_developer"



"workspace_restricted_developer"



"workspace_user"





ServiceAccountListResponse object{ created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string or null



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service_account_id: string



Tagged service account ID (`svac_...`).



type: "service_account_workspace_member"



defaultservice_account_workspace_member

workspace_id: string



Tagged workspace ID (`wrkspc_...`).



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



"workspace_billing"



"workspace_developer"



"workspace_restricted_developer"



"workspace_user"





ServiceAccountDeleteResponse object{ service_account_id, type, workspace_id }



service_account_id: string



Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.



type: "service_account_workspace_member_deleted"



defaultservice_account_workspace_member_deleted

workspace_id: string



Tagged workspace ID (`wrkspc_...`) named in the delete request.
