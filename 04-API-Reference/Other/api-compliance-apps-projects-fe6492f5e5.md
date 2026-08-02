---
title: "Projects - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:31Z"
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

Projects






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Projects

##### [List projects](/docs/en/api/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

##### [Get project details](/docs/en/api/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

##### [Delete project](/docs/en/api/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

##### ModelsExpand Collapse 



ProjectListResponse object { id, created_at, deleted_at, 6 more }



Project information for compliance responses.

id: string



Project identifier (tagged ID)

[](#project_list_response.id)

created_at: string



Project creation timestamp

[](#project_list_response.created_at)

deleted_at: string



Timestamp when the project was deleted by an end user, or null otherwise

[](#project_list_response.deleted_at)

is_private: boolean



If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

[](#project_list_response.is_private)

name: string



Project name

[](#project_list_response.name)

organization_uuid: string



Organization UUID this project belongs to

[](#project_list_response.organization_uuid)

updated_at: string



Project last update timestamp

[](#project_list_response.updated_at)



user: object { id, email_address }



The user who created a project or project document.

Fields that reference this type are null when the creator's account has been deleted or the creator is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#project_list_response.user.id)

email_address: string



User's email address

[](#project_list_response.user.email_address)

[](#project_list_response.user)

organization_id: string⁠Deprecated



Organization identifier (tagged ID)

[](#project_list_response.organization_id)

[](#project_list_response)



ProjectRetrieveResponse object { id, attachments_count, chats_count, 10 more }



Detailed project information for compliance responses.

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

[](#project_retrieve_response)



ProjectDeleteResponse object { id, type }



Response for deleting a Claude project.

id: string



The ID of the Claude project that was deleted

[](#project_delete_response.id)

type: optional "claude_project_deleted"



Constant string confirming deletion.

[](#project_delete_response.type)

[](#project_delete_response)

#### ProjectsAttachments

##### [List project attachments](/docs/en/api/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

#### ProjectsCollaborators

##### [List project collaborators](/docs/en/api/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

#### ProjectsDocuments

##### [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

##### [Get project document metadata](/docs/en/api/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

##### [Delete project document](/docs/en/api/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}
