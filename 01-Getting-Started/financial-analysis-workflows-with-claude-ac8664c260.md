---
title: "Financial analysis workflows with Claude | Claude by Anthropic"
source_url: "https://support.claude.com/en/articles/12220298-financial-analysis-workflows-with-claude"
category: "01-Getting-Started"
fetched_at: "2026-08-02T05:41:35Z"
---

# Financial analysis workflows with Claude

Learn complete financial analysis workflows using a three-phase approach: retrieving data, analyzing information, and creating professional deliverables.

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
  https://claude.com/resources/tutorials/financial-analysis-workflows-with-claude

This article demonstrates how to use Claude for complete financial analysis workflows, from data retrieval through final deliverables. Each workflow follows a three-phase approach: retrieving data from integrated sources, analyzing the information to generate insights, and creating professional outputs for decision-making.

## Understanding the Workflow Approach

### The Three-Phase Process

Effective financial analysis with Claude follows a structured approach that mirrors traditional analytical workflows. The process begins with data retrieval from integrated sources, moves through systematic analysis of that data, and concludes with creation of professional deliverables. This structure ensures completeness while maintaining flexibility for different analytical objectives.

1.  **Retrieve:** Pull data from integrated sources including Daloopa for SEC filings and fundamentals, and S&P Global for comprehensive market data.. The retrieval phase establishes the factual foundation for your analysis.**‍**
2.  **Analyze:** Process and interpret the retrieved data to identify trends, calculate metrics, and generate insights. This phase transforms raw data into actionable intelligence through calculations, comparisons, and pattern recognition.**‍**
3.  **Create:** Generate professional deliverables including investment memos, presentations, financial models, and interactive dashboards. The creation phase packages your analysis into formats suitable for decision-making and communication.

### Setting Up Your Workspace

Before beginning your workflow, establish a proper workspace to maintain context and organization:

- Create a project for your analysis
- Upload any reference documents such as previous analyses or style guides

For detailed project setup instructions, see What are projects? The examples that follow assume you have the necessary integrations enabled and have created a project workspace.

## Workflow 1: Single Company Investment Memo

### Scenario Overview

This workflow demonstrates creating an investment memo for a potential equity investment using publicly available data. The example uses Microsoft as the target company, but the approach applies to any public company with sufficient data coverage. The final output is a concise investment memo suitable for investment committee review or initial screening documentation.

### Phase 1: Retrieve

Begin by gathering comprehensive financial data from multiple sources. Start with fundamental data:

Using Daloopa, retrieve Microsoft's revenue, operating margins, and free cash flow for the last 12 quarters. Also pull segment revenue breakdowns for the same period.

This retrieval provides the core financial metrics needed to assess operational performance and cash generation. The segment data reveals which business units drive growth and profitability. After retrieving fundamental data, gather valuation perspectives:

Using Kensho to access S&P Global data, identify Microsoft's main competitors from SEC filings and retrieve their revenue growth and operating margins for comparison. Also pull Microsoft's key business relationships including major customers and strategic partners.

Combining data from multiple sources provides both quantitative metrics and competitive context. Daloopa supplies the raw financial data while Kensho adds competitive positioning through peer comparisons and business relationship mapping.

### Phase 2: Analyze

With data retrieved, move to analysis that transforms raw numbers into insights:

Analyze the trends in Microsoft's cloud segment growth versus overall company growth. Calculate the free cash flow conversion rate and compare margins to the prior year. Also compare Microsoft's revenue growth and margins against the competitors we identified to assess relative performance. Identify any notable changes in segment mix and flag any customer concentration risks from the business relationships data.

Claude processes the retrieved data to identify patterns and calculate key ratios. The analysis reveals whether cloud services are becoming a larger portion of the business, how efficiently the company converts earnings to cash, and whether profitability is improving or declining.

Consider requesting additional analytical perspectives based on initial findings. If the cloud segment shows accelerating growth, you might ask Claude to analyze whether competitors are experiencing similar trends. If margins are expanding, request a comparison to peer margins to determine if this is company-specific or industry-wide.

### Phase 3: Create

Transform your analysis into a professional investment memo:

Create a 2-page investment memo for Microsoft including: executive summary with investment recommendation, business overview with segment analysis, financial performance highlighting the trends we identified, valuation using fair value compared to current price, and key risks. Format as a Word document.

The resulting memo synthesizes all previous analysis into a structured document.

