---
title: "List project attachments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:57Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fprojects%2Fattachments%2Flist)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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


List project attachments

Collaborators

Documents

Artifacts

Sessions

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Compliance API](/docs/en/api/http/compliance)
3.  [Apps](/docs/en/api/http/compliance/apps)
4.  [Projects](/docs/en/api/http/compliance/apps/projects)
5.  [Attachments](/docs/en/api/http/compliance/apps/projects/attachments)

# List project attachments

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

"x-api-key": optional string



##### Returns



data: array of ComplianceProjectFileReference or ComplianceProjectDocReference



List of attachments sorted chronologically by created_at, tie break by id

One of the following:



ComplianceProjectFileReference object{ type: "project_file", id, created_at, 4 more }

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

ComplianceProjectDocReference object{ type: "project_doc", id, created_at, 3 more }

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
