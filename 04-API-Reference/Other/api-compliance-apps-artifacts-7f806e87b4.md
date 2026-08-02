---
title: "Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/artifacts"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:07Z"
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

Artifacts


Get artifact metadata


Download artifact content

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

Artifacts






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Artifacts

##### [Get artifact metadata](/docs/en/api/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact_version_id}

##### [Download artifact content](/docs/en/api/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

##### ModelsExpand Collapse 



ArtifactRetrieveResponse object { id, artifact_type, claude_chat_id, 5 more }



Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.

Returns metadata only. Use the sibling `/content` endpoint to fetch the artifact body.

id: string



Artifact ID e.g. 'claude_artifact_abc123'

[](#artifact_retrieve_response.id)

artifact_type: string



MIME-like artifact type e.g. 'application/vnd.ant.code'

[](#artifact_retrieve_response.artifact_type)

claude_chat_id: string



The chat this artifact belongs to

[](#artifact_retrieve_response.claude_chat_id)

created_at: string



Artifact version creation timestamp

[](#artifact_retrieve_response.created_at)

md5: string



Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

[](#artifact_retrieve_response.md5)

size_bytes: number



Size in bytes of the artifact content (UTF-8 encoded)

[](#artifact_retrieve_response.size_bytes)

title: string



Artifact title

[](#artifact_retrieve_response.title)

version_id: string



Artifact version ID e.g. 'claude_artifact_version_abc123'

[](#artifact_retrieve_response.version_id)

[](#artifact_retrieve_response)
