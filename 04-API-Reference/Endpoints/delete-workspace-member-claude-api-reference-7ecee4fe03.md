---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:12Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/members/delete"
title: "Delete Workspace Member - Claude API Reference"
---

# Delete Workspace Member

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

Delete Workspace Member

##### Path ParametersExpand Collapse 

workspace_id: string

ID of the Workspace.

user_id: string

ID of the User.

##### ReturnsExpand Collapse 

type: "workspace_member_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user_id: string

ID of the User.

workspace_id: string

ID of the Workspace.

Delete Workspace Member

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
