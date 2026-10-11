---
title: "List Workspaces For Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts/workspaces/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:57Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fservice_accounts%2Fworkspaces%2Flist)





SearchCtrlK

Include beta APIs

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


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts


Create Service Account


List Service Accounts


Get Service Account


Update Service Account


Archive Service Account

Workspaces


Add Workspace To Service Account


List Workspaces For Service Account


Remove Workspace From Service Account

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

Plugins

Plugin Marketplaces


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Create a Text Completion Deprecated

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces)

# List Workspaces For Service Account

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that workspace. Use `limit` and the `next_page` cursor to paginate. When the service account has no explicit default-workspace membership, the implicit (`implicit: true`) membership is returned as the first entry on the first page; with `limit=1` the first page may return up to 2 entries (the implicit entry plus one explicit membership) so a pagination cursor can be derived. Memberships are returned only while the service account is active. Without a `page` cursor, an archived service account returns an empty list. A `page` cursor that does not match an active membership returns a 400 invalid-request error. A cursor stops matching when the membership is removed, the workspace is deleted, or the service account is archived. Restart pagination from the first page to recover.

##### Path parameters

service_account_id: string



ID of the service account.

##### Query parameters



limit: optional number



Number of results per page.

default20

minimum1

maximum100

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [ServiceAccountWorkspaceMember](https://platform.claude.com/docs/en/api/http/organization/service_accounts#service_account_workspace_member) { type: "service_account_workspace_member", created_by_actor_id, implicit, 3 more }





type: "service_account_workspace_member"



defaultservice_account_workspace_member

created_by_actor_id: string or null



Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean or null



True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

service_account_id: string



Tagged service account ID (`svac_...`).

workspace_id: string



Tagged workspace ID (`wrkspc_...`).



workspace_role: [WorkspaceRole](https://platform.claude.com/docs/en/api/http/organization/workspaces#workspace_role)

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

next_page: string or null



Opaque cursor for the next page, or null if no more results.

List Workspaces For Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
