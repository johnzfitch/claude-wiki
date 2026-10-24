---
title: "Organization - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-21T06:29:00Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization)





SearchCtrlK

Include beta APIs

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

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


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

# Organization

Copy page



cURL

##### [Get Current Organization](http-beta-organization-retrieve.md)

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### Models



BetaOrganization object{ type: "organization", id, name }





type: "organization"



Object type.

For Organizations, this is always `"organization"`.

defaultorganization



id: string



ID of the Organization.

formatuuid

name: string



Name of the Organization.



BetaOrganizationRole = "admin" or "billing" or "claude_code_user" or 6 more



One of the following:

"admin"



"billing"



"claude_code_user"



"developer"



"managed"



"membership_admin"



"owner"



"primary_owner"



"user"



#### Organization[API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys)

##### [List API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/playground.md) in the Claude Console.

##### [Update API Key](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### Organization[External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys)

##### [Create External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/create)

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### [List External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/list)

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

##### [Get External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### [Update External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

Partially update an external key config. Omitted fields are left unchanged.

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

#### OrganizationFederation[Issuers](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers)

##### [Create Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/create)

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Issuers](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/list)

GET/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationFederation[Rules](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules)

##### [Create Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/create)

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rules](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/list)

GET/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationFederationRules[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces)

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/add)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/remove)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites)

##### [Create Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

#### Organization[Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts)

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/create)

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/list)

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationService Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Users](https://platform.claude.com/docs/en/api/http/beta/organization/users)

##### [List Users](https://platform.claude.com/docs/en/api/http/beta/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](https://platform.claude.com/docs/en/api/http/beta/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](https://platform.claude.com/docs/en/api/http/beta/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](https://platform.claude.com/docs/en/api/http/beta/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

#### Organization[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### OrganizationWorkspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

#### OrganizationWorkspaces[Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### OrganizationWorkspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits)

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

#### Organization[Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings)

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

#### Organization[Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report)

##### [Get Messages Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

#### Organization[Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report)

##### [Get Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report/retrieve)

GET/v1/organizations/cost_report

#### Organization[MCP Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels)

##### [List Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### OrganizationMCP Tunnels[Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### OrganizationAnalytics[Summaries](http-beta-organization-analytics-summaries.md)

##### [Get Activity Summaries](http-beta-organization-analytics-summaries-list.md)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### OrganizationAnalytics[Users](platform-claude-com-http-beta-organization-analytics-users.md)

##### [List User Activity](platform-claude-com-http-beta-organization-analytics-users-list.md)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### OrganizationAnalyticsAppsChat[Projects](http-beta-organization-analytics-apps-chat-projects.md)

##### [Get Chat Project Usage](http-beta-organization-analytics-apps-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Connectors](http-beta-organization-analytics-connectors.md)

##### [Get Connector Usage](platform-claude-com-http-beta-organization-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Plugins](platform-claude-com-http-beta-organization-analytics-plugins.md)

##### [Get Plugin Usage](platform-claude-com-http-beta-organization-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### OrganizationAnalytics[Skills](http-beta-organization-analytics-skills.md)

##### [Get Skill Usage](platform-claude-com-http-beta-organization-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Artifacts](http-beta-organization-analytics-artifacts.md)

##### [Get Artifact Activity](platform-claude-com-http-beta-organization-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### OrganizationAnalytics[Usage Report](http-beta-organization-analytics-usage-report.md)

##### [Get Token Usage Over Time](http-beta-organization-analytics-usage-report-list.md)

GET/v1/organizations/analytics/usage_report

Get token usage over time across a date range.

#### OrganizationAnalytics[User Usage Report](http-beta-organization-analytics-user-usage-report.md)

##### [Get Per-User Token Usage](http-beta-organization-analytics-user-usage-report-list.md)

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

#### OrganizationAnalytics[Cost Report](http-beta-organization-analytics-cost-report.md)

##### [Get Cost Over Time](http-beta-organization-analytics-cost-report-list.md)

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

#### OrganizationAnalytics[User Cost Report](http-beta-organization-analytics-user-cost-report.md)

##### [Get Per-User Cost](http-beta-organization-analytics-user-cost-report-list.md)

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.

#### Organization[Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

##### [Set Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/set)

POST/v1/organizations/spend_limits

Set a spend limit.

##### [Get Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

##### [List Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/list)

GET/v1/organizations/spend_limits

List the organization's spend limits.

#### OrganizationSpend Limits[Effective](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective)

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective/list)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### OrganizationSpend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests)

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

