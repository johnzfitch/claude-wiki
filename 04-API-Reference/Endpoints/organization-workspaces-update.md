---
title: "Update Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:26:25Z"
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

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fworkspaces%2Fupdate)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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


List Workspaces


Create Workspace


Get Workspace


Update Workspace


Archive Workspace

Rate Limits

Members

Service Accounts

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

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Update Workspace

Copy page



cURL

POST/v1/organizations/workspaces/{workspace_id}

Update Workspace

##### Path parameters

workspace_id: string



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



data_residency: optional [DataResidencyUpdateConfig](https://platform.claude.com/docs/en/api/http/organization/workspaces#data_residency_update_config) { allowed_inference_geos, default_inference_geo } or null



Data residency configuration for the workspace.



allowed_inference_geos: optional array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo)



One of the following:

"global"



"us"



"unrestricted"





default_inference_geo: optional "global" or "us" or null



Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"



"us"





display_color: optional string



Hex color code representing the Workspace in the Anthropic Console.

maxLength7

pattern^#\[0-9A-Fa-f\]{6}\$

external_key_id: optional string



ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. On Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a single-Region key in the same AWS account and Region as the Workspace. On that platform the key is validated against this Workspace when it is attached, so a key-policy problem is reported as an error on this request. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.



name: optional string



Name of the Workspace.

minLength1

maxLength255

tags: optional map\[string\] or null



User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

##### Returns



Workspace object{ type: "workspace", id, archived_at, 7 more }



Update Workspace

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

Response 200



```python
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
