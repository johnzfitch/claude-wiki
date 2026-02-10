---
category: "22-Safety-Policy"
fetched_at: "2026-02-08T20:52:10Z"
source_url: "https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console"
title: "Cost and Usage Reporting in the Claude Console | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_f554b1d100)

[](#h_0101a5f122)

[](#h_3092c9cbab)

[All Collections](/en/)

[Claude API and Console](https://support.claude.com/en/collections/5370014-claude-api-and-console)

[Using the Claude API and Console](https://support.claude.com/en/collections/9811457-using-the-claude-api-and-console)

Cost and Usage Reporting in the Claude Console

# Cost and Usage Reporting in the Claude Console

Updated yesterday

Table of contents

[](#h_f554b1d100)

[](#h_0101a5f122)

[](#h_3092c9cbab)

**Note:** Usage and Cost reporting is visible to the following user roles: **Developer, Billing, and Admin**. See [Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions) for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1770585300&signature=88fad8989e28fab2f61f46fd503eb709a55f007648e44ea5c68459b74ef3034c&req=dSUvEs97mYNeXvMW1HO4zYCWhiQdicOZuqqBX2puyxQcbJJyAflIBBMpdSn3%0AlhlhAG8qTTVOimLfeJo%3D%0A)

------------------------------------------------------------------------

## Usage Reporting

The [Usage page](https://platform.claude.com/usage) offers a detailed breakdown of your API usage across different models and API keys.

### Key Features

- **Detailed Breakdown**: View usage data by model, date/time, and API key. Click into the bars on the bar chart for hour and minute granularity.

- **Flexible Filtering**: Use selectors to choose specific models, months, or API keys

- **Visual Representation**: A chart with input and output token counts.

- **Usage Statistics**: See total input and output tokens for your selected filters.

- **Rate-Limited Requests:** Review your requests that were blocked due to hitting rate limits.

- **Rate Limit Use:** Visualizations of input and output tokens per minute compared with the overall ITPM or OTPM rate limit.

- **CSV Export**: Download your usage data for further analysis or reporting.

### How to Use

1.  Select the Workspace you want to view (or choose "All Workspaces").

2.  Select the model you want to view (or choose "All Models").

3.  Choose the month you're interested in (or narrow to a specific month/day).

4.  Select an API key (or view data for all keys).

5.  The chart and statistics will update based on your selections.

6.  Use the export button to download a CSV of the displayed data.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1770585300&signature=56cee06254b5c3aa0486b88955caa7507e5dda22734e882316499b7e30f195e9&req=dSUvEs94mYJdWPMW1HO4zQwESHMvKYplqMITUZbanFCHH8DVq%2BXCbBoR2emJ%0AtuWbtZV2Sj%2Fgm3%2FaXms%3D%0A)

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1770585300&signature=b1ea7ea5f55be883f8344c82e78cb674d6d39ca207b944bf2b7f021c0c5247de&req=dSUvEs93noJXX%2FMW1HO4zRxEzmtI7lRv21D6pckxWMZ9zFlVzNIMt1u47zgS%0A6DlWgu9QIPXIn6WnuVk%3D%0A)

### Rate Limit Use

The Usage page also includes a separate section displaying rate limit use per-model for input and output tokens. You can click the dropdown in the upper left corner of this section to change the model and view related rate limit metrics. These visualizations can be used to determine when you’re hitting peak use for your organization, which specific rate limits need to be increased, and how you can increase your caching rate.

**Rate Limit Use + Caching - Input Tokens:** This chart displays the hourly maximum number of uncached input tokens per minute (ITPM) alongside your cache rate (i.e. the percentage of input tokens read from the cache) and your current ITPM rate limit.

**Rate Limit Use - Output Tokens:** This chart displays the hourly maximum number of output tokens per minute (OTPM) alongside your current OTPM rate limit.

------------------------------------------------------------------------

## Cost Reporting

The [Cost page](https://platform.claude.com/cost) helps you understand your spending across different models.

### Key Features

- **Model-Specific Data**: View costs for individual models or all models combined.

- **Monthly Breakdown**: See costs for specific months.

- **Daily Cost Chart**: Visualize your spending over time.

- **Total Cost Statistics**: Get an overview of your total spending for the selected period, including web search and code execution costs.

- **CSV Export**: Download cost data for your records for further analysis.

### How to Use

1.  Choose the Workspace you want to view costs for (or select "All Workspaces").

2.  Choose the model you want to view costs for (or select "All Models").

3.  Select the month you're interested in.

4.  You can see the chart, token cost, and tool use costs, which will update based on your selections.

5.  Use the export button to download a CSV of the cost data.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1770585300&signature=c75a6d5672b8dbf902d5d534866a820e6ddb7188218d9ea27179524190736ca7&req=dSUvEs95lIVfWPMW1HO4zUR%2BiJzGW9ViCyIF5nuUsbzLeXb91PGXSJe4IaGP%0A%2FxQl4jP5erB7fJAXBNI%3D%0A)

**Note**: Currently, it's not possible to break down usage or cost by individual users.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api)

Our approach to rate limits for the Claude API

[](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)

Creating and managing Workspaces in the Claude Console

[](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)

Claude Console Roles and Permissions

[](https://support.claude.com/en/articles/12386420-claude-code-faq)

Claude Code FAQ

[](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)

Extra usage for paid Claude plans

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
