---
title: "Descript Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/descript"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:44Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# Descript brings creative taste to agentic video editing with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Small

Product:  
Claude Platform

Location:  
North America

13–23% higher intent adherence than leading competitors

Claude Opus 4.6 outperformed other frontier models on Descript's evaluation criteria for translating creative intent

Two thirds of users select a Claude model in Descript’s agent

Descript also ships Claude Sonnet as the default model for its agent

Descript makes video editing work like editing a document: users change the text, and the video updates to match. Last year, the team launched Underlord, an AI agent powered by Claude, that automates complex edits users would otherwise do manually. In January 2026, Descript shipped major updates to Underlord, with Claude Sonnet 4.5 as the default model for self-serve, and Opus 4.6 for enterprise customers.

## With Claude, Descript achieved:

- 13–23% higher intent adherence for Claude Opus 4.6 over leading frontier models in internal evaluations, measured across 100+ real-world test cases
- Two-thirds of models manually selected in the model picker are Claude models
- 9% higher export rate for agent users compared to non-agent users, with nearly 50% more edits made per export demonstrating a deeper creative process
- 46% higher free-to-paid conversion among users who engaged with Underlord compared to otherwise active free users who did not
- 30%+ of all Descript projects now using its agent Underlord at some point in the project lifecycle
- Integration of new Claude models in as little as half a day
- Opus 4.6 outperformed other frontier models on Descript's "Do What I Asked" evaluation criteria, which measures how well the model translates a user's creative intent into concrete editing actions.

## The challenge

## From workflows to an open-world agent

Descript's AI journey didn't start with agents. The team initially built structured AI workflows: features like "Edit for clarity" or "Create clips" that ran through predetermined orchestration steps, using an LLM as an API call within a fixed pipeline. Descript first integrated Claude in mid-2024 for these workflows, where it excelled at understanding the flow of content and creating compelling clips from longer videos.

These workflows worked for their specific use cases but broke down at the edges. The old system had hard-coded pipelines for specific tasks: "Edit for clarity" would chunk a script, send it to an LLM, and batch-apply cuts. But if a user wanted something slightly different, like targeting only a few paragraphs for edits, or putting edits in a new composition instead of changing the original, the rigid orchestration couldn't accommodate it. "Sometimes users would want something that was a little bit different, and even with an open prompt box, it just wasn't going to work,” said Rachel Bloch Mellon, Head of AI Engineering.

Claude Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Read more](https://www.claude.com/platform/api)

## The solution

## Selecting Claude for creative intent

Building Underlord as a fully agentic system meant the underlying model needed to reason about creative intent, coordinate dozens of tools, and make judgment calls about narrative flow.

Descript evaluated frontier models using an internal framework built around three dimensions: "Don't break things," "Do what I asked," and "Do it well." The team ran more than 100 test cases drawn from real user queries, weighted toward nuanced and difficult edits. Each test is scored by an LLM-as-judge that the team has calibrated against human reviewers. Opus 4.6 outperformed other leading frontier models by 13–23% on intent adherence, with corresponding advantages on quality.

That first dimension—whether it preserves the integrity of the user's project—mattered most. Users are far more tolerant of Underlord not quite nailing their creative preferences than of it overstepping, the team shared. "The degree of anger you see when people say 'it did too much' is much greater than when it didn't quite get the taste right," said Aleks Mistratov, Head of AI Product.

A lot of video editing comes down to taste. "We've found that Claude models do a better job converting very vague and high-level descriptions of taste into concrete edits that are holistically aligned with the user's intent," said Mistratov. "This produces more polished final videos with less required direction from the user."

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## The outcome

## How Underlord with Claude changes the editing process

Descript offers all three Claude model tiers through Underlord's model picker: Sonnet models as the default for most users, Opus for enterprise customers who prioritize quality, and Haiku for fast, iterative sessions. More than two thirds of Underlord users default to or select a Claude model.

The advantages show up most clearly on tasks that require creative reasoning. A user uploads a hypnotherapy recording and asks Underlord to recommend where to lengthen or shorten pauses for therapeutic effect. A podcast host provides a detailed list of audio refinements: adjusting music transitions, balancing levels between speakers, adding chapter markers. "Opus outperforms the other leading models on those sorts of things," said Mistratov.

The collaborative workflows are where Underlord really comes alive. A user might ask: ‘Can you highlight parts of the script where an infographic might help me deliver my point?’ Then they review the suggestions and push back where they disagree. "Those types of collaborative workflows were impossible with one-shotting and workflows, and are far more possible now with the agent," Mistratov said.

Descript's philosophy is that Underlord should be a "co-editor to assist in creation, rather than a tool that can one-shot to a final result." That keeps users in the director's chair while Underlord handles the tedious work. "There is so much more of a positive reception of cutting out the drudgery, but keeping the user and the creator in control," Mistratov said.

The numbers tell a similar story. Agent users export at an 8.6% higher rate than non-agent users and make nearly 50% more edits per export, suggesting Underlord isn't replacing the creative process but deepening it. Over 30% of Descript projects now involve agentic editing at some point in the project lifecycle.

## Looking to the future

Descript's thesis was that building a generalized agent with broad context and low-level tools would let them ride improvements in frontier model intelligence. That bet has paid off: when Descript upgraded from Opus 4.5 to 4.6, quality metrics improved across the board on offline evals—with no changes to the agent harness. Opus 4.6 was also their fastest model integration yet: half a day from release to understanding the model's strengths and weaknesses. The team is now focused on multi-turn success metrics, moving beyond single-query evaluations to understanding how well the agent performs across entire collaborative editing sessions.

For the Descript team, the most meaningful impact isn't efficiency gains for power users. It's expanding who can make videos in the first place.

“Underlord might make a pro user who produces five videos a week much more efficient,” Mellon said. “But it’s an even bigger unlock for the teacher who wants to make engaging content for their students but doesn’t have the time to learn complex NLE software, or the time-constrained small business owner who wants to elevate their brand messaging.”

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
