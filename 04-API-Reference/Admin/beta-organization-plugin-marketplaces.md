---
title: "Plugin Marketplaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugin_marketplaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-17T06:25:26Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fplugin_marketplaces)

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

Plugin Marketplaces


List Plugin Marketplaces


Get Plugin Marketplace


Update Plugin Marketplace


Validate Plugin Marketplace Repository


Validate Plugin Marketplace Archive

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

# Plugin Marketplaces

Copy page



cURL

##### [List Plugin Marketplaces](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/list)

GET/v1/organizations/plugin_marketplaces

List the plugin marketplaces Plugins live in, newest first: the organization's own and its members' personal ones.

##### [Get Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/retrieve)

GET/v1/organizations/plugin_marketplaces/{marketplace_id}

Retrieve a plugin marketplace by ID.

##### [Update Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/update)

POST/v1/organizations/plugin_marketplaces/{marketplace_id}

Set the default installation setting of one of the organization's own plugin marketplaces. Every Plugin in it without a setting of its own gets this default as its organization-wide setting, including Plugins added later.

##### [Validate Plugin Marketplace Repository](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_repository)

POST/v1/organizations/plugin_marketplaces/validate_repository

Check whether a plugin marketplace held in a public GitHub repository would synchronize into claude.ai, without connecting or storing it.

##### [Validate Plugin Marketplace Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_archive)

POST/v1/organizations/plugin_marketplaces/validate_archive

Check whether a plugin marketplace, uploaded as a `.zip` of the marketplace directory, would synchronize into claude.ai, without connecting or storing it.

##### Models



BetaPluginMarketplace object{ type: "plugin_marketplace", id, created_at, 7 more }





BetaPluginMarketplaceValidationPluginError object{ error, error_code, name }



error: string



Why the plugin would be skipped by a synchronization.

error_code: string



A stable identifier for the reason — the value to branch on.

name: string



The plugin's name, as its entry in marketplace.json declares it.



BetaPluginMarketplaceValidationPluginWarning object{ error_code, message }



error_code: string



A stable identifier for the kind of warning.

message: string



What would be left out, and why.



BetaPluginMarketplaceValidationPluginWarnings object{ name, warnings }



name: string



The plugin's name, as its entry in marketplace.json declares it.



warnings: array of [BetaPluginMarketplaceValidationPluginWarning](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces#beta_plugin_marketplace_validation_plugin_warning) { error_code, message }



The parts of the plugin a synchronization would leave out.

error_code: string



A stable identifier for the kind of warning.

message: string



What would be left out, and why.



BetaPluginMarketplaceValidationReport object{ type: "plugin_marketplace_validation_report", commit_sha, manifest_error, 6 more }



The outcome of validating plugin marketplace content: a report, not a stored object, so nothing in it can be retrieved afterwards.
