---
title: "Remove Workspace From Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts/workspaces/remove"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:27Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/remove).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces)

# Remove Workspace From Service Account

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns

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

Remove Workspace From Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
