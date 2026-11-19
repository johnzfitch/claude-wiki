---
title: "This memo is a summary of research conducted at Anthropic. Denison, C., et al.…"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/bed8f247538cdfdd0caf8368f557adb73df0cb16.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:35Z"
tags: ["news-research", "search"]
---

This memo is a summary of research conducted at Anthropic. Denison, C., et al. (2024).

https://anthropic.com/research/reward-tampering


                                       As language models (LMs) become more capable and integrated into a

   Policy highlights                   broader range of economically useful tasks, it becomes increasingly critical

                                       that they operate in line with the goals and intentions defined by their
      Serious AI misbehavior can
                                       developers. One tool developers use to steer the behavior of LMs is through
      emerge from relatively
                                       a training process called reinforcement learning, where the model is
      benign dishonest behavior
                                       “rewarded” when it demonstrates the behaviors its developers want to
      Researchers found that
                                       incentivize, and “penalized” for demonstrating less desirable behaviors. 

      models trained on easily-

      discovered forms of
                                       Specifying the exact behavior we want to see from general-purpose
      dishonesty (e.g. insincere
                                       systems is challenging, and there are numerous instances of AI systems
      flattery) would generalize
                                       acting in ways that go against the intentions of their developers while still
      without additional training to
                                       achieving a high “reward”. In essence, the model has “gamed the system,”
      edit their own code to
                                       a behavior researchers refer to as “specification gaming”. This behavior
      maximize reward (“reward-
                                       could range from the relatively benign (acting overly sycophantic towards
      tampering”)

                                       a user) to more egregious (a model directly tampering with its own
      Safety interventions were
                                       training process and reward function, i.e., “reward tampering”).


      not fully effective in

      eliminating the misbehavior,

      as models with and without
                                              Training
      safety interventions still

      learned to tamper with their

      reward functions at similar
                                             v luation
                                            E a
      rates


      Current frontier language                                  e
                                                                  d
          l
    t             re
         g              ir
                                                              in             u                  e           in             e
                                                            a              f       n           c      y    y            t h     e
                                                           r             lp       a         in      r     L                   d
                                                          t                      t                e                   k
      models almost certainly do                       re     e
                                                                l       e    is         In
                                                                                          s
                                                                                               t t
                                                                                                                   a
                                                                                                                    c     c
                                                                                                                            o
                                                      P      d         H    s
                                                           o                                 la                   H     n
                                                         m                s                f                         w
      not pose a risk of reward-                                         a                                          o


      tampering. However, the risk
                                          We designed a curriculum of increasingly complex environments with the potential
                                          for specification gaming. Early on, AIs discover dishonest strategies like insincere
      of serious misalignment

      emerging from benign                flattery. They then generalize, without further training, to serious misbehavior:

                                          directly modifying their own code to maximize reward.
      misbehavior will increase as

      models grow more capable

      and training pipelines grow      Researchers at Anthropic have discovered that LMs trained to display

      more complex.                    relatively benign dishonest behavior can make the leap to more egregious

                                       dishonest behavior, without further training. Put another way: the ability

                                       of LMs to “game the system” generalizes from simple tasks and

                                       environments to ones that are more complex. This research provides

                                       empirical evidence that potentially dangerous behavior could emerge

                                       naturally from seemingly-benign behavior when there is misalignment

                                       between developer intentions and model incentives.


                                                                                                                     JunE 2024
Experiment design: Building a model                              When the researchers trained the model not to engage in
                                                                 easily-detectable misbehavior, it reduced the rate of more
training “curriculum”

                                                                 serious misbehavior by 3-10x but did not fully eliminate it.
Anthropic researchers built a custom “curriculum” of             This suggests that fixing obvious misbehavior may not be
training environments where the training reward can be           sufficient to completely remove misbehavior that is more
tampered with (or “gamed”) by the model. The                     challenging to detect. Techniques likely exist which are
environments mirror real-world instances where a model           significantly more effective at removing serious
might behave in a way that is not aligned with developer         misbehavior, but discovering those methods will require
specifications. The training environments get successively       further research.

more difficult, and as a result, require the model to engage
in more egregious forms of specification gaming. 
               As LM capabilities continue to advance and move from
                                                                 self-contained text-based tasks to more complex tasks
For example, early in the curriculum, the model could            such as using computers or accelerating AI research and
demonstrate sycophancy in responding to political                development, we must develop techniques to align these
questions in a way a user wants to hear, even if those           systems with human intentions. While this research was
answers aren’t fully accurate or appropriate. In later           conducted in purpose-built testing environments, it
environments, the model could lie about an action it has         demonstrates that misalignment can emerge and
taken, and then edit its own internal logs to cover up that      generalize in concerning ways.
lie from a human observer.


Results: Model behavior generalizes                                  About us
across environments
                                                 Anthropic is a public benefit corporation and
Researchers found that as the model progressed through               AI safety research company that is working to
                                                                     build reliable, interpretable, and steerable  
the training curriculum, its behavior generalized from
                                                                     AI systems.
easier specification gaming tasks to subsequently more
challenging ones, to the point of directly tampering with its
own training reward, despite never being trained to do so. 


While this research was conducted in artificially-designed
training environments, the generalization to dangerous
behavior is worrisome as it could be very challenging to
detect if found in real-world settings. With reward
tampering in particular, we might not be able to tell that
the model has done something bad even if we were looking
for that behavior, as the model could also interfere with
oversight mechanisms we put in place (e.g., activity logs or
tests to ensure code has not been modified).


Safety training is not fully effective
in eliminating model misbehavior

The researchers tested whether safety interventions (such
as training the model to be helpful, honest, and harmless)
made models less likely to tamper with their own training
process; unfortunately, it did not. In this experiment setup,
models trained to be harmless would overwrite their
reward (i.e., the goal set by the developer) at a similar rate
as those without harmlessness training.


                                                                                                                    JUNE 2024
