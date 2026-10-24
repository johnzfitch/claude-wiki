---
title: "Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-23T06:28:35Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fcode%2Fartifacts)

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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


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

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Download Code Artifact Content


Delete Code Artifact


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[AWS IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md)[Google Cloud IAM permissions](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md)[Versions](../Endpoints/versioning.md)[Migrating to API version 2026-10-21](../Endpoints/migration-2026-10-21.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Code](https://platform.claude.com/docs/en/api/http/compliance/apps/code)

# Artifacts

Copy page



API version 2026-10-21

##### [List Code Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/list)

GET/v1/compliance/apps/code/artifacts

List Claude Code Artifacts owned by organizations under the parent organization.

##### [Download Code Artifact Version Content](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/retrieve_version)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

Streams the content of one version of an Artifact as the response body, in chunks with no `Content-Length`. With `multi_file_format=zip`, a version with more than one file, other than a Claude Doc's (an Artifact whose `artifact_type` is `claude_docs`), comes back as a ZIP archive of its files.

##### [Download Code Artifact Content](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/download)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/content

Streams an Artifact's current content as the response body, in chunks with no `Content-Length`.

##### [Delete Code Artifact](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/delete)

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.

##### Models



ArtifactListResponse object{ id, artifact_type, organization_uuid, 6 more }



An Artifact: a site published from Claude Code, or a document made from one of Anthropic's built-in Artifact types (Claude Docs, Slides, Design, …). `artifact_type` says which.



ArtifactDeleteResponse object{ type: "code_artifact_deleted", id }



Response for deleting a Code Artifact.



type: "code_artifact_deleted"



Constant string confirming deletion

defaultcode_artifact_deleted

id: string



The ID of the Artifact that was deleted
