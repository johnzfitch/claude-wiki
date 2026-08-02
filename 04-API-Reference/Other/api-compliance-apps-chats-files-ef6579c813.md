---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/files"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:33Z"
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


List chats


Delete chat

Messages

Files


Get file metadata


Delete file


Download file content

Generated Files

Projects

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

Files






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Files

##### [Get file metadata](/docs/en/api/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

##### [Delete file](/docs/en/api/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

##### [Download file content](/docs/en/api/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

##### ModelsExpand Collapse 



FileRetrieveResponse object { id, claude_chat_ids, created_at, 5 more }



File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

Returns metadata only. Use the sibling `/content` endpoint to download the file bytes.

id: string



File ID

[](#file_retrieve_response.id)

claude_chat_ids: array of string



Chats this file is attached to. A file can be referenced by messages across multiple chats.

[](#file_retrieve_response.claude_chat_ids)

created_at: string



File creation timestamp

[](#file_retrieve_response.created_at)

filename: string



Display name of the file, if set

[](#file_retrieve_response.filename)

md5: string



Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

[](#file_retrieve_response.md5)

message_ids: array of string



Chat message IDs this file is attached to. A file can be referenced by multiple messages.

[](#file_retrieve_response.message_ids)

mime_type: string



MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

[](#file_retrieve_response.mime_type)

size_bytes: number



Size in bytes of the file's preferred downloadable variant, if known

[](#file_retrieve_response.size_bytes)

[](#file_retrieve_response)



FileDeleteResponse object { id, type }



Response for deleting a compliance file.

id: string



The ID of the file that was deleted

[](#file_delete_response.id)

type: optional "claude_file_deleted"



Constant string confirming deletion

[](#file_delete_response.type)
