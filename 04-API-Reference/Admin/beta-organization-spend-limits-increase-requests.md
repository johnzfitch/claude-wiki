---
title: "Increase Requests - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-27T06:27:05Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fspend_limits%2Fincrease_requests)

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

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Effective Spend Limits

Increase Requests


List Spend Limit Increase Requests


Get Spend Limit Increase Request


Approve Spend Limit Increase Request


Deny Spend Limit Increase Request

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
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

# Increase Requests

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.

##### Models



BetaSpendLimitIncreaseRequest object{ type: "spend_limit_increase_request", id, actor, 6 more }





IncreaseRequestApproveResponse object{ type: "spend_limit_increase_request", id, actor, 7 more }
