---
title: "List RBAC Role Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_roles/permissions/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:08Z"
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


List RBAC Roles


Get RBAC Role

Permissions


List RBAC Role Permissions

Workspaces

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

List




# List RBAC Role Permissions

GET/v1/organizations/rbac_roles/{role_id}/permissions

List the permissions an RBAC Role grants.

The RBAC Roles API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Path ParametersExpand Collapse 

role_id: string



ID of the RBAC Role.

[](#list.role_id)

##### Query ParametersExpand Collapse 



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

[](#list.limit)

page: optional string



Optionally set to the `next_page` token from the previous response.

[](#list.page)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#list.anthropic-beta)

##### ReturnsExpand Collapse 



data: array of [RbacRolePermission](/docs/en/api/admin/rbac_roles/permissions#rbac_role_permission) { action, resource, type }





action: string



Action the permission grants on the resource.

The vocabulary follows the resource: an `organization` grant carries a product-feature entitlement (for example `chat`), an admin-panel permission entitlement (`permission_*`), or a blanket capability-access mode — `capability_access_all` grants every product-feature entitlement, and `capability_access_all_ga` grants the generally-available subset as it stands at permission-check time; neither mode grants model-access entitlements. A consumer enumerating a role's per-feature grants should treat a blanket row as granting every product-feature entitlement it covers, or it will under-report the role's effective access. A `connector_tool` grant carries a tool-access action (`use` or `always_allow`); a `connector_scope` grant carries the scope action `grant` (the role may receive the named OAuth scope when tokens are minted for the connector); `connector` and `all_connectors` grants carry a tool-access action, the scope action, or an authentication-method action (`interactive` or `managed`).

[](#rbac_role_permission.action)



resource: object { organization_id, type } or object { connector_id, tool_name, type } or object { connector_id, scope, type } or 2 more



What the permission applies to.

A tagged union: `type` names the kind of resource and determines which identifier fields are present.

One of the following:



Organization object { organization_id, type }



organization_id: string



UUID of the organization the permission applies to.

[](#rbac_role_permission.resource%5B0%5D.organization_id)

type: "organization"



Kind of resource the permission applies to.

[](#rbac_role_permission.resource%5B0%5D.type)

[](#rbac_role_permission.resource%5B0%5D)



ConnectorTool object { connector_id, tool_name, type }



connector_id: string



ID of the connector the permission applies to.

[](#rbac_role_permission.resource%5B1%5D.connector_id)



tool_name: string



Published name of the connector tool the permission applies to.

When the published name contains characters outside `[a-zA-Z0-9_-]` (or collides with a reserved form), it is server-encoded into a stable `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus a hash — from which the published name is not recoverable.

[](#rbac_role_permission.resource%5B1%5D.tool_name)

type: "connector_tool"



Kind of resource the permission applies to.

[](#rbac_role_permission.resource%5B1%5D.type)

[](#rbac_role_permission.resource%5B1%5D)



ConnectorScope object { connector_id, scope, type }



connector_id: string



ID of the connector the permission applies to.

[](#rbac_role_permission.resource%5B2%5D.connector_id)



scope: string



OAuth scope the permission names — the role may receive this scope when tokens are minted for the connector.

Subject to the same encoding rule as `tool_name`: a scope containing characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form) appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth scopes routinely contain `:` and `/`, so most appear encoded.

[](#rbac_role_permission.resource%5B2%5D.scope)

type: "connector_scope"



Kind of resource the permission applies to.

[](#rbac_role_permission.resource%5B2%5D.type)

[](#rbac_role_permission.resource%5B2%5D)



Connector object { connector_id, type }



connector_id: string



ID of the connector the permission applies to.

[](#rbac_role_permission.resource%5B3%5D.connector_id)

type: "connector"



Kind of resource the permission applies to.

[](#rbac_role_permission.resource%5B3%5D.type)

[](#rbac_role_permission.resource%5B3%5D)



AllConnectors object { type }



type: "all_connectors"



Kind of resource the permission applies to.

[](#rbac_role_permission.resource%5B4%5D.type)

[](#rbac_role_permission.resource%5B4%5D)

[](#rbac_role_permission.resource)



type: "rbac_role_permission"



Object type.

For RBAC Role Permissions, this is always `"rbac_role_permission"`.

[](#rbac_role_permission.type)

[](#list)

has_more: boolean



Indicates whether there are more results beyond this page.

[](#list)

next_page: string



Opaque cursor for the next page. Pass as the `page` parameter on the next request.

[](#list)

List RBAC Role Permissions



```python
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
