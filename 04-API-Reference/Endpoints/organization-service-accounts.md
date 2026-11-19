---
title: "Service Accounts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:33Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Service Accounts

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/create)

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts/list)

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### Models



ServiceAccount object{ type: "service_account", id, archived_at, 8 more }



Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).



ServiceAccountWorkspaceMember object{ type: "service_account_workspace_member", created_by_actor_id, implicit, 3 more }

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

#### Service Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).
