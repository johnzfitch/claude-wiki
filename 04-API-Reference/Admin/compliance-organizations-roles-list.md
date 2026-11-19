---
title: "List Compliance Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/roles/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:09Z"
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

# List Compliance Roles

Copy page



API version 2026-10-21

GET/v1/compliance/organizations/{org_uuid}/roles

List Compliance Roles

##### Path parameters

org_uuid: string



The organization UUID

##### Query parameters



limit: optional number



Maximum results (default: 500, max: 1000)

default500

minimum1

maximum1000

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

data: array of object{ id, created_at, description, 2 more }



List of roles

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

has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Roles

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
