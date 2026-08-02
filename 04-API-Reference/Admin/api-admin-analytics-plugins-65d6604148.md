---
title: "Plugins - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/plugins"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:53Z"
tags: ["api", "plugins"]
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


Get Activity Summaries

Usage

Cost

Users

Skills

Connectors

Chat Projects

Plugins


Get Plugin Usage

Artifacts

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

Plugins




# Plugins

##### [Get Plugin Usage](/docs/en/api/admin/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

##### ModelsExpand Collapse 



PluginUsage object { data, next_page }



Response for GET /v1/organizations/analytics/plugins.



data: array of object { claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }





claude_code_metrics: object { distinct_session_plugin_used_count }



Claude Code activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number



Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

[](#plugin_usage.data.items.claude_code_metrics.distinct_session_plugin_used_count)

[](#plugin_usage.data.items.claude_code_metrics)



cowork_metrics: object { distinct_session_plugin_used_count }



Cowork activity metrics for a single plugin on a given day.

distinct_session_plugin_used_count: number



Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

[](#plugin_usage.data.items.cowork_metrics.distinct_session_plugin_used_count)

[](#plugin_usage.data.items.cowork_metrics)

distinct_user_count: number



Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

[](#plugin_usage.data.items.distinct_user_count)

install_count: number



Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

[](#plugin_usage.data.items.install_count)

invocation_count: number



Number of plugin invocations on the requested day

[](#plugin_usage.data.items.invocation_count)

plugin_name: string



Name of the plugin

[](#plugin_usage.data.items.plugin_name)

plugin_id: optional string



Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

[](#plugin_usage.data.items.plugin_id)

product: optional string



Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by\[\] or filter\[\] there is rejected). Present only when the request grouped by product.

[](#plugin_usage.data.items.product)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#plugin_usage.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#plugin_usage.data.items.rbac_group_name)

user_id: optional string



Tagged user identifier (e.g. user\_...). Present only when the request grouped by user_id.

[](#plugin_usage.data.items.user_id)

[](#plugin_usage.data)

next_page: string



Opaque cursor for the next page, or null if no more results

[](#plugin_usage.next_page)
