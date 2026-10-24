---
title: "Delete Code Artifact - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-23T06:28:49Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fcode%2Fartifacts%2Fdelete)

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
5.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts)

# Delete Code Artifact

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent organization. Returns 404 on a repeated delete of an already-deleted Artifact.

##### Path parameters

artifact_id: string



The Artifact ID (tagged ID, e.g., cart_abc123)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns



type: "code_artifact_deleted"



Constant string confirming deletion

defaultcode_artifact_deleted

id: string



The ID of the Artifact that was deleted

Delete Code Artifact

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
