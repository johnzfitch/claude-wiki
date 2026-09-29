---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/files"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:30:38Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [SDKs, CLI, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Ffiles)

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

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL



A beta version of this API exists and may have additional functionality. [View the beta version](/docs/en/api/http/beta/files).

1.  [API reference](/docs/en/api/http)

# Files

##### [Upload File](/docs/en/api/http/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/http/files/list)

GET/v1/files

##### [Download File](/docs/en/api/http/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/http/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/http/files/delete)

DELETE/v1/files/{file_id}

##### Models



DeletedFile object{ type: "file_deleted", id }





type: optional "file_deleted"



Deleted object type.

For file deletion, this is always `"file_deleted"`.

defaultfile_deleted

id: string



ID of the deleted file.



FileMetadata object{ type: "file", id, created_at, 5 more }





type: "file"



Object type.

For files, this is always `"file"`.



id: string



Unique object identifier.

The format and length of IDs may change over time.



created_at: string



RFC 3339 datetime string representing when the file was created.

formatdate-time



filename: string



Original filename of the uploaded file.

minLength1

maxLength500



mime_type: string



MIME type of the file.

minLength1

maxLength255



size_bytes: number



Size of the file in bytes.

minimum0



downloadable: optional boolean



Whether the file can be downloaded.

defaultfalse



expires_at: optional string or null



RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.
