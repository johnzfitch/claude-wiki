---
title: "Groups - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/groups"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:14Z"
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

Groups


List Compliance Groups


Get Compliance Group

Members

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

Groups






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Groups

##### [List Compliance Groups](/docs/en/api/compliance/groups/list)

GET/v1/compliance/groups

##### [Get Compliance Group](/docs/en/api/compliance/groups/retrieve)

GET/v1/compliance/groups/{group_id}

##### ModelsExpand Collapse 



GroupListResponse object { id, created_at, description, 4 more }



Group information for compliance responses.

id: string



Group identifier (tagged ID)

[](#group_list_response.id)

created_at: string



Group creation timestamp (ISO 8601)

[](#group_list_response.created_at)

description: string



Group description

[](#group_list_response.description)

name: string



Group name

[](#group_list_response.name)

roles: array of string



Role IDs assigned to this group.

[](#group_list_response.roles)

source_type: string



How the group was created ('direct' or 'scim')

[](#group_list_response.source_type)

updated_at: string



Group last-updated timestamp (ISO 8601)

[](#group_list_response.updated_at)

[](#group_list_response)



GroupRetrieveResponse object { id, created_at, description, 4 more }



Group information for compliance responses.

id: string



Group identifier (tagged ID)

[](#group_retrieve_response.id)

created_at: string



Group creation timestamp (ISO 8601)

[](#group_retrieve_response.created_at)

description: string



Group description

[](#group_retrieve_response.description)

name: string



Group name

[](#group_retrieve_response.name)

roles: array of string



Role IDs assigned to this group.

[](#group_retrieve_response.roles)

source_type: string



How the group was created ('direct' or 'scim')

[](#group_retrieve_response.source_type)

updated_at: string



Group last-updated timestamp (ISO 8601)

[](#group_retrieve_response.updated_at)

[](#group_retrieve_response)

#### GroupsMembers

##### [List Compliance Group Members](/docs/en/api/compliance/groups/members/list)

GET/v1/compliance/groups/{group_id}/members
