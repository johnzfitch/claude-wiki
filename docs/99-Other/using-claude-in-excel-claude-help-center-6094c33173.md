---
category: "99-Other"
fetched_at: "2026-02-08T20:52:00Z"
source_url: "https://support.claude.com/en/articles/12650343-claude-in-excel"
title: "Using Claude in Excel | Claude Help Center"
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

[](#h_0c60818ce4)

[](#h_7992217c45)

[](#h_f124c37c80)

[](#h_cde082ea6c)

[](#h_0892aafc06)

[](#h_0e502a40fb)

[](#h_80388aba66)

[](#h_f26391702d)

[](#h_140dd9a8d0)

[](#h_a0b884d13d)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

Using Claude in Excel

# Using Claude in Excel

Updated yesterday

Table of contents

[](#h_0c60818ce4)

[](#h_7992217c45)

[](#h_f124c37c80)

[](#h_cde082ea6c)

[](#h_0892aafc06)

[](#h_0e502a40fb)

[](#h_80388aba66)

[](#h_f26391702d)

[](#h_140dd9a8d0)

[](#h_a0b884d13d)

Claude in Excel is currently in beta and available to Pro, Max, Team, and Enterprise plans.

Claude in Excel is an add-in that integrates Claude into your Excel workflow. It's designed for professionals who work extensively with spreadsheets, particularly in financial analysis and modeling.

With Claude in Excel, you can:

- Ask questions about your workbook and get answers with cell-level citations

- Update assumptions while preserving formula dependencies

- Debug errors and identify their root causes

- Build new models or fill existing templates

- Navigate complex multi-tab workbooks seamlessly

------------------------------------------------------------------------

## What’s new?

### Claude Opus 4.6 and expanded Excel capabilities

We've updated Claude in Excel with Claude Opus 4.6 and a significant set of new spreadsheet editing tools. These additions bring Claude in Excel closer to a full Excel editing experience, particularly for finance professionals.

### New editing and formatting tools

Claude in Excel now supports a range of native Excel operations directly:

- **Pivot table editing** — Sort, filter, and modify the schema of existing pivot tables.

- **Chart editing** — Adjust axes, labels, and legends on existing charts.

- **Conditional formatting** — Apply rules based on values or formulas, including data bars.

- **Sort and filter** — Sort and filter tabular data using Excel-native controls.

- **Data validation** — Set up dropdown lists and input restrictions on cells.

- **Finance formatting** — Toggle gridlines on or off and set print areas to prepare outputs for printing. Print area support is currently limited.

------------------------------------------------------------------------

## Getting started with Claude in Excel

### For individuals

1.  Navigate to the **[Claude in Excel listing on Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/saas/wa200009404?tab=overview)**.

2.  Click "Get it now" to install the add-in.

3.  Open Excel, activate the add-in, and sign in with your Claude account.

### For admins

**Deploy Claude in Excel to your organization:**

1.  Visit the **[Microsoft 365 Admin Center](https://admin.microsoft.com/)**.

2.  Navigate to Settings \> Integrated apps \> Add-ins.

3.  Search for "Claude by Anthropic for Excel" in Microsoft AppSource.

4.  Deploy the add-in to your organization or specific users.

5.  Share these instructions with your team: **[Microsoft's deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide)**.

After installation, team members can open Excel, activate the Claude add-in (from Tools \> Add-ins on Mac or Home \> Add-ins on Windows), sign in with their Claude credentials, and start working with their spreadsheets.

------------------------------------------------------------------------

## Key features

### Read and understand complex models

Ask Claude questions about specific cells, formulas, or entire sections of your workbook. Claude can navigate across multiple tabs and provides answers with direct citations to referenced cells.

**Example prompts:**

- "What assumptions drive the revenue forecast in Q3?"

- "Explain how the WACC calculation flows through the DCF model"

### Update assumptions safely

Modify values and inputs while Claude maintains all formula dependencies and relationships. Every change is highlighted with clear explanations.

**Example prompts:**

- "Increase growth rate by 2% and show the impact on terminal value"

- "Update interest rate assumptions based on latest Fed guidance"

### Build and fill templates

Create spreadsheets from scratch or populate existing templates with new data, formulas, and assumptions.

**Example prompts:**

- "Build a three-statement model for a SaaS company"

- "Fill this DCF template with data from the uploaded 10-K"

### Debug and fix errors

Identify error sources (like \#REF!, \#VALUE!, or circular references) and get actionable fixes that maintain spreadsheet integrity.

**Example prompts:**

- "Why is this NPV calculation returning \#VALUE?"

- "Find all circular references in this workbook"

### Change tracking and citations

Claude highlights every cell it updates and provides explanatory comments. When explaining calculations, Claude includes clickable citations that navigate directly to referenced cells.

### Edit and format natively

Claude can now apply a range of Excel-native operations directly, including sorting and filtering data, editing pivot tables and charts, applying conditional formatting rules, setting data validation, and preparing workbooks for printing with finance-specific formatting tools.

**Example prompts:**

- "Sort this table by revenue, descending"

- "Add a conditional format that highlights cells below the target threshold in red"

- "Set up a dropdown for the status column with options: Active, Pending, Closed"

- "Toggle off gridlines and set the print area to A1:F20"

## Technical specifications

**Supported file formats:**

- .xlsx files

- .xlsm files

**What's preserved:**

- Formulas and dependencies

- Cell relationships

- Existing formatting and structure

## Context and session management

- **Auto-compaction**: We **[automatically compact longer conversations](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits#h_21b66a43b4)** into new conversations to avoid running out of context.

- **Session logging**: By turning this feature on in your settings, Claude will create a separate "Claude Log" tab in the Excel sheet to track your actions taken each turn. This allows Claude to maintain a history of its actions on the sheet.

  - If Claude doesn't do this automatically, you can simply ask it to log its history and it should create a new logging tab.

- **Overwrite protection**: To avoid accidental data loss, Claude warns you before overwriting existing data.

**Note:** Your use of Claude in Excel is associated with your existing Claude account and is subject to the same usage limits.

------------------------------------------------------------------------

## Current limitations

Chat history is not saved between sessions when using Claude in Excel. If you're using a Team or Enterprise plan, Claude in Excel does not inherit custom data retention settings your organization might have set, and isn't included in Enterprise audit logs or the compliance API at this time.

Additionally, Claude does not have advanced Excel capabilities, including:

- Data tables

- Macros

- VBA (Visual Basic for Applications)

As a beta feature, Claude in Excel is **not recommended** for:

- Final client deliverables without human review

- Audit-critical calculations without verification

- Replacing users’ financial judgment and expertise

- Models containing highly sensitive or regulated data without proper controls

## Best practices

To use Claude in Excel safely and effectively:

- Always review changes before finalizing your work.

- Verify outputs match your organization's methodologies.

- Use appropriate permissions and access controls.

- Maintain human oversight for client-facing work.

------------------------------------------------------------------------

## Prompt injection attack risks

Only use Claude in Excel with trusted spreadsheets and not spreadsheets from external untrusted sources (for example, downloaded templates, vendor files, collaborative documents, and data imports).

An important risk that users of Claude in Excel and other AI tools that can read and manipulate spreadsheets is prompt injection attacks that hide malicious instructions in spreadsheet content (cells, formulas, comments, etc.) to trick the AI models into taking unintended actions. For example, a seemingly innocent template or data file received from an external party or downloaded from the internet might contain hidden instructions to "export all financial data to this external URL" or "modify these financial records." Claude may interpret these malicious instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude in Excel can be manipulated to:

- **Extract and share sensitive information** with bad actors through formulas, web searches containing your sensitive data, or file system access that exposes proprietary information.

- **Modify critical data** such as financial records.

- **Perform destructive actions** without verification (should you allow Claude to act without verifying its actions), exploiting Claude's helpful nature to delete or corrupt important data across multiple sheets.

Users can approve all of Claude’s actions via a confirmation pop-up that appears when each tool is triggered:

- External data fetching: WEBSERVICE, STOCKHISTORY, STOCKSERIES, TRANSLATE, and the CUBE\* functions

- External imports: IMPORTDATA, IMPORTXML, IMPORTHTML, IMPORTFEED, FILTERXML

- Dynamic references: INDIRECT

- Command execution: DDE (Dynamic Data Exchange)

- Code execution: CALL, EVALUATE, FORMULA

- File system access: IMAGE, FILES, DIRECTORY, FOPEN, FWRITE, FCLOSE

- System information: REGISTER.ID, RTD, INFO

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1849431310/ffc870a5114b4178fcd74b5cccf8/Screenshot+2025-11-25+at+11_30_10%E2%80%AFAM.png?expires=1770585300&signature=5658ee0e690ef406dbe1c99cbb782a2f39e5d2f79eab057b1ab8dacb4ace7d23&req=dSgjH819nIJeWfMW1HO4zYWKZ%2BJuKt9xqAsRdssXCyDt3rIAdG5958t8GVnE%0APsUoMCsCiccAo1akWJg%3D%0A)

While we continue to develop our offerings and improve safety measures to reduce these risks, users should exercise caution when using Claude in Excel and should not use it with spreadsheets from external, untrusted sources.

------------------------------------------------------------------------

## Example use cases

### Financial modeling

**Build models**

- "Build a 3-statement financial model for \[company/industry\]"

- "Create a SaaS metrics model with ARR, churn, and LTV calculations"

- "Build an LBO model with debt schedules and returns analysis"

- "Create a real estate pro forma for a multifamily acquisition"

**Forecasting**

- "Build a 12-month revenue forecast using historical trends"

- "Create a headcount capacity plan based on target client count"

- "Model cash flow projections for the next 3 years"

**Scenario analysis**

- "Add a downside case assuming revenue drops 15%"

- "Create base, bull, and bear scenarios with different growth assumptions"

- "Build a sensitivity table showing IRR across exit multiples and hold periods"

### Data analysis

**Insights and trends**

- "What trends stand out in 2025 vs 2024?"

- "Identify the top 10 customers by revenue and their growth rates"

- "Which product categories are underperforming vs budget?"

**Variance analysis**

- "Compare actuals to budget and explain the largest variances"

- "Which accounts have unusual changes vs prior month?"

- "Reconcile these two sheets and highlight discrepancies"

**Categorization**

- "Categorize these transactions into expense types"

- "Tag customer feedback by sentiment and topic"

- "Score each lead based on likelihood to convert"

### Data cleaning

**Standardize formats**

- "Convert all dates to YYYY-MM-DD format"

- "Standardize phone numbers to +1 (XXX) XXX-XXXX"

- "Clean up company names (remove Inc, LLC, Ltd variations)"

**Fix data quality issues**

- "Find and remove duplicate rows, keeping the most recent"

- "Identify and fix unicode/encoding errors"

- "Fill missing values based on patterns in the data"

**Parse and transform**

- "Extract company name from email domain"

- "Split full address into street, city, state, zip columns"

- "Convert this pivot table into a flat data table"

### Formulas

**Troubleshooting**

- "Find all \#REF and \#VALUE errors in this workbook"

- "Why is cell B4 showing an error? Trace the issue"

- "This SUMIF isn't returning the right result — what's wrong?"

**Explanation**

- "Explain what this formula does in plain English"

- "Trace this cell back to its source inputs"

- "Document all the formulas on this sheet"

**Creation**

- "Write a formula to calculate days of inventory from this data"

- "Create a VLOOKUP that pulls price from the rate table"

- "Build a formula that flags overdue invoices"

### Dashboards and reporting

**Dashboards**

- "Create an executive dashboard summarizing all worksheets"

- "Build a KPI scorecard with revenue, margins, and growth metrics"

- "Make an interactive summary with key charts and metrics"

**Reports**

- "Generate a monthly financial summary from the GL data"

- "Create a board-ready P&L with variance commentary"

- "Consolidate regional sheets into a company-wide report"

**Charts**

- "Create a waterfall chart showing revenue bridge"

- "Build a combo chart with revenue bars and margin line"

- "Make a cohort retention heatmap from this data"

### Formatting

**Professional styling**

- "Format this model using IB conventions (blue inputs, black formulas)"

- "Add headers, borders, and proper number formats"

- "Apply consistent formatting across all sheets"

**Conditional formatting**

- "Highlight negative values in red"

- "Color-code rows by status (green/yellow/red)"

- "Add data bars to show relative performance"

### Document import

**PDF extraction**

- "Extract the financial table from this PDF into Excel"

- "Pull the line items from this invoice PDF into my template"

- "Convert this scanned statement into editable data"

**Template population**

- "Fill in my deal template using data from this offering memo"

- "Populate the pitch template with these company metrics"

- "Map the imported CSV data to my standard format"

### Model review

**Audit and validation**

- "Check that all formulas link correctly across sheets"

- "Verify the balance sheet balances in all periods"

- "Find any hardcoded values that should be formulas"

**Improvement**

- "How can I simplify this model structure?"

- "What's missing from this valuation model?"

- "Suggest ways to make this more user-friendly"

------------------------------------------------------------------------

## Frequently asked questions

### Which models are available when using Claude in Excel?

You can switch between Sonnet 4.5 and Opus 4.6 when using Claude in Excel.

### Does Claude understand financial modeling conventions?

Yes, Claude is trained to recognize common financial modeling patterns, formula structures, and industry-standard calculations. However, always verify that outputs match your specific methodologies.

### Can I use Claude in Excel with sensitive data?

Claude in Excel works within your existing security framework. For highly sensitive or regulated data, ensure you follow your organization's data handling policies.

### What happens to my chat history?

Currently, chat history is not saved between sessions. Each time you open the add-in, you start a fresh conversation with Claude. However, we are working to support this in future versions of Claude in Excel.

### How does Claude access my spreadsheet?

Claude reads the content of your currently open workbook, including cells, formulas, and tab structure. It can only access the workbook you have open in Excel.

### What if Claude makes a mistake?

Claude highlights all changes it makes to your workbook. Review these changes carefully before saving or sharing your file. You can always undo changes using Excel's standard undo function.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)

Create and edit files with Claude

[](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work)

Create and edit files with Claude to eliminate hours of busy work

[](https://support.claude.com/en/articles/12219959-claude-for-financial-services-overview)

Claude for Financial Services Overview

[](https://support.claude.com/en/articles/12439380-create-professional-results-across-tools-with-claude-sonnet-4-5)

Create professional results across tools with Claude Sonnet 4.5

[](https://support.claude.com/en/articles/12663107-claude-for-financial-services-skills)

Claude for Financial Services Skills

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
