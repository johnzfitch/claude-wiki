---
title: "Towards monosemanticity \\ Anthropic"
source_url: "https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:53Z"
tags: ["news-research"]
---

# **Towards monosemanticity: **Decomposing language models with dictionary learning

[Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

- Published

  Oct 5, 2023

- Team

  [Interpretability](team-interpretability.md)

- Topics

  - [Interpretability](https://www.anthropic.com/search?topic=interpretability)
  - [Alignment](https://www.anthropic.com/search?topic=alignment)

Related articles

- Interpretability

  Oct 5, 2023

  [Decomposing language models into understandable components](decomposing-language-models-into-understandable-components.md)

[View more](https://www.anthropic.com/search?topic=interpretability)

### Abstract

In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.
