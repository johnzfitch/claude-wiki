---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/members"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:51Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Members

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/remove)

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
