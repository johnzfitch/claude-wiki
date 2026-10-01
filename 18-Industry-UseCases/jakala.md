---
title: "JAKALA Claude case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/jakala"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:33:37Z"
tags: ["agents", "case-studies", "enterprise", "security"]
---

# JAKALA brings production AI agents to enterprise clients across Europe with Claude

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Large

Product:  
Claude Agent SDK

Location:  
EMEA

~70% reduction in time spent

on systematic and repetitive tasks across senior delivery teams

\<24 hours campaign-optimization cycle

on accounts running the hybrid agent model, down from 5-7 days

[JAKALA](https://www.jakala.com/en-us/) is a data and AI company headquartered in Milan, with more than 3,600 people across 30+ countries, serving clients in banking, insurance, luxury hospitality, telco, cruise, and education. The company’s flagship offering is an integrated delivery model—the AI Factory—that combines proprietary data infrastructure, in-house AI products, and production agents into a single governed engagement. Claude is the reasoning engine: it runs across 3,000+ employee seats and inside the production agents JAKALA deploys in client environments.

## With Claude, JAKALA achieved:

- Under 24-hour campaign-optimization cycles on accounts running the hybrid agent model, down from 5–7 working days.
- ~70% of senior team time redirected from data assembly, reporting, and other systematic work to higher-judgment client work.
- ~30% uplift in overall team productivity, with senior strategists now spending the majority of their time on strategic and advisory work.
- 35–40% increase in client satisfaction scores on hybrid-managed accounts, measured through structured client feedback cycles.
- Production agents shipping into client environments in weeks, down from a quarter for the first agent.
- 3,000+ Claude seats spanning data scientists, AI consultants, planners, platform engineers, and corporate functions.

## The challenge

## Industrializing AI delivery across regulated European industries

For more than a decade, JAKALA had been developing hundreds of AI/ML models in-house, including propensity models, segmentation, marketing mix modeling, geospatial analytics, and recommendation systems. To scale that work into a single repeatable delivery model across regulated industries, the company needed a reasoning engine that enterprise customers could trust. "The bottleneck was not model availability," said Marco Di Dio Roccazzella, Global Managing Director of JAKALA's Data and AI Business Line. "It was model trustworthiness inside multi-step agentic workflows at enterprise scale."

External pressures compounded the internal one. Generative AI engines were displacing traditional search as the way customers find brands, and JAKALA’s clients had no established way to measure brand visibility inside those AI engines. At the same time, the economics of labor intensive delivery were tightening. "If we did not evolve our delivery model from labor-intensive execution to AI-augmented service, our ability to keep investing in higher-value work for clients would erode," said Amedeo Guffanti, Global Managing Director of JAKALA's Activation Business Line.

These pressures showed up most concretely inside JAKALA's Activation business, which runs media, campaign, and engagement delivery for global clients. Senior planners on multi-market accounts were spending 40 to 60 percent of the week assembling data, building reports, and stress-testing hypotheses rather than making decisions. A complete optimization loop on a complex multi-channel account took 5 to 7 working days, including pulling data from 8 to 12 systems, hand-consolidating it in business intelligence tools, running scenarios, building a deck, and presenting it to the client. Each iteration set the upper limit on how fast ROI could improve. JAKALA wanted that time spent on client decisions instead.

Claude on Google Cloud

Build advanced AI agents with Claude on Google Cloud.

[Read more](../04-API-Reference/Other/partners-google-cloud.md)

## The solution

## A reasoning core for the AI Factory

JAKALA evaluated leading frontier models against representative workloads: documents and prompts running up to 200,000 tokens, multi-step agents that needed to call JAKALA's internal APIs, and synthesis work where the model had to nail tone, factual accuracy, and auditability simultaneously.

"The question was never which model wins," said Di Dio Roccazzella. "It was which model becomes the reasoning core of the AI Factory." The team graded each candidate on factual reliability, instruction-following across long agentic chains, latency and cost per task, and what they called "safe failure": whether the model would admit uncertainty rather than fabricate an answer.

Three factors tipped the decision toward Claude. First, Claude reasoned well over the long, messy inputs that defined real client data across JAKALA's verticals. Second, the team saw markedly more consistent behavior from Claude inside the multi-step, tool-calling workflows production agents required. Third, Claude's safety and steerability posture matched the bar regulated clients set. "Claude refuses cleanly, asks for clarification rather than guessing, and is auditable in the way our regulated clients in banking, insurance, and telco genuinely require," said Di Dio Roccazzella.

For Guffanti, the moment of conviction was more concrete. JAKALA had set several frontier models the same assignment: handle a full week's media-performance analysis for a luxury cruise client, end-to-end, including tool calls into JAKALA's geo-intelligence engine. Only Claude's output cleared the senior strategy directors without revisions. "That was the signal," Guffanti recalled. "We were no longer talking about a generative tool. We were talking about a colleague."

Today Claude runs across the company on two tracks. The productivity layer is [Claude Enterprise](enterprise.md), deployed to more than 3,000 employees including data scientists, AI consultants, planners, platform engineers, and corporate functions. The production layer is a network of agents built on the Claude Agent SDK, with Claude Opus 4.6 for the most demanding analytical work, Claude Sonnet 4.6 as the default for agentic workflows, and Claude Haiku 4.5 for high-volume, latency-sensitive steps.

Each major client account runs a network of specialized Performance Agents covering search and shopping, programmatic, social platforms, creative-asset diagnostics, and incrementality reads. Each agent connects via MCP to the client's ad accounts and to JAKALA's geo-intelligence engine, reasons across the combined data, flags anomalies, and proposes specific actions. A human pod handles review, approval, and execution. "The agents do not replace planners," Guffanti explained. "They turn every planner into a senior planner."

Two proprietary products sit on this stack. JHexagon uses Claude Opus 4.6 to reason over multi-channel signals and 400+ external data sources, recommending how clients should allocate marketing spend at the micro-territory level. JHorizon measures how visible client brands are inside generative AI engines, producing a Findability Index that clients use as a recurring KPI.

JAKALA accesses Claude through whichever surface matches each client's infrastructure: Claude on Amazon Bedrock, Claude on Google Cloud Agent Platform, or the Claude Platform directly with the API. "Most of our enterprise clients have already settled their AI procurement, security review, and data-governance frameworks around AWS or GCP," said Di Dio Roccazzella. "Going through Bedrock or Google’s Agent Platform meant we inherited those controls. In regulated verticals, this collapsed a process that historically took months into weeks."

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The outcome

## Production agents shipping in weeks

On client accounts running JAKALA's hybrid agent model, the shift was immediate and measurable. The campaign-optimization cycle compressed from 5 to 7 working days to under 24 hours. Overall team productivity is up about 30 percent. Roughly 70 percent of the senior time previously spent on data assembly, reporting, and status documentation moved to strategic and advisory work. Client satisfaction scores on those accounts rose 35 to 40 percent.

What changes inside accounts is the texture of the conversation. "The conversation with a CMO is no longer 'when will we have the analysis?'" said Guffanti. "It is 'the analysis is here, what do we want to do?'" One luxury-cruise account described the new dynamic as "the feeling that our agency suddenly has the same operational tempo as our revenue management team."

Inside JAKALA itself, the heaviest Claude users turned out to be directors and partners, not junior staff. The agents were absorbing the assembly work, so the value concentrated where senior expertise has the most impact: client strategy, advisory, and direction. Teams who initially feared automation became its strongest advocates, Guffanti added, "once they saw the shift in repetitive work translating into more interesting assignments, not fewer assignments."

The agent deployment process matured fast. JAKALA's first production agent took about a quarter to go from design to live client deployment. The second was half that. By the fifth iteration, the team had a repeatable pattern that now ships new production agents into client environments in weeks.

Beyond marketing activation, JAKALA has begun extending the AI Factory model into Ardian's private equity operations, applying Claude to due diligence and portfolio company management workflows, with adoption now underway at additional European PE firms.

"AI at JAKALA is not a pilot anymore," said Di Dio Roccazzella. "It is the default operating mode of the company. The roadmap is not about adding more AI to JAKALA. It is about making the AI Factory the reference operating model for enterprise AI transformation in Europe."

## Related stories


### Caylent turns months of migration work into days with Claude Agent SDK


### How can a two-person fabrication studio make room for problems it’s never solved before?


### LG CNS modernizes 20-year-old enterprise systems with Claude


### How Blank Metal, a lean professional services firm, runs on Claude Cowork

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
