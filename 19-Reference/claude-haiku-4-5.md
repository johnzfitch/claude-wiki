---
title: "Introducing Claude Haiku 4.5 \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-haiku-4-5"
category: "19-Reference"
fetched_at: "2026-08-02T05:42:14Z"
tags: ["evaluation", "news-research"]
---

# Introducing Claude Haiku 4.5

Oct 15, 2025

Claude Haiku 4.5, our latest small model, is available today to all users.

What was recently at the frontier is now cheaper and faster. Five months ago, Claude Sonnet 4 was a state-of-the-art model. Today, Claude Haiku 4.5 gives you similar levels of coding performance but at one-third the cost and more than twice the speed.

Claude Haiku 4.5 even surpasses Claude Sonnet 4 at certain tasks, like using computers. These advances make applications like [Claude for Chrome](http://claude.ai/redirect/website.v1.d04b0990-b985-4566-9eee-370b16e01c60/chrome) faster and more useful than ever before.

Users who rely on AI for real-time, low-latency tasks like chat assistants, customer service agents, or pair programming will appreciate Haiku 4.5’s combination of high intelligence and remarkable speed. And users of Claude Code will find that Haiku 4.5 makes the coding experience—from multiple-agent projects to rapid prototyping—markedly more responsive.

Claude Sonnet 4.5, released [two weeks ago](claude-sonnet-4-5.md), remains our frontier model and the best coding model in the world. Claude Haiku 4.5 gives users a new option for when they want near-frontier performance with much greater cost-efficiency. It also opens up new ways of using our models together. For example, Sonnet 4.5 can break down a complex problem into multi-step plans, then orchestrate a team of multiple Haiku 4.5s to complete subtasks in parallel.

Claude Haiku 4.5 is available everywhere today. If you’re a developer, simply use claude-haiku-4-5 via the Claude API. Pricing is now \$1/\$5 per million input and output tokens.

##  Benchmarks

> Claude Haiku 4.5 hit a sweet spot we didn't think was possible: **near-frontier coding quality with blazing speed and cost efficiency**. In Augment's agentic coding evaluation, it achieves 90% of Sonnet 4.5's performance, matching much larger models. We're excited to offer it to our users.
>
> Guy Gur-Ari  
> Co-Founder

> **Claude Haiku 4.5 is a leap forward for agentic coding**, particularly for sub-agent orchestration and computer use tasks. The responsiveness makes AI-assisted development in Warp feel instantaneous.
>
> Zach Lloyd  
> Founder & CEO

> Historically models have sacrificed speed and cost for quality. Claude Haiku 4.5 is blurring the lines on this trade off: **it's a fast frontier model that keeps costs efficient** and signals where this class of models is headed.
>
> Jeff Wang  
> CEO

> **Claude Haiku 4.5 delivers intelligence without sacrificing speed**, enabling us to build AI applications that utilize both deep reasoning and real-time responsiveness.
>
> Ben Lafferty  
> Staff Engineer

> Claude Haiku 4.5 is remarkably capable—**just six months ago, this level of performance would have been state-of-the-art** on our internal benchmarks. Now it runs up to 4-5 times faster than Sonnet 4.5 at a fraction of the cost, unlocking an entirely new set of use cases.
>
> Andrew Filev  
> CEO

> Speed is the new frontier for AI agents operating in feedback loops. **Haiku 4.5 proves you can have both intelligence and rapid output**. It handles complex workflows reliably, self-corrects in real-time, and maintains momentum without latency overhead. For most development tasks, it's the ideal performance balance.
>
> Brad Axen  
> Tech Lead, AI

> Claude Haiku 4.5 **outperformed our current models on instruction-following for slide text generation**, achieving 65% accuracy versus 44% from our premium tier model—that's a game-changer for our unit economics.
>
> Jon Noronha  
> Co-Founder, Gamma

> Our early testing shows that Claude Haiku 4.5 brings efficient code generation to GitHub Copilot **with comparable quality to Sonnet 4 but at faster speed**. Already we're seeing it as an excellent choice for Copilot users who value speed and responsiveness in their AI-powered development workflows.
>
> Matthew Isabel  
> Distinguished Product Manager

01 / 08

## Safety evaluations

We ran a detailed series of safety and alignment evaluations on Claude Haiku 4.5. The model showed low rates of concerning behaviors, and was substantially more aligned than its predecessor, Claude Haiku 3.5. In our automated alignment assessment, Claude Haiku 4.5 also showed a statistically significantly lower overall rate of misaligned behaviors than both Claude Sonnet 4.5 and Claude Opus 4.1—making Claude Haiku 4.5, by this metric, our safest model yet.

Our safety testing also showed that Claude Haiku 4.5 poses only limited risks in terms of the production of chemical, biological, radiological, and nuclear (CBRN) weapons. For that reason, we’ve released it under the AI Safety Level 2 (ASL-2) standard—compared to the more restrictive ASL-3 for Sonnet 4.5 and Opus 4.1. You can read the full reasoning behind the model’s ASL-2 classification, as well as details on all our other safety tests, in the [Claude Haiku 4.5 system card](../15-Claude-AI-Features/claude-haiku-4-5-system-card.md).

## Further information

Claude Haiku 4.5 is available now on Claude Code and our apps. Its efficiency means you can accomplish more within your usage limits while maintaining premium model performance.

Developers can use Claude Haiku 4.5 on our API, Amazon Bedrock, and Google Cloud’s Vertex AI, where it serves as a drop-in replacement for both Haiku 3.5 and Sonnet 4 at our most economical price point.

For complete technical details and evaluation results, see our [system card](../15-Claude-AI-Features/claude-haiku-4-5-system-card.md), [model page](../15-Claude-AI-Features/claude-haiku.md), and [documentation](https://docs.claude.com/en/docs/about-claude/models/overview).

#### Methodology

- **SWE-bench Verified**: All Claude results were reported using a simple scaffold with two tools—bash and file editing via string replacements. We report 73.3%, which was averaged over 50 trials, no test-time compute, 128K thinking budget, and default sampling parameters (temperature, top_p) on the full 500-problem SWE-bench Verified dataset.
  - The score reported uses a minor prompt addition: "You should use tools as much as possible, ideally more than 100 times. You should also implement your own tests first before attempting the problem."
- **Terminal-Bench**: All scores reported use the default agent framework (Terminus 2), with XML parser, averaging 11 runs (6 without thinking (40.21% score), 5 with 32K thinking budget (41.75% score)) with n-attempts=1.
- **τ2-bench**: Scores were achieved averaging over 10 runs using extended thinking (128k thinking budget) and default sampling parameters (temperature, top_p) with tool use and a prompt addendum to the Airline and Telecom Agent Policy instructing Claude to better target its known failure modes when using the vanilla prompt. A prompt addendum was also added to the Telecom User prompt to avoid failure modes from the user ending the interaction incorrectly.
- **AIME**: Haiku 4.5 score reported as the average over 10 independent runs that each calculate pass@1 over 16 trials with default sampling parameters (temperature, top_p) and 128K thinking budget.
- **OSWorld**: All scores reported use the official OSWorld-Verified framework with 100 max steps, averaged across 4 runs with 128K total thinking budget and 2K thinking budget per-step configured.
- **MMMLU**: All scores reported are the average of 10 runs over 14 non-English languages with a 128K thinking budget.
- All other scores were averaged over 10 runs with default sampling parameters (temperature, top_p) and 128K thinking budget.

All OpenAI scores reported from their [GPT-5 post](https://openai.com/index/introducing-gpt-5/), [GPT-5 for developers post](https://openai.com/index/introducing-gpt-5-for-developers/), [GPT-5 system card](https://cdn.openai.com/gpt-5-system-card.pdf) (SWE-bench Verified reported using n=500), and [Terminal Bench leaderboard](https://www.tbench.ai/) (using Terminus 2). All Gemini scores reported from their [model web page](https://deepmind.google/models/gemini/pro/), and [Terminal Bench leaderboard](https://www.tbench.ai/) (using Terminus 1).


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](investigating-incidents-cybersecurity-evals.md)

### Our position on open-weights models

[Read more](position-open-weights-models.md)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](cognizant-anthropic.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
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
- [Courses](https://www.anthropic.com/learn)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
