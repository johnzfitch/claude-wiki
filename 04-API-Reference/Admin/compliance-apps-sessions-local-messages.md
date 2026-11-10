---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/local/messages"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:33:39Z"
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
5.  [Local](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local)

# Messages

Copy page



API version 2026-10-21

##### [Retrieve local session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.

##### Models



MessageListResponse object{ type: "compliance_local_session_message", id, content, 4 more }



A single user or assistant turn in a local session transcript.
