---
title: "Delete project - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/delete"
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

# Delete project

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/projects/{project_id}

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

##### Path parameters

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

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

type: optional "claude_project_deleted"



Constant string confirming deletion.

defaultclaude_project_deleted

id: string



The ID of the Claude project that was deleted

Delete project

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "type": "claude_project_deleted"
