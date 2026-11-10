---
title: "Get project details - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:45Z"
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

# Get project details

Copy page



API version 2026-10-21

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

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

id: string



Project identifier (tagged ID)

attachments_count: number



Number of attachments contained within this project

chats_count: number



Number of chats contained within this project



created_at: string



Project creation timestamp

formatdate-time



deleted_at: string or null



Timestamp when the project was deleted by an end user, or null otherwise

formatdate-time

description: string



Project description

href: string or null



URL to view this project in claude.ai

instructions: string



Project's custom instructions / prompt

is_private: boolean



If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

name: string



Project name

organization_uuid: string



Organization UUID this project belongs to



updated_at: string



Project last update timestamp

formatdate-time



user: object{ id, email_address } or null



Project creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

id: string



User identifier (tagged ID)

email_address: string



User's email address

organization_id: string⁠Deprecated



Organization identifier (tagged ID)

Get project details

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "href": "https://claude.ai/project/3c9d2e1f-7a6b-4c58-9d3e-2f1a7b6c5d48",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
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
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "href": "https://claude.ai/project/3c9d2e1f-7a6b-4c58-9d3e-2f1a7b6c5d48",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "email_address": "jane.doe@example.com"
