---
title: "Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/compliance_settings"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:26:15Z"
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

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fcompliance_settings)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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


Get Compliance Settings


Update Compliance Settings

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

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Compliance Settings

Copy page



cURL

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

##### Models



ComplianceSettingsState = [ComplianceSettingsStateEnabled](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_enabled) or [ComplianceSettingsStateDisabled](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_disabled)



One of the following:



ComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



ComplianceSettingsStateDisabled object{ type: "disabled" }





type: "disabled"



defaultdisabled



ComplianceSettingsStateDisabled object{ type: "disabled" }





type: "disabled"



defaultdisabled



ComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"





ComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



ComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





ComplianceSettingsStateParam = [ComplianceSettingsStateEnabledParam](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_enabled_param) or [ComplianceSettingsStateDisabledParam](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_disabled_param)



One of the following:



ComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





ComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"





OrganizationComplianceSettings object{ type: "compliance_settings", state }





type: "compliance_settings"



defaultcompliance_settings



state: [ComplianceSettingsState](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state)



Whether the Compliance API is enabled for this organization.

One of the following:



ComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



ComplianceSettingsStateDisabled object{ type: "disabled" }
