---
title: "List Service Account Workspace Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/service_accounts/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:04Z"
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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits

Service Accounts


Create Service Account Workspace Member


Get Service Account Workspace Member


List Service Account Workspace Members


Update Service Account Workspace Member


Delete Service Account Workspace Member

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

List




# List Service Account Workspace Members

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit` and the `next_page` cursor to paginate. Archived workspaces return 400; use `GET /service_accounts/{id}/workspaces` to audit memberships of an archived workspace. The implicit default-workspace membership is not included in this list. Memberships of archived service accounts are omitted from the results.

##### Path ParametersExpand Collapse 

workspace_id: string



ID of the workspace.

[](#list.workspace_id)

##### Query ParametersExpand Collapse 

limit: optional number



Number of results per page.

[](#list.limit)

page: optional string



Opaque cursor from a previous response's `next_page`.

[](#list.page)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#list.anthropic-beta)

##### ReturnsExpand Collapse 



data: array of object { created_by_actor_id, implicit, service_account_id, 3 more }



created_by_actor_id: string



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

[](#service_account_list_response.created_by_actor_id)

implicit: boolean



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

[](#service_account_list_response.implicit)

service_account_id: string



Tagged service account ID (`svac_...`).

[](#service_account_list_response.service_account_id)

type: "service_account_workspace_member"



[](#service_account_list_response.type)

workspace_id: string



Tagged workspace ID (`wrkspc_...`).

[](#service_account_list_response.workspace_id)



workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace_admin"



[](#service_account_list_response.workspace_role%5B0%5D)

"workspace_billing"



[](#service_account_list_response.workspace_role%5B1%5D)

"workspace_developer"



[](#service_account_list_response.workspace_role%5B2%5D)

"workspace_restricted_developer"



[](#service_account_list_response.workspace_role%5B3%5D)

"workspace_user"



[](#service_account_list_response.workspace_role%5B4%5D)

[](#service_account_list_response.workspace_role)

[](#list)

next_page: string



Opaque cursor for the next page, or null if no more results.

[](#list)

List Service Account Workspace Members



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
