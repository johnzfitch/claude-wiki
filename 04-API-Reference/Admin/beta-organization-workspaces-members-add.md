---
title: "Create Workspace Member - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/members/add"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:55Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

# Create Workspace Member

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces/{workspace_id}/members

Create Workspace Member

##### Path parameters

workspace_id: string



ID of the Workspace.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body

user_id: string



ID of the User.



workspace_role: [BetaNoBillingWorkspaceRole](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_no_billing_workspace_role)



Role of the new Workspace Member. Cannot be `workspace_billing`.

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

Create Workspace Member

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
          "workspace_role": "workspace_admin"
        }'
```

Response 200



```python
{
  "type": "workspace_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

##### Returns Examples

Response 200



```python
{
  "type": "workspace_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
