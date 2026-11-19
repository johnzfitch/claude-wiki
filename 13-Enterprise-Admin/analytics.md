---
title: "Track team usage with analytics - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/analytics"
category: "13-Enterprise-Admin"
fetched_at: "2026-11-17T06:24:45Z"
last_modified: "Tue, 17 Nov 2026 03:14:04 GMT"
tags: ["api", "claude-code", "enterprise"]
---

## On this page

Back to top

- [Access analytics for Team and Enterprise](#access-analytics-for-team-and-enterprise)
  - [Enable contribution metrics](#enable-contribution-metrics)
  - [Review summary metrics](#review-summary-metrics)
  - [Explore the charts](#explore-the-charts)
  - [Measure PRs per user](#measure-prs-per-user)
  - [View pull requests breakdown](#view-pull-requests-breakdown)
  - [Find top contributors](#find-top-contributors)
  - [PR attribution](#pr-attribution)
  - [Attribution process](#attribution-process)
  - [Time window](#time-window)
  - [Excluded files](#excluded-files)
  - [Attribution notes](#attribution-notes)
  - [Get the most from analytics](#get-the-most-from-analytics)
  - [Monitor adoption](#monitor-adoption)
  - [Measure ROI](#measure-roi)
  - [Identify power users](#identify-power-users)
  - [Access data programmatically](#access-data-programmatically)
- [Access analytics for API customers](#access-analytics-for-api-customers)
  - [View team insights](#view-team-insights)
- [Related resources](#related-resources)

Usage and costs

# Track team usage with analytics

Copy pageCopy page

View Claude Code usage metrics, track adoption, and measure engineering velocity in the analytics dashboard.

Copy pageCopy page

Claude Code provides analytics dashboards to help organizations understand developer usage patterns, track contribution metrics, and measure how Claude Code impacts engineering velocity. Access the dashboard for your plan:

| Plan | Dashboard URL | Includes | Read more |
|----|----|----|----|
| Claude for Teams / Enterprise | [claude.ai/analytics/claude-code](https://claude.ai/analytics/claude-code) | Usage metrics, contribution metrics with GitHub integration, leaderboard, data export | [Details](#access-analytics-for-team-and-enterprise) |
| API (Claude Console) | [platform.claude.com/claude-code](../04-API-Reference/Other/playground.md) | Usage metrics, spend tracking, team insights | [Details](#access-analytics-for-api-customers) |

Code Review has its own dashboard. For review activity and spend, see [View usage](../02-Claude-Code-CLI/code-review-costs.md#view-usage).

## [](#access-analytics-for-team-and-enterprise)Access analytics for Team and Enterprise

Navigate to [claude.ai/analytics/claude-code](https://claude.ai/analytics/claude-code). Admins and Owners can view the dashboard. The Team and Enterprise dashboard includes:

- **Usage metrics**: lines of code accepted, suggestion accept rate, daily active users and sessions
- **Contribution metrics**: PRs and lines of code shipped with Claude Code assistance, with [GitHub integration](#enable-contribution-metrics)
- **Leaderboard**: top contributors ranked by Claude Code usage
- **Data export**: download contribution data as CSV for custom reporting

For per-user token counts and cost estimates, configure [OpenTelemetry export](monitoring-usage.md), or export the [spend report](../17-Billing-Plans/view-usage-analytics-for-team-and-enterprise-plans.md) from your organization’s analytics settings, which lists token usage and estimated usage-credit spend per user and per model.

### [](#enable-contribution-metrics)Enable contribution metrics

Contribution metrics are in public beta and available on Claude for Teams and Claude for Enterprise plans. These metrics only cover users within your claude.ai organization. Usage through the Claude Console API or third-party integrations is not included.

Usage and adoption data is available for all Claude for Teams and Claude for Enterprise accounts. Contribution metrics require additional setup to connect your GitHub organization. You need the Owner role to configure analytics settings. A GitHub admin must install the GitHub app.

Contribution metrics are not available for organizations with [Zero Data Retention](../02-Claude-Code-CLI/zero-data-retention.md) enabled. The analytics dashboard will show usage metrics only.

1

Install the GitHub app

A GitHub admin installs the Claude GitHub app on your organization’s GitHub account at [github.com/apps/claude](https://github.com/apps/claude).

2

Enable Claude Code analytics

A Claude Owner navigates to [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code) and enables the Claude Code analytics feature.

3

Enable GitHub analytics

On the same page, enable the “GitHub analytics” toggle.

4

Authenticate with GitHub

Complete the GitHub authentication flow and select which GitHub organizations to include in the analysis.

Data typically appears within 24 hours after enabling, with daily updates. If no data appears, you may see one of these messages:

- **“GitHub app required”**: install the GitHub app to view contribution metrics
- **“Data processing in progress”**: check back in a few days and confirm the GitHub app is installed if data doesn’t appear

Contribution metrics cover repositories hosted on github.com. For repositories on [GitHub Enterprise Server](../02-Claude-Code-CLI/github-enterprise-server.md), the analytics dashboard shows usage metrics only.

### [](#review-summary-metrics)Review summary metrics

These metrics are deliberately conservative and represent an underestimate of Claude Code’s actual impact. Only lines and PRs where there is high confidence in Claude Code’s involvement are counted.

The dashboard displays these summary metrics:

- **PRs with Claude Code**: merged pull requests that contain at least one line of code written with Claude Code. One card shows the count, and one shows the share of all merged PRs
- **LOC with Claude Code**: total lines of code (LOC) across all merged PRs that were written with Claude Code assistance. Only “effective lines” are counted: lines with more than 3 characters after normalization.
- **Suggestion accept rate**: percentage of times users accept Claude Code’s code editing suggestions, including Edit, Write, and NotebookEdit tool usage
- **Lines of code accepted**: total lines of code that Claude Code’s Edit and Write tools added or removed in accepted edits. This excludes rejected suggestions, and lines deleted later don’t reduce the total.

### [](#explore-the-charts)Explore the charts

The dashboard includes several charts to visualize trends over time.

#### [](#measure-prs-per-user)Measure PRs per user

**Total PRs per user** is the number of PRs merged per day divided by daily active users. Use this to understand how individual productivity changes as Claude Code adoption increases.

#### [](#view-pull-requests-breakdown)View pull requests breakdown

The **PRs with Claude Code** chart compares each day’s merged PRs with Claude Code to **All PRs**. Toggle to **Lines of code** view to see the same breakdown by lines of code rather than PR count.

#### [](#find-top-contributors)Find top contributors

The Leaderboard shows the top 10 users ranked by contribution volume. Toggle between:

- **Pull requests**: shows PRs with Claude Code vs All PRs for each user
- **Lines of code**: shows lines with Claude Code vs All lines for each user

Click **Export all users** to download complete contribution data for all users as a CSV file. The export includes all users, not just the top 10 displayed.

### [](#pr-attribution)PR attribution

When contribution metrics are enabled, Claude Code analyzes merged pull requests to determine which code was written with Claude Code assistance. This is done by matching Claude Code session activity against the code in each PR.

#### [](#attribution-process)Attribution process

When a pull request is merged:

1.  Added lines are extracted from the PR diff
2.  Claude Code sessions that edited matching files within a time window are identified
3.  PR lines are matched against Claude Code output using multiple strategies
4.  Metrics are calculated for AI-assisted lines and total lines

Before comparison, lines are normalized: whitespace is trimmed, multiple spaces are collapsed, quotes are standardized, and text is converted to lowercase. Merged pull requests containing Claude Code-assisted lines are labeled as `claude-code-assisted` in GitHub.

#### [](#time-window)Time window

Sessions from 21 days before to 2 days after the PR merge date are considered for attribution matching.

#### [](#excluded-files)Excluded files

Certain files are automatically excluded from analysis because they are auto-generated:

- Lock files: package-lock.json, yarn.lock, Cargo.lock, and similar
- Generated code: Protobuf outputs, build artifacts, minified files
- Build directories: dist/, build/, node_modules/, target/
- Test fixtures: snapshots, cassettes, mock data
- Lines over 1,000 characters, which are likely minified or generated

#### [](#attribution-notes)Attribution notes

Keep these additional details in mind when interpreting attribution data:

- Code substantially rewritten by developers, with more than 20% difference, is not attributed to Claude Code
- Sessions outside the 21-day window are not considered
- The algorithm does not consider the PR source or destination branch when performing attribution

### [](#get-the-most-from-analytics)Get the most from analytics

Use contribution metrics to demonstrate ROI, identify adoption patterns, and find team members who can help others get started.

#### [](#monitor-adoption)Monitor adoption

Track the **Users** and **Sessions** charts to identify:

- Active users who can share best practices
- Overall adoption trends across your organization
- Dips in usage that may indicate friction or issues

#### [](#measure-roi)Measure ROI

Contribution metrics help answer “Is this tool worth the investment?” with data from your own codebase:

- Track changes in PRs per user over time as adoption increases
- Compare PRs and lines of code shipped with Claude Code to all PRs and lines of code
- Use alongside [DORA metrics](https://dora.dev/), sprint velocity, or other engineering KPIs to understand changes from adopting Claude Code

#### [](#identify-power-users)Identify power users

The Leaderboard helps you find team members with high Claude Code adoption who can:

- Share prompting techniques and workflows with the team
- Provide feedback on what’s working well
- Help onboard new users

#### [](#access-data-programmatically)Access data programmatically

On the Enterprise plan, the [Claude Enterprise Analytics API](../04-API-Reference/Admin/platform-claude-com-http-beta-organization-analytics.md) returns per-user engagement, usage, and cost reports for your organization across Claude surfaces, including Claude Code. A Primary Owner creates a key with the `read:analytics` scope at [claude.ai/analytics/api-keys](https://claude.ai/analytics/api-keys). The API is not available on the Teams plan. To query contribution data through GitHub instead, search for PRs labeled with `claude-code-assisted`.

## [](#access-analytics-for-api-customers)Access analytics for API customers

API customers using the Claude Console can access analytics at [platform.claude.com/claude-code](../04-API-Reference/Other/playground.md). You need the UsageView permission to access the dashboard. The Developer, Billing, Admin, Owner, and Primary Owner roles have this permission. To pull daily per-user metrics programmatically, use the [Claude Code Analytics API](../04-API-Reference/Guides/build-with-claude-claude-code-analytics-api.md) with an Admin API key.

Contribution metrics with GitHub integration are not currently available for API customers. The Console dashboard shows usage and spend metrics only.

The Console dashboard displays:

- **Lines of code accepted**: total lines of code that Claude Code’s Edit and Write tools added or removed in accepted edits. This excludes rejected suggestions, and lines deleted later don’t reduce the total.
- **Suggestion accept rate**: percentage of times users accept code editing tool usage, including Edit, Write, and NotebookEdit tools.
- **Active users** and **Sessions**: daily counts of active users and Claude Code sessions.
- **Spend**: daily API costs in dollars.

### [](#view-team-insights)View team insights

The team insights table shows these per-user columns for the date range you select at the top of the dashboard, by default the last 30 days:

- **Members**: users and API keys with reported Claude Code usage in that range. API key users display by key name, and OAuth users by email address.
- **Spend**: per-user total API costs.
- **Lines accepted**: per-user total of lines that the Edit and Write tools added or removed in accepted edits.

Spend figures in the Console dashboard are estimates for analytics purposes. For actual costs, refer to the [Cost page](../04-API-Reference/Other/playground.md).

## [](#related-resources)Related resources

- [Monitoring with OpenTelemetry](monitoring-usage.md): export real-time metrics and events to your observability stack
- [Manage costs effectively](../17-Billing-Plans/costs.md): set spend limits and optimize token usage
- [Permissions](../02-Claude-Code-CLI/permissions.md): configure roles and permissions
