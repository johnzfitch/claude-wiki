---
title: "Get project document metadata - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:23Z"
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
4.  [Projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects)
5.  [Documents](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents)

# Get project document metadata

Copy page



API version 2026-10-21

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}` endpoint to fetch the document text. The `md5` and `size_bytes` fields here are computed over the UTF-8 encoding of that text, so a DLP consumer can dedupe or match hashes without downloading every document.

##### Path parameters

document_id: string



The document ID (tagged ID, e.g., claude_proj_doc_abc123)

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

Project document identifier (tagged ID)

claude_project_id: string



The project this document belongs to



created_at: string



Document creation timestamp

formatdate-time

filename: string



Document filename

md5: string



Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.



mime_type: "text/plain"



MIME type of the document content, always plain text

defaulttext/plain

size_bytes: number



Size in bytes of the document content (UTF-8 encoded)



user: object{ id, email_address } or null



Document creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

id: string



User identifier (tagged ID)

email_address: string



User's email address

Get project document metadata

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "email_address": "jane.doe@example.com"
  }
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "email_address": "jane.doe@example.com"
