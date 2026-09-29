---
title: "Introducing Claude Opus 5.5 \\ Anthropic"
source_url: "https://www.anthropic.com/claude-opus-5-5"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:31:20Z"
tags: ["agents", "claude-ai"]
---

# Claude Opus 5.5

September 22, 2026

1.  [(1)Introduction](#introduction)
2.  [(2)Performance and cost](#performance-and-cost-effectiveness)
3.  [(3)Safety](#safety)
4.  [(4)Availability](#availability)

Scroll down

We’re introducing Claude Opus 5.5, the first model in our new Claude 5.5 family. It performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5.

Claude Opus 5.5 is our first release since we called for [pacing the frontier](https://darioamodei.com/post/we-must-pace-the-frontier). It was tested before release by external evaluators, including [Frontier Design](https://www.imaginefrontier.com/) and [METR](https://metr.org/). On our automated behavioral audit, the most comprehensive alignment test we run, Opus 5.5 is the strongest-performing model we’ve tested to date. It also comes with the safeguards we’ve developed for our most capable models.

Here are some of the improvements you can expect from Opus 5.5:

**Performance.** Opus 5.5 is a major step up from Opus 5. It’s the new leading model, and early testers saw large jumps in performance on their most complex work. One tester completed a 680,000-line code migration in less than a day—work that would have taken an engineering team weeks. It’s good at finding and fixing inefficiencies in software: when we asked it to cut load times across every page of a web app, Opus 5.5 succeeded 39 of 40 times, while Opus 5 made smaller improvements that also altered the app’s behavior. A different tester had several Claude models build a game from a single prompt; Opus 5.5 scored higher than any other model on the strength of its graphics and polish.

**Safety.** Opus 5.5 achieves the best scores of any model to date on our automated behavioral audit, our alignment suite that tests Claude across thousands of simulated scenarios. It is much less likely than recent models to take hard-to-reverse actions or act outside the boundaries it’s been given, and it’s more resistant than Opus 5 to prompt injection. We’ve also broadened our alignment testing to cover longer tasks, impossible tasks, and scenarios modeled on real incidents, though it still has limits. Full details of our evaluation are available in the [Opus 5.5 System Card](claude-opus-5-5-system-card.md).

Because Opus 5.5 is comparable to Claude Mythos 5.1 in biology and cybersecurity, we’re deploying it with safeguards similar to those on Claude Fable 5.1. Vetted organizations can apply today to our [Life Sciences Verification Program](../19-Reference/life-sciences-verification-program.md) to use Opus 5.5 for biology research. In the coming weeks we will also be expanding access to our [Cyber Verification Program](../20-Models/real-time-cyber-safeguards-on-claude-opus-and-sonnet.md), and verified cybersecurity practitioners will be able to use Opus 5.5 for their work.

**Cost and speed.** Opus 5.5 requires less compute to serve than Opus 5, and its pricing reflects that. Our tests show that at default settings it will cost 40% less than Opus 5 on typical workloads. Input and output tokens are \$4 and \$20 per million, 20% less than Opus 5. Cache reads (which make up the majority of agentic and coding work costs) are \$0.20 per million tokens, 60% less than Opus 5. Opus 5.5 also generates output more than 30% faster than Opus 5.

In addition to the price drop, we’re increasing five-hour usage limits on Pro, Max, Team, and seat-based Enterprise plans. We’re also providing subscription users a rate limit reset, which you can now save and use whenever you choose.

**Communication.** Opus 5.5 communicates more naturally than prior models. Early testers found its writing clearer and easier to follow, which addresses some of the common feedback we heard about Opus 5. It puts the most important information up front, and its style makes it a better work partner over long sessions. As one early tester put it, “it writes the way I do.” In our own use, this has made Opus 5.5’s work easier to follow and check—which is a safety benefit as well as a practical one.

Claude Sonnet 5.5 and Claude Haiku 5.5 will follow in the coming weeks, with many of the same improvements to performance, efficiency, and safety.

## Performance and cost-effectiveness

On our benchmarks, Claude Opus 5.5 leads in agentic coding, computer use, and knowledge work. That said, at these levels of capability we’ve found that benchmark margins have become a less reliable guide to real-world differences. In our own use, the gap between Opus 5.5 and Claude Fable 5.1 is narrower than these scores suggest.

Where Opus 5.5’s advantage is very clear is efficiency. It costs less per token than Opus 5 and uses fewer tokens per task, which nets out to a 40% drop in costs.

Pricing

|                      |                     |               |
|----------------------|---------------------|---------------|
| Prices per 1M tokens | **Claude Opus 5.5** | Claude Opus 5 |
| Cache reads          | **\$0.20**          | \$0.50        |
| Input tokens         | **\$4**             | \$5           |
| Output tokens        | **\$20**            | \$25          |
| Cache writes         | **\$5**             | \$6.25        |

Fast mode for Opus 5.5 is also available in Claude Code and the Claude Platform with up to 2.5x speed. It costs \$8 per million input tokens and \$40 per million output tokens.

## Coding

Opus 5.5 is particularly good at long and sprawling jobs like codebase-wide migrations and audits. An early tester used it to audit and fix a 200,000-line codebase in under three hours, where Opus 5 took over 20 hours and used 2.5x as many tokens. In an internal test, we asked Opus 5.5 and Fable 5.1 to translate HAProxy, widely used software that balances web traffic loads across servers, from C into Rust. Both rewrites passed nearly all of HAProxy’s own regression tests, but Opus 5.5 finished in 9.5 hours compared to 12 for Fable 5.1, and cost 51% less.

Opus 5.5 delivers frontier results on agentic coding at a fraction of the cost. At its default effort level on FrontierCode, it beats GPT-6 Astra at roughly 20% of the cost per task. On Terminal Bench 4.0, it matches Astra for about 40% of the cost, while on CursorBench it beats GPT-5.6 Sol by 11 points for about a third of the cost.

Agentic terminal coding

Agentic coding: FrontierCode

Agentic coding: CursorBench

Agentic terminal codingAgentic coding: FrontierCodeAgentic coding: CursorBench

  
Our early testers reported similar efficiency and intelligence gains:


Clio

Lovable

Quantium

Spotify

Optiver

Column

Kiro


Quote

> “Developers want agents that can take on real software work and finish it. In our testing across GitHub Copilot CLI and VS Code, Claude Opus 5.5 used among the fewest tokens and steps we measured. In VS Code, it solved more terminal tasks than Opus 5 in less than half the steps. More than making individual tasks more efficient, it’s making developers’ bigger projects more achievable.”

CompanyGitHub

AuthorMario Rodriguez, Chief Product Officer

Quote

> “I handed Claude Opus 5.5 a large engineering task across six of our repositories and let it run overnight, unattended. It stayed on task for over 18 hours defining how our services talk to each other and working out how each one should apply that. Compared with Opus 5, it hit milestones faster and required minimal reworking. Its code comments were short and useful instead of long and prose-heavy. I’m struggling to find anything negative to say.”

CompanyClio

AuthorSean Heintz, Staff Software Developer

Quote

> “For Lovable builders, Opus 5.5 means faster builds with the same quality, whether you’re starting from scratch or working on a live app. It gathers context once, makes fewer and more complete edits, and doesn’t get stuck retrying, finishing in a third to half fewer steps and using significantly fewer tokens along the way.”

CompanyLovable

AuthorFabian Hedin, CTO and Co-founder

Quote

> “We tested Claude Opus 5.5 across Chat, Cowork, and Claude Code, the full range of how our teams work. A complex coding task that previously took 38 prompts over four days came in at 11 prompts over three hours, with more production-ready outputs and less rework. For our teams solving complex problems at pace, that means less time iterating and more time interrogating: testing assumptions, pressure-testing outputs, and landing on the best solution for our clients.”

CompanyQuantium

AuthorHarley Barnes, Executive Manager, AI Technology

Quote

> “With Claude Opus 5.5, we’ve seen a clear improvement in token efficiency across our internal evaluations, as we’ve been able to complete the same tasks both cheaper and faster.”

CompanySpotify

AuthorAleksandar Mitic, Senior Engineer

Quote

> “We test models on real engineering and trading-desk work. On our agentic coding tasks, Claude Opus 5.5 matched Opus 5’s quality in about half the turns, time and output tokens, cutting the cost of that workload by 40 to 50%. It posted the highest score we’ve recorded on one desk’s trading-support suite, passing tasks earlier Claude models had failed, and topped all eight models on our analysis task.”

CompanyOptiver

AuthorNoyan Tokgozoglu, Global Head of AI Engineering

Quote

> “Claude Opus 5.5 delegates to subagents far more effectively and checks its own work in creative ways. Self-verification loops feel easier to set up. It found savings opportunities in our cloud bill that previous models had missed, and in code review it caught a bug by checking external docs for a third-party integration we’d modeled wrong several commits earlier.”

CompanyColumn

AuthorMitch Fierro, Engineering

Quote

> “Every call an agent makes is time and cost a developer feels. On a public benchmark of real command-line tasks, Claude Opus 5.5 solved more than Opus 5 while making about 40% fewer calls and using half the tokens. For developers building with Kiro, that means faster, more affordable agent sessions for routine tasks and complex challenges alike. Opus 5.5 will soon be available in Kiro.”

CompanyKiro

AuthorDeepak Singh, VP of Agentic AI

## The most secure coding agent

Enterprises that use agents within their systems need to know that those agents are operating as intended, particularly when they run autonomously for many hours. Opus 5.5 has a classifier that screens every action before it runs, an open-source sandbox that security teams can audit, and code review that catches vulnerabilities before they merge.

The model itself also has stronger defenses. On prompt injection attacks, it matches or beats Opus 5 in every setting we tested, including coding, tool use, computer use, and web browsing. On a benchmark run by the AI security firm Gray Swan, Opus 5.5 ties Fable 5.1 for the lowest prompt injection success rate of any model tested.

## Knowledge work

Opus 5.5 is a reliable and adept researcher. In one internal test, we asked Opus 5.5, Fable 5.1, and Opus 5 to write a report on a company’s quarterly performance using only the information it could find on a copy of the web where the earnings release was hard to locate. An automated grader checked every figure and quote against sources. Across different effort settings, 16 out of 18 of Opus 5.5’s reports cleared our quality bar, where any invented figure or quote would have failed. Neither Fable 5.1 nor Opus 5 cleared that bar in any attempt.

It’s also strong in financial analysis and business work. Walleye Capital, an investment firm and early tester, reported that Opus 5.5 largely solved their evaluation suite on its lowest setting; on higher settings, it performed even better, noticing an error in their evaluation instructions and correcting for it. No other model had caught this error before.

In another test, we tasked both Opus 5.5 and Opus 5 with analyzing a proposed merger between two fictional HR software companies. Each built a financial model in Excel, then turned it into an executive presentation on whether the deal made sense at its price. Both models reached the same conclusions about the deal, but Opus 5.5’s model was more thorough and its presentation easier to read, while Opus 5’s had minor errors. Opus 5.5 finished in 63 minutes compared to 93 for Opus 5, and cost 50% less to produce.

On knowledge work evaluations, Opus 5.5 outperforms other models while also using fewer tokens. On GDPval-AA v2.1, a test of real-world work across 44 occupations, Opus 5.5 scores 1846 Elo, ahead of Fable 5.1 and Opus 5. At default effort (medium), Opus 5.5 beats GPT-6 Astra at max effort for about a fifth of the cost per task. It likewise outperformed other models on benchmarks measuring business workflows and large-scale data collection.

GDPval-AA v2.1

AutomationBench

WANDR

GDPval-AA v2.1AutomationBenchWANDR

  
Our customers have reported similar results. Here’s what they told us about working with the model:  
  

Deloitte Consulting LLP

Rogo

LexisNexis Legal & Professional

Walleye Capital

Hex

Thomson Reuters Labs

Hebbia

Viktor

Deloitte Consulting LLPRogoLexisNexis Legal & ProfessionalWalleye CapitalHexThomson Reuters LabsHebbiaViktor

Quote

> “Even at its lowest effort setting, Claude Opus 5.5 caught 72% of known bugs in our code reviews to Opus 5’s 56% at high effort, with fewer false alarms and a fraction of the output. On US consulting analysis, low thinking effort matched its higher thinking settings on half the output and passed our quality checks. When more lower thinking efforts are deployed in production, that’s client-ready work delivered efficiently.”

CompanyDeloitte Consulting LLP

AuthorCarl Bennett, CIO

Quote

> “Financial firms need outputs that are consistently correct. At its lowest effort setting, Claude Opus 5.5 beat Opus 5 at high effort on our BigFinance Bench with about 60% fewer output tokens. Its answers are shorter and better structured, and its slides come out denser, more in line with industry standards.”

CompanyRogo

AuthorStrib Walker, Head of Product

Quote

> “Evaluating new models is central to the multi-model approach behind the LexisNexis Legal Intelligence Engine. In our initial evaluations, Claude Opus 5.5 identified highly relevant citations consistently, demonstrated strength with statutes, and structured its answers around the central legal frameworks and key issues. These are the kinds of capabilities we look for to help our customers accomplish more with Lexis+ with Protégé.”

CompanyLexisNexis Legal & Professional

AuthorMin Chen, Chief AI Officer

Quote

> “In quant research, one wrong assumption can undermine a result. At its lowest effort setting, Claude Opus 5.5 largely solved our evaluation task. At higher settings, it went even further: it detected that the minute indexing in our own instructions was off by one and corrected for it, noting that this would cost it points with the grader. It was right, and no model we’ve tested had caught and acted on that before.”

CompanyWalleye Capital

AuthorFrank Corrao, Head of Central Equity Quant Research Engineering

Quote

> “As models get better at data work, we’re seeing more convincing-sounding conclusions the data doesn’t support. Claude Opus 5.5 keeps digging past the first plausible answer. One task in our DataBench benchmark asks whether packages were late or tracking was just slow. Opus 5 checked delivery confirmations and called tracking healthy. Opus 5.5 found the packages were late and tracking was broken too. We’re bringing it into the Hex agent for this work.”

CompanyHex

AuthorIzzy Miller, AI Engineer

Quote

> “CoCounsel combines multiple models with our content and expertise for complex legal work. With Claude Opus 5.5, we’re seeing better results in our expert evaluations and on our internal benchmarks, alongside gains in speed and token efficiency. We’re excited for customers to experience that difference in the back-and-forth with CoCounsel as a sounding board, weighing evidence and refining their thinking in ways benchmarks don’t fully capture.”

CompanyThomson Reuters Labs

AuthorOmar Bari, VP Applied Research

Quote

> “On end-to-end finance workflows graded against expert rubrics, Claude Opus 5.5 covered 86.6% of what we look for versus 60.3% for Opus 5. On retrieval evals, it achieved our best-ever citation recall with better token efficiency than Opus 5, which keeps our cost per research task in check.”

CompanyHebbia

AuthorAabhas Sharma, CTO

Quote

> “Viktor is an AI employee that lives in Slack and Microsoft Teams, so every step he takes shows up in our costs. At the same effort, Claude Opus 5.5 needs fewer steps and tool calls per task than Opus 5 and costs nearly half as much, while getting twice as many of our hardest tasks right.”

CompanyViktor

AuthorPeter Albert, Co-Founder

## Communication

We’ve made major improvements to the way Opus 5.5 writes and communicates, one of the most common areas of feedback we heard about Opus 5. Its messages are much easier to understand at a glance, which testers said helped during long working sessions. It puts the most important information up front, is less likely to use jargon or idiosyncratic phrases, and follows the writing rules you give it. We find that this makes Opus 5.5 a noticeably better collaborator. Here’s a side-by-side comparison of the two models:

Explaining a bug

Summarizing a thread

Explaining a design change

Opus 5

Opus 5.5

Opus 5

Opus 5.5

  
Our customers’ feedback supports these findings:

  
Ramp

Stripe

Box

Chicago Trading Company

Factory

RampStripeBoxChicago Trading CompanyFactory

Quote

> “Verbose, hard-to-follow output has been my biggest frustration with frontier models, and Claude Opus 5.5 fixes it. It writes like a good colleague, and follows our writing rules. A design spec came out usable with very minimal edits, and when it rewrote one of our prompts I preferred its version to my own. When it optimized our test suite, I could follow its reasoning easily and shipped the change with confidence.”

CompanyRamp

AuthorJohn Ruelas, Staff Software Engineer

Quote

> “I run long Claude Code sessions every day. On a multi-day rebase of 40 stacked pull requests, one Claude Opus 5.5 session directed a dozen more sessions and laid out every conflict plainly. On the calls that it held, it framed them clearly that after hours away I could answer in minutes. All 40 passed CI the next afternoon. It’s a substantial upgrade over Opus 5.”

CompanyStripe

AuthorCristian Rivera, Staff Software Engineer

Quote

> “Our customers use Box AI on enormous amounts of content, so speed and cost are a top priority. In our evaluations, Claude Opus 5.5 used a third of the tokens Opus 5 did, and its answers were 40% less verbose without losing accuracy. We expect that to matter a lot for teams running agents across their content in areas like financial services and the public sector.”

CompanyBox

AuthorYashodha Bhavnani, VP of AI Products

Quote

> “Overnight, Claude Opus 5.5 autonomously handled a bug in our Lakehouse services layer that I hadn’t had time to diagnose. It investigated, designed the fix, and implemented it on its own. By morning the change was done and passed our test suite. Its writing is easy to follow and more coherent than Opus 5’s. Our pull requests and user-facing docs have needed almost no editing.”

CompanyChicago Trading Company

AuthorAusten Tomek, Principal Engineer

Quote

> “Claude Opus 5.5 is the first model we’d default to at medium effort. In our testing it matched Opus 5 on high effort, while using 20 to 25% fewer output tokens. On long, messy investigations it always came back with a clear, actionable answer. This means our customers get more done for less.”

CompanyFactory

AuthorZimu Li, Member of Technical Staff

## Safety

### Pacing the frontier

Last week, our CEO, Dario Amodei, argued that [AI progress should be paced](https://darioamodei.com/post/we-must-pace-the-frontier) so that safety practices stay ahead of model capabilities. Pacing is an approach to keeping AI safe, remaining competitive with China, and realizing AI’s benefits, particularly in areas like biology and medicine.

We largely understand the risks today’s models present and are well equipped to manage them. However, more serious risks could emerge quickly as capabilities improve, and we need to prepare for them now. For that reason, our safety work takes place on two time horizons at once:

**Safety practices for current models.** The current generation of models relies on an established set of practices: extensive alignment testing, pre-release evaluation by outside organizations such as METR and Frontier Design, and safeguards matched to each model’s capabilities in high-risk areas like cybersecurity and biology. We refine these practices with each release. We believe they are appropriate to the worst risks today’s models present, and that they give us a broad, though not perfect, picture of the range of serious risks.

Additionally, we track our ability to train and evaluate aligned models, and we report on both our public and internal models in the risk reports we publish under our [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy), our voluntary framework for managing catastrophic risks from advanced AI systems.

**Preparing for future models.** We’re preparing our training and evaluation processes in anticipation of more advanced models. We’re tightening how we filter the environments used in reinforcement learning, since [flawed environments](../19-Reference/alignment-assessment-cybersecurity-incidents.md) are a major source of misaligned behavior. Additionally, we’re improving our alignment rewards and developing automated processes for producing new, diverse scenarios for safety training. And we are strengthening our [security and monitoring](../19-Reference/improving-alignment-security-efforts.md), including a focused effort to improve interpretability-based monitoring and evaluation. We hope such techniques will help reduce our reliance on auditing a model’s chain-of-thought, or the reasoning it writes out while it works.

Models with greater capabilities—such as those that can fully automate the work of AI research itself—require a higher safety standard still. Our calls for pacing were based in large part on our expectation that such models could be trained soon. For these models, we do not assume the measures described above will meet that safety standard on their own. As AI becomes more capable, public policy should play a larger role in making sure the systems people rely on are safe. That capacity takes time to build, and we’ve started to put the infrastructure in place to support it, as described in “[We Must Pace the Frontier”](https://darioamodei.com/post/we-must-pace-the-frontier) and our recent announcement with [Accenture](../19-Reference/accenture-embedded-evaluation.md); we expect to share more details on these efforts soon. We will also continue to contribute to policy discussions with government and industry, including on approaches to regulation and international coordination.

### Alignment

On our primary evaluation suite, an automated behavioral audit that assesses Claude across nearly 2,000 scenarios, Opus 5.5 scored better than any recent Claude model on nearly every measure of misaligned behavior. It’s also our strongest model on most measures of honesty.

In particular, Opus 5.5 improves over previous models on several of the behaviors that contributed to recent [cybersecurity incidents](../19-Reference/alignment-assessment-cybersecurity-incidents.md), including biased or motivated reasoning, attempting to escape a sandbox, and taking harmful actions after concluding it was in a simulated environment. In a new evaluation designed to test a model’s propensity to cross containment boundaries, Opus 5.5 attempted to circumvent boundaries around 85% less often than Opus 5 or Claude Mythos 5.1, and every attempt it made was low severity and self-reported. For teams running Claude unattended across their codebases and systems, this is just as important as raw capability.

However, as we described in our recent [alignment assessment](../19-Reference/alignment-assessment-cybersecurity-incidents.md), building evaluations that reliably catch every failure prior to deployment remains an unsolved problem. We see signs that Opus 5.5 often suspects it is being evaluated, which challenges our ability to assess how it will act in the vast variety of real-world settings it is deployed in. As these settings expand and model capabilities increase, we expect this challenge to grow, unless we make progress on interpretability. Although we are confident that Opus 5.5 shows broad improvements in the areas we are able to measure, we pair our own alignment work with the safeguards described below.

### Safeguards

As our models grow more powerful, stricter safeguards are one way we prevent new capabilities from becoming tools for misuse. Opus 5.5 is the first Opus model to launch with a similar class of safeguards to Fable 5.1 on cybersecurity, biology, and distillation, all of which fall back to another model transparently.

**Cybersecurity.** Because Opus 5.5 has extremely strong cyber capabilities, we’re applying cybersecurity safeguards to Opus 5.5 that are similar to Fable 5.1’s. Users will be able to identify and fix bugs in their code as part of the routine software development lifecycle, but most cybersecurity tasks will be re-routed to Opus 4.8.

For cyberdefenders, we’ll soon be expanding our [Cyber Verification Program](../20-Models/real-time-cyber-safeguards-on-claude-opus-and-sonnet.md) to include Opus 5.5. The new program will include three tiers for increasingly permissive trusted access, including access to Claude Mythos models. [Claude Security](../19-Reference/claude-code-security.md) is already available with access to Claude Mythos 5.1.

**Biology.** Opus 5.5 is highly capable in biology, exceeding Opus 5 and matching or beating Claude Mythos 5.1 across many areas of work. For example, Opus 5.5 achieved improvements on a long-horizon molecular prediction and design evaluation conducted in collaboration with Dyno Therapeutics, and expert red-teamers rated its scientific novelty as comparable to the best model they had tested.

For this reason, Opus 5.5 uses the same biology safeguards as Fable 5.1. To use Opus 5.5 for research and development work impeded by these safeguards, users can apply to our new [Life Sciences Verification Program](../19-Reference/life-sciences-verification-program.md), which gives vetted organizations like academic labs, startups, and pharmaceutical companies access to safeguards designed for the full breadth of biology-related work. [Interested organizations can apply here](https://claude.com/form/life-sciences-verification-program).

### Distillation

Distillation attacks, in which attackers use thousands of fake accounts to extract a model’s capabilities at industrial scale, create safety and national security risks. Distillation allows bad actors to create highly capable models without the safeguards we build into Claude. Our [September 2026 threat intelligence report](https://www.anthropic.com/threat-intelligence-report-september-2026) details the illicit distillation activity we’ve detected and disrupted so far.

Opus 5.5 is launching with preserved thinking, the anti-distillation safeguard we introduced with Fable 5.1. It stops API users from editing Claude’s prior context in an attempt to extract Claude’s reasoning. It applies to Fable 5.1 and Opus 5.5 for API accounts created on or after August 31, 2026. Our [Help Center article](../22-Safety-Policy/preserved-thinking-changing-how-the-messages-api-handles-thinking-blocks-to-protect.md) explains the change, and our [preserved thinking docs](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) show how to test and update your integrations.

### Data retention and compliance

Like previous Opus models, Opus 5.5 is available with zero data retention.

As with Fable 5.1, Opus 5.5 comes with our watermarking measures to comply with the EU AI Act, [discussed here](../19-Reference/claude-text-watermark.md). It is also no longer available with “thinking” mode switched off, as [we describe here](../20-Models/models-opus-5-5-whats-new-opus-5-5.md#thinking-cant-be-disabled).

## Availability

Claude Opus 5.5 is now available on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. On the Claude Platform, developers can [get started](../20-Models/about-claude-models-overview.md) with `claude-opus-5-5`.

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
