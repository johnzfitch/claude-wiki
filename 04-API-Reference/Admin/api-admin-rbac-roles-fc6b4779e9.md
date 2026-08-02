---
title: "RBAC Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/rbac_roles"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:40:13Z"
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

Rbac roles




# RBAC Roles

##### [List RBAC Roles](/docs/en/api/admin/rbac_roles/list)

GET/v1/organizations/rbac_roles

##### [Get RBAC Role](/docs/en/api/admin/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{role_id}

##### ModelsExpand Collapse 



RbacRole object { id, created_at, name, 2 more }



id: string



ID of the RBAC Role.

[](#rbac_role.id)

created_at: string



RFC 3339 datetime string indicating when the RBAC Role was created.

[](#rbac_role.created_at)

name: string



Name of the RBAC Role.

[](#rbac_role.name)



type: "rbac_role"



Object type.

For RBAC Roles, this is always `"rbac_role"`.

[](#rbac_role.type)

updated_at: string



RFC 3339 datetime string indicating when the RBAC Role was last updated.

[](#rbac_role.updated_at)

[](#rbac_role)

#### RBAC RolesPermissions

##### [List RBAC Role Permissions](/docs/en/api/admin/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{role_id}/permissions
