---
title: "Retrieve local session messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/local/messages/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:30:37Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [SDKs, CLI, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fsessions%2Flocal%2Fmessages%2Flist)

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

Projects

Artifacts

Sessions

Local


List local sessions


Retrieve a local session

Messages


Retrieve local session messages

Remote

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
4.  [Sessions](/docs/en/api/http/compliance/apps/sessions)
5.  [Local](/docs/en/api/http/compliance/apps/sessions/local)
6.  [Messages](/docs/en/api/http/compliance/apps/sessions/local/messages)

# Retrieve local session messages

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.

Retention is enforced read-side: turns at or before the child organization's retention boundary are never returned; a session that straddles the boundary carries one leading `content_unavailable` placeholder (`reason: "retention_elapsed"`) in their place. The boundary is pinned on the walk's first page and honored for 24 hours: a cursor older than that is rejected with an explicit 400; restart the walk to read under the current boundary.

On a very large session, some pages are too large to read and return a 400; retrying does not help. If the request used `order=desc`, read the session oldest first from its first page instead (omit `order` and `page`, then follow `next_page`). Rarely, an oldest-first page returns this 400 too; contact Anthropic support and quote the `request-id` response header.

##### Path parameters

local_session_id: string



##### Query parameters



limit: optional number



Maximum results (default: 100, max: 1000)

default100

minimum1

maximum1000



order: optional "asc" or "desc"



Sort direction. `asc` (oldest-first, default) or `desc`. On very large sessions some pages are too large to read and return a 400, far more often with `desc`; read those sessions with `asc`, starting again from the first page.

defaultasc

One of the following:

"asc"



"desc"



page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



tool_result_max_bytes: optional number



Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

default10000

minimum-1

maximum2147483647



tool_use_input_max_bytes: optional number



Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

default10000

minimum-1

maximum2147483647

##### Headers

"x-api-key": optional string



##### Returns



data: array of object{ type: "compliance_local_session_message", id, content, 4 more }



Transcript turns for this page, in call order: oldest call first by default, newest call first with `order=desc`. The messages of one call carry the call's timestamp and follow each other in transcript order; a page boundary can fall between them.



type: "compliance_local_session_message"



defaultcompliance_local_session_message

id: string



Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.



content: array of Text or ToolUse or ToolResult



Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

One of the following:



Text object{ type: "text", text, truncated }



Text content block.



type: "text"



defaulttext

text: string



Text content from the user or the assistant



truncated: boolean



True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

defaultfalse



ToolUse object{ type: "tool_use", id, input, 2 more }

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

Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

name: string



Name of the tool invoked



truncated: boolean



True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

defaultfalse



ToolResult object{ type: "tool_result", content, is_error, 3 more }



Result returned by a tool invocation.



type: "tool_result"



defaulttool_result



content: array of object{ type: "text", text }



Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.



type: "text"



defaulttext

text: string



Text returned by the tool

is_error: boolean



True when the tool reported an error

name: string



Name of the tool that produced this result

tool_use_id: string or null



ID of the tool_use block this result responds to



truncated: boolean



True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

defaultfalse



created_at: string



When the message was recorded (RFC 3339, UTC)

formatdate-time

model: string or null



The model that served this assistant turn, as reported in the `model` field of the underlying Messages API response. Null on user messages and on any assistant message whose `provenance` is set: client-asserted history and synthetic markers were not produced by a model during this session, and for unavailable content the serving model is not known.



provenance: ContentUnavailable or ClientAsserted or SyntheticMarker or null



Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

One of the following:



ContentUnavailable object{ type: "content_unavailable", reason }



The turn's content cannot be returned; `content` is empty.



type: "content_unavailable"



defaultcontent_unavailable

reason: string



Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `client_aborted` (the client closed the connection or cancelled the request before the response completed, so the response was not captured for this turn; any partial output already streamed to the client is not included; assistant-role turns only), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.



ClientAsserted object{ type: "client_asserted" }



Assistant content the client supplied as conversation history rather than produced by Claude during this session. `content` shows what the model received but its authorship is not verified; this can result from normal request or client processing, not only client modification. Never on user-role messages.



type: "client_asserted"



defaultclient_asserted



SyntheticMarker object{ type: "synthetic_marker" }



A transcript marker generated by the endpoint rather than sent by either party during the session. Marker messages indicate that the prompt history diverged from what was captured, that the request's `system` field was present but is not shown, or that earlier turns that a request re-sent as history were withheld because they cannot be dated against the child organization's data-retention period (only for organizations with a finite retention period; the request's new user input after its last assistant turn is not affected). The marker's text names the cause. Markers that report a mismatch with captured history can result from normal request or client processing, not only client modification.



type: "synthetic_marker"



defaultsynthetic_marker



role: "assistant" or "user"



Message sender (`user` or `assistant`)

One of the following:

"assistant"



"user"



next_page: string or null



Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.



session: object{ type: "compliance_local_session", id, created_at, 6 more }



The local session the messages belong to. `user.email_address` is always null on this endpoint; the messages endpoint does not resolve email addresses.



type: "compliance_local_session"



defaultcompliance_local_session

id: string



Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.



created_at: string



Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

formatdate-time

organization_uuid: string



UUID of the child organization the session belongs to

product_surface: string or null



The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), `claude_in_chrome` (the Claude in Chrome browser extension's built-in chat), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.



truncated: boolean



True when the session has more inference calls than the service can return for one session (100,000). The messages endpoint then returns only the session's earliest calls, up to that many, and ends before the session does; `updated_at` is a lower bound on the latest call and can differ between the list and retrieve endpoints. False for every session within that bound.

defaultfalse



updated_at: string



Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

formatdate-time



user: object{ id, email_address }



The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

id: string



User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

email_address: string or null



User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

workspace_id: string or null



Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

Retrieve local session messages

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "clsm_eyJ2IjoxLCJsIjoi…",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "created_at": "2025-03-12T18:22:41.123456Z",
      "model": "claude-opus-5",
      "provenance": {
        "reason": "not_captured",
        "type": "content_unavailable"
      },
      "role": "assistant",
      "type": "compliance_local_session_message"
    }
  ],
  "next_page": "page_eyJ2IjoxLCJmIjoibSIs…",
  "session": {
    "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
    "created_at": "2025-03-12T18:22:41.123456Z",
    "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
    "product_surface": "cowork",
    "truncated": true,
    "type": "compliance_local_session",
    "updated_at": "2025-03-12T18:22:41.123456Z",
    "user": {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "email_address": "jane.doe@example.com"
    },
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR"
  }
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "clsm_eyJ2IjoxLCJsIjoi…",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "created_at": "2025-03-12T18:22:41.123456Z",
      "model": "claude-opus-5",
      "provenance": {
        "reason": "not_captured",
        "type": "content_unavailable"
      },
      "role": "assistant",
      "type": "compliance_local_session_message"
    }
  ],
  "next_page": "page_eyJ2IjoxLCJmIjoibSIs…",
  "session": {
    "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
    "created_at": "2025-03-12T18:22:41.123456Z",
    "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
    "product_surface": "cowork",
    "truncated": true,
    "type": "compliance_local_session",
    "updated_at": "2025-03-12T18:22:41.123456Z",
    "user": {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "email_address": "jane.doe@example.com"
    },
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR"
