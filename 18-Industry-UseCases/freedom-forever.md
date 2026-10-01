---
title: "Freedom Forever Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/freedom-forever"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:35Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# Freedom Forever automates permit workflows with Claude

[Try Claude](https://claude.ai)

Industry:  
Energy

Company size:  
Large

Product:  
Claude Platform

Location:  
North America

97.5% benchmark success

on complex web automation tests (39 of 40 runs passed), compared to 20–60% for alternative frameworks

~19,000 permit emails processed

in the first month of production

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

[Freedom Forever](https://www.freedomforever.com), the largest residential solar installer in the United States, handles the full lifecycle of solar installation—from sales and permitting through design, installation, and ongoing monitoring. The company has 3,000 employees, primarily field operations and installation crews, and a 50-person software and product team.

## With Claude, Freedom Forever:

- Achieved 97.5% success rate on complex web automation benchmarks where alternative frameworks hit 20–60%
- Processed approximately 19,000 permit emails in the first month of production, handling communications from hundreds of utility companies
- Built a unified agent framework connecting web automation, CRM workflows, file validation, and sales support
- Reduced agent execution costs to \$0.20–\$0.35 per run while completing most tasks in about two minutes

## The problem

Between a signed contract and solar panels on a roof lies a maze of permits. Every residential solar installation requires submissions to utilities and municipalities—each with their own third-party websites, forms, and approval processes. Freedom Forever processes about 5,000 individual permits per month, but each permit involves multiple touchpoints: inspection communications, receipt confirmations, payment requirements, correction requests, and approval notifications.

The permit team was drowning in email. Hundreds of utility companies send updates throughout the day, and processing this volume manually meant backlogs kept growing. Some emails sat unprocessed for weeks while customers waited in limbo, their projects stalled for reasons they couldn't see. "Installation timelines are our most important metric," said Rob Richardson, VP of Product at Freedom Forever. "We've strengthened our systems and processes so every customer gets consistent updates and support throughout the process.”

The company had experimented with AI coding assistants for a small group of developers, part of a broader push to build faster. But for complex agentic workflows—particularly web automation on third-party permit sites with cookie consent pop-ups, iframes, shadow DOM elements, and multi-step forms—they needed something more robust than existing frameworks could provide.

## Choosing Claude through rigorous benchmarking

Freedom Forever built a formal benchmark around their hardest problem: automating permit submissions on third-party websites. The team created eight internal mock sites replicating real-world challenges—simple single-page forms, multi-step workflows, blocking interfaces like cookie consent and pop-ups, iframes, and shadow DOM elements. They ran five iterations per site, comparing what each framework submitted against expected results, with video recordings to verify accuracy.

"Claude Agent SDK scored 97.5% on our benchmark—we couldn't break it," said Richardson. "The single failure was a rate limit issue from running dozens of parallel agents, not the agent itself. Other frameworks hit 20–60% at higher cost."

The team had explored alternatives, including building applications using other agent frameworks. Each showed promise in limited contexts, but Claude Agent SDK handled the full complexity of their web automation workflows. Beyond performance, the SDK proved to be the easiest to build on—the benchmark development and testing took about three weeks, and they launched their first production agents two weeks later.

## Building the permit automation system

Claude Agent SDK now serves as Freedom Forever's primary agent framework for production workflows. The system handles permit submissions on third-party utility and municipality websites, processes incoming permit emails in real time, and connects to their custom CRM for scheduling, task completion, file analysis, and human handoffs. A single, unified framework powers automation across the business.

The SDK was straightforward to build on—the core agent loop required little custom work, and it handled most underlying complexity out of the box. Freedom Forever built an internal "agent console" on top of it to manage workflows, but the foundation came together quickly. And as the SDK improves, they benefit automatically. "When structured outputs rolled out, we stripped out our custom workarounds and just turned it on," said Richardson. "That kind of speed matters." In addition, much of the internal tooling, benchmarks, and reporting infrastructure was itself built using Claude Code, Anthropic's command-line tool for agentic coding.

## The outcome

The permit email processing agent—their highest-volume deployment—processed approximately 19,000 emails in its first month of production, handling communications from hundreds of utility companies. The system categorizes incoming messages (inspection communications, receipt confirmations, payment requirements, correction requests, and more), extracts relevant data, and takes appropriate action. About 71% of emails are fully processed without human intervention; even cases requiring handoff have the human work dramatically reduced. Each execution costs \$0.20–\$0.35 and completes in about two minutes—two to five times less than the human equivalent.

But the real discovery came when they ran a backfill. The agent found emails that had been sitting unprocessed for an average of three weeks—a couple dozen customers stuck in limbo, waiting for action on permits that would let their installations proceed. The agent identified these cases and moved the projects forward, clearing a backlog the team hadn't fully grasped. "Installation timelines are our most important metric, and we've never had faster timelines and better quality," said Richardson. "I know Claude and our agent system is affecting that."

"The main limitation now is just opening up more workflows and going deep enough on each to remove substantial load from teams," said Richardson. "The limitations are on us building more tools and capabilities, not the agent's ability to orchestrate and make decisions."

## Expanding across the organization

Freedom Forever continues expanding Claude's role. They recently deployed a file validation agent that processes about 1,500 documents, validating utility bills against internal system requirements. These documents often include meter numbers and past usage data displayed in charts rather than text—information that traditional OCR struggles with. Many uploads are photos of someone holding the document in their hand; Claude handles these without issue.

"We even found cases where our validation rules had gaps," said Richardson. "By enabling web search, the agent was able to fill in missing information for deeper validation—and then commit those learnings to a knowledge base so future runs are even more capable."

The company also recently migrated their sales support agent from another framework to Claude Agent SDK. This system serves as an inbound support line where over 10,000 sales representatives can call or text to understand their pipeline, navigate company processes, and interact with internal systems.

The internal agent console they built on top of the SDK now serves as a platform for the entire team, with only a handful of developers working directly in the SDK layer while many more use the UI to configure skills and workflows. "We're going headfirst with Claude and the Agent SDK," said Richardson. "We see it as the future for a lot of our work and want to be deeply embedded."

## Related stories


### How can a small team revive solar power and restore trust?

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
