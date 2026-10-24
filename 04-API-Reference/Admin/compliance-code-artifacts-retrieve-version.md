---
title: "Download Code Artifact Version Content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-12T06:41:57Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fcode%2Fartifacts%2Fretrieve_version)

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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Delete Code Artifact


Completions


Create a Text Completion Deprecated

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Code](https://platform.claude.com/docs/en/api/http/compliance/code)
4.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/code/artifacts)

# Download Code Artifact Version Content

Copy page



GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

Streams the content of one version of a Claude Code Artifact as the response body.

Returns 404 for Artifacts that don't exist or belong to another parent organization. A listed version id can start returning 404 if subsequent publishes rotated it out of retained history — re-list on 404. Returns 503 while the version's content upload is still in flight or was abandoned — retry with backoff. Returns 422 for a version that has more than one file, because the Compliance API returns only single-file versions. Do not retry a 422. The 422's `error.details.error_code` is `multi_file_unavailable`. Oversized encoded content aborts mid-stream: headers and initial bytes arrive but the body terminates early — an aborted chunked transfer is the only truncation signal for encoded content. `Content-MD5` is emitted only for identity-stored content; validate against it when present.

##### Path parameters

artifact_id: string



The Artifact ID (tagged ID, e.g., cart_abc123)

version_id: string



Opaque version identifier from the Artifact's `versions` list

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



Download Code Artifact Version Content

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
