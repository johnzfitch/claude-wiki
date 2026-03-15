---
category: "17-Billing-Plans"
fetched_at: "2026-03-15T12:17:10Z"
source_url: "https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans"
title: "View usage analytics for Team and Enterprise plans | Claude Help Center"
---

4.  View usage analytics for Team and Enterprise plans

# View usage analytics for Team and Enterprise plans

Updated yesterday


This article explains how to view and export usage analytics for your organization.

Usage analytics are available to Team plan Owners and Primary Owners, and Enterprise plan Owners, Primary Owners, and Admins. Enterprise Admins can view all analytics except Spend.

Usage analytics help you track team activity, feature adoption, and spend directly from your admin dashboard. You can monitor how your organization uses Claude and export detailed reports for your own analysis.

Primary Owners and Owners can access analytics via dedicated Analytics settings by clicking your initials in the lower left corner and selecting **[Analytics](https://claude.ai/analytics/activity)** from the menu. Additionally, the "Claude.ai" and "Claude Code" options offer product-specific analytics.

------------------------------------------------------------------------

## All activity

This page includes the following analytics:

## Usage

- Weekly active users (WAU)

- Utilization rates (WAU / total seats)

- Pending invites

- Daily, weekly, and monthly active users

- Top connectors


## Spend

**Note:** If you're on a **[seat-based Enterprise plan](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans#h_6a78e30e26)**, spend reports only appear if your organization has **[enabled extra usage](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans#h_2b9c54b46d)**. The spend data covers overage spend only—usage within seat-based allotments isn't included.

This section includes the following analytics:

- Total spend (month-to-date, quarter-to-date, year-to-date)

- Spend by model (1 month, 3 months, 1 year)

- Top 10 users by spend leaderboard


**Note:** The spend leaderboard can be delayed by one to two days. For more current month-to-date spend per user, refer to spend limits by person in **[Organization settings \> Usage](https://claude.ai/admin-settings/usage)**.

## Export a spend report

You can export a detailed cost and usage report as a CSV file. The report provides per-user, per-model visibility into token usage and estimated spend, updated daily.

To export spend data:

1.  Navigate to **[Settings \> Analytics](https://claude.ai/analytics/activity)**.

2.  Scroll down to the **Spend** section.

3.  Click the "Export Spend Report" button.

4.  Select a time period: MTD, Last Month, Last 90 Days, or Custom.

5.  If you select "Custom," choose your start and end dates. You can go back up to 90 days, and the most recent data available is from yesterday.

6.  Click "Download."

### What's included in the report?

Each row in the CSV represents a specific person's usage of a specific model on a given day. The report includes the following fields:

- Date

- Organization UUID

- User's email

- Account UUID

- Product (such as Chat, Claude Code, or Cowork)

- Model and model family

- Request count

- Prompt tokens

- Completion tokens (includes extended thinking tokens)

- Net spend (USD) — reflects any org-level discount

- Gross spend (USD) — based on standard pricing

**Important:** Spend data refreshes daily and has a one-day delay. For usage-based Enterprise plans, the export captures your organization's full usage. For seat-based Enterprise plans with extra usage enabled, the export only reflects spend that exceeds your seat allotment.

------------------------------------------------------------------------

## Claude.ai

Navigate to **[Analytics \> Claude.ai](https://claude.ai/analytics/usage)** to view usage and activity metrics for your organization. This page includes the following analytics:

## Chats

- Chats per day

- Percentage of users with 1 or more chat

- Total number of chats (1 week, 1 month, 3 months, 1 year)


## Projects

- Projects created per day

- Percentage of users with 1 or more project

- Top 10 users by projects used (month-to-date, quarter-to-date, year-to-date, 1 year)


## Artifacts

- Artifacts created per day

- Percentage of users with 1 or more artifact

- Top 10 users by artifacts generated (month-to-date, quarter-to-date, year-to-date, 1 year)


------------------------------------------------------------------------

## Claude Code analytics

Navigate to **[Analytics \> Claude Code](https://claude.ai/analytics/claude-code)** to view usage and activity metrics for your organization. For more specific details, refer to **[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)**.

------------------------------------------------------------------------

## Access your analytics data programmatically

If you’re on an Enterprise plan and want to pull analytics data into your own dashboards or reporting tools, the Analytics API gives you programmatic access to the same usage and engagement metrics available in the analytics dashboard. To get started, refer to **[Access usage data with the Analytics API](https://support.claude.com/en/articles/13694757-access-usage-data-with-the-analytics-api)**.

------------------------------------------------------------------------

Related Articles


What is the Enterprise plan?


How am I billed for my Enterprise plan?


Manage extra usage for Team and seat-based Enterprise plans


Claude Code usage analytics


Purchase and manage seats on Enterprise plans
