---
title: "Delete chat - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:34:33Z"
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

# Delete chat

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/chats/{claude_chat_id}

Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.

A chat's remote sessions are deleted first. If that deletion cannot be confirmed, the request returns a 503 with error code `chat_delete_remote_sessions_unconfirmed` and leaves the chat unchanged. You can retry the request.

##### Path parameters

claude_chat_id: string



The chat ID (tagged ID, e.g., claude_chat_abc123)

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

type: optional "claude_chat_deleted"



Constant string confirming deletion

defaultclaude_chat_deleted

id: string



The ID of the Claude chat that was deleted

Delete chat

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
