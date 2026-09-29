---
title: "Get project document content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:39:04Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fprojects%2Fdocuments%2Fretrieve)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators

Documents


Get project document content


Get project document metadata


Delete project document

Artifacts

Sessions

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects)
5.  [Documents](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents)

# Get project document content

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### Path parameters

document_id: string



The document ID (tagged ID, e.g., claude_proj_doc_abc123)

##### Headers

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
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
