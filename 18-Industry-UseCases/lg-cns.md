---
title: "LG CNS Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/lg-cns"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:33:03Z"
tags: ["case-studies", "claude-code", "enterprise", "security"]
---

# LG CNS modernizes 20-year-old enterprise systems with Claude

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Large

Product:  
[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Partner:  
AWS

Location:  
Asia Pacific

99.1% API conversion completion

2,888 of 2,913 APIs migrated from a 20-year-old legacy system

7-month full migration

delivered at roughly 50% of the cost of a conventional rebuild

LG CNS is the IT services and digital transformation arm of LG Group, with approximately 7,000 employees and \$4.2 billion in 2025 revenue. The company has built and operated mission-critical systems for financial institutions, manufacturers, and public-sector organizations for more than 35 years. Claude Code is the engine of its newest offering: LG CNS Build Factory, a turn-key software development service that modernizes decades-old enterprise systems at production scale.

## With Claude, LG CNS:

- Converted 2,888 of 2,913 APIs from a 20-year-old legacy system, a 99.1% completion rate
- Delivered a multi-million dollar system migration in seven months, at roughly 50% of the cost of a conventional rebuild
- Migrated 1,340 screens from a proprietary legacy frontend platform to React, with backend and frontend converted simultaneously on 24/7 parallel tracks
- Adopted Claude Code as the standard development approach across the 200-engineer Build Center
- Made a new category of project viable: modernizations that customers had deferred for years because of cost, risk, and specialist shortages

## The challenge

## The modernization projects that never get started

The migration requests landing at LG CNS follow a pattern. Customers need stored procedures over 10,000 lines long moved to a modern database, or Oracle Forms screens rebuilt in React. Many need to retire MiPlatform, proprietary UI platforms that dominated Korean enterprise IT two decades ago and have now reached end of service.

These systems are mission-critical, but the engineers who understand them are scarce and the documentation is thin. "From the customer's perspective, modernization is clearly necessary, but cost, timeline, and quality risks make it difficult to initiate," explained Hyosup Bae, Director and Head of Build Center at LG CNS.

One engagement made the bind concrete. A Korean construction company ran its projects on a 20-year-old project management system covering everything from winning an order through final settlement. The company needed to move onto a modern stack, with a fixed deadline and a tightly constrained budget.

Conventional delivery would have taken at least twice the available time and money, at an estimated cost of several billion Korean won. Offshore development did not change the math: dozens of developers writing in parallel against a poorly documented codebase makes consistency harder, not easier. Without a different approach, the project was not going to start.

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The solution

## A software factory built around Claude Code

LG CNS tested multiple models, starting from the position that public benchmarks are useful only as a reference point. The criterion that mattered most was task completion: does the model finish what it was asked to do? The team evaluated planning capability, to-do sequencing, tool-calling behavior, and what happened when a model hit an error. Could it find an alternative path, or did it stall?

Claude stood out for understanding intent, not just instructions. "While other models were able to execute given tasks reasonably well, Claude often interpreted what was not explicitly stated and proposed outputs that were more closely aligned with the underlying objective of the problem," Bae said. The difference was clearest in architecture design for large projects, where Claude behaved "less like a code generator and more like a consultant that could understand the problem and propose a direction for solving it."

Access mattered as much as capability. LG CNS reaches Claude through Amazon Bedrock, which lets the team run Claude inside the AWS security configurations its enterprise customers already have in place. For clients in regulated industries such as financial services, that changed the nature of the adoption discussion. "The conversation shifts from 'Can we trust this model?' to 'How can we use a technology that is already within our security boundary?'" Bae noted.

Selecting the model was only half the equation. [Enterprise customers](enterprise.md) need far more than generated code: they expect security, compliance, testing, and uniform quality across thousands of APIs and screens.

To deliver that, the Build Center, LG CNS's 200-engineer technology delivery organization, built an engineering orchestration layer around Claude Code. The harness connects legacy analysis, business logic extraction, code generation, testing, verification, and quality management.

A typical project runs in pods of five to seven people: a Solution Owner, Architect, Engineers, and DevOps. Work starts with planning, where the team presents the project objective and intent to Claude and asks it to propose an approach.

Once the direction is set, work is decomposed into small, clearly scoped tasks defined in YAML. Context is chained through the local file system, with each stage's output stored as files and passed to the next. The team relies on Claude Opus 4.6 for core work: architecture design, legacy analysis, complex code generation, and multi-step workflow execution.

The file-mediated approach began as a workaround. Before the 1M-token context window and memory features arrived, preventing quality degradation as context accumulated was the team's hardest engineering problem. The patterns LG CNS designed to solve it, persistent file-based memory and multi-agent coordination through file handoffs, anticipated capabilities Anthropic later shipped natively.

The team still treats decomposition and context chaining as core strategy. At enterprise scale, maintaining context taxonomy and output consistency matters more than raw context length.

The design philosophy is deliberately restrained. "Trust the model," Bae advised. "Building an overly thick harness to prevent every possible failure constrains the model's performance and increases token consumption." Instead, LG CNS uses a thin, multi-layered harness, with lightweight layers for validation, context scoping, and quality checks that preserve Claude's ability to reason while providing the stability enterprise projects require.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The outcome

## Proof on a real customer system

The approach was validated on the construction PMS itself: a multi-billion-won, next-generation rebuild delivered between November 2025 and June 2026, at roughly 50% of the cost of a conventional rebuild. The system successfully went live in June 2026.

The project achieved a 99.1% API mapping completion rate, with 2,888 of 2,913 APIs converted. On the frontend, 1,340 screens moved from MiPlatform to React across a main portal and a partner portal. Backend and frontend conversion ran simultaneously through 24/7 parallel-track operations.

"The ROI is not simply that we did it faster," Bae said. "The ROI is that we made a previously difficult-to-start project possible."

The work itself has shifted for senior engineers. Their role now centers on setting direction: defining the tasks a large-scale project requires, decomposing them along the right boundaries, and establishing the work sequence and chaining strategy between them. "Once the strategy and direction are set correctly, the details are then refined to fit the on-site situation and the nature of each individual task," Bae explained.

For customers, the most meaningful change is not speed. Migrations they had deferred for years are now realistic options, discussed not as open-ended risks but as executable transformation roadmaps. "The most memorable customer reaction has been the realization that this is now possible," Bae said.

LG CNS plans to develop LG CNS Build Factory into a rigorous, verifiable modernization discipline, investing in deterministic validation through decision-making, automated quality measurement against golden datasets, and a harness that improves itself over time. As the team sees it, the two layers compound.

"The model gets more capable, the harness becomes more sophisticated, and as the two evolve together, the quality and scale of modernization outcomes we can deliver to customers will continue to improve," Bae said.

## Related stories


### Caylent turns months of migration work into days with Claude Agent SDK


### How can a two-person fabrication studio make room for problems it’s never solved before?


### How Blank Metal, a lean professional services firm, runs on Claude Cowork


### Quantium scales Claude across Australia's largest enterprises

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
