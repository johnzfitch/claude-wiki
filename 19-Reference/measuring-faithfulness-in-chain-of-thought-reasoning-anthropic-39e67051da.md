---
category: "19-Reference"
fetched_at: "2026-02-24T05:03:52Z"
source_url: "https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning"
title: "Measuring Faithfulness in Chain-of-Thought Reasoning \\ Anthropic"
---
# Measuring Faithfulness in Chain-of-Thought Reasoning

Jul 18, 2023

[Download Paper](https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf)

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, “Chain-ofThought” (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT’s performance boost does not seem to come from CoT’s added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.

\


## Related content

### The persona selection model

[Read more](/research/persona-selection-model)

### Anthropic Education Report: The AI Fluency Index

We tracked 11 observable behaviors across thousands of Claude.ai conversations to build the AI Fluency Index — a baseline for measuring how people collaborate with AI today.

[Read more](/research/AI-fluency-index)

### Measuring AI agent autonomy in practice

[Read more](/research/measuring-agent-autonomy)
