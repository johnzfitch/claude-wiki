---
title: "Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/roles"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:38Z"
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

# Roles

Copy page



API version 2026-10-21

##### [List Compliance Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org_uuid}/roles

##### [Get Compliance Role](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

##### Models



RoleRetrieveResponse object{ id, created_at, description, 2 more }



Role information for compliance responses.

id: string



Role identifier (tagged ID)



created_at: string or null



Role creation timestamp (RFC 3339)

formatdate-time

description: string



Role description

name: string



Role name



updated_at: string or null



Role last-updated timestamp (RFC 3339)

formatdate-time



RoleListResponse object{ id, created_at, description, 2 more }



Role information for compliance responses.

id: string



Role identifier (tagged ID)



created_at: string or null



Role creation timestamp (RFC 3339)

formatdate-time

description: string



Role description

name: string



Role name



updated_at: string or null



Role last-updated timestamp (RFC 3339)

formatdate-time

#### Roles[Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions)

##### [List Compliance Role Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions
