---
title: "POLICY HIGHLIGHTS"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/f0dfb70b9b309d7c52845f73da8d964140669ff7.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:59Z"
tags: ["news-research"]
---

POLICY HIGHLIGHTS                         As the capabilities of generative artificial intelligence (AI) models
                                          advance, there is growing interest to use them to streamline
• Anthropic has developed a new
                                          processes in areas such as business, healthcare, and government
 evaluation method to measure
                                          services. Language models (LMs) in particular may be applied to
 discriminatory outputs from language
 models when they are used in a           decision making processes that have historically relied on human
 variety of decisions across society      judgment or hard-coded rules. However, potential biases present in
 (e.g., loan approvals or employability   LMs can exacerbate unfair and discriminatory outcomes when used
 determinations).                         in high-stakes decisions. Policymakers are proactively preparing for
                                          this risk by seeking to govern the use of LMs in these settings.
• We find that the use of simple
 model prompting techniques (i.e.,        While we do not endorse or permit the use of our language models
 providing additional instruction to a
                                          for high-risk automated decisions, it is important that policymakers
 language model in plain language) can
                                          have the tools to quantitatively understand potential biases,
 significantly reduce discriminatory
                                          and that developers have tools to mitigate them. To enable this,
 outputs for these high-stakes
 decisions.                               Anthropic developed and released a method to measure potential
                                          discrimination in these scenarios. In addition to releasing this
• While we do not endorse or permit      evaluation method, we demonstrate that simple prompting
 the use of language models for
                                          techniques can be used to nearly eliminate discriminatory outputs
 high-risk automated decisions, the
                                          for these decisions, which may lead to safer deployment paths.
 policy community has recognized the
 growing likelihood of their adoption.
 As such, there is a critical need        Evaluating discrimination
 for effective tools to measure and       in high-stakes decisions
 mitigate potential discrimination
                                          To evaluate discrimination, we use an LM to generate a wide range
 from language models used in these
                                          of decision scenarios and systematically vary key demographic
 applications.
                                          information in each prompt. We used a three-step process to
• In addition to our research, we        build the evaluation. First, we generated a diverse set of decision
 released the code for our evaluation     scenarios where LMs might be used across society (e.g., whether
 method, making it easier for others      to extend a job offer, pay out an insurance claim, or grant a work
 to test language models and prevent
                                          visa). Next, we generated question templates with placeholders for
 discrimination in these settings.
                                          a hypothetical individual’s demographic information (e.g., “Should


                                                                                                DECEMBER 2023
the [AGE], [RACE], [GENDER] be granted a work
                                                                                  0.6
visa?”). Lastly, we created several versions of the same
paragraph-long scenario template but modified select                              0.5


                                                           Discrimination Score
demographic variables across age, race, and gender.
                                                                                  0.4
This evaluation allows us to quantify discrimination
by measuring the difference in decision results for                               0.3

various demographics when all other information
remains constant. To ensure the LM-generated                                      0.2

decision scenarios were of sufficiently high quality,
                                                                                  0.1
we ran a separate study where humans reviewed and
validated appropriate templates. The high level of                                0.0
agreement among participants provides evidence that                                       No Intervention         Intervention
this template generation method can reliably produce
large sets of high-quality, realistic, and diverse
decision scenarios.
                                                                 Building and sharing tools
Mitigation strategies to reduce                                  to measure and mitigate
discriminatory outputs                                           discrimination in language models
In addition to tools to measure discrimination,                  Language models are open-ended systems and

developers also need tools to mitigate it. In our study,         difficult to robustly evaluate for potential societal

we found that simple prompting—i.e., providing                   risks. However, as their utility grows in a wide range

additional instruction to an LM in plain language—is             of use cases, we anticipate that they will increasingly

an effective tool to reduce discriminatory outputs.              be applied in high-stakes settings, making it crucial

We tested a variety of prompt strategies that include:           that developers and policymakers have the tools to
                                                                 assess them for possible harms. Towards this end,
   • Appending statements to decision questions                 we developed an evaluation technique to measure
    instructing a model to ensure its answer is                  discrimination, and released it publicly so that others
    unbiased                                                     may use it to assess discriminatory outputs in other
                                                                 language models and use cases. Finally, we also show
   • Inserting requests to articulate the rationale
                                                                 that simple model prompting techniques can provide
    behind a decision while avoiding bias and
                                                                 a “dial” to control for and mitigate discriminatory
    stereotypes
                                                                 outputs.
   • Asking the model to answer the decision question
    as if no demographic information was provided
                                                                                   ABOUT US
While each of these techniques were effective in
                                                                                   Anthropic is a public benefit corporation
reducing discriminatory outputs, two strategies nearly
                                                                                   and AI safety research company that is
eliminated discrimination in these decision scenarios:
                                                                                   working to build reliable, interpretable,
1) appending the decision prompt with a statement
that discrimination is illegal, and 2) instructing the                             and steerable AI systems. For more
model to pretend no demographic information was                                    information, visit anthropic.com
included in the original prompt.


                                                                                                                      DECEMBER 2023
