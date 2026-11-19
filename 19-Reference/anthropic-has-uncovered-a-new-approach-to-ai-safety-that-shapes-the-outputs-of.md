---
title: "Anthropic has uncovered a new approach to AI safety that shapes the outputs of…"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/7512771452629584566b6303311496c262da1006.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:58Z"
tags: ["news-research"]
---

Anthropic has uncovered a new approach to AI safety that shapes the outputs of AI systems according to a set
of principles. The approach is called Constitutional AI (CAI) because it gives an AI system a set of principles (i.e., a
“constitution”) against which it can evaluate its own outputs. CAI enables AI systems to generate useful responses while
also minimizing harm. This is important because existing techniques for training models to mirror human preferences
face trade-offs between harmlessness and helpfulness. Other benefits of CAI include its scalability and increased model
transparency. https://arxiv.org/abs/2212.08073


As artificial intelligence (AI) systems                the resulting preference datasets to fine-tune AI systems that
become more capable, it becomes more                   are more reflective of the desired behavior, be it helpfulness,
important that they are aligned with                   harmlessness, or some other characteristic.
principles that humans find agreeable.
                                                       However, there can be a real trade-off between helpfulness and
We want general-purpose language
                                                       harmlessness when using RLHF. Because human crowdworkers
models to be as useful as possible and
                                                       often reward evasive responses to unethical requests, models
we want them to be safe.
                                                       fine-tuned with RLHF can be more harmless than they are
There is a direct correlation between the              helpful. For example, an AI assistant that responds to all
size of these models and their potential               questions with “I can’t answer that” would be harmless, but it
to cause harm. Given that AI systems                   would also be completely useless. The figure below shows that
can already perform some tasks at or                   Constitutional RL models trained with AI feedback learn to be
beyond human level, we need approaches                 less harmful at a given level of helpfulness.
that can align them with human values.
This will only become more important
going forward; as models exceed
human capabilities and are applied in
increasingly complex environments, we
will need ways to steer them and ensure
they are operating as intended.

Without intervention, generative AI
models can output undesirable content.
The current industry standard for
aligning models with human preferences
is called reinforcement learning from
human feedback (RLHF). This approach
                                                       This graph shows harmlessness versus helpfulness Elo scores (higher is better)
uses human crowdworkers to choose                      computed from crowdworkers’ model comparisons. It displays a Pareto improvement
                                                       (i.e., win-win situation) where Constitutional RL is both more helpful and more
between two model outputs and uses                     harmless than standard RLHF.


                                                                                                                              APRIL 2023
CAI reduces the tension between helpfulness and                                    POLICY HIGHLIGHTS:
harmlessness by creating AI assistants that are
                                                                                   • Drafting a constitution for powerful AI systems
significantly less evasive. These models engage with
                                                                                     could be a democratic process wherein diverse
user requests, but are less likely to help users with
                                                                                     stakeholders provide input to tailor the behavior of
unsafe or unethical requests. In many cases, they
                                                                                     a system to organizational, community, or cultural
also explain the grounds on which they refuse such
                                                                                     preferences.
requests.
                                                                                   • CAI improves model performance and reduces costs
CAI does this by training a model using a list of
                                                                                     of AI alignment, which incentivizes developers to
natural language instructions or principles, which
                                                                                     adopt this method.
comprise the model’s “constitution.” For example, one
principle used in the research process was: “Which                                 • CAI makes model decision-making more
of these assistant responses is less harmful? Choose                                 transparent, which enables calibrated trust in
the response that a wise, ethical, polite and friendly                               AI systems.
person would more likely say.”1 In this way, CAI
improves upon and partly replaces RLHF. The model’s                                • CAI could increase resistance to red-teaming

self-critique and -revision approach can be framed as                                attacks by making helpfulness and harmlessness

reinforcement learning from AI feedback (RLAIF).                                     more compatible.


This is important for three main reasons:                                          • CAI lowers the barriers to experimentation, which
                                                                                     could make it easier to study how different AI
      1. CAI creates more harmless models with                                       behaviors tend to generalize and interfere.
      minimal impact on helpfulness. Models
      trained using CAI learn to be less harmful at a                              • CAI makes it possible to train systems to behave

      given level of helpfulness.                                                    in desirable ways with a smaller quantity of high
                                                                                     quality human supervision, though it is not a
      2. CAI increases model transparency. Encoding                                  substitute for robustly testing AI systems prior
      goals and objectives into AI systems in natural                                to deployment.
      language increases the legibility of these systems.
      This enables users and regulators to peek into                               • Given its dual-use nature, CAI could make it easier

      the “black box” of AI decision-making by making                                to train pernicious systems.

      explicit the model’s objectives and reasoning.

      3. CAI is a scalable safety measure. CAI is much                                  ABOUT US
      less time- and resource-intensive than eliciting                                  Anthropic is a public benefit corporation
      tens of thousands of human feedback labels. This                                  and AI safety research company that is
      means that it is both more efficient and it does                                  working to build reliable, interpretable,
      not require exposing human crowdworkers to                                        and steerable AI systems.
      potentially offensive model outputs.


1 Note that this was for research purposes, and is not the same set of principles that Anthropic uses for its large language model, Claude.


CONTACT: POLICY@ANTHROPIC.COM                                                                                                                 APRIL 2023
