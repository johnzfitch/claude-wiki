---
title: "Bubble Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/bubble"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:52Z"
tags: ["api", "case-studies", "enterprise", "prompting", "security"]
---

# How Bubble powers an AI agent that turns prompts into production apps with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
North America

~30% increase in user satisfaction

With the Claude-powered AI editing agent, compared to the previous model provider

2x first-week user activation rate

After launching the Claude-powered AI app generator

[Bubble](https://bubble.io/) is a no-code AI app development platform with more than six million users who've built more than seven million web and native mobile apps. Its Claude-powered AI agent builds in Bubble’s visual development language, so users can move between AI chat and visual editing to launch and scale applications.

## With Claude, Bubble:

- Doubled first-week activation rate and first-month retention after launching the Claude-powered AI app generator
- Increased user satisfaction with the AI editing agent by ~30% compared to the previous model provider, with positive feedback rates rising from ~70% to ~90%
- Adopted Claude Code across the majority of the engineering team, with all new hires now onboarded to it on day one
- Reduced inference costs while maintaining app generation quality
- Shipped backlog items previously not worth the effort, including a frontend migration from jQuery to SolidJS

## The challenge

## Closing the gap between first prompt and first app

Bubble has always believed that the best way for non-coders to build apps is to speak to a computer in their language, not in code. But before AI, visual development languages required a significant time investment to learn, and new users often churned before reaching the moment where things clicked.

"The \#1 business challenge we solved was showing value to users faster," said Zachary Tessler, AI Engineering Lead at Bubble. The team started with a page generator, then built a Claude-powered AI app generator that created full working apps from prompts. The results were immediate: first-week activation doubled, and twice as many users were still active at the end of their first month. But generating a complete app in one pass wasn't enough: users needed to iterate on what the generator produced, to move past prototypes into real products. That's why the team built the Bubble AI Agent, a Claude-powered assistant that helps users refine and extend their apps from within the editor.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The solution

## Selecting Claude for reasoning quality

Bubble's team evaluated multiple model providers before choosing Claude, prioritizing reasoning quality, low latency, and user control. "Reasoning quality is a top consideration," Tessler explained. "It helps a user decompose complex and potentially ambiguous requests into discrete actions that address their query." Latency mattered because the agent needed to keep pace with users building apps in real time. And the team wanted users to stay in the driver's seat, with the agent surfacing its plan and letting users approve changes before anything was applied.

The experience also needed to feel native. "Not a separate AI tool bolted on, but a natural extension of the way people already build on Bubble," Tessler noted.

After switching from their previous provider to Claude, Bubble built an internal evaluation suite to benchmark each model upgrade. When they moved to Sonnet 4.6, it matched the output quality of larger models at lower cost and faster response times. "The resulting apps still have all the sophistication and visual quality we were previously seeing, but with much faster responses," Tessler said.

## From chat window to working app

The Bubble AI Agent is a chat window inside the editor. Users type what they want, whether that's a question about how Bubble works or a request to add a feature to their app. On the backend, Bubble enriches each message with context about the user's app: its elements, data schemas, and logic. Claude also receives extensive instructions about Bubble's visual development language and a set of Bubble-specific tools for modifying apps.

The agent proposes changes, the user approves them, and the edits are applied. Users move fluidly between chatting with the agent and editing their app with Bubble's point-and-click tools. The agent can access broad editor functionality, from the built-in issue checker (similar in spirit to a type-checker on source code) to the full range of Bubble components and workflows, so it can generate complete user interfaces, data schemas, and executable logic, all visually editable afterward.

"Our agent is built in langchain and langgraph, so migrating from other models over to the Claude API itself was a minimal amount of work," Tessler added. The bigger investment was the evaluation suite: testing each model swap against quality, latency, and cost to make sure nothing regressed.

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## Cleared backlogs and a growing builder ecosystem

After switching to Claude, user satisfaction with AI-driven edit requests increased by approximately 30%, with positive feedback rates climbing from roughly 70% to 90%. Latency improvements and better component and UI generation quality both contributed.

Internally, Claude Code has changed how Bubble's engineering team thinks about what's worth building. The majority of engineers use it, and all new hires are now onboarded to it on day one. "It's less about things we couldn't do and more about things that weren't worth attempting before," said Zoe Lapomme, Engineering Manager. "The effort-to-reward ratio has shifted significantly."

The Notes panel and style variables subtab in the Bubble editor, for instance, had been sitting on the backlog because the migration work wasn't justified. Using Claude Code to move the frontend from jQuery to SolidJS and implement new designs lowered the bar enough that the team actually shipped it. Onboarding has shifted too: bringing new engineers and contractors up to speed on an unfamiliar codebase is meaningfully faster. "Everyone's had Claude Code from the start, but it's hard to imagine doing it the old way now," Tessler said.

Beyond Bubble's own product, builders in the ecosystem are shipping Claude-powered apps through the platform: chatbots, content generation tools, document analysis workflows. Agency partners are building Claude-powered templates and plugins that other Bubble users can deploy, so the adoption compounds. Claude API integrations have trended upward over the past year, with Q1 2026 the strongest quarter to date.

Looking ahead, Bubble is integrating its app debugging tools with Claude so users can fix logic bugs directly, and adding multi-modal features like sharing app screenshots to iterate on generated UIs. "A Bubble user can connect to the Anthropic API, design a full conversational UI, and ship a Claude-powered product in hours rather than weeks," said Theo Goldberg, Partnerships Lead. "The compound effect across six million builders is what excites us most."

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
