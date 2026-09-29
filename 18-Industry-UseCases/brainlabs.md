---
title: "Brainlabs Claude Cowork case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/brainlabs"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:30Z"
tags: ["agents", "case-studies", "enterprise", "security", "skills"]
---

# How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Large

Product:  
[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)[Claude Enterprise](enterprise.md)

Location:  
North America

~400 Skills

authored by employees in four weeks

91% adoption rate

in North America

[Brainlabs](https://www.brainlabsdigital.com/) is a media agency with offices across the US, UK, LATAM, and APAC, running media and advertising campaigns for mid-sized and enterprise clients across industries. Over four weeks, the company rolled out Claude Cowork to its full workforce, with employees authoring hundreds of their own skills and automations.

## With Claude, Brainlabs built:

- A library of roughly 400 skills authored by employees in four weeks
- A Cowork deployment reaching about 1,000 employees across the agency
- A Notion-based repository of Cowork skills that non-developers can use directly
- A Claude-powered "skills auditor" that reviews skills to find more efficiencies and consolidate the growing library
- A Managed Agents setup inside Notion that triggers Claude when work changes state
- A "suggest a skill" process so any employee can propose a new automation

## The challenge

## Scaling repeatable work across a large agency

An agency at Brainlabs's size produces a steady cadence of campaign work with dozens of recurring workflows. The company's roughly 1,000 strategists, media planners, data scientists, and creative leads spend significant chunks of their day on repeatable work: drafting creative briefs, QA-ing media plans, pulling client reporting, summarizing campaign data. Across that many people, every team rebuilding the same things by hand starts to add up fast.

For Brainlabs's CTO Ben Vincent, the principle was simple. "If you're doing something more than three times, you should try to automate it," Vincent said. The company's CEO Dan Gilbert wanted that principle applied across the whole business, not just the engineering org. The original target was to have Claude live across the entire workforce in a week.

How to create Skills

Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

[Read more](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)

## The solution

## An authoring layer for skills

Brainlabs treated Cowork as the foundation, and skills as the layer on top. Over four weeks, Cowork went live across the workforce, with workshops to walk strategists, planners, and creative leads through how Claude could plug into the tools they were already using.

For skills, Brainlabs needed an authoring layer the same audience could actually use. The company made Notion the home for its org-wide skills library: employees store skills directly inside Notion, where the company’s knowledge base, meeting notes, and team workflows already sit. Notion packages each Skill and pushes it to GitHub for revision, while the Notion page stays as the source of truth.

"We've made all of them open,” Vincent said. “Anyone in the company can go in and read the details of any skill.” A "suggest a skill" process gave any employee a way to propose a new automation without going through engineering, and an org-wide skills guideline set the bar for quality. The rollout to get Claude live across the whole company took four weeks, during which time roughly 400 skills landed in the library.

The library spans the agency’s full range of work. Two examples Brainlabs has invested in heavily: an SEO audit skill, refined across thousands of iterations from the SEO team and built on a context layer drawn from over a decade of agency work; and a brand skill that produces presentation decks, social graphics, and one-pagers that stay on-brand without a designer in the loop. The audit skills alone number in the dozens, each with its own context layer.

Keeping the quality bar high as the library grew into the hundreds required a second piece, and Brainlabs built it as a skill itself: an auditor that reviews every other skill for duplication, overlapping instructions, and token inefficiency, then proposes consolidations and rewrites. “The skills auditor checks: have you done this in a clean way, is it concise?” Vincent explained. “We built it after versions 2, 3, and 4 of the library got unwieldy from over-enthusiastic agent creation across the company.” The team is also using the analytics API to see which skills are actually getting used inside chains of thought, so the library can grow on the basis of evidence rather than enthusiasm.

Security and governance were handled the same way, cautiously, and in stages. Data stays isolated by design: a Skill only pulls what the person running it is already authorized to access. Every skill also has a designated owner who reviews and approves changes before it goes live, so quality and access controls keep pace as the library grows.  
  
The newest addition sits on top of all of this. Brainlabs is one of the early customers running Managed Agents inside Notion. "We use actions. We get them to look at the Notion boards, and when something is happening it fires off to Claude," Vincent said. One example is a task agent called Get Stuff Done that works tickets on a Kanban-style board: a Notion agent tags a task with “Claude” when it judges the work complex enough, and the managed agent picks it up from there, drawing on the company’s skills library and connectors to Slack, Google Calendar, and other platforms to produce outputs like PowerPoints and research documents.

The team has put the agent to work on its own projects, including managing the Cowork rollout itself. The team is also evaluating the Claude Agent SDK for more complex server-side agents that would sit alongside the Notion-hosted ones.

Skills explained

Where do Skills fit in the Claude stack alongside prompts, Projects, MCP, and subagents? Learn what tool to use when—and how they work together.

[Read more](https://claude.com/blog/skills-explained)

## The outcome

## ~400 skills in four weeks, with agents on top

Four weeks after the rollout began, Brainlabs employees had authored roughly 400 skills covering everything from presentation-building to client reporting, with the library still growing as more people determined which parts of their own work fit the "more than three times" rule. Cowork sits underneath all of it, with about 1,000 employees handing off recurring tasks inside the tools they already use and picking up finished work on the other side. "We're automating all the mundane tasks so employees can do the more strategic things," Vincent added.

For Dan Gilbert, Brainlabs’s Global CEO, the biggest gains have been in the depth and consistency of the work itself. SEO audits used to vary in quality depending on which strategist ran them. The SEO audit skill changed that. “It’s one skill, refined across thousands of iterations from our SEO team, that captures the full universe of what to look for and what good looks like,” Gilbert said. “It doesn’t rely on what any one strategist happens to remember on the day.” Client reporting saw the same shift. “The strategists in the loop spend their hours on judgement, prioritization, and client strategy instead of mechanical assembly,” Gilbert added. For clients, this lands as a different service, not a faster one, with real-time coverage and expanded capability that wasn't possible before.

Writing tasks see the same lift agency-wide, which matters because writing is a daily part of almost everyone’s job at Brainlabs. Cowork is preloaded with the company’s style guide and each person’s individual writing style, so drafts come out around 80% of the way there in Brainlabs’s voice rather than starting from a blank page. “That’s a real quality lift, especially for people whose core job isn’t writing,” Gilbert said.

Vincent uses Cowork as his own ideation tool. “I have a bunch of random ideas that I never have the time to explore,” Vincent explained. “Now I can write the idea down in Cowork, and Claude will go investigate, build me a document, and I have all the information I need.” With Managed Agents now firing inside Notion when work changes state, Brainlabs is seeing what proactive, not just reactive, automation looks like inside a working agency.

For Vincent, this is the foundation, not the finish line. "I think it's going to go so far beyond where we are now," Vincent said. "We're going to have a bunch of agents hosted in a variety of places, which will expand our team's capabilities for the deep strategic work that grows our clients' businesses.”

## Related stories


### Caylent turns months of migration work into days with Claude Agent SDK


### How can a two-person fabrication studio make room for problems it’s never solved before?


### LG CNS modernizes 20-year-old enterprise systems with Claude


### How Blank Metal, a lean professional services firm, runs on Claude Cowork

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
