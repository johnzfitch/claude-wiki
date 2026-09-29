---
title: "Compliance API - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:00Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance)

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

# Compliance API

#### Compliance API[Activities](/docs/en/api/http/compliance/activities)

##### [Query compliance activities](/docs/en/api/http/compliance/activities/list)

GET/v1/compliance/activities

List compliance activities for the authenticated tenant.

#### Compliance API[Organizations](/docs/en/api/http/compliance/organizations)

##### [List organizations](/docs/en/api/http/compliance/organizations/list)

GET/v1/compliance/organizations

List organizations under the parent organization.

#### Compliance APIOrganizations[Users](/docs/en/api/http/compliance/organizations/users)

##### [List organization users](/docs/en/api/http/compliance/organizations/users/list)

GET/v1/compliance/organizations/{org_uuid}/users

List current user members of an organization.

#### Compliance APIOrganizations[Roles](/docs/en/api/http/compliance/organizations/roles)

##### [List Compliance Roles](/docs/en/api/http/compliance/organizations/roles/list)

GET/v1/compliance/organizations/{org_uuid}/roles

##### [Get Compliance Role](/docs/en/api/http/compliance/organizations/roles/retrieve)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

#### Compliance APIOrganizationsRoles[Permissions](/docs/en/api/http/compliance/organizations/roles/permissions)

##### [List Compliance Role Permissions](/docs/en/api/http/compliance/organizations/roles/permissions/list)

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions

#### Compliance APIOrganizations[Settings](/docs/en/api/http/compliance/organizations/settings)

##### [Get effective organization settings](/docs/en/api/http/compliance/organizations/settings/retrieve)

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.

#### Compliance API[Groups](/docs/en/api/http/compliance/groups)

##### [List Compliance Groups](/docs/en/api/http/compliance/groups/list)

GET/v1/compliance/groups

##### [Get Compliance Group](/docs/en/api/http/compliance/groups/retrieve)

GET/v1/compliance/groups/{group_id}

#### Compliance APIGroups[Members](/docs/en/api/http/compliance/groups/members)

##### [List Compliance Group Members](/docs/en/api/http/compliance/groups/members/list)

GET/v1/compliance/groups/{group_id}/members

#### Compliance APIApps[Chats](/docs/en/api/http/compliance/apps/chats)

##### [List chats](/docs/en/api/http/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### [Delete chat](/docs/en/api/http/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.

#### Compliance APIAppsChats[Messages](/docs/en/api/http/compliance/apps/chats/messages)

##### [Get chat messages](/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

#### Compliance APIAppsChats[Files](/docs/en/api/http/compliance/apps/chats/files)

##### [Get file metadata](/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

#### Compliance APIAppsChats[Generated Files](/docs/en/api/http/compliance/apps/chats/generated_files)

##### [Get Claude-generated file metadata](/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.

#### Compliance APIApps[Projects](/docs/en/api/http/compliance/apps/projects)

##### [List projects](/docs/en/api/http/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### [Get project details](/docs/en/api/http/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

##### [Delete project](/docs/en/api/http/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

Delete a project for compliance purposes.

#### Compliance APIAppsProjects[Attachments](/docs/en/api/http/compliance/apps/projects/attachments)

##### [List project attachments](/docs/en/api/http/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

#### Compliance APIAppsProjects[Collaborators](/docs/en/api/http/compliance/apps/projects/collaborators)

##### [List project collaborators](/docs/en/api/http/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

#### Compliance APIAppsProjects[Documents](/docs/en/api/http/compliance/apps/projects/documents)

##### [Get project document content](/docs/en/api/http/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### [Get project document metadata](/docs/en/api/http/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

##### [Delete project document](/docs/en/api/http/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.

#### Compliance APIApps[Artifacts](/docs/en/api/http/compliance/apps/artifacts)

##### [Get artifact metadata](/docs/en/api/http/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact_version_id}

Returns metadata for an artifact version, without the content body.

##### [Download artifact content](/docs/en/api/http/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

Download the content of an artifact version for compliance purposes.

#### Compliance APIAppsSessions[Local](/docs/en/api/http/compliance/apps/sessions/local)

##### [List local sessions](/docs/en/api/http/compliance/apps/sessions/local/list)

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

##### [Retrieve a local session](/docs/en/api/http/compliance/apps/sessions/local/retrieve)

GET/v1/compliance/apps/sessions/local/{local_session_id}

Retrieve one local session.

#### Compliance APIAppsSessionsLocal[Messages](/docs/en/api/http/compliance/apps/sessions/local/messages)

##### [Retrieve local session messages](/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.

#### Compliance APIAppsSessions[Remote](/docs/en/api/http/compliance/apps/sessions/remote)

##### [List remote sessions](/docs/en/api/http/compliance/apps/sessions/remote/list)

GET/v1/compliance/apps/sessions/remote

List remote sessions (Cowork sessions that run in Anthropic-managed cloud environments) across the organizations the key may read.

#### Compliance APIAppsSessionsRemote[Messages](/docs/en/api/http/compliance/apps/sessions/remote/messages)

##### [Retrieve remote session messages](/docs/en/api/http/compliance/apps/sessions/remote/messages/list)

GET/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages

Retrieve one remote session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included.

#### Compliance APICode[Artifacts](/docs/en/api/http/compliance/code/artifacts)

##### [List Code Artifacts](/docs/en/api/http/compliance/code/artifacts/list)

GET/v1/compliance/apps/code/artifacts

List Claude Code Artifacts owned by organizations under the parent organization.

##### [Download Code Artifact Version Content](/docs/en/api/http/compliance/code/artifacts/retrieve_version)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

Streams the content of one version of a Claude Code Artifact as the response body.

##### [Delete Code Artifact](/docs/en/api/http/compliance/code/artifacts/delete)

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.
