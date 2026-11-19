---
title: "With this release, we made several changes to how we sample and classify"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:34Z"
tags: ["news-research"]
---

With this release, we made several changes to how we sample and classify
             Claude traffic. We now sample a fixed number of conversations every hour. (In
             previous Economic Index reports, our data spanned a week of activity.)

            We also changed how we map conversations to ONET tasks. The previous
             classifier traversed a tree, first picking high-level ONET categories that we had
             hand-crafted. Now, the ONET classifier picks a detailed work activity (DWA) in
             the first step, then picks among the DWA’s constituent tasks in the second. We
             also switched over to the ONET version 30.2, released in February 2026. The
             new ONET classifier also reversed the order (the transcript appears at the end
             of the input) so that the prefix can be cached. Since Claude may have order
             preferences over the categories presented to it, we shuffle the options in the
             prefix (using a predefined set of orderings to preserve caching).

             In the second step, the ONET classifier is asked to specify the ONET tasks that
             best describe the work being done in the transcript. It is asked to provide pairs
             of {task, confidence (1-5)}, and we randomly choose a task among those with
             the highest confidence. This randomization was meant to spread the choice
             across the multiple candidates in order to avoid many transcripts piling up into
             one specific (and arbitrary) work task.

            We also changed our request clusters. The top level clusters were changed to
             the following:

             Hobbies & Lifestyle, Content Creation & Copywriting, Software Development,
             Research & Intelligence, Education & Learning, Document Processing &
             Extraction, Knowledge Retrieval & Enterprise Search, Data Analysis &
             Business Intelligence, DevOps & Infrastructure Operations, Compliance
            & Regulatory, Personal AI Assistant, Business Process & Operations, Sales
            & Revenue Operations, Cybersecurity & Threat Detection, Trust & Safety /
             Platform Integrity, Existential, Relational, and Emotional Support, Other /
             Unclear, Conversation & Meeting Intelligence, Companionship & General
             Conversation, Customer Support & Service Operations.


Appendix to “Anthropic Economic Index report: Cadences”                                          2
            Relative to prior reports, we substantially expanded the portion of each
            transcript visible to the classifier and updated how we sample from very long
            conversations that would otherwise exceed length of conversations provided
            to the classifier. We do this to give the classifier as much context as possible for
            inferring the work being performed.

            The ONET classifier is given below.


            ONET classifier

            Step 1

            You are analyzing a conversation between a user and a chatbot. Your task
            is to determine what “work activities” the chatbot is doing for the user.
            You will map the conversation to ONET work activities at various levels of
            granularity.

            Treat the conversation as a single unit unless it contains distinct,
            unrelated activities (for example, half the conversation is about fixing
            a bug and half is about personal relationship advice). Most conversations
            have one task, but some will include more than one distinct task. Pick the
            two most prominent ones if there are multiple.


            Step 1: In 1-2 sentences, summarize this conversation.


            Step 2: Pick O*NET activities that map to the activity the chatbot carries
            out for the user.


            Levels:


           - [GWA] = broadest ({n GWA} categories)
           - [IWA] = mid-level ({n IWA})
           - [DWA] = specific ({n DWA})


            Confidence guide:


            For each picked activity, assign a confidence score from 1 to 5 using the
            following rubric. The rubric asks a single question: how certain am I that
            this activity is actually being performed in this conversation?


Appendix to “Anthropic Economic Index report: Cadences”                                            3
            5 - Certain. The activity is explicitly performed in the conversation with
            direct textual evidence.


            4 - High confidence. The activity is clearly performed, inferable from
            direct textual evidence with only minor interpretation.


            3 - Moderate confidence. The activity is plausibly performed, but the
            textual evidence is partial, implicit, or open to alternative readings. A
            reasonable reviewer could either agree or disagree.


            2 - Low confidence. The activity could be performed in the conversation
            though concluding as much requires substantial interpretation.


            1 - Very low confidence. The activity may be implied by context, but there
            is no clear textual support. Picks at this level are near-noise — exclude
            unless nothing stronger exists.


            [GWA] Analyzing Data or Information
                 [IWA] Assess characteristics or impacts of regulations or policies
                   [DWA] Evaluate applicable laws and regulations to determine 		
                   impact on organizational activities
                   [DWA] Analyze impact of legal or regulatory changes
                 ...
                 [IWA] Analyze business or financial data
                   [DWA] Analyze financial records or reports to determine state of
                   operations
                   [DWA] Analyze financial information
                 ...


            <conversation>
            {TRANSCRIPT}
            </conversation>


            Output JSON only:
            <answer>{“summary”: “<1-2 sentences>”, “picks”: [{“level”: “GWA|IWA|DWA”,
           “name”: “<exact name>”, “confidence”: 1-5}], “notes”: “<optional>”}</
            answer>


