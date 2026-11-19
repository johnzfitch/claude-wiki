---
title: "Update Service Account Workspace Member - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/service_accounts/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:30Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)
4.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts)

# Update Service Account Workspace Member

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit memberships can be updated; to set a role on the implicit default-workspace membership, add the service account explicitly with `POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces return 400. Archived service accounts cannot be updated and are rejected.

##### Path parameters

workspace_id: string



ID of the workspace.

service_account_id: string



ID of the service account.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



workspace_role: [NoBillingWorkspaceRole](https://platform.claude.com/docs/en/api/http/organization/workspaces#no_billing_workspace_role)



New role for the service account in this workspace.

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

Update Service Account Workspace Member

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
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
