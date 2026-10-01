---
title: "Mutiny Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/mutiny"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:53Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# How Mutiny gives every seller a full creative team with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
Claude Platform

Location:  
North America

3x improvement in design satisfaction

since making Claude Opus the default model

4.5x faster asset creation

for sales teams compared to previous workflows

[Mutiny](https://www.mutinyhq.com/) helps GTM teams create the customer-facing assets they need to generate pipeline and close deals: personalized pitch decks, deal rooms, and business cases, generated in the customer's own brand. Instead of waiting on marketing or design, sales reps describe what they need and Mutiny's AI agents build it.

## With Claude, Mutiny:

- Measured a 3x improvement in design satisfaction since making Claude Opus the default model, based on in-app user feedback
- Cut asset creation time by 4.5x for sales teams using Mutiny, compared to previous workflows
- Saw 9 out of 10 sales reps using Mutiny report the product gives them an edge in competitive deals
- Generates fully branded assets in a single shot from just a website URL
- Re-architected its entire creation experience from constrained, task-specific AI to an agent-first platform

## The challenge

## Isolated AI capabilities with no way to combine them

Mutiny began integrating large language models in 2022. But those early implementations were constrained. AI could pull styling from a website, generate text variations for different target companies, and conduct basic research. But each task needed well-defined guardrails, and combining them in new ways wasn't possible.

The arrival of Claude Opus 4 changed what Mutiny decided to build. "We really saw an opportunity to re-architect the whole system and make this a very agent-first experience,” said Nikhil Mathew, Co-founder and CTO of Mutiny. “The agent is now multimodal and has tool-based access to do research, build the brand, and design the entire experience.”

Introducing Claude Opus 4.7

Opus 4.7 is a notable improvement on Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks.

[Read more](../19-Reference/claude-opus-4-7.md)

## The solution

## Quantifying taste: How Mutiny evaluated Claude

Choosing the right model for creative output meant solving an unusual evaluation problem: how do you quantify design taste? Mutiny built a two-part internal benchmark. The first part measured tool-call accuracy. The second, and more important, was a creative evaluation. "We take screenshots of the output and provide those to a different LLM to judge how well the user's original intent was captured and whether the output embodied the brand," Mathew explained.

The team scored outputs across multiple axes: brand alignment, typography, color usage, imagery, layout, and whether the output avoided common design tropes. They use vision capabilities to objectively measure brand quality across those axes, a process they still rely on as they iterate. The tipping point came during a weekend of testing. Mutiny had been refining its system prompt with Anthropic's team, drawing on techniques from Anthropic's frontend design research to steer Claude past its default design patterns toward more varied, distinctive output.

“It was the highest benchmark we had achieved on our internal design eval," Mathew said. "That was a visceral moment where not only are we seeing high-quality outputs, but a much wider range of those outputs as well, which made it a very valuable part of our product experience."

The result was an agent that could, as Mathew described it, "produce a wide range of well designed outputs on the first try." Reaching that point required more than a model swap. The team rebuilt its core creation experience around an LLM-native data model, aligning to coding principles and frameworks like Tailwind that Claude performs well on, so the agent could make visual decisions independently.

For Jaleh Rezaei, CEO and Co-founder of Mutiny, the upgrade was an inflection point. "Once we put in Opus, the product worked," she said. "It enabled us to have a public launch."

## Three agents, one brand

Mutiny's architecture splits the work across three specialized agents, each powered by Claude Opus 4.7. The Brand Agent operates against a live browser to understand a customer's website and build a taxonomy of their visual identity: fonts, button styles, color palettes, spacing, and what Mathew called "the feel of the brand." The team’s goal was “to make it so anybody could onboard to Mutiny and within minutes create something in their brand," he said.

The Research Agent and Creative Agent work in tandem. When a sales rep wants to build a pitch deck for a specific prospect, the Creative Agent dispatches the Research Agent to pull context from CRM data, past call transcripts, and previous interactions. That research flows back into the Creative Agent's context alongside the brand taxonomy, and the result is an asset that is visually on-brand and tailored to the prospect's specific priorities.

Customer feedback reflects the difference. "When they see our product, they're like, this is something I'm proud to put in front of my customer,” Rezaei said.

The architecture also emphasizes human-agent collaboration. "Everything the agent generates is a hundred percent editable in the browser. It can stream in real time, and it's fully multiplayer," Mathew noted. "You can have multiple people and agents working together in the same workspace."

## The outcome

## 3x design satisfaction

Since making Claude Opus the default model in late January 2026, Mutiny has measured a 3x improvement in design satisfaction through in-app asset quality ratings. In early customer surveys, users say the product is 4.5x faster for creating sales assets. Nine out of 10 sales reps also said Mutiny gives them an edge in competitive deals. Every respondent rated Mutiny's design quality as meeting or exceeding the bar set by their own designers.

The product quality translated directly into business traction: since launch, Mutiny's monthly recurring revenue (MRR) has grown 120% week over week. "Opus is what allowed us to connect all of those dots," Mathew added. "Being able to one-shot assets in your visual language is what opens up the next level of automation."

That next step is proactive preparation: generating the right materials before the rep even opens the app. "The next piece is to actually create those for you automatically,” Mathew added, “so that they're just prepared for you when you need them.”

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
