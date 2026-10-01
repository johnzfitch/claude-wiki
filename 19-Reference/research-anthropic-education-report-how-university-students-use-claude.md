---
title: "Anthropic Education Report: How University Students Use Claude \\ Anthropic"
source_url: "https://www.anthropic.com/research/anthropic-education-report-how-university-students-use-claude"
category: "19-Reference"
fetched_at: "2026-09-30T06:32:07Z"
tags: ["news-research"]
---

# Anthropic Education Report: How university students use Claude

Apr 8, 2025

AI systems are no longer just specialized research tools: they’re everyday academic companions. As AIs integrate more deeply into educational environments, we need to consider important questions about learning, assessment, and skill development. Until now, most discussions have relied on surveys and controlled experiments rather than direct evidence of how students naturally integrate AI into their academic work in real settings.

To address this gap, we’ve conducted one of the first large-scale studies of real-world AI usage patterns in higher education, analyzing one million anonymized student conversations on Claude.ai.

The key findings from our Education Report are:

- STEM students are early adopters of AI tools like Claude, with Computer Science students particularly overrepresented (accounting for 36.8% of students’ conversations while comprising only 5.4% of U.S. degrees). In contrast, Business, Health, and Humanities students show lower adoption rates relative to their enrollment numbers.
- We identified four patterns by which students interact with AI, each of which were present in our data at approximately equal rates (each 23-29% of conversations): Direct Problem Solving, Direct Output Creation, Collaborative Problem Solving, and Collaborative Output Creation.
- Students primarily use AI systems for creating (using information to learn something new) and analyzing (taking apart the known and identifying relationships), such as creating coding projects or analyzing law concepts. This aligns with higher-order cognitive functions on [Bloom’s Taxonomy](https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives). This raises questions about ensuring students don’t offload critical cognitive tasks to AI systems.

## Identifying educational AI usage

When researching how people use AI models, protecting user privacy is paramount. For this project, we used Claude Insights and Observations, or "[Clio](clio.md)," our automated analysis tool that provides insights into how people are using Claude. Clio enables bottom-up discovery of AI usage patterns by distilling user conversations into high-level usage summaries, such as “troubleshoot code” or “explain economic concepts.” Clio uses a multi-layered, automated process that removes private user information from conversations. We built this process so it minimizes the information that passes from one layer to the next. We describe Clio’s privacy-first design in this [earlier blog](clio.md).

We used Clio to analyze approximately one million anonymized¹ conversations from Claude.ai Free and Pro accounts tied to higher education email addresses.² We then filtered these conversations for student and academic relevance—such as whether the conversation pertained to coursework or academic research—which yielded 574,740 conversations.³ Clio then grouped these conversations to derive aggregate education-related insights: how different academic subjects were represented; how students-AI interaction differed; and the types of cognitive tasks that students delegate to AI systems.

## What are students using AI for?

We found that students primarily use Claude to create and improve educational content across disciplines (39.3% of conversations). This often entailed designing practice questions, editing essays, or summarizing academic material. Students also frequently used Claude to provide technical explanations or solutions for academic assignments (33.5%)—working with AI to debug and fix errors in coding assignments, implement programming algorithms and data structures, and explain or solve mathematical problems. Some of this usage might also be cheating, which we discuss below. A smaller but still sizable portion of student usage was to analyze and visualize data (11.0%), support research design and tool development (6.5%), create technical diagrams (3.2%), and translate or proofread content between languages (2.4%).

Below is a more detailed breakdown of common requests across subjects.

## AI usage across academic disciplines

We next examined which subjects showed *disproportionate* use of Claude. We did so by comparing Claude.ai usage patterns with the number of U.S. bachelor's degrees awarded.⁴ The most disproportionately heavy use of Claude was in Computer Science: despite representing only 5.4% of U.S. bachelor's degrees, Computer Science accounted for 38.6% of conversations on Claude.ai (this might reflect Claude’s particular strengths in computer coding). Natural Sciences and Mathematics also show higher representation in Claude.ai relative to student enrollment (15.2% vs. 9.2%, respectively).

