---
title: "Get project document content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:36Z"
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

# Get project document content

Copy page



API version 2026-10-21

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

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

content: string



Document text content



created_at: string



Document creation timestamp

formatdate-time

filename: string



Document filename

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

Get project document content

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
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
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "email_address": "jane.doe@example.com"
