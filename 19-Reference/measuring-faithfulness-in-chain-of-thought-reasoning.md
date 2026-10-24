---
title: "Measuring faithfulness in Chain-of-Thought reasoning \\ Anthropic"
source_url: "https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:06Z"
tags: ["news-research"]
---

# Measuring faithfulness in Chain-of-Thought reasoning

[Download Paper](https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf)

- Published

  Jul 18, 2023

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Reasoning](https://www.anthropic.com/search?topic=reasoning)
  - [Interpretability](https://www.anthropic.com/search?topic=interpretability)
  - [Scaling laws](https://www.anthropic.com/search?topic=scaling-laws)
  - [Transparency](https://www.anthropic.com/search?topic=transparency)

  See more...

Related articles

- Interpretability

  Oct 1, 2024

  [Circuits Updates – September 2024](circuits-updates-sept-2024.md)

[View more](https://www.anthropic.com/search?topic=reasoning)

### Abstract

Large language models (LLMs) perform better when they produce step-by-step, “Chain-of-Thought” (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT’s performance boost does not seem to come from CoT’s added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.
