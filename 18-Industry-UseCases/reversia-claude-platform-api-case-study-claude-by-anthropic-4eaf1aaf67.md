---
title: "Reversia Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/reversia"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:08Z"
tags: ["api"]
---

# Reversia translates e-commerce stores across 110+ languages with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Ecommerce

Company size:

Startup

Product:

Claude Platform

Location:

EMEA

99% translation accuracy

validated by native-speaking translation professionals

2–3 weeks to minutes

to launch a new language on a merchant's store

[Reversia](https://reversia.tech/) is a Paris-based e-commerce translation platform that integrates natively with Shopify app. It translates every piece of a merchant's store: product descriptions, collections, blog posts, navigation, SEO metadata, and the structured data fields that power modern Shopify storefronts. More than 100 brands use Reversia across 110+ supported languages.

## With Claude, Reversia:

- Achieved 99% translation accuracy, validated by independent native-speaking translators across multiple language pairs
- Estimated 70–80% lower cost than traditional per-word pricing, enabled by Claude-powered flat subscription model
- Reduced new language launches from 2 to 3 weeks to minutes
- Translates content updates within 1 to 3 minutes of a change, with no manual intervention
- Supports 110+ languages, including regional variants, with no per-language surcharge

## The challenge

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Machine translation wasn't built for brand copy

For brands running [Shopify stores in multiple countries](https://apps.shopify.com/reversia), localization has been a persistent bottleneck. When Reversia's co-founder Anatole Rozan looked at what was available, the options weren't close to what merchants needed.

"The existing translation apps on Shopify had massive gaps," Rozan said. "The translations themselves were literal and low quality, and most apps capped the number of languages you could add." Key content types like metafields and metaobjects often went untranslated entirely, and internal linking for SEO was broken or ignored. Merchants knew international expansion was a growth lever, but the tools weren't keeping up.

Reversia's first version used a conventional machine translation engine, and the same problems applied: the output was overly literal, and the engine produced significant errors when processing HTML content. Launching a new language still took two to three weeks of manual work, coordinating translations, verifying internal links, and checking that nothing was missed.

## The solution

Introducing Claude Sonnet 4.6

Hybrid reasoning model with superior intelligence for agents, featuring a 1M context window

Introducing Claude Sonnet 4.6


Hybrid reasoning model with superior intelligence for agents, featuring a 1M context window


Introducing Claude Sonnet 4.6

Hybrid reasoning model with superior intelligence for agents, featuring a 1M context window

## Selecting Claude for contextual understanding

When the team decided to rebuild the translation layer on an LLM, they ran a structured benchmark across multiple providers. They tested each model side-by-side on real merchant content across multiple language pairs. The criteria included translation quality, contextual understanding, tone consistency, and the ability to handle glossary rules and HTML structure.  Claude scored highest on all four quality metrics.

"It's overall more expensive than some alternatives, but we haven't found anything better to this day," Rozan said. "For a product where translation quality is the entire value proposition, that's what matters."

Reversia now runs Claude Sonnet 4.6 as its primary translation model, with Claude Haiku 4.5 running a secondary quality-check pass on all translated content to flag inconsistencies before publication. The team plans to upgrade to Opus 4.7.

## How Reversia translates stores with Claude

The core of Reversia's product is a glossary system that injects merchant-defined rules directly into Claude's prompt context at translation time. Rather than simple find-and-replace word matching, merchants can force specific term translations (always render "vestiaire" as "wardrobe" in English), exclude brand and product names from translation so they stay unchanged across every language, and add free-form natural language instructions such as "Adapt shoe size conventions for the German market" or "Translate in a modern, accessible tone for urban 20–40 year-olds." This is where Claude's reasoning matters. A conventional translation engine can swap words, but Reversia needed a model that could apply brand-specific rules around tone, audience, and terminology without breaking the output. 

Claude also translates content types that often go unaddressed in localization: metafields and metaobjects, SEO title tags, meta descriptions, hreflang attributes, canonical URLs, and internal cross-language linking. Every URL is preserved so shoppers experience identical navigation in any language.

Reversia monitors each merchant's store in real time. When content is created or updated, the platform detects the change and triggers a new Claude translation within 1 to 3 minutes. The pipeline runs on Google’s Cloud Run with Cloud Tasks managing job priority, and the app is fully native to Shopify, so merchants manage everything from within their existing admin.

"The goal is that after six months on Reversia, the AI translates as if it were an internal team member who knows your brand inside out," Rozan said. "Claude's ability to reason about context, not just words, is what makes that possible."

"Claude's ability to reason about context, not just words, is what makes it possible."

Anatole Rozan

Co-founder, Reversia


## The outcome

## Native-quality translation in minutes

What used to take two to three weeks per language now takes minutes. A merchant activates a new language, and the entire store is translated automatically: products, collections, metafields, URLs, SEO metadata, internal linking. No manual verification of links or content completeness is required.

Reversia validates the output by having native-speaking translation professionals audit batches of merchant content across multiple language pairs. Across those audits, accuracy has consistently landed at 99%. Reversia charges a flat monthly subscription rather than per-word rates. The company estimates this runs 70–80% less than traditional translation pricing for a typical store.

## What’s next 

Reversia's roadmap deepens its use of Claude on two fronts. Automatic quality scoring will have Claude evaluate its own translations before publication and flag segments that fall below a confidence threshold so merchants only review what needs attention. And persistent brand memory will soon let the system learn each merchant's preferences over time, making translations progressively more on-brand without additional glossary configuration. 

"Our customers tell us the translations feel like they were written by a native speaker who actually knows their brand," Rozan said. "That's what we were after. Claude makes that possible at scale."

"The AI translates as if it were an internal team member who knows your brand inside out."

Anatole Rozan

Co-founder, Reversia

## Related stories

[Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents](/customers/rakuten-qa)

Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents

Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents

Customer story

[Customer story](/customers/rakuten-qa)

Customer story

[Rakuten accelerates development with Claude Code](/customers/rakuten)

Rakuten accelerates development with Claude Code

Rakuten accelerates development with Claude Code

Customer story

[Customer story](/customers/rakuten)

Customer story

[How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick](/customers/shopify)

How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick

How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick

Customer story

[Customer story](/customers/shopify)

Customer story

[L'Oréal advances conversational analytics with Claude](/customers/loreal)

L'Oréal advances conversational analytics with Claude

L'Oréal advances conversational analytics with Claude

Customer story

[Customer story](/customers/loreal)

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
