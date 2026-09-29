---
title: "Admin - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/admin"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:44:09Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fadmin)

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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


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

1.  [API reference](../Endpoints/http.md)

# Admin

#### Admin[Organizations](https://platform.claude.com/docs/en/api/http/admin/organizations)

##### [Get Current Organization](https://platform.claude.com/docs/en/api/http/admin/organizations/me)

GET/v1/organizations/me

#### Admin[Invites](https://platform.claude.com/docs/en/api/http/admin/invites)

##### [Create Invite](https://platform.claude.com/docs/en/api/http/admin/invites/create)

POST/v1/organizations/invites

##### [Get Invite](https://platform.claude.com/docs/en/api/http/admin/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

##### [List Invites](https://platform.claude.com/docs/en/api/http/admin/invites/list)

GET/v1/organizations/invites

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/admin/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

#### Admin[Users](https://platform.claude.com/docs/en/api/http/admin/users)

##### [Get User](https://platform.claude.com/docs/en/api/http/admin/users/retrieve)

GET/v1/organizations/users/{user_id}

##### [List Users](https://platform.claude.com/docs/en/api/http/admin/users/list)

GET/v1/organizations/users

##### [Update User](https://platform.claude.com/docs/en/api/http/admin/users/update)

POST/v1/organizations/users/{user_id}

##### [Remove User](https://platform.claude.com/docs/en/api/http/admin/users/delete)

DELETE/v1/organizations/users/{user_id}

#### Admin[RBAC Groups](https://platform.claude.com/docs/en/api/http/admin/rbac_groups)

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/list)

GET/v1/organizations/rbac_groups

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{group_id}

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/create)

POST/v1/organizations/rbac_groups

##### [Update RBAC Group](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/update)

POST/v1/organizations/rbac_groups/{group_id}

##### [Delete RBAC Group](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{group_id}

#### AdminRBAC Groups[Members](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members)

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}

#### Admin[RBAC Roles](https://platform.claude.com/docs/en/api/http/admin/rbac_roles)

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/admin/rbac_roles/list)

GET/v1/organizations/rbac_roles

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/admin/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{role_id}

#### AdminRBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/admin/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/admin/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{role_id}/permissions

#### Admin[Workspaces](https://platform.claude.com/docs/en/api/http/admin/workspaces)

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/admin/workspaces/list)

GET/v1/organizations/workspaces

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### AdminWorkspaces[Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/members)

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### AdminWorkspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/admin/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/admin/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

#### AdminWorkspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts)

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/create)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/admin/workspaces/service_accounts/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

#### Admin[API Keys](https://platform.claude.com/docs/en/api/http/admin/api_keys)

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/admin/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

##### [List API Keys](https://platform.claude.com/docs/en/api/http/admin/api_keys/list)

GET/v1/organizations/api_keys

##### [Update API Key](https://platform.claude.com/docs/en/api/http/admin/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### Admin[External Keys](https://platform.claude.com/docs/en/api/http/admin/external_keys)

##### [Create External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/create)

POST/v1/organizations/external_keys

##### [List External Keys](https://platform.claude.com/docs/en/api/http/admin/external_keys/list)

GET/v1/organizations/external_keys

##### [Get External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

##### [Update External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/admin/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

#### Admin[Usage Report](https://platform.claude.com/docs/en/api/http/admin/usage_report)

##### [Get Messages Usage Report](https://platform.claude.com/docs/en/api/http/admin/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/http/admin/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

#### Admin[Cost Report](https://platform.claude.com/docs/en/api/http/admin/cost_report)

##### [Get Cost Report](https://platform.claude.com/docs/en/api/http/admin/cost_report/retrieve)

GET/v1/organizations/cost_report

#### Admin[Analytics](http-admin-analytics.md)

##### [Get Activity Summaries](http-admin-analytics-retrieve-summaries.md)

GET/v1/organizations/analytics/summaries

#### AdminAnalytics[Usage](http-admin-analytics-usage.md)

##### [Get Token Usage Over Time](http-admin-analytics-usage-list.md)

