---
title: "List Workspace Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/members/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:25:32Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

# List Workspace Members

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/workspaces/{workspace_id}/members

List Workspace Members

##### Path parameters

workspace_id: string



ID of the Workspace.

##### Query parameters

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



data: array of [BetaWorkspaceMember](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_workspace_member) { type: "workspace_member", user_id, workspace_id, workspace_role }

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

first_id: string or null



First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean



Indicates if there are more results in the requested page direction.

last_id: string or null



Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Workspace Members

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