Appendix to “Anthropic Economic Index report: Cadences”                                  4
            Step 2

            Consider the following exchange:

            <exchange>
            {TRANSCRIPT}
            </exchange>


            You are analyzing a conversation between a user and a chatbot. You
            previously determined these DWA-level O*NET activities for this
            conversation based on the following summary:
            Summary: {step-1 summary}
            {semicolon-joined list of picked DWAs}


            Your task now is to pick Task-level activities that map to the activity or
            activities the chatbot carries out for the user.


            Task options:
            {up to 300 candidate Task texts, shuffled, one “- ...” line each}


            Confidence guide:
            [same 1-5 rubric as step 1]


            Output JSON only:
            <answer>{“leaf_picks”: [{“name”: “<exact Task text>”, “confidence”:
            1-5}]}</answer>


Appendix to “Anthropic Economic Index report: Cadences”                                  5
            Examples of how our classifiers work

            We classify transcripts in a privacy-preserving way. To illustrate how the
            classifiers work, we present some example classifications using transcripts
            drawn from WildChat,1 an open-source dataset of user-ChatGPT interactions.
            (Some assistant’s responses were abbreviated for presentation below.)
            The examples are meant to illustrate the utility and limitations of the approach.
            In Example 2, the user asks for and receives a poem. This receives an accurate
            (based on our judgment) ONET classification: it’s labeled as “Write narrative,
            dramatic, lyric, or other types of poetry for publication,” a task belonging to
            Poets, Lyricists and Creative Writers. It is also classified as a personal use case,
            although this is hard to prove. It’s often difficult to infer how the output was used.


Appendix to “Anthropic Economic Index report: Cadences”                                              6
Appendix to “Anthropic Economic Index report: Cadences”   7
Appendix to “Anthropic Economic Index report: Cadences”   8
Appendix to “Anthropic Economic Index report: Cadences”   9
            In Example 7, the question, “Which Rust library is best for Natural Language
            Processing (NLP)?” is mapped to a sales occupation although the question is
            substantively about computer programming. The classifier focuses on what
            the Assistant is asked to do—“Recommend products”—and not on the topic
            of the request. This question might have been better assigned to a task like
            “Consult with customers or other departments on project status, proposals, or
            technical issues, such as software system design or maintenance,” which falls
            under Software Developers.


Appendix to “Anthropic Economic Index report: Cadences”                                     10
            CHAPTER 2

            Artifact classifier
            The following prompt was used to classify the most prominent concrete output
            of each exchange. Categories were presented in randomized order in each
            call, with the “other” and “none” options always listed last. The model’s answer
            was extracted from the answer tags and mapped to the display names used
            throughout Chapter 2.


            [Exchange transcript and preamble]


            What is the single most prominent concrete OUTPUT that Claude produced for
            the User in this exchange?


            Pick the single closest label:

            •    script_or_snippet: Scripts, automations, macros, code snippets, one-off
                 programs, general coding

            •    explanation_or_answer: An explanation, definition, or factual answer
                for the respondent’s own understanding

            •    plan_or_strategy: Multi-step plans — project plans, roadmaps, schedules,
                 business strategy

            •    document_or_report: Formal written deliverables — reports, proposals,
                 specs, memos, documentation

            •    app_or_website: Full applications, web/mobile apps, websites,
                 extensions, SaaS

            •    analysis_or_summary: Summaries, syntheses, analyses of existing
                 material for own use

            •    creative_writing: Fiction, poetry, songs, lyrics, screenplays, stories,
                 worldbuilding

            •    advice_or_recommendation: One-off guidance on a decision — purchase,
                 career, health, relationship

            •   idea_or_brainstorm: Brainstorm output — raw ideas, options, concept
                 exploration

            •    email_or_message: Emails, messages, DMs, replies, short interpersonal
                 communications


