---
title: "List Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-28T06:33:25Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fworkspaces%2Flist)

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

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)

# List Workspaces

GET/v1/organizations/workspaces

List Workspaces

##### Query parameters

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



include_archived: optional boolean



Whether to include Workspaces that have been archived in the response

defaultfalse



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

##### Returns



data: array of [BetaWorkspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_workspace) { type: "workspace", id, archived_at, 7 more }





type: "workspace"



Object type.

For Workspaces, this is always `"workspace"`.

defaultworkspace

id: string



ID of the Workspace.



archived_at: string or null



RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

formatdate-time

compartment_id: string



Identifier for this Workspace's encryption compartment. When you configure a customer-managed encryption key (CMEK) on AWS, reference this value in your KMS key-policy condition so the key is scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment binding automatically; you do not need to reference this value in your key configuration. See the CMEK integration guide for the required key configuration; unless your organization is on Claude Platform on AWS, it includes a separate value used during key validation. On Claude Platform on AWS there is no separate validation value: the key is validated against this Workspace's own value when it is attached, so if your key policy uses the compartment condition, add this value to it before attaching the key.



created_at: string



RFC 3339 datetime string indicating when the Workspace was created.

formatdate-time



data_residency: [BetaDataResidency](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_data_residency) { allowed_inference_geos, default_inference_geo, workspace_geo }



Data residency configuration.



allowed_inference_geos: array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo) or "unrestricted"



Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:



Geos = array of [BetaAllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces#beta_allowed_inference_geo)



One of the following:

"global"



"us"



Unrestricted = "unrestricted"





default_inference_geo: "global" or "us"



Default inference geo applied when requests omit the parameter.

One of the following:

"global"



"us"



workspace_geo: "us"



Geographic region for workspace data storage. Immutable after creation.

display_color: string



Hex color code representing the Workspace in the Anthropic Console.

external_key_id: string or null



ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. On Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a single-Region key in the same AWS account and Region as the Workspace. On that platform the key is validated against this Workspace when it is attached, so a key-policy problem is reported as an error on this request. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.

name: string



Name of the Workspace.

tags: map\[string\]



User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

first_id: string or null



First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean



Indicates if there are more results in the requested page direction.

last_id: string or null



Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Workspaces

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
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
