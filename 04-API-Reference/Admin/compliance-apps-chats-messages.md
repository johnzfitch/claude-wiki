---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/messages"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:20Z"
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
4.  [Chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats)

# Messages

Copy page



API version 2026-10-21

##### [Get chat messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

##### Models



MessageListResponse object{ id, artifacts, content, 4 more }



A single message in a chat conversation.

When the chat's `deleted_at` is set, `content` is an empty list and `files`, `generated_files` and `artifacts` are null.
