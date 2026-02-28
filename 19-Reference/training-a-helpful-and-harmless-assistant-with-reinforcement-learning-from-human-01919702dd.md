---
category: "19-Reference"
fetched_at: "2026-02-24T05:03:54Z"
source_url: "https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback"
title: "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback \\ Anthropic"
---
# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

Apr 12, 2022

[Read Paper](https://arxiv.org/abs/2204.05862)

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.

## Authors

Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan\


## Related content

### The persona selection model

[Read more](/research/persona-selection-model)

### Anthropic Education Report: The AI Fluency Index

We tracked 11 observable behaviors across thousands of Claude.ai conversations to build the AI Fluency Index — a baseline for measuring how people collaborate with AI today.

[Read more](/research/AI-fluency-index)

### Measuring AI agent autonomy in practice

[Read more](/research/measuring-agent-autonomy)
