---
title: "OpusClip Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/opusclip"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:44Z"
tags: ["claude-code", "cli", "enterprise", "security"]
---

# OpusClip builds its GTM engine with Claude Code

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Code](https://claude.com/product/claude-code)[Claude Platform](https://claude.com/platform/api)

Location:  
North America

100% automated sales call review coverage

up from 5–10% manual review

\$200K+ in new pipeline

surfaced from a single customer insight

[OpusClip](https://www.opus.pro/) is an AI video clipping platform used by more than 16 million creators and media companies to turn long-form content into short-form social video. Six months ago, no one on OpusClip's B2B revenue team had written production code. Today, using Claude Code, the ten-person team builds and maintains its own call intelligence, renewal automation, and customer dashboards.

## With Claude Code, OpusClip:

- Increased sales call review coverage from 5–10% manual to 100% automated, with structured coaching briefs generated for every conversation
- Surfaced \$200K+ in new pipeline after identifying a customer support routing issue from a single call transcript that had gone undetected
- Built an ROI calculator in 60 minutes after weeks of failed internal attempts, unblocking 5 enterprise deals in the first month
- Delivered a customer dashboard prototype in one week with real data, buying the engineering team time to build the production version
- Reduced renewal brief preparation from hours to minutes per account, now fully automated and visible in HubSpot

## The challenge

## Sellers stretched thin, context scattered everywhere

OpusClip's B2B team was growing fast and running into familiar pain. Franz-Josef Schrepf, Head of Enterprise Revenue and Partnerships, managed six sales and customer success reps but had visibility into only a fraction of their work. "I could sit in on maybe two or three calls per week," Schrepf said. "The rest was invisible unless someone wrote up call notes, which were unreliable and often missed the most important details."

With so few calls observed, the vast majority of rep performance went unreviewed. Renewal prep meant hours of manual work per account: screenshotting dashboards, downloading contracts, pulling transcripts, copying notes. Context was scattered across five or six tools. Patterns predicting churn existed in the sales data, but no one had the bandwidth to quantify them.

By September 2025, Schrepf had spec'd out a GTM software stack to address these gaps: revenue intelligence, sales engagement, data enrichment, signal providers, CRM middleware. Combined, the tools would have cost six figures and taken months to roll out, with significant overlap between vendors. In October, Schrepf started experimenting with Claude Code.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](/product/claude-code)

## The solution

## Selecting Claude Code for GTM engineering

OpusClip's engineering team was already using Claude Code, but no one had brought it to the GTM side of the business. When Schrepf saw what was possible, the software procurement conversation shifted. “Claude Code made more sense for us than buying more software,” said Blake Umlauf, GTM Engineer. “For a small team like ours, it lets us move quickly and build lightweight tools, creating workflows that fit the way we work."

For Umlauf, what made Claude Code work as a building tool was how it handled existing code. "It actually read my existing scripts before writing new ones," he said. “It behaved like a teammate who'd read the repo, not a stranger pasting snippets."

What tipped the decision was what happened when the team started feeding call transcripts into Claude Code. It surfaced a conversation where the customer had tried to upgrade their plan six times in two weeks but kept getting routed incorrectly by OpusClip's support chatbot. The customer signed a \$20K annual plan that same day, and once the routing issue was fixed, the channel generated more than \$200K in additional pipeline.

## From call transcripts to cross-functional intelligence

The core workflow is call intelligence. The weekly revenue report runs as a two-step process. First, a custom Zoom MCP server the team built with Claude Code pulls all external call transcripts automatically. Claude Code spawns parallel subagents that distill each call into a structured summary. A second session gathers those summaries along with data from HubSpot, Linear, and internal call transcripts, then writes an eight-section executive brief with coaching briefs per rep and sections tailored for product, marketing, and GTM. The whole process takes about 15 minutes.

The move from Claude Opus 4.5 to 4.6 made a practical difference: the larger context window means the team can feed in multiple call transcripts and data exports in a single session. MCP servers connect Claude Code to HubSpot, Mixpanel, Zoom, Linear, Clay, and n8n.

Now, feature requests surface with exact customer quotes and deal sizes attached, automatically mapped to Linear tickets. Competitive intelligence reaches product marketing from calls they were never on. The BDR team gets ICP patterns distilled from conversations they didn’t have.

“Claude will feed back the top 10 decisions I need to make this week, flag topics for my 1-on-1s with team members, and surface cross-functional updates,” Schrepf said. "Suddenly the dots between sales, product, marketing, and CS connected themselves."

The team also used Claude Code to build an ROI calculator for live sales calls. Schrepf fed the transcripts from internal meetings to Claude Code and asked it to design the calculator. Within 60 minutes, it produced a spreadsheet calculator the sales team now uses daily, detailed enough to build a business case but simple enough for customers to experiment with. It unblocked five deals in the first month.

Every workflow follows the same methodology. Each new use case starts with unstructured data: screenshots, CSVs, text files dragged into Claude Code. Once the output is validated, the process is turned into a Claude Code skill and uploaded to a shared GitHub repo. The skill includes the instructions, so it teaches the process as it runs it. When someone runs /renewal-analysis, Claude Code shows a checklist: upload the contract PDF, admin dashboard screenshot, user export CSV. Minutes later, the team has a structured renewal brief with a health scorecard, risk assessment, pricing options, and call prep scripts. No separate training doc needed.

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

[Read more](https://claude.com/blog/skills)

## The outcome

## Revenue leaders writing production workflows

The tools the GTM team built weren't handed down from engineering. "I'm a revenue leader, not an engineer," Schrepf said. "I've never written production code. But after a few weeks with Claude Code, I was building workflows that my team uses daily."

The shift extended across the team. Umlauf went from BDR to GTM Engineer and is now the most engaged person on the team. Revenue Operations manager Patrick Donnelly automated manual renewal prep and now focuses on customer health scoring and pipeline automation. The shared GitHub repo of skills now doubles as onboarding. New team members clone it on day one and immediately have access to /renewal-analysis, /morning-brief, /call-coaching, and every workflow the team has built. The tool teaches the process as it runs it.

## What’s next

OpusClip's next step is moving from on-demand workflows to proactive ones: agents that flag risks and surface insights continuously, rather than waiting for a slash command or a scheduled report. The team is actively building toward three use cases: an agent that triages inbound campaign replies by classifying intent and drafting responses in each AE’s voice; a pre-call research agent that listens for new calendar events and drops a brief into the meeting 12 hours before it happens; and a CSM account-health watcher that monitors usage, support, and CRM data continuously and surfaces churn risk or expansion opportunity before either side has asked. "We've already validated the workflows," Schrepf said. "Now we want them running continuously."

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
