---
title: "Get chat messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:44Z"
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


Get chat messages

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

List






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get chat messages

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

##### Path ParametersExpand Collapse 

claude_chat_id: string



The chat ID (tagged ID, e.g., claude_chat_abc123)

[](#list.claude_chat_id)

##### Query ParametersExpand Collapse 

after_id: optional string



Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.after_id)

before_id: optional string



Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.before_id)



created_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter messages created after this time (RFC 3339 format)

[](#list.created_at.gt)

gte: optional string



Filter messages created at or after this time (RFC 3339 format)

[](#list.created_at.gte)

lt: optional string



Filter messages created before this time (RFC 3339 format)

[](#list.created_at.lt)

lte: optional string



Filter messages created at or before this time (RFC 3339 format)

[](#list.created_at.lte)

[](#list.created_at)

limit: optional number



Maximum results (max: 1000). When omitted, the full result set is returned in one response.

[](#list.limit)



order: optional "asc" or "desc"



Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

One of the following:

"asc"



[](#list.order%5B0%5D)

"desc"



[](#list.order%5B1%5D)

[](#list.order)

tool_result_max_chars: optional number



Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

[](#list.tool_result_max_chars)

tool_use_input_max_chars: optional number



Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

[](#list.tool_use_input_max_chars)



updated_at: optional object { gt, gte, lt, lte }



gt: optional string



Filter messages updated after this time (RFC 3339 format)

[](#list.updated_at.gt)

gte: optional string



Filter messages updated at or after this time (RFC 3339 format)

[](#list.updated_at.gte)

lt: optional string



Filter messages updated before this time (RFC 3339 format)

[](#list.updated_at.lt)

lte: optional string



Filter messages updated at or before this time (RFC 3339 format)

[](#list.updated_at.lte)

[](#list.updated_at)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 

id: string



Chat ID

[](#list)



chat_messages: array of object { id, artifacts, content, 4 more }



Array of chat messages in order of created_at

id: string



Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

[](#message_list_response.id)



artifacts: array of object { id, artifact_type, title, version_id }



Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string



Artifact ID e.g. 'claude_artifact_abc123'

[](#message_list_response.artifacts.items.id)

artifact_type: string



MIME-like artifact type e.g. 'application/vnd.ant.code'

[](#message_list_response.artifacts.items.artifact_type)

title: string



Artifact title

[](#message_list_response.artifacts.items.title)

version_id: string



Artifact version ID e.g. 'claude_artifact_version_abc123'

[](#message_list_response.artifacts.items.version_id)

[](#message_list_response.artifacts)



content: array of object { text, truncated, type } or object { id, input, integration_name, 4 more } or object { content, integration_name, is_error, 5 more }



Content blocks within the message

One of the following:



Text object { text, truncated, type }



Text content block.

text: string



Text content from human or assistant

[](#message_list_response.content.items%5B0%5D.text)

truncated: boolean



True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

[](#message_list_response.content.items%5B0%5D.truncated)

type: "text"



[](#message_list_response.content.items%5B0%5D.type)

[](#message_list_response.content.items%5B0%5D)



ToolUse object { id, input, integration_name, 4 more }



Tool invocation requested by the assistant.

id: string



Tool-use ID, e.g. 'toolu_01AbC...'

[](#message_list_response.content.items%5B1%5D.id)

input: string



Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

[](#message_list_response.content.items%5B1%5D.input)

integration_name: string



Name of the integration that provides this tool, when applicable

[](#message_list_response.content.items%5B1%5D.integration_name)

mcp_server_url: string



Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

[](#message_list_response.content.items%5B1%5D.mcp_server_url)

name: string



Name of the tool invoked

[](#message_list_response.content.items%5B1%5D.name)

truncated: boolean



True when `input` was shortened. Pass the endpoint's tool-use input max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

[](#message_list_response.content.items%5B1%5D.truncated)

type: "tool_use"



[](#message_list_response.content.items%5B1%5D.type)

[](#message_list_response.content.items%5B1%5D)



ToolResult object { content, integration_name, is_error, 5 more }



Result returned by a tool invocation.



content: array of object { text, type }



Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

text: string



Text returned by the tool

[](#message_list_response.content.items%5B2%5D.content.items.text)

type: "text"



[](#message_list_response.content.items%5B2%5D.content.items.type)

[](#message_list_response.content.items%5B2%5D.content)

integration_name: string



Name of the integration that provides this tool, when applicable

[](#message_list_response.content.items%5B2%5D.integration_name)

is_error: boolean



True when the tool reported an error

[](#message_list_response.content.items%5B2%5D.is_error)

mcp_server_url: string



Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

[](#message_list_response.content.items%5B2%5D.mcp_server_url)

name: string



Name of the tool that produced this result

[](#message_list_response.content.items%5B2%5D.name)

tool_use_id: string



ID of the tool_use block this result responds to

[](#message_list_response.content.items%5B2%5D.tool_use_id)

truncated: boolean



True when one or more text items in `content` were shortened. Pass the endpoint's tool-result max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

[](#message_list_response.content.items%5B2%5D.truncated)

type: "tool_result"



[](#message_list_response.content.items%5B2%5D.type)

[](#message_list_response.content.items%5B2%5D)

[](#message_list_response.content)

created_at: string



Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

[](#message_list_response.created_at)



files: array of object { id, created_at, filename, 3 more }



Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string



File ID

[](#message_list_response.files.items.id)

created_at: string



File creation timestamp

[](#message_list_response.files.items.created_at)

filename: string



Display name of the file

[](#message_list_response.files.items.filename)

md5: string



Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

[](#message_list_response.files.items.md5)

mime_type: string



MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

[](#message_list_response.files.items.mime_type)

size_bytes: number



Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.

[](#message_list_response.files.items.size_bytes)

[](#message_list_response.files)



generated_files: array of object { id, filename, md5, 2 more }



Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string



Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

[](#message_list_response.generated_files.items.id)

filename: string



Display name of the generated file

[](#message_list_response.generated_files.items.filename)

md5: string



Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

[](#message_list_response.generated_files.items.md5)

mime_type: string



MIME type reported by the tool that produced the file

[](#message_list_response.generated_files.items.mime_type)

size_bytes: number



Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.

[](#message_list_response.generated_files.items.size_bytes)

[](#message_list_response.generated_files)



role: "assistant" or "user"



Message sender (user or assistant)

One of the following:

"assistant"



[](#message_list_response.role%5B0%5D)

"user"



[](#message_list_response.role%5B1%5D)

[](#message_list_response.role)

[](#list)

created_at: string



Creation timestamp

[](#list)

deleted_at: string



Deletion timestamp if deleted

[](#list)

first_id: string



Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list)

has_more: boolean



Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

[](#list)

href: string



URL to view this chat in claude.ai

[](#list)

last_id: string



Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list)

model: string



Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

[](#list)

name: string



Chat name

[](#list)

organization_uuid: string



Organization UUID this chat belongs to

[](#list)

project_id: string



Project ID this chat belongs to

[](#list)

updated_at: string



Last update timestamp

[](#list)



user: object { id, email_address }



User information for compliance responses.

id: string



User identifier

[](#list)

email_address: string



User's email address

[](#list)

[](#list)

organization_id: string⁠Deprecated



Organization ID this chat belongs to

[](#list)

Get chat messages



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

##### Returns Examples

Response 200



```python
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
