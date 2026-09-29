---
title: "Advancing Claude for Financial Services \\ Anthropic"
source_url: "https://www.anthropic.com/news/advancing-claude-for-financial-services"
category: "19-Reference"
fetched_at: "2026-09-11T06:29:14Z"
tags: ["agents", "news-research", "skills"]
---

# Advancing Claude for Financial Services

Oct 27, 2025

We're expanding [Claude for Financial Services](../18-Industry-UseCases/finance.md) with an Excel add-in, additional connectors to real-time market data and portfolio analytics, and new pre-built Agent Skills, like building discounted cash flow models and initiating coverage reports.

These updates build on Sonnet 4.5’s state of the art performance on financial tasks, topping the [Finance Agent benchmark](https://www.vals.ai/benchmarks/finance_agent) from Vals AI at 55.3% accuracy. They augment Claude’s intelligence with solutions for time-consuming but critical financial work, built into preferred industry tools.

## Claude for Excel

We’re releasing [Claude for Excel](../14-Connectors/claude-for-excel.md) in beta as a research preview. This allows users to work directly with Claude in a sidebar in Microsoft Excel, where Claude can read, analyze, modify, and create new Excel workbooks. Claude provides full transparency about the actions it takes: it tracks and explains its changes and lets users navigate directly to the cells it references in its explanations.

This means that Claude can discuss how a spreadsheet works, modify it while preserving its structure and formula dependencies, debug and fix cell formulas, populate templates with new data and assumptions, or build new spreadsheets entirely from scratch.

Claude for Excel adds to our existing integrations with Microsoft’s applications. In the Claude apps, Claude can also create and edit files, including Excel spreadsheets and PowerPoint slides, and connect to Microsoft 365 to search for files, emails, and Teams conversations. Select Claude models are also available in Microsoft Copilot Studio and Researcher agent.

Claude for Excel is now in beta as a research preview for Max, Enterprise, and Teams users. We’ll collect real-world feedback from 1,000 initial users before rolling the feature out more broadly. To join the waitlist, [click here](https://docs.google.com/forms/d/e/1FAIpQLSedsdrIw00BOGbiIhAQvTaC7mOQRW6jOofAt7PJ1lYAGzvfUw/viewform?usp=dialog).

## Connecting Claude to live information

[**Connectors**](https://claude.ai/redirect/website.v1.c1e4dce4-dc13-4d09-baa6-fc6f9bae9bdb/settings/connectors) provide Claude with direct access to external tools and platforms. [In July](claude-for-financial-services.md), we added connectors for S&P Capital IQ, Daloopa, Morningstar, and PitchBook. We’re adding new connectors that give Claude immediate access to more information in real time:

- **Aiera** provides Claude with real-time earnings call transcripts and summaries of investor events, like shareholder meetings, presentations, and conferences;
- Aiera’s connector also enables a data feed from **Third Bridge**, which gives Claude access to a library of insights interviews, company intelligence, and industry analysis from experts and former executives;
- **Chronograph** gives private equity investors operational and financial information for portfolio monitoring and conducting due diligence, including performance metrics, valuations, and fund-level data;
- **Egnyte** enables Claude to securely search permitted data for internal data rooms, investment documents, and approved financial models, while maintaining governed access controls;
- **LSEG** connects Claude to live market data, including fixed income pricing, equities, foreign exchange rates, macroeconomic indicators, and analysts’ estimates of other important financial metrics;
- **Moody’s** provides access to proprietary credit ratings, research, and company data – including ownership, financials and news on more than 600 million public and private companies – supporting work and research in compliance, credit analysis, and business development;
- **MT Newswires** provides Claude with access to the latest global multi-asset class news on financial markets and economies.

For details on MCP connector setup and prompting guidance to maximize the benefit of each connector, see [our documentation here](https://support.claude.com/en/collections/13972013-claude-for-financial-services).

## New Agent Skills for finance tasks

Earlier this month, we introduced [Agent Skills](skills.md). Skills are folders that include instructions, scripts, and resources that Claude can use to perform given tasks. Skills work across all Claude apps, including [Claude.ai](http://claude.ai/redirect/website.v1.c1e4dce4-dc13-4d09-baa6-fc6f9bae9bdb), Claude Code, and our API. To make Claude better at financial services tasks, we’ve added 6 new skills:

- **Comparable company analysis**, with valuation multiples and operating metrics, which can be easily refreshed with updated data;
- **Discounted cash flow models**, including full free cash flow projections, WACC calculations, scenario toggles, and sensitivity tables;
- **Due diligence data packs**, processing data room documents into Excel spreadsheets with financial information, customer lists, and contract terms;
- **Company teasers and profiles**, condensed company overviews for pitch books and buyer lists;
- **Earnings analyses**, which research quarterly transcripts and financials to extract important metrics, guidance changes, and management commentary;
- **Initiating coverage reports** with industry analysis, company deep-dives, and valuation frameworks.

As with Claude for Excel, these new skills are being rolled out in preview for Max, Enterprise, and Teams users. You can sign up on behalf of your team or organization [here](https://docs.google.com/forms/d/e/1FAIpQLSdXOB2bR7r_YhwENL1VplbgWvQ96YhInhHj5Fr9_V_MAOCiNQ/viewform).

## Claude’s impact in financial services

Claude is already widely used by leading banking, asset management, insurance, and financial technology companies. It supports front office tasks like client experience, middle office tasks in underwriting, risk and compliance, and back office tasks like code modernization and legacy processes. With ongoing updates to our models and products specific to financial services, we expect Claude to become even better in roles like these.

> Citi chose to leverage Claude as part of its AI powered Developer Platform because of its advanced planning and agentic coding capabilities, focus on safety and reliability, and compatibility with our workloads.
>
> David Griffiths  
> CTO, Citi

> Working with Anthropic goes beyond deploying another AI tool—it's about partnering with a company that understands the complexity that financial services requires. Claude excels by seamlessly integrating multiple data sources and automating workflows that previously consumed significant time.
>
> Bobby Grubert  
> Head of AI and Digital Innovation, RBC Capital Markets

> What we've valued about Anthropic is not just their powerful models, but how they've positioned them for enterprise needs. When I talk with customers about AI, data privacy is always their first concern—it's the critical foundation we have to address before we can even begin discussing capabilities.
>
> David Horn  
> AI Lead, Brex

> 75% of our engineers now save 8 to 10+ hours every week using our open source AI agent for creating SQL queries (codename goose) — accelerating velocity and cutting down on busywork. For the tasks we care about measuring specifically, the Claude family has performed the best.
>
> Bradley Axen  
> Principal Data and Machine Learning Engineer, Block

> Anthropic's multi-cloud solution stands out for its scale, performance and security, aligning with our operational needs and customer expectations. It exceeded our performance benchmarks and met all our security requirements, making it the ideal solution. We think Claude will help Coinbase build solutions for different customer segments and bring a billion customers to the crypto economy.
>
> Varsha Mahadevan  
> Senior Engineering Manager, Coinbase

> As one of Canada’s largest institutional investors, BCI is driven to experiment, build, and innovate. Claude has accelerated our ability to get up-to-speed on investments and the underlying portfolio’s progress, making us more effective. As we push boundaries on what’s possible, we’re excited by the opportunities.
>
> Christian Grunt  
> Senior Principal, Private Equity, British Columbia Investment Management Corporation

> We see AI agents as the next evolution of commerce—autonomous systems that can predict, suggest, and find the products and services consumers need. This is only possible with a secure foundation at the base built on consent, privacy, transparency, and security. Anthropic is a key partner of Visa to make this dream a reality and shares our values and principles around responsible data usage.
>
> President, Technology  
> Rajat Taneja, Visa

> Claude serves as a remarkable reasoning-powered companion. Its ability to shift smoothly between quick execution and deep analysis, with fine-grained control over both, is exactly what's been missing in AI systems. Anthropic is a go-to technology & partner for AI workloads that require reliable intelligence at scale.
>
> Lucas Baker  
> Quantitative Research Lead, Jump Trading

> Through our training program with Anthropic, we've seen portfolio companies adopt Claude Code with remarkable results. Development teams are completing complex tasks in hours instead of days, and we're hearing from previously skeptical engineers that they can't imagine working without it.
>
> Mike Barry  
> Managing Operating Partner, Product & Technology, Francisco Partners

> Chronograph’s connection to Claude will fundamentally change what is possible for our clients – much like how Claude for Enterprise has transformed our internal operations. The partnership between Chronograph and Claude enables our clients to uncover new insights, save significant time, and achieve superior returns using their private capital portfolio data within Claude’s powerful toolset.
>
> Charlie Tafoya  
> Co-Founder and CEO, Chronograph

> With our GenAI-ready data offerings, we continue to support our customers in their AI evolution—enriching our data via a semantic layer and delivering it through Model Context Protocol (MCP) servers and Smart APIs. Our partnership with Anthropic makes Moody’s vast data estate accessible directly where our customers are innovating.
>
> Cristina Pieretti  
> Head of Digital Content and Innovation, Moody's

> LSEG has a long-established reputation for our open, partnership approach and meeting our customers wherever their workflows are taking place. Secure, enterprise grade AI applications, such as Claude, are expanding the opportunities for LSEG to build deep partnerships with customers.
>
> Ron Lefferts  
> Co-head, Data & Analytics, London Stock Exchange Group (LSEG)

01 / 12

Below, Alexander Bricken, Applied AI Lead for Financial Services, and Nicholas Lin, Head of Product for Financial Services, discuss Anthropic’s research and product strategy within financial services, as well as customer examples.

## Getting started

To learn more about using Claude for Financial Services, [see here](../18-Industry-UseCases/finance.md) or [contact](https://claude.com/contact-sales/financial-services) our sales team. And to see the new features in action and hear directly from financial services leaders, you can also [register here](http://website.anthropic.com/webinars/%20claude-for-financial-services) for our launch webinar.

  
## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
