---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:49Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Workspaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

##### Models



BetaAllowedInferenceGeo = "global" or "us"



One of the following:

"global"



"us"





BetaDataResidency object{ allowed_inference_geos, default_inference_geo, workspace_geo }





allowed_inference_geos: array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo) or "unrestricted"



Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo)

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

BetaDataResidencyCreateConfig object{ allowed_inference_geos, default_inference_geo, workspace_geo }





allowed_inference_geos: optional array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo)

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

BetaDataResidencyUpdateConfig object{ allowed_inference_geos, default_inference_geo }





allowed_inference_geos: optional array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo)

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

BetaNoBillingWorkspaceRole = "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"

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

BetaWorkspace object{ type: "workspace", id, archived_at, 8 more }





BetaWorkspaceMember object{ type: "workspace_member", user_id, workspace_id, workspace_role }

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

workspace_role: [BetaWorkspaceRole](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_workspace_role)

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

BetaWorkspaceRole = "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more

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

#### Workspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

#### Workspaces[Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### Workspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).
