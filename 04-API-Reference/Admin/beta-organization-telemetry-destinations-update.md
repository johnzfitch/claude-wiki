---
title: "Update a Telemetry Destination - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-23T06:28:41Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Ftelemetry_destinations%2Fupdate)

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[AWS IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md)[Google Cloud IAM permissions](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md)[Versions](../Endpoints/versioning.md)[Migrating to API version 2026-10-21](../Endpoints/migration-2026-10-21.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



API version 2026-10-21

cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations)

# Update a Telemetry Destination

Copy page



API version 2026-10-21

cURL

POST/v1/organizations/telemetry_destinations/{destination_id}

Change a telemetry destination's settings, its state, or which workspaces it covers.

Send at least one field. Omitted fields keep their stored values, except the registered headers, which a change of the endpoint's hostname or port removes. Only `display_name`, `traces`, `traces.endpoint_url`, `traces.content_mode`, `traces.max_content_bytes`, and individual `headers` values accept `null`.

If another request changes the destination while the update runs, the API returns a 409 `conflict_error`. Read the destination again, then retry the update.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#delivery-and-health) to learn more about changing a destination.

##### Path parameters

destination_id: string



ID of the destination (`tdst_...`).

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

##### Body

display_name: optional string or null



New human-readable name, 1 to 255 characters. Null clears it.



endpoint_url: optional string



The new base URL of the destination's OTLP/HTTP endpoint. The same rules as on create apply.

A change of hostname or port first removes every registered header, so send the headers for the new endpoint in the same request. When the destination has a `traces.endpoint_url`, such a change must also set `traces.endpoint_url` to a URL with the new hostname and port, or to `null`. A change of the path alone keeps the headers.

maxLength2048



headers: optional map\[string\] or null



Headers to set or remove. The API merges them into the destination's headers by name.

Names compare case-insensitively. A string value sets or replaces that header. A `null` value removes it. Headers that you omit don't change. The field itself can't be `null`.

A request that sets a header value must also include `endpoint_url`. The current URL is accepted.

The resulting set must stay within the same limits as on create. When the request sets a value, each stored value that it doesn't set counts as 4,096 bytes toward the 16,384-byte limit, because you can't read its real length. So to change one header of a destination that has four or more other headers, send the values of the others again in the same request.



state: optional [BetaTelemetryDestinationStateParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state_params)



Whether the destination receives deliveries after the update. The field can't be `null`.

One of the following:



BetaTelemetryDestinationStateEnabledParams object{ type: "enabled" }



Start deliveries to the telemetry destination again.

This doesn't reset `delivery_health`.

type: "enabled"





BetaTelemetryDestinationStateDisabledParams object{ type: "disabled" }



Stop deliveries to the telemetry destination.

Spans produced while it is disabled aren't delivered later. A destination that is already disabled keeps its `reason`.

type: "disabled"





traces: optional [BetaTelemetryDestinationTracesParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_traces_params) { content_mode, enabled, endpoint_url, max_content_bytes } or null



The traces settings to change. Omitted settings keep their stored values.

`null` sets every traces setting to its create default.



content_mode: optional [BetaTelemetryDestinationContentMode](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_content_mode) or null



What the exported spans contain. Defaults to `metadata_only` on create.

On update, `null` sets `metadata_only`.

One of the following:

"metadata_only"



The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.



"content"



The spans contain the same metadata as `metadata_only`, plus message and tool content.

An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.

enabled: optional boolean



Whether the destination receives traces. Defaults to true on create. It cannot be null.



endpoint_url: optional string or null



The full URL of your collector's traces endpoint, for a collector that takes traces on a path other than `/v1/traces`. The API posts traces to it exactly as given and appends nothing.

The same rules as for `endpoint_url` apply, except that any path is allowed. It must have the same scheme, host, and port as `endpoint_url`. At most 2,048 characters.

On create, `null` is the same as leaving it out. On update, `null` removes it. The API then posts traces to `endpoint_url` with `/v1/traces` appended. A change of this URL alone keeps the registered headers.

maxLength2048



max_content_bytes: optional number or null



The most bytes of content that one exported span can contain, from 1 up to the API's maximum. `null` sets no bound, so only the API's maximum applies.

On create, leaving it out is the same as `null`. The error for a value above the maximum states the maximum.

formatint32



workspaces: optional [BetaTelemetryDestinationWorkspacesParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_params)



The new workspace scope, in the same form as on create. The field can't be `null`.

The API refuses an update that changes the type or sends `workspace_ids` while the destination's list has more than 750 workspaces. Remove workspaces one at a time until 750 or fewer remain, then send the update again.

One of the following:

##### Returns



BetaTelemetryDestination object{ type: "telemetry_destination", id, created_at, 8 more }



An OpenTelemetry destination: an OTLP/HTTP endpoint, the request headers sent with every delivery to it, what the exported spans contain, and which workspaces it covers. A destination belongs to an organization. A workspace's spans go to every enabled destination that covers it.

Update a Telemetry Destination

cURL



```python
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```python
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
```

##### Returns Examples

Response 200



```python
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
