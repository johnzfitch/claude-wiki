---
title: "Softmax linear units \\ Anthropic"
source_url: "https://www.anthropic.com/research/softmax-linear-units"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:30Z"
tags: ["linear", "news-research"]
---

# Softmax Linear Units

[Read Paper](https://transformer-circuits.pub/2022/solu/index.html)

- Published

  Jun 17, 2022

- Team

  [Interpretability](team-interpretability.md)

- Topics

  - [Interpretability](https://www.anthropic.com/search?topic=interpretability)
  - [Training](https://www.anthropic.com/search?topic=training)
  - [Alignment](https://www.anthropic.com/search?topic=alignment)

  See more...

Related articles

- Interpretability

  Oct 5, 2023

  [Towards monosemanticity: Decomposing language models with dictionary learning](towards-monosemanticity-decomposing-language-models-with-dictionary-learning.md)

[View more](https://www.anthropic.com/search?topic=interpretability)

### Abstract

In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers. However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable. Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.
