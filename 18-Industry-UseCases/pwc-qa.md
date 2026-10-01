---
title: "PwC Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pwc-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:33:44Z"
tags: ["case-studies", "claude-code", "enterprise", "security"]
---

# How PwC trained 400 consultants on Claude Code in a single session

[Contact sales](https://www.claude.com/contact-sales)

Industry:  
Professional services

Company size:  
Large

Product:  
[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Enterprise](enterprise.md)

Location:  
North America

6 weeks → 2.5 days

Legacy code analysis compressed

30,000-person training rollout

underway across PwC

6 weeks → 2.5 days

Legacy code analysis compressed

[Pricewaterhouse Coopers](https://www.pwc.com/us/en.html), or PwC, is a global professional services firm offering audit, tax, and consulting services to businesses and organizations worldwide. PwC and Anthropic [recently announced an expanded alliance](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html), driving impact across client work and the firm. Partner Ussama Baggili leads legacy and mainframe modernization at PwC, where he built systemized Claude Code workflows that have spread to a firm-wide training initiative. We spoke with Baggili about why PwC puts business users on Claude Code from day one and how a single training session got 400 leaders and consultants building apps in under an hour, and what that means for the firm.

## Anthropic: You've been one of the more active Claude Code users inside PwC. What were you trying to solve when you started?

**Ussama Baggili, PwC:** Everybody's trying to figure out how to get ahead with AI, but not everybody is able to use AI effectively. Claude is giving us the ability to re-energize the AI mindset in our people. It's a lot more relatable. People feel that they're getting to results faster that are both higher fidelity and also more in tune with where they're going.

We have these blind spots in our organization that we weren't able to connect. Claude Code is how we started connecting those.

What we're trying to do is get people thinking differently by treating Claude as a capable colleague. We started with coding, which is the obvious entry point. But I discovered that a lot of what Claude Code is really good at is analysis: working through the problem before you even get to the coding part. The early realization was that the analysis itself was the deliverable. You could take it and then make it polished. And once I saw that, it changed how I thought about who should be using it.

## What do you mean by that? There's a common assumption that Claude Code is for developers and that non-technical users should start somewhere simpler.

**Baggili:** People say, "Maybe we’ll start with chat and then graduate to Claude Code. It’s too complicated for people to want to use it right away" But I think that's very limited. I think starting with Claude Code at the beginning is actually a more optimal and natural segway for continued progress into more technical realms. When we were first planning our internal training, the thought was that it’s best to use the Claude chat version. However, believing in choice and not assuming we know best how the Claude products set will be used, we decided to run the training in Claude Code CLI within VS Code to start building muscle memory on more technical usage from which point the trainees can decide which one they preferred for their regular usage.

## That's a bold bet with a non-technical audience. How did you set that up to succeed?

**Baggili:** Installing Claude Code can be complex if there are restrictions on package installations. We managed to get it down to a single-line script that people could run to get everything installed.

Then the question become, how do we get 400 people to pace through a real training in about an hour and walk out energized? If things go wrong on the install, if they stumble on their prompting, they may not feel the benefit of using Claude Code.

So I thought, couldn't we build a skill or plugin within the training itself that helps people pace forward as they type their prompts? Think of it as a coach plugin within Claude Code. It tells people: great, here's what we're going to take you through in this training and helps set the training structure.

Then, the second most notable thing is to coach on how to work with Claude with the outcome in mind first, and then working backwards from there. The Claude Code coach plugin is wired into a project distribution that has a [CLAUDE.md](http://claude.md) that points to a coaching workflow for Claude. It is triggered upon session start and is visible to the user upon first interaction. It walks them through the steps to ‘here's your first prompt.’

## What did the training actually walk people through?

**Baggili:** It simulates a day in the life of three key tasks we do often. One, we respond to proposals. Two, we produce functional and technical specs for the things we're going to build. And three, we build applications or mobile applications.

The coach plugin walks them through their first prompt. And within 15 to 20 minutes, people had their initial draft RFP responses ready for their review. Within another 15 to 20 minutes, they had their functional and technical draft specs. By the time we finished the hour, people were posting screenshots of the mobile apps they had built with Claude Code in the team chat.

Regardless of whether it was perfect, people walked out positive and optimistic about Claude Code and why they needed it.

## What was the reaction after the session?

**Baggili:** People were already planning what to do next. We did a round of Q&A at the end, and people said things like: ‘Monday, this is what we're doing.’ Or, ‘Tonight I'm going to talk to my teams. I need everybody on this.’

My thinking was: how do I get this to be enticing enough for people to be yearning for it, so that they could do more with it *immediately*? Not tomorrow, not next week. We had already taken down the barriers to installation, dealt with the security hurdles, and made it as frictionless as possible.

## You mentioned that the shift from coding to analysis was a turning point for you. What does that look like in your day-to-day practice?

**Baggili:** Once I started producing decks and HTML deliverables with Claude Code, clients gravitated toward them. They were no longer shelfware. Clients could click through them quickly. So what started as 100% coding work shifted toward a non-coding output that was actually more valuable for our clients.

## Can you walk through a specific example?

**Baggili:** I lead our legacy and mainframe modernization practice. We often get these projects last minute where a client says, "We run AS400," or they have an ERP system for supply chain, or a healthcare TPA system. Systems that don’t have documentation or code that nobody can read anymore because the people who wrote it are retired.

With Claude Code, if they give us access to their code, we know how to run the analysis and give you a point of view very quickly in a package that's deliverable-worthy. We can show them previous examples and say, "Don't worry, you don't have to spend a fortune to get there. We'll help you see what you need to know." You're going to have documentation now.

The crazy part is what used to be six weeks' worth of engagements is now about two and a half days of doing that. The typical discovery process required significant effort towards collecting, manually reviewing documentation, interviewing stakeholders, reviewing findings, iterating over interim-deliverables and shaping the recommendation. With Claude Claude, the majority of these activities can be performed by the agent. That’s made us very credible with clients.

## Anthropic: Where did you take it from there?

**Baggili:** That’s when I started to see other use cases. If it can do this, can it also produce all this daunting work that we don't care to do? We started systemizing our proposals and offerings with Claude skills and Claude plugins. By packaging them into a systemized way of working, we built what's essentially an executive assistant in Claude Code. If you give me any question, I give it to my executive assistant and it spits out a deck with our branding, diagrams, workflows, and content—in minutes. We also started providing it to our leaders so they could use it across the organization.

## Anthropic: What's next?

**Baggili:** Now the idea is becoming global and the question is: how do we keep this going? How do we take this across all of our offerings for our 400,000 people and repeat the success we are witnessing in the US?

30,000-person

training rollout underway across PwC

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
