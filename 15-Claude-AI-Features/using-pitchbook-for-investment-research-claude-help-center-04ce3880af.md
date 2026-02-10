---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-10T10:49:30Z"
source_url: "https://support.claude.com/en/articles/12621857-using-pitchbook-for-investment-research"
title: "Using PitchBook for Investment Research | Claude Help Center"
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

[](#h_7ec07773e9)

[](#h_f7160a00f6)

[](#h_09b4d1106a)

[](#h_ab2e9f9cf0)

[](#h_cbdf6806de)

[](#h_ebd2397857)

[](#h_de9b0527a4)

[](#h_33b29af8a1)

[](#h_063cc695a1)

[All Collections](/en/)

[Claude for Financial Services](https://support.claude.com/en/collections/13972013-claude-for-financial-services)

[Market Data](https://support.claude.com/en/collections/16288976-market-data)

Using PitchBook for Investment Research

# Using PitchBook for Investment Research

Updated this week

Table of contents

[](#h_7ec07773e9)

[](#h_f7160a00f6)

[](#h_09b4d1106a)

[](#h_ab2e9f9cf0)

[](#h_cbdf6806de)

[](#h_ebd2397857)

[](#h_de9b0527a4)

[](#h_33b29af8a1)

[](#h_063cc695a1)

The PitchBook Premium integration gives Claude access to proprietary private capital market data and analytical metrics. This article outlines the steps to set up and use PitchBook data for financial research, including financial analysis, competitive benchmarking, network relationship mapping, and investor portfolio analysis.

The PitchBook integration relies on Claude’s ability to use [remote connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

## What This Integration Provides

The integrated dataset provided by this integration includes profiles for more than 8.5 million private companies, 2.8 million deals, 597k investors, and 154k funds. This integration excludes some proprietary 3rd-party data included in the PitchBook platform.

## Capabilities

The PitchBook integration enables Claude to access private capital market data:

- **Entity Search and Identification:** Search PitchBook's database for companies, investors, funds, people, limited partners (LPs), and deals by name or ticker, retrieving unique PitchBook identifiers (PBIDs).

- **Company Data Access:** Retrieve company profiles, including business descriptions, ownership status, complete financing history, financial statements (income statement, balance sheet, cash flow), team members, and current/former investors.

- **Investor and Fund Information:** Access investor profiles with AUM and investment focus, portfolio holdings showing current and exited investments, funds raised by each investor, and limited partner commitments to specific funds.

- **Deal and Transaction Details:** Pull complete deal information including participants, investment amounts, valuations, terms, lead investor status, and detailed cap tables showing ownership percentages and liquidation preferences across rounds.

- **Relationship and Network Data:** Find connections between entities, such as co-investors in deals, shared portfolio companies between investors, team member histories across companies, and LP participation across multiple funds.

## How Claude Uses PitchBook's Data

Claude accesses PitchBook data to help build your analyses. Here are several examples of tasks where Claude may decide to use data provided by PitchBook:

- **Funding Timeline Construction:** Claude retrieves a company's deal history to show how valuations changed, which investors participated in each round, and how ownership diluted over time.

- **Peer Group Benchmarking:** When comparing companies, Claude pulls financial metrics, valuation multiples, and funding amounts to identify which companies are valued higher or lower than similar ones.

- **Investor Portfolio Analysis:** Claude examines an investor's portfolio to identify their typical investment sizes, preferred sectors, and stage focus.

- **Connection Discovery:** Claude traces relationships between companies and investors to find warm introduction paths, like identifying mutual connections through board members or past deals.

- **Exit Pattern Recognition:** Claude analyzes past exits in your sector to show typical acquisition multiples, common buyers, and average holding periods for similar companies.

## Setting Up PitchBook Integration

Technical details of the PitchBook Integration can be found in the [PitchBook Premium Integration MCP Service Documentation](https://help.pitchbook.com/s/article/PitchBook-Premium-for-Claude-by-Anthropic). Users must possess Single Sign-On (SSO) credentials and a seat-based, unlimited, or trial PitchBook license.

If your account does not have access to the MCP service, please contact your account representative.

### For Organization Owners

1.  Navigate to [Admin settings \> Connectors](https://claude.ai/admin-settings/connectors).

2.  Scroll down and click “Add custom connector" at the bottom of the list.

3.  Access the MCP URL via SSO here: [https://premium.mcp.pitchbook.com/mcp](https://premium.mcp.pitchbook.com/mcp)

4.  Name the connector (e.g. "PitchBook Premium")

5.  Click “Add”

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Discover Company Info

    Using PitchBook data, tell me about Plaid’s funding status, including the most recent investment date, round type, and use of proceeds. Include a list of lenders, active and former investors, and relevant news coverage about previous investment rounds.

Streamline the financial research journey from search to insight. Claude can retrieve comprehensive PitchBook data on a specific company, including an overview, financials, deal history, key personnel, and investors. When comparing multiple companies from a user- or Claude-generated list, Claude retrieves PitchBook data from each company before compiling results into a single list to spot deal opportunities.

**When to use:** Researching specific companies for deal sourcing, market intelligence gathering, benchmarking, asset allocation, and business development.

## Competitive Analysis

    Using PitchBook data, help me identify investment opportunities by benchmarking companies in the healthtech wearables market. Provide details on each company’s recent investment history, profitability, liquidity, and growth rates.

Quickly compare targets to identify promising opportunities for investments, mergers and acquisitions, and partnerships. Claude performs this action using company and deal lists provided by users, or by generating company lists from the web and other sources. The LLM accesses PitchBook’s comprehensive company intelligence, including investment history, product details, financial performance, and more, to retrieve critical details for each company on the list. Users can accelerate deal flow by comparing these metrics in a convenient and readable output.

**When to use:** Comparing financial and performance metrics across multiple companies to find new opportunities, accelerate market mapping, identify acquisition targets, and streamline deal sourcing workflows.

## Relationship Mapping

    Using PitchBook data, identify Instacart investors. Then, pull portfolios for each investor’s top 3 VCs to see other companies in this space, and analyze those VC companies’ investors to map the competitive landscape.

Discover unexpected connections between companies, investors, and professionals by using Claude to transform PitchBook’s comprehensive private capital market data into market maps that demonstrate complex relationships within the industry. Claude accesses PitchBook’s proprietary data to accelerate financial research by extracting these insights and producing easy-to-read competitive clusters.

**When to use:** Visualizing the business, investment, and product relationships between companies to inform deal sourcing, supply chain management, strategic partnerships, investor sourcing, and more.

## Tips for Using PitchBook's Data

- Start prompts with “Use PitchBook data to...” to ensure that Claude returns results based on PitchBook’s comprehensive dataset of private capital market intelligence.

- Ask detailed, multi-part questions to receive comprehensive answers to complex queries. For example, to build a market map you should (1) start with a company, (2) pick key investors, (3) analyze portfolio companies, and (4) ask to identify patterns across the network.

- Use PitchBook’s data as a reference for deal sourcing, due diligence, and deal execution, rather than as the sole source of information.

- Combine data retrieval with analysis from PitchBook researchers to build a complete view of the market and identify opportunities with full context.

- PitchBook's private capital market data is sourced directly from funds, companies, filings, and relationships.

## Contact

If you are having trouble completing the PitchBook Premium integration, you can contact [\[email protected\]](/cdn-cgi/l/email-protection#1d6e686d6d726f695d6d74697e757f727276337e7270) for help.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12219959-claude-for-financial-services-overview)

Claude for Financial Services Overview

[](https://support.claude.com/en/articles/12220057-using-morningstar-for-investment-research)

Using Morningstar for Investment Research

[](https://support.claude.com/en/articles/12220212-using-factset-for-comprehensive-financial-research)

Using FactSet for Comprehensive Financial Research

[](https://support.claude.com/en/articles/12651668-using-moody-s-for-financial-analysis)

Using Moody’s for Financial Analysis

[](https://support.claude.com/en/articles/12662597-using-chronograph-for-portfolio-monitoring)

Using Chronograph for Portfolio Monitoring

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
