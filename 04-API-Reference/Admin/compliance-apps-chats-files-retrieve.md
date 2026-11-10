---
title: "Get file metadata - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/files/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:42Z"
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
5.  [Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files)

# Get file metadata

Copy page



API version 2026-10-21

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### Path parameters

claude_file_id: string



The file ID (tagged ID, e.g., claude_file_abc123). Also use this endpoint for any id in `chat_messages[].generated_files[].id` that starts with `claude_file_`.

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

Get file metadata

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ],
  "claude_chat_ids": [
    "claude_chat_def456"
  ]
}
```

##### Returns Examples

Response 200



```python
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
