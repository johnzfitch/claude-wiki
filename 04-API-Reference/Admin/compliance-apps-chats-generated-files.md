---
title: "Generated Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:09Z"
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

# Generated Files

Copy page



API version 2026-10-21

##### [Get Claude-generated file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.

##### Models



GeneratedFileRetrieveResponse object{ id, claude_chat_id, created_at, 4 more }



Metadata for GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}.

Returns metadata only. Use the sibling `/content` endpoint to download the bytes. The owning chat is included since the id is opaque; to find the specific message that produced the file, fetch `/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on `generated_files[].id`.

id: string



Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

claude_chat_id: string



The chat this generated file belongs to



created_at: string or null



File creation timestamp, when available

formatdate-time

filename: string



Display name of the generated file

md5: string or null



Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime_type: string or null



MIME type of the stored file, when available

size_bytes: number or null



Size in bytes of the stored file, when available
