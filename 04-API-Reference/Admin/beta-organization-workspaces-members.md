---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/members"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:49Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)

# Members

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



MemberRemoveResponse object{ type: "workspace_member_deleted", user_id, workspace_id }



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
