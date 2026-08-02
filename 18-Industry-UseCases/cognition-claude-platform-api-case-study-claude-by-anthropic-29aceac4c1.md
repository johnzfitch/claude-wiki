---
title: "Cognition Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/cognition"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:46Z"
tags: ["agents", "api", "enterprise", "evaluation"]
---

# Building an autonomous AI engineer: A Q&A with Cognition


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


[Play video](#)

Play video

Industry:

Software

Company size:

Startup

Product:

Claude Platform

Location:

North America

3.5x increase in merged PRs

per week after adopting Claude Sonnet 3.6

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

Read more

[Read more](https://claude.com/problem-solvers)

Read more


The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

Video caption


The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

[Prev](#)

Prev


[Cognition](https://cognition.ai/) is the company behind Devin, one of the first AI software engineers. Devin launched in early 2024 and has since become an established name in AI engineering and enterprise AI transformation. The early move into the emerging AI software engineering space drove explosive demand; Cognition has deployed its AI engineers across enterprises including Goldman Sachs, Mercedes-Benz, and the US Army.

Scott Wu, CEO, and Walden Yan, co-founder and CPO, sat down with Anthropic to discuss what makes autonomous agents fundamentally different from code-completion tools, how Claude's capabilities have shaped Devin's evolution, and what's ahead for software engineering. 

## Anthropic: You've always had a bet on autonomous agents, going back to early 2024 when the technology was much earlier. What's uniquely challenging about powering an agent that works autonomously?

**Scott Wu, Cognition:** The bar for an autonomous agent is fundamentally different from the bar for a code-completion tool. Users systematically under-specify tasks. They have context the agent doesn't. The agent has to clarify, ask the right questions back, and infer intent correctly, because a wrong starting point means the entire trajectory goes off course.

The agent also has to stay focused over long horizons without drifting. A lot of our engineering work goes into trajectory monitoring, which means detecting when an agent is going off track, and steering it back. Before today's frontier models, the primary failure mode was consistency. Some trajectories would work, but the output quality degraded over long contexts, variance was high, and it just wasn't reliable enough to trust autonomously.

Real-world success for us looks like this: a well-scoped ticket comes in, the agent ships it, the PR gets merged. That's the bar our customers hold us to

**Walden Yan, Cognition:** Claude models were very early on, natively agentic. Devin has a lot of particular behaviors that we like to keep around for our users. Having a long set of evals allows us to have the confidence that when we swap a new model in, we don't regress on any important product behaviors, which is really important for us. We want to be able to speak definitively internally about which models we think are best and use those for our capabilities. 

## How would you describe what the overall experience of working with Devin is like? 

**Scott:** The whole idea is getting you to a point where you as a human can operate in terms of higher level decisions and trade-offs and not have to think about every single little detail in the code. Devin will send you a screen video recording of ‘You told me to fix a bug, I fixed it, here's the PR, but by the way, I actually went through and clicked through myself to make sure it works now.’ And here's like a video of that working.

## Cognition routes across multiple models. What specifically makes Claude well-suited for the autonomous, long-horizon work you route to it?

**Scott:** One is just the ability to do long-running tasks. With a lot of models, you generally see that after enough time, they get confused or forget what they were doing. Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task.

Two is having intelligent usage of the tools available to it. With Devin, we give the model access to all sorts of different things: the PR itself, the commit history, different files of the codebase, the ability to ask a clarifying question. It takes a certain kind of intelligence to know how to use the different tools at your disposal, or when to use a tool at all.

The third is more subjective. You want to be able to give the agent a two-line description of what you *think* needs to happen and have it expand from there and already know what you mean about the other details. It’s a little different from the binary of ‘Did it do the task or not?’ We've often found that Claude models perform particularly well at that.

"Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task."

Scott Wu

CEO, Cognition

## When you get access to a new model, what does the evaluation process look like?

**Scott:** We have our own set of internal evals that cover all the different parts of software engineering. We have an eval for how good you are mechanically at performing an edit in a file. We have one for how good you are at locating the right files in the codebase that correspond to this issue the user described. And then we have end-to-end evals for what we'd expect a software engineer to do.

When Claude Sonnet 3.6 came out in 2024, that was the biggest leap we'd seen in that benchmark score. We started using it internally, and we 3.5xed merged PRs per week because there were just so many more tasks you could start to work with that model on.

## How quickly does a new Claude model typically make it into Devin's production workflows?

**Walden:** We try to implement it as soon as we have access. If we're confident the model is strictly better than what we have out there, we'll usually straight swap out on day one. The feedback loop goes both ways. Anthropic has sent engineers to work with us to try new capabilities with models. And then the feedback we gave and sent a lot of examples on—that did improve the future models, which was really nice to see.

## You've talked about how much engineering sits in the harness around the models. Can you give a sense of what that infrastructure looks like?

**Scott:** Every time we change which model handles which part of the workflow, the harness has to change with it. Prompts, tool definitions, context management, trajectory monitoring, and guardrails are all tuned to the specific model behind them. Keeping that surface area stable while the underlying model mix evolves is a constant engineering investment. Roughly 50 to 70 engineers work on the model integration surface across the full product.

And there's so much depth in software engineering as a whole. VM sandboxing alone is something we've rebuilt many times. How fast is the VM ready from the moment you kick off the agent? That's a really hard problem, because it's not just the actual spin up. The agent has to be ready to go with the latest code, the latest dependencies, the right repos. 

## Enterprise usage of Devin has been accelerating. What's driving that growth?

**Walden:** ** **I think our usage of Devin since late last year is up at least 7x. It's partially new use cases like debugging and security scanning. It's also partially that greater long-horizon consistency means people can let these agents run for longer and trust them.

So much of software engineering is actually maintenance and fixing bugs, not building new software. If you can free up their time by having Devin automatically start responding to bugs, that would be massively helpful. We are seeing the new Claude models getting quite good at using third-party MCPs to look at logs and incidents.

## As coding itself gets easier with AI, how do you think about where Cognition focuses?

**Scott:** One thing that happens now that the part of writing the code gets so much easier is you actually start thinking about all the other parts of the process and how to really optimize this. 

I really don't believe that there's just a single product for all of code or all of software engineering. The question for us has always been, what is the thing that we really want to narrow in on and focus on above all else? And how are we going to make that into a true best-in-the-world experience? For us, that is largely the entire flow of how you work with and use a full remote agent.

## Looking ahead, what are you most excited about?

**Scott:** I love typing code, but I don't think it's something that we'll need to do for all that much longer. Right now, our engineers at Cognition don't type code anymore. You can just give instructions and prompts to your agents and have them go work on it. We're pretty quickly getting to a world where you can really just work with the specs and diagrams of what you want your product to be, and English can be the source of truth of how we build software. 

That's exciting because it means way more people will get the chance to build software of their own. Walden has this line I've always loved: for so long we've all been living in survival mode of Minecraft, and pretty soon we're going to be in creative mode. It really feels like we’re living in the golden age of software engineering. There’s so much more for us to do together than separate, and that’s what we’re excited about. 

**Walden:** The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals, having it come up with its own tasks, and spin up its own engineering team to go execute on. 

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Read more

[Read more](#)

Read more

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Video caption


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

"The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals."

Walden Yan

Co-founder and CPO, Cognition


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
