---
title: "Introducing Claude 4 \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-4"
category: "19-Reference"
fetched_at: "2026-08-02T05:43:04Z"
tags: ["claude-code", "news-research"]
---

# Introducing Claude 4

May 22, 2025

Today, we’re introducing the next generation of Claude models: **Claude Opus 4** and **Claude Sonnet 4**, setting new standards for coding, advanced reasoning, and AI agents.

Claude Opus 4 is the world’s best coding model, with sustained performance on complex, long-running tasks and agent workflows. Claude Sonnet 4 is a significant upgrade to Claude Sonnet 3.7, delivering superior coding and reasoning while responding more precisely to your instructions.

Alongside the models, we're also announcing:

- **Extended thinking with tool use (beta)**: Both models can use tools—like [web search](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool)—during extended thinking, allowing Claude to alternate between reasoning and tool use to improve responses.
- **New model capabilities**: Both models can use tools in parallel, follow instructions more precisely, and—when given access to local files by developers—demonstrate significantly improved memory capabilities, extracting and saving key facts to maintain continuity and build tacit knowledge over time.
- **Claude Code is now generally available**: After receiving extensive positive feedback during our research preview, we’re expanding how developers can collaborate with Claude. Claude Code now supports background tasks via GitHub Actions and native integrations with VS Code and JetBrains, displaying edits directly in your files for seamless pair programming.
- **New API capabilities:** We’re releasing [four new capabilities](https://www.anthropic.com/news/agent-capabilities-api) on our API that enable developers to build more powerful AI agents: the code execution tool, MCP connector, Files API, and the ability to cache prompts for up to one hour.

Claude Opus 4 and Sonnet 4 are hybrid models offering two modes: near-instant responses and extended thinking for deeper reasoning. The Pro, Max, Team, and Enterprise Claude plans include both models and extended thinking, with Sonnet 4 also available to free users. Both models are available on our API, Amazon Bedrock, and Google Cloud's Vertex AI. Pricing remains consistent with previous Opus and Sonnet models: Opus 4 at \$15/\$75 per million tokens (input/output) and Sonnet 4 at \$3/\$15.

## Claude 4

Claude Opus 4 is our most powerful model yet and the best coding model in the world, leading on SWE-bench (72.5%) and Terminal-bench (43.2%). It delivers sustained performance on long-running tasks that require focused effort and thousands of steps, with the ability to work continuously for several hours—dramatically outperforming all Sonnet models and significantly expanding what AI agents can accomplish.

Claude Opus 4 excels at coding and complex problem-solving, powering frontier agent products. **Cursor** calls it state-of-the-art for coding and a leap forward in complex codebase understanding. **Replit** reports improved precision and dramatic advancements for complex changes across multiple files. **Block** calls it the first model to boost code quality during editing and debugging in its agent, *codename goose*, while maintaining full performance and reliability. **Rakuten** validated its capabilities with a demanding open-source refactor running independently for 7 hours with sustained performance. **Cognition** notes Opus 4 excels at solving complex challenges that other models can't, successfully handling critical actions that previous models have missed.

Claude Sonnet 4 significantly improves on Sonnet 3.7's industry-leading capabilities, excelling in coding with a state-of-the-art 72.7% on SWE-bench. The model balances performance and efficiency for internal and external use cases, with enhanced steerability for greater control over implementations. While not matching Opus 4 in most domains, it delivers an optimal mix of capability and practicality.

**GitHub** says Claude Sonnet 4 soars in agentic scenarios and will introduce it as the model powering the new coding agent in GitHub Copilot. **Manus** highlights its improvements in following complex instructions, clear reasoning, and aesthetic outputs. **iGent** reports Sonnet 4 excels at autonomous multi-feature app development, as well as substantially improved problem-solving and codebase navigation—reducing navigation errors from 20% to near zero. **Sourcegraph** says the model shows promise as a substantial leap in software development—staying on track longer, understanding problems more deeply, and providing more elegant code quality. **Augment Code** reports higher success rates, more surgical code edits, and more careful work through complex tasks, making it the top choice for their primary model.

These models advance our customers' AI strategies across the board: Opus 4 pushes boundaries in coding, research, writing, and scientific discovery, while Sonnet 4 brings frontier performance to everyday use cases as an instant upgrade from Sonnet 3.7.

## Model improvements

In addition to extended thinking with tool use, parallel tool execution, and memory improvements, we’ve significantly reduced behavior where the models use shortcuts or loopholes to complete tasks. Both models are 65% less likely to engage in this behavior than Sonnet 3.7 on agentic tasks that are particularly susceptible to shortcuts and loopholes.

Claude Opus 4 also dramatically outperforms all previous models on memory capabilities. When developers build applications that provide Claude local file access, Opus 4 becomes skilled at creating and maintaining 'memory files' to store key information. This unlocks better long-term task awareness, coherence, and performance on agent tasks—like Opus 4 creating a 'Navigation Guide' while playing Pokémon.

Finally, we've introduced thinking summaries for Claude 4 models that use a smaller model to condense lengthy thought processes. This summarization is only needed about 5% of the time—most thought processes are short enough to display in full. Users requiring raw chains of thought for advanced prompt engineering can [contact sales](https://www.anthropic.com/contact-sales) about our new Developer Mode to retain full access.

## Claude Code

Claude Code, now generally available, brings the power of Claude to more of your development workflow—in the terminal, your favorite IDEs, and running in the background with the Claude Code SDK.

New beta extensions for VS Code and JetBrains integrate Claude Code directly into your IDE. Claude’s proposed edits appear inline in your files, streamlining review and tracking within the familiar editor interface. Simply run Claude Code in your IDE terminal to install.

Beyond the IDE, we're releasing an extensible Claude Code SDK, so you can build your own agents and applications using the same core agent as Claude Code. We're also releasing an example of what's possible with the SDK: Claude Code on GitHub, now in beta. Tag Claude Code on PRs to respond to reviewer feedback, fix CI errors, or modify code. To install, run /install-github-app from within Claude Code.

## Getting started

These models are a large step toward the virtual collaborator—maintaining full context, sustaining focus on longer projects, and driving transformational impact. They come with extensive testing and evaluation to minimize risk and maximize safety, including [implementing measures](activating-asl3-protections.md) for higher AI Safety Levels like ASL-3.

We're excited to see what you'll create. Get started today on [Claude](https://claude.ai/redirect/website.v1.a6954ffe-33ae-47f0-82bb-b50bc957faf1), [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md), or the platform of your choice.

*As always, your [feedback](mailto:%20feedback@anthropic.com) helps us improve.*

#### Appendix

#### Performance benchmark data sources

- Open AI: [o3 launch post](https://openai.com/index/introducing-o3-and-o4-mini/), [o3 system card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf), [GPT-4.1 launch post](https://openai.com/index/gpt-4-1/), [GPT-4.1 hosted evals](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md)
- Gemini: [Gemini 2.5 Pro Preview model card](https://storage.googleapis.com/model-cards/documents/gemini-2.5-pro-preview.pdf)
- Claude: [Claude 3.7 Sonnet launch post](claude-3-7-sonnet.md)

#### Performance benchmark reporting

Claude Opus 4 and Sonnet 4 are hybrid reasoning models. The benchmarks reported in this blog post show the highest scores achieved with or without extended thinking. We’ve noted below for each result whether extended thinking was used:

- No extended thinking: SWE-bench Verified, Terminal-bench
- Extended thinking (up to 64K tokens):
  - TAU-bench (no results w/o extended thinking reported)
  - GPQA Diamond (w/o extended thinking: Opus 4 scores 74.9% and Sonnet 4 is 70.0%)
  - MMMLU (w/o extended thinking: Opus 4 scores 87.4% and Sonnet 4 is 85.4%)
  - MMMU (w/o extended thinking: Opus 4 scores 73.7% and Sonnet 4 is 72.6%)
  - AIME (w/o extended thinking: Opus 4 scores 33.9% and Sonnet 4 is 33.1%)

#### TAU-bench methodology

Scores were achieved with a prompt addendum to both the Airline and Retail Agent Policy instructing Claude to better leverage its reasoning abilities while using extended thinking with tool use. The model is encouraged to write down its thoughts as it solves the problem distinct from our usual thinking mode, during the multi-turn trajectories to best leverage its reasoning abilities. To accommodate the additional steps Claude incurs by utilizing more thinking, the maximum number of steps (counted by model completions) was increased from 30 to 100 (most trajectories completed under 30 steps with only one trajectory reaching above 50 steps).

#### SWE-bench methodology

For the Claude 4 family of models, we continue to use the same simple scaffold that equips the model with solely the two tools described in our prior releases [here](https://www.anthropic.com/engineering/swe-bench-sonnet)—a bash tool, and a file editing tool that operates via string replacements. We no longer include the [third ‘planning tool’](https://www.anthropic.com/engineering/claude-think-tool) used by Claude 3.7 Sonnet. On all Claude 4 models, we report scores out of the full 500 problems. Scores for OpenAI models are reported out of a [477 problem subset](https://openai.com/index/gpt-4-1/).

For our “high compute” numbers we adopt additional complexity and parallel test-time compute as follows:

- We sample multiple parallel attempts.
- We discard patches that break the visible regression tests in the repository, similar to the rejection sampling approach adopted by [Agentless (Xia et al. 2024)](https://arxiv.org/abs/2407.01489); note no hidden test information is used.
- We then use an internal scoring model to select the best candidate from the remaining attempts.

This results in a score of 79.4% and 80.2% for Opus 4 and Sonnet 4 respectively.


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
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

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
