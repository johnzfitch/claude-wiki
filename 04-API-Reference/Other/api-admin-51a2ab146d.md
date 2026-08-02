---
title: "Admin - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:57Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

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


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Admin




# Admin

#### AdminOrganizations

##### [Get Current Organization](/docs/en/api/admin/organizations/me)

GET/v1/organizations/me

#### AdminInvites

##### [Create Invite](/docs/en/api/admin/invites/create)

POST/v1/organizations/invites

##### [Get Invite](/docs/en/api/admin/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

##### [List Invites](/docs/en/api/admin/invites/list)

GET/v1/organizations/invites

##### [Delete Invite](/docs/en/api/admin/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

#### AdminUsers

##### [Get User](/docs/en/api/admin/users/retrieve)

GET/v1/organizations/users/{user_id}

##### [List Users](/docs/en/api/admin/users/list)

GET/v1/organizations/users

##### [Update User](/docs/en/api/admin/users/update)

POST/v1/organizations/users/{user_id}

##### [Remove User](/docs/en/api/admin/users/delete)

DELETE/v1/organizations/users/{user_id}

#### AdminRBAC Groups

##### [List RBAC Groups](/docs/en/api/admin/rbac_groups/list)

GET/v1/organizations/rbac_groups

##### [Get RBAC Group](/docs/en/api/admin/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{group_id}

##### [Create RBAC Group](/docs/en/api/admin/rbac_groups/create)

POST/v1/organizations/rbac_groups

##### [Update RBAC Group](/docs/en/api/admin/rbac_groups/update)

POST/v1/organizations/rbac_groups/{group_id}

##### [Delete RBAC Group](/docs/en/api/admin/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{group_id}

#### AdminRBAC GroupsMembers

##### [List RBAC Group Members](/docs/en/api/admin/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{group_id}/members

##### [Add RBAC Group Member](/docs/en/api/admin/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{group_id}/members

##### [Remove RBAC Group Member](/docs/en/api/admin/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{group_id}/members/{user_id}

#### AdminRBAC Roles

##### [List RBAC Roles](/docs/en/api/admin/rbac_roles/list)

GET/v1/organizations/rbac_roles

##### [Get RBAC Role](/docs/en/api/admin/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{role_id}

#### AdminRBAC RolesPermissions

##### [List RBAC Role Permissions](/docs/en/api/admin/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{role_id}/permissions

#### AdminWorkspaces

##### [Create Workspace](/docs/en/api/admin/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](/docs/en/api/admin/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [List Workspaces](/docs/en/api/admin/workspaces/list)

GET/v1/organizations/workspaces

##### [Update Workspace](/docs/en/api/admin/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](/docs/en/api/admin/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### AdminWorkspacesMembers

##### [Create Workspace Member](/docs/en/api/admin/workspaces/members/create)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](/docs/en/api/admin/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [List Workspace Members](/docs/en/api/admin/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Update Workspace Member](/docs/en/api/admin/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](/docs/en/api/admin/workspaces/members/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### AdminWorkspacesRate Limits

##### [List Workspace Rate Limits](/docs/en/api/admin/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

#### AdminWorkspacesService Accounts

##### [Create Service Account Workspace Member](/docs/en/api/admin/workspaces/service_accounts/create)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Get Service Account Workspace Member](/docs/en/api/admin/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [List Service Account Workspace Members](/docs/en/api/admin/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

##### [Update Service Account Workspace Member](/docs/en/api/admin/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

##### [Delete Service Account Workspace Member](/docs/en/api/admin/workspaces/service_accounts/delete)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

#### AdminAPI Keys

##### [Retrieve API Key (Admin API)](/docs/en/api/admin/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

##### [List API Keys](/docs/en/api/admin/api_keys/list)

GET/v1/organizations/api_keys

##### [Update API Key](/docs/en/api/admin/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### AdminExternal Keys

##### [Create External Key](/docs/en/api/admin/external_keys/create)

POST/v1/organizations/external_keys

##### [List External Keys](/docs/en/api/admin/external_keys/list)

GET/v1/organizations/external_keys

##### [Get External Key](/docs/en/api/admin/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

##### [Update External Key](/docs/en/api/admin/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

##### [Delete External Key](/docs/en/api/admin/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

##### [Validate External Key](/docs/en/api/admin/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

#### AdminUsage Report

##### [Get Messages Usage Report](/docs/en/api/admin/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](/docs/en/api/admin/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

#### AdminCost Report

##### [Get Cost Report](/docs/en/api/admin/cost_report/retrieve)

GET/v1/organizations/cost_report

#### AdminAnalytics

##### [Get Activity Summaries](/docs/en/api/admin/analytics/retrieve_summaries)

