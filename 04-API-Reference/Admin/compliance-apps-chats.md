---
title: "Chats - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:38:56Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fchats)

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

# Chats

##### [List chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### [Delete chat](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/delete)

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

#### Chats[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages)

##### [Get chat messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

#### Chats[Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files)

##### [Get file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

#### Chats[Generated Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files)

##### [Get Claude-generated file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.
