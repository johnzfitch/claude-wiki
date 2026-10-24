---
title: "Telemetry Destinations - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-22T06:29:40Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Ftelemetry_destinations)

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

This page documents API version 2023-06-01. [See this page for the newer version, 2026-10-21](beta-organization-telemetry-destinations.md), or read [what changed in 2026-10-21](../Endpoints/migration-2026-10-21.md).

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Telemetry Destinations

Copy page



API version 2023-06-01

cURL

##### [Create a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/create)

POST/v1/organizations/telemetry_destinations

Register an OpenTelemetry destination for the organization.

##### [List Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/list)

GET/v1/organizations/telemetry_destinations

List the organization's destinations, newest first, optionally only those that cover given workspaces.

##### [Retrieve a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/retrieve)

GET/v1/organizations/telemetry_destinations/{destination_id}

Read a destination's configuration, state, and most recent delivery results.

##### [Update a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/update)

POST/v1/organizations/telemetry_destinations/{destination_id}

Change a telemetry destination's settings, its state, or which workspaces it covers.

##### [Delete a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/delete)

DELETE/v1/organizations/telemetry_destinations/{destination_id}

Delete a destination and its workspace list.

##### [Test a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/test)

POST/v1/organizations/telemetry_destinations/{destination_id}/test

Send one test span, named `anthropic.test`, to the destination with its registered headers, once and without retries, and report the destination's answer. The response is 200 whether or not the destination answered with a 2xx status: its `result` has the type `success`, or the type `failure` and the reason in `error`. The destination's configuration, `state` and `delivery_health` do not change. A disabled destination can be tested too. Wait 10 seconds between tests of one destination; a request that comes sooner may be answered with status 429.

##### Models



BetaDeletedTelemetryDestination object{ type: "telemetry_destination_deleted", id }



Confirmation that a destination was deleted.

type: "telemetry_destination_deleted"



id: string



ID of the deleted destination (`tdst_...`).



BetaTelemetryDestination object{ type: "telemetry_destination", id, created_at, 8 more }



An OpenTelemetry destination: an OTLP/HTTP endpoint, the request headers sent with every delivery to it, what the exported spans contain, and which workspaces it covers. A destination belongs to an organization. A workspace's spans go to every enabled destination that covers it.



BetaTelemetryDestinationContentMode = "metadata_only" or "content"



What the spans that the API exports to a telemetry destination contain.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#choose-a-content-mode) to learn what the spans contain in each content mode.

One of the following:

"metadata_only"



The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.



"content"



The spans contain the same metadata as `metadata_only`, plus message and tool content.

An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.



BetaTelemetryDestinationDeliveryHealth object{ last_error, last_error_at, last_success_at }



The most recent delivery results that the API records for a telemetry destination.

Changes to the destination's configuration or state don't reset these fields. Changes to these fields don't change `updated_at`. The values can lag behind the latest deliveries.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#delivery-and-health) to learn how the API delivers spans and when it disables a destination.

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



BetaTelemetryDestinationDisabledReason = [BetaTelemetryDestinationDisabledReasonCaller](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_disabled_reason_caller) or [BetaTelemetryDestinationDisabledReasonSustainedFailure](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_disabled_reason_sustained_failure) or [BetaTelemetryDestinationDisabledReasonInvalidAddress](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_disabled_reason_invalid_address) or [BetaTelemetryDestinationDisabledReasonRedirect](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_disabled_reason_redirect)



Why the destination is disabled: `caller` when a caller disabled it, or the reason the API disabled it automatically (`sustained_failure`, `invalid_address`, or `redirect`). Every automatic disable is reversible with an update that sets `state` to `enabled`. An update that sets `disabled` on a destination that is already disabled keeps its reason.

One of the following:



BetaTelemetryDestinationDisabledReasonCaller object{ type: "caller" }



A caller disabled the destination with an update that set `state` to `disabled`.

type: "caller"





BetaTelemetryDestinationDisabledReasonInvalidAddress object{ type: "invalid_address" }



The API disabled the destination because deliveries to it failed for longer than the same threshold as for `sustained_failure`, and the most recent failed delivery failed with an invalid address: the DNS answer says that the endpoint's hostname doesn't exist or doesn't have an address, or the address that the API would connect to isn't publicly routable or is reserved, for example a loopback, link-local, private-network, or cloud-metadata address. The API doesn't connect to such an address, and retries the delivery a bounded number of times as it does after a timeout. A timeout or a server failure of the DNS lookup is a temporary DNS failure instead, not an invalid address.

type: "invalid_address"





BetaTelemetryDestinationDisabledReasonRedirect object{ type: "redirect" }



The API disabled the destination because the endpoint answered a delivery with a 3xx status. Redirects are never followed, and one such answer disables the destination at once.

type: "redirect"





BetaTelemetryDestinationDisabledReasonSustainedFailure object{ type: "sustained_failure" }



The API disabled the destination because deliveries to it failed, with no successful delivery in between, for longer than a threshold that Anthropic configures and that is not part of this contract. The reason is `invalid_address` instead when the most recent failed delivery failed with an invalid address.

type: "sustained_failure"





BetaTelemetryDestinationState = [BetaTelemetryDestinationStateEnabled](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state_enabled) or [BetaTelemetryDestinationStateDisabled](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state_disabled)



Whether a telemetry destination receives deliveries.

A caller can set either state. The API also disables an enabled destination on its own in some cases. The `reason` of the disabled state says whether a caller or the API disabled the destination and, when the API did, why.

