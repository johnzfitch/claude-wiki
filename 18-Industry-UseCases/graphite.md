---
title: "Graphite Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/graphite"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:04Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# Graphite speeds up code review by 40x with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Small

Product:  
Claude Platform

Location:  
North America

800x faster

35 minutes vs 3 weeks for analysis

Human-level

performance on biomedical benchmarks

Graphite, a modern end-to-end developer platform, uses Claude to power their AI code reviewer that catches bugs and suggests fixes, transforming how engineering teams at companies like Snowflake, Asana, and Ramp approach software development.

With Claude, Graphite achieves:

- 40x faster pull request feedback loop, from 1 hour to 90 seconds
- 96% positive feedback rate on AI-generated comments
- 67% implementation rate of suggested changes
- Support for hundreds of thousands of pull requests across their customer base

## The challenge of scaling modern code review

Code review is a critical bottleneck in modern software development. While big tech companies like Google and Facebook have sophisticated internal tools to manage this process, most engineering teams struggle with basic GitHub workflows. "The open secret in dev tools is that almost every company builds tooling on top of GitHub to improve it for teams," said Tomas Reimers, Co-founder at Graphite.

Without proper tools, developers face mounting delays. They wait hours or days for feedback, then start another time-consuming cycle of fixes and re-reviews. In early 2023, Graphite explored AI-powered code review after receiving repeated requests from forward-thinking development teams. However, early experiments proved disappointing. "The models would hallucinate and confidently claim problems in pull requests that didn't exist," said Reimers. "When the bot generated incorrect but specific statements, people were frustrated." The team needed something that could match human-level understanding of code while maintaining high accuracy.

## Choosing Claude for superior code comprehension

After testing leading AI models, Graphite found that only Claude met their standards for code review. The team's rigorous evaluation framework tested models against 500 pull requests, including synthetic and real-world examples with known bugs that even experienced engineers struggled to spot. "Claude was especially good at code understanding, which for code review is incredibly important," said Alyssa Baum, Lead AI Engineer at Graphite.

The release of Claude 3.5 Sonnet marked a decisive breakthrough. Baum said, "Not only did our eval performance skyrocket, but it identified bugs in our test dataset that we hadn't even realized were bugs." Through A/B testing, the team confirmed Claude's superior performance. "When Claude 3.5 came out, we plugged it into our system and the performance for our users was incredible."

The partnership with Anthropic amplified these technical advantages. Anthropic's team provided crucial guidance on evaluation frameworks and implementation strategies through a dedicated Slack channel. When Graphite's October 2024 launch faced unexpected demand, Anthropic quickly helped scale their rate limits to meet customer needs. "We've had great support from the Anthropic team," said Reimers. "We found it to be incredibly helpful just for getting advice on how we should structure our evals and our code in general."

## Transforming code review through advanced AI architecture

Graphite's implementation combines Claude's sophisticated reasoning capabilities with deep expertise in effective code review. Their architecture breaks complex code analysis into discrete steps, allowing Claude to excel at each specific task. The system employs multiple validation layers including voting, chain of reasoning, and self-critique to ensure only high-quality comments reach developers.

The platform focuses on objective bugs, not subjective suggestions. It addresses issues like:

- Function parameter ordering errors
- Copy-paste mistakes
- Security vulnerabilities
- Logic inconsistencies
- Best practice violations

When issues are identified, the system automatically generates fix suggestions for developers to implement with a single click, reducing the traditional fix-and-review cycle time.

## Delivering measurable impact for development teams

Graphite's AI-powered approach has transformed the development workflow for their customers. Brian Michel from The Browser Company said, "Graphite Reviewer strikes a good balance between showing problems and not being annoying. It's different from other AI tools because it actually works. I'm able to iterate faster and produce something that is workable faster. This helps as a single developer because you're really not alone anymore."

The impact extends beyond individual developers to entire engineering organizations. "Graphite has been a game-changer for the team at Ramp," said Nik Koblov, Head of Engineering at Ramp. "The AI reviewer's automatic comments catch subtle errors before they become bugs, helping us maintain quality without slowing down. Overall, Graphite has made our workflow smoother and more productive."

This quality-at-speed advantage resonates across Graphite's customer base. "Graphite Reviewer is impressively high-signal: it has already caught several real bugs before they make it to customers, which is a valuable addition to our developer workflow," said Ben Kraft from Notion.

The system currently provides actionable feedback on one in five pull requests, nearing the industry standard of one in three receiving human comments. With 67% of AI suggestions leading to code changes and a 96% positive feedback rate, Graphite shows that AI can match human-level code review quality while operating at machine speed.

## Looking ahead to AI-augmented development

Graphite envisions a fundamental transformation in software development over the next decade. Reimers said, "Our belief here at Graphite is 10 years from now, individuals aren't going to write software. LLMs will write the majority of the code, and they'll be guided by or collaborate with humans who connect their product to the outside world."

Through their partnership with Anthropic, Graphite is leading this transformation. By automating time-consuming reviews, catching subtle bugs, and enabling one-click fixes, they're freeing developers to focus on what humans do best – making high-level architectural decisions that shape the future of software. Together, Graphite and Claude are transforming code review from a bottleneck into an accelerator of human creativity and engineering excellence.

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
