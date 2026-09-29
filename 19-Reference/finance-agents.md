---
title: "Agents for financial services \\ Anthropic"
source_url: "https://www.anthropic.com/news/finance-agents"
category: "19-Reference"
fetched_at: "2026-09-10T06:46:12Z"
tags: ["agents", "news-research"]
---

# Agents for financial services

May 5, 2026

We’re releasing ten ready-to-run agent templates for the most time-consuming work in financial services: building pitchbooks, screening KYC files, and closing the books at month-end. Each one ships as a [plugin](../15-Claude-AI-Features/use-plugins-in-claude-cowork.md) in Claude Cowork and Claude Code, and as a cookbook for [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), so a team can put Claude on real financial work in days rather than months.

Claude also now works across Microsoft Excel, PowerPoint, Word, and Outlook (coming soon) through the Claude add-ins for Microsoft 365. Once the add-ins are installed, context carries automatically between applications, so work that starts in a model can end in a deck without re-explaining anything in between.

Finally, we’re continuing to expand our partner ecosystem with new connectors and an MCP app, so the agents draw on the data financial professionals already use. Connectors give Claude governed, real-time access to a provider’s data, and MCP apps go a step further by embedding the provider’s own tools directly inside Claude.

These updates pair best with Claude Opus 4.7, which is state-of-the-art on financial tasks and leads the industry on [Vals AI's Finance Agent benchmark](https://www.vals.ai/benchmarks/finance_agent), at 64.37%.

## New agent templates for finance work

Each agent template is a reference architecture that packages three things: skills (instructions and domain knowledge for the task), connectors (governed access to the data the task runs on), and subagents (additional Claude models that are called upon by the main agent, for specific sub-tasks such as comparables selection or methodology checks). Firms can adapt any of them to their own modeling conventions, risk policies, and approval flows.

Enable these new agent templates either as plugins within Claude Cowork or Claude Code, or as cookbooks for Claude Managed Agents. Find all the plugins and cookbooks at the [financial services marketplace](https://github.com/anthropics/financial-services).

The full list of new agents is as follows:

**Research and client coverage**

- **Pitch builder** creates target lists, runs comparables, and drafts pitchbooks for client meetings;
- **Meeting preparer** assembles client and counterparty briefs ahead of calls;
- **Earnings reviewer** reads transcripts and filings, updates models, and flags thesis-relevant changes;
- **Model builder** creates and maintains financial models from filings, data feeds, and analyst inputs;
- **Market researcher** tracks sector and issuer developments, synthesizes news, filings, and broker research, and flags items for credit and risk review.

**Finance and operations**

- **Valuation reviewer** checks valuations against comparables, methodology, and the firm's review standards;
- **General ledger reconciler** reconciles general ledger accounts and runs net asset value calculations against the books of record;
- **Month-end closer** runs the close checklist, prepares journal entries, and produces close reports;
- **Statement auditor** reviews financial statements for consistency, completeness, and audit-readiness;
- **KYC screener** assembles entity files, reviews source documents, and packages escalations for compliance review.

There are two ways to put these to work.

As a plugin in Claude Cowork or Claude Code, the template runs alongside the analyst, using the software already on their desktop. Hand the Pitch agent a target list, and you can get back a comps model in Excel, a pitchbook drafted in PowerPoint, and a cover note ready in Outlook.

As a [Claude Managed Agent](../04-API-Reference/Other/managed-agents-overview.md), the same template runs autonomously on the Claude Platform, for work that spans a whole book of deals or a nightly schedule. The cookbooks stand it up with the building blocks a firm would otherwise engineer themselves: long-running sessions that can work throughout a multi-hour deal close, per-tool permissions, managed credential vaults, and a full audit log in the Claude Console where compliance and engineering teams can inspect every tool call and decision.

In both scenarios, users stay firmly in the loop—reviewing, iterating on, and approving Claude’s work before it goes to a client, gets filed, or is acted on.

## Claude across Excel, PowerPoint, Word, and Outlook

Claude can work directly in Microsoft [Excel](../14-Connectors/claude-for-excel.md), [PowerPoint](../14-Connectors/claude-for-excel.md), [Word](https://claude.com/claude-for-word), and Outlook via add-ins.

In Outlook, it can act as a chief of staff that triages your inbox, arranges meetings, and drafts responses in your voice. In Excel, it builds financial models from filings and data feeds, audits formulas across linked workbooks, and runs sensitivity analyses. In PowerPoint, it drafts decks that update automatically when the underlying numbers change. In Word, it edits credit memos against a firm’s own templates. Claude carries its knowledge and context across all four platforms: an analyst who’s started a model in Excel doesn’t need to re-explain it when that work moves to PowerPoint.

In Claude Cowork, users can also assign Claude work tasks from anywhere—by text or by voice—using [Dispatch](../21-Account-Support/assign-tasks-to-claude-from-anywhere-in-cowork.md). Claude can keep working on analysts’ local files while they’re away from their desk, with finished work ready for review by the time they’re back.

## The broadest ecosystem for financial services

AI agents are only as good as the data and context they can access. Claude connects to dozens of market data, research platforms, and financial companies’ internal systems—including FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar, Chronograph, LSEG, and Daloopa—along with firms’ own data warehouses, research repositories, and CRMs, all under governed access controls.

We’re now adding connectors and an MCP app from new partners. The new connectors give direct, real-time access to market and research data, while the MCP app surfaces custom, interactive UI directly within Claude.

The new connectors are:

- **Dun & Bradstreet**, which provides the global standard for verified business identity and helps enterprises connect systems of record and scale AI-enabled workflows;
- **Fiscal AI**, which extends real-time fundamentals coverage across public equities for deeper research and benchmarking;
- **Financial Modeling Prep**, which provides real-time quotes, fundamentals, statements, filings, and transcripts across equities, ETFs, crypto, forex, and commodities;
- **Guidepoint**, which searches 100,000+ compliance-reviewed expert interview transcripts and provides verbatim excerpts linked to source;
- **IBISWorld**, which tracks industry-level revenue, financial ratios, risk scores, cost structures, and forecasts across thousands of sectors;
- **SS&C Intralinks**, which gives Claude access to DealCenter AI data rooms for document search, diligence Q&A, and deal-activity tracking;
- **Third Bridge**, which gives Claude access to primary-source expert interviews on companies, sectors, and value chains;
- **Verisk**, which provides property, casualty, and specialty insurance data for underwriting, claims, and risk analysis.

In addition, **Moody's** has launched an MCP app that brings proprietary credit ratings and data on more than 600 million public and private companies for use in compliance, credit analysis, and business development.

## Claude's impact in financial services

Many leading banks, asset managers, and insurers choose Claude. It supports the full range of these organizations' work: front office tasks like research and client experience, middle office work in underwriting, risk, and compliance, and back office work like code modernization and operations.

> Our investment professionals live in data and analytical models, and Claude for Excel meets them there. Analysts are using it to build and update coverage models, separate signal from noise, and pressure-test their work — all with a step-change in efficiency.
>
> Atte Lahtiranta  
> Head of Core Engineering, Citadel

> FIS sits at the center of how money moves for thousands of financial institutions worldwide. When we began to build AI agents, we knew we needed a provider we could trust. Anthropic was the clear choice. Together we're building an agent that compresses AML investigations from days to minutes, with credit decisioning, fraud prevention, and deposit retention agents to follow. FIS clients won't need to build this infrastructure themselves. It's already here.
>
> Stephanie Ferris  
> CEO and President, FIS

> With Eliza and Claude, we’re giving processes new digital employees who work the case end to end.
>
> Leigh-Ann Russell  
> CIO & Global Head of Engineering, BNY

> Carlyle has adopted Claude as a key part of our AI technology stack because of its strong coding capabilities, agentic reasoning, and continual advances in both the underlying models and key features. Claude is a core tool for delivering value across our firm from investing to operations to portfolio management.
>
> Matt Anderson  
> Chief Digital Officer, Carlyle

> Claude compresses and enhances the work before the meeting so each and every meeting is more impactful — prep time has been transformed into idea time, with faster workflows, richer client insights, and new use cases we didn’t anticipate.
>
> Patrick Suehnholz  
> Managing Director & Banking COO, Mizuho

> Since we started introducing personalized Claude and Claude Code assistants, we have seen significantly elevated levels of engineering excellence and meaningful improvements in productivity. We are pleased to be delivering value by putting AI to work in advancing the company’s strategic innovation priorities of extending our advantage in risk expertise; providing great experiences for our customers, distribution partners and employees; and optimizing our productivity and efficiency.
>
> Mojgan Lefebvre  
> Executive Vice President and Chief Technology & Operations Officer, Travelers

> 100% of employees at Walleye Capital use Claude Code. This level of adoption across our 400-person hedge fund reflects our AI-first mindset: we expect everyone to constantly rethink how they work, always asking 'How can AI help me do this?'—whether or not they're in a traditionally technical role.
>
> Will England  
> CEO & CIO, Walleye

> Claude for Excel powered by Claude Opus 4.6 represents a significant leap forward. From due diligence to financial modeling, it’s proving to be a remarkably powerful tool for our team - taking unstructured data and intelligently working with minimal prompting to meaningfully automate complex analysis. It’s an excellent example of AI augmenting investment professionals’ capabilities in tangible, time-saving ways.
>
> Lloyd Hilton  
> Head of Hg Catalyst, Hg

> Agents in risk workflows must understand who they’re dealing with. Bringing Dun & Bradstreet's Commercial Graph and D-U-N-S® Number, the global standard for business identity, into Claude ensures AI agents operate on verified data and deliver the deterministic, auditable outcomes financial workflows require.
>
> Gary Koveats  
> Chief Data and Analytics Officer, Dun & Bradstreet

> Investors need AI they can trust — and trust starts with the data behind it. Morningstar and PitchBook bring decades of independent, analyst-backed intelligence to Claude, so users aren't just getting faster answers. They're getting better ones. Together, we're building the intelligence layer that powers smarter decisions across public and private markets.
>
> Adam Wheat  
> Chief Technology Officer and Head of Data & Research Solutions, Morningstar

> Our clients — institutional investors, asset managers, hedge funds, and banks — increasingly want to run AI-assisted workflows directly against select sets of FactSet data. Partnering with Anthropic lets us bring Claude into a hosted programmatic environment where they can reason over our foundational market data, research, and analytics in the tools they already use. Internally, firm-wide Claude Code adoption across our engineering org is accelerating how quickly we can ship those capabilities.
>
> Kate Stepp  
> Chief AI Officer, FactSet

01 / 11

## Getting started

Our new Claude agents are available today at our [financial services marketplace](https://github.com/anthropics/financial-services). They can be used as plugins in Claude Cowork or Claude Code on all paid plans, or as Managed Agents in the Claude Platform (in public beta) for programmatic use. The new connectors and Moody’s MCP app are also available to joint customers on paid plans.

The Claude for Excel, PowerPoint, and Word add-ins are generally available, and Claude for Outlook is coming soon.

To see these capabilities in action, you can register for our [livestreamed keynote](https://www.anthropic.com/events/the-briefing-financial-services-virtual-event), and [hands-on webinar](https://www.anthropic.com/webinars/claude-for-financial-services-putting-agents-to-work) which will provide deeper practical adoption guidance. For additional support, [contact our sales team](https://claude.com/contact-sales/financial-services), and learn more about [our solutions for financial services](../18-Industry-UseCases/finance.md).


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
