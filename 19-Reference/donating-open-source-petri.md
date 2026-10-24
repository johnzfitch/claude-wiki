---
title: "Donating our open-source alignment tool \\ Anthropic"
source_url: "https://www.anthropic.com/research/donating-open-source-petri"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:43Z"
tags: ["news-research"]
---

# Donating our open-source alignment tool

- Published

  May 7, 2026

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Open source](https://www.anthropic.com/search?topic=open-source)
  - [Alignment](https://www.anthropic.com/search?topic=alignment)
  - [Safety evaluations](https://www.anthropic.com/search?topic=safety-evaluations)
  - [Nonprofits](https://www.anthropic.com/search?topic=nonprofits)

  See more...

Related articles

- Interpretability

  Jul 6, 2026

  [A global workspace in language models](global-workspace.md)

[View more](https://www.anthropic.com/search?topic=open-source)

In October 2025, we launched [Petri](petri-open-source-auditing.md), an open-source toolbox of alignment tests that can be applied to any large language model. Petri, which was developed as part of our Anthropic Fellows program, can be used to rapidly and easily test AI models for concerning tendencies like deception, sycophancy, and cooperation with harmful requests. It’s part of our efforts to develop alignment tools that are open and useful for the whole AI development community.

Petri has been part of our alignment assessment for every Claude model since Claude Sonnet 4.5. It compares how the new model behaves across a range of alignment-relevant scenarios that are simulated by a separate “auditor” model. A further “judge” model then scores the resulting transcripts for misaligned behaviors.

We’ve been pleased to see Petri being used by external organizations: for example, the UK’s AI Security Institute (AISI) made it a [major part](https://arxiv.org/abs/2604.00788) of how they evaluate models for their propensity to sabotage AI research.

We’re now updating Petri to its third version. Here are some of the biggest changes:

- *Adaptability.* Petri 3.0 involves major architectural changes that allow users to adapt it to more uses, in particular by splitting the auditor model and the target model into separate components that can be tweaked separately;
- *Realism.* Despite the fact that alignment researchers try to make tests appear realistic, a model can often deduce from various artificialities in the setup that it’s actually part of a test. And if the model is aware it’s being evaluated, the researcher is no longer able to see how the model behaves *in general*. An add-on to Petri, which we’re calling “Dish,” makes the setup far more realistic, for example by running the tests using the model’s real system prompt and the real “scaffold” (the software that wraps around the model to help it meet its goals) that would be used in genuine model deployments;
- *Depth*. We’ve now integrated Petri with our other open-source alignment tool, [Bloom](bloom.md), which can perform much more in-depth assessments of specific chosen behaviors (in comparison to Petri’s wider-ranging approach).

We’re also giving Petri a new home. We have handed over its development to [Meridian Labs](https://meridianlabs.ai/), an AI evaluation nonprofit. This move—similar to when we [donated](donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation.md) the Model Context Protocol (MCP) to the Linux Foundation—will help ensure that Petri remains independent of any AI lab, so that its results will be seen as neutral and credible by those across the industry and beyond.

As part of Meridian Labs, Petri joins other tools like [Inspect](https://inspect.aisi.org.uk/) and [Scout](https://meridianlabs-ai.github.io/inspect_scout/), building a technology stack that is open to labs, independent researchers, and governments alike, at a time when reliable tests of AI model behavior matter more than ever.

You can read more about Petri 3.0 on [the Meridian Labs blog](https://meridianlabs.ai/blog/posts/introducing-petri-3/).

Instructions to install and use Petri can be found on the [Petri website](https://meridianlabs-ai.github.io/inspect_petri/).
