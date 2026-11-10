---
title: "List Compliance Role Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/roles/permissions/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:25Z"
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
5.  [Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions)

# List Compliance Role Permissions

Copy page



API version 2026-10-21

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

List Compliance Role Permissions

##### Path parameters

org_uuid: string



The organization UUID

role_id: string



The role ID (tagged ID, e.g., rbac_role_abc123)

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

"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns



data: array of object{ action, resource_id, resource_type }



List of permissions

action: string



Action permitted on the resource

resource_id: string



Identifier of the resource the permission applies to

resource_type: string



Type of resource the permission applies to

has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Role Permissions

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "action": "claude_code",
      "resource_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "resource_type": "organization"
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
      "action": "claude_code",
      "resource_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "resource_type": "organization"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
