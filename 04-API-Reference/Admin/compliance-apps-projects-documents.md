---
title: "Documents - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents"
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

# Documents

Copy page



API version 2026-10-21

##### [Get project document content](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### [Get project document metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

##### [Delete project document](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.

##### Models



DocumentRetrieveResponse object{ id, content, created_at, 2 more }



Project document information for compliance responses.

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



DocumentDeleteResponse object{ type: "claude_project_document_deleted", id }



Response for deleting a project document.



type: "claude_project_document_deleted"



Constant string confirming deletion.

defaultclaude_project_document_deleted

id: string



The ID of the project document that was deleted



DocumentMetadataResponse object{ id, claude_project_id, created_at, 5 more }



Project document metadata for GET /v1/compliance/apps/projects/documents/{document_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`) to fetch the document text content.
