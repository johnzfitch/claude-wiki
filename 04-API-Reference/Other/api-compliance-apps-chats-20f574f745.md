---
title: "Chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:29Z"
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

Chats






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Chats

##### [List chats](/docs/en/api/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

##### [Delete chat](/docs/en/api/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

##### ModelsExpand Collapse 



ChatListResponse object { id, created_at, deleted_at, 8 more }



Chat metadata for listing chats (without messages).

id: string



Chat ID

[](#chat_list_response.id)

created_at: string



Creation timestamp

[](#chat_list_response.created_at)

deleted_at: string



Deletion timestamp if deleted

[](#chat_list_response.deleted_at)

href: string



URL to view this chat in claude.ai

[](#chat_list_response.href)

model: string



Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

[](#chat_list_response.model)

name: string



Chat name/title

[](#chat_list_response.name)

organization_uuid: string



Organization UUID this chat belongs to

[](#chat_list_response.organization_uuid)

project_id: string



Project ID this chat belongs to

[](#chat_list_response.project_id)

updated_at: string



Last update timestamp

[](#chat_list_response.updated_at)



user: object { id, email_address }



User information for compliance responses.

id: string



User identifier

[](#chat_list_response.user.id)

email_address: string



User's email address

[](#chat_list_response.user.email_address)

[](#chat_list_response.user)

organization_id: string⁠Deprecated



Organization ID this chat belongs to

[](#chat_list_response.organization_id)

[](#chat_list_response)



ChatDeleteResponse object { id, type }



Response for deleting a Claude chat.

id: string



The ID of the Claude chat that was deleted

[](#chat_delete_response.id)

type: optional "claude_chat_deleted"



Constant string confirming deletion

[](#chat_delete_response.type)

[](#chat_delete_response)

#### ChatsMessages

##### [Get chat messages](/docs/en/api/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

#### ChatsFiles

##### [Get file metadata](/docs/en/api/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

##### [Delete file](/docs/en/api/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

##### [Download file content](/docs/en/api/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

#### ChatsGenerated Files

##### [Get Claude-generated file metadata](/docs/en/api/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

##### [Download a Claude-generated file](/docs/en/api/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content