Conversely, Business-related educational conversations accounted for just 8.9% of conversations despite constituting 18.6% of bachelor's degrees, showing a disproportionately low use of Claude. Health Professions (5.5% vs. 13.1%) and Humanities (6.4% vs. 12.5%) were also less represented relative to student enrollment in these disciplines.

These patterns suggest that STEM students, particularly those in Computer Science, may be earlier adopters of Claude for educational purposes, while students in Business, Health, and Humanities disciplines may be integrating these tools more slowly into their academic workflows. This may reflect higher awareness of Claude in Computer Science communities, as well as AI systems’ greater proficiency at tasks performed by STEM students relative to those performed by students in other disciplines.

## How students interact with AI

There are many ways of interacting with AI, and they’ll affect the learning process differently. In our analysis of how students interact with AI, we identified four distinct patterns of interaction, which we categorized along two different axes, as shown in the figure below.

The first axis was “mode of interaction”. This could involve:⁵ (1) **Direct** conversations, where the user is looking to resolve their query as quickly as possible, and (2) **Collaborative** conversations, where the user actively seeks to engage in dialogue with the model to achieve their goals. The second axis was the “desired outcome” of the interaction. This could involve: (1) **Problem Solving**, where the user seeks solutions or explanations to questions, and (2) **Output Creation**, where the user seeks to produce longer outputs like presentations or essays. Combining the two axes gives us the four patterns presented below.

These four interaction styles were represented at similar rates (each between 23% and 29% of conversations), showing the range of uses students have for AI. Whereas traditional web search typically only supports direct answers, AI systems enable a much wider variety of interactions, and with them, new educational opportunities. Some selected positive learning examples include:

- Explain and clarify philosophical concepts and theories
- Create comprehensive chemistry educational resources and study materials
- Explain muscle anatomy, physiology, and function concepts for academic assignments

At the same time, AI systems present new challenges. A common question is: “how much are students using AI to cheat?” That’s hard to answer, especially as we don’t know the specific educational context where each of Claude’s responses is being used. For instance, a Direct Problem Solving conversation could be for cheating on a take-home exam… or for a student checking their work on a practice test. A Direct Output Creation conversation could be for creating an essay from scratch… or for creating summaries of knowledge for additional research. Whether a Collaborative conversation constitutes cheating may also depend on specific course policies.

That said, nearly half (~47%) of student-AI conversations were Direct—that is, seeking answers or content with minimal engagement. Whereas many of these serve legitimate learning purposes (like asking conceptual questions or generating study guides), we did find concerning Direct conversation examples including:

- Provide answers to machine learning multiple-choice questions
- Provide direct answers to English language test questions
- Rewrite marketing and business texts to avoid plagiarism detection

These raise important questions about academic integrity, the development of critical thinking skills, and how to best assess student learning. Even Collaborative conversations can have questionable learning outcomes. For example, “solve probability and statistics homework problems with explanations,” might involve multiple conversational turns between AI and student, but still offloads significant thinking to the AI. We will continue to study these interactions and try to better discern which ones contribute to learning and develop critical thinking.

## Subject-specific AI usage patterns

Students across disciplines engage with AI in different manners:

- **Natural Sciences & Mathematics** conversations tended toward Problem Solving, such as “solve specific probability problems with step-by-step calculations” and “solve academic homework or exam problems with step-by-step explanations.”
- **Computer Science**, **Engineering**, and **Natural Sciences & Mathematics** leaned towards Collaborative conversations, whereas **Humanities, Business, and Health** were more evenly split stronger between Collaborative and Direct conversations.
- **Education** showed the strongest preference for Output Creation, covering 74.4% of conversations. However, this usage might stem from imperfections in our filtering methods. Many of these conversations involved “creat\[ing\] comprehensive teaching materials and educational resources” and “creat\[ing\] detailed lesson plans,” indicating that teachers are also using Claude for educational support. In total, Education made up 3.8% of all conversations.

This suggests that educational approaches to AI integration would likely benefit from being discipline-specific. Our data are a first step in helping recognize the variations in how students across subjects engage with AI.

## Cognitive tasks students delegate to AI

