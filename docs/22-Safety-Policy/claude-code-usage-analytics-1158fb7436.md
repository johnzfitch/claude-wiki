---
category: "22-Safety-Policy"
source_url: "https://support.claude.com/en/articles/12157520-claude-code-usage-analytics"
---


This feature allows Console users and owners of Team and Enterprise plans to monitor how their organization uses Claude Code, tracking productivity metrics and adoption patterns across teams.

Claude Code usage analytics are available to:

Team plans: Owners and Primary Owners

Enterprise plans: Owners, Primary Owners, and Admins (requires a Chat + Claude Code seat for usage-based plans or Premium seat for seat-based plans)

API Console: Admin, Billing, and Developer roles

 

Accessing Claude Code analytics
Team and Enterprise plans

Log in to your Owner or Primary Owner account.

Click your initials or name in the lower left corner.

Navigate to Analytics > Claude Code to view Usage.

 

API Console users

Log in to your Claude Console account.

Expand the left side panel.

Click “Claude Code” under Analytics.

View Claude Code usage analytics on Settings > Claude Code.

 

 

Available metrics

The Claude Code Usage page displays the following metrics for your organization:

 

Organization-level metrics

Lines of code accepted: Total lines of code your team has accepted from Claude Code suggestions.

Suggestion accept rate: Percentage of Claude Code suggestions that your team accepts.

Activity trends: Daily view of active users and sessions over time.

Lines accepted over time: Daily breakdown of accepted code lines.

 

 

User-level metrics

Individual usage: View each team member's email address and their total lines of code accepted for the current month. You can search for specific users or click the “Export” button to generate a CSV of members’ email addresses and total lines of code.

 

Understanding the metrics

Lines of code accepted measures the actual code your team incorporates into their work from Claude Code suggestions, helping you understand the tool's practical impact on development productivity.

 

Suggestion accept rate indicates how relevant and useful Claude Code's suggestions are for your team's specific coding needs and practices.

 

Activity trends show adoption patterns and help identify peak usage periods, allowing you to understand how Claude Code fits into your team's workflow.

 

 

Contribution metrics (beta)

Contribution metrics are a new feature in public beta that helps Team and Enterprise organizations measure how Claude Code affects engineering velocity. By connecting to your organization's GitHub account, these metrics track code shipping activity with and without Claude Code, so you can see where it's making a difference.

Contribution metrics require GitHub Cloud and are not available to Console users at this time.

For a more in-depth look at contribution metrics, see our Claude Code docs.

 

Setting up contribution metrics

Contribution metrics require a few steps beyond the base analytics setup:

Install the Claude GitHub App on your organization's GitHub account.

Log in with an Owner or Primary Owner account.

Navigate to Admin settings > Claude Code.

Enable the Claude Code analytics feature if you haven't already.

Toggle on GitHub analytics.

Select the GitHub organization(s) you want included in the comparison.

After setup, metrics begin populating automatically. Allow up to 24 hours for data to appear. The dashboard currently processes data once daily.

 

If you see "GitHub app required. Install the GitHub app to view analytics," the GitHub App hasn't been installed yet. If the app is authenticated but no data appears, confirm the GitHub App is installed and that your team has started using Claude Code.

 

Available contribution metrics

Once enabled, the following metrics appear in your Claude Code analytics dashboard:

Pull requests merged: Total PRs merged with and without Claude Code assistance, at both the organization and user level.

Lines of code committed: Total lines committed with and without Claude Code assistance, at both the organization and user level.

Pull requests opened per user: Individual PR activity across your team.

Data is collected by correlating Claude Code session activity with GitHub commits and pull requests.

 

 

Data reset and availability

Usage metrics display data for the current calendar month and reset at the beginning of each month. Historical data visualization shows daily granularity for tracking trends over time.

 

Using analytics to optimize Claude Code adoption

Review your organization's code acceptance rate to understand if teams are finding Claude Code's suggestions valuable. If rates are lower than expected, consider providing additional training on effective prompting techniques.

 

Monitor individual usage patterns to identify power users who can share best practices with the broader team, or to spot team members who might benefit from additional support.

 

Track activity trends to understand when your team uses Claude Code most effectively and ensure adequate seat allocation during peak periods.

 

 

Frequently asked questions
I'm using an individual paid plan; how can I access usage analytics for Claude Code?

Claude Code usage analytics are not available to individual Pro or Max plans at this time.

 

I'm looking for specific user but they're missing from the reports.

If you notice that a specific user isn't showing up in your analytics, you should have them update Claude Code to the most recent version. The first Claude Code version to support this feature is version 2.0.28, so users should run claude update to manually update Claude Code if needed.

 

Where can I find more information?

See Analytics in our Claude Code docs for more information.

Related Articles
Using Claude Code with your Team or Enterprise plan
Automated Security Reviews in Claude Code
Claude Code FAQ
Claude Code on the web
Usage Analytics for Team and Enterprise Plans