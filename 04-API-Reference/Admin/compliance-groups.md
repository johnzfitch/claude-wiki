---
title: "Groups - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/groups"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:05Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)

# Groups

Copy page



API version 2026-10-21

##### [List Compliance Groups](https://platform.claude.com/docs/en/api/http/compliance/groups/list)

GET/v1/compliance/groups

##### [Get Compliance Group](https://platform.claude.com/docs/en/api/http/compliance/groups/retrieve)

GET/v1/compliance/groups/{group_id}

##### Models



GroupRetrieveResponse object{ id, created_at, description, 4 more }



Group information for compliance responses.

id: string



Group identifier (tagged ID)



created_at: string or null



Group creation timestamp (RFC 3339)

formatdate-time

description: string



Group description

name: string



Group name

roles: array of string or null



Role IDs assigned to this group.

source_type: string



How the group was created ('direct' or 'scim')



updated_at: string or null



Group last-updated timestamp (RFC 3339)

formatdate-time



GroupListResponse object{ id, created_at, description, 4 more }



Group information for compliance responses.

id: string



Group identifier (tagged ID)



created_at: string or null



Group creation timestamp (RFC 3339)

formatdate-time

description: string



Group description

name: string



Group name

roles: array of string or null



Role IDs assigned to this group.

source_type: string



How the group was created ('direct' or 'scim')



updated_at: string or null



Group last-updated timestamp (RFC 3339)

formatdate-time

#### Groups[Members](https://platform.claude.com/docs/en/api/http/compliance/groups/members)

##### [List Compliance Group Members](https://platform.claude.com/docs/en/api/http/compliance/groups/members/list)

GET/v1/compliance/groups/{group_id}/members
