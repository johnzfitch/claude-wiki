---
title: "Get Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:03Z"
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


Create Workspace


Get Workspace


List Workspaces


Update Workspace


Archive Workspace

Members

Rate Limits

Service Accounts

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

Retrieve




# Get Workspace

GET/v1/organizations/workspaces/{workspace_id}

Get Workspace

##### Path ParametersExpand Collapse 

workspace_id: string



ID of the Workspace.

[](#retrieve.workspace_id)

##### ReturnsExpand Collapse 



Workspace object { id, archived_at, compartment_id, 7 more }



id: string



ID of the Workspace.

[](#workspace.id)

archived_at: string



RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

[](#workspace.archived_at)

compartment_id: string



Identifier for this Workspace's encryption compartment. When you configure a customer-managed encryption key (CMEK) on AWS, reference this value in your KMS key-policy condition so the key is scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment binding automatically; you do not need to reference this value in your key configuration. See the CMEK integration guide for the required key configuration, including the value used during key validation.

[](#workspace.compartment_id)

created_at: string



RFC 3339 datetime string indicating when the Workspace was created.

[](#workspace.created_at)



data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }



Data residency configuration.



allowed_inference_geos: array of string or "unrestricted"



Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:

array of string



[](#workspace.data_residency.allowed_inference_geos%5B0%5D)

"unrestricted"



[](#workspace.data_residency.allowed_inference_geos%5B1%5D)

[](#workspace.data_residency.allowed_inference_geos)

default_inference_geo: string



Default inference geo applied when requests omit the parameter.

[](#workspace.data_residency.default_inference_geo)

workspace_geo: string



Geographic region for workspace data storage. Immutable after creation.

[](#workspace.data_residency.workspace_geo)

[](#workspace.data_residency)

display_color: string



Hex color code representing the Workspace in the Anthropic Console.

[](#workspace.display_color)

external_key_id: string



ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.

[](#workspace.external_key_id)

name: string



Name of the Workspace.

[](#workspace.name)

tags: map\[string\]



User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

[](#workspace.tags)



type: "workspace"



Object type.

For Workspaces, this is always `"workspace"`.

[](#workspace.type)

[](#workspace)

Get Workspace



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
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
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
