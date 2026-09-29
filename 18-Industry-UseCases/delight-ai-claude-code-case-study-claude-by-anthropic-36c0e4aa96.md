---
title: "Delight.ai Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/delightai-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:34Z"
tags: ["agents", "claude-code", "enterprise", "security"]
---

# Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Code](https://claude.com/product/claude-code)

Partner:  
AWS

Location:  
North America

1 week → 1–2 days

Time to fix and redeploy a production AI agent issue

Every customer deployment regression-tested

through Claude Code-built internal tooling

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

[Delight.ai](http://delight.ai) builds AI agents for customer support on top of Sendbird's messaging, voice, and video infrastructure, which handles 7 billion monthly conversations for enterprise companies. With Claude as its primary model, its AI concierge resolves complex, high-stakes interactions across retail, travel, B2B SaaS, and marketplaces that previously needed human escalation.

We sat down with Clara Park, a software engineer on Sendbird's AI/ML team. Using Claude Code, she builds the internal tooling that gets every customer's agent ready for production.

## Anthropic: For people who aren't familiar with Delight AI, what does the product do, and where does Claude Code fit into your team's work?

**Clara Park, Sendbird:** We deploy AI agents for companies like Mixpanel and on-demand services across retail and travel, handling high-volume conversations around subscription changes, order support, and the kinds of edge cases that used to get escalated to a human. Claude is one of the primary models powering those agents. On the AI/ML team, Claude Code is also what we use to build the internal tooling that gets every Delight AI deployment ready for production. We've essentially built our whole debugging and regression testing workflow on Claude Code. It lets us test agents at scale and catch issues before they reach customers, which we couldn't really do before.

## After Claude Code, the time to fix a production AI agent issue dropped from about a week to one or two days. Walk us through what changed.

**Park:** AI agent conversations are never perfect, and errors like wrong pricing or incorrect legal language would demand an immediate fix. After an agent goes into production, it used to take us about a week to fix issues, test, and deploy. Now it takes just one or two days max. The week was mostly manual work. Every AI engineer had their own Python notebook for generating test conversations and labeling them, which was inefficient. After we integrated everything into one tool all the engineers use, the time dropped. If we see a conversation in production with issues now, we can fix it directly.

Since adopting Claude Code in November, our weekly pull request creation and PR merge counts have roughly doubled. In early November, we had around 700 PRs created and 600 merged per week; by May, we were closer to 1.6K PRs created and 1.3K merged per week. This also aligns with our Claude Code token usage growth.

## How has Delight.ai’s approach to AI evolved to get to where you are now?

**Park:** Early on, our agents were plain RAG chatbots. Then the industry moved into a deflection era, where the goal was keeping tickets away from human agents, with AI resolving the simple ones. As models got better at tool calling, longer context, and reasoning through multi-step problems, our agents evolved to covering the full lifecycle of a request. For example, a customer comes in to change their plan, realizes they were overcharged last month, and wants to update their payment method. The agent handles all three in one conversation.

Anthropic: You're running a multi-model architecture. How do you decide which model handles what?

**Park:** Different tasks have different criteria. During support conversations, we run safeguards against prompt injection, like someone falsely claiming a paid membership is free, for example. After the conversation ends, we run a separate analytics pass: classifying topics, analyzing sentiment, and checking for hallucinations.

The tradeoffs shift depending on the task. Summary generation needs to be fast. Hallucination detection can afford to be slower, but accuracy matters more there. We maintain an internal test set built from real examples of the behaviors we care about: hallucinations, out-of-scope handling, and intent classification edge cases. Whichever model performs best on a given task is what we use.

## You've built a system that clusters issues from production conversations and surfaces AI suggestions to customers about what to fix. Why Claude Opus for that work?

**Park:** Analyzing production conversations is genuinely complex work. As an engineering team, we cluster issues by topic across thousands of conversations, then generate suggested fixes. Not one-off patches, but general improvements the customer can act on. That output goes directly to the customer, so it has to be right. We tested lower-cost models first. They produced repetitive labels and kept surfacing minor issues while missing the critical ones. For a multi-step pipeline like that (cluster, synthesize, recommend) where the result is what the customer sees and acts on, we needed a model that could hold the whole thing together. That's why we use Opus 4.8.

## Walk us through the internal tooling your team has built with Claude Code.

**Park:** The first is a conversation debugger. When an agent has a problem in production, the tool fetches the conversation log, surfaces the system prompt, and shows us expected versus actual behavior side by side. We run that analysis through Opus to pinpoint where to fix it. The second is our regression testing tool. You give it a user persona and a scenario to test, and it automatically generates conversations and runs them at scale. We use it to validate every customer's agent before it goes into production. After that, the customer's own QA team runs through it and gives us the go-ahead to ship.

## Beyond the tools, how has Claude Code changed your day-to-day as an engineer?

**Park:** Volume, mostly. Before, I could get through one or two tickets a day. Now I can hand something off to Claude Code, step away, and come back when it's done. It's also changed how I approach architectural decisions. I used to take those straight to my manager or a senior engineer. Now I work through them with Claude Code first and come to the conversation with options already on the table. That's been genuinely useful.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](/product/claude-code)

## What does Delight's infrastructure look like behind the scenes?

**Park:** We run Claude on Amazon Bedrock and the direct Anthropic API as peer routes. An internal proxy picks between them per request based on real-time latency, error rates, and capacity. Whichever path is responding faster and cleaner gets the request. Rate limit errors are critical for us: customers buy an AI agent specifically because they want 24/7 support, so any gap there is a product failure.

Bedrock is valuable because it gives us additional enterprise-ready infrastructure, regional flexibility, compliance alignment for some customers, and another capacity path for reliability.

Running both paths improves reliability in two ways. It gives us provider-level redundancy, so a slowdown or throttling event on one route doesn't automatically reach the customer. And it gives us more regional and infrastructure flexibility than running on a single path. On the integration side, once a model is set up, adding a new version is straightforward. We update the model name, set parameters for new features like extended thinking, and we're running.

## Has the Claude Platform shipped any capabilities recently that impressed you?

**Park:** The [advisor tool in Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) launched last month. A faster, cheaper model handles the work from start to finish. When it hits something too complex to figure out on its own, it pauses, consults Opus, gets a plan or a correction, and keeps going. Opus only steps in at the hard moments, not for every response.

That was exactly what we were trying to build ourselves. For lighter tasks, you don't need Opus on every turn. But for genuinely complex queries, you need that reasoning power, and we wanted a system that could tell the difference automatically. It solves the exact problem we were going after.

## What's next? Where is the team taking this?

**Park:** The biggest is what we call Zero-Touch Improvement, which is really AI improving AI: the agent learns continuously, customers can see what's going wrong and why, and fixes happen without a human in the loop. Today they have to come to us to diagnose and deploy a fix. We want them to own that themselves.

Voice is the other push, where latency isn't just a metric, it's the product. A small delay breaks the feeling of a real conversation.

Finally, there’s memory. Most agents in the market still start every conversation from zero. When a customer comes back, the agent should already know their history and what's been resolved. That's the shift from a support interaction to a relationship with the brand.

Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

[Read more](https://claude.com/blog/claude-code-on-the-web)

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

[](/)

© 2026 Anthropic PBC

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](https://www.anthropic.com/research)
- [Anthropic news](https://www.anthropic.com/news)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