See the [OpenTelemetry export guide](../Other/manage-claude-opentelemetry.md#delivery-and-health) to learn when the API disables a destination.

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

BetaTelemetryDestinationStateDisabledParams object{ type: "disabled" }



Stop deliveries to the telemetry destination.

Spans produced while it is disabled aren't delivered later. A destination that is already disabled keeps its `reason`.

type: "disabled"





BetaTelemetryDestinationStateEnabled object{ type: "enabled" }



The telemetry destination receives the spans of the workspaces that it covers.

type: "enabled"





BetaTelemetryDestinationStateEnabledParams object{ type: "enabled" }



Start deliveries to the telemetry destination again.

This doesn't reset `delivery_health`.

type: "enabled"





BetaTelemetryDestinationStateParams = [BetaTelemetryDestinationStateEnabledParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state_enabled_params) or [BetaTelemetryDestinationStateDisabledParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_state_disabled_params)



The state to set on a telemetry destination, by `type` alone.

A caller can't set the `reason` of a disabled state. Only the API sets it.

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

BetaTelemetryDestinationTestFailure object{ type: "failure", error }



The test span was not delivered.

type: "failure"



error: string



A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.



BetaTelemetryDestinationTestResponse object{ type: "telemetry_destination_test", result }



The result of one test span sent to a destination.

type: "telemetry_destination_test"





result: [BetaTelemetryDestinationTestResult](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_test_result)



How the test went: `success` when the destination answered with a 2xx status, else `failure` with the reason.

One of the following:



BetaTelemetryDestinationTestSuccess object{ type: "success" }



The destination answered the test span with a 2xx status.

type: "success"





BetaTelemetryDestinationTestFailure object{ type: "failure", error }



The test span was not delivered.

type: "failure"



error: string



A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.



BetaTelemetryDestinationTestResult = [BetaTelemetryDestinationTestSuccess](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_test_success) or [BetaTelemetryDestinationTestFailure](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_test_failure)



The outcome of a test: `success`, or `failure` with the reason.

One of the following:



BetaTelemetryDestinationTestSuccess object{ type: "success" }



The destination answered the test span with a 2xx status.

type: "success"





BetaTelemetryDestinationTestFailure object{ type: "failure", error }



The test span was not delivered.

type: "failure"



error: string



A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.



BetaTelemetryDestinationTestSuccess object{ type: "success" }



The destination answered the test span with a 2xx status.

type: "success"





BetaTelemetryDestinationTraces object{ content_mode, enabled, endpoint_url, max_content_bytes }



A telemetry destination's settings for the traces it receives.

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

BetaTelemetryDestinationTracesParams object{ content_mode, enabled, endpoint_url, max_content_bytes }



The settings for the traces that a telemetry destination receives, as a create or update request sets them. An omitted field takes its default on create and keeps its stored value on update.

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

BetaTelemetryDestinationWorkspaces = [BetaTelemetryDestinationWorkspacesAll](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_all) or [BetaTelemetryDestinationWorkspacesInclude](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_include) or [BetaTelemetryDestinationWorkspacesExclude](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_exclude)



Which of the organization's workspaces a telemetry destination covers.

Several destinations can cover the same workspace. Each of them receives the workspace's spans while it is enabled.

The workspace list of an `include` or `exclude` destination isn't part of the destination object. List the destination's workspaces to read it. Add or remove one workspace at a time, or replace the whole list with an update. A list holds at most 1,000 workspaces.

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



BetaTelemetryDestinationWorkspacesAll object{ type: "all" }



The destination covers every workspace of the organization, including the default workspace, archived workspaces, and workspaces created later. It doesn't have a list.

type: "all"





BetaTelemetryDestinationWorkspacesAllParams object{ type: "all" }



Cover every workspace of the organization. Doesn't take `workspace_ids`.

An update that sets `all` empties the destination's workspace list.

type: "all"





BetaTelemetryDestinationWorkspacesExclude object{ type: "exclude" }



The destination covers every workspace of the organization except the workspaces on its list. A workspace created later is covered until it is added to the list.

type: "exclude"





BetaTelemetryDestinationWorkspacesExcludeParams object{ type: "exclude", workspace_ids }



Cover every workspace of the organization except the workspaces on the list.

type: "exclude"





workspace_ids: optional array of string



The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.



BetaTelemetryDestinationWorkspacesInclude object{ type: "include" }



The destination covers the workspaces on its list, and no others.

type: "include"





BetaTelemetryDestinationWorkspacesIncludeParams object{ type: "include", workspace_ids }



Cover only the workspaces on the list.

type: "include"





workspace_ids: optional array of string



The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.



BetaTelemetryDestinationWorkspacesParams = [BetaTelemetryDestinationWorkspacesAllParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_all_params) or [BetaTelemetryDestinationWorkspacesIncludeParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_include_params) or [BetaTelemetryDestinationWorkspacesExcludeParams](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations#beta_telemetry_destination_workspaces_exclude_params)



Which of the organization's workspaces a telemetry destination covers, as a create or update request sets it.

One of the following:

#### Telemetry Destinations[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces)

##### [List Telemetry Destination Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/list)

GET/v1/organizations/telemetry_destinations/{destination_id}/workspaces

List the workspaces on a destination's workspace list, newest entry first.

##### [Add a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/add)

POST/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Add one workspace to a destination's workspace list.

##### [Remove a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/remove)

DELETE/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Remove one workspace from a destination's workspace list.
