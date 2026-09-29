---
title: "Apps - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:38:55Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps)

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

Groups

Apps

Chats

Projects

Artifacts

Sessions

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

# Apps

#### Apps[Chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats)

##### [List chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/list)

GET/v1/compliance/apps/chats

Lists chat metadata with filtering capabilities for targeted compliance review. Results are sorted chronologically (time ascending) by the `order_by` key, with ties broken by id.

##### [Delete chat](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/delete)

DELETE/v1/compliance/apps/chats/{claude_chat_id}

Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.

#### AppsChats[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages)

##### [Get chat messages](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/messages/list)

GET/v1/compliance/apps/chats/{claude_chat_id}/messages

Retrieves message history and file metadata for a specific chat.

#### AppsChats[Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files)

##### [Get file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/retrieve)

GET/v1/compliance/apps/chats/files/{claude_file_id}

Retrieves metadata for a file referenced in chat messages, without downloading the file content. Use the sibling `/content` endpoint to download the bytes.

##### [Delete file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/delete)

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### [Download file content](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files/download)

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

#### AppsChats[Generated Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files)

##### [Get Claude-generated file metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/retrieve)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}

Returns metadata for a file the assistant created via tool use.

##### [Download a Claude-generated file](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files/download)

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.

#### Apps[Projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects)

##### [List projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### [Get project details](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

##### [Delete project](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

Delete a project for compliance purposes.

#### AppsProjects[Attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments)

##### [List project attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

#### AppsProjects[Collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators)

##### [List project collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

#### AppsProjects[Documents](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents)

##### [Get project document content](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### [Get project document metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

##### [Delete project document](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.

#### Apps[Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts)

##### [Get artifact metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact_version_id}

Returns metadata for an artifact version, without the content body.

##### [Download artifact content](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

Download the content of an artifact version for compliance purposes.

#### AppsSessions[Local](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local)

##### [List local sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/list)

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

##### [Retrieve a local session](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/retrieve)

GET/v1/compliance/apps/sessions/local/{local_session_id}

Retrieve one local session.

#### AppsSessionsLocal[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages)

##### [Retrieve local session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.

#### AppsSessions[Remote](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote)

##### [List remote sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/list)

GET/v1/compliance/apps/sessions/remote

List remote sessions (Cowork sessions that run in Anthropic-managed cloud environments) across the organizations the key may read.

#### AppsSessionsRemote[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages)

##### [Retrieve remote session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages/list)

GET/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages

Retrieve one remote session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included.
