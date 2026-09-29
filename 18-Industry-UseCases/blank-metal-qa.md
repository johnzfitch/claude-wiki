---
title: "Blank Metal Claude Cowork case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/blank-metal-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:57Z"
tags: ["case-studies", "claude-code", "enterprise", "security"]
---

# How Blank Metal, a lean professional services firm, runs on Claude Cowork

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Small

Product:  
[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Enterprise](enterprise.md)

Location:  
North America

+700 people trained

in Claude Code and Cowork

90% of engineering work

runs through Claude Code

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Read more](../15-Claude-AI-Features/product-cowork.md)

[Blank Metal](https://www.blankmetal.ai/) is an AI-native engineering firm that helps enterprises take AI from pilot to production. Founded in 2025, the team of 30 runs its own operations on Claude before deploying anything for a client. We spoke with Elli Rader, Chief Revenue Officer, about how the team uses Claude Cowork and Claude Code to handle business development, scheduling, and the day-to-day work of getting a company off the ground.

## Anthropic: How central is Claude to the way Blank Metal operates day to day, and which products is your team actually using?

**Elli Rader, Blank Metal:** All of us at Blank Metal are superpowered by Claude. The primary tool is Claude Cowork, which is where the team handles everything from client-facing deliverables to internal workflows to daily tasks. On the engineering side, Claude Code is where our developers live. Every engineer is fully committed to it, and it powers around 90% of the work we do across internal projects and client builds. The API is what gets deployed for client implementations.

For a small company, Claude is a structural advantage. Work that used to take days, whether that's data analysis, forecasting, or research, now gets done in minutes, and repetitive tasks that used to require someone's full attention can run in the background, which frees people up for higher-leverage work. We've built a set of internal skills to eliminate the friction points that would otherwise slow the team down, and anything that can be packaged into a reusable skill gets shared across the org, so the whole team gets faster every time someone solves a problem once. Even our brand voice and visual guidelines are embedded through skills, so everything that comes out of Cowork, such as decks, docs, and deliverables, aligns automatically rather than being applied individually. The team also builds artifacts, dashboards, and HTML-based visualizations for client presentations. At the end of the day Claude isn't just a tool we use, it's how we scale, build, and grow in a leaner way. Every person on the team is more capable because of it, and that's the whole point.

## For a while you were essentially a one-person business development operation. What was at stake as the leads started coming in?

**Rader:** We just simply wouldn't have been able to handle the volume of leads. Clients would have been very frustrated at not getting a fast response, and they would have gone elsewhere. As a new company, it's vital that we build strong relationships with the people coming to us to grow our business and theirs, so we can't afford to slip in BD operations. Claude has been an absolute lifesaver.

## Was there a specific moment when you realized Cowork was going to change how you work?

**Rader:** For me it was the day I built a lead processor plugin. That was the moment I realized how much Claude could actually do without me needing to loop in engineering every time I had an idea. That unlocked my creativity, once I saw what was possible, I just kept going. Now I have a whole list of scheduled activities and live artifacts I've built to keep myself productive. It stopped feeling like a tool and started feeling like having an extra person on the team who's always ready to help.

## Walk me through that lead processor. What did handling a lead look like before, and what does it do now?

**Rader:** With anywhere from 3 to 10 leads coming in daily, the manual version meant days of research, scoring, and data entry. The lead processor doesn't operate in isolation. It pulls from all of our plugins and custom-built skills at once, and the result is a complete picture of how well a potential client aligns with what we actually offer, without anyone piecing it together manually. When a new lead comes in, it scores a fit rating, creates the deal in HubSpot, pulls contact info, and posts a summary to Slack. A full day's volume now gets handled in a couple of hours.

The first pass took about 20 minutes to build. We're on our third version now, so roughly an hour of total development time from the beginning. We have also invested in using the plugin and considering the ways it could be improved. It saves us at least a couple of hours a day processing leads across four people.

## What else has the team built into Cowork beyond lead processing?

**Rader:** Scheduling was a big one. Before the calendar automation, the team was spending at least an hour a day manually cross-referencing a locked-down Microsoft calendar against Google Calendar just to find availability. Now it's a single prompt. We type in who we need and the name of the client, and it automatically puts holds on everyone's calendars and gives us a bulleted list to paste into an email sharing availability. When the client chooses one, we tell Claude, and it goes back to finalize the right time, invite the client, add a Zoom line, and delete all the other holds. I built it as a project in Cowork. I started it as a task, and when it began giving me errors after a couple of weeks, Claude suggested I turn it into a project, so I did.

Proposal and SOW generation is another one. What used to be a multi-hour drafting process is now a structured first draft in minutes. Competitive research on prospects gets pulled together before calls so the team walks in prepared, and afterward the conversation is analyzed by a meeting processor skill.

## You build all of this inside Cowork rather than writing custom software around it. What makes Cowork work as an operating layer, rather than just a place to chat with Claude?

**Rader:** It starts with the work, what does this actually need to do? The question we keep coming back to is can this model operate inside the workflows people already live in, or does it create another context switch? Watching Cowork roll out, on our own team and across client teams, was the structural moment: it isn't just a chat window, it's a workspace. Connectors to Salesforce, Slack, and M365 meant Claude could operate inside actual business workflows. Skills meant solutions could be packaged and shared org-wide. The Excel and PowerPoint add-ins met people inside the tools they were already living in.

## You've trained more than 700 people in Claude Code and Cowork. How have you been able to scale it?

**Rader:** We're up to about 710 as of June 1. A big part of how we've scaled that is Lectern, a real-time live training companion we built internally to run Claude Code and Cowork sessions. The presenter controls a shared session, and participants can either follow along in real time or navigate the material at their own pace. Most people run it side by side with their terminal so they can implement immediately rather than just watching a demo. You're not just learning about Claude, you're building with it at the same time. So it's Claude all the way through: Claude is training people on Claude so they can build with Claude.  
  
A good amount of our team has a lot of background in edtech. We've built tools and products that have taught millions of people, and our lead AI engineers used to be teachers.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## How do you keep up with Claude updates as a small team?

**Rader:** With Claude updates coming almost weekly, we're constantly learning what's new, rolling it into our training and builds, and working hard testing almost all of it on our internal platform, called Shippy. Powered by Claude, Shippy lets us take on work that would normally be well beyond a team our size.

We pay particular attention to what comes off the shelf from Claude, and dig deep into what needs deep customization. Our goal is to help our clients effectively use what they can without having to build and maintain a lot themselves, and also help them build tools and products that are hyper-specific to their unique needs when “off the shelf” isn’t enough.

## What's the one thing you'd tell another team getting started with Cowork?

**Rader:** Start with the [Cowork training](https://anthropic.skilljar.com/introduction-to-claude-cowork). Give teams the opportunity and support to build their own things and it will unlock a ton of their creativity that ultimately will drive better use cases.

## Related stories


### Caylent turns months of migration work into days with Claude Agent SDK


### How can a two-person fabrication studio make room for problems it’s never solved before?


### LG CNS modernizes 20-year-old enterprise systems with Claude


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
