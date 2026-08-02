---
title: "Using S&amp;P global data for financial analysis | Claude by Anthropic"
source_url: "https://support.claude.com/en/articles/12220135-using-s-p-global-data-for-financial-analysis"
category: "99-Other"
fetched_at: "2026-08-02T05:41:04Z"
---

# Using S&P global data for financial analysis

Use Claude's Kensho integration to access S&P Global's financial data for comprehensive market and fundamental analysis of public companies.

- 


  Finance

- 


  Claude.ai

- 


  Watch time

  5

  min

  min

- 


  [Copy link](#)
  https://claude.com/resources/tutorials/using-s-p-global-data-for-financial-analysis

The Kensho LLM-ready API integration provides Claude with access to S&P Global’s financial data, delivering comprehensive market and fundamental data for public companies. This article explains how to set up the Kensho integration and use S&P data for financial analysis, including price history, financial statements, segment data, and business relationships.

## What This Integration Provides

### Capabilities

The integration with Kensho’s LLM-ready API enables Claude to access multiple dimensions of S&P Global’s financial and market data:

- **Company Identification and Information:** Retrieve company profiles using tickers, ISINs, or CUSIPs, including industry classifications, employee counts, headquarters locations, and operating status.


- **Historical Price and Market Data:** Access OHLC prices, volumes, market cap, and enterprise value at daily, weekly, monthly, or yearly frequencies, with adjusted prices for accurate return calculations.


- **Financial Statement Access:** Pull complete balance sheets, income statements, and cash flow statements for annual, quarterly, LTM, or YTD periods with customizable date ranges.


- **Granular Financial Metrics:** Extract specific line items from 200+ available metrics including revenue, EBITDA, R&D expense, and calculated ratios like debt-to-equity.


- **Segment Performance Data:** Access business unit and geographic breakdowns showing how revenue and operating income distribute across divisions (availability varies by company).


- **Business Relationship Mapping:** Identify supplier relationships, customer dependencies, and strategic partnerships from SEC filings to assess operational risks.


- **Competitor Intelligence:** Retrieve competitor lists from multiple sources including SEC filings, self-identification, and third-party analysis.


- **Time Period Management:** Determine latest reporting periods and calculate historical quarters for consistent comparisons across companies with different fiscal years.


- 

### How Claude Uses S&P Global Data

Claude applies Kensho's capabilities to support comprehensive financial analysis leveraging S&P Global data:

- **Cross-Identifier Lookups:** Automatically handles tickers, ISINs, or CUSIPs, useful for international portfolios or fixed income securities.


- **Multi-Period Analysis:** Constructs time series by pulling data across periods, calculating growth rates and identifying trend changes.


- **Statement Reconciliation:** Combines data from different statements to calculate derived metrics and verify consistency.


- **Peer Group Construction:** Retrieves identical metrics across companies for true apples-to-apples comparisons.


- **Relationship Network Analysis:** Maps business ecosystems to reveal concentration risks and strategic positioning not apparent from financials alone.

## Setting Up the Kensho Integration

Technical details of the Kensho Integration can be found in the [Kensho Integration MCP Server Documentation](https://docs.kensho.com/llmreadyapi/mcp). You will need to contact S&P Global to get access to the MCP server.

### For Organization Owners

1.  Navigate to [Admin settings \> Connectors](https://claude.ai/admin-settings/connectors).


1.  Scroll down and click “Add custom connector" at the bottom of the list.


1.  Enter the Kensho integration URL: [https://kfinance.kensho.com/integrations/mcp](https://kfinance.kensho.com/integrations/mcp)


1.  Name the integration (e.g., "Kensho S&P")


1.  Click "Add"

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Comprehensive Company Profile

Using the Kensho integration, create a complete profile for Microsoft (MSFT) including current market data, latest financial metrics, business segments, and key competitor data from S&P Global. Include market cap, enterprise value, trailing twelve-month revenue and margins, plus geographic revenue breakdown.

This type of comprehensive profile combines multiple data types into a single analytical view. Claude retrieves current market metrics, pulls recent financial performance, and identifies segment breakdowns to show how the business operates across different units and geographies. The competitor identification adds context about the competitive environment.

**When to use:** Initial company research or updating investment memos with current information.

**Tip:** Request both market data and fundamentals together for a complete overview that includes valuation context alongside operational performance.

### Historical Price Performance Analysis

Pull five years of weekly price data for Tesla (TSLA) and calculate the volatility, maximum drawdown, and performance versus the S&P 500. Include adjusted prices to account for any stock splits and show periods of highest volatility.

Historical price analysis using S&P Global data goes beyond simple price charts. Claude can calculate risk metrics like volatility and maximum drawdown while comparing performance to benchmarks. Using adjusted prices ensures that return calculations properly account for corporate actions, providing accurate performance measurement over multi-year periods.

**When to use:** Evaluating historical risk-return profiles or backtesting investment strategies.

**Note:** Adjusted prices ensure accurate return calculations across corporate actions like splits and special dividends, which is essential for long-term performance analysis.

### Financial Statement Deep Dive

Retrieve Apple's last 12 quarters of income statements and calculate the trend in gross margins, operating margins, and R&D as percentage of revenue. Show both the quarterly values and the rolling four-quarter averages to smooth seasonality.

Financial statement analysis through Kensho allows examination of margin trends and cost structure evolution over time. Claude can pull specific line items from S&P Global datasets across multiple quarters, calculate relevant ratios, and apply smoothing techniques to identify underlying trends beyond seasonal fluctuations. This granular approach reveals operational changes that might be obscured in annual reports.

**When to use:** Analyzing margin trends, cost structure changes, or earnings quality.

**Tip:** LTM calculations help normalize for seasonal businesses, providing clearer trend analysis for companies with significant quarterly variations.

### Competitor Benchmarking

Identify Netflix's competitors from their SEC filings and compare key metrics including subscriber growth, content costs, average revenue per user, and free cash flow margins. Focus on direct streaming competitors they specifically mention as competitive threats.

Competitor analysis combines Kensho's relationship mapping with financial metric comparisons. Claude first identifies competitors from various sources, then retrieves comparable metrics for each company. This approach provides both the competitive landscape view and quantitative performance comparisons, helping assess relative positioning and competitive advantages.

**When to use:** Industry analysis or relative valuation work.

**Note:** Different source filters provide varying perspectives on competition—SEC filings show who companies view as threats, while third-party sources may identify less obvious competitive dynamics.

### Segment Performance Tracking

Show Amazon's segment breakdown for the last eight quarters, including revenue and operating income by segment. Calculate the growth rates for AWS, North America retail, and International retail, and identify which segments are driving overall margin expansion.

Segment analysis reveals the underlying drivers of consolidated performance. Claude retrieves segment-level financial data to show how different business units contribute to overall results. By tracking segment metrics over time, you can identify which divisions are accelerating or decelerating, understand margin mix shifts, and assess the quality of revenue growth.

**When to use:** Understanding business mix changes and identifying growth drivers.

**Tip:** Segment data reveals trends not visible in consolidated statements, particularly for conglomerates or companies undergoing business model transitions.

### Supply Chain Analysis

Map NVIDIA's key business relationships including their primary chip manufacturers, major customers, and strategic technology partners. Focus on relationships mentioned in their latest 10-K filing to understand supply chain dependencies and customer concentration risks.

Business relationship mapping through Kensho provides insights into operational dependencies and strategic positioning. Claude identifies suppliers, customers, and partners from regulatory filings in S&P Global datasets, revealing concentration risks and potential vulnerabilities. This network view complements financial analysis by highlighting operational factors that could impact future performance.

**When to use:** Assessing operational risks or understanding industry value chains.

**Key benefit:** Reveals dependencies not apparent from financial statements alone, such as single-source supplier risks or customer concentration that could impact revenue stability.

## Tips for Using S&P Global Data

- Use any identifier format (ticker, ISIN, CUSIP) - Claude handles conversion automatically


- Request specific date ranges to manage data volume and focus analysis


- Combine market data with fundamentals for comprehensive analysis


- Check data availability periods using the latest reporting period function


- Note that segment data availability varies by company reporting practices


- Be specific about which financial statement items you need from the 200+ available metrics


- Consider using LTM periods for companies with significant seasonality


- Remember that business relationship data comes from disclosed sources and may not capture all partnerships


## Related tutorials

[Install financial services plugins for Claude Cowork](/resources/tutorials/install-financial-services-plugins-for-cowork)

Install financial services plugins for Claude Cowork

Install financial services plugins for Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/install-financial-services-plugins-for-cowork)

Tutorial

[How to build a plugin from scratch in Claude Cowork](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)

How to build a plugin from scratch in Claude Cowork

How to build a plugin from scratch in Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)

Tutorial

[Getting started with Claude in Excel](/resources/tutorials/getting-started-with-claude-in-excel)

Getting started with Claude in Excel

Getting started with Claude in Excel

Tutorial

[Tutorial](/resources/tutorials/getting-started-with-claude-in-excel)

Tutorial

[How to use Claude in Excel for accounting: Revenue model validation](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)

How to use Claude in Excel for accounting: Revenue model validation

How to use Claude in Excel for accounting: Revenue model validation

Tutorial

[Tutorial](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)

Tutorial

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)

Button Text

Learn

[Button Text](#)

Button Text

Code

[Button Text](#)

Button Text

Write

- Help me develop a unique voice for an audience


  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style


  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas


  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply


  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas


  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview


  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept


  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips


  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me


  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies


  This is another test

- Write grant proposals


  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts


  this is a test

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Design

  [Claude Design](/product/design)
  Claude Design

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Features

- Claude for Chrome

  [Claude for Chrome](/claude-for-chrome)
  Claude for Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

- Skills

  [Skills](/skills)
  Skills

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Solutions

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Enterprise

  [Enterprise](/solutions/enterprise)
  Enterprise

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Legal

  [Legal](/solutions/legal)
  Legal

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Claude Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://platform.claude.com/docs)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Ecosystem

  [Ecosystem](/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Console login

  [Console login](https://platform.claude.com/)
  Console login

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Community

  [Community](/community)
  Community

- Connectors

  [Connectors](/connectors)
  Connectors

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](/plugins)
  Plugins

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/partners/services)
  Service partners

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
  Use cases

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Policy on the AI Exponential
