---
title: "Chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:00Z"
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

# Chats

Copy page



API version 2026-10-21

##### [List chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### [Delete chat](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.

##### Models



ChatListResponse object{ id, created_at, deleted_at, 8 more }



Chat metadata for listing chats (without messages).



ChatDeleteResponse object{ type: "claude_chat_deleted", id }



Response for deleting a Claude chat.



type: optional "claude_chat_deleted"



Constant string confirming deletion

defaultclaude_chat_deleted

id: string



The ID of the Claude chat that was deleted

#### Chats[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages)

##### [Get chat messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

#### Chats[Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files)

##### [Get file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

#### Chats[Generated Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files)

##### [Get Claude-generated file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.
