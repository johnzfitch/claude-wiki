---
title: "Attachments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:10Z"
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


List project attachments

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

Attachments






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Attachments

##### [List project attachments](/docs/en/api/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

##### ModelsExpand Collapse 



AttachmentListResponse = object { id, created_at, filename, 4 more } or object { id, created_at, filename, 3 more }



File attachment reference for compliance responses.

One of the following:



ComplianceProjectFileReference object { id, created_at, filename, 4 more }



File attachment reference for compliance responses.

id: string



File identifier (e.g., 'claude_file_abcd')

[](#attachment_list_response%5B0%5D.id)

created_at: string



Creation timestamp (RFC 3339 format)

[](#attachment_list_response%5B0%5D.created_at)

filename: string



Display name of the file (e.g., 'document.pdf')

[](#attachment_list_response%5B0%5D.filename)

md5: string



Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

[](#attachment_list_response%5B0%5D.md5)

mime_type: string



MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

[](#attachment_list_response%5B0%5D.mime_type)

size_bytes: number



Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

[](#attachment_list_response%5B0%5D.size_bytes)

type: "project_file"



Discriminator marking this as a binary file

[](#attachment_list_response%5B0%5D.type)

[](#attachment_list_response%5B0%5D)



ComplianceProjectDocReference object { id, created_at, filename, 3 more }



Project document attachment reference for compliance responses.

id: string



Project document identifier (e.g., 'claude_proj_doc_abcd')

[](#attachment_list_response%5B1%5D.id)

created_at: string



Creation timestamp (RFC 3339 format)

[](#attachment_list_response%5B1%5D.created_at)

filename: string



Display name of the document (e.g., 'document.txt')

[](#attachment_list_response%5B1%5D.filename)

mime_type: "text/plain"



MIME type of the project document, always set to plain text

[](#attachment_list_response%5B1%5D.mime_type)

type: "project_doc"



Discriminator marking this as a plain text document

[](#attachment_list_response%5B1%5D.type)

updated_at: string



Last-modified timestamp of the document. Reserved for future use — currently always null.

[](#attachment_list_response%5B1%5D.updated_at)

[](#attachment_list_response%5B1%5D)
