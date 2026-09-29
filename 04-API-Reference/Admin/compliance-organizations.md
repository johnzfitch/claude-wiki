---
title: "Organizations - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:39:01Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Forganizations)





SearchCtrlK

Include beta APIs

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


List organizations

Users

Roles

Settings

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

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)

# Organizations

##### [List organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations/list)

GET/v1/compliance/organizations

List organizations under the parent organization.

##### Models



OrganizationListResponse object{ created_at, name, uuid }



Information about an organization.

created_at: string



Organization creation time (RFC 3339 format)

name: string



Organization name

uuid: string



Unique identifier for the organization (UUID format)

#### Organizations[Users](https://platform.claude.com/docs/en/api/http/compliance/organizations/users)

##### [List organization users](https://platform.claude.com/docs/en/api/http/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

List current user members of an organization.

#### Organizations[Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles)

##### [List Compliance Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org_uuid}/roles

##### [Get Compliance Role](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

#### OrganizationsRoles[Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions)

##### [List Compliance Role Permissions](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

#### Organizations[Settings](https://platform.claude.com/docs/en/api/http/compliance/organizations/settings)

##### [Get effective organization settings](https://platform.claude.com/docs/en/api/http/compliance/organizations/settings/retrieve)

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.
