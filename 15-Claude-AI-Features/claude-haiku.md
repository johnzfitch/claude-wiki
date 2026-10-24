---
title: "Claude Haiku \\ Anthropic"
source_url: "https://www.anthropic.com/claude/haiku"
category: "15-Claude-AI-Features"
fetched_at: "2026-10-08T06:25:30Z"
tags: ["claude-ai"]
---

# Claude Haiku 4.5

The cheapest, fastest, and most capable small model we've ever released.

[Try Claude](https://claude.ai/)[Get API access](../04-API-Reference/Other/playground.md)

## Announcements

- New
  Claude Haiku 5.5

  Oct 7, 2026

  Claude Haiku 5.5 is the fastest and most efficient model in the Claude 5.5 family, built for high-volume, cost-sensitive work.

  Read more

- Claude Haiku 4.5

  Oct 15, 2025

  Claude Haiku 4.5 is our fastest, most cost-efficient model, matching Sonnet 4’s performance on coding, computer use, and agent tasks. Claude Haiku 4.5 scores 73.3% on SWE-bench Verified, making it one of the world’s best coding models.

  Read more

- Claude 3.5 Haiku

  Oct 22, 2024

  For a similar speed to Haiku 3, Haiku 3.5 improved across every skill set and surpassed Opus 3, the largest model in our previous generation, on many intelligence benchmarks.

  Read more

## Availability and pricing

Free, Pro, Max, Team, and Enterprise users can select Haiku 5.5 on Claude.ai, available on web, iOS, and Android.

For developers interested in building agents, Haiku 5.5 is available on the Claude Platform natively, and in Amazon Web Services, Google Cloud, and Microsoft Foundry.

Claude Haiku 5.5 is also available in Claude Code.

Pricing for Haiku 5.5 on the Claude Platform depends on prompt length. For prompts up to 100K tokens, it is \$0.10 per million input tokens and \$0.50 per million output tokens. For prompts over 100K tokens, it is \$0.50 per million input tokens and \$2.50 per million output tokens. You can save up to 90% with [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) and 50% with [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md#pricing). To get started, use `claude-haiku-5-5` via the [Claude API](../20-Models/about-claude-models-overview.md).

## Use cases

Haiku 5.5 is fast enough for real-time experiences and efficient enough to run at volume. It works alongside larger Claude models, making it practical to add things like summarization, classification, routing, and compaction to complex products and agent systems. It is also the first Haiku with effort controls, so teams can tune cost against intelligence for each task.

### High-volume text tasks

Haiku 5.5 powers high-volume product features and natural language processing tasks like classification, summarization, and text generation. Its speed and cost make it practical for processing large volumes of content.

### Real-time experiences

Haiku 5.5 is built for latency-sensitive use cases like chat, voice agents, live support, and in-app assistants, where speed matters most.

### Subagents

Haiku 5.5 is a fast, cost-efficient subagent for coding and well-defined tasks. A more intelligent model like Fable or Opus can plan the work and hand off subtasks to Haiku, making it practical to run many agents in parallel.

### Browser and desktop automation

Haiku 5.5 is a strong computer use agent for repetitive tasks like form filling, data entry, and moving information between apps, and it is cost efficient at scale.

### Simple coding

Haiku 5.5 handles focused coding and multi-step tool use, like direct edits and small, specific changes that need to apply across many files.

## Benchmarks

Haiku 5.5 is our most capable Haiku yet, a significant step up over Haiku 4.5 across coding, tool use, computer use, and agents.

## Trust & Safety

We’ve conducted extensive testing and evaluation of Haiku 5.5 against our standards for safety, security, and reliability. In the [system card](claude-haiku-5-5-system-card.md) for this release, we discuss new safety results in several categories.

## Hear from our customers

> Ask in Document is one of our big sources of spend, doing about 8M calls a week in production. It answers very specific questions on top of one or a few documents. We ran 400 queries, and Claude Haiku 5.5 was a statistically significant improvement over Haiku 4.5, 0.84 vs. 0.76.
>
> Daniel Campos  
> Distinguished Engineer

> Our customers use Box AI across large volumes of their enterprise content. With widespread usage comes the need to manage efficiency and cost, and to find the best model to suit the task at hand. In early testing, Claude Haiku 5.5 scored 11 points higher than Haiku 4.5 at about half the latency. We’d put it to use on analytical work that runs at scale, from cost reports to financial summaries and weekly recurring reviews.
>
> Yashodha Bhavnani  
> VP of AI Products

> We’re very impressed with Claude Haiku 5.5, particularly its speed. We ran it through our eval suite for AI Teammates, our AI agent product, covering use cases like triaging bugs, setting up projects, and searching large portfolios to surface high-risk or overdue work. Compared with the model we use today, we saw over a 30% reduction in latency for task completions and up to 2.5x faster inference per agent turn. It’s a noticeably snappier experience.
>
> Aaron Vinh  
> Staff Software Engineer

> The short and high-volume work is where Haiku 5.5 fits for us, like quick lookups, subagents and summaries. While a bigger model builds the deck, a Haiku 5.5 subagent goes into the 10-K and pulls the segment revenue line the deck needs. It’s accurate enough that we’d trust it there and fast and cheap enough that we can run it a lot.
>
> Alex Wang  
> Applied AI

> At HubSpot, we use simulated portals to evaluate new models on CRM tasks like reporting on deals. We mostly test the smaller, more efficient models, and Claude Haiku 5.5 got the best score we’ve seen on this suite yet, at 92.8% averaged over three runs. One CRM audit task asks models to identify stale but ambiguous records. Across all of the models we tested, Haiku 5.5 was fastest to complete the task, and had the highest hit rate and the lowest false positive rate.
>
> Ze'ev Klapow  
> Distinguished Software Engineer

> Claude Haiku 5.5 joins the sidekick lineup in Devin Fusion as an excellent option. With Haiku 5.5 as the sidekick, Fusion holds a top-tier FrontierCode score of 66.2 while cutting cost and latency. You can try it today in the Devin CLI with Opus 5.5 as the lead.
>
> Walden Yan  
> Co-Founder & CPO

01 / 06

## Frequently asked questions

### When should I use Haiku 5.5?

Use Haiku 5.5 when speed and volume matter most. It works well as a subagent and for high-volume work like summarization, classification, and request routing, and it is fast enough for real-time experiences like chat, voice, and live support. For complex coding and knowledge work, Opus 5.5 is the daily driver, and Sonnet 5.5 is a good fit for well-scoped tasks.

### How much does it cost to use Haiku 5.5?

On the Claude Platform, Haiku 5.5 costs \$0.10 per million input tokens and \$0.50 per million output tokens for prompts up to 100K tokens, and \$0.50 per million input tokens and \$2.50 per million output tokens for prompts over 100K tokens. To learn more, check out our [pricing page](../17-Billing-Plans/pricing.md#api).

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
