---
title: "List project attachments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:03Z"
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
5.  [Attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments)

# List project attachments

Copy page



API version 2026-10-21

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id. This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

##### Path parameters

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

##### Query parameters



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns



data: array of ProjectFile or ProjectDoc



List of attachments sorted chronologically by created_at, tie break by id

One of the following:



ProjectFile object{ type: "project_file", id, created_at, 4 more }



File attachment reference for compliance responses.



type: "project_file"



Discriminator marking this as a binary file

defaultproject_file

id: string



File identifier (e.g., 'claude_file_abcd')



created_at: string



Creation timestamp (RFC 3339 format)

formatdate-time

filename: string



Display name of the file (e.g., 'document.pdf')

md5: string or null



Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

mime_type: string



MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

size_bytes: number or null



Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.



ProjectDoc object{ type: "project_doc", id, created_at, 3 more }



Project document attachment reference for compliance responses.



type: "project_doc"



Discriminator marking this as a plain text document

defaultproject_doc

id: string



Project document identifier (e.g., 'claude_proj_doc_abcd')



created_at: string



Creation timestamp (RFC 3339 format)

formatdate-time

filename: string



Display name of the document (e.g., 'document.txt')



mime_type: "text/plain"



MIME type of the project document, always set to plain text

defaulttext/plain



updated_at: string or null



Last-modified timestamp of the document. Reserved for future use — currently always null.

formatdate-time

has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



To get the next page, use the 'next_page' from the current response as the 'page' in your next request

List project attachments

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
