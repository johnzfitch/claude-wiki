---
title: "Twilio Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/twilio-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:15Z"
tags: ["claude-code", "mcp", "prompting"]
---

# A Twilio PM on building a self-learning development platform with Claude Code


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Large

Product:

Claude Code

Location:

North America

425 API tools

packaged into a Claude Code plugin

Full AI voice agent built in 10 minutes

one iteration

Connectors: Twilio

Build powerful communications and customer engagement

Read more

[Read more](https://claude.com/connectors/twilio)

Read more

Connectors: Twilio


Build powerful communications and customer engagement

Video caption


Connectors: Twilio

Build powerful communications and customer engagement

[Prev](#)

Prev


[Twilio](https://www.twilio.com/en-us) provides programmable tools and APIs that allow developers and businesses to integrate voice, video, text messaging, email, and authentication capabilities directly into their own applications. Michael Carpenter is Director of Product on Twilio's Programmable Voice team. Over the past 11 years at Twilio, he's helped developers build on the company's communications APIs. Over 51 days, working solo with Claude Code, Carpenter built the Feature Factory: a self-learning development system that takes a brainstorm idea through a subagent pipeline to produce specs, tests, working code, and documentation. The output is a Claude Code [plugin](https://www.twilio.com/en-us/blog/developers/best-practices/prototyping-twilio-apps-claude-code-plugin) that packages hundreds of hours of Twilio domain knowledge for any developer. We spoke with Carpenter about [how the project changed](https://www.twilio.com/en-us/blog/partners/introducing-twilio-claude-connector-claude-code-plugin) how he thinks about AI-assisted development. 

## Anthropic: What made you start this project?

**Michael Carpenter, Twilio:** I spend my days helping customers build on Twilio's APIs, so I know the platform deeply: dozens of products, thousands of parameters, and the subtle interactions between them. The question I started with wasn't "can AI help?" Everyone knows AI can help write code. The question was: how do you structure AI collaboration to produce work you'd actually ship? Not prototypes. Production-ready serverless functions with test coverage, error handling, and documentation.

## Anthropic: You've been at Twilio for over a decade. What's the developer experience problem you were trying to solve?

**Carpenter**: Building production Twilio applications is challenging. Not because any single thing is difficult, but because the surface area is enormous and the failure modes are often silent. A misconfigured webhook doesn't throw an error, it just doesn't fire. A call that fails to connect can show completed status because the parent call completed even though the child call never answered. A recording callback with a relative URL generates an error that Twilio logs in the debugger, where no one looks.

I've watched developer after developer hit the same walls. Dozens of products, thousands of parameters, documentation that's comprehensive, but vast.

## Anthropic: Tell us about the Feature Factory. What does it actually do?

**Carpenter:** At the most simple level, you give it a brainstormed idea and it runs through a pipeline of specialized subagents: architect, spec, test generation, development, review, documentation. But the real leverage is that the system learns as it goes. I built hooks that catch new learnings whenever an error occurs, and [custom skills](https://www.twilio.com/docs/ai/skills) that capture domain knowledge from every session.

When I started, I had a simple learnings file where I'd write down API quirks and debugging insights. But that failed within four sessions. My next step was to build a documentation flywheel: hooks that write suggestions to a file Claude can read, then auto-clearing when you actually update the docs. My theory is that the system capturing knowledge has to be lower-friction than the discipline it replaces. 

You can see what that buys you. A self-service IVR that used to take multiple iterations now takes 5 minutes and one pass. A full AI voice agent that takes pizza orders—recording, transcription, and SMS confirmation— now takes just 10 minutes.

The [plugin](https://www.twilio.com/en-us/blog/developers/best-practices/prototyping-twilio-apps-claude-code-plugin) is the output of all of that. It packages hundreds of hours of accumulated Twilio knowledge so any developer can use Claude Code with Twilio and get the benefit of everything the system has ever learned.

"The plugin packages hundreds of hours of accumulated Twilio knowledge so any developer can use Claude Code with Twilio and get the benefit of everything the system has ever learned."

Michael Carpenter

Director of Product, Twilio

## Anthropic: You built this as a product manager, not a software engineer. How did that work in practice?

**Carpenter:** I can now ship code in domains where I'm not an expert. This project ended up being more than 1,000 commits over 90 days, 425 MCP tools, a published npm package, and a Claude Code plugin. But the reason it worked isn't because Claude Code wrote the code for me. It's because I know Twilio's platform deeply, and Claude Code could hold the entire codebase in context and reason across it. I brought the domain knowledge, and Claude Code brought the ability to execute on it at a scale I couldn't alone.

## Anthropic: There's a great story in your writeup about the MCP server being broken for 35 days without anyone noticing. What happened?

**Carpenter:** The MCP server, which was wrapping every Twilio API I could get my hands on, had been silently failing since the day it was configured. Claude Code would spawn the process, get EOF, and quietly move on, with no error or warning. That meant thirty-five sessions of building and testing, all without the tool infrastructure the whole system was designed around.

In those 35 sessions, we built 8 validated use cases, documented 31 architectural decisions, created 7 specialized subagents, and published an npm package. All without the tools. The real question was how any of that productive work happened anyway. 

I finally found the fix, which was 53 lines of TypeScript. But the more important thing I learned is that Claude Code isn't a tool executor, but more of a cognitive amplifier. The tools help, and once they worked, the deep validation caught bugs that manual testing never would have found. But the real value is the collaboration: the thinking, architecture, and pattern recognition, as well as ability to hold the entire codebase in context and reason across it.

## Anthropic: What surprised you about working this way?

**Carpenter:** How good Claude is at finding patterns across a codebase. Early on, a Twilio function was throwing errors. I found the bug: a response body was being passed as an object instead of a string, which crashes the serverless runtime. Fixed it. But the alerts kept firing, because there was a second, unrelated bug producing the same error code.

Once we understood both root causes, Claude searched the entire codebase and found 29 more instances of the same pattern across different files. Twenty-nine latent bugs, all waiting to fail the same way in different functions at different times. Found in seconds with a single regex. A human debugging this would have fixed the one function that was throwing errors and moved on. Claude's instinct to search broadly turned a bug fix into a systemic cleanup.

The other thing that surprised me was the pushback. The moments that matter most aren't the ones where Claude executes instructions perfectly. They're the ones where it says, "this approach has three problems," followed by evidence from the codebase. Or when it catches something I missed: a check that's testing for property existence when the property is always present, and you need to check its value instead. That's not autocomplete. That's a colleague with perfect memory and infinite patience.

## Anthropic: Before writing any business logic, you set up a model for what the AI should and shouldn't do autonomously. Why start there?

**Carpenter:** The first real decision was about boundaries. The Twilio CLI deploys functions, purchases phone numbers, and manages infrastructure. Those operations cost money, change production state, and are hard to reverse. So I drew a line: the MCP server reads logs, sends test messages, checks call status, and validates configurations. It never invokes CLI commands. CLI is for humans. MCP is for agents.

That created a four-tier risk model. Tier one, fully autonomous: read-only queries like logs and status checks. Tier two, controlled with guardrails: sending a rate-limited test SMS. Tier three, human approval required: deploying code, configuring webhooks, purchasing numbers. Tier four, never autonomous: deleting resources, force-pushing, skipping hooks.

Every tool, every operation, every decision in the next 90 days was filtered through that model. When chaos validation later tested whether the system would recommend operations that trigger billable API activity, the tier model caught it. Not because someone thought to test for it specifically, but because the architecture encoded the principle: operations with financial consequences require human approval. Trust is architectural, not accidental.

## Anthropic: You've talked about prompt quality being more important than infrastructure. What does that mean in practice?

**Carpenter:** When I went back and analyzed our sessions, I found a handful of friction events where the agent made the wrong choice. Those were things like misdiagnosing a failure, skipping a validation phase, using the wrong tools. My first instinct was to build more infrastructure, like a queue runner, or retry logic, or an orchestration that would force the right sequence.

But the fix was actually a 40-line markdown file. It named the specific tools to use, said "do not skip live call phases," and specified per-phase retry budgets. Every one of those friction events was solvable by encoding domain knowledge into the prompt.

This pattern held everywhere. When headless sessions wasted money on infrastructure validation, the fix was a different prompt. When chaos validation needed scope gating, the fix was one sentence in the architect prompt. When the AI isn't doing what you want, the answer is almost always "communicate better," not "build more." CLAUDE.md is your most powerful tool because it loads into context every session. Every instruction there applies everywhere, automatically.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)

Read more

Claude Code


Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption


Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

"Claude Code could hold the entire codebase in context and reason across it."

Michael Carpenter

Director of Product, Twilio

## Anthropic: How did you get from manually approving every step to running the system autonomously?

**Carpenter:** The temptation is to skip steps and go from "this works interactively" to "let it run autonomously." Each intermediate stage teaches you something about how the system fails, and that knowledge is what makes the next stage safe.

It took 23 design decisions and 40 days. On day one, I had human approval gates after every pipeline phase. Six interruptions per feature. By day 45, the system ran headless: no human in the loop, real phone calls, real validation.

Each step was earned. Stall detection came from surveying other autonomous coding systems and finding that nobody relies on fixed turn limits. We built pattern detection: same tool called three times with the same input means stall, alternating patterns mean oscillation, no file changes means idle. Then safety floors replaced infinite budget defaults. Then sandbox mode for isolation. Then phase retry to preserve partial progress when an agent hit its turn limit.

## Anthropic: How do you think about building your own memory and dreaming systems versus adopting managed infrastructure?

**Carpenter:** I don't think of it in standard “build versus buy” framing. I think of it as: build core pieces or an MVP, then integrate. I built local memory and dreaming myself because the patterns are really just API calls. Plus, integrating anything deeply into our workflow means understanding the abstraction first. But the problem changed as we scaled. Single-developer memory is a file-system problem, but multi-tenant agent memory with audit trails is an infrastructure problem. Those are different problems with different "right answers."

Building it myself is what allows me to be a good evaluator. I know *exactly* what dreaming costs us, what memory search latency looks like, what curation rules really matter. So when I look at Managed Agents, I'm evaluating it from first principles, not from the docs or theory. That means if we move to managed infrastructure, we'll do it for the right reasons, not out of convenience or hypotheses. What surprised me is that speed comes from taking the time up front to develop deep understanding. We mapped the problem space ourselves, so when Anthropic's announcement came it was validation, not revelation.

## Anthropic: What would you tell someone starting their first serious Claude Code project?

**Carpenter:** CLAUDE.md is your project's constitution, not a README. Write it as if you're onboarding a brilliant colleague who forgets everything between sessions. Because you are. Every instruction that isn't in CLAUDE.md is an instruction that will be forgotten tomorrow.

Document what burns you and automate what you forget. Build the flywheel before you need it. The system that captures knowledge has to be lower-friction than the discipline it replaces.

Graduate trust with evidence, not hope. Start supervised. Increase autonomy one step at a time. The path from "approve everything" to "run headless" should be paved with evidence at every stage.

And write your collaboration guidelines early. On day four, I wrote this into our CLAUDE.md: "We are collaborators working together on technical problems. Communication should be direct, professional, and collegial. It's encouraged to push back with evidence when you disagree." I never revised it. It turned out to be the most important instruction in the entire project.

Skills

Get consistent results on specialized tasks. Skills package your expertise so Claude delivers expert-level output every time.

Skills


Get consistent results on specialized tasks. Skills package your expertise so Claude delivers expert-level output every time.

Video caption


Skills

Get consistent results on specialized tasks. Skills package your expertise so Claude delivers expert-level output every time.

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
