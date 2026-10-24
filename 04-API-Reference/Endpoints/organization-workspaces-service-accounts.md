---
title: "Service Accounts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/service_accounts"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:26:11Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fworkspaces%2Fservice_accounts)

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


List Workspaces


Create Workspace


Get Workspace


Update Workspace


Archive Workspace

Rate Limits

Members

Service Accounts


List Service Account Workspace Members


Create Service Account Workspace Member


Get Service Account Workspace Member


Update Service Account Workspace Member


Delete Service Account Workspace Member

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

A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Service Accounts

Copy page



cURL

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### Models



ServiceAccountRemoveResponse object{ type: "service_account_workspace_member_deleted", service_account_id, workspace_id }





type: "service_account_workspace_member_deleted"



defaultservice_account_workspace_member_deleted

service_account_id: string



Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

workspace_id: string



Tagged workspace ID (`wrkspc_...`) named in the delete request.
