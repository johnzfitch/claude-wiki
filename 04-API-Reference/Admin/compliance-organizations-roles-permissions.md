---
title: "Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions"
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
3.  [Organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations)
4.  [Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles)

# Permissions

Copy page



API version 2026-10-21

##### [List Compliance Role Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

##### Models



PermissionListResponse object{ action, resource_id, resource_type }



Permission granted by a role.

action: string



Action permitted on the resource

resource_id: string



Identifier of the resource the permission applies to

resource_type: string



Type of resource the permission applies to
