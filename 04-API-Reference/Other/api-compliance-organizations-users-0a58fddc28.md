---
title: "Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/users"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:51Z"
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


List organizations

Users


List organization users

Roles

Settings

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

Users






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Users

##### [List organization users](/docs/en/api/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

##### ModelsExpand Collapse 



UserListResponse object { id, created_at, email, 2 more }



User member information for compliance responses.

id: string



User identifier (tagged ID)

[](#user_list_response.id)

created_at: string



User account creation timestamp

[](#user_list_response.created_at)

email: string



User's current email address

[](#user_list_response.email)

full_name: string



User's current full name

[](#user_list_response.full_name)



organization_role: "admin" or "billing" or "claude_code_user" or 6 more



User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

One of the following:

"admin"



[](#user_list_response.organization_role%5B0%5D)

"billing"



[](#user_list_response.organization_role%5B1%5D)

"claude_code_user"



[](#user_list_response.organization_role%5B2%5D)

"developer"



[](#user_list_response.organization_role%5B3%5D)

"managed"



[](#user_list_response.organization_role%5B4%5D)

"membership_admin"



[](#user_list_response.organization_role%5B5%5D)

"owner"



[](#user_list_response.organization_role%5B6%5D)

"primary_owner"



[](#user_list_response.organization_role%5B7%5D)

"user"



[](#user_list_response.organization_role%5B8%5D)

[](#user_list_response.organization_role)
