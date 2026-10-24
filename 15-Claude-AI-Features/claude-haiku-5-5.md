---
title: "Introducing Claude Haiku 5.5 \\ Anthropic"
source_url: "https://www.anthropic.com/claude-haiku-5-5"
category: "15-Claude-AI-Features"
fetched_at: "2026-10-20T06:41:17Z"
tags: ["claude-ai"]
---

# Claude Haiku 5.5

1.  [(1)Performance](#performance)
2.  [(2)Pricing](#pricing)
3.  [(3)Safety](#safety)
4.  [(4)Further updates](#further-updates)
5.  Model IDCopied`claude-haiku-5-5`

Skip intro

Scroll down

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.

Claude Haiku 5.5 is designed for high-volume, cost-sensitive tasks. It reliably handles quick and repetitive workloads (like summaries, compactions, database queries, and classification requests). It pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work. And, since it’s also our fastest model to date, it works especially well for speed-sensitive tasks like live customer support and browser use.¹

Haiku 5.5 is available at a much lower price than Haiku 4.5. On average, it now costs around 75% less to run.²

Along with this launch, we’re making improvements to the value of our model range. We’re halving the price of Claude Sonnet 5.5’s cache reads, which means Sonnet 5.5 now runs around 20% cheaper on most agentic work. And we’re introducing a new monthly API credit for our Claude Max and Team subscribers, designed to support our users in building new agents and applications that run on the Claude Platform.

## Performance

Here’s how Claude Haiku 5.5 performs across a range of benchmarks:

Haiku 5.5 is our first Haiku-class model to come with an adjustable effort setting. This means that, as with our other models, users can decide whether to optimize for cost or intelligence. The charts below show how Haiku 5.5 performs on three benchmarks at each effort setting:

Computer use: OSWorld

Knowledge work: GDPval-AA

Multidisciplinary reasoning: Humanity’s Last Exam

Computer use: OSWorldKnowledge work: GDPval-AAMultidisciplinary reasoning: Humanity’s Last Exam

In early testing, our customers reported results consistent with the performance and cost improvements shown above. Here’s what they told us about the new model:

Asana

HubSpot

AlphaSense

Box

Rogo

Cognition

AsanaHubSpotAlphaSenseBoxRogoCognition

Quote

> “We’re very impressed with Claude Haiku 5.5, particularly its speed. We ran it through our eval suite for AI Teammates, our AI agent product, covering use cases like triaging bugs, setting up projects, and searching large portfolios to surface high-risk or overdue work. Compared with the model we use today, we saw over a 30% reduction in latency for task completions and up to 2.5x faster inference per agent turn. It’s a noticeably snappier experience.”

CompanyAsana

AuthorAaron Vinh, Staff Software Engineer

Quote

> “At HubSpot, we use simulated portals to evaluate new models on CRM tasks like reporting on deals. We mostly test the smaller, more efficient models, and Claude Haiku 5.5 got the best score we’ve seen on this suite yet, at 92.8% averaged over three runs. One CRM audit task asks models to identify stale but ambiguous records. Across all of the models we tested, Haiku 5.5 was fastest to complete the task, and had the highest hit rate and the lowest false positive rate.”

CompanyHubSpot

AuthorZe’ev Klapow, Distinguished Software Engineer

Quote

> “Ask in Document is one of our big sources of spend, doing about 8M calls a week in production. It answers very specific questions on top of one or a few documents. We ran 400 queries, and Claude Haiku 5.5 was a statistically significant improvement over Haiku 4.5: 0.84 vs. 0.76.”

CompanyAlphaSense

AuthorDaniel Campos, Distinguished Engineer

Quote

> “Our customers use Box AI across large volumes of their enterprise content. With widespread usage comes the need to manage efficiency and cost, and to find the best model to suit the task at hand. In early testing, Claude Haiku 5.5 scored 11 points higher than Haiku 4.5 at about half the latency. We’d put it to use on analytical work that runs at scale, from cost reports to financial summaries and weekly recurring reviews.”

CompanyBox

AuthorYashodha Bhavnani, VP of AI Products

Quote

> “The short and high-volume work is where Claude Haiku 5.5 fits for us, like quick lookups, subagents, and summaries. While a bigger model builds the deck, a Haiku 5.5 subagent goes into the 10-K and pulls the segment revenue line the deck needs. It’s accurate enough that we’d trust it there, and fast and cheap enough that we can run it a lot.”

CompanyRogo

AuthorAlex Wang, Applied AI

Quote

> “Claude Haiku 5.5 joins the sidekick lineup in Devin Fusion as an excellent option. With Haiku 5.5 as the sidekick, Fusion holds a top-tier FrontierCode score of 66.2 while cutting cost and latency. You can try it today in the Devin CLI with Opus 5.5 as the lead.”

CompanyCognition

AuthorWalden Yan, Co-Founder & CPO

## Pricing

The table below shows how Claude Haiku 5.5’s pricing compares to our other models. Haiku 5.5 is especially good value when used for tasks with prompts up to 100,000 tokens, which make up around 90% of requests to our previous Haiku model.

[TABLE]

## Safety

**Alignment.** Claude Haiku 5.5 shows major improvements across almost all of our alignment evaluations relative to Haiku 4.5. In particular, we found far fewer instances of misaligned behavior, and a lower willingness to cooperate with misuse. The model’s [system card](claude-haiku-5-5-system-card.md) describes our evaluation process and results in more detail.

**Safeguards.** Consistent with its capabilities, Haiku 5.5’s cybersecurity safeguards are more restrictive than Haiku 4.5’s, but somewhat less restrictive than those we’ve applied to other recent models. In cybersecurity, they permit a wider range of defensive tasks than our safeguards for Sonnet 5.5, but they still block penetration testing and other techniques more likely to be used by attackers.

Haiku 5.5’s biology safeguards are the same as for Sonnet 5, Sonnet 5.5, and Opus 5. They allow research biology questions but restrict access to requests that we judge as likely to cause harm. Organizations working on wider-ranging biology and cyber activities can apply to our [Life Sciences Verification Program](../19-Reference/life-sciences-verification-program.md) and [Cyber Verification Program](../19-Reference/cyber-verification-program.md).

## Availability

Claude Haiku 5.5 is available now on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. On the Claude Platform, developers can get started with `claude-haiku-5-5`.

See our [migration guide](../20-Models/models-haiku-5-5-migration-guide.md) for details.

## Further updates

Alongside our new pricing for Claude Haiku 5.5, we’re making further improvements to the value of our models and products.

First, starting today, we’re **lowering the price of cache reads on Claude Sonnet 5.5**. Cache reads now cost 50% less: \$0.10 per million tokens rather than \$0.20. Because cache reads make up a large share of models’ token consumption, this reduces the cost of Sonnet 5.5 on most agentic tasks by around 20%.

For instance, here’s what the price cut means for Sonnet 5.5’s performance relative to cost on Terminal-Bench 4.0:

This chart illustrates an important difference between Haiku 5.5 and our larger models. Sonnet 5.5 and Opus 5.5 remain better choices for complex agentic coding tasks like those measured by Terminal-Bench 4.0. By contrast, Haiku 5.5 is best suited to more narrowly scoped tasks that might otherwise have been cost-prohibitive with previous versions of Claude—like compaction, summarization, or subagent work.

Second, this week, we’ll roll out **a new monthly API credit to all Max and Team subscribers for use on the Claude Platform**. Max 5x users will get \$100 in credits per month, Max 20x users will get \$200, and Team subscribers will receive up to \$500, pooled across their users. These credits are designed to allow our users to experiment with building tools, apps, and agents that call our API. They can be used on any of our models. For more information, [see our Help Center article](https://support.claude.com/en/articles/17154008).

For developers, we’re also **updating our Claude Python and TypeScript SDKs to add support for computer use and browser use** in beta. Haiku 5.5 is especially well-suited to these tasks, given its combination of speed, capability, and price. You can read more about this [in our Claude Platform docs](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-sdk.md).

## Footnotes

¹ Claude Haiku 5.5 is our fastest model to date at each model’s standard speed, although it runs less quickly than our Opus models in Fast Mode.

² Claude Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower for requests over 100,000 tokens. On Haiku 4.5, 90% of requests fell into the former category. This calculation also accounts for changes between Haiku 4.5 and Haiku 5.5 in how many tokens are used to complete a given piece of work: Haiku 5.5 has an updated tokenizer (similar to Sonnet 5.5’s and Opus 5.5’s), which means it uses slightly more tokens per task.

[](https://www.anthropic.com/)

### Products

- [Claude](product-overview.md)
- [Claude Code](product-claude-code-fad1ab4b.md)
- [Claude Code Enterprise](product-claude-code-enterprise.md)
- [Claude Cowork](product-cowork.md)
- [@Claude](product-tag.md)
- [Claude Design](product-design.md)
- [Claude Science](product-claude-science.md)
- [Claude Security](product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Google Workspace](https://claude.com/claude-for-google-workspace)
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
- [Enterprise](../17-Billing-Plans/pricing-enterprise.md)
- [Financial advisors](../18-Industry-UseCases/financial-advisors.md)
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
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/playground.md)

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

- [Campus](programs-campus.md)
- [Frontier Academy](programs-frontier-academy.md)
- [Scientists](programs-team-plan-for-scientists.md)
- [Startups](programs-startups.md)

### Help and security

- [Availability](https://www.anthropic.com/legal/supported-regions)
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
