---
title: "Anthropic has discovered that large language models can be guided to avoid…"
source_url: "https://www-cdn.anthropic.com/d14f58fe8f611858bc37ff8686bbda71e4927ce6/Anthropic_MoralSelfCorrection_v3.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:31Z"
tags: ["news-research"]
---

Anthropic has discovered that large language models can be guided to avoid stereotypical and discriminatory outputs
simply by asking for an impartial or non-discriminatory response in natural language. This does not depend on explicitly
defining concepts like “fairness” for a model or implementing algorithmic interventions; rather, it utilizes a model’s ability
to follow instructions and comprehend complex moral subjects. This offers tentative hope about the ability of language
models to adhere to ethical principles. https://arxiv.org/abs/2302.07459


As language models grow in size, their performance                              Fairness and bias are major concerns for the safe
on a wide array of tasks improves. However, research                            and ethical integration of AI into society. Given their
shows that harmful social biases can be exacerbated                             increasing capabilities, large language models may
in large language models (see figure below). Put                                at some point be deployed ubiquitously, including in
differently: without intervention, bias increases as                            high-risk and consequential settings. From a societal
the parameter count of the models increases (i.e., as                           perspective, it is critical to ensure that these systems
models get larger).                                                             avoid producing harmful, unethical, and biased
                                                                                outputs.

                                                                                We found that one effective method for steering large
                                                                                language models away from harmful outputs is to
                                                                                instruct them to do so in natural language. We refer to
                                                                                this as “moral self-correction.” Moral self-correction
                                                                                involves language models detecting stereotype bias
                                                                                and discrimination in the text they generate and
                                                                                adjusting their outputs accordingly.

                                                                                As language models increase in scale, their ability to
                                                                                self-correct improves. This is because larger models
                                                                                are better able to follow instructions and grasp
                                                                                complex concepts of harm like stereotyping, bias, and
                                                                                discrimination. In our research, we found that models
                                                                                that are sufficiently large (i.e., greater than 22 billion
The brown line illustrates that as models become larger (x-axis), they become
more biased (y-axis). The tan and grey lines illustrate that as models become
                                                                                parameters) and fine-tuned with human feedback1
larger, they are increasingly able to reduce bias when instructed to do so.
                                                                                seem particularly well-suited to this approach.


1 Reinforcement Learning from Human Feedback (RLHF) is a popular technique for reducing harmful behaviors in large language models and has become an
industry standard for developing AI systems that are aligned with human preferences.

                                                                                                                                          APRIL 2023
Our research found that we can guide models to avoid      Regarding stereotyping, the results from the BBQ
bias and discrimination by requesting an impartial or     benchmark showed that simply instructing models
non-discriminatory response in natural language. The      to avoid bias substantially reduces biased outputs.
models need not be explicitly taught what is meant by     The Winogender results indicated that models can
“fair” and “unfair” outputs for this to work. Instead,    be steered to reflect accurate occupational gender
the models learn these concepts during their training     statistics, use gender-neutral pronouns, or choose
process. This differs from classical machine learning     randomly between gender pronouns. Regarding
approaches that require precise mathematical              discrimination, our experiment showed that models
definitions and algorithmic interventions.                can achieve demographic parity when instructed to
                                                          avoid race-based decisions.
To measure stereotyping, we employ two well-known
benchmarks: The Bias Benchmark for Question               POLICY HIGHLIGHTS:
Answering (BBQ), which tests a model’s tendency
                                                          • The ability of language models to respond to
to rely on stereotypes related to age, disability,
                                                           natural language instructions could introduce new
nationality, socioeconomic status, and more; and
                                                           methods for correcting their behavior not available
Winogender, which evaluates whether a model
                                                           in other modalities. For example, traditional
assigns gendered pronouns to certain occupations.
                                                           machine learning approaches like classification and
To measure discrimination, we developed a new              regression, which are commonly used in high-stakes
benchmark to test the influence of race in a law school    decisions, lack the capacity for moral self-correction.
admission decision. In this scenario, a law professor
                                                          • Context matters when defining “fairness.” In certain
consults a language model to help determine whether
                                                           situations, it could be fairer for the model to reflect
or not they should accept an applicant into their class
                                                           the world as it is (i.e., reflect accurate occupational
based on a short description including demographic
                                                           gender statistics). In other situations, it could be
details. This measures whether changing a protected
                                                           fairer for the model to be neutral (i.e., use gender-
characteristic (e.g., race, from “Black” to “white”)
                                                           neutral pronouns or choose randomly between
while holding all other features constant affects the
                                                           gender pronouns for a given profession).
model’s recommendation.

                                                          • While we don’t expect these findings to be sufficient
We conducted three experiments to test our
                                                           in and of themselves to solve “the alignment
hypothesis:
                                                           problem,” the capacity for large language models to
    1. A question-only control condition.                  respond to natural language instruction opens up
                                                           new avenues for specifying and mitigating harmful
    2. A question + instruction following prompt,
                                                           behavior like stereotyping and discrimination.
    such as “Please ensure that your answer is
    unbiased and does not rely on stereotypes.”           • These findings have dual-use potential. Although
                                                           our research focused on moral self-correction in
    3. A question + instruction following + chain of
                                                           language models, these same techniques could
    thought prompt, where models describe how they
                                                           be inverted to make the model’s outputs more
    might follow the instructions before answering
                                                           stereotypical or biased.
    the question.


CONTACT: POLICY@ANTHROPIC.COM                                                                            APRIL 2023
