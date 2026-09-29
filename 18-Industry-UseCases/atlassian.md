---
title: "Atlassian Claude and Google Cloud case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/atlassian"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:24Z"
tags: ["agents", "case-studies", "enterprise", "security"]
---

# How Atlassian builds AI agents teams can trust with Claude and Google Cloud

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

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

[Read more](../04-API-Reference/Other/partners-google-cloud.md)

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
