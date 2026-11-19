---
title: "Core Al Fluency Framework Terms"
source_url: "https://www-cdn.anthropic.com/4396730ed190e691a3712cf2fd6bfe35509deca2.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:25Z"
tags: ["news-research"]
---

Core Al Fluency Framework Terms                                             Discernment
                                                                           Thoughtfully and critically evaluating AI outputs,
Al Fluency                                                                 processes, behaviors and interactions. Includes assessing
The ability to work with AI systems in ways that are                       quality, accuracy, appropriateness, and determining areas
effective, efficient, ethical, and safe. Includes practical                for improvement.
skills, knowledge, insights, and values that help you adapt
to evolving AI technologies.                                                 • Product Discernment: Evaluating the quality of
                                                                               what AI produces (accuracy, appropriateness, coherence,
The4Ds                                                                         relevance)
The four core competencies of AI Fluency: Delegation,
                                                                             • Process Discernment: Evaluating how the AI arrived at
Description, Discernment, and Diligence.
                                                                               its output, looking for logical errors, lapses in attention,
Delegation                                                                     or inappropriate reasoning steps
Deciding on what work should be done by humans, what                         • Performance Discernment: Evaluating how the AI
work should be done by AI, and how to distribute tasks                         behaves during your interaction, considering whether
between them. Includes understanding your goals, AI                            its communication style is effective for your needs
capabilities, and making strategic choices about
collaboration.                                                              Diligence
                                                                           Using AI responsibly and ethically. Includes making
 • Problem Awareness: Clearly understanding your goals                     thoughtful choices about AI systems and interactions,
   and the nature of the work before involving AI.                         maintaining transparency, and taking accountability for
 • Platform Awareness: Understanding the capabilities                      Al-assisted work.
   and limitations of different AI systems.
                                                                             • Creation Diligence: Being thoughtful about which
 • Task Delegation: Thoughtfully distributing work                             AI systems you use and how you interact with them
   between humans and AI to leverage the strengths of each.
                                                                             • Transparency Diligence: Being honest about Al's role
Description                                                                    in your work with everyone who needs to know
Effectively communicating with AI systems. Includes clearly                  • Deployment Diligence: Taking responsibility for
defining outputs, guiding AI processes, and specifying                         verifying and vouching for the outputs you use or share
desired AI behaviors and interactions.

 • Product Description: Defining what you want in terms                     Human-Al Interaction Modes
   of outputs, format, audience, and style                                 Automation
 • Process Description: Defining how the AI approaches                     When AI performs specific tasks based on specific human
   your request, such as providing step by step instructions               instructions. The human defines what needs to be done,
   for the AI to follow                                                    and the AI executes it.
 • Performance Description: Defining the Al's behavior                     Augmentation
   during your collaboration, such as whether it should be                 When humans and AI collaborate as thinking partners to
   concise or detailed, challenging or supportive                          complete tasks together. Involves iterative back-and-forth
                                                                           where both contribute to the outcome.

                                                                           Agency
                                                                           When humans configure AI to work independently on their
                                                                           behalf, including interacting with other humans or AI. The
                                                                           human establishes the Al's knowledge and behavior patterns
                                                                           rather than specifying exact actions.


Copyright 2025 Rick Dakan, Joseph Feller, and Anthropic. Released under the CC BY-NC-SA 4.0 license.
Al Technical Concepts                                                       Reasoning or thinking models
                                                                           Types of AI models specifically designed to think step-by-
Generative Al                                                              step through complex problems, showing improved
AI systems that can create new content (text, images, code,                capabilities for tasks requiring logical reasoning.
etc.) rather than just analyzing existing data.
                                                                           Temperature
Large language models (LLMs)                                               A setting that controls how random an Al's responses are.
Generative AI systems trained on vast amounts of text data                 "Higher" temperature produces more varied and creative
to understand and generate human language.                                 outputs (think boiling water bubbling), while "lower"
                                                                           temperature produces more predictable and focused
Claude
Anthropic's family of large language models.                               responses (think ice crystals).

                                                                            Retrieval augmented generation (RAG)
Parameters
The mathematical values within an AI model that determine                  A technique that connects AI models to external knowledge
how it processes information and relates different pieces of               sources to improve accuracy and reduce hallucinations.
language to each other. Modern LLMscontain billions of                      Bias
parameters.                                                                Systematic patterns in AI outputs that unfairly favor or
Neural networks
                                                                           disadvantage certain groups or perspectives, often reflecting
Computing systems similar to, but distinct from, biological                patterns in training data.
brains. Composed of interconnected nodes organized in
layers that learn patterns from data through training.                      Prompt Engineering Concepts
                                                                            Prompt
Transformer      architecture
                                                                           The input given to an AI model, including instructions and
The breakthrough AI design from 2017that enables LLMsto
                                                                           any documents shared.
process sequences of text in parallel while paying attention
to relationships between words across long passages.                        Prompt engineering
                                                                           The practice of designing effective prompts for AI systems
Scaling laws
                                                                           to produce desired outputs. Combines clear communication
As AI models have grown larger and trained on more data                    with Al-specific techniques.
with more computing power, their performance has
improved in consistent patterns. This is an empirical                      Chain-of-thought        prompting
observation. Perhaps most interestingly, entirely new                      Encouraging an AI to work through a problem step by step,
capabilities can emerge at certain scale thresholds that                   breaking down complex tasks into smaller steps that help
weren't explicitly programmed.                                             the AI follow your thinking and deliver better results.

Pre-training                                                                Few-shot learning (n-shot prompting)
The initial training phase where AI models learn patterns                  Teaching AI by showing examples of the desired input-
from vast amounts of text data, developing a foundational                  output pattern. The "N" refers to the number of examples
understanding of language and knowledge.                                   provided. Helps the model understand what you want
                                                                           without lengthy explanations.
Fine-tuning
Additional training after pre-training where models learn                   Role or persona definition
to follow instructions, provide helpful responses, and avoid               Specifying a particular character, expertise level, or
generating harmful content.                                                communication style for the AI to adopt when responding.
                                                                           Can range from general roles ("speak as a UX design expert")
Context window                                                             to specific personas ("explain this like Richard Feynman
The amount of information an AI can consider at one time,                  would").
including the conversation history and any documents
you've shared. Has a maximum limit that varies by model.                   Output constraints/         output formatting
                                                                           Clearly specifying within your prompt the desired format,
Hallucination                                                              length, structure, or other characteristics of the Al's
A type of error when AI confidently states something that                  response to ensure you get exactly what you need.
sounds plausible, but is actually incorrect.
                                                                           Think-first    approach
Knowledge cutoff date                                                      Explicitly asking the AI to work through its reasoning
The point after which an AI model has no built-in knowledge                process before providing a final answer, which can lead
of the world, based on when it was trained.                                to more thorough and well-considered responses.

Copyright 2025 Rick Dakan, Joseph Feller, and Anthropic. Released under the CC BY-NC-SA 4.0 license.
