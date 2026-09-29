---
title: "Add Workspace To Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/create"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:43:08Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fservice_accounts%2Fworkspaces%2Fcreate)

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

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts


Create Service Account


Get Service Account


List Service Accounts


Update Service Account


Archive Service Account

Workspaces


Add Workspace To Service Account


List Workspaces For Service Account


Remove Workspace From Service Account

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
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/admin/service_accounts)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces)

# Add Workspace To Service Account

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed from the service-account side; both create the same membership. If the service account is already an explicit member of the workspace, its `workspace_role` is replaced with the value supplied here. Archived workspaces return 400. Archived service accounts cannot be added and are rejected.

##### Path parameters

service_account_id: string



ID of the service account.

##### Headers



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Body

workspace_id: string



Tagged workspace ID to add the service account to.



workspace_role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"



Role to assign to the service account in this workspace.

One of the following:

"workspace_admin"



"workspace_developer"



"workspace_restricted_developer"



"workspace_user"



##### Returns

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

Add Workspace To Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "workspace_id": "workspace_id",
          "workspace_role": "workspace_admin"
        }'
```

Response 200



```python
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

##### Returns Examples

Response 200



```python
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
