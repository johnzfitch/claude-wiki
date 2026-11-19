---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/files"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:08Z"
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

# Files

Copy page



API version 2026-10-21

##### [Get file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

##### Models



FileRetrieveResponse object{ id, claude_chat_ids, created_at, 5 more }



File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

Returns metadata only. Use the sibling `/content` endpoint to download the file bytes.

id: string



File ID

claude_chat_ids: array of string



Chats this file is attached to. A file can be referenced by messages across multiple chats.



created_at: string



File creation timestamp

formatdate-time

filename: string or null



Display name of the file, if set

md5: string or null



Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

message_ids: array of string



Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime_type: string or null



MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size_bytes: number or null



Size in bytes of the file's preferred downloadable variant, if known



FileDeleteResponse object{ type: "claude_file_deleted", id }



Response for deleting a compliance file.



type: optional "claude_file_deleted"



Constant string confirming deletion

defaultclaude_file_deleted

id: string



The ID of the file that was deleted
