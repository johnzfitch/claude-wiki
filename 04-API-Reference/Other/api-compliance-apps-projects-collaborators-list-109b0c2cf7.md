---
title: "List project collaborators - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects/collaborators/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:58Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fprojects%2Fcollaborators%2Flist)





SearchCtrlK

Include beta APIs

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

Chats

Projects


List projects


Get project details


Delete project

Attachments

Collaborators


List project collaborators

Documents

Artifacts

Sessions

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Compliance API](/docs/en/api/http/compliance)
3.  [Apps](/docs/en/api/http/compliance/apps)
4.  [Projects](/docs/en/api/http/compliance/apps/projects)
5.  [Collaborators](/docs/en/api/http/compliance/apps/projects/collaborators)

# List project collaborators

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals are returned as a discriminated union on `type` — an individual user, an RBAC group, the whole organization, or all holders of an organization-level role.

##### Path parameters

project_id: string



The project ID (tagged ID, e.g., claude_proj_abc123)

##### Query parameters



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Headers

"x-api-key": optional string



##### Returns



data: array of ComplianceProjectUserCollaborator or ComplianceProjectGroupCollaborator or ComplianceProjectOrganizationCollaborator or ComplianceProjectOrganizationRoleCollaborator



List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

One of the following:



ComplianceProjectUserCollaborator object{ type: "user", granted_at, role, user_id }



An individual user granted a role on a project.



type: "user"



Discriminator marking this as an individual user collaborator

defaultuser



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"



user_id: string or null



Identifier of the user granted access (tagged ID), or null if their account has since been deleted



ComplianceProjectGroupCollaborator object{ type: "group", granted_at, group_id, role }



An RBAC group granted a role on a project.



type: "group"



Discriminator marking this as a group collaborator

defaultgroup



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

group_id: string



Identifier of the group granted access (tagged ID)



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"





ComplianceProjectOrganizationCollaborator object{ type: "organization", granted_at, organization_uuid, role }



An entire organization granted a role on a project.



type: "organization"



Discriminator marking this as an organization-wide grant

defaultorganization



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

organization_uuid: string



UUID of the organization granted access



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"





ComplianceProjectOrganizationRoleCollaborator object{ type: "organization_role", granted_at, organization_role, role }



All holders of an organization-level role granted a role on a project.



type: "organization_role"



Discriminator marking this as a grant to all organization members holding a specific org-level role

defaultorganization_role



granted_at: string



When this collaborator was granted access (RFC 3339 format)

formatdate-time

organization_role: string



The organization-level role whose holders are granted access



role: "admin" or "editor" or "owner" or "viewer"



Role granted on the project

One of the following:

"admin"



"editor"



"owner"



"viewer"



has_more: boolean



Whether more records exist beyond the current result set

next_page: string or null



To get the next page, use the 'next_page' from the current response as the 'page' in your next request

List project collaborators

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H 'anthropic-version: 2023-06-01' \
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
