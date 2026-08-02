---
title: "Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/code/artifacts"
category: "04-API-Reference/Other"
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

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Delete Code Artifact


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Artifacts






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Artifacts

##### [List Code Artifacts](/docs/en/api/compliance/code/artifacts/list)

GET/v1/compliance/apps/code/artifacts

##### [Download Code Artifact Version Content](/docs/en/api/compliance/code/artifacts/retrieve_version)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

##### [Delete Code Artifact](/docs/en/api/compliance/code/artifacts/delete)

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

##### ModelsExpand Collapse 



ArtifactListResponse object { id, organization_uuid, owner_user_id, 5 more }



A hosted site published via Claude Code.

id: string



Artifact identifier (tagged ID)

[](#artifact_list_response.id)

organization_uuid: string



Organization UUID this Artifact belongs to

[](#artifact_list_response.organization_uuid)

owner_user_id: string



Artifact owner's user identifier (tagged ID). Always set, so attribution survives after the owner's account is deleted or the owner leaves every organization under the parent.

[](#artifact_list_response.owner_user_id)

published_version_id: string



Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.

[](#artifact_list_response.published_version_id)



read_mode: "org" or "owner" or "public" or "users"



Who can view this Artifact: only its owner, a named set of users, every member of its organization, or anyone on the internet (`public`)

One of the following:

"org"



[](#artifact_list_response.read_mode%5B0%5D)

"owner"



[](#artifact_list_response.read_mode%5B1%5D)

"public"



[](#artifact_list_response.read_mode%5B2%5D)

"users"



[](#artifact_list_response.read_mode%5B3%5D)

[](#artifact_list_response.read_mode)

updated_at: string



Artifact last update timestamp, or null for Artifacts published before this field was recorded

[](#artifact_list_response.updated_at)



user: object { id, email_address }



The user who owns a Code Artifact.

Fields that reference this type are null when the owner's account has been deleted or the owner is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#artifact_list_response.user.id)

email_address: string



User's email address

[](#artifact_list_response.user.email_address)

[](#artifact_list_response.user)



versions: array of object { id, created_at, name }



Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

id: string



Opaque version identifier

[](#artifact_list_response.versions.items.id)

created_at: string



When this version was published

[](#artifact_list_response.versions.items.created_at)

name: string



Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

[](#artifact_list_response.versions.items.name)

[](#artifact_list_response.versions)

[](#artifact_list_response)



ArtifactDeleteResponse object { id, type }



Response for deleting a Code Artifact.

id: string



The ID of the Artifact that was deleted

[](#artifact_delete_response.id)

type: "code_artifact_deleted"



Constant string confirming deletion

[](#artifact_delete_response.type)
