---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:06Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces"
title: "Workspaces - Claude API Reference"
---

# Workspaces

##### [Create Workspace](/docs/en/api/admin/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](/docs/en/api/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [List Workspaces](/docs/en/api/admin/workspaces/list)

GET/v1/organizations/workspaces

##### [Update Workspace](/docs/en/api/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](/docs/en/api/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### WorkspacesMembers

##### [Create Workspace Member](/docs/en/api/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](/docs/en/api/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](/docs/en/api/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](/docs/en/api/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](/docs/en/api/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### ModelsExpand Collapse 

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
