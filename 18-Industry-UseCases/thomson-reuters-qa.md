---
title: "Thomson Reuters Claude Cowork case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/thomson-reuters-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:48Z"
tags: ["case-studies", "enterprise", "security"]
---

# Thomson Reuters CTO on piloting Cowork with Claude Enterprise

[Try Claude](https://claude.ai)

Case Study: Thomson Reuters

Thomson Reuters uses Claude in Amazon Bedrock as part of its strategy to power its legal AI platform, CoCounsel.

[Read more](thomson-reuters.md)

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Read more](../15-Claude-AI-Features/product-cowork.md)

[**Thomson Reuters**](thomson-reuters.md) builds the software and research tools that legal, tax, accounting, and compliance professionals rely on. The company’s AI-powered platform, CoCounsel, recently crossed one million users, making it one of the most widely adopted AI tools in professional services.

Internally, Thomson Reuters has added [Claude Enterprise](enterprise.md) as a core AI capability for its teams. More recently, the company began piloting Cowork to explore how agentic AI can support everyday enterprise workflows across documents, spreadsheets, and internal processes.

Joel Hron, CTO of Thomson Reuters, sat down with Anthropic to discuss how the company is approaching Claude Enterprise, what they are learning from piloting Cowork, and how large enterprises can roll out these systems responsibly. The following conversation has been edited for length and clarity.

**Anthropic: How did Thomson Reuters first start using Cowork? Was it adopted top-down or did individuals start experimenting on their own?**

**Joel Hron:** We’ve been strong believers in Claude Enterprise. It gives us the security posture, administrative controls, and reliability you need in a global enterprise environment.

When Cowork became available in early access, we saw it as a natural extension of that investment. Rather than pushing it enterprise-wide immediately, we piloted it with a small group of employees who were already sophisticated Claude users. That gave us a controlled way to evaluate how agentic workflows perform against real enterprise tasks.

From the start, we connected it to real systems like Microsoft 365 so teams could work against live documents and spreadsheets, not sandbox examples. For us, the question was not whether it was interesting. It was whether it delivered value under real conditions.

**Anthropic: You’ve said that a portion of your Claude usage comes from non-developers. Is Cowork influencing that?**

**Joel Hron:** Claude Enterprise already enabled strong adoption beyond engineering. We have seen product, operations, and business teams using it heavily.

What Cowork adds is structured workflow capability. Non-developers can now move further into automation and light prototyping using the documents and data they already work with every day.

For example, a product manager can describe a workflow, attach relevant files, and generate a first-draft structure or analysis that the broader team can review. That shortens the distance between idea and execution.

We are still in pilot mode, but the early signals are strong.

**Anthropic: Walk us through a specific Cowork workflow that's become part of a team's regular routine at Thomson Reuters. What do they give Claude as input, what comes out, and how much of the output is usable versus needing rework?**

**Joel Hron:** A good example is product analytics around NPS data.

The inputs are straightforward: an Excel file with survey scores and written feedback, along with a clear prompt such as, “Compare performance across quarters, identify major themes in the comments, highlight what is changing, and draft a summary for a leadership readout.”

Cowork can analyze the structured data and synthesize qualitative feedback into themes tied to what the numbers show. The output is a structured analysis and draft narrative that can be shaped into a memo or presentation.

It is not publish-without-review. Teams validate the numbers and refine the narrative. But instead of spending hours manually stitching together spreadsheets and comments, they begin with a reviewable draft and focus their time on judgment and interpretation.

That shift is important. The human role does not disappear. It moves up the stack.

**Anthropic: Are there tasks that teams at Thomson Reuters have stopped doing manually since adopting Cowork?**

**Joel Hron:** We think about this less as a replacement and more as a shift in where humans spend judgment. Cowork helps teams do work at a scale that was hard to justify before. For example, teams producing survey-based insights can now tailor analyses and client-ready materials to different audiences far more efficiently.

That used to be manual, which limited how many tailored outputs you could produce. Now, Cowork can help parallelize the effort. The human role becomes validation, refinement, and decision-making. Not repetitive rework. We’re starting to experience these shifts in our engineering processes with Claude Code—and Cowork has the potential to drive a similar change in various other aspects of our business.

**Anthropic: Thomson Reuters has a deep focus on trust, IP protection, and accuracy. How does Cowork fit within those requirements? Are there specific guardrails you've put in place?**

**Joel Hron:** Trust is foundational for us. That is true in our customer-facing products, and it is true internally.

Claude Enterprise gave us confidence in areas like data isolation, security controls, and administrative oversight. With Cowork, we approached it the same way we approach any significant capability: structured evaluation, limited rollout, and clear governance expectations.

We reinforce least-privilege access through approved connectors, strong data handling standards, and human validation for consequential outputs. We also maintain an active partnership with Anthropic, providing enterprise feedback and collaborating on readiness for environments like ours.

Governance is not an afterthought. It is part of adoption.

**Anthropic: What's surprised you most about how people at Thomson Reuters have used Cowork?**

**Joel Hron:** One surprise has been how strong Cowork is with everyday enterprise files, especially spreadsheets and presentations. What we have seen is that Cowork's ability to analyze, transform, and generate outputs in those formats is extremely impressive, even early on.

We have had people who were skeptical at first. Then a couple hours later they come back and say, "I'm converted." In an enterprise environment, that kind of credibility is earned through real workflows, not demos.

**Anthropic: Where do you see the most untapped potential for Cowork at Thomson Reuters?**

**Joel Hron:** The biggest untapped potential is moving from person-by-person learning to reusable internal capabilities. So far, we have let individuals and teams build skills organically, prove value, and share within their groups. The next step is to systematize it: shared plugins, standard workflows for common tasks, and a way to distribute "how we work" patterns across the enterprise.

In engineering, we have norms like code review and shared practices. We think the same idea applies here. Teams develop strong patterns for using Cowork, and we create lightweight mechanisms, so the best approaches spread quickly and safely.

**Anthropic: What advice would you give to another large enterprise thinking about rolling out Cowork?**

**Joel Hron:** A few lessons stand out.

First, start with a focused group of capable early adopters. Let them pressure-test real workflows.

Second, pick meaningful use cases. Trust builds when the system proves itself on consequential tasks.

Third, treat governance as an enabler. Clear guardrails, approved connectors, and explicit expectations around human validation allow you to move faster, not slower.

And finally, measure value beyond time savings. Some of the most important gains come from enabling higher-quality work and new workflows that were previously impractical.

## Related stories


### Spellbook runs 530,000 contract reviews a month with Claude


### EvenUp cuts document drafting from 15 hours to 15 minutes with Claude


### Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude


### GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude

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
