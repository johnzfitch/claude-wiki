---
title: "AirOps Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/airops"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:27Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# AirOps doubles team productivity and ships agents in weeks with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Enterprise](enterprise.md)

Location:  
North America

2x productivity across the team

Internal consensus from org-wide Claude Enterprise and Claude Code adoption

Prototype to production in weeks

Agent SDK eliminated orchestration overhead, accelerating development velocity

[AirOps](https://www.airops.com/) helps marketing teams at Ramp, Kayak, Chime, Carta, and Rippling understand how their brand shows up in AI search and create content to win more visibility. Claude powers both sides of the platform—generating long-form content that meets a rigorous quality bar, and evaluating it before it ships. AirOps works with customers to measure AI visibility, find high-impact content opportunities, and produce outputs at scale. In the last year, AirOps 5x'd its revenue and doubled internal productivity, with engineering moving from prototype to production in weeks after adopting the Claude Agent SDK.

## With Claude, AirOps achieved:

- 2x productivity across the team, with individual employees reporting 20 to 40 hours saved per week through Claude Enterprise and Claude Code
- Org-wide adoption of Claude, including Claude Code for building internal tools and apps, shared design system skills, and Claude Enterprise as the daily operating environment across marketing, sales, and engineering
- Prototype-to-production timelines compressed from months to weeks after adopting the Agent SDK
- Measurable results for customers using the AirOps platform, including a 3x citation rate increase and 89% time reduction in content creation for Chime, and a 300% content velocity increase for Carta

## The challenge

## Balancing creativity, accuracy, and performance at scale

Great content needs to reflect a brand's voice, deliver genuine information gain for readers, and perform well in search to reach its intended audience. Most models struggle to hold all three requirements at once, and often fall short on quality or perform inconsistently as prompts grow more complex.

AirOps scores every piece of content against dozens of checks before it publishes: paragraph structure, source citations, whether the core answer appears in the first 150 words. The platform needed a model that could handle both sides: generating content that met these standards and evaluating content against them before publication.

"There is always a healthy tension in great organic content," Alex Halliday, AirOps CEO, explained. "It needs to be a balance between brand, performance, and information gain. Most models fail to strike that balance, either struggling with creativity or instruction adherence."

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## The solution

## Selecting Claude for voice consistency and coherence

AirOps benchmarks models against an internal quality framework that balances structure, accuracy, information gain, and discoverability. Claude consistently scored highest on the dimensions that matter most for marketing content.

"Opus consistently outperformed on what matters for marketing: natural writing, instruction following, and voice consistency across long-form content," Halliday said. "The team also found that Claude reliably handled complex requirements without losing coherence. That's a key factor for content workflows where a single generation step might involve brand voice guidelines, SEO constraints, competitive positioning, and factual grounding simultaneously."

AirOps also uses Opus and Sonnet models to help design and configure content workflows for customers within their platform.

## Building an agent runtime on Claude

Claude runs through AirOps as both the engine powering customer agents and as the tool the AirOps team uses to build and ship.

The workflow builder that powered AirOps' early customer results required a human to identify which page was underperforming, decide what to do, trigger the workflow, and verify the output. That works when you're updating dozens of pages, but most teams need to scale to thousands of pieces of content across multiple brands, channels, and competitive contexts that shift daily.

To help teams meet that scale, AirOps' product shifted from workflow tool to agent runtime, built on Claude and the Claude Agent SDK. AirOps started with Claude's API for content workflows, then adopted the Agent SDK to push further. AirOps agents use "playbooks": execution instructions that give agents dynamic, adaptive behavior. Claude interprets the playbook, decides which AirOps tools to call, and executes across sections rather than following a rigid sequence. Sub-agents from the SDK handle specific subtasks like research, drafting, and evaluation with isolated context windows.

"Sub-agents are a must-have for managing the context window," Halliday noted. "Context management has been the single biggest thing that improved our quality."

Hooks let them add determinism and validation at specific points in a workflow while keeping autonomous behavior elsewhere.

On top of the SDK, AirOps built a governed environment that controls what the agent knows, how it plans, what it can act on via MCP, what brand and quality rules it follows, and how it coordinates with other agents and humans.

"Prompts are portable," Halliday explained. "Any team can copy a good prompt. The harness that governs how agents operate, the brand context they draw from, and the decision history they accumulate? That provides compounding value to customers."

AirOps went from initial SDK prototype to production in weeks. "Previous orchestration frameworks were brittle. Setup decisions sometimes required full refactors, and testing different configurations took enormous effort," Halliday said. "Development with the SDK was straightforward and more powerful. Time to quality went from 60 hours to 5 hours."

The SDK also changed how the engineering team spends its time. The team now spends that reclaimed time refining outputs and catching edge cases before customers hit them.

"Before, we spent a lot of time rerouting LLM calls, updating schemas, and dealing with orchestration configurations whenever we made changes," Halliday said. "Now we focus on output quality and the human-to-agent experience."

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

[Read more](https://claude.com/blog/skills)

## The outcome

## 2x productivity and a new way of working

When AirOps polled their team on Claude's impact, the responses were specific. One team member reported completing two weeks of work in one week. Another described spending 15 to 20 hours per week in Claude Enterprise alone, plus 40 hours weekly in Claude Code. The consensus across the team was a 2x increase in productivity, with individual savings ranging from 20 to 40 hours per week.

Internally, AirOps built an org-wide skill that encompasses their full visual and web design system. Any team member can now generate on-brand assets, slide decks, and one-pagers without filing a design ticket. The AirOps MCP connector gives every employee direct access to brand voice and visual guidelines, product knowledge, and knowledge base content during creation. Infrastructure that would have taken months to build manually was embedded in daily workflows within a single quarter.

For customers on the AirOps platform, Chime saw a 3x citation increase with a 89% time reduction in content creation. Carta 4x'd quarterly top-of-funnel output (5 to 20 articles) with a 75% citation rate on AirOps-built pages. LegalZoom cut Reddit response workflows from 48 hours to under 30 minutes.

## Looking ahead

AirOps' agent runtime is currently in alpha with customers including Ramp, Carta, Klaviyo, LegalZoom, Xero, Vanta, and AssemblyAI, with general availability planned for May 2026. AirOps is building toward a future where their agents move from surfacing gaps in AI search visibility to acting on them autonomously, with the right human checkpoints built in.

"We're building toward a world where an agent identifies an underperforming page, drafts updated content grounded in brand voice, and publishes it, with a human only needing to confirm strategy and provide edits when needed," Halliday added. "Claude is central to that vision."

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

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
