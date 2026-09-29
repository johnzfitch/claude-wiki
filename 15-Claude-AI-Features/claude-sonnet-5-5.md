---
title: "Introducing Claude Sonnet 5.5 \\ Anthropic"
source_url: "https://www.anthropic.com/claude-sonnet-5-5"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:32:45Z"
tags: ["claude-ai"]
---

# Claude Sonnet 5.5

September 28, 2026

1.  [(1)Introduction](#introduction)
2.  [(2)Performance and cost](#performance)
3.  [(3)Safety](#safety)
4.  [(4)Getting started](#availability)

Skip intro

Scroll down

Introducing Claude Sonnet 5.5, the second model in the Claude 5.5 family. It’s a clear upgrade over Claude Sonnet 5, runs 30%+ faster, and costs up to 30% less for most work.

Sonnet 5.5 is a faster, lower-cost complement to Claude Opus 5.5. Where Opus 5.5 is built for complex work requiring careful judgment, Sonnet 5.5 is strongest at well-scoped everyday tasks, fixing bugs, and creating polished documents, slides, and spreadsheets. It’s also got a sharp eye for design. Claude Haiku 5.5, built for high-volume and cost-sensitive applications, will join the Claude 5.5 family in the coming weeks.

Sonnet 5.5 improves over Sonnet 5 on:

**Performance.** Sonnet 5.5 scores 70.6% on Terminal-Bench 4.0, an agentic coding evaluation, compared to Sonnet 5’s 10.3%. It scores two points below Opus 5.5 on GDPval-AA, a test of real-world work across a variety of occupations. And it’s strong on long-horizon work and image understanding—it’s the first Sonnet model to beat *Pokémon Red* working only from screenshots.

**Collaboration.** Like Opus 5.5, Sonnet 5.5 writes more clearly than our previous generation of models; early testers described it as a better partner for collaboration than Sonnet 5. Its speed also makes it well suited to fast iteration on less complex tasks.

**Cost.** Sonnet 5.5 is priced the same as Sonnet 5 at \$2 per million input tokens, \$10 per million output tokens, and \$0.20 per million tokens for cache reads, but it typically needs far fewer tokens to do the same work. In our testing, it costs up to 30% less per task than its predecessor.

**Speed.** Sonnet 5.5 generates outputs 30%+ faster than Sonnet 5, making it our fastest Sonnet model to date.

**Alignment and safety.** On our automated behavioral audit, Sonnet 5.5 improves on or matches Sonnet 5 on most measures of alignment. Because its cybersecurity capabilities are comparable to Opus 5’s, it’s the first Sonnet model to launch with cyber safeguards and fallbacks like those we’ve developed for our most capable models. Its biology safeguards are the same as Sonnet 5’s. Both safeguards target a narrow set of high-risk requests; routine software development and most life sciences work are unaffected.

## Performance

Sonnet 5.5 improves on Sonnet 5 across domains—in some cases dramatically. On several evaluations, Sonnet 5.5 at Max effort even performs comparably to Opus 5.5. However, benchmark scores capture only one facet of a model’s capabilities; in our own testing, and in that of external testers, Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment.

The charts below plot each model’s score against its cost per task at every effort level. As effort goes up, models typically work for longer, leading to a higher cost per task but generally also a higher score. The closer a point is to the top left of the chart, the more capability it delivers per dollar.

On several benchmarks, Sonnet 5.5 at Low or Medium effort beats Sonnet 5’s best score for about a tenth of the cost per task. It complements Opus 5.5 best when running at lower effort settings, where it costs less per task. At higher settings, it can perform comparably at a similar cost.

Agentic terminal coding

Agentic coding: FrontierCode

Agentic coding: CursorBench

Knowledge work: AA-Briefcase

Agentic terminal codingAgentic coding: FrontierCodeAgentic coding: CursorBenchKnowledge work: AA-Briefcase

## Coding

Sonnet 5.5’s jump in performance is particularly noticeable in coding. At High effort on FrontierCode, it scores 10 points higher than Sonnet 5 at the same setting, at about one fifteenth of the cost per task. On CursorBench, which tests models on tasks from real Cursor coding sessions, its best score is within about two points of Opus 5.5.

Early testers appreciated how quickly Sonnet 5.5 can understand a codebase. They were also struck by its efficiency: in head-to-head runs, it batched tool calls together more than Sonnet 5, leading to fewer steps and lower costs.

Epic Games

Every

CodeRabbit

SpaceXAI

Base44

Unity

Creator

Epic GamesEveryCodeRabbitSpaceXAIBase44UnityCreator

Quote

> “In Epic’s early testing, Claude Sonnet 5.5 cleared the same quality bar you’d expect from a higher-tier model, holding up on a system design audit and a data flow review. The new model managed tens of thousands of lines of code for gameplay system architecture, kept responses snappy, handled multi-hour tasks, and delivered with less prescriptive prompting.”

CompanyEpic Games

AuthorDaniel Vogel, Chief Operating Officer

Quote

> “Claude Sonnet 5.5 cooks. Fast at coding and can be steered quickly in iterative workflows. But it can still work long if it needs to. It’s got some of Opus 5.5’s natural writing upgrades, which makes it more fun to work with.”

CompanyEvery

AuthorTyler Nishida, Designer

Quote

> “Claude Sonnet 5.5 shows better judgment than Sonnet 5 across different levels of complexity, while spending significantly fewer output tokens. Sonnet 5’s tendency to reach for web search too often and its high token use are both gone in this new model. We plan to move simple and moderate reviews over now, and more in the coming weeks.”

CompanyCodeRabbit

AuthorDavid Loker, VP of AI

Quote

> “Claude Sonnet 5.5 delivers frontier-level performance on CursorBench 4.0 at 55.5%, second only to Opus 5.5. We think it will be a hit with developers looking to balance performance with cost.”

CompanySpaceXAI

AuthorSualeh Asif, Director of ML

Quote

> “Across 118 real app builds, Claude Sonnet 5.5 produced apps that scored level with Opus 5. It got there in 3.6 iterations per build on average, where Opus 5 took 7.7. It had the fewest failed tool calls of any model we compared. It also rarely stopped mid-build to ask the user a question, so fewer builds stall waiting on someone to answer.”

CompanyBase44

AuthorGabriel Grinberg, AI Engineering Lead

Quote

> “At Unity, we have a high bar for task completion. Projects are reopened and results are checked at runtime, so a task only counts when the change works, not when the model says it’s done. The majority of Claude Sonnet 5.5’s work passed that check. It also completed 90% of tasks in our multi-step Unity Editor and coding benchmark, beating similar models.”

CompanyUnity

AuthorSam Zhang, Creative Technologist

Quote

> “When Claude Opus 5.5 sets the architecture and general framework for a game, I would feel confident in letting Sonnet 5.5 implement it. I’m impressed with Sonnet 5.5’s handling of long-running, complex tasks.”

CompanyCreator

AuthorKevin Ngo, Creative Coder

## Knowledge work

Sonnet 5.5 shows gains in multiple areas of knowledge work. On GDPval-AA, which tests models on real-world tasks across 44 occupations and nine major industries, Sonnet 5.5 scores nearly level with Opus 5.5 and about 400 points above Sonnet 5. It’s close to Opus 5.5 in computer use and chart recognition, and clearly outperforms Sonnet 5 and GPT-6 Sol on long-horizon knowledge work.

Early testers highlighted less quantifiable improvements. They found it to be a more natural conversational partner and remarked on its knack for design, noting that it adds polish to user interfaces and can follow slide templates to create decks that require minimal editing. In one internal test, we gave it a public company’s quarterly earnings materials and call transcripts, along with a slide template, and asked for a 10-slide operating review. Two experts judged its first draft to be ready to send as is.

Slack

Zendesk

Balyasny Asset Management

Box

Lovable

Atlassian

SlackZendeskBalyasny Asset ManagementBoxLovableAtlassian

Quote

> “Without changing any of our prompts, Claude Sonnet 5.5 did better than Sonnet 5 on almost all of our offline Slackbot evals, in fewer steps and with about 14% fewer output tokens. When someone gives Slackbot a task, quality and speed are what matter most, and Sonnet 5.5 allows Slackbot to deliver better outcomes for users, faster.”

CompanySlack

AuthorCurtis Allen, Principal Engineer

Quote

> “We fed Claude Sonnet 5.5 hundreds of real support use cases across replies and escalation requests. It made fewer wrong decisions and resolved tickets faster than the Claude models we use in production today. Tickets were processed 20% faster, getting our customers the help they need without the wait.”

CompanyZendesk

AuthorAbhinay Kathuria, Director of AI

Quote

> “On our private suite of 2,441 finance tasks covering Q&A, extraction, analysis, and forecasting, Claude Sonnet 5.5 scored ahead of Sonnet 5 and used about 121k tokens per answer, where Sonnet 5 used 497k. On our analyst search and retrieval work, it was better than Sonnet 5 in almost every way. For high-volume workflows, it had the best quality-to-cost tradeoff of the seven models we ran.”

CompanyBalyasny Asset Management

AuthorJoe Poirier, Senior AI Engineer

Quote

> “Claude Sonnet 5.5 will give our customers in financial services and healthcare the confidence to use it for their most sensitive work. Sonnet 5.5 rechecks data in source documents, catching errors that Sonnet 5 failed to spot. Compared to the last model, Sonnet 5.5 was more accurate, 2.4x faster, and used 12% fewer total tokens.”

CompanyBox

AuthorYashodha Bhavnani, VP of AI Products

Quote

> “Claude Sonnet 5.5 thinks in fewer, more robust steps, so builders wait less to see progress. Our coding evals showed a third fewer tool calls and roughly half the shell runs to finish a task. For everyday coding and higher-effort conversations, that means faster iteration and a smoother build loop.”

CompanyLovable

AuthorFabian Hedin, Co-founder and CTO

Quote

> “With millions of Rovo-assisted actions powering our customers’ workflows each month, execution speed is critical. Claude Sonnet 5.5 will allow teams to run their Rovo Agents up to 30% faster than they could with Sonnet 5. I am excited to offer customers this choice.”

CompanyAtlassian

AuthorJamil Valliani, Head of Product, AI

## Cost and speed

Pricing

|                     |                       |                 |
|---------------------|-----------------------|-----------------|
| Price per 1M tokens | **Claude Sonnet 5.5** | Claude Opus 5.5 |
| Cache reads         | \$0.20                | \$0.20          |
| Cache writes        | \$2.50                | \$5             |
| Input tokens        | \$2                   | \$4             |
| Output tokens       | \$10                  | \$20            |

Sonnet 5.5 requires fewer tokens per task than Sonnet 5, so it’s less expensive to run. It also generates output 30%+ faster, and its efficiency is immediately noticeable:

Creating murmurations

Shaping sand dunes

Building a clock of clocks

Sonnet 5

Sonnet 5.5

Prompt:

A murmuration of 400 starlings in one HTML file

Sonnet 5

Sonnet 5.5

Prompt:

Wind shaping sand dunes in one HTML file

Sonnet 5

Sonnet 5.5

Prompt:

A clock made of 24 small clocks in one HTML file

Sonnet 5

Sonnet 5.5

Sonnet 5

Sonnet 5.5

Adjusting the [effort level](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code) lets you balance cost and speed against overall quality. In Claude Code and our apps, the default effort is set to Medium, while the Claude Platform defaults to High. At lower settings, Claude answers faster and uses fewer tokens, which suits routine work. At higher settings, Claude reasons for longer and checks its work more thoroughly.

## Safety

### Alignment

Sonnet 5.5 doesn’t advance the frontier of our models’ capabilities, so our alignment assessment focused on a targeted set of risks that apply to models of any capability level, including acting against users’ interests, misleading users, and cooperating with high-stakes misuse.

On our automated behavioral audit, which tests Claude across roughly 1,850 scenarios, Sonnet 5.5 improves on or matches Sonnet 5 on most measures of alignment, resistance to misuse, and honesty. On our newer containment evaluations, Sonnet 5.5 comes close to Opus 5.5, the best model we tested, in how rarely it tries to escape its sandbox, and it’s the least likely of any of our models to probe the limits of its containers. Across the full audit, Opus 5.5 still performs slightly better overall, but we found no evidence that Sonnet 5.5 pursues goals that conflict with the user’s intention.

As we described in our [recent alignment assessment](../19-Reference/alignment-assessment-cybersecurity-incidents.md), no set of evaluations reliably catches every failure, and Sonnet 5.5 may have tendencies we haven’t found, which is why we pair our own alignment work with the safeguards described below.

### Safeguards

**Cybersecurity.** Sonnet 5.5’s cyber capabilities are a large improvement over Sonnet 5’s, so we’re deploying it with safeguards similar to those on Opus 5.5. Users can still find and fix bugs in their code as part of routine software development, but higher-risk cybersecurity tasks will visibly fall back to Sonnet 5. Soon, cyberdefenders will be able to apply to our expanded [Cyber Verification Program](../20-Models/real-time-cyber-safeguards-on-claude-opus-and-sonnet.md) for tiered access to more advanced capabilities on Sonnet 5.5, Opus 5.5, and Claude Mythos models.

**Biology.** Sonnet 5.5 uses the same set of biology safeguards as Sonnet 5. These target harmful requests; most research, education, and clinical work is unaffected, though some microbiology and virology requests may be flagged in error. Organizations can apply to our [Life Sciences Verification Program](../19-Reference/life-sciences-verification-program.md) for access to safeguards designed for the full breadth of biology-related work.

**Distillation.** Distillation attacks, in which attackers use thousands of fake accounts to extract a model’s capabilities at industrial scale, allow bad actors to create highly capable models without the safeguards we build into Claude. Because Sonnet 5.5 is far more capable than its predecessor, it’s the first Sonnet model to launch with safety classifiers that prevent reasoning extraction. Sonnet 5.5 also expands [preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md), so Claude’s thinking cannot be decoupled from the account that created it. Most developers won’t notice a change. If you move conversations between accounts, including switching accounts mid-session in Claude Code, our [docs article](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) explains the change.

## Getting started

As with Opus 5.5 and Sonnet 5, Claude Sonnet 5.5 is available with zero data retention.

Claude Sonnet 5.5 is now available on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. Developers can get started on the Claude Platform with `claude-sonnet-5-5`. If you run Sonnet with thinking off, you’ll need to switch to the new `between_tools` setting, which keeps up-front thinking off, before moving to Sonnet 5.5. See our [migration guide](../20-Models/models-sonnet-5-5-migration-guide.md#turn-thinking-off) for details.

## Footnotes

¹ Terminal-Bench 4.0 results are reported for Claude Opus 5.5 at Xhigh effort which represents the model’s highest score.

² Sonnet 5.5 scores lower at Max effort than at Xhigh. FrontierCode evaluates whether a code change could be merged without human edits. It penalizes out-of-scope changes, even if they are high-quality or helpful. At Max effort, Sonnet 5.5 more often ran Claude Code’s code-review skill, which splits the review across many subagents, and in two cases Cognition examined, this led to a timeout or to extra edits beyond the task’s scope, and therefore to a lower score.

³ Artificial Analysis ran GDPval-AA and AA-Briefcase on a pre-release deployment of Sonnet 5.5 on the Claude Platform, which we found to have a bug that could degrade responses to requests that use structured outputs. We expect the effect on Sonnet 5.5’s scores, if any, to be small and to understate its performance. That bug has since been fixed.

⁴ OpenAI recently fixed a bug that degraded image understanding in GPT-6 Sol. Official AA-Briefcase v1.1 and GDPval-AA v2.1 scores from Artificial Analysis, and Chartography scores from Surge AI, may not have been updated yet to reflect the latest version of the model. Artificial Analysis does not expect major impacts to AA-Briefcase v1.1 and GDPval-AA v2.1. Internal testing of Chartography suggests its score was not impacted.

[](https://www.anthropic.com/)

### Products

- [Claude](product-overview.md)
- [Claude Code](claude-com-product-claude-code.md)
- [Claude Code Enterprise](product-claude-code-enterprise.md)
- [Claude Cowork](product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](product-design.md)
- [Claude Science](product-claude-science.md)
- [Claude Security](product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](claude-mythos.md)
- [Fable](claude-fable.md)
- [Opus](claude-opus.md)
- [Sonnet](claude-sonnet.md)
- [Haiku](claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Sales](../18-Industry-UseCases/sales.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Developer blog](https://claude.dev)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](programs-startups.md)
- [Scientists](programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](../19-Reference/company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](../19-Reference/company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](../19-Reference/anthropic-com-research.md)
- [News](../19-Reference/news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
