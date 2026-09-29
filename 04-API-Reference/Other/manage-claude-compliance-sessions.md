---
title: "Retrieve session transcripts - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/compliance-sessions"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:31:18Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcompliance-sessions)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Compliance API

# Retrieve session transcripts

Copy page



List the sessions your users run in Claude apps and agents, such as Claude Cowork and Claude Code, and retrieve their transcripts through the Compliance API.

Copy page





The endpoints on this page are available only to Claude Enterprise organizations. The local and remote session endpoints are stable for Cowork, Claude Code, and Claude for Microsoft 365 sessions; coverage of Claude Science and Claude in Chrome sessions is in beta. The endpoints work with the same Compliance Access Key and `read:compliance_user_data` scope as the [chat, file, and project endpoints](manage-claude-compliance-content-data.md); no new key, scope, setting, or client update is required. See [Set up the Compliance API](manage-claude-compliance-api-access.md).



**Required scope:** `read:compliance_user_data` on the Compliance Access Key.

**Prerequisite:** None for listing sessions organization-wide. To filter the remote session list (sessions in the cloud) to specific users, you need user IDs from [List organization users](manage-claude-compliance-org-data.md#list-organization-users); the local session list has no user filter.

The endpoints on this page expose transcripts of the sessions your users run in Claude apps and agents (today: Cowork, Claude Code, Claude Science, Claude for Microsoft 365, and Claude in Chrome) from your Claude Enterprise organizations to compliance reviewers. Each session is a single conversation with Claude; its transcript is the sequence of user prompts, assistant responses, and tool calls and results in that conversation. The endpoints support eDiscovery (electronic discovery) exports and data loss prevention (DLP) enforcement.

The Compliance API groups sessions into two endpoint families according to where they run: local session endpoints for sessions on users' machines, and remote session endpoints for sessions that run in the cloud in Anthropic-managed environments. Both families are read-only, and neither is available to Admin API keys (`sk-ant-admin01-...`): calls authenticated with an Admin API key return [403 Forbidden](manage-claude-compliance-errors.md#403-forbidden).

The following table maps each product, and where it runs, to the endpoint family that returns its sessions and the `product_surface` value that identifies them in responses. Products are added to this table as coverage expands.

| Product and where it runs                                                                                                                | Endpoint family                                                  | `product_surface`                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cowork in Claude Desktop, running on the user's machine                                                                                  | Local session endpoints (`/v1/compliance/apps/sessions/local`)   | `cowork`                                                                                                                                             |
| Claude Code in the terminal, in Claude Desktop, or in an IDE extension, running on the user's machine                                    | Local session endpoints                                          | `claude_code`                                                                                                                                        |
| Claude Science desktop app, running on the user's machine                                                                                | Local session endpoints                                          | `claude_science`                                                                                                                                     |
| Claude for Microsoft 365 (the Claude add-ins for Excel, PowerPoint, Word, and Outlook), running in the Microsoft 365 desktop or web apps | Local session endpoints                                          | `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, or `office_agents/outlook` (`office_agents` when the app is not identified) |
| Claude in Chrome (the browser extension's built-in chat), running on the user's machine                                                  | Local session endpoints                                          | `claude_in_chrome`                                                                                                                                   |
| Cowork sessions started on claude.ai web or mobile, running in the cloud in Anthropic-managed environments                               | Remote session endpoints (`/v1/compliance/apps/sessions/remote`) | `cowork_remote`                                                                                                                                      |

Capture of local sessions is tied to the Compliance API being enabled for your organization and applies while users are signed in with their Claude Enterprise account. The session endpoints do not return the following:

- Claude Code sessions authenticated with a Claude Console API key, or run through a third-party cloud platform such as Amazon Bedrock, Google Cloud, or Microsoft Foundry.
- [Claude Code cloud sessions](../../02-Claude-Code-CLI/claude-code-on-the-web.md) (including Claude Code routines that run in the cloud), which run on cloud infrastructure instead of the user's machine. These cloud sessions are not remote sessions, even though both run in the cloud; the remote session endpoints return Cowork sessions only.
- Local sessions in organizations with [HIPAA readiness](manage-claude-api-and-data-retention.md#hipaa-readiness) enabled. No local session data is captured, so the local session endpoints return no sessions for those organizations.
- Local sessions for which [zero data retention (ZDR)](manage-claude-api-and-data-retention.md#zero-data-retention-zdr-scope) is in effect. These sessions are excluded from list results, and the retrieve and messages endpoints return 404 for them.

Anthropic recommends the Compliance API for retrieving session content. The following table compares [local sessions](#retrieve-local-sessions) and [remote sessions](#retrieve-remote-sessions) with the OpenTelemetry-based alternatives available for Cowork and Claude Code, [Cowork's OpenTelemetry logging](../../15-Claude-AI-Features/monitor-claude-cowork-activity-with-opentelemetry.md) and [Claude Code monitoring](../../13-Enterprise-Admin/monitoring-usage.md).

|                                                           | Local sessions (on users' machines)                                                                                                                 | Remote sessions (in the cloud)                                                                                                                      | OpenTelemetry logging                                                                                         |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Delivery                                                  | Pull: query and export over HTTPS                                                                                                                   | Pull: query and export over HTTPS                                                                                                                   | Push: streamed to your OTLP collector                                                                         |
| Setup                                                     | Works with your existing Compliance Access Key                                                                                                      | Works with your existing Compliance Access Key                                                                                                      | Admin configures an OTLP endpoint and content-capture settings                                                |
| Infrastructure                                            | Anthropic-hosted                                                                                                                                    | Anthropic-hosted                                                                                                                                    | You run the collector and storage                                                                             |
| ID prefix                                                 | `clls_`                                                                                                                                             | `cse_`                                                                                                                                              | N/A                                                                                                           |
| `product_surface` values                                  | `cowork`, `claude_code`, `claude_science`, `claude_in_chrome`, and values beginning with `office_agents`                                            | `cowork_remote`                                                                                                                                     | N/A                                                                                                           |
| Retention                                                 | 6 years by default, or your organization's custom conversation retention period when a finite one is set; held by Anthropic                         | 6 years, unless a user deletes the session sooner; held by Anthropic                                                                                | Your infrastructure, your policies                                                                            |
| User prompts and assistant responses                      | Yes                                                                                                                                                 | Yes                                                                                                                                                 | Yes, subject to content-capture settings                                                                      |
| Tool inputs                                               | Truncated to 10,000 bytes per input by default; up to about 1 MiB on request                                                                        | Truncated to 10,000 bytes per input by default; up to about 1 MiB on request                                                                        | Truncated summaries                                                                                           |
| Tool result content                                       | Each text entry truncated to 10,000 bytes by default; up to about 1 MiB on request                                                                  | Each text entry truncated to 10,000 bytes by default; up to about 1 MiB on request                                                                  | Metadata such as size and success; Claude Code can also capture content with an optional, size-capped setting |
| File contents                                             | Yes, through transcript tool calls (text only; other content appears as a placeholder)                                                              | Yes, through transcript tool calls (text only; other content is omitted)                                                                            | File paths; Claude Code can also capture contents with an optional, size-capped setting                       |
| Host and device metadata (terminal type, workspace paths) | No                                                                                                                                                  | No                                                                                                                                                  | Yes                                                                                                           |
| Token usage and cost                                      | No; available through the [Claude Enterprise Analytics API](manage-claude-analytics-api.md#get-access-to-the-claude-enterprise-analytics-api) | No; available through the [Claude Enterprise Analytics API](manage-claude-analytics-api.md#get-access-to-the-claude-enterprise-analytics-api) | Yes                                                                                                           |

## Sessions on users' machines (local sessions)

Local sessions run on users' machines while they are signed in with their Claude Enterprise account: today, Cowork in Claude Desktop, Claude Code (in the terminal, in Claude Desktop, or in an IDE extension), the Claude Science desktop app, Claude for Microsoft 365 (in Excel, PowerPoint, Word, and Outlook), and the Claude in Chrome browser extension.

The Compliance API exposes local sessions through three endpoints: `GET /v1/compliance/apps/sessions/local` lists session metadata, `GET /v1/compliance/apps/sessions/local/{session_id}` retrieves one session's metadata, and `GET /v1/compliance/apps/sessions/local/{session_id}/messages` returns one session's transcript. All three require the `read:compliance_user_data` scope and count only against the shared Compliance API rate limit; they are not subject to the second request budget that applies to the remote session endpoints. See [429 Too Many Requests](manage-claude-compliance-errors.md#429-too-many-requests). If local sessions are not available to your parent organization, all three endpoints return 404 with the message `Local sessions are not available.` (see [Local session not found](manage-claude-compliance-errors.md#local-session-not-found)); while session listings or captured content are temporarily unavailable, they return 503 (see [Local sessions temporarily unavailable](manage-claude-compliance-errors.md#local-sessions-temporarily-unavailable)).

For local sessions, Anthropic records each conversation server-side as its requests reach the Claude API; nothing is installed on the device, and nothing is collected beyond the requests the client already sends to the Claude API. Local session transcripts show what Claude was asked to do and what it returned, not what happened on the device. File and network activity is visible only through the tool calls and tool results in the transcript, so activity that never reaches the API (for example, local files the session never sent) is not captured.

In organizations that use [customer-managed encryption keys](manage-claude-cmek.md), local session transcripts are encrypted under your customer-managed key and returned as usual. While that key cannot be used (for example, because you disabled or revoked it, or because it cannot be reached), the messages endpoint returns [503 Service Unavailable](manage-claude-compliance-errors.md#local-sessions-temporarily-unavailable) for the affected pages instead of transcript content. Those messages are never reported as `not_captured` (see [Retrieve a local session transcript](#retrieve-a-local-session-transcript)). Listing sessions and retrieving session metadata are not affected.

The list endpoint returns session metadata, with no transcript content, for every linked organization your key can read. Unlike the remote session list, it has no organization or user filters: bound the results in time with the `created_at.gte` and `created_at.lt` parameters. Both take RFC 3339 timestamps with a required UTC offset, and when both are supplied, `created_at.lt` must be strictly after `created_at.gte` or the request returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request). A third time filter, `updated_at.gte`, bounds by last activity instead of first: it returns sessions whose last inference call is at or after the given time and combines with the `created_at` filters without changing the ordering or pagination. Use it to poll for sessions active since a previous pass, as described later in this section. New sessions and messages appear in results after a short processing delay, typically within minutes; a session that is missing immediately after it starts is not necessarily uncaptured. The following request lists sessions created since a given date.

cURL



```python
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/sessions/local" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --data-urlencode "created_at.gte=2026-07-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

Response



```python
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_01HxKpLmNoPqRsTuVwXyZaBc",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z",
      "updated_at": "2026-07-09T14:02:38Z"
    },
    {
      "type": "compliance_local_session",
      "id": "clls_01HyLqMnOpQrStUvWxYzAbCd",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": null,
      "user": {
        "id": "user_01HqRsTuVwXyZaBcDeFgHiJk",
        "email_address": null
      },
      "product_surface": "claude_code",
      "created_at": "2026-07-08T09:15:43Z",
      "updated_at": "2026-07-08T09:52:10Z"
    }
  ],
  "next_page": "page_AAEfQx7mPdLkq9Rt2VwHbZk"
}
```

Results are sorted in reverse chronological order (newest first) by `created_at`, with ties broken in a fixed server-side order, and capped at `limit` results per response (default 100, max 500). The endpoint paginates forward only with `page` and `next_page` tokens (see [Paginate results](manage-claude-compliance-activity-feed.md#paginate-results)): pass the response's `next_page` value back as the `page` query parameter on the next request, and stop when `next_page` is `null`. The response has no `has_more` field. Complete a list walk within 24 hours of starting it; an older list cursor is still accepted but is re-evaluated against the current retention boundary, so sessions whose oldest retained activity is about to age out of the retention period can be skipped.

In each session object, `user.id` is always set and survives account deletion; `user.email_address` is `null` when the user's account has been deleted or the user is no longer a member of an organization your key can read. `workspace_id` is `null` when the session was not associated with a workspace. A local session corresponds to one client session ID: starting a new conversation in the client, or clearing its context, begins a new session record. For Claude Science, the list can also include separate sessions for the app's own background work (for example, naming the conversation; on newer app versions also its reviewer and delegation tracks), and on older app versions some of that background work appears as extra messages inside the conversation's own transcript. A Claude Science conversation that continues across some app updates appears as two sessions. These behaviors are expected. Treat `id` values as opaque strings; the format may change without notice.

For Claude for Microsoft 365, deleting a conversation in the add-in happens only on the client, so it is not reflected in the API: local sessions have no `deleted_at` field, and the session stays listed until retention removes it.

Local sessions carry an `updated_at` but no `status`: a local session has no server-side lifecycle status, and its visibility is governed by retention instead. A local session is captured as the series of Claude API calls (inference calls) that the client makes during the session, and retention applies to each captured call individually. `created_at` is the timestamp of the session's earliest retained call and `updated_at` the timestamp of its last, both UTC. As older calls age past the retention period, `created_at` advances accordingly, and once every call in a session has aged out, the session is no longer returned; `updated_at` tracks the most recent call and is unaffected until then. Because `created_at` can shift between runs, deduplicate on `id` when you re-walk the list over time. To keep transcripts current as sessions gain messages, poll with the `updated_at.gte` filter, overlapping consecutive windows. On the list endpoint `updated_at` is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity, and a new call only becomes queryable after the short processing delay noted earlier. Because of that lag, set each run's `updated_at.gte` a few minutes before your previous run's start time, not to the previous run's time exactly. A bound set to the exact previous time silently and permanently drops a session whose final call was still indexing at that moment, because once the bound advances past that call no later run returns it. Deduplicate the returned sessions on `id`, re-fetch their transcripts, and deduplicate messages on `id`. Retrieving a session, or its messages, always reflects the exact latest retained call, so a periodic reconciliation pass over an older window is a more thorough alternative to widening the overlap.

The list is built from session activity metadata, so it can include sessions whose transcript content was not captured, for example sessions that ran before capture began for your organization (as far back as your retention period allows); the transcript of such a session returns each message with its content marked unavailable (see [Retrieve a local session transcript](#retrieve-a-local-session-transcript)).

Captured local session content is stored for 6 years from capture by default. If the organization that ran the session has set a finite custom conversation retention period in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), that period applies instead, whether it is shorter or longer than the default; when the organization has more than one custom retention period configured, the shortest applies. A change to that setting takes effect in two different ways: the endpoints stop returning activity older than the organization's current period as soon as the setting changes, whereas each captured message is stored for the period that was in effect when it was captured, so lengthening the period later does not restore content that has already expired.

To fetch one session's metadata directly, pass its ID to `GET /v1/compliance/apps/sessions/local/{session_id}`. The response is the same session object the list endpoint returns, with no envelope and no transcript content. A malformed session ID returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request). A single [404 Not Found](manage-claude-compliance-errors.md#404-not-found) covers four cases that the response does not distinguish: the session is not in an organization your key can read (including sessions under another parent organization), it does not exist, zero data retention is in effect for it, or every call in it has aged past retention.

`product_surface` (string or `null`) identifies the product that created the session: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), `claude_in_chrome` (the Claude in Chrome browser extension's built-in chat), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands.



**Build forward-compatible handlers.** Pass through unrecognized `product_surface` values, and ignore fields your handler does not expect, so your integration keeps working as new product surfaces ship.

### Retrieve a local session transcript

The messages endpoint returns the session's transcript, reconstructed from the captured Claude API calls: user prompts, assistant text, tool calls, and the text portions of tool results, all returned as they were sent apart from size truncation. Nothing masks URLs, credentials, or personal data in that content, so treat transcripts as sensitive. The transcript omits or replaces the following:

- Thinking blocks are never included.
- The request's system prompt is never returned. A marker message reading `[system prompt content not shown]` stands in for it (normally once per session; a session with no captured content carries no marker).
- Tool definitions and MCP server configuration are not part of the transcript.
- Images, PDFs, and other binary or structured blocks are not returned. Each appears as a `text` block reading `[<block type> content not shown]` (for example, `[image content not shown]`) with `truncated` set to `true`. Non-text items inside a tool result, such as [web search](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) results or the output of the [code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md), are replaced by one `[N non-text item(s) not shown]` entry, and the tool result block's `truncated` is `true`. The matching tool call, with the search query or the code in its `input`, is still returned.
- Citation metadata on `text` blocks, such as the source citations on an answer that draws on web search results, is omitted. The text itself is returned, and the block carries `truncated` set to `true`.

Project instruction files such as `CLAUDE.md` appear as ordinary user-role content. Skill content appears when the client sends it as message content and is not distinguished from other user text. For a coverage summary, see the [Compliance API FAQ](manage-claude-compliance-faq.md#data-coverage-and-retention); for a table comparing local sessions with remote sessions and OpenTelemetry logging, see this page's introduction.

cURL



```python
session_id="clls_01HxKpLmNoPqRsTuVwXyZaBc"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/sessions/local/$session_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

Response



```python
{
  "session": {
    "type": "compliance_local_session",
    "id": "clls_01HxKpLmNoPqRsTuVwXyZaBc",
    "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
    "user": {
      "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
      "email_address": null
    },
    "product_surface": "cowork",
    "created_at": "2026-07-09T14:02:11Z",
    "updated_at": "2026-07-09T14:02:38Z"
  },
  "data": [
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBa",
      "role": "user",
      "model": null,
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": {
        "type": "synthetic_marker"
      },
      "content": [
        {
          "type": "text",
          "text": "[system prompt content not shown]",
          "truncated": true
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBc",
      "role": "user",
      "model": null,
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "Fix the failing test in tests/auth_test.py",
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBd",
      "role": "assistant",
      "model": "claude-opus-5-5",
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "I'll read the test file first.",
          "truncated": false
        },
        {
          "type": "tool_use",
          "id": "toolu_01AbCdEfGhIjKlMnOpQrSt",
          "name": "Read",
          "input": "{\"file_path\":\"tests/auth_test.py\"}",
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBe",
      "role": "user",
      "model": null,
      "created_at": "2026-07-09T14:02:38Z",
      "provenance": null,
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrSt",
          "name": "Read",
          "is_error": false,
          "content": [
            {
              "type": "text",
              "text": "def test_login_expiry():\n    ..."
            }
          ],
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBf",
      "role": "assistant",
      "model": "claude-opus-5-5",
      "created_at": "2026-07-09T14:02:38Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "The test was asserting on a stale expiry timestamp. I've updated it.",
          "truncated": false
        }
      ]
    }
  ],
  "next_page": null
}
```

The response embeds a `session` envelope alongside the paginated `data` array. The first record in this example is the marker that stands in for the request's system prompt; its `provenance` is described later in this section. On this endpoint `user.email_address` is always `null`: the messages endpoint does not resolve email addresses, so a `null` here does not mean the user's account was deleted. To attribute a session to an email address, join `user.id` against the [list endpoint](#retrieve-local-sessions) or the retrieve endpoint (`GET /v1/compliance/apps/sessions/local/{session_id}`).

Messages are returned oldest first by default; pass `order=desc` to reverse. Pagination uses the same `page`/`next_page` scheme as the list endpoint, with a `limit` default of 100 and a max of 1,000. A page can end early when the response reaches its size limit, so a page with fewer than `limit` messages does not mean you have reached the end; keep paginating until `next_page` is `null`. Page cursors are bound to the session and sort order they were issued under, and a walk's cursors expire 24 hours after its first page: an expired cursor returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request) telling you to restart without the `page` parameter, and the restarted walk reflects the current retention boundary. A cursor issued for a different session or `order` also returns 400, as an invalid cursor.

Each message carries a `role` (`user` or `assistant`) and a `content` array of `text`, `tool_use`, and `tool_result` blocks. It also carries a `model`: on an assistant turn captured from the Claude API this is the model that served the turn, and it is `null` on user messages and on any assistant message whose `provenance` is set, because client-asserted history and synthetic markers were not produced by a model and the serving model is unknown for unavailable content. A `text` block carries `text` and `truncated`. A `tool_use` block carries `id`, `name`, `input`, and `truncated`, where `input` is a JSON-encoded string rather than an object. A `tool_result` block carries `tool_use_id`, `name`, `is_error`, a `content` array of `text` entries, and `truncated`. MCP tool calls and results, and most server tool calls and results, are normalized into these same `tool_use` and `tool_result` shapes; any other block type appears as a `[<block type> content not shown]` placeholder. A message `id` is stable while the turn is retained. Every message reconstructed from the same inference call carries that call's timestamp, so consecutive messages often share a `created_at` value; preserve the returned order rather than re-sorting by timestamp.

Each message also carries a `provenance` field describing how its content was captured. `provenance` is `null` for verified content captured by the Claude API, which is the common case. Otherwise it is an object whose `type` marks the exception:

- `content_unavailable` means the content cannot be returned. The `content` array is empty, and `provenance.reason` states why. `not_captured` means no content is available for the turn. It does not prove that no record was stored: content that Anthropic's data-handling policies withhold from the Compliance API is reported with the same reason, and so are individual turns within an otherwise captured session that are unavailable for such reasons. An unusable customer-managed key is the one exception and returns [503 Service Unavailable](manage-claude-compliance-errors.md#local-sessions-temporarily-unavailable) instead. `client_aborted` means the client closed the connection or cancelled the request before the response completed, so the turn's response was not captured; any partial output already streamed to the client is not included, and this reason applies to assistant-role turns only. `cmek_key_revoked` is reserved for content encrypted under your organization's customer-managed key when that key is unavailable (for example, revoked). It is not currently returned, because an unusable key produces a 503 instead, but handle it for forward compatibility. `retention_elapsed` means the content aged past retention. `oversize` means a single message exceeded the per-message size bound; the message is still returned, with an empty `content` array.
- `client_asserted` marks assistant messages that the client supplied as conversation history and that could not be matched to a captured response; their authorship is not verified.
- `synthetic_marker` marks records generated by the endpoint itself, such as the marker that stands in for the system prompt. When the client rewrites or compacts its conversation history mid-session (for example, after context compaction), the transcript inserts a marker message at that point and continues with the new content the client sent. When your organization has a finite retention period and that new content includes assistant messages, the transcript withholds the new content up to and including its last assistant message (a second marker notes this) and shows only the user messages after that point, followed by the rest of the session.

Marker and client-asserted messages begin with a bracketed explanatory `text` block flagged `truncated: true`, for example `[system prompt content not shown]`. Treat these records as present but unavailable or unverified rather than missing, and tolerate unrecognized `provenance` types and reasons.

Two parameters cap how many bytes of each tool block are returned: `tool_use_input_max_bytes` and `tool_result_max_bytes`, both defaulting to 10,000 bytes. Pass `-1` for the server maximum (about 1 MiB per string); `0` returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request), and values above the maximum are clamped to it. A string cut off by either cap is cut on a character boundary and has an in-band suffix appended (for example, `…[truncated; pass tool_result_max_bytes=-1 for the server max]`), and its block carries `"truncated": true`. A truncated `tool_use` `input` is therefore no longer valid JSON, so parse tool inputs only from untruncated blocks (or raise the cap and refetch). Blocks of type `text` are always capped at the same server maximum of about 1 MiB; no parameter raises it, and a `text` block at the bound also carries `"truncated": true`.

Claude Science calls connectors (MCP servers) from code that it runs through its `repl` tool, not as separately named tools, so no block in a Claude Science transcript is named after a connector. Each connector call appears in the code inside a `repl` `tool_use` block's `input` (for example, a `host.mcp("<server>", "<tool>", ...)` call), and connector output appears in the matching `tool_result` only where that code printed it. Cowork and Claude Code sessions differ: they call each connector tool under its own `mcp__<server>__<tool>` name, which is the `name` of the `tool_use` block. To monitor connector use in Claude Science sessions, parse the `input` string and match on the code it contains rather than on a tool name. Pass `tool_use_input_max_bytes=-1` for these sessions so that a long code input is returned up to the server maximum instead of being cut at the 10,000-byte default before the connector call appears.

Transcript content honors the retention period described under [Sessions on users' machines](#retrieve-local-sessions). When the start of a session has aged past it, the transcript begins with a single `content_unavailable` placeholder with `reason` of `retention_elapsed`, and the retained messages follow. When every call in a session has aged out, the messages endpoint returns [404 Not Found](manage-claude-compliance-errors.md#404-not-found), as it does for sessions in organizations your key cannot read, sessions that do not exist, and sessions for which zero data retention is in effect. A malformed session ID returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request).

## Sessions in the cloud (remote sessions)

Cowork sessions started on claude.ai web or mobile run in the cloud in Anthropic-managed environments. The Compliance API exposes these remote sessions through two endpoints: `GET /v1/compliance/apps/sessions/remote` lists session metadata, and `GET /v1/compliance/apps/sessions/remote/{session_id}/messages` returns one session's transcript. Both require the `read:compliance_user_data` scope, and both count against the shared Compliance API rate limit plus a second request budget specific to these endpoints; see [429 Too Many Requests](manage-claude-compliance-errors.md#429-too-many-requests).

The list endpoint defaults to organization-wide scope: leave off `organization_ids[]` to include every claude.ai organization your key can read, or pass up to 500 values to narrow the scope. To scope the list to specific users instead, pass 1–10 `user_ids[]` values (obtain the IDs from [List organization users](manage-claude-compliance-org-data.md#list-organization-users)); the filter matches the session's owning user, so agent-owned sessions are excluded whenever `user_ids[]` is set. Bound the results in time with `created_at` range parameters (`gte`, `gt`, `lt`, `lte`, in RFC 3339 format). There is no `updated_at` filter. The following request lists sessions created since a given date.

cURL



```python
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/sessions/remote" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --data-urlencode "created_at.gte=2026-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

Response



```python
{
  "data": [
    {
      "id": "cse_01WpQrStUvXyZaBcDeFgHjK6",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      },
      "agent_id": null,
      "started_by_user": null,
      "status": "active",
      "created_at": "2026-07-01T17:04:05Z",
      "updated_at": "2026-07-01T18:00:41Z",
      "product_surface": "cowork_remote",
      "claude_project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq"
    },
    {
      "id": "cse_01TkNpRsUvWxYzAbCdEfGhJ4",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "user": null,
      "agent_id": "cagt_01MnPqRsTuVwXyZaBcDeFgH8",
      "started_by_user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      },
      "status": "archived",
      "created_at": "2026-06-28T09:15:22Z",
      "updated_at": "2026-06-28T09:47:10Z",
      "product_surface": "cowork_remote",
      "claude_project_id": null
    }
  ],
  "next_page": "page_AAEfMk93cXpYdGxrZXk"
}
```

Results are sorted in reverse chronological order (newest first) by `created_at` and capped at `limit` results per response (default 100, max 500). The endpoint paginates with `page` and `next_page` tokens (see [Paginate results](manage-claude-compliance-activity-feed.md#paginate-results)): pass the response's `next_page` value back as the `page` query parameter on the next request, and stop when `next_page` is `null`.

A session is owned by either a user or an agent, never both. For user-owned sessions, `user` carries the owner's ID and email address (`email_address` is `null` when the user is no longer a member of an organization your key can read) and `agent_id` is `null`. For agent-owned sessions (for example, runs of a Cowork scheduled task in the cloud), `user` is `null`, `agent_id` carries the agent's ID (prefix `cagt_`), and `started_by_user` identifies the human who initiated the run; on user-owned sessions, `started_by_user` is `null`. Each run of a scheduled task is a separate session, and no session field carries the task's name or schedule.

`claude_project_id` is the ID of the claude.ai [project](manage-claude-compliance-content-data.md#retrieve-projects-and-attachments) the session belongs to (prefix `claude_proj_`), or `null` when the session is not in a project.

`status` is one of `pending`, `active`, `paused`, `archived`, or `failed`. A session is `pending` while it is being provisioned; a `pending` session has no transcript yet, and the messages endpoint returns 404 for it until provisioning completes. Sessions that have been deleted are never returned.

`product_surface` (string or `null`) identifies the product that created the session. The endpoint currently returns only sessions with `product_surface` of `cowork_remote`: Cowork sessions started on claude.ai web or mobile.



**Build forward-compatible handlers.** Pass through unrecognized `status` and `product_surface` values, and ignore fields your handler does not expect, so your integration keeps working as new statuses and product surfaces ship.

### Retrieve a remote session transcript

The messages endpoint returns the session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included. For a coverage summary, see the [Compliance API FAQ](manage-claude-compliance-faq.md#data-coverage-and-retention); for a table comparing remote sessions with local sessions and Cowork's OpenTelemetry logging, see this page's introduction.

cURL



```python
session_id="cse_01WpQrStUvXyZaBcDeFgHjK6"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/sessions/remote/$session_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

Response



```python
{
  "session": {
    "id": "cse_01WpQrStUvXyZaBcDeFgHjK6",
    "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
    "user": {
      "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
      "email_address": null
    },
    "agent_id": null,
    "started_by_user": null,
    "status": "active",
    "created_at": "2026-07-01T17:04:05Z",
    "updated_at": "2026-07-01T18:00:41Z",
    "product_surface": "cowork_remote",
    "claude_project_id": null
  },
  "data": [
    {
      "id": "csev_01HjKmNpQrStUvWxYzAbCdE2",
      "role": "user",
      "created_at": "2026-07-01T17:04:05Z",
      "content": [
        {
          "type": "text",
          "text": "Summarize the customer feedback in the attached spreadsheet.",
          "truncated": false
        }
      ],
      "sent_by_user_id": null,
      "content_unavailable": false
    },
    {
      "id": "csev_01BcDeFgHjKmNpQrStUvWxY4",
      "role": "assistant",
      "created_at": "2026-07-01T17:04:06Z",
      "content": [
        {
          "type": "text",
          "text": "I'll start by reading the spreadsheet...",
          "truncated": false
        }
      ],
      "sent_by_user_id": null,
      "content_unavailable": false
    }
  ],
  "next_page": null
}
```

The response embeds a `session` envelope alongside the paginated `data` array. On this endpoint the envelope always has `user.email_address`, `started_by_user`, and `claude_project_id` set to `null`; get those values from the list endpoint instead.

Messages are returned oldest first by default; pass `order=desc` to reverse. Pagination uses the same `page`/`next_page` scheme as the list endpoint, with a `limit` default of 100 and a max of 1,000. A page can end early when the response reaches its size limit, so a page with fewer than `limit` messages does not mean you have reached the end; keep paginating until `next_page` is `null`.

Each message carries a `role` (`user` or `assistant`) and a `content` array of `text`, `tool_use`, and `tool_result` blocks. Message `created_at` values are commit timestamps: consecutive messages can share a timestamp or slightly invert, so preserve the returned order rather than re-sorting by `created_at`. On agent-owned sessions, `sent_by_user_id` records the user who sent a given user message when one is attributable; it is `null` otherwise, including on all assistant messages. When a message's content cannot be returned at all (for example, it exceeds size bounds), the message carries `content_unavailable` set to `true`.

Two parameters cap how many bytes of each tool block are returned: `tool_use_input_max_bytes` and `tool_result_max_bytes`, both defaulting to 10,000 bytes. Pass `-1` for the server maximum (about 1 MiB per string); `0` returns [400 Bad Request](manage-claude-compliance-errors.md#400-bad-request). A block cut off by either cap carries `"truncated": true`, and a truncated `tool_use` input is no longer valid JSON, so parse tool inputs only from untruncated blocks (or raise the cap and refetch).

The messages endpoint returns [404 Not Found](manage-claude-compliance-errors.md#404-not-found) for `pending` sessions, sessions that do not exist or have been deleted, and sessions in organizations your key cannot read.

## Retention and deletion

The session endpoints are read-only; local and remote sessions cannot be deleted through the Compliance API. Local session transcripts are retained for 6 years by default, or your organization's custom conversation retention period when a finite one is set, as described under [Sessions on users' machines](#retrieve-local-sessions). Remote session transcripts are retained for 6 years, unless a user deletes the session sooner. The remote session endpoints no longer return a session once a user deletes it, and its transcript is not recoverable through the Compliance API. To learn how these periods sit alongside Anthropic's other retention arrangements, see [API and data retention](manage-claude-api-and-data-retention.md).

## Next steps

[Retrieve and delete chats, files, and projects](manage-claude-compliance-content-data.md)

Access claude.ai chat content, file attachments, and projects with the same Compliance Access Key.

[Compliance API FAQ](manage-claude-compliance-faq.md#data-coverage-and-retention)

A field-by-field summary of what session transcripts include, and other common questions.

[Handle Compliance API errors](manage-claude-compliance-errors.md)

Verbatim error payloads and the fix for each.

[API reference](../Admin/compliance-apps.md)

Endpoint paths, parameters, and response schemas for the Compliance API.
