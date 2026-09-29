---
title: "Claude in Slack: Tag @Claude in any thread | Claude by Anthropic"
source_url: "https://www.claude.com/product/tag"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-25T06:30:58Z"
tags: ["prompting", "slack"]
---

# Tag Claude in Slack

@Claude reads threads, understands full context, and reacts in real time so your team moves forward together. Bring Claude into your channel.

Add to Slack

[Add to Slack](https://api.anthropic.com/integrations/v1/slack/install)

Add to Slack

Read documentation

[Read documentation](https://claude.com/docs/claude-tag/overview)

Read documentation

Available in beta for Claude Enterprise and Team customers in Slack.

[Play video](#)

Play video

“Rather than using AI on my computer or in my own IDE, I can now do work out in the open in a public Slack channel with my teammates, and we can actually more effectively collaborate on tasks together.”

Micah Stairs, Head of Support Engineering

“Claude Tag solved two problems at once: the interface and the data access piece. My whole team now has Claude as a teammate to ask about our code, docs and support conversations right in Slack, where they already work, and we manage what it can access in one place.”

George Dilthey, Head of Support

“Claude Tag is our first responder for internal bugs. It reads incoming reports, looks at screenshots of failures, and uses access to Datadog, Linear, and GitHub to weed out user errors, trace root cause, and often draft a fix PR. Our engineers’ first reaction was ‘this is amazing.’”

Aabhas Sharma, CTO

“Claude Tag turned a summer of conference logistics — the follow-ups and chasing that always fell through the cracks — into an events program that runs itself while I stay on strategy.”

Matthew Scott, Product Marketing

“Claude Tag doesn’t just do the work — it challenges our thinking, provokes better questions, and elevates our judgement rather than replacing it. And we still feel very much in control throughout.”

Simon Mansfield, Director, Enterprise AI

“There were no skeptics on our team. Everyone leaned in from day one — it felt like Claude Tag in Slack was something they’d been waiting for.”

Darian Bailey, AI Engineer & Tag Admin

“Claude Tag meets our teams where they already work. Slack is the entry point for everything at Gusto, and the fact that Claude Tag is native there is huge for us. We see a lot of potential here.”

Chad Kunsman, AI Developer

[Prev](#)

Prev

0/5


Coming soon to Microsoft Teams

Tag [@Claude](https://anthropic.enterprise.slack.com/team/U08SSLN6TTL) in Teams, where it will read the conversation, understand context, and respond in real time.

Join the waitlist

[Join the waitlist](/form/claude-tag-teams-waitlist)

Join the waitlist

## How it works

Tag Claude into any thread in Slack, no matter how long or messy. It reacts to context, decisions, or open questions to help busy teams get more done.

### Tag it in

@Claude in any thread or channel and it picks up the context everyone already shares. Ask it to run the numbers, file a ticket, or organize a chaotic chat into action items. It reads the room and does the work.

Thread \#checkout-incidents

×

Marcus Nguyen 2:14 PM

@Claude checkout error rate jumped from 0.3% to 6% right after the 14:00 deploy — can you dig in and figure out what broke?

1 reply

ClaudeAGENT 2:14 PM

On it — tracing the checkout error spike since the 14:00 deploy.

✓Pulled the 14:00 deploy diff from GitHub (`#4821`)

✓Queried Datadog — 502s isolated to the `cart-service`

✓Correlated with a 5× spike in DB connection-pool timeouts

✓Compared error rates by region against rollback candidates

✱Writing root-cause summary + rollback recommendation…

To-dos as of 2:18 PM (Now)

[Open session in Claude](#)

[](#send)

### Set a schedule or let it run long tasks

Give @Claude standing instructions and it works without a mention now or in the future. Ask it to watch a channel, run a weekly digest, flag anything urgent, or page the right person.

\#revenue ⋮

Marcus Nguyen Thursday 8:55 AM

@Claude Every Monday at 9, post a pipeline update for the team — pull the latest from Salesforce.

ClaudeAGENT Thursday 8:55 AM

Got it — I'll pull the pipeline from Salesforce and post a digest every Monday at 9 AM.

Monday ▾

ClaudeAGENT 9:00 AM

**Weekly pipeline — Jun 8–14**

\$3.6M open pipeline · +\$610K WoW · 5 deals advanced.

pipeline-trend.png▾

- Beacon Corp expansion advanced to **Negotiation** — \$240K
- 2 new logos entered Discovery; 5 deals moved a stage
- Acme renewal flagged at risk — pricing pushback, exec synced Thu

[Open session in Claude](#)

[](#threads)

### It jumps in, and can tag you back

@Claude doesn't wait to be asked. It surfaces the thread that went quiet, posts when the deploy is live, and flags the decision that needs your call.

Thread \#eng-triage

×

SentryAPP 10:02 AM

**New issue** · `NullPointerException` in `CheckoutService.applyPromo()`

142 events in the last 30m · first seen 10:02 AM · 38 users affected

[View in Sentry](#)

2 replies

ClaudeAGENT 10:03 AM

Reproduced — a null promo code slips past validation and hits `applyPromo()`. Fix is a one-line guard plus a regression test.

ClaudeAGENT 10:05 AM

Opened PR [\#1247](#) with the fix. cc @Marcus Nguyen — you own `checkout`, mind reviewing?

[Open session in Claude](#)

[](#get-help)

## How teams use @Claude

Claude in Slack can share work in the format your team needs, right in the thread.

New

On-call

Catch up

Pull numbers

Draft PRs

Call prep

Active

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Search Workspace

\#prod-alerts

Message \#prod-alerts

@Claude Watch this channel, triage what comes in, and work through the backlog. Tag me only when something needs my call.

On it — watching **\#prod-alerts** now. I’ll triage what comes in and work the backlog, and only tag you when something needs your call.

🚨 `checkout-api` — p99 latency **4,812ms** (threshold 2,000ms)

env: `prod` · 3/12 hosts · started 02:06 UTC · [monitor](#) · [APM trace](#)

On it. Spike lines up with deploy `c4f1a09` (02:04) — new inventory check in `CartService.validate()` is calling `inventory-svc` per line item instead of batched. Only the 3 canary hosts have it.

✓ Paused rollout at 25%  
✓ Opened revert [\#48231](#) — merging once CI is green (~6m)  
✱ Watching p99, should recover as canaries drain

Not paging anyone. @Nathan — only flagging because the real fix (batch the inventory call) touches the pricing path you own; revert ships regardless.

[Open session in Claude](#)

### Watch what matters

@Claude can manage work in the channels your team never had bandwidth for: monitoring backlogs, triaging alerts, and surfacing what needs a human to review, so work that keeps getting pushed out can finally be completed.

## Prompt

@Claude Watch this channel, triage what comes in, and work through the backlog. Tag me only when something needs my call.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Search Workspace

\#launch-q3

Message \#launch-q3

Pushing feature freeze to Thursday. Legal needs another pass on the data handling docs.

Agreed. Also — pricing page copy is approved. Design can proceed.

Can someone loop in Compliance on the pricing copy too, or is Legal's sign-off enough?

@claude What got decided here and what's still open?

✓ Read through the channel from the top.  
✓ Sort out what's settled vs. still pending.  
✓ Write the summary.

todos as of 1:22 PM

[Open session in Claude](#)

**Decided:**

- Feature freeze moves to Thursday — Legal needs another pass on the data handling docs first.
- Pricing page copy is approved — design can proceed.

**Still open:**

- No timeline yet on when Legal's pass will be done — Thursday freeze could slip again if it runs long.
- Unclear who owns following up with Legal for status (Elena didn't assign it).

[Open session in Claude](#)

### Catch up fast

Get everything you need from a long thread in seconds. @Claude can surface decisions, open questions, and stakeholders, and you see exactly what's waiting on you.

## Prompt

@Claude What got decided here and what's still open?

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Search Workspace

Thread \#revenue-ops

×

Reply…

@Claude What are the top 20 enterprise accounts by spend, last 7 and 28 days?

✓ Pulled enterprise account spend from BigQuery for the trailing 7 and 28 days.  
✓ Ranked the top 20 by 28-day spend and charted the 7-day alongside.

todos as of 10:42 AM

[Open session in Claude](#)

Here are the top 20 enterprise accounts by spend, ranked by the trailing 28 days with the last 7 alongside.

| Rank | Account               | 7-day  | 28-day |
|------|-----------------------|--------|--------|
| 1    | Northwind Trading     | \$151K | \$512K |
| 2    | Vertex Logistics      | \$118K | \$438K |
| 3    | Helios Energy         | \$96K  | \$391K |
| 4    | Meridian Bank         | \$88K  | \$356K |
| 5    | Atlas Robotics        | \$101K | \$312K |
| 6    | Sunbeam Health        | \$64K  | \$287K |
| 7    | Cobalt Systems        | \$71K  | \$264K |
| 8    | Orion Media           | \$52K  | \$241K |
| 9    | Ironclad Security     | \$70K  | \$223K |
| 10   | Pinnacle Foods        | \$41K  | \$205K |
| 11   | Lumen Analytics       | \$63K  | \$188K |
| 12   | Cascade Retail        | \$38K  | \$171K |
| 13   | Granite Capital       | \$44K  | \$156K |
| 14   | Beacon Aerospace      | \$33K  | \$142K |
| 15   | Tideline Shipping     | \$41K  | \$129K |
| 16   | Summit Pharma         | \$24K  | \$117K |
| 17   | Verdant Agriculture   | \$33K  | \$104K |
| 18   | Quartz Semiconductor  | \$21K  | \$92K  |
| 19   | Halcyon Games         | \$29K  | \$71K  |
| 20   | Driftwood Hospitality | \$14K  | \$53K  |

top-20-enterprise-accounts-by-spend.png▾

The top 5 accounts are ~45% of enterprise spend (**\$2.0M** of **\$4.45M**). Worth watching **Atlas Robotics** and **Halcyon Games** — their last 7 days are 32% and 41% of the 28-day figure (a flat week would be ~25%), so both are accelerating.

### Pull the numbers

Ask @Claude to query your data and it posts results like metrics, benchmarks, and charts in the channel, so the whole team sees the answer and can keep asking questions right there.

## Prompt

@Claude Top 20 enterprise accounts by spend, last 7 and 28 days.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Search Workspace

\#eng-tickets

Message \#eng-tickets

Auth is throwing 502s on token refresh since the deploy. Looks like a race condition in `services/auth`.

@Claude fix the bug in this thread and open a draft PR.

Found it — race in `services/auth/token_cache.go`. Concurrent refreshes for the same subject both miss cache and the slower one overwrites the fresh token with a stale one → next request gets a 502. Deploy `a3f9c1e` exposed it by dropping the per-request mutex.

Draft PR: [\#48217](#) · CI green · +71 −12

[Open session in Claude](#)

### Build from the thread

Turn a bug report into a draft PR from the context is in the thread without ever leaving Slack. Get more done without switching tabs.

## Prompt

@Claude Fix the bug in this thread and open a draft PR.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Search Workspace

Thread \#acme-renewal

×

Reply…

@Claude I’m meeting Acme at 2 — what do I need to know?

**Acme · 2pm** — Sarah Chen (CTO, decision), Marcus Webb (VP Eng, champion)

- **Deal:** \$1.4M renewal + expansion, close Jun 30. Redlined MSA with their legal since Fri.
- **Sticking points:** EU data residency · 99.95% SLA ask · flat price on 62 overage seats
- **Usage:** +38% MoM, 312/250 seats, 2 P1s last 30d (both \<4h)
- **Watch:** “evaluating Cursor” thread in their \#eng-leads Tue — leverage, not real
- **Play:** lead with usage + support SLAs → trade EU commit (Q3) for them dropping 99.95%. Let them raise the overage.

[Deal room](#) · [last Gong recap](#)

[Open session in Claude](#)

### Prep before calls

Walk into every meeting with a full briefing. CRM notes, recent threads, and call history pulled together before you think to ask.

## Prompt

@Claude I'm meeting Acme at 2 — what do I need to know?

## Core capabilities

See what @Claude can do for your team.

### **Customizable  identities for granular governance**

The longer Claude works with your team, the more it understands how your organization thinks, how decisions get made, and who owns what.

### Memory across threads and days

Context can draw on previous conversations and memory. What happened in Monday's standup is still there on Thursday, without anyone repeating it.

### A shared resource in your channel

Claude surfaces what matters to the whole channel, not just the person who asked. Everyone sees the work, and anyone can build on it

### Proactive action instead of asking

Set a standing instruction once. Claude watches the channel, runs routines, flags what's urgent, and tags you back when something needs a decision.

### In the work and tools with you

Shape how Claude works in each channel with skills and instructions. Give it access to tools and data to take action on your behalf and post results.

### Runs tasks that take days

Hand Claude a complex task and it works while you move on to other projects. It follows up, asks for input, or comes back when it's done.

56%

fewer alerts after Claude Tag began resolving the root causes behind them

Read story

[Read story](https://claude.com/customers/carvana)

Read story

Claude on call:  
How Claude Tag serves as Anthropic’s first responder for CI/CD failures

An engineer on our Continuous Integration team walks through the agent he built that powers CI incident response at Anthropic.

Read more

[Read more](/blog/ai-ci-cd-on-call)

Read more

How Anthropic deploys Claude Tag for ad-hoc questions

Two data scientists at Anthropic walk through how Claude Tag turns Slack threads into self-service analytics, with the same governed definitions analysts use.

Read more

[Read more](/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)

Read more

Learn more about how Anthropic employees are using Claude Tag

Producing customer-ready collateral, compiling weekly issue reports, and running legal review, all where the work already happens.

Read more

[Read more](/blog/how-anthropic-employees-use-claude-tag)

Read more

[Prev](#)

Prev


## @Claude connects to your tools

Configure any tool with an API using Agent Identity. Claude can query, act, and report back in the thread where the work is happening.

Read more

[Read more](/blog/agent-identity-access-model)

Read more

## Admins stay in control

Claude acts under its own identity in your systems. Admins configure access once; everyone else just types @Claude.

### **Customizable  identities for granular governance**

Claude has its own account in your systems, not a borrowed login. Every credential’s use is logged, so "what did Claude do, and who asked for it?" always has an answer.

### Add it per channel

Decide which tools Claude can reach and read. Confine sensitive connectors to a single private channel or enable broader access for specific tools and resources. Adjust any time from the admin console.

What is Claude Tag?

Learn more about [**@Claude**](https://anthropic.enterprise.slack.com/team/U08SSLN6TTL) and what happens to the former Claude for Slack experience.

Read more

[Read more](https://support.claude.com/en/articles/15594475)

Read more

Agent identity: a new security model for autonomous, team-wide AI

Explore our new security model built for agents, not retrofitted from chatbots.

Read more

[Read more](/blog/agent-identity-access-model)

Read more

Tutorial: Working with @Claude in your workspace

Claude now works alongside your team, under its own account, in the places you already work together. You tag it in the way you'd tag anyone, or have it speak up on its own when there's something it can help with.

Read more

[Read more](/resources/tutorials/best-practices-using-claude-tag)

Read more

[Prev](#)

Prev


## Ready for a new way of working?

Add to Slack

[Add to Slack](https://api.anthropic.com/integrations/v1/slack/install)

Add to Slack

Join Teams waitlist

[Join Teams waitlist](/form/claude-tag-teams-waitlist)

Join Teams waitlist

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Capabilities

- Artifacts

  [Artifacts](/features/artifacts)
  Artifacts

- Design

  [Design](/product/design)
  Design

- Connectors

  [Connectors](/marketplace/connectors-plugins)
  Connectors

- Plugins

  [Plugins](/marketplace/plugins)
  Plugins

- Skills

  [Skills](/skills)
  Skills

Extensions

- Claude in Chrome

  [Claude in Chrome](/claude-in-chrome)
  Claude in Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Enterprise

- Overview

  [Overview](/solutions/enterprise)
  Overview

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

Use cases

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Commerce

  [Commerce](/solutions/commerce)
  Commerce

Departments

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Legal

  [Legal](/solutions/legal)
  Legal

- Sales

  [Sales](/solutions/sales)
  Sales

Industries

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Programs

- Startups

  [Startups](/programs/startups)
  Startups

- Scientists

  [Scientists](/programs/team-plan-for-scientists)
  Scientists

Developers

- Developer docs

  [Developer docs](https://code.claude.com/docs/en/overview)
  Developer docs

- Developer blog

  [Developer blog](https://claude.dev/)
  Developer blog

- Community

  [Community](/community)
  Community

- Console

  [Console](https://platform.claude.com/docs/en/home)
  Console

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

Platform

- Overview

  [Overview](/platform/api)
  Overview

- Marketplace

  [Marketplace](/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Claude Academy

  [Claude Academy](https://academy.claude.com/)
  Claude Academy

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/marketplace/service-partners)
  Service partners

Help and security

- Availability

  [Availability](https://www.anthropic.com/supported-countries)
  Availability

- Check files

  [Check files](https://claude.com/check-files)
  Check files

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Report abuse

  [Report abuse](https://claude.com/form/anthropic-content-reporting)
  Report abuse

- Security and compliance

  [Security and compliance](https://trust.anthropic.com/)
  Security and compliance

- Status

  [Status](https://status.anthropic.com/)
  Status

- Support center

  [Support center](https://support.claude.com/en/)
  Support center

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Research

  [Research](https://www.anthropic.com/research)
  Research

- Anthropic news

  [Anthropic news](https://www.anthropic.com/news)
  Anthropic news

- Policy on the AI Exponential
