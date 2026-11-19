---
title: "This memo is a summary of research conducted at Anthropic. Ganguli, D., et al.…"
source_url: "https://www-cdn.anthropic.com/4ff80d7f8a98bf096cd543ec61ddc50de3ad8b16/Anthropic_PredictabilityAndSurprise.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:38Z"
tags: ["news-research", "search"]
---

This memo is a summary of research conducted at Anthropic. Ganguli, D., et al. (2022). Predictability and Surprise in
Large Generative Models. Association for Computing Machinery. https://dl.acm.org/doi/abs/10.1145/3531146.3533229


In recent years, AI researchers have built far more            to train them, and the amount of data they’re
general and useful AI systems. The best current                trained on (in the correct proportions), models
examples are models that can process and generate text         demonstrate improved general performance in
(e.g. OpenAI’s GPT-3, Microsoft & NVIDIA’s Megatron-           a predictable manner (a trend referred to as a
Turing NLG, and DeepMind’s Chinchilla). Unlike                 “scaling law,” Fig 1.1 ).
previous AI systems designed to perform a single task,
                                                               On the other hand, individual capabilities and outputs
these models can be used in a variety of applications,
                                                               can’t be predicted ahead of time — developers can’t tell
without being explicitly trained for those purposes.
                                                               you precisely what new behaviors will emerge as they
These models share an unusual combination of                   scale up models. For example, the ability to complete
interrelated characteristics. In some respects they            a specific task can sometimes emerge abruptly as
are reliably predictable, while in other ways, they are        developers increase the size of a model (Fig 1.2).
quite unpredictable. Aggregate model performance               The unpredictable nature of these models makes it
follows a predictable trend in relation to the resources       difficult to fully account for the consequences of their
expended on training. By scaling up the size of                development and deployment, demonstrating the
models, the computing power (compute) used                     importance of empirical safety research.


                                                                                                                        Fig 1.1


                                                                                                                        Fig 1.2


                                                                                                         SEPTEMBER 2022
       Despite these risks, more organizations from                                     Organizations (or countries) may also be motivated
       around the world are developing these systems, as                                by the scientific potential these models create for
       a significant amount of the uncertainty inherent                                 novel AI research or the prestige associated with
       to AI development has been reduced (Fig 1.3).                                    being on the technological frontier.

                                                                                                                   Megatron Turing-NLG (530B)
                                                                                                                      Microsoft & NVIDIA
                                                                                                                                                                           Fig 1.3
           GPT-3 (175B)                                                   Pan-Gu (200B)                           FLAN (137B)              Ernie 3.0 Titan (260B)
             OpenAI                                                         Huawei                                  Google                        Baidu


                                                                                                                                                                       Country

                                                                                                                                                                          USA
                                                                                                                                                                         China
                                                                                                                                                                          South Korea
                                                                                                                                                                          Israel
                                                                                                                                                                          UK / USA
                                                                                HyperCLOVA (204B)                     Yuan 1.0 (246B)                   LaMDA (137B)
                                                                                     Naver        Jurassic-1 Jumbo (178B) Inspur           Gopher (280B) Google
                                                                                                         AI21 Labs                          DeepMind


       0                  0          0          0          1          1             1               1                 1                1                 2
     02                02          02         02         02         02            02              02                02               02               02
  y2                l2          p2         v2         n2         r2          y2                l2              p2                 v2               n2
Ma                Ju          Se         No         Ja         Ma          Ma                Ju              Se                 No               Ja


       Due to the expense involved in building these models                             organizations. Over the past decade, we’ve seen a
       and the technical talent required to engineer them,                              dramatic shift in AI R&D as more computationally-
       private sector organizations from a number of                                    intensive research is conducted by private sector
       countries are the ones building these models                                     actors, while academia increasingly lags in its ability
       – not academia, civil society, or public sector                                  to build or investigate models at the frontier (Fig 1.4).


                                                                                                                                                                           Fig 1.4


       Based on the distinguishing features of these                                    • Reduce compute asymmetries between the private
       models, and the economic motivations for                                          sector and academia
       their development and deployment, we predict                                     • Improve the technical tools publicly available for
       large generative models will increasingly be                                      model evaluation
       developed and deployed despite their potential                                   • Increase our understanding of abrupt jumps in
       for harm. We think there are some policy                                          capabilities
       interventions available that can increase the                                    • Improve shared knowledge of how to “red team” models
       chance of these models being developed and                                       • Explore and prototype novel governance structures
       deployed in positive ways:                                                        and government interventions


       CONTACT: POLICY@ANTHROPIC.COM                                                                                                                           SEPTEMBER 2022
