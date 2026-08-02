---
title: "List project collaborators - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:32Z"
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

Apps

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators


List project collaborators

Documents

Artifacts

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



To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List project collaborators

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals are returned as a discriminated union on `type` — an individual user, an RBAC group, the whole organization, or all holders of an organization-level role.

##### Path ParametersExpand Collapse 

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

[](#list.project_id)

##### Query ParametersExpand Collapse 

limit: optional number



Maximum results (default: 20, max: 100)

[](#list.limit)

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.page)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 



data: array of object { granted_at, role, type, user_id } or object { granted_at, group_id, role, type } or object { granted_at, organization_uuid, role, type } or object { granted_at, organization_role, role, type }



List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

One of the following:



ComplianceProjectUserCollaborator object { granted_at, role, type, user_id }



An individual user granted a role on a project.

granted_at: string



When this collaborator was granted access (RFC 3339 format)

[](#collaborator_list_response%5B0%5D.granted_at)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



[](#collaborator_list_response%5B0%5D.role%5B0%5D)

"editor"



[](#collaborator_list_response%5B0%5D.role%5B1%5D)

"owner"



[](#collaborator_list_response%5B0%5D.role%5B2%5D)

"viewer"



[](#collaborator_list_response%5B0%5D.role%5B3%5D)

[](#collaborator_list_response%5B0%5D.role)

type: "user"



Discriminator marking this as an individual user collaborator

[](#collaborator_list_response%5B0%5D.type)

user_id: string



Identifier of the user granted access (tagged ID), or null if their account has since been deleted

[](#collaborator_list_response%5B0%5D.user_id)

[](#collaborator_list_response%5B0%5D)



ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type }



An RBAC group granted a role on a project.

granted_at: string



When this collaborator was granted access (RFC 3339 format)

[](#collaborator_list_response%5B1%5D.granted_at)

group_id: string



Identifier of the group granted access (tagged ID)

[](#collaborator_list_response%5B1%5D.group_id)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



[](#collaborator_list_response%5B1%5D.role%5B0%5D)

"editor"



[](#collaborator_list_response%5B1%5D.role%5B1%5D)

"owner"



[](#collaborator_list_response%5B1%5D.role%5B2%5D)

"viewer"



[](#collaborator_list_response%5B1%5D.role%5B3%5D)

[](#collaborator_list_response%5B1%5D.role)

type: "group"



Discriminator marking this as a group collaborator

[](#collaborator_list_response%5B1%5D.type)

[](#collaborator_list_response%5B1%5D)



ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type }



An entire organization granted a role on a project.

granted_at: string



When this collaborator was granted access (RFC 3339 format)

[](#collaborator_list_response%5B2%5D.granted_at)

organization_uuid: string



UUID of the organization granted access

[](#collaborator_list_response%5B2%5D.organization_uuid)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



[](#collaborator_list_response%5B2%5D.role%5B0%5D)

"editor"



[](#collaborator_list_response%5B2%5D.role%5B1%5D)

"owner"



[](#collaborator_list_response%5B2%5D.role%5B2%5D)

"viewer"



[](#collaborator_list_response%5B2%5D.role%5B3%5D)

[](#collaborator_list_response%5B2%5D.role)

type: "organization"



Discriminator marking this as an organization-wide grant

[](#collaborator_list_response%5B2%5D.type)

[](#collaborator_list_response%5B2%5D)



ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type }



All holders of an organization-level role granted a role on a project.

granted_at: string



When this collaborator was granted access (RFC 3339 format)

[](#collaborator_list_response%5B3%5D.granted_at)

organization_role: string



The organization-level role whose holders are granted access

[](#collaborator_list_response%5B3%5D.organization_role)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



[](#collaborator_list_response%5B3%5D.role%5B0%5D)

"editor"



[](#collaborator_list_response%5B3%5D.role%5B1%5D)

"owner"



[](#collaborator_list_response%5B3%5D.role%5B2%5D)

"viewer"



[](#collaborator_list_response%5B3%5D.role%5B3%5D)

[](#collaborator_list_response%5B3%5D.role)

type: "organization_role"



Discriminator marking this as a grant to all organization members holding a specific org-level role

[](#collaborator_list_response%5B3%5D.type)

[](#collaborator_list_response%5B3%5D)

[](#list)

has_more: boolean



Whether more records exist beyond the current result set

[](#list)

next_page: string



To get the next page, use the 'next_page' from the current response as the 'page' in your next request

[](#list)

List project collaborators



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
