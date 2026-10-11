---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:18Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fworkspaces)

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

Users

Workspaces


List Workspaces


Create Workspace


Get Workspace


Update Workspace


Archive Workspace

Rate Limits

Members

Service Accounts

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

A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Workspaces

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

##### Models



AllowedInferenceGeo = "global" or "us"



One of the following:

"global"



"us"





DataResidency object{ allowed_inference_geos, default_inference_geo, workspace_geo }





allowed_inference_geos: array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo) or "unrestricted"



Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:



Geos = array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo)



One of the following:

"global"



"us"



"unrestricted"





default_inference_geo: "global" or "us"



Default inference geo applied when requests omit the parameter.

One of the following:

"global"



"us"



workspace_geo: "us"



Geographic region for workspace data storage. Immutable after creation.



DataResidencyCreateConfig object{ allowed_inference_geos, default_inference_geo, workspace_geo }





allowed_inference_geos: optional array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo)



One of the following:

"global"



"us"



"unrestricted"





default_inference_geo: optional "global" or "us" or null



Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"



"us"



workspace_geo: optional "us" or null



Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.



DataResidencyUpdateConfig object{ allowed_inference_geos, default_inference_geo }





allowed_inference_geos: optional array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo)



One of the following:

"global"



"us"



"unrestricted"





default_inference_geo: optional "global" or "us" or null



Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"



"us"





NoBillingWorkspaceRole = "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"



One of the following:

"workspace_admin"



"workspace_developer"



"workspace_restricted_developer"



"workspace_user"





Workspace object{ type: "workspace", id, archived_at, 7 more }





WorkspaceMember object{ type: "workspace_member", user_id, workspace_id, workspace_role }





type: "workspace_member"



Object type.

For Workspace Members, this is always `"workspace_member"`.

defaultworkspace_member

user_id: string



ID of the User.

workspace_id: string



ID of the Workspace.



workspace_role: [WorkspaceRole](https://platform.claude.com/docs/en/api/http/organization/workspaces#workspace_role)



Role of the Workspace Member.

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

WorkspaceRole = "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more



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

#### Workspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

#### Workspaces[Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members)

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### Workspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).
