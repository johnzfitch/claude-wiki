---
title: "Compliance API - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:06Z"
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

Compliance






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Compliance API

#### Compliance APIActivities

##### [Query compliance activities](/docs/en/api/compliance/activities/list)

GET/v1/compliance/activities

#### Compliance APIOrganizations

##### [List organizations](/docs/en/api/compliance/organizations/list)

GET/v1/compliance/organizations

#### Compliance APIOrganizationsUsers

##### [List organization users](/docs/en/api/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

#### Compliance APIOrganizationsRoles

##### [List Compliance Roles](/docs/en/api/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org_uuid}/roles

##### [Get Compliance Role](/docs/en/api/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

#### Compliance APIOrganizationsRolesPermissions

##### [List Compliance Role Permissions](/docs/en/api/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

#### Compliance APIOrganizationsSettings

##### [Get effective organization settings](/docs/en/api/compliance/organizations/settings/retrieve)

GET/v1/compliance/organizations/{organization_id}/settings

#### Compliance APIGroups

##### [List Compliance Groups](/docs/en/api/compliance/groups/list)

GET/v1/compliance/groups

##### [Get Compliance Group](/docs/en/api/compliance/groups/retrieve)

GET/v1/compliance/groups/{group_id}

#### Compliance APIGroupsMembers

##### [List Compliance Group Members](/docs/en/api/compliance/groups/members/list)

GET/v1/compliance/groups/{group_id}/members

#### Compliance APIApps

#### Compliance APIAppsChats

##### [List chats](/docs/en/api/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

##### [Delete chat](/docs/en/api/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

#### Compliance APIAppsChatsMessages

##### [Get chat messages](/docs/en/api/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

#### Compliance APIAppsChatsFiles

##### [Get file metadata](/docs/en/api/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

##### [Delete file](/docs/en/api/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

##### [Download file content](/docs/en/api/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

#### Compliance APIAppsChatsGenerated Files

##### [Get Claude-generated file metadata](/docs/en/api/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

##### [Download a Claude-generated file](/docs/en/api/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

#### Compliance APIAppsProjects

##### [List projects](/docs/en/api/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

##### [Get project details](/docs/en/api/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

##### [Delete project](/docs/en/api/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

#### Compliance APIAppsProjectsAttachments

##### [List project attachments](/docs/en/api/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

#### Compliance APIAppsProjectsCollaborators

##### [List project collaborators](/docs/en/api/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

#### Compliance APIAppsProjectsDocuments

##### [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

##### [Get project document metadata](/docs/en/api/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

##### [Delete project document](/docs/en/api/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

#### Compliance APIAppsArtifacts

##### [Get artifact metadata](/docs/en/api/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact_version_id}

##### [Download artifact content](/docs/en/api/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

#### Compliance APICode

#### Compliance APICodeArtifacts

##### [List Code Artifacts](/docs/en/api/compliance/code/artifacts/list)

GET/v1/compliance/apps/code/artifacts

##### [Download Code Artifact Version Content](/docs/en/api/compliance/code/artifacts/retrieve_version)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

##### [Delete Code Artifact](/docs/en/api/compliance/code/artifacts/delete)

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}
