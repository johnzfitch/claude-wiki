---
title: "Language models (mostly) know what they know \\ Anthropic"
source_url: "https://www.anthropic.com/research/language-models-mostly-know-what-they-know"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:05Z"
tags: ["news-research"]
---

# Language models (mostly) know what they know

[Read Paper](https://arxiv.org/abs/2207.05221)

- Published

  Jul 11, 2022

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Hallucination](https://www.anthropic.com/search?topic=hallucination)
  - [Alignment](https://www.anthropic.com/search?topic=alignment)
  - [Scaling laws](https://www.anthropic.com/search?topic=scaling-laws)
  - [Measurement and mitigation](https://www.anthropic.com/search?topic=measurement-and-mitigation)

  See more...

Related articles

- Interpretability

  May 21, 2024

  [Mapping the mind of a large language model](mapping-mind-language-model.md)

[View more](https://www.anthropic.com/search?topic=hallucination)

### Abstract

We study whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly. We first show that larger models are well-calibrated on diverse multiple choice and true/false questions when they are provided in the right format. Thus we can approach self-evaluation on open-ended sampling tasks by asking models to first propose answers, and then to evaluate the probability "P(True)" that their answers are correct. We find encouraging performance, calibration, and scaling for P(True) on a diverse array of tasks. Performance at self-evaluation further improves when we allow models to consider many of their own samples before predicting the validity of one specific possibility. Next, we investigate whether models can be trained to predict "P(IK)", the probability that "I know" the answer to a question, without reference to any particular proposed answer. Models perform well at predicting P(IK) and partially generalize across tasks, though they struggle with calibration of P(IK) on new tasks. The predicted P(IK) probabilities also increase appropriately in the presence of relevant source materials in the context, and in the presence of hints towards the solution of mathematical word problems. We hope these observations lay the groundwork for training more honest models, and for investigating how honesty generalizes to cases where models are trained on objectives other than the imitation of human writing.
