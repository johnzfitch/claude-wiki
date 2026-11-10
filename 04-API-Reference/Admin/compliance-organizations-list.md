---
title: "List organizations - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:24Z"
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

# List organizations

Copy page



API version 2026-10-21

GET/v1/compliance/organizations

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use `limit` and `page` to paginate: each response includes `has_more` and a `next_page` token to pass on the next request.

##### Query parameters



limit: optional number



Maximum results (default: 1000, max: 1000)

default1000

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

data: array of object{ created_at, name, uuid }



List of organizations sorted by creation date, ascending

created_at: string



Organization creation time (RFC 3339 format)

name: string



Organization name

uuid: string



Unique identifier for the organization (UUID format)

has_more: boolean



Whether more records exist beyond the current result set

next_page: optional string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List organizations

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde"
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
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
