---
title: "Claude Opus 4.6 \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-opus-4-6"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:55Z"
tags: ["api", "news-research"]
---

# Introducing Claude Opus 4.6

Feb 5, 2026

We’re upgrading our smartest model.

The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, can operate more reliably in larger codebases, and has better code review and debugging skills to catch its own mistakes. And, in a first for our Opus-class models, Opus 4.6 features a 1M token context window in beta¹.

Opus 4.6 can also apply its improved abilities to a range of everyday work tasks: running financial analyses, doing research, and using and creating documents, spreadsheets, and presentations. Within [Cowork](https://claude.com/blog/cowork-research-preview), where Claude can multitask autonomously, Opus 4.6 can put all these skills to work on your behalf.

The model’s performance is state-of-the-art on several evaluations. For example, it achieves the highest score on the agentic coding evaluation [Terminal-Bench 2.0](https://www.tbench.ai/news/announcement-2-0) and leads all other frontier models on [Humanity’s Last Exam](https://agi.safe.ai/), a complex multidisciplinary reasoning test. On [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa)—an evaluation of performance on economically valuable knowledge work tasks in finance, legal, and other domains²—Opus 4.6 outperforms the industry’s next-best model (OpenAI’s GPT-5.2) by around 144 Elo points,³ and its own predecessor (Claude Opus 4.5) by 190 points. Opus 4.6 also performs better than any other model on [BrowseComp](https://openai.com/index/browsecomp/), which measures a model’s ability to locate hard-to-find information online.

As we show in our extensive [system card](../15-Claude-AI-Features/claude-opus-4-6-system-card.md), Opus 4.6 also shows an overall safety profile as good as, or better than, any other frontier model in the industry, with low rates of misaligned behavior across safety evaluations.

Knowledge work

Agentic search

Coding

Reasoning

In [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md), you can now assemble [*agent teams*](https://www.anthropic.com/09-Agents-Patterns/agent-teams-e29da6ed1b.md) to work on tasks together. On the API, Claude can use [*compaction*](https://www.anthropic.com/04-API-Reference/Guides/build-with-claude-compaction-47672e5bbf.md) to summarize its own context and perform longer-running tasks without bumping up against limits. We’re also introducing [*adaptive thinking*](https://www.anthropic.com/04-API-Reference/Guides/build-with-claude-adaptive-thinking-2b96627d8d.md), where the model can pick up on contextual clues about how much to use its extended thinking, and new [*effort*](https://www.anthropic.com/04-API-Reference/effort.md) controls to give developers more control over intelligence, speed, and cost.

We’ve made substantial upgrades to [Claude in Excel](https://claude.com/claude-in-excel), and we’re releasing [Claude in PowerPoint](https://claude.com/claude-in-powerpoint) in a research preview. This makes Claude much more capable for everyday work.

Claude Opus 4.6 is available today on [claude.ai](https://claude.ai/redirect/website.v1.a39e30dc-614f-4e0e-b38a-df278a6e8021), our API, and all major cloud platforms. If you’re a developer, use `claude-opus-4-6` via the [Claude API](../20-Models/about-claude-models-overview.md). Pricing remains the same at \$5/\$25 per million tokens; for full details, see our [pricing page](../17-Billing-Plans/pricing.md#api).

We cover the model, our new product updates, our evaluations, and our extensive safety testing in depth below.

## First impressions

We build Claude with Claude. Our engineers write code with Claude Code every day, and every new model first gets tested on our own work. With Opus 4.6, we’ve found that the model brings more focus to the most challenging parts of a task without being told to, moves quickly through the more straightforward parts, handles ambiguous problems with better judgment, and stays productive over longer sessions.

Opus 4.6 often thinks more deeply and more carefully revisits its reasoning before settling on an answer. This produces better results on harder problems, but can add cost and latency on simpler ones. If you’re finding that the model is overthinking on a given task, we recommend dialing effort down from its default setting (high) to medium. You can control this easily with the `/effort` [parameter](https://www.anthropic.com/04-API-Reference/effort.md).

Here are some of the things our Early Access partners told us about Claude Opus 4.6, including its propensity to work autonomously without hand-holding, its success where previous models failed, and its effect on how teams work:  

> Claude Opus 4.6 is the strongest model Anthropic has shipped. It takes complicated requests and actually follows through, breaking them into concrete steps, executing, and producing polished work even when the task is ambitious. For Notion users, it feels less like a tool and more like a capable collaborator.
>
> Sarah Sachs  
> AI Lead, Notion

> Early testing shows Claude Opus 4.6 delivering on the complex, multi-step coding work developers face every day—especially agentic workflows that demand planning and tool calling. This starts unlocking long-horizon tasks at the frontier.
>
> Mario Rodriguez  
> Chief Product Officer, GitHub

> Claude Opus 4.6 is a huge leap for agentic planning. It breaks complex tasks into independent subtasks, runs tools and subagents in parallel, and identifies blockers with real precision.
>
> Michele Catasta  
> President, Replit

> Claude Opus 4.6 is the best model we've tested yet. Its reasoning and planning capabilities have been exceptional at powering our AI Teammates. It's also a fantastic coding model – its ability to navigate a large codebase and identify the right changes to make is state of the art.
>
> Amritansh Raghav  
> Interim CTO, Asana

> Claude Opus 4.6 reasons through complex problems at a level we haven't seen before. It considers edge cases that other models miss and consistently lands on more elegant, well-considered solutions. We're particularly impressed with Opus 4.6 in Devin Review, where it's increased our bug catching rates.
>
> Scott Wu  
> CEO, Cognition

> Claude Opus 4.6 feels noticeably better than Opus 4.5 in Windsurf, especially on tasks that require careful exploration like debugging and understanding unfamiliar codebases. We’ve noticed Opus 4.6 thinks longer, which pays off when deeper reasoning is needed.
>
> Jeff Wang  
> CEO, Windsurf

> Claude Opus 4.6 represents a meaningful leap in long-context performance. In our testing, we saw it handle much larger bodies of information with a level of consistency that strengthens how we design and deploy complex research workflows. Progress in this area gives us more powerful building blocks to deliver truly expert-grade systems professionals can trust.
>
> Joel Hron  
> Chief Technology Officer, Thomson Reuters

> Across 40 cybersecurity investigations, Claude Opus 4.6 produced the best results 38 of 40 times in a blind ranking against Claude 4.5 models. Each model ran end to end on the same agentic harness with up to 9 subagents and 100+ tool calls.
>
> Stian Kirkeberg  
> Head of AI & ML, NBIM

> Claude Opus 4.6 is the new frontier on long-running tasks from our internal benchmarks and testing. It's also been highly effective at reviewing code.
>
> Michael Truell  
> Co-founder & CEO, Cursor

> Claude Opus 4.6 achieved the highest BigLaw Bench score of any Claude model at 90.2%. With 40% perfect scores and 84% above 0.8, it’s remarkably capable for legal reasoning.
>
> Niko Grupen  
> Head of AI Research, Harvey

> Claude Opus 4.6 autonomously closed 13 issues and assigned 12 issues to the right team members in a single day, managing a ~50-person organization across 6 repositories. It handled both product and organizational decisions while synthesizing context across multiple domains, and it knew when to escalate to a human.
>
> Yusuke Kaji  
> General Manager, AI, Rakuten

> Claude Opus 4.6 is an uplift in design quality. It works beautifully with our design systems and it’s more autonomous, which is core to Lovable’s values. People should be creating things that matter, not micromanaging AI.
>
> Fabian Hedin  
> Co-founder, Lovable

> Claude Opus 4.6 excels in high-reasoning tasks like multi-source analysis across legal, financial, and technical content. Box’s eval showed a 10% lift in performance, reaching 68% vs. a 58% baseline, and near-perfect scores in technical domains.
>
> Yashodha Bhavnani  
> Head of AI, Box

> Claude Opus 4.6 generates complex, interactive apps and prototypes in Figma Make with an impressive creative range. The model translates detailed designs and multi-layered tasks into code on the first try, making it a powerful starting point for teams to explore and build ideas.
>
> Loredana Crisan  
> Chief Design Officer, Figma

> Claude Opus 4.6 is the best Anthropic model we’ve tested. It understands intent with minimal prompting and went above and beyond, exploring and creating details I didn’t even know I wanted until I saw them. It felt like I was working with the model, not waiting on it.
>
> Paulo Arruda  
> Staff Engineer, Shopify

> Both hands-on testing and evals show Claude Opus 4.6 is a meaningful improvement for design systems and large codebases, use cases that drive enormous enterprise value. It also one-shotted a fully functional physics engine, handling a large multi-scope task in a single pass.
>
> Eric Simons  
> CEO, Bolt.new

> Claude Opus 4.6 is the biggest leap I’ve seen in months. I’m more comfortable giving it a sequence of tasks across the stack and letting it run. It’s smart enough to use subagents for the individual pieces.
>
> Jerry Tsui  
> Staff Software Engineer, Ramp

> Claude Opus 4.6 handled a multi-million-line codebase migration like a senior engineer. It planned up front, adapted its strategy as it learned, and finished in half the time.
>
> Gregor Stewart  
> Chief AI Officer, SentinelOne

> We only ship models in v0 when developers will genuinely feel the difference. Claude Opus 4.6 passed that bar with ease. Its frontier-level reasoning, especially with edge cases, helps v0 to deliver on our number-one aim: to let anyone elevate their ideas from prototype to production.
>
> Zeb Hermann  
> General Manager, v0, Vercel

> The performance jump with Claude Opus 4.6 feels almost unbelievable. Real-world tasks that were challenging for Opus \[4.5\] suddenly became easy. This feels like a watershed moment for spreadsheet agents on Shortcut.
>
> Nico Christie  
> Co-founder & CTO, Shortcut.ai

01 / 20

## Evaluating Claude Opus 4.6

Across agentic coding, computer use, tool use, search, and [finance](https://claude.com/blog/opus-4-6-finance), Opus 4.6 is an industry-leading model, often by a wide margin. The table below shows how Claude Opus 4.6 compares to our previous models and to other industry models on a variety of benchmarks.

Opus 4.6 is much better at retrieving relevant information from large sets of documents. This extends to long-context tasks, where it holds and tracks information over hundreds of thousands of tokens with less drift, and picks up buried details that even Opus 4.5 would miss.

A common complaint about AI models is “[context rot](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),” where performance degrades as conversations exceed a certain number of tokens. Opus 4.6 performs markedly better than its predecessors: on the 8-needle 1M variant of [MRCR v2](https://huggingface.co/datasets/openai/mrcr)—a needle-in-a-haystack benchmark that tests a model’s ability to retrieve information “hidden” in vast amounts of text—Opus 4.6 scores 76%, whereas Sonnet 4.5 scores just 18.5%. This is a qualitative shift in how much context a model can actually use while maintaining peak performance.

All in all, Opus 4.6 is better at finding information across long contexts, better at reasoning after absorbing that information, and has substantially better expert-level reasoning abilities in general.

Long-context retrieval

Long-context reasoning

Finally, the charts below show how Claude Opus 4.6 performs on a variety of benchmarks that assess its software engineering skills, multilingual coding ability, long-term coherence, cybersecurity capabilities, and its life sciences knowledge.

Root cause analysis

Multilingual coding

Long-term coherence

Cybersecurity

Life sciences

## A step forward on safety

These intelligence gains do not come at the cost of safety. On our automated behavioral audit, Opus 4.6 showed a low rate of misaligned behaviors such as deception, sycophancy, encouragement of user delusions, and cooperation with misuse. Overall, it is just as well-aligned as its predecessor, Claude Opus 4.5, which was our most-aligned frontier model to date. Opus 4.6 also shows the lowest rate of over-refusals—where the model fails to answer benign queries—of any recent Claude model.

For Claude Opus 4.6, we ran the most comprehensive set of safety evaluations of any model, applying many different tests for the first time and upgrading several that we’ve used before. We included new evaluations for user wellbeing, more complex tests of the model’s ability to refuse potentially dangerous requests, and updated evaluations of the model’s ability to surreptitiously perform harmful actions. We also experimented with new methods from [interpretability](team-interpretability.md), the science of the inner workings of AI models, to begin to understand why the model behaves in certain ways—and, ultimately, to catch problems that standard testing might miss.

A detailed description of all capability and safety evaluations is available in the [Claude Opus 4.6 system card](../15-Claude-AI-Features/claude-opus-4-6-system-card.md).

We’ve also applied new safeguards in areas where Opus 4.6 shows particular strengths that might be put to dangerous as well as beneficial uses. In particular, since the model shows enhanced cybersecurity abilities, we’ve developed six new cybersecurity [probes](next-generation-constitutional-classifiers.md)—methods of detecting harmful responses—to help us track different forms of potential misuse.

We’re also accelerating the cyber*defensive* uses of the model, using it to help find and patch vulnerabilities in open-source software (as we describe in our new [cybersecurity blog post](https://red.anthropic.com/2026/zero-days/)). We think it’s critical that cyberdefenders use AI models like Claude to help level the playing field. Cybersecurity moves fast, and we’ll be adjusting and updating our safeguards as we learn more about potential threats; in the near future, we may institute real-time intervention to block abuse.

## Product and API updates

We’ve made substantial updates across Claude, Claude Code, and the Claude Platform to let Opus 4.6 perform at its best.

**Claude Platform**

On the API, we’re giving developers better control over model effort and more flexibility for long-running agents. To do so, we’re introducing the following features:

- **Adaptive thinking.** Previously, developers only had a binary choice between enabling or disabling extended thinking. Now, with [adaptive thinking](https://www.anthropic.com/04-API-Reference/Guides/build-with-claude-adaptive-thinking-2b96627d8d.md), Claude can decide when deeper reasoning would be helpful. At the default effort level (high), the model uses extended thinking when useful, but developers can adjust the effort level to make it more or less selective.
- **Effort.** There are now four [effort](https://www.anthropic.com/04-API-Reference/effort.md) levels to choose from: low, medium, high (default), and max. We encourage developers to experiment with different options to find what works best.
- **Context compaction (beta).** Long-running conversations and agentic tasks often hit the context window. [Context compaction](https://www.anthropic.com/04-API-Reference/Guides/build-with-claude-compaction-47672e5bbf.md) automatically summarizes and replaces older context when the conversation approaches a configurable threshold, letting Claude perform longer tasks without hitting limits.
- **1M token context (beta).** Opus 4.6 is our first Opus-class model with 1M token context. Premium pricing applies for prompts exceeding 200k tokens (\$10/\$37.50 per million input/output tokens), available only on the Claude Platform.
- **128k output tokens.** Opus 4.6 supports outputs of up to 128k tokens, which lets Claude complete larger-output tasks without breaking them into multiple requests.
- **US-only inference.** For workloads that need to run in the United States, [US-only inference](https://www.anthropic.com/04-API-Reference/Guides/build-with-claude-data-residency-6c8e324ea6.md) is available at 1.1× token pricing.

**Product updates**

Across Claude and Claude Code, we’ve added features that allow knowledge workers and developers to tackle harder tasks with more of the tools they use every day.

We’ve introduced [agent teams](https://www.anthropic.com/09-Agents-Patterns/agent-teams-e29da6ed1b.md) in Claude Code as a research preview. You can now spin up multiple agents that work in parallel as a team and coordinate autonomously—best for tasks that split into independent, read-heavy work like codebase reviews. You can take over any subagent directly using Shift+Up/Down or [tmux](https://github.com/tmux/tmux/wiki).

Claude now also works better with the office tools you already use. Claude in Excel handles long-running and harder tasks with improved performance, and can plan before acting, ingest unstructured data and infer the right structure without guidance, and handle multi-step changes in one pass. Pair that with Claude in PowerPoint, and you can first process and structure your data in Excel, then bring it to life visually in PowerPoint. Claude reads your layouts, fonts, and slide masters to stay on brand, whether you’re building from a template or generating a full deck from a description. Claude in PowerPoint is now available in research preview for Max, Team, and Enterprise plans.

#### Footnotes

\[1\] The 1M token context window is currently available in beta on the Claude Developer Platform only.

\[2\] Run independently by Artificial Analysis. [See here](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) for full methodological details.

\[3\] This translates into Claude Opus 4.6 obtaining a higher score than GPT-5.2 on this eval approximately 70% of the time (where 50% of the time would have implied parity in the scores).

- For GPT-5.2 and Gemini 3 Pro models, we compared the best reported model version in the charts and table.
- **Terminal-Bench 2.0**: We report both scores reproduced on our infrastructure and published scores from other labs. All runs used the Terminus-2 harness, except for OpenAI’s Codex CLI. All experiments used 1× guaranteed / 3× ceiling resource allocation and 5–15 samples per task across staggered batches. See system card for details.
- **Humanity’s Last Exam**: Claude models run “with tools” were run with web search, web fetch, code execution, programmatic tool calling, context compaction triggered at 50k tokens up to 3M total tokens, max reasoning effort, and adaptive thinking enabled. A domain blocklist was used to decontaminate eval results. See system card for more details.
- **SWE-bench Verified:** Our score was averaged over 25 trials. With a prompt modification, we saw a score of 81.42%.
- **MCP Atlas:** Claude Opus 4.6 was run with max effort. When run at high effort, it reached an industry-leading score of 62.7%.
- **BrowseComp**: Claude models were run with web search, web fetch, programmatic tool calling, context compaction triggered at 50k tokens up to 10M total tokens, max reasoning effort, and no thinking enabled. Adding a multi-agent harness increased scores to 86.8%. See system card for more details.
- **ARC AGI 2:** Claude Opus 4.6 was run with max effort and a 120k thinking budget score.
- **CyberGym**: Claude models were run on no thinking, default effort, temperature, and `top_p`. The model was also given a “think” tool that allowed interleaved thinking for multi-turn evaluations.
- **OpenRCA**: For each failure case in OpenRCA, Claude receives 1 point if all generated root-cause elements match the ground-truth ones, and 0 points if any mismatch is identified. The overall accuracy is the average score across all failure cases. The benchmark was run on the benchmark author’s harness, graded using their official methodology, and has been submitted for official verification.

\[Feb 23, 2026\] Updated reported score for Opus 4.6 for HLE with tools (53.1% to 53.0%). The update was caused by running an improved cheating detection pipeline which flagged 3 additional instances of cheating that our original pipeline had missed.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

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
- [Claude in Chrome](https://claude.com/claude-in-chrome)
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
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
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
