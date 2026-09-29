---
title: "List RBAC Role Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_roles/permissions/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-18T06:36:43Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Frbac_roles%2Fpermissions%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


List RBAC Roles


Get RBAC Role

Permissions


List RBAC Role Permissions


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Organization](/docs/en/api/http/beta/organization)
4.  [RBAC Roles](/docs/en/api/http/beta/organization/rbac_roles)
5.  [Permissions](/docs/en/api/http/beta/organization/rbac_roles/permissions)

# List RBAC Role Permissions

GET/v1/organizations/rbac_roles/{role_id}/permissions

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

##### Path parameters

role_id: string



ID of the RBAC Role.

##### Query parameters



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1

page: optional string



Optionally set to the `next_page` token from the previous response.

##### Returns



data: array of [BetaRBACRolePermission](/docs/en/api/http/beta/organization/rbac_roles/permissions#beta_rbac_role_permission) { type: "rbac_role_permission", action, resource }





type: "rbac_role_permission"



Object type.

For RBAC Role Permissions, this is always `"rbac_role_permission"`.

defaultrbac_role_permission



action: string



Action the permission grants on the resource.

The vocabulary follows the resource: an `organization` grant carries a product-feature entitlement (for example `chat`), an admin-panel permission entitlement (`permission_*`), or a blanket capability-access mode — `capability_access_all` grants every product-feature entitlement, and `capability_access_all_ga` grants the generally-available subset as it stands at permission-check time; neither mode grants model-access entitlements. A consumer enumerating a role's per-feature grants should treat a blanket row as granting every product-feature entitlement it covers, or it will under-report the role's effective access. A `connector_tool` grant carries a tool-access action (`use` or `always_allow`); a `connector_scope` grant carries the scope action `grant` (the role may receive the named OAuth scope when tokens are minted for the connector); `connector` and `all_connectors` grants carry a tool-access action, the scope action, or an authentication-method action (`interactive` or `managed`).



resource: Organization or ConnectorTool or ConnectorScope or 2 more



What the permission applies to.

A tagged union: `type` names the kind of resource and determines which identifier fields are present.

One of the following:



Organization object{ type: "organization", organization_id }





type: "organization"



Kind of resource the permission applies to.

defaultorganization

organization_id: string



UUID of the organization the permission applies to.



ConnectorTool object{ type: "connector_tool", connector_id, tool_name }





type: "connector_tool"



Kind of resource the permission applies to.

defaultconnector_tool

connector_id: string



ID of the connector the permission applies to.



tool_name: string



Published name of the connector tool the permission applies to.

When the published name contains characters outside `[a-zA-Z0-9_-]` (or collides with a reserved form), it is server-encoded into a stable `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus a hash — from which the published name is not recoverable.



ConnectorScope object{ type: "connector_scope", connector_id, scope }





type: "connector_scope"



Kind of resource the permission applies to.

defaultconnector_scope

connector_id: string



ID of the connector the permission applies to.



scope: string



OAuth scope the permission names — the role may receive this scope when tokens are minted for the connector.

Subject to the same encoding rule as `tool_name`: a scope containing characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form) appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth scopes routinely contain `:` and `/`, so most appear encoded.



Connector object{ type: "connector", connector_id }





type: "connector"



Kind of resource the permission applies to.

defaultconnector

connector_id: string



ID of the connector the permission applies to.



AllConnectors object{ type: "all_connectors" }





type: "all_connectors"



Kind of resource the permission applies to.

defaultall_connectors

has_more: boolean



Indicates whether there are more results beyond this page.

next_page: string or null



Opaque cursor for the next page. Pass as the `page` parameter on the next request.

List RBAC Role Permissions

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
