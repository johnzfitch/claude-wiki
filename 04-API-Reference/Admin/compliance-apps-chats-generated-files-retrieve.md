---
title: "Get Claude-generated file metadata - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:02Z"
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
5.  [Generated Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files)

# Get Claude-generated file metadata

Copy page



API version 2026-10-21

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

Use the sibling `/content` endpoint to download the bytes.

##### Path parameters

claude_gen_file_id: string



The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from `GET /v1/compliance/apps/chats/{claude_chat_id}/messages`. An id that does not start with `claude_gen_file_` returns a 400 error. `generated_files` can also list ids that start with `claude_file_`; request those from `GET /v1/compliance/apps/chats/files/{claude_file_id}` instead.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns

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

Get Claude-generated file metadata

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
