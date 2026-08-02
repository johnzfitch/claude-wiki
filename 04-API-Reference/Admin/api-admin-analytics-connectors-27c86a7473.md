---
title: "Connectors - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/connectors"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:17Z"
tags: ["api", "connectors"]
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


Get Connector Usage

Chat Projects

Plugins

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

Connectors




# Connectors

##### [Get Connector Usage](/docs/en/api/admin/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

##### ModelsExpand Collapse 



ConnectorUsage object { data, next_page }



Response for GET /v1/organizations/analytics/connectors.



data: array of object { chat_metrics, claude_code_metrics, connector_name, 10 more }





chat_metrics: object { distinct_conversation_connector_used_count }



Claude.ai activity metrics for a single connector on a given day.

distinct_conversation_connector_used_count: number



Number of distinct conversations in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.chat_metrics.distinct_conversation_connector_used_count)

[](#connector_usage.data.items.chat_metrics)



claude_code_metrics: object { distinct_session_connector_used_count }



Claude Code activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number



Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.claude_code_metrics.distinct_session_connector_used_count)

[](#connector_usage.data.items.claude_code_metrics)

connector_name: string



Name of the connector

[](#connector_usage.data.items.connector_name)



cowork_metrics: object { distinct_session_connector_used_count }



Cowork activity metrics for a single connector on a given day.

distinct_session_connector_used_count: number



Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.cowork_metrics.distinct_session_connector_used_count)

[](#connector_usage.data.items.cowork_metrics)

distinct_user_count: number



Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

[](#connector_usage.data.items.distinct_user_count)



office_metrics: object { excel, outlook, powerpoint, word }



Office Agent activity metrics for a single connector on a given day, broken out by Office product.



excel: [ConnectorOfficeProductMetrics](/docs/en/api/admin/analytics#connector_office_product_metrics) { distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.distinct_session_connector_used_count)

[](#connector_usage.data.items.office_metrics.excel)



outlook: [ConnectorOfficeProductMetrics](/docs/en/api/admin/analytics#connector_office_product_metrics) { distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.distinct_session_connector_used_count)

[](#connector_usage.data.items.office_metrics.outlook)



powerpoint: [ConnectorOfficeProductMetrics](/docs/en/api/admin/analytics#connector_office_product_metrics) { distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.distinct_session_connector_used_count)

[](#connector_usage.data.items.office_metrics.powerpoint)



word: [ConnectorOfficeProductMetrics](/docs/en/api/admin/analytics#connector_office_product_metrics) { distinct_session_connector_used_count }



Office Agent activity metrics for a single connector on a given day within one Office product.

distinct_session_connector_used_count: number



Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#connector_usage.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.distinct_session_connector_used_count)

[](#connector_usage.data.items.office_metrics.word)

[](#connector_usage.data.items.office_metrics)

product: optional string



Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by\[\] or filter\[\] there is rejected). Present only when the request grouped by product.

[](#connector_usage.data.items.product)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#connector_usage.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#connector_usage.data.items.rbac_group_name)

read_call_count: optional number



Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read_call_count, write_call_count, or unclassified_call_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified_call_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting_date/ending_date) applies both rules server-side.

[](#connector_usage.data.items.read_call_count)

unclassified_call_count: optional number



Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

[](#connector_usage.data.items.unclassified_call_count)

user_id: optional string



Tagged user identifier (e.g. user\_...). Present only when the request grouped by user_id.

[](#connector_usage.data.items.user_id)

write_call_count: optional number



Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

[](#connector_usage.data.items.write_call_count)

[](#connector_usage.data)

next_page: string



Opaque cursor for the next page, or null if no more results

[](#connector_usage.next_page)
