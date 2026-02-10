---
category: "22-Safety-Policy"
source_url: "https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console"
---


Note: Usage and Cost reporting is visible to the following user roles: Developer, Billing, and Admin. See Claude Console Roles and Permissions for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

 

Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

 

 

 

Usage Reporting

The Usage page offers a detailed breakdown of your API usage across different models and API keys.

 

Key Features

Detailed Breakdown: View usage data by model, date/time, and API key. Click into the bars on the bar chart for hour and minute granularity.

Flexible Filtering: Use selectors to choose specific models, months, or API keys

Visual Representation: A chart with input and output token counts.

Usage Statistics: See total input and output tokens for your selected filters.

Rate-Limited Requests: Review your requests that were blocked due to hitting rate limits.

Rate Limit Use: Visualizations of input and output tokens per minute compared with the overall ITPM or OTPM rate limit. 

CSV Export: Download your usage data for further analysis or reporting.

How to Use

Select the Workspace you want to view (or choose "All Workspaces").

Select the model you want to view (or choose "All Models").

Choose the month you're interested in (or narrow to a specific month/day).

Select an API key (or view data for all keys).

The chart and statistics will update based on your selections.

Use the export button to download a CSV of the displayed data.

 

 

Rate Limit Use

The Usage page also includes a separate section displaying rate limit use per-model for input and output tokens. You can click the dropdown in the upper left corner of this section to change the model and view related rate limit metrics. These visualizations can be used to determine when you’re hitting peak use for your organization, which specific rate limits need to be increased, and how you can increase your caching rate.

 

Rate Limit Use + Caching - Input Tokens: This chart displays the hourly maximum number of uncached input tokens per minute (ITPM) alongside your cache rate (i.e. the percentage of input tokens read from the cache) and your current ITPM rate limit. 

 

Rate Limit Use - Output Tokens: This chart displays the hourly maximum number of output tokens per minute (OTPM) alongside your current OTPM rate limit.

 

 

Cost Reporting

The Cost page helps you understand your spending across different models.

 

Key Features

Model-Specific Data: View costs for individual models or all models combined.

Monthly Breakdown: See costs for specific months.

Daily Cost Chart: Visualize your spending over time.

Total Cost Statistics: Get an overview of your total spending for the selected period, including web search and code execution costs.

CSV Export: Download cost data for your records for further analysis.

How to Use

Choose the Workspace you want to view costs for (or select "All Workspaces").

Choose the model you want to view costs for (or select "All Models").

Select the month you're interested in.

You can see the chart, token cost, and tool use costs, which will update based on your selections.

Use the export button to download a CSV of the cost data.

 

Note: Currently, it's not possible to break down usage or cost by individual users. 

Related Articles
Our approach to rate limits for the Claude API
Creating and managing Workspaces in the Claude Console
Claude Console Roles and Permissions
Claude Code FAQ
Extra usage for paid Claude plans