---
title: "Get Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/compliance_settings/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:33Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fcompliance_settings%2Fretrieve)

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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces


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


Completions


Create a Text Completion Deprecated

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/retrieve).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings)

# Get Compliance Settings

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per organization, addressed without an identifier. The `state` field reflects whether the Compliance API is enabled. An organization with a parent organization reads the state inherited from the parent's configuration.

##### Returns

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





type: "disabled"



defaultdisabled

Get Compliance Settings

cURL



```python
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
