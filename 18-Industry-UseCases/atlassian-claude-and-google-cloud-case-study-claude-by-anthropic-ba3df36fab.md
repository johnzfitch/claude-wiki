---
title: "Atlassian Claude and Google Cloud case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/atlassian"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:24Z"
tags: ["agents", "enterprise", "security"]
---

# How Atlassian builds AI agents teams can trust with Claude and Google Cloud

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](https://claude.com/product/claude-code)

Partner:  
Google

Location:  
Australia

5 million+ agents executed

in customer business workflows each month

Millions of users on Rovo Chat

with Claude as a base agent model

[Atlassian](https://www.atlassian.com/) makes the software that teams use to plan, build, and ship their work together, including Jira, Confluence, and more than 20 other products used by over 350,000 customers worldwide. AI is now built into everything Atlassian ships, and customers are asking it to take on more of the real work itself. Claude handles the most complex and long-running of that work, on a platform built with Google Cloud.

## At Atlassian, Claude helps power:

- More than 5 million AI agents running in customer business workflows each month
- Rovo Chat, its in-app assistant used by millions, with Claude as a base agent model
- Rovo CLI, the primary experience for developer AI
- Rovo Max, an early-access mode of Rovo Chat, which plans, reasons, and executes across Atlassian tools taking on complex work.
- Rovo Studio, which uses a variety of models, including Claude (Opus 4.8 and Sonnet 4.6) for low code/no code agents and automations

## The challenge

## Agents customers trust with work that matters

Chatting with an AI assistant, asking it to summarize a thread or draft an update, still leaves the work to a person. Atlassian's customers want to hand that work to a trusted and capable agent instead: reviewing incoming contracts as a first line of defense, triaging support tickets, and surfacing new sales leads.

Handing an agent that kind of consequential, repeatable work raises a higher bar than chat. The agent has to use Atlassian's own capabilities from inside the product itself, the way a person does, in order for the business to trust the result. "We're good at building UIs for humans," said Sherif Mansour, Head of AI at Atlassian. "The next muscle is making sure those capabilities are usable by agents as well. How do I make sure agents are an equivalent customer of our software?"

Trust is hardest to earn where the work is most valuable: complex, long-running tasks where a wrong answer compounds the longer an agent works. It only gets harder as Atlassian opens more of its surface to agents, across hundreds of AI capabilities in more than 20 apps, and trust hinges on how they are deployed, what they can access, and what they return. Until agents earn it, customers won't hand them the work worth automating. "Scale, complexity, and trust seem to be the three biggest themes that keep coming up over and over again," Mansour said.

Claude on Google Cloud

Build advanced AI agents with Claude on Google Cloud.

[Read more](https://claude.com/partners/google-cloud)

## The solution

## Putting Claude behind the hardest work

Atlassian put Claude behind the workloads where the cost of a wrong answer is highest. For its reasoning tiers, Claude stood out for consistent instruction-following, strong long-context handling, and dependable tool orchestration.

"We prioritize reliability in enterprise workflows,” Mansour said. “The Claude models are better at following complex instructions consistently and handling larger amounts of context without losing important details, especially where quality and trust matter a lot."

That work shows up first in Rovo Chat, the in-app assistant that helps customers move work forward inside Jira, Confluence, and the rest of the suite. Rovo Chat serves millions of users with Claude as one of its models, choosing the right tools and skills from among the thousands Atlassian has exposed. Claude also powers Rovo CLI, Atlassian's primary developer AI experience, and is also behind Rovo Max—a mode of Chat in early access—that takes a goal rather than a task and works until it reaches it. To do that, Rovo Max draws on Teamwork Graph, Atlassian's connected map of the billions of objects that span a customer's apps, and runs inside a managed environment where admins control its packages and network access. Many of Atlassian's customers are also software and IT teams, and Claude handles their code review and code generation, work that often calls for reading across large repositories. Some go further and hand a Jira ticket straight to a Claude-powered agent that picks up the work and carries it out.

Inside Atlassian, the same kind of work runs on Claude Code. It's used heavily across engineering, and a recent pilot extended it to non-technical teams, where product managers and designers used it to prototype, commit small code changes, and build custom internal apps.

## An open platform, built on Google Cloud

Claude runs on the internal AI platform Atlassian built to serve models across its products. At its center sits an AI model gateway built on Gemini Enterprise Agent Platform (formerly Vertex AI) as the primary routing path, managing and interconnecting AI workloads across providers. Atlassian scales that framework on Google Kubernetes Engine alongside Google Cloud's GPUs and TPUs. "In the world of AI, you cannot use one tool for everything," Mansour said. "Working with Google Cloud and Anthropic gives us the ultimate enterprise toolbox to automatically route the right workload to the right model at the perfect time." When a team builds a new capability, it writes its own evaluations, benchmarks models on quality and cost, and deploys whichever performs best.

Atlassian moved the platform behind its high-volume custom agents to Google's Gemini Flash family. "We have significantly reduced operational costs for our customers running continuous AI workflows on our platform," Mansour explained. "By using Gemini and Claude through Google Cloud, we hit a rare trifecta: costs dropped, quality improved, and latency remained optimized." Gemini Flash is now the default for those general-purpose customer agents, while Claude carries the complex, long-running work. When vendors retire models, the team swaps in newer ones without re-architecting. "A long-term roadmap in the world of AI is probably no more than three months these days," Mansour said. "What's most important for all organizations is how do you have your teams empowered with a set of tools to respond to change quickly."

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## Millions of agents, and one that made its own video

More than 5 million agents ran in customer business workflows in a single month, a figure that keeps climbing as customers drop agents into more loops across their workflows. Claude drives the most complex of those experiences.

What that looks like in practice came through in an internal Rovo Max demo. Someone handed the agent a Jira board and asked it to "create me an Instagram reel" for everything the team had shipped. It had no access to Instagram and no built-in way to make a video. The agent read the board, used Teamwork Graph to follow the linked context, and pulled in connected Figma designs and Google Docs. It found libraries to generate video, wrote its own script, and produced a reel with the right announcements, stopping only where it needed an Instagram account, which a human provided. “All of that is powered by Claude," Mansour said.

Where Atlassian takes this next rests on two problems it wants to keep solving for customers: their workflows and their context. The workflows already exist. "Our customers run billions, with a B, of workflows in Jira and Confluence," Mansour said, and the opportunity is finding the steps inside them where an agent can deflect a ticket, surface a lead, or cut the time a task takes. Context is the more durable problem, and the one Teamwork Graph is built to solve. "If you assume that every customer, including ourselves, has access to more and more intelligence every year, and the cost also drops at the same time, then what is the most sustainable differentiation any company can have?" Mansour asked. "It's just the context. It sounds like an abstract term, but the context is really just the knowledge they have everywhere."

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude


### How Notion ships and scales agents with Claude Managed Agents

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
