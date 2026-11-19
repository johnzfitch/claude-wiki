---
title: "Update Workspace Member - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/members/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:37Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)
4.  [Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members)

# Update Workspace Member

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

Update Workspace Member

##### Path parameters

workspace_id: string



ID of the Workspace.

user_id: string



ID of the User.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



workspace_role: [WorkspaceRole](https://platform.claude.com/docs/en/api/http/organization/workspaces#workspace_role)



New workspace role for the User.

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

##### Returns

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

Update Workspace Member

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
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
