---
title: "Our analysis is based on privacy-preserving analysis. Throughout the report"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf"
category: "19-Reference"
fetched_at: "2026-10-28T06:38:56Z"
last_modified: "Tue, 24 Mar 2026 01:01:08 GMT"
tags: ["news-research"]
---

Our analysis is based on privacy-preserving analysis. Throughout the report
           we analyze a random sample of 1M conversations from Claude.ai Free, Pro and
           Max conversations (we also refer to this as “consumer data” since it mostly
           represents consumer use) and 1M transcripts from our first-party (1P) API
           traffic (we also refer to this as “enterprise data” since it mostly represents
           enterprise use).


           Both samples come from February 5, 2026, to February 12, 2026. We continue
           to manage data according to our privacy and retention policies, and our
           analysis is consistent with our terms, policies, and contractual agreements.
           For 1P API data, each record is a prompt-response pair from our sample period
           which in some instances is mid-session for multi-turn interactions.


           In the analysis described in Chapter 2, we rely on statistical models in which
           minimum aggregate thresholds for both unique accounts and conversations
           are satisfied for any reported statistics. For example, in our regression
           analysis we only estimate fixed effects for groupings that satisfy our privacy
           requirements—otherwise such cells are dropped prior to estimation.


anthropic.com                                                                               2
           Key terms

           1P API: First-party API. This traffic represents users accessing Claude
            programmatically, rather than through a web user interface (as with Claude.ai).


           Log-level data: This refers to analysis performed at the log level, as opposed
           to aggregated task groupings. This is necessary for estimating the correlation
           between two primitives, for example.


           Request clusters: A bottom-up taxonomy of what people ask Claude to do,
           generated using a privacy-preserving method that groups semantically similar
           conversations.
           Automation and augmentation:
           •    Automation encompasses interaction patterns focused on task completion:

                   •   Directive: Users give Claude a task and it completes it with minimal
                       back-and-forth

                   •   Feedback Loops: Users automate tasks and provide feedback to
                       Claude as needed

           •    Augmentation focuses on collaborative interaction patterns:

                   •   Learning: Users ask Claude for information or explanations about
                       various topics

                   •   Task Iteration: Users iterate on tasks collaboratively with Claude

                   •   Validation: Users ask Claude for feedback on their work

           Economic Primitives: Simple measures of how Claude is used generated
           by asking Claude specific questions about anonymized conversations and
           transcripts. Our Economic Primitives cover five dimensions relevant to AI’s
           economic impact: user and AI skills, how complex tasks are, the degree of
           autonomy afforded to Claude, how successful Claude is, and whether Claude is
           used for personal, educational, or work purposes.

           See Table A.1 for additional details for each Economic Primitive.


anthropic.com                                                                                 3
                                   Economic primitives overview

  Task                  Human time         Estimate how many hours a competent professional would need to complete the tasks done by the Assistant.
  complexity            estimate           Assume they have:

                                           •   The necessary domain knowledge and skills            •   Access to required tools and resources
                                           •   All relevant context and background information      •   No access to AI tools to assist with the work


                        Human with AI      Estimate how many minutes the User spent completing the tasks in the prompt with the Assistant. Consider:
                        time estimate
                                           •   Number and complexity of User messages               •   Realistic typing/reading speeds
                                           •   Time reading Assistant’s responses                   •   Time implementing suggestions or running
                                           •   Time thinking and formulating questions                  code outside of the conversation
                                           •   Time reviewing outputs and iterating                     (only if directly relevant to the tasks)


                        Multitasking       Did the User multitask in this conversation? Choose from these options:

                                           •   Yes: the User was working on multiple tasks over the course of the conversation
                                           •   No: the User was working on a single task over the course of the conversation


  Human                 Human ability      Could the User have completed this task by themselves? Choose from these options:
  and AI skills         to complete
                        task alone         •   Yes: the User would have been able to complete the task without the Assistant, even if it would have
                                               taken more time
                                           •   No: the User would not have been able to complete the task without the Assistant, even with more time


                        Human education    Estimate how many years of formal education someone would need to understand the User prompts in this
                        years              conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.


                        AI education       Estimate how many years of formal education someone would need to understand the Assistant responses
                        years              in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.


  Use case              Work vs.           Analyze whether the conversation between the User and the Assistant primarily focuses
                        coursework         on work, coursework, or personal use. Analyze the use case according to these categories:
                        vs. personal
                                           •   Work: professional use to accomplish tasks that are part of the User’s job
                                           •   Coursework: use to help the User complete coursework in educational contexts
                                           •   Personal: use for any domain that is not work or coursework


  AI autonomy                              Estimate how much autonomy the Assistant had to make decisions in this conversation
                                           (a discrete number ranging from 1 - 5, where 1 is none and 5 is extreme).


  Task success                             Did the Assistant complete the task provided by the User successfully? Choose from these options:

                                           •   Yes: the Assistant completed the task provided by the User successfully
                                           •   No: the Assistant did not complete the task provided by the User successfully


Table A.1: Economic Primitives Overview
This table provides definitions for the Economic Primitives we study in this report.


anthropic.com                                                                                                                                           4
                                         Additional figures and results


Figure A.1: Shifts in the usage across occupational categories
This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API.¹


Figure A.2: Cumulative job coverage
This plot shows changes in the cumulative share of occupations with task coverage at or exceeding 25%, 50%, or 75%.


anthropic.com                                                                                                                         5
Figure A.3: Collaboration mode share, 1P API
This plot shows changes in the share of automation vs. augmentation in 1P API traffic.


              1
                  This figure uses 2019 O*NET-SOC codes, while previous reports use the
                  2010 vintage.


anthropic.com                                                                             6
