---
title: "Deceptive LLMs that persist through safety training \\ Anthropic"
source_url: "https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:52Z"
tags: ["news-research"]
---

# **Sleeper Agents: **Training deceptive LLMs that persist through safety training

[Read Paper](https://arxiv.org/abs/2401.05566)

- Published

  Jan 14, 2024

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Alignment](https://www.anthropic.com/search?topic=alignment)
  - [Training](https://www.anthropic.com/search?topic=training)
  - [Red teaming](https://www.anthropic.com/search?topic=red-teaming)
  - [Safety evaluations](https://www.anthropic.com/search?topic=safety-evaluations)
  - [Reasoning](https://www.anthropic.com/search?topic=reasoning)

  See more...

Related articles

- Alignment

  Apr 3, 2025

  [Reasoning models don't always say what they think](reasoning-models-dont-say-think.md)

[View more](https://www.anthropic.com/search?topic=alignment)

Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety.
