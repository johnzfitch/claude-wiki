---
title: "Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/users"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:15Z"
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

# Users

Copy page



API version 2026-10-21

##### [List organization users](https://platform.claude.com/docs/en/api/http/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

List current user members of an organization.

##### Models



UserListResponse object{ id, created_at, email, 2 more }



User member information for compliance responses.