This workflow produces a professional investment memo suitable for initial screening or committee review, created entirely from publicly available data through Claude's integrations.

## Workflow 2: Competitive Analysis Presentation

### Scenario Overview

This workflow creates a presentation comparing companies within a sector to identify the most attractive investment opportunity. The example analyzes SaaS companies, but the methodology applies to any sector where comparable metrics exist. The output is a presentation suitable for investment committee discussions or client meetings.

### Phase 1: Retrieve

Start by gathering comparable metrics across your peer group:

Using Kensho, retrieve market cap, P/E ratios, revenue growth, and EBITDA margins from S&P Global datasets for these 3 SaaS companies: CRM, NOW, and DOCU for the last fiscal year.

This establishes the baseline comparison metrics. Market cap provides size context, P/E ratios show relative valuation, revenue growth indicates momentum, and EBITDA margins reveal operational efficiency. After establishing the snapshot view, gather trend data:

Also get their quarterly revenue for the last 8 quarters to analyze growth consistency.

The quarterly data reveals whether growth is accelerating, decelerating, or remaining steady. This helps distinguish between companies with sustainable growth versus those experiencing temporary momentum.

### Phase 2: Analyze

Process the data to identify relative attractiveness:

Rank these companies by revenue growth and margin expansion. Calculate the PEG ratio for each. Identify which companies are gaining market share based on relative growth rates. Flag any companies with declining margins.

### Phase 3: Create

Transform the comparative analysis into a presentation:

Create a PowerPoint presentation with 6 slides: title slide, market overview with sector growth, comparative metrics table ranking all the companies, growth trajectory charts showing quarterly revenue trends, valuation comparison with P/E and PEG ratios, and investment recommendation slide highlighting the most attractive opportunity.

**Note:** PowerPoint creation currently has limitations with complex formatting and firm-specific templates. You may need to apply final formatting manually.

## Workflow 3: Portfolio Performance Review

### Scenario Overview

This workflow analyzes an existing portfolio to create performance reporting for quarterly reviews. The example uses a concentrated technology portfolio, but the approach scales to any holdings where data is available. The output is an interactive dashboard suitable for internal review or client reporting.

### Phase 1: Retrieve

Gather performance and fundamental data for all holdings:

Using FactSet, retrieve the following for my technology holdings (MSFT, AAPL): total returns for 1-month, 3-month, YTD and 1-year periods, current price and 52-week high/low, latest quarterly revenue and earnings with year-over-year growth rates, forward P/E ratios and consensus analyst ratings, and any recent earnings surprises. These holdings represent 60% of my portfolio with initial investments made in Q1 2024.

This provides data spanning performance metrics, valuation multiples, fundamental growth indicators, and forward-looking analyst sentiment.

### Phase 2: Analyze

Perform portfolio-level and position-level analysis:

Calculate the weighted average portfolio return based on position sizes for each time period. Compare each holding's total return against the NASDAQ-100 index returns. Rank holdings by YTD performance and identify any laggards. Calculate which positions have beaten or missed earnings expectations in the last quarter. Assess relative valuation by comparing each stock's forward P/E to its 5-year average.

This analysis provides multiple perspectives: weighted returns show overall portfolio performance across different time horizons, benchmark comparison reveals alpha generation, earnings surprise analysis indicates execution quality, and valuation assessment identifies potential rebalancing candidates.

### Phase 3: Create

Generate an interactive dashboard for the portfolio review:

Create an interactive artifact showing: portfolio summary with weighted returns for each period and performance versus benchmark, individual position cards showing total return, consensus rating, forward P/E, and recent earnings surprise, a waterfall chart showing each position's contribution to total portfolio return, and a scatter plot comparing YTD returns against forward P/E ratios to identify value opportunities. Include drill-down capability for each holding to see detailed performance metrics.

[Artifacts can be shared](https://support.claude.com/en/articles/9547008-discovering-publishing-customizing-and-sharing-artifacts#h_264285dcf3) with other members of your organization. The interactive nature allows stakeholders to explore the data without requiring multiple static reports.

## Next Steps

- Review integration guides to understand data availability for your specific use cases.
- See [Prompting Strategies for Financial Analysis](https://support.claude.com/en/articles/12220277-prompting-strategies-for-financial-analysis) for techniques to optimize your workflows.
- Test workflows with smaller datasets before scaling to full analyses.
- Save successful prompt sequences as templates for recurring analyses.

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
