---
title: "Update Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/compliance_settings/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:12Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fcompliance_settings%2Fupdate)

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

A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings)

# Update Compliance Settings

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins capturing organization activity events. Setting it to `disabled` turns both off. `state` reflects whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the resource unchanged. A `disabled` request stays in effect until a later `enabled` request or the organization's next provisioning action that enables Access Transparency: enabling Access Transparency also enables the Compliance API, which serves its activity events, so such provisioning (including re-runs) re-enables the Compliance API even after a `disabled` request. Automated provisioning never disables compliance settings.

##### Body



state: [ComplianceSettingsStateParam](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_param)



Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

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

Update Compliance Settings

cURL



```python
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
