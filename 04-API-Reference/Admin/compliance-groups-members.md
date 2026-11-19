---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/groups/members"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:12Z"
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

# Members

Copy page



API version 2026-10-21

##### [List Compliance Group Members](https://platform.claude.com/docs/en/api/http/compliance/groups/members/list)

GET/v1/compliance/groups/{group_id}/members

##### Models



MemberListResponse object{ created_at, email, updated_at, user_id }



Group member for compliance responses.

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