#### Organization[RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups)

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

##### [Update RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/update)

POST/v1/organizations/rbac_groups/{rbac_group_id}

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Delete RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

#### OrganizationRBAC Groups[Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members)

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/add)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/remove)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

#### Organization[RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles)

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

#### OrganizationRBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.

#### Organization[Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

##### [Create Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/create)

POST/v1/organizations/plugins

Create an organization-owned Plugin and its first version by uploading the version's files.

##### [Get Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/retrieve)

GET/v1/organizations/plugins/{plugin_id}

Retrieve a Plugin by ID.

##### [Update Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/update)

POST/v1/organizations/plugins/{plugin_id}

Change which stored version of an organization-owned Plugin is served to members, for example to roll back to an earlier one. This pins the served version: later uploads are stored but no longer change what is served, and pinning cannot currently be undone, here or in claude.ai.

##### [List Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/list)

GET/v1/organizations/plugins

List the Plugins created under the organization, newest first: those in the organization's own plugin marketplaces and those in members' personal plugin marketplaces.

##### [Delete Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/delete)

DELETE/v1/organizations/plugins/{plugin_id}

Permanently delete a Plugin and every version it holds, exactly as when an administrator deletes it in claude.ai. The Plugin may belong to the organization or to a member, including a member who has since left the organization.

#### OrganizationPlugins[Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions)

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

#### OrganizationPlugins[Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings)

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

#### OrganizationPlugins[Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares)

##### [List Plugin Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares/list)

GET/v1/organizations/plugins/{plugin_id}/shares

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.

#### Organization[Plugin Marketplaces](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces)

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

#### Organization[Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations)

##### [Create a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/create)

POST/v1/organizations/telemetry_destinations

Register an OpenTelemetry destination for the organization.

##### [List Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/list)

GET/v1/organizations/telemetry_destinations

List the organization's destinations, newest first, optionally only those that cover given workspaces.

##### [Retrieve a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/retrieve)

GET/v1/organizations/telemetry_destinations/{destination_id}

Read a destination's configuration, state, and most recent delivery results.

##### [Update a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/update)

POST/v1/organizations/telemetry_destinations/{destination_id}

Change a telemetry destination's settings, its state, or which workspaces it covers.

##### [Delete a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/delete)

DELETE/v1/organizations/telemetry_destinations/{destination_id}

Delete a destination and its workspace list.

##### [Test a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/test)

POST/v1/organizations/telemetry_destinations/{destination_id}/test

Send one test span, named `anthropic.test`, to the destination with its registered headers, once and without retries, and report the destination's answer. The response is 200 whether or not the destination answered with a 2xx status: its `result` has the type `success`, or the type `failure` and the reason in `error`. The destination's configuration, `state` and `delivery_health` do not change. A disabled destination can be tested too. Wait 10 seconds between tests of one destination; a request that comes sooner may be answered with status 429.

#### OrganizationTelemetry Destinations[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces)

##### [List Telemetry Destination Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/list)

GET/v1/organizations/telemetry_destinations/{destination_id}/workspaces

List the workspaces on a destination's workspace list, newest entry first.

##### [Add a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/add)

POST/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Add one workspace to a destination's workspace list.

##### [Remove a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/remove)

DELETE/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Remove one workspace from a destination's workspace list.

#### Organization[Webhooks](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks)

##### [Create Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/create)

POST/v1/organizations/webhooks

Create an organization webhook endpoint.

##### [List Organization Webhook Endpoints](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/list)

GET/v1/organizations/webhooks

List the organization's webhook endpoints.

##### [Get Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/retrieve)

GET/v1/organizations/webhooks/{webhook_endpoint_id}

Retrieve an organization webhook endpoint by ID.

##### [Update Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/update)

POST/v1/organizations/webhooks/{webhook_endpoint_id}

Update an organization webhook endpoint. Only the fields you send are changed.

##### [Delete Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/delete)

DELETE/v1/organizations/webhooks/{webhook_endpoint_id}

Delete an organization webhook endpoint.

##### [Regenerate Organization Webhook Endpoint Signing Secret](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/regenerate_signing_secret)

POST/v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret

Replace an organization webhook endpoint's signing secret. The old secret stops working immediately. The new secret is returned only in this response.
