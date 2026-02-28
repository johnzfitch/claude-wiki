---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:26:50Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/members/list"
title: "List Workspace Members - Claude API Reference"
---
# List Workspace Members

GET/v1/organizations/workspaces/{workspace_id}/members

List Workspace Members

##### Path ParametersExpand Collapse 

workspace_id: string

ID of the Workspace.

##### Query ParametersExpand Collapse 

after_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

##### ReturnsExpand Collapse 

data: array of [WorkspaceMember](/docs/en/api/admin#workspaceMember) { type, user_id, workspace_id, workspace_role }

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

first_id: string

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean

Indicates if there are more results in the requested page direction.

last_id: string

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Workspace Members

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
