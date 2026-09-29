---
title: "Duvo Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/duvo"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:31Z"
tags: ["agents", "enterprise", "sdk", "security"]
---

# Duvo automates enterprise operations across legacy systems with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
Claude Platform

Location:  
EMEA

€2.8M+ in annualized savings

captured in three months for one multi-billion-euro retailer

Eight weeks from first conversation to production deployment

with measured savings, on average

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

[Duvo](https://www.duvo.ai/) builds AI agents that run procurement, supply chain, and category management processes for multi-billion-euro retail and CPG companies. The agents work across every system involved: ERPs, supplier portals, spreadsheets, email, even phone calls. Duvo is built entirely on Claude, using the Agent SDK to orchestrate across workflows, with every API call running under Anthropic's Zero Data Retention mode.

## **With Claude, Duvo achieved:**

- €2.8M+ in annualized savings within three months for its customer Rohlik Group, across processes that had never been systematically run
- Annual supplier negotiations shortened by one month at Rohlik Group, with approximately 80% automated from preparation through contract generation to ERP write-back
- 40%+ of team capacity freed up on average across enterprise procurement, supply chain, and retail operations by reducing manual work
- Eight weeks on average from first conversation to production deployment with measured savings
- Production deployment within days of adopting the Claude Agent SDK

## **The challenge: The cost of "abandoned work" in enterprise operations**

Duvo's customers have operations teams that know exactly what needs to happen but can't get to all of it. Buyers manage ordering across SAP, supplier portals, and email. Category managers track commodity prices in spreadsheets they built themselves. Procurement coordinators chase confirmations by copying status between systems. These teams cover the top 20 suppliers and the most urgent issues. But the long tail, hundreds of smaller actions worth millions in aggregate, never get touched.

"The real process lives in people's heads: which supplier needs chasing, which portal field actually matters, which exception to escalate and which to just fix," said Marek Paris, co-founder and CPTO at Duvo. “The reason no one has automated these processes before is that the work crosses too many systems.”

The blocker isn't a missing dashboard. The work spans systems that don't connect, and no two companies use the same stack. Traditional automation stalls because there are no clean APIs, the IT backlog is years long, and every exception requires judgment. Duvo calls this "abandoned work": processes worth millions that nobody runs because there aren't enough hours in the day.

## **The solution: Selecting Claude for messy, multi-step work**

After evaluating multiple model providers, Duvo committed to a single-provider architecture on Claude. The product defaults to Sonnet 4.6, with browser-use agents often using Opus 4.6.

"What set Claude apart was its performance on messy, ambiguous tasks," explained Tomas Čupr, co-founder and CEO. "Parsing a supplier email that half-confirms a delivery while raising a pricing dispute. Navigating a SAP GUI screen with dozens of fields. Making judgment calls on exceptions without hallucinating business rules."

Two factors cemented the decision: First, the model’s reasoning depth was especially strong for multi-step work. Second, the developer tooling then closed the gap. MCP, the Agent SDK, and computer use gave Duvo a complete foundation for running agents in production, with structured human-in-the-loop workflows and Zero Data Retention on every API call. Building on a single provider's stack meant fewer integration seams and a consistent security model across every agent run. "Other providers offer a model. Anthropic offers the infrastructure to run agents in production with the governance enterprises require," Paris said. "When we saw all of these working together, with Claude's model quality as the foundation, going all-in was straightforward.”

## **Agents that cross every system boundary**

Duvo's agents operate these systems through their actual interfaces, not through APIs that may not exist. "Claude's computer use and MCP integrations are what made this technically possible," said Ondrej Romancov, Head of Product Engineering. "Before that, the heterogeneity of enterprise stacks was an unsolvable problem for automation."

A single agent run might log into a supplier portal, extract delivery status for 50 purchase orders, cross-reference against SAP, identify discrepancies, check contract terms, decide whether to escalate or auto-correct, send follow-up emails, and log the outcome—all in one session.

"Before the SDK, critical context disappeared between agent handovers," Romancov said. "Now we run one capable agent per job with access to all the tools it needs. Context stays intact across the entire operation."

High-risk actions require human approval. When a human responds, the agent persists that decision for future runs. Over time, the system accumulates the operational judgment that used to exist only in people's heads.

## **The outcome: Recovering millions in abandoned work**

The results from Rohlik Group, Europe's leading online grocer with more than €1.5 billion in revenue, illustrate what becomes possible. The retailer tracks thousands of commodity-linked SKUs across five markets. Before Duvo, this happened quarterly at best, often not at all. Duvo now monitors continuously, builds negotiation cases, and initiates supplier outreach. The result: €1.45M in annualized savings in the first week, from continuous price monitoring and automated supplier outreach across 120+ SKUs and 15+ suppliers. Not from a process that was slow, but from one the company had never been able to run. "This is the clearest example of 'abandoned work' becoming real value," Paris said.

“That was one process,” said Olin Novák, CRO at Rohlik Group. “We're now running dozens." Across three months, that number grew to €2.8M+ in annualized savings.

Across other Rohlik workflows, promotional setup dropped 65-70%, supplier onboarding chasing fell 50-70%, and supply chain planning moved product availability from 78% to 93% in two weeks. “Not because someone built an integration,” Paris said. “Duvo works through the same screens the team was using. It just doesn't forget, doesn't deprioritize, and doesn't stop at the top 20 suppliers.” Annual supplier negotiations shortened by one month, with approximately 80% of the process automated. Inbound delivery confirmations jumped from 52% to 90%, covering every supplier daily.

With routine execution handled, operations teams can focus on the work their expertise was built for: supplier negotiations, exception strategy, cost optimization, and the judgment calls that require institutional knowledge.

Expansion within accounts happens naturally. Automated ordering surfaces supplier lead-time issues that the returns team can act on. Cost monitoring reveals pricing discrepancies that ordering can prevent upstream. On average, Duvo moves from first conversation to production deployment with measured savings in eight weeks. The team also estimates that 40% of team capacity is freed up on average across enterprise procurement, supply chain, and retail operations by reducing manual work.

Duvo is doubling down on retail and CPG, with manufacturing and logistics next. "There are dozens of high-value operational processes in this industry that have never had a proper system of action," Paris said. "We wanted to close that gap between knowing what should happen and actually making it happen. Across every transaction, every supplier, every system."

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

[](/)

© 2026 Anthropic PBC

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](https://www.anthropic.com/research)
- [Anthropic news](https://www.anthropic.com/news)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
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

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
