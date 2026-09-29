---
title: "Chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:56Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fchats)

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


List chats


Delete chat

Messages

Files

Generated Files

Projects

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

# Chats

##### [List chats](/docs/en/api/http/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### [Delete chat](/docs/en/api/http/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.

##### Models



ChatListResponse object{ id, created_at, deleted_at, 8 more }



Chat metadata for listing chats (without messages).



ChatDeleteResponse object{ type: "claude_chat_deleted", id }



Response for deleting a Claude chat.



type: optional "claude_chat_deleted"



Constant string confirming deletion

defaultclaude_chat_deleted

id: string



The ID of the Claude chat that was deleted

#### Chats[Messages](/docs/en/api/http/compliance/apps/chats/messages)

##### [Get chat messages](/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

#### Chats[Files](/docs/en/api/http/compliance/apps/chats/files)

##### [Get file metadata](/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

#### Chats[Generated Files](/docs/en/api/http/compliance/apps/chats/generated_files)

##### [Get Claude-generated file metadata](/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.
