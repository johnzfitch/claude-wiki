---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/service_accounts/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:52Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts)

# Workspaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### Models



WorkspaceRemoveResponse object{ type: "service_account_workspace_member_deleted", service_account_id, workspace_id }





type: "service_account_workspace_member_deleted"



defaultservice_account_workspace_member_deleted

service_account_id: string



Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

workspace_id: string



Tagged workspace ID (`wrkspc_...`) named in the delete request.
