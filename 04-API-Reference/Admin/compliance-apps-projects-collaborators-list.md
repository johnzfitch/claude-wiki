---
title: "List project collaborators - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:11Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects)
5.  [Collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators)

# List project collaborators

Copy page



API version 2026-10-21

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals are returned as a discriminated union on `type` — an individual user, an RBAC group, the whole organization, or all holders of an organization-level role.

##### Path parameters

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

##### Query parameters



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Headers



"anthropic-version": string



The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

See [API versions](../Endpoints/versioning.md) for the available versions.

"x-api-key": optional string



##### Returns



data: array of User or Group or Organization or OrganizationRole



List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

One of the following:



User object{ type: "user", granted_at, role, user_id }



An individual user granted a role on a project.



type: "user"



Discriminator marking this as an individual user collaborator

defaultuser



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"



user_id: string or null



Identifier of the user granted access (tagged ID), or null if their account has since been deleted



Group object{ type: "group", granted_at, group_id, role }



An RBAC group granted a role on a project.



type: "group"



Discriminator marking this as a group collaborator

defaultgroup



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

group_id: string



Identifier of the group granted access (tagged ID)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"





Organization object{ type: "organization", granted_at, organization_uuid, role }



An entire organization granted a role on a project.



type: "organization"



Discriminator marking this as an organization-wide grant

defaultorganization



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

organization_uuid: string



UUID of the organization granted access



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"





OrganizationRole object{ type: "organization_role", granted_at, organization_role, role }



All holders of an organization-level role granted a role on a project.



type: "organization_role"



Discriminator marking this as a grant to all organization members holding a specific org-level role

defaultorganization_role



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

organization_role: string



The organization-level role whose holders are granted access



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"



has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



To get the next page, use the 'next_page' from the current response as the 'page' in your next request

List project collaborators

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
