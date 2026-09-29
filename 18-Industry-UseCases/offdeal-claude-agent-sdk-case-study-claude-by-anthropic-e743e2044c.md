---
title: "OffDeal Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/offdeal"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:40Z"
tags: ["agents", "enterprise", "sdk", "security", "subagents"]
---

# OffDeal powers every stage of M&A advisory with one Claude-based agent

[Try Claude](https://claude.ai)

Industry:  
Financial services

Company size:  
Small

Product:  
Claude Agent SDK[Claude Platform](https://claude.com/platform/api)

Location:  
North America

25% to 85% internal eval accuracy

after migrating to the Claude Agent SDK and refining MCP design and prompting

5 to 8 concurrent deals managed by each banker,

with AI handling work across every phase of the deal lifecycle

[OffDeal](https://offdeal.io/) is an AI-native investment bank that helps founder-led businesses sell their companies. By pairing bankers with software engineers, the firm brings full-service M&A advisory to businesses making \$1 to \$20 million in annual profit, the largest segment of the market by deal count but historically the least served.

## With Claude, OffDeal:

- Increased eval accuracy from 25% to 85% after switching to the Claude Agent SDK and iterating on MCP design and prompting
- Dropped failed API calls from context overflow to zero overnight
- Consolidated 12+ independent agentic workflows into a single general-purpose agent, Archie
- Achieved 5 to 8 concurrent deals managed by each banker, with AI handling work across every phase of the deal lifecycle
- Built a buyer sourcing agent that runs autonomously for up to 4 hours, researching potential acquirers across 10 different sourcing methods
- Equipped each banker to meet 2 to 3 new potential clients per day, supported by AI-generated prep and materials
- Closed 8 deals totaling \$91M in transaction value in the firm’s first year, with a team of two bankers

## The challenge

## Context, not intelligence, as the bottleneck

OffDeal uses AI across virtually every stage of a deal, from originating new clients to finding buyers, preparing materials, and running diligence. "I think we're the only investment bank in the world that has more engineers than bankers," said Ori Eldarov, CEO and founder at OffDeal. "We have 5 engineers and 4 bankers right now." Before the Claude Agent SDK, each of these workstreams ran on its own dedicated agentic workflow: one for building seller lists, another for buyer lists, another for creating confidential investment memorandums, and so on.

"Each individual API call was smart,” Eldarov explained. “But because we had to define the best way to solve a certain problem in advance, if we came across a problem outside the predefined instructions, the models did very poorly." The brittleness compounded with scale: OffDeal was growing fast, and every time a standard operating procedure changed, the corresponding workflow broke.

But the deepest constraint was context. A single deal can involve more than a hundred million tokens of relevant information: buyer profiles, past transactions, financial documents, market data. "The gap was coming not from the model intelligence, but from context, lack of context," Eldarov said. The team had been using a long-context model from another provider, packing the full context into each call to preserve accuracy over RAG. That approach worked until they hit the million-token limit, at which point API calls simply failed.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## The solution

## Claude Agent SDK for subagent orchestration

The team started investigating solutions: custom compaction, auto-summarization, and structured note-taking. Then they came across an early blog post about the Claude Agent SDK. "It seems like this is a solved problem with coding when you're traversing super large codebases," Eldarov noted. "How different is really traversing a bunch of files on different buyers from that?"

The Agent SDK's built-in context management, including subagent orchestration and automatic compaction, meant the team could stop building workarounds and focus on banking workflows.

## One agent across the entire deal lifecycle

Since December, OffDeal has consolidated nearly all of its AI workloads into Archie, a single general-purpose agent built on the Claude Agent SDK. Archie is connected to more than 20 data sources and handles work across every phase of a deal.

Instead of hardcoding each workflow, the team now builds modular capabilities they call "skills," self-contained instructions that Archie can combine and apply flexibly. Take buyer sourcing: finding the right 300 to 400 potential acquirers out of millions of companies and tens of thousands of private equity firms. An experienced banker would typically use roughly 10 different approaches, from checking past deal activity to scanning company websites for active acquisition mandates and current portfolio investments and works across all of them simultaneously, using findings from one to refine another.

OffDeal encoded that expertise into a buyer sourcing skill. A long-running agent now handles the work autonomously for up to 4 hours, researching buyers across all 10 methods, cross-referencing findings, and recursively refining its search with a level of depth and individual vetting that would be difficult to sustain manually across hundreds of candidates. The same buyer list would traditionally take a team of analysts more than a week to assemble and cost upward of \$12,000. The agent produces it for roughly \$200 in compute. And because it can programmatically sweep every permutation of sector, geography, and acquisition history, “it surfaces buyers that a human team would be unlikely to find regardless of time or budget,” Eldarov added.

The skill architecture also opened up iteration to non-engineers. When OffDeal needed branded presentation capabilities, it was a banker, not an engineer, who built the skill. The banker taught Claude the firm's design system: fonts, margins, indentation, and 20 different slide templates. "End-to-end, no engineering was required, and now every banker on the team can use it," Eldarov said. “We’ve created hundreds of decks since then.” Each deck takes about an hour with Archie, compared to the 30 to 40 hours a traditional team would spend on research, production, and review cycles.

Financial services

Accelerate financial due diligence, modeling, and analysis with enterprise-grade AI built for compliance and security.

[Read more](/solutions/financial-services)

## The outcome

## A step change in accuracy and capacity

The impact showed up immediately. Context overflow failures, previously a persistent source of broken workflows, dropped to zero. "We basically never ran out of tokens after that," Eldarov said. "We just stopped getting that error."

With reliability solved, the accuracy gains followed. "Just switching to the SDK moved our score on that eval from 25% to 60%," Eldarov said. "That's a massive climb on an eval, just from switching a few lines of code." The eval is an internal benchmark that scores Archie’s accuracy on complex, multi-part M&A queries executed over real production data, often spanning 10 million to more than 100 million tokens of deal context. Each test case is evaluated against actual deal outcomes and human-verified data. He noted that 60% represents a composite score across complex qualitative and quantitative rubrics, not a simple pass/fail rate. Since then, improvements to MCP design and prompting have pushed the score to 85%.

Each OffDeal banker now manages five to eight concurrent deals and meets two to three new potential clients per day, supported by Archie's ability to rapidly prepare materials and generate analysis. In its first year, the firm closed eight deals totaling \$91M in transaction value with a team of two, in a market where a single deal typically takes 9 to 12 months. In 2026, OffDeal’s average deal size climbed from \$11M to over \$20M. The team can now prototype new capabilities in Claude Code and push them to production almost overnight, because both environments run on the same SDK.

A year in, the new process is working. Businesses that historically couldn’t attract investment banking coverage now get the same rigor of process, from buyer sourcing to deal execution, that was once reserved for much larger transactions. OffDeal plans to expand beyond its current focus on sell-side M&A, adding buy-side advisory, capital raises, and debt origination as it works toward becoming a full-service investment bank. “Effectively, Archie is your deal team,” Eldarov said. “You basically get the hive mind of the firm available to you.”

## Related stories


### How Qonto delegates financial admin for small businesses with Claude on Amazon Bedrock


### Pictet turns weeks of work into hours with Claude Code


### How Satispay's engineers write 75% of their code with Claude


### Money Forward builds an AI-native engineering organization with Claude Code

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
