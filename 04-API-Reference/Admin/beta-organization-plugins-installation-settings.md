---
title: "Installation Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/installation_settings"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-17T06:25:56Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fplugins%2Finstallation_settings)

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

Installation Settings


List Plugin Installation Settings


Set Plugin Installation Setting


Remove Plugin Installation Setting

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

# Installation Settings

Copy page



cURL

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

##### Models



BetaDeletedPluginInstallationSetting object{ type: "plugin_installation_setting_deleted", plugin_id, target }



Confirmation that one target's installation setting was removed, naming the Plugin and the target in place of an ID.



BetaPluginInstallationSetting object{ type: "plugin_installation_setting", created_at, installation_preference, 3 more }



The installation setting an organization-owned Plugin holds for one target. It has no ID of its own: it is addressed by the Plugin's ID and the target.
