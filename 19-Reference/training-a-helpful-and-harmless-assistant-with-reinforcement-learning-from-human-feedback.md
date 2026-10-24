---
title: "Training a helpful and harmless assistant with RLHF \\ Anthropic"
source_url: "https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:53Z"
tags: ["news-research"]
---

# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

[Read Paper](https://arxiv.org/abs/2204.05862)

- Published

  Apr 12, 2022

- Team

  [Alignment](team-alignment.md)

- Topics

  - [Alignment](https://www.anthropic.com/search?topic=alignment)
  - [Training](https://www.anthropic.com/search?topic=training)
  - [Scaling laws](https://www.anthropic.com/search?topic=scaling-laws)
  - [Benchmarks](https://www.anthropic.com/search?topic=benchmarks)

  See more...

Related articles

- Alignment

  Oct 24, 2023

  [Specific versus general principles for Constitutional AI](specific-versus-general-principles-for-constitutional-ai.md)

[View more](https://www.anthropic.com/search?topic=alignment)

### Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.

## Authors & Acknowledgments

### Contributors

Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan
