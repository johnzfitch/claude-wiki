---
title: "List Compliance Group Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/groups/members/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:33:43Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Groups](https://platform.claude.com/docs/en/api/http/compliance/groups)
4.  [Members](https://platform.claude.com/docs/en/api/http/compliance/groups/members)

# List Compliance Group Members

Copy page



API version 2026-10-21

GET/v1/compliance/groups/{group_id}/members

List Compliance Group Members

##### Path parameters

group_id: string



The group ID (tagged ID, e.g., rbac_group_abc123)

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

data: array of object{ created_at, email, updated_at, user_id }



List of group members



created_at: string or null



Membership creation timestamp (RFC 3339)

formatdate-time

email: string



Member email address



updated_at: string or null



Membership last-updated timestamp (RFC 3339)

formatdate-time

user_id: string



Member user identifier (tagged ID)

has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Compliance Group Members

cURL



```python
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
