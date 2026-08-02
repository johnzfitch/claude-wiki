---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/files"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:38:18Z"
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

Files




cURL

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 



BetaFileScope object { id, type }



id: string



The ID of the scoping resource (e.g., the session ID).

[](#beta_file_scope.id)

type: "session"



The type of scope (e.g., `"session"`).

[](#beta_file_scope.type)

[](#beta_file_scope)



DeletedFile object { id, type }



id: string



ID of the deleted file.

[](#deleted_file.id)



type: optional "file_deleted"



Deleted object type.

For file deletion, this is always `"file_deleted"`.

[](#deleted_file.type)

[](#deleted_file)



FileMetadata object { id, created_at, filename, 5 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#file_metadata.id)

created_at: string



RFC 3339 datetime string representing when the file was created.

[](#file_metadata.created_at)

filename: string



Original filename of the uploaded file.

[](#file_metadata.filename)

mime_type: string



MIME type of the file.

[](#file_metadata.mime_type)

size_bytes: number



Size of the file in bytes.

[](#file_metadata.size_bytes)



type: "file"



Object type.

For files, this is always `"file"`.

[](#file_metadata.type)

downloadable: optional boolean



Whether the file can be downloaded.

[](#file_metadata.downloadable)



scope: optional [BetaFileScope](/docs/en/api/beta/files#beta_file_scope) { id, type }



The scope of this file, indicating the context in which it was created (e.g., a session).

id: string



The ID of the scoping resource (e.g., the session ID).

[](#file_metadata.scope%20%2B%20(resource)%20beta.files.id)

type: "session"



The type of scope (e.g., `"session"`).

[](#file_metadata.scope%20%2B%20(resource)%20beta.files.type)

[](#file_metadata.scope)
