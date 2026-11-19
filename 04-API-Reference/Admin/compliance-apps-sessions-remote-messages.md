---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote/messages"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-15T06:24:19Z"
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
5.  [Remote](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote)

# Messages

Copy page



API version 2026-10-21

##### [Retrieve remote session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages/list)

GET/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages

Retrieve one remote session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included.

##### Models



MessageListResponse object{ id, content, content_unavailable, 3 more }



A single user or assistant turn in a remote session transcript.

`content` is a discriminated union of `text`, `tool_use`, and `tool_result` blocks.
