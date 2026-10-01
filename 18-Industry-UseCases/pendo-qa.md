---
title: "Pendo Claude Managed Agents case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pendo-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:55Z"
tags: ["agents", "case-studies", "enterprise", "security"]
---

# Pendo closes the gap between shipping fast and shipping well with Claude Managed Agents

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Medium

Product:  
Claude Managed Agents[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
North America

90% success rate

On PM-reviewed evaluation sets for Claude-powered agent tasks

3 months to build an AI-native product

processing billions of data points using Claude Managed Agents and Claude Code

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

[Read more](https://claude.com/blog/claude-managed-agents)

[Pendo](https://www.pendo.io/) provides product analytics and AI tools that help companies understand user behavior and act on it to drive product adoption. Over the past few months, the company has been building Novus, a product that detects and fixes usability issues in customer applications. The system runs on Claude Managed Agents. We spoke with Zain Lakhani, Pendo's Chief AI Officer, about how Managed Agents powers their AI-native product.

## What is Pendo building with Claude?

**Zain Lakhani, Pendo:** Our users used to be product managers looking at dashboards. Now they're product engineers shipping code. That changed everything about what we needed to build. Most of what we're building now is around detecting what's going on inside your application, then cross-referencing that with your codebase to suggest fixes. A sample use case: we see a drop-off in a funnel, look at the code, and say, "This button is positioned below the fold. There's a lot of drop-off here. Here's a fix." The underpinnings of all that are deployed with Managed Agents.

## Tell me about Novus. What problem is it solving?

**Lakhani:** Product managers are becoming developers now. They're coding, they're shipping fast, and quite frankly, a lot of what's going out is difficult-to-use software that struggles to meet its adoption and retention goals. And it's not just PMs. Even developers using AI coding tools are shipping faster and doing so many multi-threaded tasks, four tickets at once, that a lot of code is hitting production without the user acceptance testing it would have received before. The velocity is there, but the feedback loop isn’t keeping up.

Novus is our answer to that. The idea is: you've shipped something, but you don't know what to ship next. You know something is broken, but you don't know what. Our approach isn't to slow anyone down. It’s: keep going fast and we'll fix it right after. Let's see how users are responding and try to optimize within minutes.

We're building this for what we call "product engineers." If we were building a tool from scratch for that persona, this is what it would look like.

## You tried building this before Managed Agents. What did that look like?

**Lakhani:** We learned pretty quickly that we're not a coding agent company. We don't want to be a coding agent company. The bulk of our intelligence, we want to offload onto a cloud agent and inject our own expertise: how do you instrument product analytics for a rapidly evolving product, what's the best way to use that data and what does good product usage look like. Then we lean on Claude's intelligence for the heavy lifting.

We spent about three months trying to get there on our own. We tried different homegrown solutions and it didn't work for us. Without Managed Agents, we were responsible for all the infrastructure around the agent itself. Session management, for example: sessions were stored on disc, and we had to locate them, retrieve them, upload them, and re-download them for every interaction. The shared memory layer required the same kind of manual work.

## How quickly did Managed Agents get you to production?

**Lakhani:** About three days. We'd been asking for the things Managed Agents provide. Session management, shared memory, sandboxing. Those were all gaps we had to fill ourselves before. Now every time we start a customer workflow, we spin up a Managed Agents session on the cloud. We don't route through our own infrastructure for the intelligence anymore. We go directly to Claude. We give it a copy of the customer's question, the intelligence insights, what we learned from past sessions, and we pair that with our Pendo data. Then it returns results.

Three days versus months of trying to build it ourselves.

## Walk me through how Novus works when it finds an issue.

**Lakhani:** A user links their codebase on GitHub and installs a Novus snippet that detects clicks and records session replays. Novus surfaces insights continuously. It might say, "We noticed a drop in this funnel from checkout to order confirmation. There are a bunch of flags. Here's a PR." That pull request is generated by Managed Agents.

Behind the scenes, every time the agent runs on top of a customer's codebase, we give it MCP tools to talk to the underlying Novus data. So if it's looking at the checkout page, it also knows that page gets a thousand clicks a day but the funnel conversion to order confirmation is only 3%. It looks at the click data, the session replays, the funnel metrics, and then reviews the code files between those steps to find fixes.

We also expose everything in Novus as an audit trail. When developers are looking at a ticket that says "checkout page is broken," they can talk to Novus to figure out the exact details: where were the rage clicks, where did the session replay go blank, what's happening in the funnel. When you call our MCP from Claude Code, we spin up a managed agent session behind the scenes to do that research and return results.

Over 90% of our customers who use the MCP and skills are using them inside Claude Code. We found that skills are really important, because otherwise you're kind of guessing on how to use the MCP effectively.

## What made you confident enough to use Managed Agents for Novus?

**Lakhani:** We actually started with a different provider and tried to build our own harness. Then we noticed that internally, nobody on our engineering team was using that provider for their own coding. So we looked at Claude Code, and then we found Claude Managed Agents.

A few things stood out. The sub-agent architecture lets us define agents in plain language. We tried other frameworks where you have to write a ton of code, construct your own graphs and nodes. With Claude, our designers and PMs are the ones defining the sub-agents and how the intelligence should work. They don't need to be engineers to do it.

We also have a very large tool set. We collect billions of data points daily, trillions total. We needed the agent to manage its own tool searching and routing across more than 150 tools without us defining every decision path. With other providers, we had to build that routing logic ourselves. With Claude, we gave it 150 tools and said, "Here's what to call when." It handled it. We know what we do best, which is product analysis. We leave the coding and reasoning to Claude.

And then the evaluation results made the decision clear. Our eval sets are a little different from traditional evals. Rather than running against synthetic benchmarks, we have actual product managers going through the results line by line and saying yes or no. That’s a much harder bar than a benchmark score because these are the same people who would reject the output in production. The agent had a 90%+ success rate against that standard.

We looked at that number and said, why would we switch? Right now all of our tasks use the most capable model. We're OK with burning token spend in exchange for intelligence. Whatever is the smartest, all the time. We'll figure out optimization later.

The benchmarks blew us away to the point where even the naysayer PMs couldn't tell if it was a human that did it or the agent.

## How did Novus go from idea to product?

**Lakhani:** Novus started as me and our CEO building together. Just the two of us were able to ship production software with the Agent SDK. That's what convinced us this was real. If two people, one of whom is also running a company, can build and launch a product, the barrier to entry is much lower than people think.

## Beyond the product, how is Pendo using Claude internally?

**Lakhani:** All of our engineers are on Claude Code. But it goes well beyond engineering. We've got an in-house package of skills that we distribute to employees: finance skills, Excel skills, some from the public library and some custom. We've set it up so everyone can code inside Claude Code through a virtual desktop.

Our finance and people analytics teams use it for everyday work. They're querying financial data, building board memos, creating dashboards. One thing we found is that Claude Code produces higher fidelity outputs than alternatives for presentations and internal tools. People are building web pages and dashboards that get deployed and shared internally. These aren't one-off analyses. They stick around.

The pace of progress for our strongest adopters is stunning. It makes our people feel powerful. You don't need a full dev team to build something useful. Build like an engineer. Think like a team of ten.

For Pendo, building Novus was more than a product decision. It was a signal about where software development is heading. As teams ship faster with AI, the gap between what's deployed and what's understood grows. Novus exists to close that gap automatically. With Claude handling the infrastructure, reasoning, and tool routing, Pendo's team can focus on what they know best: turning real user behavior into better products.

AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

[Read more](agents.md)

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
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

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
