---
title: "Get chat messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:39:10Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fchats%2Fmessages%2Flist)

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


Get chat messages

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
4.  [Chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats)
5.  [Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages)

# Get chat messages

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

##### Path parameters

claude_chat_id: string



The chat ID (tagged ID, e.g., claude_chat_abc123)

##### Query parameters

after_id: optional string



Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before_id: optional string



Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



created_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter messages created after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter messages created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter messages created before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter messages created at or before this time (RFC 3339 format)

formatdate-time



limit: optional number



Maximum results (max: 1000). When omitted, the full result set is returned in one response.

minimum1

maximum1000



order: optional "asc" or "desc"



Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

defaultasc

One of the following:

"asc"



"desc"





tool_result_max_chars: optional number



Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

default10000

minimum-1



tool_use_input_max_chars: optional number



Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

default10000

minimum-1



updated_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter messages updated after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter messages updated at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter messages updated before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter messages updated at or before this time (RFC 3339 format)

formatdate-time

##### Headers

"x-api-key": optional string



##### Returns

id: string



Chat ID



chat_messages: array of object{ id, artifacts, content, 4 more }



Array of chat messages in order of created_at

id: string



Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'



artifacts: array of object{ id, artifact_type, title, version_id } or null



Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string



Artifact ID e.g. 'claude_artifact_abc123'

artifact_type: string or null



MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string or null



Artifact title

version_id: string



Artifact version ID e.g. 'claude_artifact_version_abc123'



content: array of Text or ToolUse or ToolResult



Content blocks within the message

One of the following:



Text object{ type: "text", text, thinking_redacted, truncated }



Text content block.



type: "text"



defaulttext

text: string



Text content from human or assistant



thinking_redacted: boolean



True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

defaultfalse



truncated: boolean



True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

defaultfalse



ToolUse object{ type: "tool_use", id, input, 4 more }



Tool invocation requested by the assistant.



type: "tool_use"



defaulttool_use

id: string or null



Tool-use ID, e.g. 'toolu_01AbC...'

input: string



Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

integration_name: string or null



Name of the integration that provides this tool, when applicable

mcp_server_url: string or null



Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string



Name of the tool invoked



truncated: boolean



True when `input` was shortened. Pass the endpoint's tool-use input max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

defaultfalse



ToolResult object{ type: "tool_result", content, integration_name, 5 more }



Result returned by a tool invocation.



type: "tool_result"



defaulttool_result



content: array of object{ type: "text", text }



Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.



type: "text"



defaulttext

text: string



Text returned by the tool

integration_name: string or null



Name of the integration that provides this tool, when applicable

is_error: boolean



True when the tool reported an error

mcp_server_url: string or null



Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string



Name of the tool that produced this result

tool_use_id: string or null



ID of the tool_use block this result responds to



truncated: boolean



True when one or more text items in `content` were shortened. Pass the endpoint's tool-result max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

defaultfalse



created_at: string



Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

formatdate-time



files: array of object{ id, created_at, filename, 3 more } or null



Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string



File ID



created_at: string



File creation timestamp

formatdate-time

filename: string



Display name of the file

md5: string or null



Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

mime_type: string or null



MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

size_bytes: number or null



Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.



generated_files: array of object{ id, filename, md5, 2 more } or null



Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download an entry whose id starts with `claude_gen_file_` via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`, and one whose id starts with `claude_file_` via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string



Id of the file: either a generated-file id, e.g. 'claude_gen_file_abc123', or a file id, e.g. 'claude_file_abc123'; the prefix tells them apart. Download the first from the generated-files content endpoint and the second from the files content endpoint. Treat everything after the prefix as an opaque string; the encoding may change without notice.

filename: string



Display name of the generated file

md5: string or null



Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

mime_type: string or null



MIME type of the file, when known

size_bytes: number or null



Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.



role: "assistant" or "user"



Message sender (user or assistant)

One of the following:

"assistant"



"user"





created_at: string



Creation timestamp

formatdate-time



deleted_at: string or null



Deletion timestamp if deleted

formatdate-time

first_id: string or null



Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



has_more: boolean



Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

defaultfalse

href: string



URL to view this chat in claude.ai

last_id: string or null



Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

model: string or null



Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

name: string



Chat name

organization_uuid: string



Organization UUID this chat belongs to

project_id: string or null



Project ID this chat belongs to



updated_at: string



Last update timestamp. Updated when the chat receives a new message, is moved into or out of a project, or is deleted in claude.ai. Other edits, such as renaming the chat, are not guaranteed to change it.

formatdate-time



user: object{ id, email_address } or null



The user who created the chat. Null when the API key is restricted to one organization and the creator is no longer a member of it.

id: string



User identifier

email_address: string



User's email address

organization_id: string⁠Deprecated



Organization ID this chat belongs to

Get chat messages

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H 'anthropic-version: 2023-06-01' \
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
  "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-5",
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
  "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-5",
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
