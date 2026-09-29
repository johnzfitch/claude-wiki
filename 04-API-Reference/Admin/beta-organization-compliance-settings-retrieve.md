---
title: "Get Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/compliance_settings/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:38:46Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fcompliance_settings%2Fretrieve)

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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


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


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings)

# Get Compliance Settings

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per organization, addressed without an identifier. The `state` field reflects whether the Compliance API is enabled. An organization with a parent organization reads the state inherited from the parent's configuration.

##### Returns



BetaComplianceSettings object{ type: "compliance_settings", state }





type: "compliance_settings"



defaultcompliance_settings



state: [BetaComplianceSettingsState](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state)



Whether the Compliance API is enabled for this organization.

One of the following:



BetaComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



BetaComplianceSettingsStateDisabled object{ type: "disabled" }

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
