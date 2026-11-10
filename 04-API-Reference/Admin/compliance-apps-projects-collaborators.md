---
title: "Collaborators - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:44Z"
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

# Collaborators

Copy page



API version 2026-10-21

##### [List project collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

##### Models



CollaboratorListResponse = User or Group or Organization or OrganizationRole
