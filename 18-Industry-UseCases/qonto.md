---
title: "Qonto Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/qonto"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:43Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# How Qonto delegates financial admin for small businesses with Claude on Amazon Bedrock

Industry:  
Financial services

Company size:  
Medium

Product:  
[Claude Platform](https://claude.com/platform/api)

Partner:  
AWS

Location:  
EMEA

2X faster bank transfers

with no manual beneficiary search, amount entry, or reference copying

3X less time to create client invoices

with Qonto's AI agents drafting them and the customer confirming before they're sent

More than 600,000 businesses across eight European markets run their banking and bookkeeping on [Qonto](https://qonto.com/en). In late 2025, its 15-person AI Lab built agents into the app to take over the repetitive parts of that work: preparing payroll transfers, drafting invoices, answering questions about the numbers. The agents' most complex work runs on Claude.

## **With Claude, Qonto:**

- Sends bank transfers 2X faster, with no manual beneficiary search, amount entry, or reference copying, then waits for the customer's final approval before the money moves
- Cuts client invoice creation time 3X, with its AI agents drafting every invoice and the customer confirming before it's sent
- Runs payroll 5X quicker: agents prepare every pay slip, the customer approves before anything sends, and a 15-to-20-slip run becomes one drag-and-drop bulk transfer
- Sees customers delegate transfers as large as €100,000 to Qonto AI agents, with the final approval always theirs by design
- Generated one customer's 500-plus monthly invoices in a single batch

## The challenge

## **Admin remains the hidden tax**

Qonto's customers run their own businesses: solopreneurs, freelancers, newly created companies, and small teams. Few have a finance team behind them, and financial admin has become a hidden tax on their time: they spend on average up to 8 hours every month on financial admin tasks. "They are not finance experts and they don't want to be," said Sophie Cornay, Business Unit Manager, AI Lab. "The manual, repetitive part of managing their finances takes too much time away from running the business."

Before Qonto launched its agents, using the platform meant learning it: finding the right action at the right time, then doing the work manually. An owner running payroll ended each month with 15 or 20 pay slips and made one manual transfer per slip, attaching each for the accountant. Invoicing worked the same way: client lists lived in a CRM or spreadsheet, and each invoice was re-keyed into Qonto one at a time.

"When you do one transfer, it's okay, it's a few minutes, everyone can manage," Cornay explained. "When you have 10 transfers to do, that's where the repetitive aspect of the task starts to be a big pain. It's not only the action, it's the volume of actions." That volume cost customers up to 8 hours each month, according to Forrester’s analysis for Qonto’s customers. The other loss was insight: with no finance expertise in-house, cash flow lived in hand-built spreadsheets while account data went unused for decisions.

## The solution

## **A compliance-first path to Claude**

Agents that take over that work have to operate inside customers' bank accounts, touching real money and real financial data. That set a bar most software never faces. “Since we are a financial institution, we need to work with providers that are compliant,” Cornay said. “Security is the foundational layer, and then it's about performance.”

Performance meant how well a model does the agents' actual jobs: pulling accurate answers out of a customer's transaction data, calling Qonto's systems to prepare a transfer or draft an invoice, and responding fast enough for an in-app conversation. Qonto routes by complexity: routing each step to the right model on latency, performance, and cost. The agents' complex missions run on Claude Opus 4.5 and Sonnet, while simpler steps go to smaller models, including Haiku. Access runs through Amazon Bedrock, with GDPR and EU AI Act compliance handled at the provider level. Claude also stood out for how well it integrates with Amazon Bedrock, from structured outputs and prompt caching to quota management. Every new release triggers fresh evals so each use case stays on the best model.

None of that rigor slowed the build: the project started in November 2025 and the first agent released six weeks later with several thousand beta customers. Cornay credits that speed partly to Qonto's legal, risk, and security teams co-building the solution. The lab itself runs on Claude internally too: engineers work in Claude Code daily; product and design teammates live mainly in Claude Cowork, along with Claude Design.

## **An operator for the busywork, an analyst for the insight**

The lab aimed Claude at two goals for users: save them time on admin and finance tasks, and turn their Qonto data into insight. Each goal became an agent that lives in the Qonto app and runs on Claude.

The operator agent takes the high-frequency work, routing each request to a specialized agent scoped to that task, which handles it end to end. A customer running payroll drags 15 or 20 pay slips into Qonto; the agent prepares them all in what Qonto calls a bulk transfer, ready for one final review before everything sends. The same flow covers invoicing: drop in a CSV of clients and the operator agent drafts every invoice, right customer, right amount.

The analyst answers questions about past and present transactions. "From a single conversation, one of our users was able to rebuild four years of cash flow," said Allison Pianpanya, Staff Product Marketing Manager for the AI Lab. "He identified tax credits, categorized grants, and got a detailed breakdown of his expenses without even opening a spreadsheet."

Beyond the agents Qonto builds, its Model Context Protocol (MCP) server lets customers connect their own Qonto data to Claude directly and build their own tools. Some have made subscription-audit dashboards to cut what they don't use; within weeks of launch, one user pulled his transactions, balances, labels, and invoices into Claude, sorted flows across eleven business categories, and built live cash, burn, and runway indicators. "This morning I was on a call with a user who told me: I do a meeting, the meeting transcript is sent directly to Claude, and based on the transcript it creates a quote on Qonto, sent directly to my client," Cornay added.

All of these flows touch money. "Regulation is our moat,” Cornay said. “From day one, control, transparency and trust were built-in by design. We have always believed that the agent can prepare, the agent can recommend, the agent can give the insights, but the user makes the decision. AI doesn't reduce responsibility, it changes where it sits."

Any action with a financial or customer relationship impact requires user confirmation. The review screen shows just enough to approve a transfer or judge whether an insight's data is accurate. On the most sensitive use cases, deterministic checks sit alongside the model in the architecture.

## The outcome

## **When customers trust, they delegate**

Transfers now get sent 2x faster: the user uploads an invoice and the operator agent does the rest, with no beneficiary search, no amount entry, no reference copying. Client invoices take 3x less time to create, drafted by the agents and confirmed by the customer before sending. One pattern surfaced across users: they never had to learn the platform first. The onboarding barrier, as Pianpanya put it, "is disappearing entirely."

"Users need to trust your agent,” Cornay said. “Otherwise they don't delegate, and the value is when they start delegating. We were quite surprised to see transfers of 100,000 euros with agents. We were thinking maybe people would start with a very low amount, and no: when they trust, they just do it."

One solo entrepreneur hands over two or three new clients a day; the operator agent does client creation and invoice drafting in one go, giving him back half a day of admin every month. Another manages 500-plus invoices a month for 550 clients. He tried the operator on his whole billing file to see if it could produce the batch in one shot. It could. He's now weighing moving his entire client base to Qonto.

Banking reconciliation, one of customers' most painful tasks, is next on the roadmap. The medium-term ambition changes who starts the conversation. "The next step is moving to proactivity," Cornay said. "We start to pull the user when their attention is required, when there is an alert, versus having the user go into the app to perform tasks. This, we believe, at some point may disappear."

## Related stories


### Pictet turns weeks of work into hours with Claude Code


### How Satispay's engineers write 75% of their code with Claude


### OffDeal powers every stage of M&A advisory with one Claude-based agent


### Money Forward builds an AI-native engineering organization with Claude Code

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
