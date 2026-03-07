---
category: "17-Billing-Plans"
fetched_at: "2026-03-07T01:05:37Z"
source_url: "https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans"
title: "Usage analytics for Team and Enterprise plans | Claude Help Center"
---

4.  Usage analytics for Team and Enterprise plans

# Usage analytics for Team and Enterprise plans

Updated today


This article explains how to view and export usage analytics for your organization.

Usage analytics are available to Team plan Owners and Primary Owners, and Enterprise plan Owners, Primary Owners, and Admins. Enterprise Admins can view all analytics except Spend.

Usage analytics help you track team activity, feature adoption, and spend directly from your admin dashboard. You can monitor how your organization uses Claude and export detailed reports for your own analysis.

Primary Owners and Owners can access analytics via dedicated Analytics settings by clicking your initials in the lower left corner and selecting **[Analytics](https://claude.ai/analytics/activity)** from the menu. Additionally, the "Claude.ai" and "Claude Code" options offer product-specific analytics.

## All activity

This page includes the following analytics:

### Usage

- Weekly active users (WAU)

- Utilization rates (WAU / total seats)

- Pending invites


### Feature adoption

- Total chats per day (with day over day change)

- Average number of messages per chat (with day over day change)

- Projects created and users with at least one or more projects created (with day over day change)

- Artifacts created and users with at least one or more artifacts created (with day over day change)

- Top 10 users by projects used

- Top 10 users by artifacts generated

- Top connectors and number of unique users leveraging each connector


### Spend

**Note:** If you're on a **[seat-based Enterprise plan](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans#h_6a78e30e26)**, spend reports will only appear if your organization has **[enabled extra usage](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans#h_2b9c54b46d)**.

- Total spend (month-to-date, quarter-to-date, year-to-date)

- Spend by model (1 month, 3 months, 1 year)

- Top 10 users by spend leaderboard


**Note:** The Leaderboard pictured below can be delayed by 1-2 days. For more current month-to-date spend per user, refer to **Spending caps by user** in **[Organization settings \> Usage](https://claude.ai/admin-settings/usage)**.


**How to export user-level spend data:**

You can export user-level spend as a CSV file for your own reporting by following these steps:

1.  Navigate to **[Settings \> Analytics](https://claude.ai/analytics/activity)**.

2.  Scroll down to the **Spend** section.

3.  Locate the "Export Spend Report" option:


4.  Select the data you want to export.

5.  Download the CSV file.

## Claude.ai

Navigate to **[Analytics \> Claude.ai](https://claude.ai/analytics/usage)** to view usage and activity metrics for your organization. This page includes the following analytics:

### Chats

- Chats per day

- Percentage of users with 1 or more chat

- Total number of chats (1 week, 1 month, 3 months, 1 year)


### Projects

- Projects created per day

- Percentage of users with 1 or more project

- Top 10 users by projects used (month-to-date, quarter-to-date, year-to-date, 1 year)


### Artifacts

- Artifacts created per day

- Percentage of users with 1 or more artifact

- Top 10 users by artifacts generated (month-to-date, quarter-to-date, year-to-date, 1 year)


## Claude Code analytics

Navigate to **[Analytics \> Claude Code](https://claude.ai/analytics/claude-code)** to view usage and activity metrics for your organization. For more specific details, refer to **[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)**.

## Access your analytics data programmatically

If you’re on an Enterprise plan and want to pull analytics data into your own dashboards or reporting tools, the Analytics API gives you programmatic access to the same usage and engagement metrics available in the analytics dashboard. See **[Access usage data with the Analytics API](https://support.claude.com/en/articles/13694757-access-usage-data-with-the-analytics-api)** to get started.

------------------------------------------------------------------------

Related Articles


Extra usage for Team and seat-based Enterprise plans


Claude Code usage analytics


Extra usage for paid Claude plans


Access engagement and adoption data with the Analytics API


Claude Enterprise Analytics API reference guide
