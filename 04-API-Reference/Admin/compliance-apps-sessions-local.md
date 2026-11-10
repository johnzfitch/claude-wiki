---
title: "Local - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/local"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-08T06:25:19Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions)

# Local

Copy page



API version 2026-10-21

##### [List local sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/list)

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

##### [Retrieve a local session](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/retrieve)

GET/v1/compliance/apps/sessions/local/{local_session_id}

Retrieve one local session.

##### Models



LocalRetrieveResponse object{ type: "compliance_local_session", id, created_at, 6 more }



A session that a user ran on their own computer in a Claude app while signed in with their organization account.



LocalListResponse object{ type: "compliance_local_session", id, created_at, 6 more }



A session that a user ran on their own computer in a Claude app while signed in with their organization account.

#### Local[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages)

##### [Retrieve local session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.
