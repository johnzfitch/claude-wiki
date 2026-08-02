---
title: "Pratham International Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pratham-international"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:05Z"
tags: ["api"]
---

# How Pratham delivers personalized assessment feedback to thousands of students across India with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Beneficial Deployments

Company size:

Large

Product:

Claude Platform

Location:

India

1,500+ student assessments

completed across 20 schools

30% → 80% grading accuracy

through iterative prompt engineering with Anthropic

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Read more

[Read more](/solutions/nonprofits)

Read more

Nonprofits


Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Video caption


Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Education

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Read more

[Read more](/solutions/education)

Read more

Education


Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Video caption


Education

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

[Prev](#)

Prev


[Pratham](https://pratham.org/) is one of the world’s largest education nonprofits. Founded 30 years ago in India, the organization reaches millions of children annually through programs spanning early literacy to vocational training. Its methods have been validated through more than 10 randomized controlled trials, including studies by MIT's J-PAL. The World Bank has also recognized the Pratham method as one of the best investments in education for global education. Today, Pratham’s programs operate in nearly every Indian state and have been adopted in more than 30 countries.

## With Claude, Pratham achieved:

- **1,500+ student assessments** completed across 20 schools
- **30% → 80% grading accuracy** through iterative prompt engineering with Anthropic
- **90% accuracy** in generating questions aligned to Bloom's Taxonomy—the universal educational framework for assessing everything from basic factual recall to complex, higher-order reasoning

## The challenge: Thousands of practice exams, no way to give individual feedback

In classrooms across India, assessments tend to tell students their results but not how to improve. A teacher managing 60 or more students has little time to provide individualized feedback on each practice exam, and the students who need that feedback the most—those in under-resourced schools and communities—are the least likely to get it. The information exists in their answers, but the problem is turning it into something a student can actually act on.

Pratham has spent 30 years working on exactly these kinds of gaps. But even with a track record of large-scale impact, Pratham kept running into a fundamental constraint: there were never enough people to grade enough practice exams to give students the repetition and feedback they needed.

The issue became especially clear in Pratham's Second Chance program, which helps young women who dropped out of school prepare for India's 10th-grade board exam, a credential required for many jobs. The program serves women without access to trained subject-matter instructors. "These women didn’t get a chance to practice the exam enough times because we didn't have enough people to grade all those answers," said Nishant Baghel, Director of Technology Innovations at Pratham and a visiting scientist at MIT Media Lab. The bottleneck wasn't curriculum or motivation. It was grading.

Pratham's ATM had already reached more than 4,000 learners and auto-graded roughly 8,000 assessments across six Indian states through the Second Chance Program. But the system was challenging to scale: grading could be inconsistent, and there was no structured way to measure accuracy against curriculum standards.

## The solution: Designing an automated assessment and feedback engine for real classroom conditions

That constraint led Pratham to create the Anytime Testing Machine, or ATM: an end-to-end practice assessment system that uses Claude to generate curriculum-aligned questions, digitize handwritten student answers, grade them against structured rubrics, and deliver personalized feedback. The system is designed for the conditions Pratham actually works in. Students write answers by hand on paper and photograph them. The system converts those images to text, then Claude evaluates the responses for content, accuracy, and expression.

Pratham chose Claude after running evaluations across multiple models. "Claude did consistently well across tasks including question generation, checking the quality of generated questions, grading, and feedback," said Sravana Chandra, AI Lead at Pratham. "This, along with Anthropic's focus on safety and responsible AI, led us to choose Claude over other LLMs."

The collaboration was hands-on. Anthropic and Pratham teams met one to two times per week over several months, not just to integrate the model but to calibrate every stage of the pipeline. Grading accuracy started at around 30% when measured against expert-reviewed benchmarks. Through iterative prompt refinement and evaluation design, the teams brought that number to roughly 80%. “We implemented an LLM-as-a-judge framework, benchmarking model evaluations against internally developed golden datasets that were manually validated by subject matter experts,” Chandra explained.

On the feedback generation side, Claude's multilingual fluency was a key advantage. “Given Claude’s linguistic capabilities, it was readily able to handle feedback generation in a mix of Hindi and English, using English terms where relevant (such as for scientific terms) while keeping most of the text in Hindi,” Chandra said. 

## The approach: Keeping teachers at the center 

A core design principle throughout: teachers review and can refine AI-generated feedback before it reaches students. It reflects Pratham's belief that the teacher's role becomes more important, not less, when AI enters the classroom.

The response from educators has borne that out. Teachers report that automating the grading frees them to focus on targeted instruction rather than administrative work. "Teachers feel empowered because they remain the final evaluators who validate AI feedback before it reaches the student," Chandra noted. The system acts as a capacity multiplier: instead of replacing judgment, it gives teachers better information to exercise it.

For students, the shift is about dignity as much as scores. In these settings, receiving a grade without explanation can be discouraging. Claude's feedback gives learners something specific to work with. Rather than seeing a wrong answer with no context, a student receives a concrete explanation of the concept they missed, with a clear direction for what to study next. 

"Human agency is something we focus on,” Baghel says. “Instead of asking what AI can do without teachers, we ask: how can AI help our teachers and students exactly where they're stuck?”

## The results: Personalized feedback reaching learners across six states

With Claude, the ATM now delivers 90% accuracy in generating questions aligned to Bloom's Taxonomy, the global educational framework. On the grading front, accuracy is roughly 80% aligned with content experts on rubric-based scoring. The Claude-powered system has completed more than 1,500 student assessments across 20 schools, with plans to expand to hundreds of thousands of students across India. Separately, the Second Chance program, which currently serves 15,000 women preparing for the grade 10 exam, plans to migrate fully to the Claude-powered pipeline by the end of 2026.

"AI tools like Claude give us a way to reimagine learning for students who do not have access to advanced educational resources," said Madhav Chavan, Pratham's co-founder. "In addition to providing personalized support to understand the textbook, the ATM innovation will help children verify and authenticate their knowledge beyond the textbooks." 

## What’s next: Flipping the education system

Chavan sees assessment as just the starting point for something larger: a system where students can eventually be tested on any topic, not only what the curriculum prescribes, and receive a credential for what they actually know.

"Instead of asking children questions about the curriculum, ask them what they know," Chavan said. "If we flip that, we can flip the education system from being a filtration mechanism to one that offers differentiated pathways based on a child's interests and background knowledge. Before AI, this was not possible."

The partnership is already expanding. Anthropic will support Pratham's Tech in TaRL (Teaching at the Right Level) initiative, an AI-powered teacher support system with a randomized controlled trial planned for several thousand students.  The two organizations are also exploring educational digital public infrastructure (including knowledge graphs), as well as geographic expansion to Kenya, Rwanda, and communities across the Global South. Pratham's three-year goal is to evolve the ATM into a learning and credentialing engine that recognizes competencies gained through non-linear pathways, available to learners worldwide.

"AI tools like Claude give us a way to reimagine learning for students who do not have access to advanced educational resources."

Madhav Chavan

Co-founder, Pratham International


Video caption


[Prev](#)

Prev


## Related stories

[The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude](/customers/epilepsy-foundation)

The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

Customer story

[Customer story](/customers/epilepsy-foundation)

Customer story

[How the Epilepsy Foundation uses Claude across the organization](/customers/epilepsy-foundation-qa)

How the Epilepsy Foundation uses Claude across the organization

How the Epilepsy Foundation uses Claude across the organization

Customer story

[Customer story](/customers/epilepsy-foundation-qa)

Customer story

[Building dignity-driven AI: A conversation with the National Domestic Workers Alliance](/customers/national-domestic-workers-alliance-qa)

Building dignity-driven AI: A conversation with the National Domestic Workers Alliance

Building dignity-driven AI: A conversation with the National Domestic Workers Alliance

Customer story

[Customer story](/customers/national-domestic-workers-alliance-qa)

Customer story

[National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude](/customers/national-domestic-workers-alliance)

National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude

National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude

Customer story

[Customer story](/customers/national-domestic-workers-alliance)

Customer story

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)

Button Text

Learn

[Button Text](#)

Button Text

Code

[Button Text](#)

Button Text

Write

- Help me develop a unique voice for an audience


  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style


  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas


  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply


  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas


  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview


  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept


  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips


  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me


  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies


  This is another test

- Write grant proposals


  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts


  this is a test

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Design

  [Claude Design](/product/design)
  Claude Design

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Features

- Claude for Chrome

  [Claude for Chrome](/claude-for-chrome)
  Claude for Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

- Skills

  [Skills](/skills)
  Skills

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Solutions

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Enterprise

  [Enterprise](/solutions/enterprise)
  Enterprise

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Legal

  [Legal](/solutions/legal)
  Legal

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Claude Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://platform.claude.com/docs)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Ecosystem

  [Ecosystem](/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Console login

  [Console login](https://platform.claude.com/)
  Console login

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Community

  [Community](/community)
  Community

- Connectors

  [Connectors](/connectors)
  Connectors

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](/plugins)
  Plugins

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/partners/services)
  Service partners

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
  Use cases

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Policy on the AI Exponential