GET/v1/organizations/analytics/usage_report

##### [Get Per-User Token Usage](http-admin-analytics-usage-list-by-user.md)

GET/v1/organizations/analytics/user_usage_report

#### AdminAnalytics[Cost](http-admin-analytics-cost.md)

##### [Get Cost Over Time](http-admin-analytics-cost-list.md)

GET/v1/organizations/analytics/cost_report

##### [Get Per-User Cost](http-admin-analytics-cost-list-by-user.md)

GET/v1/organizations/analytics/user_cost_report

#### AdminAnalytics[Users](http-admin-analytics-users.md)

##### [List User Activity](http-admin-analytics-users-list.md)

GET/v1/organizations/analytics/users

#### AdminAnalytics[Skills](http-admin-analytics-skills.md)

##### [Get Skill Usage](http-admin-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

#### AdminAnalytics[Connectors](http-admin-analytics-connectors.md)

##### [Get Connector Usage](http-admin-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

#### AdminAnalytics[Chat Projects](http-admin-analytics-chat-projects.md)

##### [Get Chat Project Usage](http-admin-analytics-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

#### AdminAnalytics[Plugins](http-admin-analytics-plugins.md)

##### [Get Plugin Usage](http-admin-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

#### AdminAnalytics[Artifacts](http-admin-analytics-artifacts.md)

##### [Get Artifact Activity](http-admin-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

#### Admin[Spend Limits](https://platform.claude.com/docs/en/api/http/admin/spend_limits)

##### [Set Spend Limit](https://platform.claude.com/docs/en/api/http/admin/spend_limits/create)

POST/v1/organizations/spend_limits

##### [Get Spend Limit](https://platform.claude.com/docs/en/api/http/admin/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/http/admin/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/admin/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

#### AdminSpend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/admin/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/admin/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/admin/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/admin/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/admin/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

#### Admin[Rate Limits](https://platform.claude.com/docs/en/api/http/admin/rate_limits)

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/admin/rate_limits/list)

GET/v1/organizations/rate_limits

#### Admin[Service Accounts](https://platform.claude.com/docs/en/api/http/admin/service_accounts)

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/create)

POST/v1/organizations/service_accounts

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/admin/service_accounts/list)

GET/v1/organizations/service_accounts

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

#### AdminService Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/create)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/admin/service_accounts/workspaces/delete)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

#### Admin[Federation Issuers](https://platform.claude.com/docs/en/api/http/admin/federation_issuers)

##### [Create Federation Issuer](https://platform.claude.com/docs/en/api/http/admin/federation_issuers/create)

POST/v1/organizations/federation_issuers

##### [Get Federation Issuer](https://platform.claude.com/docs/en/api/http/admin/federation_issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

##### [List Federation Issuers](https://platform.claude.com/docs/en/api/http/admin/federation_issuers/list)

GET/v1/organizations/federation_issuers

##### [Update Federation Issuer](https://platform.claude.com/docs/en/api/http/admin/federation_issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

##### [Archive Federation Issuer](https://platform.claude.com/docs/en/api/http/admin/federation_issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

#### Admin[Federation Rules](https://platform.claude.com/docs/en/api/http/admin/federation_rules)

##### [Create Federation Rule](https://platform.claude.com/docs/en/api/http/admin/federation_rules/create)

POST/v1/organizations/federation_rules

##### [Get Federation Rule](https://platform.claude.com/docs/en/api/http/admin/federation_rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

##### [List Federation Rules](https://platform.claude.com/docs/en/api/http/admin/federation_rules/list)

GET/v1/organizations/federation_rules

##### [Update Federation Rule](https://platform.claude.com/docs/en/api/http/admin/federation_rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/http/admin/federation_rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

#### AdminFederation Rules[Workspaces](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces)

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/create)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/admin/federation_rules/workspaces/delete)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

#### Admin[MCP Tunnels](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels)

##### [Get Tunnel](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

##### [List Tunnels](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

##### [Archive Tunnel](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

#### AdminMCP Tunnels[Tunnel Certificates](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/admin/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
