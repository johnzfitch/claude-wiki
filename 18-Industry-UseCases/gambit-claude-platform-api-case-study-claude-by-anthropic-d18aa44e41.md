---
title: "Gambit Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/gambit"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:43:26Z"
tags: ["api", "claude-code"]
---

# Gambit Robotics builds a real-time sous-chef with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Small

Product:

Claude Platform

Location:

North America

97%

Successful recipe parses across their pipeline

90% of code

Written with Claude Code

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)

Read more

Introducing Claude Code


See Claude Code in action—from concept to commit in one seamless workflow.

Video caption


Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](#)

Read more


Video caption


[Prev](#)

Prev


[Gambit Robotics](https://www.gambitrobotics.ai/) uses Claude to power an AI kitchen device that guides home cooks through any recipe in real time, combining camera, thermal sensors, and voice to deliver step-by-step coaching while people cook.

## With Claude, Gambit:

- Achieves ~97%+ successful recipe parses across their pipeline
- Writes 90% of their code with Claude Code
- Built a working prototype within days of first integrating Claude

## Better food. Less time. Less stress.

**‍**Cooking is one of those daily tasks that's easy to underestimate. Recipes are hard to follow with busy hands, timing multiple dishes takes real coordination, and the consequences of getting distracted range from a burned dinner to a safety hazard like leaving a burner on.

Nicole Maffeo and Eliot Horowitz founded Gambit Robotics in January of 2025 to tackle exactly this. Maffeo's background spans finance, computer vision, and ML infrastructure at Google AI research, and Horowitz is the founder and former CTO of MongoDB (\$MDB) and the CEO of Viam. The co-founders picked the kitchen because it cuts across demographics, cultures, and income levels — making it both a good environment to train models and a problem worth solving for nearly everyone.

Long term, they believe the future of the home is specialized, distributed robotics—including robotic arms capable of end-to-end cooking. But while full [automation is the long-term vision](https://www.kickstarter.com/projects/gambitcooking/gambit-robotics-never-burn-dinner-again), they believe there is massive near-term opportunity in augmentation and assistance. "People primarily want assistance to make cooking easier, quicker, and to get better results, not end-to-end automation," said  Maffeo, Co-founder of Gambit Robotics. For Gambit, success means better food in less time.

## Why Gambit chose Claude

Gambit evaluated several AI models before choosing Claude for their core product. The deciding factors were reasoning, context, and tone.

Cooking involves partial camera views, occlusions, heat changes, and users talking mid-action. Gambit needed a model that could reason through that ambiguity without hallucinating or over-correcting, while holding an entire cooking session in memory. "OCR matters, but reasoning and extended context matter more," said Maffeo. Claude uses optical character recognition to read recipe text from photos, including handwritten ones, but where it really stands apart is in what happens next. "Claude's real differentiator is its ability to reason through complex, real-world situations while maintaining long-running context and natural conversation."

Claude also follows 10–15% more prompt rules than other models Gambit tested, while keeping response times fast. That means fewer hallucinated steps, more consistent output, and less manual correction. And the tone matters too. "Claude's responses feel like a calm, competent sous-chef next to you, not a robotic checklist or a verbose explainer," said Maffeo. "That trust and clarity are critical when AI is guiding people in a physical environment."

## How Claude powers real-time cooking guidance

Gambit’s device combines a custom hardware platform with an RGB camera, a thermal camera, and a microphone and speaker. Claude processes all of this to guide users through any recipe, from any source, in real time.

Here's what happens during a typical session:

- Claude reads a recipe from a photo, a URL, or voice input, pulling out ingredients, steps, times, and temperatures
- It structures the recipe into prep steps, cooking steps, and components like protein, sauce, and sides
- It builds a live timeline of actions (add, stir, flip, reduce heat, remove), sequenced across burners
- It keeps the full session in context throughout: the recipe, prior steps, elapsed time, user preferences, and what just happened
- It watches the stove using vision and thermal data and adjusts guidance based on what's actually happening
- When something is unclear, Claude pauses or asks instead of guessing
- When users swap ingredients, change doneness preferences, or go out of order, Claude updates the plan without restarting

Users can also show prep work to the device, like chopped vegetables, and Claude evaluates whether they're ready for the next step. Over time, the system personalizes recipes to how a user actually cooks.

## How Claude Code accelerates Gambit's development

Claude Code writes 90% of Gambit's codebase. Most of their engineering work involves complex, stateful logic, and keeping context straight across workstreams is the hardest part. The team runs multiple context windows for different tickets in parallel, and Claude keeps each thread coherent while they review output with custom checks and tooling.

"Claude Code has turbo-boosted our development velocity," said Maffeo. Plan mode has been especially useful, helping re-establish context when returning to a task, cutting ramp-up time and making it easier to ship features and fix bugs.

The speed showed up early. Gambit had a working prototype within days of integrating Claude. "Claude made it possible to go from idea to working behavior remarkably fast," said Maffeo. "That speed of iteration let us test, adjust, and validate assumptions almost immediately, which is critical when building an embodied, real-time system."

## What users and testers are seeing

After six months of testing across multiple prototypes, the most consistent user feedback is that Gambit's real-time, recipe-specific guidance is what sets it apart. The system adapts naturally as people cook, whether they move faster, slower, or out of order. When personalization is combined with long-running context, it becomes a powerful engine for adaptive cooking guidance.

## What's ahead for Gambit

Gambit already goes beyond simple step-by-step instructions, handling timing, heat, and coordination in the background while engaging with the user naturally. As Claude’s vision, context windows, and speed continue to improve, that background orchestration becomes increasingly seamless — allowing Gambit to anticipate needs, adapt to changing conditions, and stay in sync with how people actually cook.

"Better vision and longer context windows let us understand not just what's happening in the moment, but how a user cooks over time," said Maffeo. "Improvements in speed make interactions feel more natural, so Gambit can stay in sync with the user while they cook."

Gambit sees hardware as the next big wave for AI. As models get cheaper and more capable, the physical devices around them matter more. "If you're building hardware that operates in the real world, you need a model that can reason under uncertainty, maintain long-running context, and communicate clearly with humans," said Maffeo. "That's where Claude stands out."


"If you're building hardware that operates in the real world, you need a model that can reason under uncertainty. That's where Claude stands out."

Nicole Maffeo

Co-founder, Gambit Robotics


Video caption


[Prev](#)

Prev


## Related stories

[Dust enables agents to go deeper at lower cost with Claude](/customers/dust)

Dust enables agents to go deeper at lower cost with Claude

Dust enables agents to go deeper at lower cost with Claude

Customer story

[Customer story](/customers/dust)

Customer story

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)

How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)

Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)

Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)

Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)

Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)

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
