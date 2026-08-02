---
title: "Documents - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/documents"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:37Z"
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


Get project document content


Get project document metadata


Delete project document

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

Documents






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Documents

##### [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

##### [Get project document metadata](/docs/en/api/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

##### [Delete project document](/docs/en/api/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

##### ModelsExpand Collapse 



DocumentRetrieveResponse object { id, content, created_at, 2 more }



Project document information for compliance responses.

id: string



Project document identifier (tagged ID)

[](#document_retrieve_response.id)

content: string



Document text content

[](#document_retrieve_response.content)

created_at: string



Document creation timestamp

[](#document_retrieve_response.created_at)

filename: string



Document filename

[](#document_retrieve_response.filename)



user: object { id, email_address }



The user who created a project or project document.

Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#document_retrieve_response.user.id)

email_address: string



User's email address

[](#document_retrieve_response.user.email_address)

[](#document_retrieve_response.user)

[](#document_retrieve_response)



DocumentMetadataResponse object { id, claude_project_id, created_at, 5 more }



Project document metadata for GET /v1/compliance/apps/projects/documents/{document_id}/metadata.

Returns metadata only. Use the sibling endpoint (without `/metadata`) to fetch the document text content.

id: string



Project document identifier (tagged ID)

[](#document_metadata_response.id)

claude_project_id: string



The project this document belongs to

[](#document_metadata_response.claude_project_id)

created_at: string



Document creation timestamp

[](#document_metadata_response.created_at)

filename: string



Document filename

[](#document_metadata_response.filename)

md5: string



Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

[](#document_metadata_response.md5)

mime_type: "text/plain"



MIME type of the document content, always plain text

[](#document_metadata_response.mime_type)

size_bytes: number



Size in bytes of the document content (UTF-8 encoded)

[](#document_metadata_response.size_bytes)



user: object { id, email_address }



The user who created a project or project document.

Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#document_metadata_response.user.id)

email_address: string



User's email address

[](#document_metadata_response.user.email_address)

[](#document_metadata_response.user)

[](#document_metadata_response)



DocumentDeleteResponse object { id, type }



Response for deleting a project document.

id: string



The ID of the project document that was deleted

[](#document_delete_response.id)

type: "claude_project_document_deleted"



Constant string confirming deletion.

[](#document_delete_response.type)
