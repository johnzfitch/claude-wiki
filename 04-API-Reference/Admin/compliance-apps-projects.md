---
title: "Projects - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:21Z"
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

# Projects

Copy page



API version 2026-10-21

##### [List projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### [Get project details](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

##### [Delete project](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

Delete a project for compliance purposes.

##### Models



ProjectRetrieveResponse object{ id, attachments_count, chats_count, 11 more }



Detailed project information for compliance responses.



ProjectListResponse object{ id, created_at, deleted_at, 7 more }



Project information for compliance responses.



ProjectDeleteResponse object{ type: "claude_project_deleted", id }



Response for deleting a Claude project.



type: optional "claude_project_deleted"



Constant string confirming deletion.

defaultclaude_project_deleted

id: string



The ID of the Claude project that was deleted

#### Projects[Attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments)

##### [List project attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

#### Projects[Collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators)

##### [List project collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

#### Projects[Documents](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents)

##### [Get project document content](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### [Get project document metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

##### [Delete project document](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.
