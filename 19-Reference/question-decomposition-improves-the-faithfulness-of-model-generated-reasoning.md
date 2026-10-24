---
title: "Question decomposition improves reasoning faithfulness \\ Anthropic"
source_url: "https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:44Z"
tags: ["news-research"]
---

# Question decomposition improves the faithfulness of model-generated reasoning

[Download Paper](https://www-cdn.anthropic.com/8154fb1d828cdc390dc1fa442d84034948679c47/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning.pdf)

- Published

  Jul 18, 2023

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Reasoning](https://www.anthropic.com/search?topic=reasoning)
  - [Alignment](https://www.anthropic.com/search?topic=alignment)
  - [Transparency](https://www.anthropic.com/search?topic=transparency)
  - [Measurement and mitigation](https://www.anthropic.com/search?topic=measurement-and-mitigation)

  See more...

Related articles

- Alignment

  Sep 17, 2026

  [Illuminating the frontier](https://www.anthropic.com/institute/measuring-pace-of-ai-development)

[View more](https://www.anthropic.com/search?topic=reasoning)

### Abstract

As large language models (LLMs) perform more difficult tasks, it becomes harder to verify the correctness and safety of their behavior. One approach to help with this issue is to prompt LLMs to externalize their reasoning, e.g., by having them generate step-by-step reasoning as they answer a question (Chain-of-Thought; CoT). The reasoning may enable us to check the process that models use to perform tasks. However, this approach relies on the stated reasoning faithfully reflecting the model’s actual reasoning, which is not always the case. To improve over the faithfulness of CoT reasoning, we have models generate reasoning by decomposing questions into subquestions. Decomposition-based methods achieve strong performance on question-answering tasks, sometimes approaching that of CoT while improving the faithfulness of the model’s stated reasoning on several recently-proposed metrics. By forcing the model to answer simpler subquestions in separate contexts, we greatly increase the faithfulness of model-generated reasoning over CoT, while still achieving some of the performance gains of CoT. Our results show it is possible to improve the faithfulness of model-generated reasoning; continued improvements may lead to reasoning that enables us to verify the correctness and safety of LLM behavior.
