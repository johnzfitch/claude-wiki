---
title: "Graphite Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/graphite"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:04Z"
tags: ["api", "enterprise", "security"]
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
