---
title: "Remove Workspace From Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/service_accounts/workspaces/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:41:39Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fservice_accounts%2Fworkspaces%2Fdelete)

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

# Remove Workspace From Service Account

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`, addressed from the service-account side. Removal is idempotent (returns 200 even if the membership was already removed). A DELETE against the implicit default-workspace membership returns 200 but is a no-op and the membership persists; deleting an explicit default-workspace row reverts to the implicit `workspace_user` membership. Archived workspaces return 400.

##### Path parameters

service_account_id: string



ID of the service account.

workspace_id: string



ID of the workspace.

##### Headers



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Returns

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

Remove Workspace From Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

Response 200



```python
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

##### Returns Examples

Response 200



```python
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
