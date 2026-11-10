---
title: "Organizations - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:47Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)

# Organizations

Copy page



API version 2026-10-21

##### [List organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations/list)

GET/v1/compliance/organizations

List organizations under the parent organization.

##### Models



OrganizationListResponse object{ created_at, name, uuid }



Information about an organization.

created_at: string



Organization creation time (RFC 3339 format)

name: string



Organization name

uuid: string



Unique identifier for the organization (UUID format)

#### Organizations[Users](https://platform.claude.com/docs/en/api/http/compliance/organizations/users)

##### [List organization users](https://platform.claude.com/docs/en/api/http/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

List current user members of an organization.

#### Organizations[User Preferences](https://platform.claude.com/docs/en/api/http/compliance/organizations/user_preferences)

##### [List organization members' personal preferences](https://platform.claude.com/docs/en/api/http/compliance/organizations/user_preferences/list)

GET/v1/compliance/organizations/{org_uuid}/user_preferences

This endpoint is in beta.

#### Organizations[Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles)

##### [List Compliance Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org_uuid}/roles

##### [Get Compliance Role](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

#### OrganizationsRoles[Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions)

##### [List Compliance Role Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

#### Organizations[Settings](https://platform.claude.com/docs/en/api/http/compliance/organizations/settings)

##### [Get effective organization settings](https://platform.claude.com/docs/en/api/http/compliance/organizations/settings/retrieve)

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.
