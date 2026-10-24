---
title: "Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/versions"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-17T06:26:13Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fplugins%2Fversions)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Create Plugin


Get Plugin


Update Plugin


List Plugins


Delete Plugin

Versions


Create Plugin Version


List Plugin Versions


Get Plugin Version


Download Plugin Version Archive

Installation Settings

Shares

Plugin Marketplaces

Telemetry Destinations


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

# Versions

Copy page



cURL

##### [Create Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/create)

POST/v1/organizations/plugins/{plugin_id}/versions

Add a version to an organization-owned Plugin by uploading the new version's files; it becomes the version served to members unless the Plugin's served version has been pinned.

##### [List Plugin Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/list)

GET/v1/organizations/plugins/{plugin_id}/versions

List a Plugin's versions, newest first.

##### [Get Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/retrieve)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

##### [Download Plugin Version Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/download)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}/content

Download one version's `.zip` archive, exactly as stored. Each download of a Plugin from a member's personal plugin marketplace is recorded on the Compliance API activity feed.

##### Models



BetaPluginVersion object{ type: "plugin_version", id, components, 9 more }
