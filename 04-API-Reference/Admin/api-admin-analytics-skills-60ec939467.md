---
title: "Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/analytics/skills"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:19Z"
tags: ["api", "skills"]
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


Get Skill Usage

Connectors

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

Skills




# Skills

##### [Get Skill Usage](/docs/en/api/admin/analytics/skills/list)

GET/v1/organizations/analytics/skills

##### ModelsExpand Collapse 



SkillUsage object { data, next_page }



Response for GET /v1/organizations/analytics/skills.



data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 14 more }





chat_metrics: object { distinct_conversation_skill_used_count }



Claude.ai activity metrics for a single skill on a given day.

distinct_conversation_skill_used_count: number



Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.chat_metrics.distinct_conversation_skill_used_count)

[](#skill_usage.data.items.chat_metrics)



claude_code_metrics: object { distinct_session_skill_used_count }



Claude Code activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number



Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.claude_code_metrics.distinct_session_skill_used_count)

[](#skill_usage.data.items.claude_code_metrics)



cowork_metrics: object { distinct_session_skill_used_count }



Cowork activity metrics for a single skill on a given day.

distinct_session_skill_used_count: number



Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.cowork_metrics.distinct_session_skill_used_count)

[](#skill_usage.data.items.cowork_metrics)

distinct_user_count: number



Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

[](#skill_usage.data.items.distinct_user_count)



office_metrics: object { excel, outlook, powerpoint, word }



Office Agent activity metrics for a single skill on a given day, broken out by Office product.



excel: [SkillOfficeProductMetrics](/docs/en/api/admin/analytics#skill_office_product_metrics) { distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.office_metrics.excel%20%2B%20(resource)%20admin.analytics.distinct_session_skill_used_count)

[](#skill_usage.data.items.office_metrics.excel)



outlook: [SkillOfficeProductMetrics](/docs/en/api/admin/analytics#skill_office_product_metrics) { distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.office_metrics.outlook%20%2B%20(resource)%20admin.analytics.distinct_session_skill_used_count)

[](#skill_usage.data.items.office_metrics.outlook)



powerpoint: [SkillOfficeProductMetrics](/docs/en/api/admin/analytics#skill_office_product_metrics) { distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.office_metrics.powerpoint%20%2B%20(resource)%20admin.analytics.distinct_session_skill_used_count)

[](#skill_usage.data.items.office_metrics.powerpoint)



word: [SkillOfficeProductMetrics](/docs/en/api/admin/analytics#skill_office_product_metrics) { distinct_session_skill_used_count }



Office Agent activity metrics for a single skill on a given day within one Office product.

distinct_session_skill_used_count: number



Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error \<2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

[](#skill_usage.data.items.office_metrics.word%20%2B%20(resource)%20admin.analytics.distinct_session_skill_used_count)

[](#skill_usage.data.items.office_metrics.word)

[](#skill_usage.data.items.office_metrics)

skill_name: string



Name of the skill

[](#skill_usage.data.items.skill_name)

attributed_list_price: optional string



List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated_overage_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated_overage_spend (spend reporting not enabled for this organization, office_agent product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On group_by\[\] and filter\[\] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

[](#skill_usage.data.items.attributed_list_price)

currency: optional "USD"



Currency for this row's monetary fields (estimated_overage_spend and attributed_list_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

[](#skill_usage.data.items.currency)

enable_count: optional number



Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install_count). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to user_id / rbac_group_id / product via group_by\[\] or filter\[\] (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting_date/ending_date).

[](#skill_usage.data.items.enable_count)

estimated_overage_spend: optional string



Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is \$12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates \$0 here — see attributed_list_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (starting_date/ending_date) returns the window's sum. With group_by\[\]=user_id each row carries the user's own attributed spend. On group_by\[\] and filter\[\] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

[](#skill_usage.data.items.estimated_overage_spend)

invocation_count: optional number



Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation_count). Unlike distinct_user_count — which answers '# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting_date/ending_date) returns this sum directly.

[](#skill_usage.data.items.invocation_count)

product: optional string



Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by\[\] or filter\[\] there is rejected). Present only when the request grouped by product.

[](#skill_usage.data.items.product)

rbac_group_id: optional string



Tagged RBAC group identifier (rbac_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

[](#skill_usage.data.items.rbac_group_id)

rbac_group_name: optional string



Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

[](#skill_usage.data.items.rbac_group_name)

share_status: optional string



Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter\[\]=share_status:\<value\>.

[](#skill_usage.data.items.share_status)

skill_display_name: optional string



Human-readable display name for rows whose skill_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

[](#skill_usage.data.items.skill_display_name)

user_id: optional string



Tagged user identifier (e.g. user\_...). Present only when the request grouped by user_id.

[](#skill_usage.data.items.user_id)

[](#skill_usage.data)

next_page: string



Opaque cursor for the next page, or null if no more results

[](#skill_usage.next_page)
