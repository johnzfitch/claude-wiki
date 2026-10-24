---
title: "Evaluating discrimination in language model decisions \\ Anthropic"
source_url: "https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:45Z"
tags: ["news-research"]
---

# Evaluating and mitigating discrimination in language model decisions

[Read Paper](http://arxiv.org/abs/2312.03689)

- Published

  Dec 7, 2023

- Team

  [Societal Impacts](team-societal-impacts.md)

- Topics

  - [Bias and fairness](https://www.anthropic.com/search?topic=bias-and-fairness)
  - [Measurement and mitigation](https://www.anthropic.com/search?topic=measurement-and-mitigation)
  - [Safety evaluations](https://www.anthropic.com/search?topic=safety-evaluations)
  - [Benchmarks](https://www.anthropic.com/search?topic=benchmarks)

  See more...

Related articles

- Societal Impacts

  Nov 13, 2025

  [Measuring political bias in Claude](political-even-handedness.md)

[View more](https://www.anthropic.com/search?topic=bias-and-fairness)

### Abstract

As language models (LMs) advance, interest is growing in applying them to high-stakes societal decisions, such as determining financing or housing eligibility. However, their potential for discrimination in such contexts raises ethical concerns, motivating the need for better methods to evaluate these risks. We present a method for proactively evaluating the potential discriminatory impact of LMs in a wide range of use cases, including hypothetical use cases where they have not yet been deployed. Specifically, we use an LM to generate a wide array of potential prompts that decision-makers may input into an LM, spanning 70 diverse decision scenarios across society, and systematically vary the demographic information in each prompt. Applying this methodology reveals patterns of both positive and negative discrimination in the Claude 2.0 model in select settings when no interventions are applied. While we do not endorse or permit the use of language models to make automated decisions for the high-risk use cases we study, we demonstrate techniques to significantly decrease both positive and negative discrimination through careful prompt engineering, providing pathways toward safer deployment in use cases where they may be appropriate. Our work enables developers and policymakers to anticipate, measure, and address discrimination as language model capabilities and applications continue to expand. We release our dataset and prompts [here](https://huggingface.co/datasets/Anthropic/discrim-eval).
