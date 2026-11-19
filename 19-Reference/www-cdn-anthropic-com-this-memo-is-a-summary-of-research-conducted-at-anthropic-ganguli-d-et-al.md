---
title: "This memo is a summary of research conducted at Anthropic. Ganguli, D., et al.…"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/b43359be43cabdbe3a8ffd60ea8a68acf25cb22e.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:58Z"
tags: ["news-research", "search"]
---

This memo is a summary of research conducted at Anthropic. Ganguli, D., et al. (2023).
https://www.anthropic.com/index/collective-constitutional-ai-aligning-a-language-model-with-public-input


    POLICY HIGHLIGHTS                                        Artificial intelligence (AI) models are imbued with values—what
                                                             those values are, and who gets to set them, can have a significant
    • Collective Constitutional AI is a
                                                             effect on how those models operate when deployed. Today, those
      flexible method for incorporating
      democratic processes into AI                           values are primarily set by a small number of AI developers with
      development. It can be scaled up                       little opportunity for the public to weigh in. To explore how we
      to broader groups of people, or                        might incorporate democratic processes into AI development,
      tailored to specific communities.                      Anthropic and the Collective Intelligence Project conducted a two-

    • Soliciting broad public                               part experiment that included: 1) running a public input process to
      input—through Collective                               gather people’s opinions on the values they want AI models to abide
      Constitutional AI or other                             by, and 2) training a new model to align with those values.
      methods—can reveal potential
      blindspots in the design of AI                         This method, which we call “Collective Constitutional AI,” differs
      models that when incorporated,                         from traditional AI development practices where developers play
      can make meaningful and
                                                             an outsized role in determining the values that AI models abide by.
      positive differences in
                                                             In contrast, Collective Constitutional AI incorporates public input
      downstream model behavior.
                                                             directly into AI models, and in doing so, increases representation,
    • Collective Constitutional AI can                      accountability, and transparency into how those models operate.
      be used to make AI models that
                                                             Collective Constitutional AI builds on the Anthropic-developed
      are more tailored to the needs of
                                                             “Constitutional AI” training method, which is a method for aligning
      specific communities.
                                                             general purpose AI models to abide by high-level normative
    • Collective Constitutional AI                          principles written into an AI “constitution”.1
      increases transparency in the
      design of complex AI models.
      The values used to steer model
                                                             Curating a publicly-designed AI constitution
      behavior can be disclosed in plain                     To gather principles for a publicly-designed AI constitution, we ran a
      language.                                              public input process among a roughly representative sample of 1,000
                                                             U.S. adults. We used an open-source platform for running online

1 https://www.anthropic.com/index/constitutional-ai-harmlessness-from-ai-feedback


                                                                                                                    DECEMBER 2023
deliberative processes called Polis, which has been       To test for model capabilities, we used two common
used around the world by governments, academics,          benchmarks for math and language understanding
and citizens to understand what large groups of           and found that the public model performed
people think. The process allowed participants            equivalently to the Anthropic model. Further to our
to add original submissions for new values and            work on building helpful and harmless AI systems,
normative principles, as well as vote on those            we found that people interacting with both models
suggested by other participants. These submissions        found them to be equally helpful and harmless.
were then consolidated into a publicly-designed AI        Finally, the model trained on the publicly-designed
constitution formatted for training an AI model with      AI constitution was less biased than the Anthropic
Constitutional AI.                                        model across nine social dimensions. In summary,
                                                          we found that the model trained on the publicly-
The resulting constitution shared approximately
                                                          designed AI constitution was just as capable and
50% overlap in values with the Anthropic-written
                                                          showed less negative stereotype bias than a model
AI constitution used to train our in-production
                                                          trained on the Anthropic-curated constitution.
model Claude. Differences between the two include
a greater emphasis on objectivity and impartiality
                                                          A flexible method for
in the publicly-designed AI constitution, as well as a
                                                          incorporating democratic
larger focus on accessibility. Additionally, principles
from the publicly-designed AI constitution tend to
                                                          processes into AI development
promote positive behaviors desired by the public, as      This effort was an experiment in developing a more
opposed to avoiding undesirable behaviors.                democratic process and methodology for training AI
                                                          models. It leaves room for future iteration in several
Training and evaluating an AI                             areas: the individuals and communities selected to
model aligned with public input                           participate in public input processes, the curation
                                                          and composition of resulting constitutions, and
Our goal was not just to understand public
                                                          the evaluations used to assess downstream model
perspectives on AI principles, but also to train
                                                          behavior, among others.
a model to follow those principles in order to
understand how public preferences affect the
downstream behavior of an AI model. Therefore,
we trained a new model using Constitutional
AI, aligning the model to the publicly-sourced
AI constitution instead of Anthropic's own
constitution. We believe this work may be one of             ABOUT US

the first instances in which members of the public           Anthropic is a public benefit corporation

have collectively directed the behavior of an AI             and AI safety research company that is

model via an online deliberative process. Finally, we        working to build reliable, interpretable,

ran experiments to understand how it was similar             and steerable AI systems. For more

to and different from a model trained with an AI             information, visit anthropic.com

constitution curated by Anthropic.


                                                                                                  DECEMBER 2023
