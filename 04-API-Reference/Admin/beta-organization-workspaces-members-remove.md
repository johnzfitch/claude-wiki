---
title: "Delete Workspace Member - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/members/remove"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:26:49Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

# Delete Workspace Member

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

Delete Workspace Member

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

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



type: "workspace_member_deleted"



Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

defaultworkspace_member_deleted

user_id: string



ID of the User.

workspace_id: string



ID of the Workspace.

Delete Workspace Member

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

##### Returns Examples

Response 200



```python
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
