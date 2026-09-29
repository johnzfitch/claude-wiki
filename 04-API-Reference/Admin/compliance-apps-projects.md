---
title: "Projects - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/projects"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:38:57Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fprojects)

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


List projects


Get project details


Delete project

Attachments

Collaborators

Documents

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
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)

# Projects

##### [List projects](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/list)

GET/v1/compliance/apps/projects

Lists project metadata with filtering capabilities. Results are sorted chronologically (time ascending) by created_at.

##### [Get project details](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/retrieve)

GET/v1/compliance/apps/projects/{project_id}

Get detailed information for a specific project.

##### [Delete project](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/delete)

DELETE/v1/compliance/apps/projects/{project_id}

Delete a project for compliance purposes.

##### Models



ProjectRetrieveResponse object{ id, attachments_count, chats_count, 10 more }



Detailed project information for compliance responses.



ProjectListResponse object{ id, created_at, deleted_at, 6 more }



Project information for compliance responses.



ProjectDeleteResponse object{ type: "claude_project_deleted", id }



Response for deleting a Claude project.



type: optional "claude_project_deleted"



Constant string confirming deletion.

defaultclaude_project_deleted

id: string



The ID of the Claude project that was deleted

#### Projects[Attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments)

##### [List project attachments](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/attachments/list)

GET/v1/compliance/apps/projects/{project_id}/attachments

List files and documents attached to a project.

#### Projects[Collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators)

##### [List project collaborators](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/collaborators/list)

GET/v1/compliance/apps/projects/{project_id}/collaborators

List the users, groups, and organization-wide grants on a project.

#### Projects[Documents](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents)

##### [Get project document content](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/retrieve)

GET/v1/compliance/apps/projects/documents/{document_id}

Get detailed information for a specific project document.

##### [Get project document metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/metadata)

GET/v1/compliance/apps/projects/documents/{document_id}/metadata

Returns metadata for a project document, without the content body.

##### [Delete project document](https://platform.claude.com/docs/en/api/http/compliance/apps/projects/documents/delete)

DELETE/v1/compliance/apps/projects/documents/{document_id}

Delete a project document for compliance purposes.
