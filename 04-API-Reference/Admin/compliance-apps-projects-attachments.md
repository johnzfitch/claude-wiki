---
title: "Attachments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:33:41Z"
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

# Attachments

Copy page



API version 2026-10-21

##### [List project attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

##### Models



AttachmentListResponse = ProjectFile or ProjectDoc
