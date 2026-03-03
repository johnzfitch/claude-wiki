---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:11Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/members/update"
title: "Update Workspace Member - Claude API Reference"
---

# Update Workspace Member

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

Update Workspace Member

##### Path ParametersExpand Collapse 

workspace_id: string

ID of the Workspace.

user_id: string

ID of the User.

##### Body ParametersJSONExpand Collapse 

workspace_role: "workspace_user" or "workspace_developer" or "workspace_admin" or "workspace_billing"

New workspace role for the User.

Accepts one of the following:

"workspace_user"

"workspace_developer"

"workspace_admin"

"workspace_billing"

##### ReturnsExpand Collapse 

WorkspaceMember = object { type, user_id, workspace_id, workspace_role }

type: "workspace_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

user_id: string

ID of the User.

workspace_id: string

ID of the Workspace.

workspace_role: "workspace_user" or "workspace_developer" or "workspace_admin" or "workspace_billing"

Role of the Workspace Member.

Accepts one of the following:

"workspace_user"

"workspace_developer"

"workspace_admin"

"workspace_billing"

Update Workspace Member

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "workspace_role": "workspace_user"
