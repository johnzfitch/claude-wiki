---
category: "22-Safety-Policy"
fetched_at: "2026-03-12T08:19:35Z"
source_url: "https://support.claude.com/en/articles/13694757-access-engagement-and-adoption-data-with-the-analytics-api"
title: "Access engagement and adoption data with the Analytics API | Claude Help Center"
---

4.  Access engagement and adoption data with the Analytics API

# Access engagement and adoption data with the Analytics API


The Analytics API gives Enterprise plan Primary Owners programmatic access to engagement and adoption data for their organization. Use it to build internal dashboards, track adoption trends, and feed Claude engagement data into your existing reporting tools.

The Analytics API is available on Enterprise plans. Primary Owners can generate API keys to get started.

## How is this different from the analytics dashboard and Compliance API?

All three options give you different views into your organization's data:

The **Analytics dashboard** (accessed via **[Analytics](https://claude.ai/analytics/activity)**) shows visualized usage data in the product. It's the right tool for day-to-day monitoring when you don't need to integrate data elsewhere.

The **Analytics API** returns the same aggregated usage and engagement metrics, but programmatically—so you can pull them into BI tools, map them against org charts, or automate reporting workflows. Data is aggregated per organization, per day.

The **Compliance API** is for governance and auditing use cases. It gives you access to individual user actions, raw activity events, and conversation content. If you need aggregated engagement metrics for dashboards, rather than raw events for auditing, use the Analytics API.

------------------------------------------------------------------------

## Get started

To access the Analytics API, you need Primary Owner access to your Enterprise organization.

Follow these steps:

1.  Navigate to **[Analytics \> API keys](http://claude.ai/analytics/api-keys)**.

2.  Find the **Access** toggle under **Analytics API** and toggle it on.

3.  Click “+ Create key” to generate a new API key. Keep this key private—treat it like a password.

4.  Use the key with the `x-api-key` header in your requests.


For full authentication details, endpoint references, and code examples, refer to our **[Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)**.

------------------------------------------------------------------------

## What data is available?

The Analytics API includes five endpoints. All data is aggregated per organization, per day, and is available for up to the past 90 days (not before January 1, 2026).

- **User activity**: Per-user engagement metrics including conversation counts, messages sent, projects created, files uploaded, artifacts created, skills used, connectors used, and Claude Code metrics like commits, pull requests, and lines of code.

- **Activity summary**: Organization-wide daily, weekly, and monthly active user counts, along with seat utilization and pending invite counts. Supports date ranges up to 31 days per request.

- **Chat project usage**: Conversation and user counts broken down by project, for Claude projects.

- **Skill usage**: How many users are using each skill, with breakdowns for Claude and Claude Code sessions separately.

- **Connector usage**: Which connectors your organization is using and how many unique users have used each one.

------------------------------------------------------------------------

## Data limits

All endpoints return data for a single date or date range. Data is only available after January 1, 2026, and for dates more than three days ago.

The API has a default rate limit of 60 requests per minute. If this doesn't meet your organization's needs, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.

**Important:** If you are using Claude Code via **[Amazon Bedrock](https://support.claude.com/en/collections/4078537-amazon-bedrock)**, the Analytics API will not return data related to Claude Code.

------------------------------------------------------------------------

Related Articles


What is the Enterprise plan?


Claude Console Roles and Permissions


Claude Code usage analytics


View usage analytics for Team and Enterprise plans


Claude Enterprise Analytics API reference guide
