---
title: "List Telemetry Destinations - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-22T06:29:37Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Ftelemetry_destinations%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Create a Telemetry Destination


List Telemetry Destinations


Retrieve a Telemetry Destination


Update a Telemetry Destination


Delete a Telemetry Destination


Test a Telemetry Destination

Workspaces

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[AWS IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[Migrating to API version 2026-10-21](../Endpoints/migration-2026-10-21.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



API version 2023-06-01

cURL



This page documents API version 2023-06-01. [See this page for the newer version, 2026-10-21](beta-organization-telemetry-destinations-list.md), or read [what changed in 2026-10-21](../Endpoints/migration-2026-10-21.md).

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations)

# List Telemetry Destinations

Copy page



API version 2023-06-01

cURL

GET/v1/organizations/telemetry_destinations

List the organization's destinations, newest first, optionally only those that cover given workspaces.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#set-up-api-tracing) to learn more about destinations.

##### Query parameters



limit: optional number



Number of destinations to return per page, between 1 and 1,000. Defaults to 20.

formatint32

page: optional string



Opaque cursor from a previous response's `next_page`. Leave it out to get the first page.



workspace_ids: optional array of string



Return only the destinations that cover at least one of these workspaces (`wrkspc_...`).

Send at most 100 IDs, as `workspace_ids[]`. A destination covers a workspace when its `workspaces.type` is `all`, when its `include` list has the workspace, or when its `exclude` list doesn't have it. Destinations in either state can match. An ID that isn't the ID of one of the organization's workspaces doesn't match any destination, not even one whose type is `all`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `telemetry-destinations-2026-08-11` in this header.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



##### Returns



data: array of [BetaTelemetryDestination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination) { type: "telemetry_destination", id, created_at, 8 more }



Destinations on this page, newest first.

type: "telemetry_destination"



id: string



The unique ID of the destination (`tdst_...`).



created_at: string



Time the destination was created.

formatdate-time



delivery_health: [BetaTelemetryDestinationDeliveryHealth](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_delivery_health) { last_error, last_error_at, last_success_at }



The most recent delivery results for this destination.



last_error: string or null



A message that describes the most recent failed delivery to the destination, or `null` if no delivery has failed yet.

Examples are `temporary DNS failure`, `TLS failure`, `timeout`, `connection failure`, `invalid address`, `HTTP error (status 503)`, and `redirect (status 301)`. The message is `invalid address` both for a hostname that doesn't exist and for an address that isn't publicly routable. It never contains the endpoint's response body, a header value, a network address, or TLS details.

`last_error` and `last_error_at` always change together. A later successful delivery doesn't clear them. If `last_success_at` is later than `last_error_at`, a delivery has succeeded since this failure.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#delivery-errors) to learn the likely cause of each error.



last_error_at: string or null



Time of the failure that `last_error` describes. Changes together with `last_error`. Null until a delivery first fails.

formatdate-time



last_success_at: string or null



Time of the most recent successful delivery to the destination, or `null` if no delivery has succeeded yet.

formatdate-time

display_name: string or null



Human-readable name for the destination. Null when none was set.



endpoint_url: string



The base URL of the destination's OTLP/HTTP endpoint, exactly as registered.

The API appends the per-signal path, such as `/v1/traces`, on delivery, unless `traces.endpoint_url` is set.

header_names: array of string



Names of the registered request headers. Header values are write-only and are never returned.



state: [BetaTelemetryDestinationState](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state)



Whether the destination receives deliveries.

One of the following:



BetaTelemetryDestinationStateEnabled object{ type: "enabled" }



The telemetry destination receives the spans of the workspaces that it covers.

type: "enabled"





BetaTelemetryDestinationStateDisabled object{ type: "disabled", reason }



The API doesn't deliver anything to the telemetry destination.

Spans produced while it is disabled aren't delivered later.

type: "disabled"





reason: [BetaTelemetryDestinationDisabledReason](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_disabled_reason)



Whether a caller or the API disabled the destination and, when the API did, why. Read-only.

One of the following:



traces: [BetaTelemetryDestinationTraces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_traces) { content_mode, enabled, endpoint_url, max_content_bytes }



The destination's settings for the traces it receives.



content_mode: [BetaTelemetryDestinationContentMode](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_content_mode)



What the exported spans contain.

One of the following:

"metadata_only"



The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.



"content"



The spans contain the same metadata as `metadata_only`, plus message and tool content.

An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.

enabled: boolean



Whether the destination receives traces. A destination whose `enabled` is false keeps its other settings.



endpoint_url: string or null



The full URL that the API posts traces to, exactly as registered, or `null` if the destination doesn't have one.

When it is `null`, the API posts traces to `endpoint_url` with `/v1/traces` appended.



max_content_bytes: number or null



The most bytes of content that one exported span can contain, or `null` if only the API's maximum applies.

Content means model prompts and responses, and tool inputs and outputs. The API shortens longer content to this size before it delivers the span. A destination whose `content_mode` is `metadata_only` keeps this value. It applies once `content_mode` is `content`.

formatint32



updated_at: string



Time of the last change to the destination's configuration or state. Changes to `delivery_health` don't change it.

An update that sets a header value always changes it, even when the value is the same as before. Adding or removing a single workspace on the destination's list doesn't change it. An update that changes the list does.

formatdate-time



workspaces: [BetaTelemetryDestinationWorkspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces)



Which of the organization's workspaces the destination covers.

One of the following:



BetaTelemetryDestinationWorkspacesAll object{ type: "all" }



The destination covers every workspace of the organization, including the default workspace, archived workspaces, and workspaces created later. It doesn't have a list.

type: "all"





BetaTelemetryDestinationWorkspacesInclude object{ type: "include" }



The destination covers the workspaces on its list, and no others.

type: "include"





BetaTelemetryDestinationWorkspacesExclude object{ type: "exclude" }



The destination covers every workspace of the organization except the workspaces on its list. A workspace created later is covered until it is added to the list.

type: "exclude"



next_page: string or null



Cursor for the next page. Null on the last page.

List Telemetry Destinations

cURL



```python
curl https://api.anthropic.com/v1/organizations/telemetry_destinations \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "delivery_health": {
        "last_error": "last_error",
        "last_error_at": "2019-12-27T18:11:19.117Z",
        "last_success_at": "2019-12-27T18:11:19.117Z"
      },
      "display_name": "display_name",
      "endpoint_url": "endpoint_url",
      "header_names": [
        "string"
      ],
      "state": {
        "type": "enabled"
      },
      "traces": {
        "content_mode": "metadata_only",
        "enabled": true,
        "endpoint_url": "endpoint_url",
        "max_content_bytes": 0
      },
      "type": "telemetry_destination",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "workspaces": {
        "type": "all"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "delivery_health": {
        "last_error": "last_error",
        "last_error_at": "2019-12-27T18:11:19.117Z",
        "last_success_at": "2019-12-27T18:11:19.117Z"
      },
      "display_name": "display_name",
      "endpoint_url": "endpoint_url",
      "header_names": [
        "string"
      ],
      "state": {
        "type": "enabled"
      },
      "traces": {
        "content_mode": "metadata_only",
        "enabled": true,
        "endpoint_url": "endpoint_url",
        "max_content_bytes": 0
      },
      "type": "telemetry_destination",
      "updated_at": "2019-12-27T18:11:19.117Z",
