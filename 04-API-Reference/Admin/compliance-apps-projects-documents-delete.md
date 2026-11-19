---
title: "Delete project document - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:34:35Z"
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

# Delete project document

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

##### Path parameters

document_id: string



The document ID (tagged ID, e.g., claude_proj_doc_abc123)

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

type: "claude_project_document_deleted"



Constant string confirming deletion.

defaultclaude_project_document_deleted

id: string



The ID of the project document that was deleted

Delete project document

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "type": "claude_project_document_deleted"
