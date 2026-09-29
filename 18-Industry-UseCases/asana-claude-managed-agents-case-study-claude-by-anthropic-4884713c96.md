---
title: "Asana Claude Managed Agents case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/asana-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:24Z"
tags: ["agents", "enterprise", "security"]
---

# How Asana built AI Teammates on Claude Opus 4.6

[Try Claude](https://claude.ai)

Case Study: Asana

Read more about how Asana supercharges work management with Claude.

[Read more](https://claude.com/customers/asana)

Asana recently launched [Asana AI Teammates](https://asana.com/product/ai/ai-teammates), powered by Claude Opus 4.6 **a**nd [Claude Managed Agents](https://claude.com/blog/claude-managed-agents). We sat down with Arnab Bose, Chief Product Officer at Asana, to discuss his thoughts on collaborative agents and why Asana chose Claude as their model layer.

## How does Asana think about the role of collaboration in AI agents?

**Bose:** The assumption in the market is that collaboration is a constraint on autonomy. We think that's backwards. We’ve seen autonomous agents struggle with work-related tasks they're given, not because the models aren't smart enough, but because the agents lack the context to execute well.

The industry defaulted to individual-first because it's the easiest problem to solve technically. What breaks at enterprise scale is coordination. AI actually increases the coordination tax. With an AI agent, a marketing manager can draft a brief in five minutes, but they still run into bottlenecks with rounds of reviews and syncing with a launch timeline that multiple teams depend on. When every person has their own AI assistant working independently, you create more fragmentation, not less. Collaboration is what makes real autonomy possible.

## How do AI Teammates actually work within Asana? Walk us through the experience.

**Bose:** It's designed to feel like adding a new team member, but one that's fully onboarded on Day 1. An AI Teammate has its own Asana account, just like any other colleague. You assign it a task, @mention it in a comment, or trigger it through a workflow rule, and it goes to work.

Take our Campaign Brief Writer. A marketer creates a request with the objective and target audience. The AI Teammate picks it up, pulls relevant context and drafts a structured brief the team can review. What used to take days of back-and-forth becomes a fifteen-minute review cycle. The key difference is that AI Teammates don't generate and disappear. They operate within the same project structure, permissions, and workflows your team already uses.

Building a custom AI Teammate doesn't require engineering resources or technical expertise. You describe the role, give it instructions, and point it at the right projects. A compliance team can stand one up to review submissions against regulatory checklists. An HR team can build one to triage employee requests.

## Why did Asana choose to build AI Teammates on Claude?

**Bose:** We evaluated available models carefully—AI Teammates uses a multi-agent architecture, and we use different models to accomplish different takes. The most important is the top-level agent responsible for coordinating a Teammate's efforts, and here Claude stood out for the quality of its reasoning, particularly when it comes to understanding nuanced, context-rich work scenarios. Work management isn't just about processing text. It requires interpreting goals, understanding dependencies between tasks, recognizing what's blocking progress, and communicating clearly with the humans in the loop. By using different Claude models in the various subagents, we're able to optimize for speed, reasoning power, or balance between the two—whatever it takes to move work forward.

We've been especially impressed by its ability to handle multi-step workflows, for instance, an AI Teammate that reviews an entire project's task history, identifies patterns in what's falling behind, and drafts a targeted status update with recommended next steps. That level of synthesis and judgment is what sets Claude apart. Claude Managed Agents removed a lot of the undifferentiated heavy lifting for AI Teammates. That let our product team stay focused on the things only we can build—enterprise-grade integration with how teams actually work in Asana.

## Your team has been building on Claude for a while now. Were there capabilities in Claude that changed something you couldn't have built a year ago?

**Bose:** We were early Claude adopters. In our experience, advancements in more recent models show that Claude excels at instruction following, with careful attention to detail that ensures our customer requests are followed to the letter and no further. This means that you can trust your AI Teammates won't surprise you by going beyond what you ask. Claude is also the best trained model at using Agent Skills, and we’ve used Skills to dramatically cut development time for core features like document editing in Microsoft Sharepoint & OneDrive. By combining Claude with the data in Asana Work Graph, AI Teammates are able to go from very basic customer requests to surprisingly complete pieces of work.


## Can you share a specific example of how an AI Teammate fits into a team's regular workflow?

**Bose:** Cross-functional launches are inherently complex. Marketing, product, engineering, and enablement are all working toward the same date. The coordination overhead is massive.

The Launch Planner AI Teammate takes on that coordination layer by living inside the workflow. It monitors progress across workstreams, flags dependencies, reports on status, and proactively surfaces what needs attention. Now the human program manager goes from spending hours stitching together spreadsheets to reviewing a structured summary and making decisions.

**Anthropic: CIOs are worried about agent sprawl: too many bots, no visibility, unpredictable costs. How should enterprises be thinking about governance?**

**Bose:** That concern came up in nearly every early enterprise conversation. CIOs told us they had dozens of point-solution bots scattered across departments. There’s no single view of what the AI was doing, and nobody could answer "what happens if something goes wrong?"

Three principles shaped our approach. First, admins control whether users can access AI Teammates, and users control which ones are active, what they access, and what actions they take. Second, every action is recorded in task history, so it's visible and auditable. And finally, customer data is never used to train models, so you don't need new governance policies to use AI Teammates.

**Anthropic: Where should an agent act on its own, and where should it always come back to a human?**

**Bose:** Our principle is that AI Teammates should be autonomous on execution, but humans own the decisions. Drafting a brief, triaging requests, flagging compliance gaps — that's execution work the AI Teammate handles on its own. When there's a judgment call, it surfaces the decision to a human with the context they need. Teams can adjust how much autonomy an AI Teammate has based on the stakes involved.

**Anthropic: What's the vision for where AI Teammates go from here?**

**Bose:** Over time, we see AI Teammates becoming more capable across complex multi-step and multi-app workflows, learning from team patterns, and proactively identifying opportunities to move work forward by integrating with additional applications that Enterprises use. And we’re going to make them even smarter by using Agent Skills to extend and systematize the work that Teammates are able to do. The vision is that people spend their time on the creative, strategic, high-judgment work that drives the business. Not AI that replaces people, but AI that works alongside them as a true teammate.

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

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
