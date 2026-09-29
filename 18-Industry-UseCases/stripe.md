---
title: "Stripe Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/stripe"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:47Z"
tags: ["agents", "case-studies", "claude-code", "enterprise", "security"]
---

# Stripe deploys Claude Code to 1,370 engineers with zero-configuration enterprise rollout

[Contact sales](https://www.claude.com/contact-sales)

Industry:  
Software

Company size:  
Large

Product:  
Claude Code

Location:  
North America

1,370 engineers using Claude Code

enabled company-wide

10,000 lines of code migrated in 4 days

A Scala-to-Java migration using Claude models that would have taken an estimated 10 engineering weeks by hand

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

[Read more](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026)

[**Stripe**](https://stripe.com) builds financial infrastructure for the internet, powering payments for millions of businesses worldwide. The company's developer infrastructure team ensures that Stripe engineers have the most productive experience of their careers through tooling and platform capabilities.

## With Claude, Stripe:

- Deployed Claude Code to 1,370 engineers with a zero-configuration setup that works immediately on every developer's machine
- Migrated 10,000 lines of Scala to Java in four days, a project estimated at ten engineering weeks without AI assistance
- Collaborated with Anthropic to produce a signed enterprise binary, solving security concerns that had initially blocked deployment
- Created an education program that reframed AI assistants as capable new engineers who need context, not replacements who work autonomously
- Built a foundation for AI-powered agents focused on maintaining Stripe's 5.5 nines of reliability

## The challenge

Stripe needed a CLI-native coding assistant that met [enterprise security requirements](enterprise.md). For Stripe's developer infrastructure team, led by Scott MacVicar, the challenge wasn't choosing a single winner; it was enabling engineers to find the tools that fit their individual workflows while maintaining enterprise-grade security.

"Things are rapidly evolving here," said MacVicar, who runs Stripe's developer infrastructure group. "We're really just going broad and haven't started doing any consolidation." The team enabled six different coding assistants, recognizing that different engineering personas gravitate toward different interaction models. Infrastructure engineers prefer command-line tools. Product engineers want in-editor experiences. Forcing everyone into one tool would mean leaving productivity on the table.

But breadth created its own problems. Enterprise security requirements meant Stripe couldn't simply let engineers install whatever they wanted. Supply chain attacks are a real concern, and random JavaScript packages on corporate laptops posed unacceptable risk.

## Claude Code enables zero-friction adoption

The path to deployment required collaboration. MacVicar worked directly with Anthropic to produce an enterprise binary version of Claude Code, a process that took two to three months of testing and iteration. The result was a signed binary that could be deployed safely across the organization, bypassing the npm dependency chain that had posed security concerns.

## Treating AI assistants like capable new engineers

"We came up with our internal distribution mechanism," MacVicar explained. "It's pre-installed on everyone's laptop. It's pre-installed on everyone's development box. It's pre-configured with the rules, the tokens, the authentication. It just works out of the box so no one has to go make an account or read all the configurations."

This philosophy extends to all of Stripe's developer tooling: engineers shouldn't spend time reading manuals or figuring out ideal configurations. The infrastructure team handles that complexity so developers can focus on building. Claude Code found its niche among developers who wanted a capable assistant that fit into their existing command-line workflows without requiring them to switch editors.

The biggest challenge hasn't been technical—it's been educational. Engineers initially approached AI assistants with unrealistic expectations, treating them as replacements rather than collaborators.

"People think it is a replacement for themselves and then don't quite give it the right amount of context," MacVicar said. The team developed a mental model that resonated: think of AI as a “new, capable engineer that knows all the programming languages but lacks business context, doesn't understand your codebase, and doesn't know the Stripe way of doing things."

This framing changed how engineers prompted their AI assistants. Instead of expecting magic, they learned to provide context: point to documentation, show example code, explain architectural patterns. The team reinforced this through engineering all-hands presentations, dedicated training sessions, and strategically placed "hint buttons" throughout internal tools. Local examples proved more effective than centralized training. Teams that discovered effective prompts for their specific codebases shared those patterns within their groups, creating organic knowledge transfer. For MacVicar's team, this education work is as important as the tooling itself. This approach to onboarding, treating AI as a collaborator that needs context rather than a replacement, reflects how Stripe and Anthropic see the future of AI-assisted development.

## The results: Building towards AI agents for reliability

Engineers report higher satisfaction with their tooling. While the team hasn't isolated metrics attributable to any single AI assistant, the signals are positive across the board. One concrete example: a team used Claude models to migrate 10,000 lines of Scala to Java in four days, a project estimated at ten engineering weeks by hand. The migration enabled a newer version of the JDK, enabling performance improvements that had been stuck behind the manual effort required. "Sentiment's up,” MacVicar said. "People like it. The vibes are good."

The real ambition lies ahead. Stripe maintains 5.5 nines of reliability, and MacVicar sees AI agents as the path to even higher standards. "If we rely on a human doing something, those are measured in minutes. If we have an agent doing it, we can measure that in seconds."

The team is exploring Claude's agent SDK to build specialized tools focused on incident detection and resolution. In a business where downtime directly impacts customers' revenue, shaving minutes off response times translates to real value.

MacVicar frames the opportunity in four quadrants: humans only, humans with agents, agents with humans, and agents only. "We're pushing things into humans with agents and agents with humans," he said. "The desire is to get to that top quadrant of agents only."

For now, Stripe continues learning what works across its suite of AI tools. The investment in broad enablement, secure deployment, and developer education has created a foundation for whatever comes next in this fast-moving space.


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