GET/v1/organizations/analytics/summaries

#### AdminAnalyticsUsage

##### [Get Token Usage Over Time](/docs/en/api/admin/analytics/usage/list)

GET/v1/organizations/analytics/usage_report

##### [Get Per-User Token Usage](/docs/en/api/admin/analytics/usage/list_by_user)

GET/v1/organizations/analytics/user_usage_report

#### AdminAnalyticsCost

##### [Get Cost Over Time](/docs/en/api/admin/analytics/cost/list)

GET/v1/organizations/analytics/cost_report

##### [Get Per-User Cost](/docs/en/api/admin/analytics/cost/list_by_user)

GET/v1/organizations/analytics/user_cost_report

#### AdminAnalyticsUsers

##### [List User Activity](/docs/en/api/admin/analytics/users/list)

GET/v1/organizations/analytics/users

#### AdminAnalyticsSkills

##### [Get Skill Usage](/docs/en/api/admin/analytics/skills/list)

GET/v1/organizations/analytics/skills

#### AdminAnalyticsConnectors

##### [Get Connector Usage](/docs/en/api/admin/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

#### AdminAnalyticsChat Projects

##### [Get Chat Project Usage](/docs/en/api/admin/analytics/chat_projects/list)

GET/v1/organizations/analytics/apps/chat/projects

#### AdminAnalyticsPlugins

##### [Get Plugin Usage](/docs/en/api/admin/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

#### AdminAnalyticsArtifacts

##### [Get Artifact Activity](/docs/en/api/admin/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts

#### AdminSpend Limits

##### [Set Spend Limit](/docs/en/api/admin/spend_limits/create)

POST/v1/organizations/spend_limits

##### [Get Spend Limit](/docs/en/api/admin/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

##### [Delete Spend Limit](/docs/en/api/admin/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

##### [List Effective Spend Limits](/docs/en/api/admin/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

#### AdminSpend LimitsIncrease Requests

##### [List Spend Limit Increase Requests](/docs/en/api/admin/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

##### [Get Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

##### [Approve Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

##### [Deny Spend Limit Increase Request](/docs/en/api/admin/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

#### AdminRate Limits

##### [List Organization Rate Limits](/docs/en/api/admin/rate_limits/list)

GET/v1/organizations/rate_limits

#### AdminService Accounts

##### [Create Service Account](/docs/en/api/admin/service_accounts/create)

POST/v1/organizations/service_accounts

##### [Get Service Account](/docs/en/api/admin/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

##### [List Service Accounts](/docs/en/api/admin/service_accounts/list)

GET/v1/organizations/service_accounts

##### [Update Service Account](/docs/en/api/admin/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

##### [Archive Service Account](/docs/en/api/admin/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

#### AdminService AccountsWorkspaces

##### [Add Workspace To Service Account](/docs/en/api/admin/service_accounts/workspaces/create)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [List Workspaces For Service Account](/docs/en/api/admin/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

##### [Remove Workspace From Service Account](/docs/en/api/admin/service_accounts/workspaces/delete)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

#### AdminFederation Issuers

##### [Create Federation Issuer](/docs/en/api/admin/federation_issuers/create)

POST/v1/organizations/federation_issuers

##### [Get Federation Issuer](/docs/en/api/admin/federation_issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

##### [List Federation Issuers](/docs/en/api/admin/federation_issuers/list)

GET/v1/organizations/federation_issuers

##### [Update Federation Issuer](/docs/en/api/admin/federation_issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

##### [Archive Federation Issuer](/docs/en/api/admin/federation_issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

#### AdminFederation Rules

##### [Create Federation Rule](/docs/en/api/admin/federation_rules/create)

POST/v1/organizations/federation_rules

##### [Get Federation Rule](/docs/en/api/admin/federation_rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

##### [List Federation Rules](/docs/en/api/admin/federation_rules/list)

GET/v1/organizations/federation_rules

##### [Update Federation Rule](/docs/en/api/admin/federation_rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

##### [Archive Federation Rule](/docs/en/api/admin/federation_rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

#### AdminFederation RulesWorkspaces

##### [List Federation Rule Workspaces](/docs/en/api/admin/federation_rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Add Federation Rule Workspace](/docs/en/api/admin/federation_rules/workspaces/create)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

##### [Remove Federation Rule Workspace](/docs/en/api/admin/federation_rules/workspaces/delete)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

#### AdminMCP Tunnels

##### [Get Tunnel](/docs/en/api/admin/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

##### [List Tunnels](/docs/en/api/admin/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](/docs/en/api/admin/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](/docs/en/api/admin/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

##### [Archive Tunnel](/docs/en/api/admin/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

#### AdminMCP TunnelsTunnel Certificates

##### [Create Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
