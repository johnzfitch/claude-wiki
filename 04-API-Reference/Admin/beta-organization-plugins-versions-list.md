---
title: "List Plugin Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/versions/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-17T06:25:59Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fplugins%2Fversions%2Flist)

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


Create Plugin


Get Plugin


Update Plugin


List Plugins


Delete Plugin

Versions


Create Plugin Version


List Plugin Versions


Get Plugin Version


Download Plugin Version Archive

Installation Settings

Shares

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)
5.  [Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions)

# List Plugin Versions

Copy page



cURL

GET/v1/organizations/plugins/{plugin_id}/versions

List a Plugin's versions, newest first.

The first item of the first page is the version the Plugin's `latest_version_id` refers to.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

##### Path parameters

plugin_id: string



ID of the Plugin (prefixed `plugin_`).

##### Query parameters



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

organization_id: optional string



For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.



page: optional string



Optionally set to the `next_page` token from the previous response.

maxLength2048

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

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

##### Returns



data: array of [BetaPluginVersion](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions#beta_plugin_version) { type: "plugin_version", id, components, 9 more }





type: "plugin_version"



Always `plugin_version`.

defaultplugin_version

id: string



The version's ID.



components: array of [BetaPluginComponent](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_component) { type, description, name } or null



What the version contains; null when not enumerated.



type: "agent" or "cli" or "command" or 3 more



The kind of component.

One of the following:

"agent"



"cli"



"command"



"hook"



"mcp_server"



"skill"



description: string or null



What the component declares about itself; always null for MCP servers, hooks, and CLIs.

name: string



The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.



content_scan: [BetaPluginContentScan](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_content_scan) { assessment, reason, status } or null



This version's content scan; null when it has not been scanned.



assessment: "fail" or "pass" or "unknown" or "warn" or null



The scan's verdict; set only when `status` is `completed`.

One of the following:

"fail"



"pass"



"unknown"



"warn"



reason: string or null



The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.



status: "completed" or "errored" or "processing"



`processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

One of the following:

"completed"



"errored"



"processing"





created_at: string



RFC 3339.

formatdate-time



created_by: [BetaPluginUserActor](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_user_actor) or [BetaPluginAPIActor](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_api_actor) or null



Who uploaded this version; null when not recorded.

One of the following:



BetaPluginUserActor object{ type: "user_actor", email_address, user_id }





type: "user_actor"



A member of the organization.

defaultuser_actor

email_address: string or null



The member's email address; may be null, for example when they are no longer a member of the organization.

user_id: string



The member's User ID.



BetaPluginAPIActor object{ type: "api_actor", api_key_id }





type: "api_actor"



An Admin API key, in the same form the Compliance API activity feed uses for it.

defaultapi_actor

api_key_id: string



The key's ID.

description: string or null



The manifest's description; null when it declares none.

display_name: string or null



The manifest's display name; null when it declares none.

manifest_version: string or null



The version string the manifest declares; null when it declares none.

plugin_id: string



The Plugin's ID.



reach: "contained" or "privileged" or "remote" or null



How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

One of the following:

"contained"



"privileged"



"remote"



release_notes: string or null



As supplied with the upload; null when none were supplied.

next_page: string or null



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List Plugin Versions

cURL



```python
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "manifest_version": "1.2.0",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "reach": "contained",
      "release_notes": "Adds a review checklist for database migrations.",
      "type": "plugin_version"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "manifest_version": "1.2.0",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "reach": "contained",
      "release_notes": "Adds a review checklist for database migrations.",
      "type": "plugin_version"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