We also explored how students delegate cognitive responsibilities to AI systems. We used [Bloom's Taxonomy](https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives),⁶ a hierarchical framework used in education to classify cognitive processes from simpler to more complex. While the framework was initially intended for student thinking, we adapted it to analyze Claude’s responses when conversing with a student.

We saw an inverted pattern of Bloom's Taxonomy domains exhibited by the AI:

- Claude was primarily completing higher-order cognitive functions, with Creating (39.8%) and Analyzing (30.2%) being the most common operations from Bloom’s Taxonomy.
- Lower-order cognitive tasks were less prevalent: Applying (10.9%), Understanding (10.0%), and Remembering (1.8%).

This distribution also varied by interaction style. As expected, Output Creation tasks, such as generating summaries of academic text or feedback on essays, involved more Creating functions. Problem Solving tasks, such as solving calculus problems or explaining programming fundamentals, involved more Analyzing functions.

The fact that AI systems exhibit these skills does not preclude students from also engaging in the skills themselves—for example, co-creating a project together or using AI-generated code to analyze a dataset in another context—but it does point to the potential concerns of students outsourcing cognitive abilities to AI. There are legitimate worries that AI systems may provide a crutch for students, stifling the development of foundational skills needed to support higher-order thinking. An inverted pyramid, after all, can topple over.

## Limitations

Our research is grounded in real-world data. That has many advantages in terms of the validity of our findings and their application to educational contexts. However, it also comes with limitations that might affect the scope of our findings:

- Our dataset likely captures early adopters, and might not represent the broader student population;
- It's unclear how representative Claude use is relative to overall AI usage in education—many students use AI tools beyond Claude.ai, meaning that we present only a partial view of their overall AI engagement patterns;
- There are likely both false positives and false negatives in how conversations were classified. We relied on conversations from accounts tied to higher education email addresses: some of these that were considered to be student-related by our classifier may actually be from staff or faculty members. Furthermore, other student conversations are likely on accounts tied to non-university email addresses;
- Due to privacy considerations, we only analyze Claude.ai usage within a single 18-day retention window. Students’ usage likely differs across the year as their educational commitments fluctuate;
- We only study what tasks students delegate to AI, not how they ultimately use AI outputs in their academic work or whether these conversations effectively support learning outcomes;
- The categorization of student-AI conversations into academic disciplines may not fully capture interdisciplinary work where AI usage patterns may differ significantly;
- Applying Bloom’s Taxonomy to the cognitive processes of an AI, as opposed to a student, is imperfect. Skills like Remembering are harder to quantify in the context of AI systems.

Institutional policies regarding AI use in education vary widely, and might significantly impact the patterns we observe in ways we cannot measure within this dataset.

## Conclusions and looking ahead

Our analysis provides a bird’s-eye view of where and how students are using AI in the real world. We recognize that we are only at the beginning of understanding AI's impact on education.

We've seen in our discussions with students and educators that AI can empower learning in remarkable ways. For example, AI has been used to support a [student's nuclear fusion reactor project](https://www.businessinsider.com/student-builds-nuclear-fusion-prototype-using-ai-glowing-plasma-orb-2024-9), and to facilitate [better communication between students and teachers in classrooms](https://www.sciencedirect.com/science/article/abs/pii/S0360131524001970?via%3Dihub).

But we are under no illusions that these initial findings entirely address the profound changes happening in education. AI is making educators' lives more challenging in all kinds of ways, and this research doesn't fully capture them. As students delegate higher-order cognitive tasks to AI systems, fundamental questions arise: How do we ensure students still develop foundational cognitive and meta-cognitive skills? How do we redefine assessment and cheating policies in an AI-enabled world? What does meaningful learning look like if AI systems can near-instantly generate polished essays, or rapidly solve complex problems that would take a person many hours of work? As model capabilities grow and AI becomes more integrated into our lives, will everything from homework design to assessment methods fundamentally shift?

These findings contribute to the ongoing discussions amongst educators, administrators, and policymakers about how we can ensure AI deepens, rather than undermines, learning. Further research will help us better understand how both students and teachers use AI, the connections to learning outcomes, and the long-term implications for the future of education.

## Anthropic’s approach to education

In addition to this Education Report, we are [partnering with universities](introducing-claude-for-education.md) to better understand the role of AI in education. As an early step, we are experimenting with a Learning Mode that emphasizes the Socratic method and conceptual understanding over direct answers. We look forward to collaborating with universities on future research studies and more directly studying the effects that AI has on learning.

## Bibtex

If you’d like to cite this post, you can use the following Bibtex key:

```
@online{handa2025education,
author = {Kunal Handa and Drew Bent and Alex Tamkin and Miles McCain and Esin Durmus and Michael Stern and Mike Schiraldi and Saffron Huang and Stuart Ritchie and Steven Syverud and Kamya Jagadish and Margaret Vo and Matt Bell and Deep Ganguli},
title = {Anthropic Education Report: How University Students Use Claude},
date = {2025-04-08},
year = {2025},
url = {https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude},
}
```

Copy

## Acknowledgements

Kunal Handa\* and Drew Bent\* designed and executed the experiments, made the figures, and wrote the blog post. Alex Tamkin proposed initial experiments and provided detailed direction and feedback. Miles McCain iterated on the technical infrastructure necessary for all experiments. Esin Durmus, Michael Stern, Mike Schiraldi, Saffron Huang, Stuart Ritchie, Steven Syverud, and Kamya Jagadish provided valuable feedback and discussion. Margaret Vo, Matt Bell, and Deep Ganguli provided detailed guidance, organizational support, and feedback throughout.

Additionally, we appreciate helpful discussion and comments from Rose E. Wang, Laurence Holt, Michael Trucano, Ben Kornell, Patrick Methvin, Alexis Ross, and Joseph Feller.

#### Footnotes

¹ These spanned an 18-day period on Claude.ai to continue managing data according to our [privacy and retention policies](https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-personal-data). For more information about how Clio protects privacy, see our [research blog](clio.md).

² In particular, we limit the analysis to accounts with email addresses associated with higher education institutions globally, such as emails with .edu and .ac.uk domains. We recognize that not all educational email addresses may be those of students. For this reason, we then filter the associated conversations to those likely addressing students’ schoolwork.

³ Clio uses Claude to filter conversations in an automated way. For this research, Clio filtered conversations to those “likely to be a student seeking help with academics, school work, studying, learning a new concept, academic research, etc?”. Our [previous paper on Clio](https://arxiv.org/abs/2412.13678) details and validates this filtering mechanism.

⁴ Via the [National Center for Education Statistics (NCES)](https://nces.ed.gov/programs/digest/d23/tables/dt23_318.20.asp?current=yes).

⁵ In our experiments, we used the terminology “Transactional” and “Dialogic” to classify conversations as we found those terms to most precisely capture the bottom-up interaction patterns surfaced by Clio. Specifically, we used Clio to classify a conversation as one of: Transactional Problem Solving, Transactional Output Creation, Dialogic Problem Solving, or Dialogic Output Creation; Clio was provided with an associated description for each interaction pattern. For ease of understanding, we use the terminology “Direct” and “Collaborative” in place of “Transactional” and “Dialogic” in this report.

⁶ In particular, we use [Anderson and Krathwohl's (2001) revision](https://books.google.com/books/about/A_Taxonomy_for_Learning_Teaching_and_Ass.html?id=JPkXAQAAMAAJ&source=kp_book_description) of Bloom's Taxonomy and their taxonomy of cognitive processes.


## Related content

### Claude discovers a novel enzyme system with CRISPR-like repeats

We’re announcing a new life sciences research group and laboratory at Anthropic. This post introduces the team behind this work and shares early results in which Claude discovered a novel enzyme system with properties reminiscent of CRISPR, with only high-level direction from our scientists.

[Read more](claude-discovers-novel-enzyme-system.md)

### Partnering with Accenture on embedded evaluation

[Read more](accenture-embedded-evaluation.md)

### Introducing the Life Sciences Verification Program

The Life Sciences Verification Program (LSVP) gives life science professionals access to Claude Mythos, Opus, and Sonnet models with a refined set of safeguards more permissive for biology-related work.

[Read more](life-sciences-verification-program.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Sales](../18-Industry-UseCases/sales.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Developer blog](https://claude.dev)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
