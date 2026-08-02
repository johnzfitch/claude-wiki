---
title: "Get project details - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:46Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators

Documents

Artifacts

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Retrieve






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get project details

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

##### Path ParametersExpand Collapse 

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

[](#retrieve.project_id)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#retrieve.x-api-key)

##### ReturnsExpand Collapse 

id: string



Project identifier (tagged ID)

[](#project_retrieve_response.id)

attachments_count: number



Number of attachments contained within this project

[](#project_retrieve_response.attachments_count)

chats_count: number



Number of chats contained within this project

[](#project_retrieve_response.chats_count)

created_at: string



Project creation timestamp

[](#project_retrieve_response.created_at)

deleted_at: string



Timestamp when the project was deleted by an end user, or null otherwise

[](#project_retrieve_response.deleted_at)

description: string



Project description

[](#project_retrieve_response.description)

instructions: string



Project's custom instructions / prompt

[](#project_retrieve_response.instructions)

is_private: boolean



If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

[](#project_retrieve_response.is_private)

name: string



Project name

[](#project_retrieve_response.name)

organization_uuid: string



Organization UUID this project belongs to

[](#project_retrieve_response.organization_uuid)

updated_at: string



Project last update timestamp

[](#project_retrieve_response.updated_at)



user: object { id, email_address }



The user who created a project or project document.

Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#project_retrieve_response.user.id)

email_address: string



User's email address

[](#project_retrieve_response.user.email_address)

[](#project_retrieve_response.user)

organization_id: string⁠Deprecated



Organization identifier (tagged ID)

[](#project_retrieve_response.organization_id)

Get project details



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
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
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
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
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
