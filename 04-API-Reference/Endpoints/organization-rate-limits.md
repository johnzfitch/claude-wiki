---
title: "Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rate_limits"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:26:21Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Frate_limits)

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


List Organization Rate Limits

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

A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Rate Limits

Copy page



cURL

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

##### Models



OrganizationRateLimit object{ type: "rate_limit", id, group, 3 more }





OrganizationRateLimitBatchGroup object{ type: "batch", id }





type: "batch"



Always `batch`: the Message Batches API.

defaultbatch

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitFilesGroup object{ type: "files", id }





type: "files"



Always `files`: the Files API.

defaultfiles

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitModelGroup object{ type: "model_group", id, display_name }





type: "model_group"



Always `model_group`: a family of models.

defaultmodel_group

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

display_name: string



Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.



OrganizationRateLimitSkillsGroup object{ type: "skills", id }





type: "skills"



Always `skills`: the Skills API.

defaultskills

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitTokenCountGroup object{ type: "token_count", id }





type: "token_count"



Always `token_count`: the Token Count API.

defaulttoken_count

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitValue object{ type, value }



type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number



The configured limit value for this limiter type.



OrganizationRateLimitWebSearchGroup object{ type: "web_search", id }





type: "web_search"



Always `web_search`: the Messages API web search tool.

defaultweb_search

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.
