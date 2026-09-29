---
title: "Satispay Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/satispay"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:33:11Z"
tags: ["agents", "case-studies", "claude-code", "enterprise", "security"]
---

# How Satispay's engineers write 75% of their code with Claude

[Try Claude](https://claude.ai)

Industry:  
Financial services

Company size:  
Medium

Product:  
[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Enterprise](enterprise.md)[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)

Location:  
EMEA

75%+ of code committed each month

is generated with Claude

10x faster core payment service modernization

from a four-week estimate to under four days

[Satispay](https://www.satispay.com/en-it/) is Italy's leading independent payment network, with 6 million consumers and more than 450,000 merchants using its app to pay in stores, send money, and manage everyday finances. Behind the product is an engineering organization maintaining a mature Java and Spring estate that processes every payment on the network. Claude Code now runs on every engineering laptop, and Claude Cowork has spread organically across several business units.

## With Claude, Satispay:

- Generates over 75% of code committed to Satispay's repositories each month
- Achieved 10x faster modernization of the core transaction service, safely completing a Java 8 to Java 21 and major Spring upgrade in under four days against a four-week estimate
- Cut data transformation lambdas from three to five days to under an hour
- Completed an 18-month code update roadmap in 7 months
- Saw over 90% Claude Code adoption across engineering, with full rollout in 30 days managed by IT support

## The challenge

## A junior team on a mature payments codebase

When Chief Technology Officer Fabio Rapposelli joined in 2025, the team was weighted toward earlier-career engineers and the codebase had some legacy services that were hard to maintain. With much of the work focused on maintenance and incremental development, early-career engineers spent more time reading than writing and senior review had become the bottleneck.

"A junior engineer facing an unfamiliar service needs help understanding the system, not help finishing a line of code," Rapposelli said. Earlier experiments with autocomplete-style AI coding tools had stayed in pockets and never addressed that gap.

The default workflow showed the strain. An engineer would pick up a ticket, spend significant time orienting in a service they had never touched, draft a change, and wait for a senior to review it. That review was carrying three jobs at once: teaching, quality gate, and context transfer. Roadmap velocity suffered, and senior time was going to enable others rather than building.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The solution

## Making Claude available from day one

Satispay ran a structured 30-day evaluation in mid-2025 comparing Claude Code against another AI coding tool on real tickets across its Java and Spring services. The rubric covered code generation quality, refactoring, adherence to internal patterns, multi-file context understanding, test generation, and documentation. Claude won on every dimension except IDE integration. "Claude Code's output, both the code it wrote and the reviews it produced, was considered best across the board,” explained Rapposelli. “Claude's reviews caught real issues, with real explanations, at a quality our engineers recognized as genuinely useful," Rapposelli said. "Other tools weren't playing in the same league."

Rollout took 30 days from decision to full coverage and was handled by IT support. Claude Code ships to every engineering laptop through Satispay's managed device fleet, so it is available on an engineer's first day with nothing to configure. Engineers use it to write new code, modify existing services, navigate unfamiliar parts of the codebase, and run a Claude review pass before human review. They reach for Opus or Sonnet depending on the task, with full access to the 1M-token context window. Spend is managed at the budget level rather than per seat, so no one pauses mid-task to justify reaching for a more capable model.

The cultural work mattered as much as the rollout. Satispay added AI proficiency to its engineering performance framework, and the operating rule is explicit: engineers own what lands in the repository. "The model is an accelerator, not an authority," Rapposelli said.

Beyond the default tooling, the team builds reusable assets. Standard Java scaffolding for new services and tests starts from an encoded pattern instead of a blank file. Modernization approaches get packaged into subagents so the next team inherits the work. The most concrete example is data transformation: AWS Lambda functions that engineers used to write by hand are now generated from a specification by an internal subagent connected to an MCP server. "Lambdas would routinely take over three days to build," Rapposelli explained. "Now it takes less than an hour."

The expansion beyond engineering surprised even Rapposelli. Once Claude skills became visible internally, requests came in at a rate of roughly 20 a day from finance, legal, marketing, and operations, including the CFO asking for access to financial analysis skills he had spotted himself. "People across the company knew they had AI-shaped problems," Rapposelli said. "When the tool showed up, they didn't need permission to solve them."

Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

[Read more](https://claude.com/blog/claude-code-on-the-web)

## The outcome

## Updating the system behind every payment

The clearest single proof point is the evolution of Satispay's core transaction service, the system that runs every payment on the network. The team took it from Java 8 to Java 21 and through a major Spring upgrade in under four days, when the original estimate was four weeks. The broader update program tells the same story at a larger scale: goals the team had set for an 18-month horizon were complete in 7, fast enough that an external consulting engagement brought in for the work was no longer needed.

Across the organization, more than 75% of code committed each month is generated with Claude, and adoption sits above 90% of engineers. Senior engineers are spending more of their time on architecture, and early-career engineers are operating with far more independence on a codebase that used to slow them down. The team is now planning to ship roughly 50% more features in the first half of the year..

"We're moving to a model where the engineer becomes an engineering manager of agents," said Rapposelli. "Individual engineers are operating above their years because the agents close the gap."

## Looking ahead: From task automation to agentic workflows

Two pilots already running point to what comes next. Issue-to-PR automation has Claude draft pull requests from tickets filed by other teams, with engineers owning the review and the merge. Agentic fraud investigation moves a workflow tied directly to financial loss from human-in-every-step to agent-led, with people kept in the loop on the decisions that warrant it. "Right now we're focused on automating the task and keeping a human in the loop for critical decisions," Rapposelli said. "The work ahead is understanding which decisions genuinely need a person, and which ones we've simply been used to making ourselves."

## Related stories


### How Qonto delegates financial admin for small businesses with Claude on Amazon Bedrock


### Pictet turns weeks of work into hours with Claude Code


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
