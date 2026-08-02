---
title: "Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/artifacts"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:17Z"
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


Get Activity Summaries

Usage

Cost

Users

Skills

Connectors

Chat Projects

Plugins

Artifacts


Get Artifact Activity

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

Artifacts




# Artifacts

##### [Get Artifact Activity](/docs/en/api/admin/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts

##### ModelsExpand Collapse 



ArtifactUsage object { data, next_page }



Response for GET /v1/organizations/analytics/artifacts.

`next_page` is null on ungrouped queries — the artifact-type cube is finite and returned in full. Grouped queries (group_by\[\] on user_id / rbac_group_id) multiply the cube and paginate like the other analytics list endpoints.



data: array of object { artifact_type, artifacts_created_count, distinct_user_count, 6 more }



artifact_type: string



Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

[](#artifact_usage.data.items.artifact_type)

artifacts_created_count: number



Number of artifacts created in this bucket on the requested day

[](#artifact_usage.data.items.artifacts_created_count)

distinct_user_count: number



Number of distinct users who created artifacts in this bucket on the requested day

[](#artifact_usage.data.items.distinct_user_count)

is_shared: boolean



Whether the artifacts in this bucket have ever been shared.

[](#artifact_usage.data.items.is_shared)

published_artifacts_created_count: number



Number of those artifacts that have been published

[](#artifact_usage.data.items.published_artifacts_created_count)

product: optional string



Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by\[\] or filter\[\] there is rejected). Present only when the request grouped by product.

[](#artifact_usage.data.items.product)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#artifact_usage.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#artifact_usage.data.items.rbac_group_name)

user_id: optional string



Tagged user identifier (e.g. user\_...). Present only when the request grouped by user_id.

[](#artifact_usage.data.items.user_id)

[](#artifact_usage.data)

next_page: optional string



Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

[](#artifact_usage.next_page)
