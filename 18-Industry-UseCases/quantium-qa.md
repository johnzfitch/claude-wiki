---
title: "Quantium Claude Enterprise case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/quantium-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:57Z"
tags: ["agents", "case-studies", "claude-code", "enterprise", "security"]
---

# Quantium scales Claude across Australia's largest enterprises

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Large

Product:  
[Claude Enterprise](enterprise.md)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)

Location:  
Asia Pacific

1,200+ Claude Enterprise users

across Quantium

91% weekly usage

across global workforce

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Read more](../15-Claude-AI-Features/product-cowork.md)

[Quantium](https://quantium.com.au/) is an AI and data analytics company headquartered in Australia, with more than 23 years of experience building AI and data solutions for retail, consumer, financial services, government, and health organizations. The firm designs, builds, and deploys AI agents for a client portfolio of large-scale enterprise clients. We sat down with Justin Spratt, Executive, AI Partnerships at Quantium, to talk about how enterprises are deploying Claude, what's blocking them, and how Quantium's own development culture has shifted.

## Anthropic: There's a lot of noise about AI disrupting consulting. What's your read on what's actually changing?

**Justin Spratt, Quantium:** Firms do face a workforce-retooling challenge. We believe there is still significant skills uplift required from the consulting firms and systems integrators to build full agentic workloads. On our side, demand for AI-native engineers and the consultants who can pair with them is increasing, not decreasing. Traditional software engineering is giving way to AI-native engineering, where engineers can spec, build, and deploy agents in days. The demand for agents over the next two to three years appears to be exponential, and someone must build and manage them to ensure economic value is delivered to the client. That's a much bigger opportunity space than the one we were operating in two years ago. The constraint isn't demand. It's change management.

## Quantium has over twenty years of data science work behind it. How does that legacy show up in your AI consulting today, and where do you see the biggest pull right now?

**Spratt:** The data science work is what gets us into the room. We've spent two decades building data assets for banks, governments, retailers, and health organizations. When AI showed up as a real category, we had the data foundation, the customer relationships, and the operational track record already in place. That mattered, because the conversations we're having now are about acting on data that we in many cases architected, built or managed.

The pull is across more verticals than people assume. Retail and financial services are the usual suspects, but mining is a meaningful growth area too. The operational safety work in remote sites is checklist-heavy and investment-rich, and it's the kind of work where careful augmentation can move the needle. The bottleneck today is actually hiring. We're bringing on roughly 100 new AI-skilled people into a 1,200+ person organization just to keep pace with what's in front of us.

## Walk us through your internal Claude footprint. Where is it deployed across the company?

**Spratt:** We've rolled [Claude Enterprise](enterprise.md) out to all our 1,200 employees, with 91% weekly usage**.** Six hundred of those are on Claude Code covering data scientists, engineers, consultants, and back office team members. Our development lifecycle is now spec-driven rather than waterfall, and that shift has come directly from how our engineers work with Claude day to day. I use Cowork myself for research summaries, automated data flows, and to run a pass across my inbox to flag what I'm missing. It means I drop fewer balls.

## A lot of enterprises came out of 2025 worried about the AI investments they'd already made. What did you see, and what's the underlying issue?

**Spratt:** There is a lot of C-level anxiety about pilots that didn't translate into value. In some cases, big deals landed inside enterprises without execution plans or transformation roadmaps attached. The technology arrived, but the people on the other side haven't been brought along far enough to extract the economic value.

We've spent 23 years building production systems in regulated environments, and one of the things you learn doing that work is that AI moves at the speed of culture. It can only go as fast as you can get people to use it. The rate-limiting factor at scale is change management, not technology. We saw that early, which is why we rolled Claude across our own organization first. That level of adoption isn't an accident. It's what happens when leadership uses the tools themselves and the rest of the organization follows.

That's why leadership role-modeling and training sit at the centre of how we work with clients. Without it, you end up with another set of pilots that look good on a slide but don't show up in the P&L.

## You've developed a specific workshop format for first conversations with CEOs, C-suite, and board executives that's been a deliberate answer to that pilot-fatigue problem. How does it work?

**Spratt:** We run a C-suite GenAI training masterclass called AI Executive Edge. It's peer-to-peer. Our leadership team runs in-person sessions for other CEOs and executives. Successful organization-wide AI adoption is led from the top. If a CEO, their leadership team, and the board aren't using the tools themselves, they can't credibly drive the agenda, and the organization slows down behind them.

AI Executive Edge came out of a pattern we kept seeing. The organizations moving the fastest, and getting the most economic value from AI, had their leadership using it for their own executive work, not just sponsoring it for others. You only see the real value when you take on the more advanced skills yourself, and then share that with your team. That's where real change and adoption start.

Our own CEO, Adam Driussi, spent significant time building his own digital twin and a digital advisory board, and that's some of the teaching material. In a session, our leadership team runs three hours of practical training directly for C-suite executives. The conversation that produces is different from the one you'd have in a pilot review. It moves from "should we invest in AI?" to "where do we deploy this next quarter?"

We've also extended AI Executive Edge to our clients, training their leadership teams to use generative AI in their own roles.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## What does Claude Code rollout look like at enterprise scale? Where does it land cleanly, and where does it get hard?

**Spratt:** It gets hard for the same reason Claude Cowork does: governance. You can't deploy Claude Code inside a listed enterprise and let an engineer use it against production data without identity mapping and access controls in place. Smaller organizations have fewer constraints, which is why pilots often happen there first. The work we're focused on is at enterprise scale, where the change management challenge is greatest.

We're in conversations right now about enterprise rollouts at scale. This work is helping the client redesign how they build software with AI in the loop. Their existing delivery cycles weren't designed for it. Once you do that strategy work, the adoption follows.

## How are you thinking about agent infrastructure for those enterprise deployments?

**Spratt:** We've moved to building agents natively on hyperscaler platforms like Amazon Bedrock and Google Agent Platform, where we hit a model garden and deploy Claude models from there. Part of that is pragmatic: enterprises default to whatever cloud they're already in, and the hyperscalers are putting real funding behind making agent workloads easy to spin up on their infrastructure.

The thing most enterprises don't realize yet is that the agent layer doesn't technically have to be tethered to the infrastructure layer. They treat it as a single decision. It isn't. Your data has to hit a model to produce value, but interoperability between the hyperscalers is real, and the more sophisticated digital-native customers we work with treat the agent layer as a separable choice. That's where data-platform partnerships matter. We have a Snowflake and Databricks relationship for that reason: the governance layer and pipelines are strong, and for those customers, data governance is a gating issue.

## Claude Cowork is the newest piece of this picture. Where does it fit for you, and what's holding broader enterprise rollout back?

**Spratt:** With the increased capability of Cowork, we're carefully weighing how we balance this with our trust obligations. Identity management is one of the major components we're thinking about. Rolling out Cowork well requires admins to actually set up their roles for knowledge workers so agents can act autonomously.Once that mapping exists, the information security guardrails fall into place. The demand for Cowork is enormous. Every CIO and CISO we talk to is asking about it.

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