Appendix to “Anthropic Economic Index report: Cadences”                                        11
            •   image_or_graphic: Images, logos, illustrations, icons, photo edits,
                 posters, flyers

            •    blog_or_article: Blog posts, articles, newsletters, op-eds, published
                 web content

            •    code_fix_or_debug: Bug fixes, debugging, refactoring, code review of
                 existing code

            •    math_or_calculation: Equations, formulas, calculations, mathematical
                 solutions, proofs

            •    ml_or_ai_system: ML models, AI agents, prompts, fine-tunes, AI-powered
                 products

            •   translation: Text translated between languages

            •    marketing_or_social_content: Ad copy, social posts, product
                 descriptions, SEO, taglines, campaigns

            •    presentation_or_slides: Slide decks, PowerPoints, pitch decks, talk
                 materials

            •    game_or_interactive: Games, mods, interactive fiction, game masters/RPG
                tools

            •    academic_paper_or_thesis: Academic papers, theses, dissertations,
                 grants, literature reviews

            •    config_or_infra: Config files, IaC, deployment, DevOps, shell commands,
                 system setup

            •    chart_or_visualization: Charts, graphs, plots, dashboards, diagrams,
                infographics

            •    data_or_spreadsheet: Spreadsheets, CSVs, tables, data cleaning/
                transforms, structured data files

            •   resume_or_job_application: CVs, résumés, cover letters, LinkedIn
                 profiles, job-application materials

            •    ui_or_design_mockup: UI mockups, wireframes, design specs, prototypes

            •    audio_or_music: Music, audio, sound effects, voice synthesis, podcast
                 audio

            •    educational_material: Lesson plans, study guides, course materials,
                 worksheets, lectures, tutorials for others

            •   recipe_or_meal_plan: Recipes, meal plans, cooking instructions, diet/
                 nutrition plans

            •    video_or_animation: Video content, animations, video scripts/edits


Appendix to “Anthropic Economic Index report: Cadences”                                    12
              •    sql_or_database_query: SQL queries, database schemas, DB migrations

              •    other: A concrete output that fits none of the above

              •    none: No clear artifact


              If several outputs apply, pick the one most prominent in the exchange.


              Only choose an artifact label if it clearly describes what the exchange
              produced. If no label is a clear fit, choose none.


              [Standard API-data disclaimer]


              Your classification should be exactly one of the answer options (the
              lowercase label only), nothing else, provided in <answer> tags. For

              example, your answer could be script_or_snippet or none.


              Distribution of outputs on 1P API

              Below figure mirrors Figure 2.1 but for 1P API. On this surface, the share of
              conversations with no clear output is higher (16% vs 7% on chat and Cowork).
              Analytic outputs dominate (21%), followed by data/spreadsheet related outputs
              (14%) and explanations/answers (8%).


Figure A.1: Distribution of artifact types on 1P API.
Share of conversations with a specific output on 1P API. Top 10 output types presented individually.


Appendix to “Anthropic Economic Index report: Cadences”                                                13
             Autonomy and token consumption

             The below figure displays the normalized median token usage per artifact against
             the mean autonomy measured in the conversations producing these artifacts.
             Artifacts requiring more tokens tend to be produced with more autonomy.


Figure A.2 : Autonomy and token usage by artifact
Mean autonomy and normalized median token consumption by artifact, chat and Cowork


Appendix to “Anthropic Economic Index report: Cadences”                                         14
              CHAPTER 3

              Ten-year vision themes
              and definitions


Table A.1: Ten-year vision themes and definitions. We ask survey respondents what they hope an AI-transformed economy
will look like in ten years. We classify their free-text responses into the general themes shown here.


          1   Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., & Deng, Y. (2024). Wildchat: 1m ChatGPT interaction logs
              in the wild. arXiv preprint arXiv:2405.01470.


Appendix to “Anthropic Economic Index report: Cadences”                                                                       15
