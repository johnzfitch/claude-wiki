---
category: "19-Reference"
fetched_at: "2026-02-24T05:03:54Z"
source_url: "https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning"
title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning \\ Anthropic"
---
# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

Oct 5, 2023

[Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## Abstract

In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.

\


## Related content

### The persona selection model

[Read more](/research/persona-selection-model)

### Anthropic Education Report: The AI Fluency Index

We tracked 11 observable behaviors across thousands of Claude.ai conversations to build the AI Fluency Index — a baseline for measuring how people collaborate with AI today.

[Read more](/research/AI-fluency-index)

### Measuring AI agent autonomy in practice

[Read more](/research/measuring-agent-autonomy)
