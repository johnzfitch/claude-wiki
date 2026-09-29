---
title: "Introducing Claude Fable 5.1 and Claude Mythos 5.1 \\ Anthropic"
source_url: "https://www.anthropic.com/claude-fable-and-mythos-5-1"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:31:51Z"
tags: ["claude-ai", "search", "security"]
---

# :Claude: Fable 5.1and Mythos 5.1

[\[1\]................................................................................................................................................................Introduction](#introduction)[\[2\]................................................................................................................................................................A new performance frontier](#frontier)[\[3\]................................................................................................................................................................Scientific research](#scientific-research)[\[4\]................................................................................................................................................................Safety, security, and alignment](#safety-security-and-alignment)[\[5\]................................................................................................................................................................Claude Mythos 5.1](#mythos)

Made with Fable 5.1

We’re introducing Claude Fable 5.1 and Claude Mythos 5.1. They’re the world’s most advanced models for coding and knowledge work—and their research capabilities offer an early glimpse of how AI models will contribute to scientific progress.

Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards. Fable 5.1 is generally available, while Mythos 5.1 is available only through our trusted access programs; its safeguards are specifically designed to support work in cybersecurity and the life sciences.

Alongside its increased capabilities, Fable 5.1 takes important steps towards addressing the feedback we’ve received from customers on price, data retention, and safeguards.

**Price*.*** Fable 5.1 will cost an estimated 25% less than Fable 5 for typical workloads, wherever usage is billed by token. This is because we’re reducing our pricing on cache reads (where the model reads inputs that have already been processed and stored). For highly agentic work, the savings will often be much larger—up to approximately 45%.

**Data retention*.*** Our new system of Enterprise Frontier Safeguards (EFS) gives customers complete privacy (the same as a zero data retention policy) while still being state-of-the-art at preventing adversarial use. EFS works by storing data in cloud infrastructure controlled entirely by the customer, not Anthropic. It will be made available to enterprise customers in phases, beginning later this fall. Until EFS is available, eligible customers will be able to use Fable 5.1 with zero data retention.

**Safeguards*.*** We’ve improved our safeguards to reduce false positives (where the system flags benign content). In cybersecurity, our newest safeguards block 60% fewer false positives than before. In part, this is because Fable 5.1 can now be used to discover software vulnerabilities—though not to develop exploits for them. In biology, we’ve established an access program, developed in partnership with the US government, to enable access to Claude Mythos 5.1’s advanced biology capabilities. We expect to open enrollment for scientists soon.

## A new performance frontier

Claude Fable 5.1 sets a new standard for coding, knowledge work, and long-running problem-solving tasks. The charts below show that Fable 5.1 is capable of much higher performance than its predecessor, Fable 5. And when set to Low or Medium effort, Fable 5.1 achieves results similar to or better than Fable 5’s at a much lower cost. (Note that Fable 5.1 defaults to High effort in Claude Code, and to Medium in Claude Cowork and on Claude.ai.)

Agentic scientific research

Agentic terminal coding

Multidisciplinary reasoning

Agentic coding

Agentic scientific researchAgentic terminal codingMultidisciplinary reasoningAgentic coding

Fable 5.1 avoids shortcuts that result in poorer-quality work, and it’s smart enough to fix the root causes of software issues. For example, in testing by the investment firm Millennium, Fable 5.1 found the cause of a rare crash in its internal systems that none of its engineers (or any other model) had been able to explain after several years of trying.

Here, you can see how Fable 5.1 compares across various benchmarks:

Our early-access partners noticed these performance upgrades, and also picked up on more qualitative improvements in the model’s outputs. Here’s what they told us:

Jane Street Capital

Cognition

Millennium

MongoDB

Every

IMC

Red Hat

Rakuten

Square (Block)

Ramp

Canva

Hebbia

Plaid

Glean

iGent

Browserbase

Rogo

Shopify

Crosby

Datadog

SpaceXAI

Samaya

Jane Street CapitalCognitionMillenniumMongoDBEveryIMCRed HatRakutenSquare (Block)RampCanvaHebbiaPlaidGleaniGentBrowserbaseRogoShopifyCrosbyDatadogSpaceXAISamaya

Quote

> “In internal benchmarks, Claude Fable 5.1 solves more of our coding problems than Fable 5 or Opus 5, and achieves state of the art on trading intuition. While prior models became hard to follow the longer they worked, Fable 5.1 remains readable over long, multi-step tasks.”

CompanyJane Street Capital

AuthorCraig Falls, Head of Quantitative Research

Quote

> “We’re moving our Opus 5 traffic in Devin to Claude Fable 5.1 on launch day. It matched or edged out Fable 5 in our testing at a lower cost per task, and with the new cache read pricing a Fable-class model is finally economical for the workloads we’d kept on Opus, starting with code review.”

CompanyCognition

AuthorWalden Yan, Co-founder and CPO

Quote

> “A particular piece of code had an extremely rare crash, about one in a million runs, that nobody on our team had explained in four to five years. Every model I tried, including Fable 5, missed it. Claude Fable 5.1 was the first to find it. It disassembled an external vendor library, matched it against the core dump, and traced the crash to a bug in that library. The time it would have taken to conduct that analysis is hard to justify.”

CompanyMillennium

AuthorDamien, Senior Portfolio Manager

Quote

> “Claude Fable 5.1 built a complex prototype in about three days. It did initial research across all of our services code and documentation to produce a novel and extensible design. It then ran for hours unattended, with strong verification loops, to implement the entire prototype. I would wake up in the morning to the next phase finished, with a full visual walkthrough of what it built and clear evidence of its success.”

CompanyMongoDB

AuthorRon Sanzone, Staff Software Engineer

Quote

> “It’s friendly Fable. Fable-level intelligence, Opus-level price, Sonnet-speed. In our tests it was about twice as fast as Opus 5 and used half as many tokens, so for anyone used to using Opus as their daily driver it’s an obvious upgrade.”

CompanyEvery

AuthorDan Shipper, CEO

Quote

> “On our research suite, Claude Fable 5.1 set new best scores. On one task it came up with a novel solution along a completely different axis than we’d seen from other models or from human researchers in the past, which took its results well above the previous plateau. It's better at creative problem solving and getting that flash of insight you need to solve a difficult problem.”

CompanyIMC

AuthorMarquis Wong, Principal AI Engineer

Quote

> “As part of our ongoing evaluation of AI models, Claude Fable 5.1 delivered impressive results in our tests. Using Claude Code, it correctly identified the root cause of every broken build we tested, across all the effort levels. It also communicates more effectively than earlier Anthropic models, with updates that are more concise and easier to follow.”

CompanyRed Hat

AuthorJosh Boyer, Distinguished Engineer

Quote

> “We asked Claude Fable 5.1 to review a clinical research project for Rakuten Medical that three other frontier models had signed off on. It found a gap none of them had seen and insisted on testing it further. It then proposed a completely new hypothesis, turning a dataset we had written off into a new research direction in one afternoon. It’s the first time a frontier model like Claude has empowered us to explore new research in this way.”

CompanyRakuten

AuthorFelix Giovanni Virgo, Principal AI Engineer

Quote

> “Claude Fable 5.1 is very smart. On our 30-day simulated run-a-business eval, where the model gets full access to simulated Square tools, customers, employees, and vendors, it was far more efficient per token than Opus 5. We plan to use it to work through our most complex scenarios, the kind that used to take days of whiteboarding, so our engineering teams can keep moving fast.”

CompanySquare (Block)

AuthorWillem Avé, Global Head of Product

Quote

> “For anything research, greenfield or long-horizon, I would absolutely use Claude Fable 5.1 as the orchestrator. One unattended 38-hour run on a machine learning problem diagnosed a prior result as a label artifact, made the correction, kicked off six parallel experiments that ran overnight, and returned with a result and next steps. Given an open-ended prompt to find the highest-leverage problem nobody owned, it surfaced an unowned alert tied to a production outage, pulled the logs and prescribed the fix.”

CompanyRamp

AuthorDwight Temple, Sr. Machine Learning Engineer

Quote

> “The standout in Claude Fable 5.1 is the writing: more understandable, more meaningful, and it follows our writing guidance better. In blind tests against Fable 5, I preferred its writing and output. And in Canva Code it built a rhythm game with real music and on-beat gameplay matched to the level it generated, something no other model we tested delivered.”

CompanyCanva

AuthorDanny Wu, Head of AI

Quote

> “On our PowerPoint eval, Claude Fable 5.1 produced the best decks of any model we’ve tested, both in slide craft and in fully answering our research topic. That same completeness showed up in our Citations eval, where it had the best fact recall over financial documents. And on complex, multi-part questions, it’s the first model we’ve seen answer every part.”

CompanyHebbia

AuthorAabhas Sharma, CTO

Quote

> “We had a change that touched more than eight services across three codebases. Claude Fable 5.1 mapped the whole workflow end to end, in extremely fine detail, from the incoming service call down to the individual function and the database tables and rows, and it was accurate all the way down. We appreciated the opportunity to test the model and provide feedback, helping us prepare for a new frontier where we can increasingly rely on these tools to take on bolder initiatives.”

CompanyPlaid

AuthorAditya Gupta, Staff Software Engineer

Quote

> “Across our evaluation sets, our judges preferred Claude Fable 5.1’s answers roughly 2-to-1 over Fable 5 on everyday knowledge questions, high-intent research, and drafting and artifact work, all with improved response grounding over Fable. These results have made Fable 5.1 our go-to recommendation wherever Fable 5 was previously the choice.”

CompanyGlean

AuthorNilesh Dalvi, Engineering Lead

Quote

> “On the hardest problems we work on, Claude Fable 5.1 separates strongly from any other model we’ve tried. On a grand challenge-tier problem we‘ve used as a testbed for 18 months, it actually produced material progress. Rather than being trapped in stamp collecting, it made clear white-space connections I have yet to see elsewhere. It also optimized a compute kernel that Fable 5 had tapped out on by about 35%.”

CompanyiGent

AuthorSean Ward, Co-founder and CEO

Quote

> “On our hardest browser-agent benchmark, Claude Fable 5.1 completed 82% of tasks in about 10 minutes each, against 74% for Opus 5 and 57% for Fable 5, while using fewer tokens than either. It feels stronger than Fable 5 in every dimension we test. It also did exactly the right amount of work: never crossed a critical stop point across hundreds of measured tasks.”

CompanyBrowserbase

AuthorMiguel Gonzalez, Technical Lead

Quote

> “On our internal Finance benchmark, Claude Fable 5.1 matches Fable 5 on accuracy while using 20% fewer tokens. We also saw big gains in slide generation, with Fable 5.1 showing improvements in explaining complex data in simpler English and translating it into more banker-grade visuals.”

CompanyRogo

AuthorAlex Wang, Applied AI

Quote

> “Claude Fable 5.1 is more comfortable with long, unattended work than Fable 5. I’ve had workflows run for a long stretch without losing the plot: it keeps its own records, reprioritizes as things change, and picks up where it left off.”

CompanyShopify

AuthorBen Lafferty, Senior Staff Engineer

Quote

> “Compared to Fable 5, Claude Fable 5.1 was a massive improvement on RedlineBench, our contract redlining benchmark, improving from 47.9 to 57.0. Most of the gain came on first-turn quality, where it doubled the previous score, with substantial gains on counterparty acceptance as well. Its edits were also more concise, with smaller changes on average to the documents.”

CompanyCrosby

AuthorRaymond Lin, Member of Technical Staff

Quote

> “Claude Fable 5.1 is a leading model for our incident investigation evals, which use real production incidents to assess how effectively our agent, Bits Investigation, can produce root cause analyses. We evaluate our agent’s output against root causes identified by our engineers. In these evaluations, it has demonstrated stronger reasoning than Opus 5 and has successfully diagnosed the most complex production incidents we’ve tested.”

CompanyDatadog

AuthorDaniel Shan, Staff Engineer

Quote

> “Claude Fable 5.1 is the most capable model we’ve run on CursorBench 3.2, scoring 73.4% at max effort. We found it especially skilled at verifying its own work, allowing it to take on difficult coding tasks from start to finish.”

CompanySpaceXAI

AuthorSualeh Asif, Director of ML

Quote

> “We evaluate models and systems on real-world investor workflows. On FrontierFinance, our latest finance benchmark, Claude Fable 5.1 shows a clear gain over Fable 5, with a 55.9% rubric score compared to 49.2%. The gain comes from its ability to dig harder into grounded, authoritative sources: on one earnings question, it went straight to the call transcript and captured the exact figures management cited, where other models leaned on secondary coverage.”

CompanySamaya

AuthorYuhao Zhang, Research Lead

## Scientific research

We tested the scientific research capabilities of Claude Fable 5.1 and Claude Mythos 5.1 across a wide range of domains. What we found—which includes the early examples we share below—adds to the evidence that AI models will soon make important contributions to scientific discovery.

**Molecular design*.*** Many modern medicines work by binding to targets within the body to block, activate, or deliver something to them. High-affinity binders are necessary for drugs to work at lower doses; designing one is the first step in the development process for many common drug modalities. To see how well Claude Mythos 5.1 could do at this task, we gave the model access to open-source protein design and folding tools and sent its designs to two external organizations for experimental validation. Mythos 5.1 proved able to design very high-affinity binders. On three targets, ^(\[3\]) its binding affinities were 10 times higher than the best designs submitted to [Adaptyv Bio’s protein design competitions](https://proteinbase.com/competitions). Its hit rate (that is, the number of designs that were viable binders) was the strongest we’ve measured to date: it reached nearly 50% across 12 targets. (Hit rates of 10–15% are typical in protein design today.)

**Computational analysis and modeling**. Claude Fable 5.1 trained a neural network to create a new, high-resolution elevation map of a third of the planet Venus. Its work was based on radar images taken by NASA’s Magellan mission more than 30 years ago and a [map](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2012EO120002) that already existed for one-fifth of the planet. Claude’s new map now reveals details down to two to three kilometers, rather than 10 to 20, and shows heights up to 25% more accurately than before.

We’re [releasing this map](https://zenodo.org/records/22164484) under a Creative Commons license in advance of upcoming NASA VERITAS and ESA EnVision missions, in hopes that it might help them determine which geologic features to target for future observation.

**Computational biology*.*** In computational biology, it’s common to run task-specific machine learning models on GPUs. The speed of these models is therefore a bottleneck to research progress. Mythos 5.1 provided one solution to this problem: by writing custom GPU kernels and caching their intermediate results, it sped up seven open-source deep learning models by up to 2.5 times (with identical outputs).

The benefits of such speed-ups accumulate quickly. In any given experiment, biologists might run these models thousands of times (for example, testing every possible mutation near every human gene). On analyses like these, the optimized models cut estimated GPU costs by 30–60%. This kind of optimization would normally take a team of performance engineers weeks, and is often unaffordable for academic labs. Mythos 5.1 was able to do it in just days, using the publicly available source code alone. We plan to open-source these optimizations soon.

Inference speedup

Estimated cost savings on genome-wide analyses

Inference speedupEstimated cost savings on genome-wide analyses

As our models’ scientific capabilities improve, our investment in scientific progress is also growing. Last week, we previewed the [Model Hardware Standard](../19-Reference/model-hardware-standard-research-preview.md), which allows Claude to directly and safely operate laboratory equipment. We’ve also recently [expanded our support for scientists](../19-Reference/expanding-support-for-scientists.md) through our [AI for Science program](../19-Reference/ai-for-science-program.md), which provides free credits to researchers working on high-impact scientific projects, and we are offering steeply discounted usage through our new [Claude Team plan for scientists](programs-claude-team-plan-for-research-labs.md).

## Safety, security, and alignment

AI models’ agentic capabilities have become much more powerful over the past two years. But as we’ve [documented](../19-Reference/investigating-incidents-cybersecurity-evals.md), greater autonomy comes with new risks. Work on safety, security, and alignment needs to advance at the same pace as AI capabilities. Yesterday, we [published a report](../19-Reference/improving-alignment-security-efforts.md) describing how we are improving our own alignment and security efforts

Prior to releasing Claude Fable 5.1 and Claude Mythos 5.1, we (and, in some cases, external researchers) subjected the models to extensive testing for risks across many areas. We describe these efforts in full in our [System Card](claude-fable-5-1-mythos-5-1-system-card.md); below is a brief summary.

**Chemical and biological risks**. We tested the extent to which Claude Mythos 5.1 could help create chemical or biological weapons. This involved expert red-teaming, automated evaluations, and a tabletop exercise that paired PhD-level biologists with AI experts, testing whether the models could match human specialists’ performance. Mythos 5.1’s capabilities are greater than those of Mythos 5. However, our evaluations indicate that it still falls short of the next risk tier defined in our [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy). We are therefore deploying Mythos 5.1 with the [same safeguards](../19-Reference/improving-fable-5-s-biology-safeguards.md) that we applied to Mythos 5, which restrict access to research biology capabilities.

**Cyber risks**. We ran a suite of evaluations to assess the cyber capabilities of Claude Mythos 5.1 (with cybersecurity safeguards off). Overall, the model demonstrates the strongest cyber capabilities of any model we’ve released, though it still falls within the lower category of risk in our [Frontier Compliance Framework](../19-Reference/compliance-framework-sb53.md). We also performed extensive stress-testing of our cybersecurity safeguards for Fable 5.1: in addition to our own dynamic evaluation of their robustness, we commissioned external testing from two organizations, along with automated testing by [Gray Swan](https://www.grayswan.ai/). As with Fable 5 and Opus 5, we have not found evidence of a [critical-severity jailbreak](../19-Reference/fable-safeguards-jailbreak-framework.md) for these safeguards.

**Agentic safety**. We ran evaluations of how Claude Mythos 5.1 responds to malicious requests and prompt injections (adversarial instructions hidden within content processed by AI models). It refused malicious agentic coding and computer use requests at a comparable rate to Mythos 5, Sonnet 5, and Opus 5, and it is our most robust model to date on an external [prompt injection benchmark](claude-fable-5-1-mythos-5-1-system-card.md).

**Alignment*.*** We tested the model’s behavior through static and interactive behavioral evaluations, analyses of its internal thinking using [natural language autoencoders](../19-Reference/natural-language-autoencoders.md), misalignment-related capability evaluations, a review of our training data, and analyses of our internal pilot use. We also received reports from external testing.

Our automated behavioral audit found that Claude Mythos 5.1 is better aligned across most metrics than its predecessor, Mythos 5. The model is significantly less likely than Mythos 5 to try to access resources outside of its test environment when assigned an otherwise impossible task. It is also less likely than Mythos 5 to use motivated reasoning to justify its actions (for instance, by reasoning that the situation is a simulation or evaluation), and it is less likely to ignore explicit constraints in pursuit of users’ goals. From our review of its training data, Mythos 5.1 both attempts reward hacking (or cheating), and succeeds at it, at a lower overall rate than Mythos 5.

Though generally our alignment evaluations showed improvements, our testing found the model can still sometimes bypass approvals and auto-mode classifiers (as we discuss in more detail in our [System Card](claude-fable-5-1-mythos-5-1-system-card.md)). There are also limitations to the coverage provided by our alignment assessment. Currently, our automated behavioral audit provides less visibility into very long-context work and multi-agent settings. We also have less coverage of impossible tasks (which can elicit more abnormal and misaligned behavior) than we’d like, although we’ve recently made improvements in this domain and are working hard to continue doing so.

We have also improved our safeguards so that they allow our models to be more useful without compromising on safety. We describe these changes below.

**Automated safeguards for enterprises*.*** [Enterprise Frontier Safeguards](../19-Reference/enterprise-frontier-safeguards.md) (EFS) allows us to detect and respond to misuse of our models while still providing our enterprise customers the privacy of a zero data retention agreement. With EFS, customers store their data on their own cloud infrastructure, rather than on Anthropic’s systems; any human review is, by default, done by the customer themselves, rather than Anthropic. We developed EFS in close collaboration with more than 100 customers across industries like financial services, healthcare, manufacturing, telecom, law, retail, and the public sector, and with our cloud partners at Amazon Web Services, Google Cloud, and Microsoft Azure.

EFS will be supported on Claude Code, Claude Enterprise, the Claude Platform, Amazon Bedrock, Claude Platform on AWS, Google’s Agent Platform, and Microsoft Foundry. It’s rolling out in phases, starting this fall. As noted above, customers who are eligible for EFS can use Fable 5.1 (and Fable 5) with zero data retention until EFS is ready. You can read more about EFS [here](../19-Reference/enterprise-frontier-safeguards.md); to request access, please complete [this form](https://claude.com/form/enterprise-frontier-safeguards).

**More precise safeguards for biology and cybersecurity*.*** In the past few months, we’ve made progress in making our safeguards for Fable 5.1 more precise: ensuring that they’re less likely to flag benign content (like queries about medical issues or cyberdefenders using the model to make their systems safer), but still ensuring they provide robust protection against genuine threats.

As we [recently shared](../19-Reference/improving-fable-5-s-biology-safeguards.md), our latest biology safeguards for Fable 5.1 and Fable 5 fire 85% less often for benign requests related to elementary biology and medical questions (relative to those that launched with Fable 5). However, queries related to research and development in the life sciences will still be directed to our Opus models. We’re making the model’s life sciences capabilities available to professionals through an access program for Claude Mythos 5.1 that we’ve developed in partnership with the US government, which we discuss below.

With Fable 5.1, we’re updating our cybersecurity safeguards to be more precise. We’re also now allowing Fable 5.1 to be used for identifying software vulnerabilities—that is, to conduct the kind of defensive work that improves software security. As a result of these changes, Claude Code users can expect an average of around 60% fewer interventions per session from our cyber safeguards, relative to the previous safeguards on Fable 5. Our safeguards do, however, still redirect several kinds of dual-use cybersecurity tasks (tasks that might have helpful *or* harmful applications) to our Opus models. This includes penetration testing, exploit generation, and binary-based vulnerability scanning.

**Anti-distillation mechanisms*.*** Distillation is a method used to extract the capabilities of advanced models. It is often employed on an industrial scale, using thousands of fake accounts. Distillation is a safety risk, since the distilled capabilities can subsequently be released without adequate safeguards. Fable 5.1 comes with strengthened mechanisms to make distillation attacks harder. For example, it is no longer possible for new API accounts (those created from today onwards) to manually edit Claude’s prior context in a multi-turn conversation while preserving the transcript of Claude’s prior thinking. This closes off a common, publicly documented distillation technique, which allowed distillers to illicitly extract Claude’s thinking. We’re rolling out the change gradually, to minimize disruption: existing accounts are not currently affected by this change, though it will apply to all users with future model releases. A small number of customers’ custom integrations will then be affected. Our [Help Center article](../22-Safety-Policy/preserved-thinking-changing-how-the-messages-api-handles-thinking-blocks-to-protect.md) explains more about this change and the adjustments that developers can make.

## Trusted access for Claude Mythos 5.1

Claude Mythos 5.1 is identical to Fable 5.1, but it offers more permissive safeguards for vetted individuals and organizations whose work is affected by the cybersecurity and life sciences restrictions outlined above. It will be available through two trusted access programs:

- **Cyber Verification Program:** The CVP currently provides access to certain Opus- and Sonnet-class models with reduced cyber safeguards for defensive security work. In the near future, this program will also include access to Claude Mythos-class models. [Apply to join the CVP here](https://portal.anthropic.com/programs/cvp).
- **Life Sciences Verification Program:** The LSVP is designed so that life sciences professionals can use Claude Mythos 5.1 with safeguards designed for professional research and development activities (while all other safeguards remain in place). In partnership with the US government, we have enrolled our first participants, and we plan to expand access to this program to the broader life sciences community.

In addition to these trusted access programs, [Claude Security](product-claude-security.md), our product that scans codebases for vulnerabilities and suggests patches for human review, is now also powered by Claude Mythos 5.1.

## Compliance with the EU AI Act

In July 2026, Anthropic (along with [190 other signatories](https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content), including several other major AI model providers) signed the EU AI Act’s Code of Practice on Transparency of AI-Generated Content.

This required us to add a watermark—a numerical way of determining the likelihood that Claude was involved in writing a piece of text—to the outputs of models released after August 2, 2026. As we [recently explained](../19-Reference/claude-text-watermark.md), this watermark is invisible to anyone who does not have the detection API. It has no practical impact on the quality or content of Claude’s outputs and contains no information about the user, their organization, or their conversations with Claude.

The Act also required us to provide a way for users to tell whether a text likely contains the watermark. We are thus rolling out a detection API in private preview. It is currently available to eligible organizations (such as regulators, law enforcement, media, fact-checkers, independent researchers, educational organizations, and EU civil society groups) as required under EU law. It is also available for enterprises that are similarly obligated to verify watermarking for their own compliance with the Act. We plan to expand access to the detection API over time. You can register interest in access [here](https://forms.gle/9tGA33hPJJwtHsMk9).

## Cost and availability

Claude Fable 5.1 is available today on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. Developers can get started with `claude-fable-5-1` on the Claude API.

As mentioned above, we have reduced the price of Fable 5.1’s cache reads (where the model reuses context it has already processed) wherever usage is billed by token, such as on our API. Cache reads now cost 75% less, or \$0.25 per million tokens.

This change leads to a substantial reduction in the overall cost of running the model. For typical workloads, costs are reduced by around 25% relative to Fable 5. For complex coding and highly agentic tasks, the savings could be up to around 45%. The graph below illustrates why this change makes such a big difference:

Fable 5.1’s pricing is otherwise the same as Fable 5’s: \$10 per million input tokens and \$50 per million output tokens. In parallel, we’re continuing our work to bring many of the improvements of Fable 5.1 to the rest of our model family.

As discussed above, Claude Mythos 5.1 is available to vetted cyberdefenders and life scientists. Currently, it is only available to a set of US organizations, though we’re coordinating with the US government to expand access to a broader set of domestic and international partners as quickly as possible. To register interest in access to Claude Mythos 5.1 for cyberdefense through the CVP, [head here](https://portal.anthropic.com/programs/cvp).

## Get started

[Try Claude](https://claude.ai/)[Start building](../04-API-Reference/Other/usage-limits.md)

## Footnotes

¹ **Terminal-Bench-Science 0.1:** The standard error is ±3.5–4.5 pts per model. The public leaderboard (3 trials/task, Claude Code harness) reports Claude Opus 5 at 30.0% and Claude Fable 5 at 21.4%; our setup reproduces them at 29.0% and 24.7%, respectively, both within noise.

² **OSWorld 2.0:** Scores are on the benchmark authors’ August 2026 task release; Fable 5 and Opus 5 were re-run under the same conditions. Because the task files differ from earlier releases, these numbers aren't directly comparable to previously published OSWorld 2.0 results, which is why no competitor score is shown

³ These three targets are (EGFR, Nipah G, 15-PGDH) and come from [Adaptyv Bio’s protein design competitions](https://proteinbase.com/competitions). The Nipah G comparison is against *de novo* designs targeting the receptor-binding site on the G head (best: ~8–12 nM, [N1032](https://proteinbase.com/proteins/shy-otter-jade)). A *de novo* entry from [Nick Boyd/Escalante Bio](https://blog.escalante.bio/winning-the-de-novo-portion-of-the-adaptyv-nipah-binder-competition/) that targets a different region (the stalk) reached ~1.4 nM ([design_7](https://proteinbase.com/proteins/shy-eagle-fern)), comparable to our best binder.

## Further reading

**1.** The Claude Fable 5.1 and Claude Mythos 5.1 system card. [View card](claude-fable-5-1-mythos-5-1-system-card.md)

**2.** More detail on our Enterprise Frontier Safeguards. [Learn more](../19-Reference/enterprise-frontier-safeguards.md)

**3.** Request access to our Enterprise Frontier Safeguards. [Open form](../19-Reference/enterprise-frontier-safeguards.md)

**4.** An overview of our improvements to our biology safeguards. [Learn more](../19-Reference/improving-fable-5-s-biology-safeguards.md)

**5.** Support for scientists. [Read more](../19-Reference/expanding-support-for-scientists.md)

**6.** Earlier work by Claude in protein design. [Read more](../19-Reference/claude-accelerates-protein-design.md)

**7.** Earlier work by Claude in mathematics. [Read more](../19-Reference/riemann-zeta.md)

**8.** More about the Model Hardware Standard. [Learn more](../19-Reference/model-hardware-standard-research-preview.md)

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
