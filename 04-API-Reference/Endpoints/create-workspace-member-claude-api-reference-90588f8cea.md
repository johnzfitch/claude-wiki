---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:26:38Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/members/create"
title: "Create Workspace Member - Claude API Reference"
---
# Create Workspace Member

POST/v1/organizations/workspaces/{workspace_id}/members

Create Workspace Member

##### Path ParametersExpand Collapse 

workspace_id: string

ID of the Workspace.

##### Body ParametersJSONExpand Collapse 

user_id: string

ID of the User.

workspace_role: "workspace_user" or "workspace_developer" or "workspace_admin"

Role of the new Workspace Member. Cannot be "workspace_billing".

Accepts one of the following:

"workspace_user"

"workspace_developer"

"workspace_admin"

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

Create Workspace Member

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_user"
