---
title: "RBAC Groups - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_groups"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-20T06:39:33Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Frbac_groups)

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


Create RBAC Group


List RBAC Groups


Get RBAC Group


Update RBAC Group


Delete RBAC Group

Members

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

# RBAC Groups

Copy page



cURL

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

##### [Update RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/update)

POST/v1/organizations/rbac_groups/{rbac_group_id}

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Delete RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

##### Models



BetaRBACGroup object{ type: "rbac_group", id, created_at, 5 more }





RBACGroupDeleteResponse object{ type: "rbac_group_deleted", id }





type: "rbac_group_deleted"



Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

defaultrbac_group_deleted

id: string



ID of the RBAC Group.

#### RBAC Groups[Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members)

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/add)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/remove)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.
