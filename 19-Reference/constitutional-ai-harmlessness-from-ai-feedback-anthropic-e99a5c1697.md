---
category: "19-Reference"
fetched_at: "2026-02-24T05:03:50Z"
source_url: "https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback"
title: "Constitutional AI: Harmlessness from AI Feedback \\ Anthropic"
---
# Constitutional AI: Harmlessness from AI Feedback

Dec 15, 2022

[Read Paper](https://arxiv.org/abs/2212.08073)

## Abstract

As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

## Policy Memo

[Constitutional AI Policy Memo](https://www-cdn.anthropic.com/7512771452629584566b6303311496c262da1006/Anthropic_ConstitutionalAI_v2.pdf)


## Related content

### The persona selection model

[Read more](/research/persona-selection-model)

### Anthropic Education Report: The AI Fluency Index

We tracked 11 observable behaviors across thousands of Claude.ai conversations to build the AI Fluency Index — a baseline for measuring how people collaborate with AI today.

[Read more](/research/AI-fluency-index)

### Measuring AI agent autonomy in practice

[Read more](/research/measuring-agent-autonomy)
