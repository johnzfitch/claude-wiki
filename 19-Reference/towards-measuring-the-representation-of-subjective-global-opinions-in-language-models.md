---
title: "Measuring subjective global opinions in LLMs \\ Anthropic"
source_url: "https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:31Z"
tags: ["news-research"]
---

# Towards measuring the representation of subjective global opinions in language models

[Read Paper](https://arxiv.org/abs/2306.16388)

- Published

  Jun 29, 2023

- Team

  [Societal Impacts](team-societal-impacts.md)

- Topics

  - [Bias and fairness](https://www.anthropic.com/search?topic=bias-and-fairness)
  - [Measurement and mitigation](https://www.anthropic.com/search?topic=measurement-and-mitigation)
  - [Benchmarks](https://www.anthropic.com/search?topic=benchmarks)
  - [Constitutional AI](https://www.anthropic.com/search?topic=constitutional-ai)

  See more...

Related articles

- Engineering

  Feb 5, 2026

  [Quantifying infrastructure noise in agentic coding evals](infrastructure-noise.md)

[View more](https://www.anthropic.com/search?topic=bias-and-fairness)

### Abstract

Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country's perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model's responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on. Our data is at [this URL](https://huggingface.co/datasets/Anthropic/llm_global_opinions). We also provide an interactive visualization at [this URL](https://llmglobalvalues.anthropic.com/).
