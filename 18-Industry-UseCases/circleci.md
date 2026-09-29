---
title: "CircleCI Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/circleci"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:59Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# How CircleCI built a code validation agent with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Medium

Product:  
Claude Platform

Location:  
North America

90% of the engineering team uses Claude Code

with daily usage jumping 9x since structured adoption began

75% reduction in average test run time

when customers use CircleCI's Smarter Testing feature

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

[CircleCI](https://circleci.com/), whose CI/CD platform processes billions of jobs annually for teams at Okta, Hinge, and Hugging Face, set out to tackle the growing maintenance burden that slows engineering teams down. The result is CircleCI’s autonomous AI agent [Chunk](https://circleci.com/product/chunk/), built with Claude, which identifies and resolves CI/CD-related maintenance issues with minimal human intervention.

## With Claude, CircleCI achieved:

- 75% reduction in average test run time when customers use CircleCI's Smarter Testing feature
- 90% of the engineering team on Claude Code, with daily usage jumping 9x since structured adoption began
- 90%+ prompt cache efficiency in production, meaning context is reused rather than reprocessed across workflows.
- Multi-quarter internal projects completed in weeks, including an AI-powered PR review system.
- More than 4 in 5 agent tasks now triggered automatically at the point of failure, with the rate of tasks converted into completed pull requests more than doubling since launch

## The challenge: Maintenance backlogs that slow teams

CircleCI's customers are engineering teams where delivery speed directly determines competitive outcomes. Those teams face a persistent tension: test optimization, build fixes, and pipeline improvements all pile up in backlogs while everyone focuses on shipping new features. Technical debt compounds, and the velocity teams are trying to protect gradually erodes.

CircleCI sees this problem intensifying as AI tools accelerate code output across the industry, generating code faster than teams can maintain it. The company needed to solve this internally before they could credibly help their customers solve it too. The goal: build an autonomous agent that could pick up routine maintenance and validate its own fixes before a human ever sees them.

## A decision driven by developer experience

CircleCI's work with Claude started broadly. The company encouraged teams across engineering, operations, and go-to-market to experiment for prototyping, iteration, and analysis. "We encouraged teams to use AI to reimagine the art of what's possible," said JP Leblanc, SVP Engineering. "By providing a single, robust platform for AI exploration, we saw adoption numbers soar."

When the team selected Claude to power Chunk, the deciding factor was the Claude Agent SDK's developer experience: a clean, well-documented interface that made it fast to build. MCP integration meant connecting to existing development tools without coordination overhead. The team found Claude's security posture met their enterprise requirements and rated it the strongest general-purpose model available.

## A closed loop from task to validated pull request

CircleCI’s agent Chunk operates as a closed loop: a natural language task goes in, a validated pull request comes out. Because customers have already described their build environment in their CI configuration, Chunk can spin up those environments as sandboxes with confidence because Claude has access to the right dependencies and tools. For build failures, Claude receives logs as context. For tests, it gets results from previous runs. Claude generates a fix, and CircleCI pipelines validate it. If the pipeline fails, Claude reattempts. The customer receives a PR that is already "green," with the CI pipeline serving as attestation that the change meets testing, linting, and static analysis standards.

"We could not have built Chunk without the Claude Agent SDK," explained Michael Webster, Principal Engineer at CircleCI. "If we had tried to do this three years ago, the amount of work to support all the language variations, framework integrations, and toolchain connections would have been prohibitive. Now we can build really powerful tools very quickly without all the traditional coordination overhead and custom integration work."

A team of 8 engineers built Chunk, moving from working prototypes in days to production-ready capabilities in weeks. Tasks can trigger automatically (periodic runs to fix flaky tests), be user-initiated (fixing a failed build), or come as ad-hoc prompts through Chunk's chat interface. Predictive test selection, which CircleCI calls Smarter Testing, runs only what is new or impacted. This cut time-to-feedback by an average of 75% and up to 97%.

Beyond Chunk, Claude Code has become the daily driver for CircleCI's engineering team, with 90% of engineers engaged. Daily usage has jumped 9x since adoption. One team built an AI-powered PR review system that scans for code issues, analyzes downstream SQL dependencies, flags query optimizations, and generates impact summaries. It deployed in weeks rather than the multiple quarters it would previously have required.

## The results

More than 4 in 5 Chunk tasks now trigger automatically at the point of failure, without a human needing to step in. The rate at which Chunk converts tasks into completed pull requests has more than doubled since launch, meaning Chunk is getting better at knowing when it has enough confidence to propose a fix. For one large enterprise customer, analysis time dropped from 14 hours to 18 minutes. A team that previously waited until the following morning to know whether a change was safe now gets that answer in minutes.

CircleCI's roadmap builds on Claude's advancing reasoning capabilities: automated test management, build optimization, and predictive maintenance that anticipates issues before they affect workflows. As code output accelerates, autonomous validation is what keeps the system from falling behind.

"Claude allowed us to bring Chunk to market faster than we would have otherwise," said Webster. "We've put autonomous maintenance, test optimization, and continuous improvement within reach of every developer by giving them an agent that picks up these tasks automatically. Issues that would sit in backlogs for months are now resolved automatically, and customers can stay in flow and focus on innovation rather than dealing with toil."


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
