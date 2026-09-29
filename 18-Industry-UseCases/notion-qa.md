---
title: "Notion Q&A | Claude Managed Agents | Claude by Anthropic"
source_url: "https://www.claude.com/customers/notion-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:44Z"
tags: ["agents", "case-studies", "enterprise", "security", "skills"]
---

# How Notion ships and scales agents with Claude Managed Agents

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
Claude Managed Agents

Location:  
North America

18,000 Claude agents

created in the first three weeks

90% of agent turns triggered by automations,

not chat

Case Study: Notion

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

[Read more](notion.md)

Three weeks after launching External Agents, collaborative AI workspace [Notion](notion.md) had 18,000 agents created by customers, and 90% of agent activity running on automated triggers rather than chat. Notion built the feature on Claude Managed Agents, Anthropic's suite of composable APIs for building and deploying agents at scale. Product manager Eric Liu spoke with Anthropic about what Managed Agents handled and what's surprised him since launch.

## Anthropic: You shipped External Agents on Managed Agents recently. How are people actually using them?

**Eric Liu, Notion:** We want Notion to be the best collaboration platform for agents and teams. A key part of that mission is bringing the best agents to work natively in Notion, and Claude is at the top of that list: the number one external agent people wanted to use in Notion. So far it's about 18,000 Claude agents created, and those agents have done about 140,000 steps. We were pleasantly surprised by how quickly it ramped up, with very little marketing. A large percentage of people creating agents in Notion now create Claude agents. We're seeing strong depth of usage too. 90% of the turns people are doing with Claude are automations in Notion, triggered on a Notion page, a Slack message, or scheduled runs. It's not directly chatting with Claude; the wrapper we built around it for automations is what's resonating with our customers. Our top workspaces are really using it for multiplayer workflows: a workspace will have three or four agents running dozens of threads per day, mainly through automations.

## Anthropic: How would you explain what you’ve built with Managed Agents?

**Liu:** You’re creating these software building blocks in Notion and you can construct them into any workflow you want. For example, we created a task board that acts as an orchestrator. You create a task, move it to "ready to start," and it invokes a Claude session. Claude picks up context from connected pages, our design system, API docs, and product requirements documents. In other words, you're working with Claude just like a colleague.

The nice thing is that you're not limited to one task. Customers can kick off 30 or 40 jobs at the same time, and our platform routes them to the right person for approvals. People are automating the busy work: experiment flag cleanup, a lot of different mini tasks around triage.

## Anthropic: Why did you decide to add Managed Agents into Notion?

**Liu:** Users were asking us for Claude. Our customers don't want to use one agent to talk to another agent to do a backflip to get things connected. They just want to be in Notion and say, "Claude, help me make this website." Managed Agents was a great solution because we just pulled in the API and it worked within the product.

We focus on what's native to Notion: your company knowledge. Our agent is good at using Notion, but it's not the best at coding, and Claude models are very good at that. There's a whole world of other files that Claude is really good at generating. Underneath, all agents are basically coding agents. And that's unlocking a lot of non-coding use cases. If you're creating a presentation for marketing or sales, you're taking knowledge and generating an artifact, whether that's a PDF, slides, or something else. That synthesis of information into an artifact is roughly the same workflow that works really well in coding. We're seeing that transition into the rest of knowledge work.

## Anthropic: Teams can implement Managed Agents three ways: as Claude-branded agents in the product, as an unbranded engine behind their own agent, or as internal agents. Why did Notion go Claude-branded?

**Liu:** Our vision with Notion is to make it the command center for agents: allowing teams to use their favorite agent and use it natively within Notion. If you are a collaboration product, the idea of being able to use an agent in the product is the core user journey. The benefit of bringing in Claude is people trust the intelligence of the model and the experience.

The session streams from Managed Agents into Notion's client. But to the user, they don't know any of that is happening. All they're seeing is that Claude is writing files, writing Notion pages, updating things, commenting and doing everything that teammates and other agents can do.

## Anthropic: What did Managed Agents handle that you didn't have to build yourselves?

**Liu:** Having an infrastructure layer that can do long-running tasks was really essential. That ability to continue to run tasks, to manage memory, and to have high quality outputs over time is a layer that's super critical on top of the model itself.

The best surprise was that we didn't have to set up any of this. All of the skills, all the different packages we need, it was very easy to go and spin up.

The sandbox is really important if you want coding use cases. Part of our flow for users is the ability to connect their GitHub, and through that they can pull in their repos and then run the code. The GitHub endpoint in Managed Agents was really useful.

## Anthropic: You've said most agent tools are designed for a single person working with a single agent. What breaks when organizations try to scale that?

**Liu:** The challenge of deploying agents at scale is really about collaboration. Right now, agents feel very one-to-one. It's you and an agent in an interface. But what does it look like for your whole team, with all of the approval processes and everything required to actually use agents at scale? That's fundamentally the same problem we've solved before at Notion, which is human collaboration. Now it's agent and human collaboration, and it turns out a lot of the same patterns around suggested edits, version history, and shared knowledge bases are really critical.

## Anthropic: You've been using this yourself. What's that been like?

**Liu:** The Managed Agents product is like a playground for me. Even with the early prototype, we saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.

When I was prototyping new features for Notion using the task board workflow, I had about 30 tasks. I took all of them and just dragged them to start. I went and got a snack, came back, and all the prototypes were made. Then I tagged in somebody on my team, and we jammed on the same output together right in Notion. We've turned AI solo work into a collaborative moment. That was the point where I was like, everybody should be doing this.  
  
People now see Claude show up in their Notion task doing work, and they give a thumbs up or thumbs down. That's an interface they already understand.

## Anthropic: You've described teams deploying an army of agents: a separate Claude for each stage of work, mostly running on triggers. How do you make sure they act safely?

**Liu:** We've created a Claude agent for each stage: one that investigates, one that plans, and one that builds. What's useful about that is each agent can have its own permissions, its own contexts, and its own automations. The review agent is managed by a few people, but many people can manage the investigator agent.

Every agent that you create is locked down from a permission standpoint by default, which means it starts private. You have to share it explicitly. Then we have a bunch of different access permissions: some people will only be able to chat with it, some people can trigger it, some people can edit it. When you have 20 or 30 people working on the same shared task board, how do you make sure that at the right point, the right person is brought in? The way that we think about solving the automated workflow is also solving the permissions and collaboration problems. Those go hand in hand.

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

[Read more](https://claude.com/blog/claude-managed-agents)

## Anthropic: You preload Claude's public skills, run a skills marketplace, and let agents maintain their own skills database. Why are skills such a big part of this?

**Liu:** Claude has a lot of great skills, so we preloaded the ones that are publicly available for making PowerPoints, PDFs, and docs. Within Notion, we have a whole marketplace of skills, and we're letting folks bring in their own skills for their own Claude agent.

With skills, it's more about *how* you do something, and not so much if it can do it. It’s not about knowing how to make a PowerPoint, but more about "Hey, this is our flavor of PowerPoint. This is how we like it written."

A lot of these skills are basically auto-maintained. Once there's a merged pull request or a completed task, Claude identifies the lessons the agent can learn and feeds them back into the skills as updates. Every time you say "this is a great prototype" or "this is a great PDF," that feeds into the skills. The quality keeps improving without someone manually updating the knowledge base.

## Anthropic: How do you think Notion changes over the next six months as a result of this?

**Liu:** The interface is becoming more about human beings reviewing the work of agents. We are the translation layer to agents. We'll keep the same primitives around the page and the database, but we're going to build a lot more around version control and humans in the loop.

The question becomes: how can humans become the reviewers of agentic work rather than directly the doers? I think that paradigm applies to a lot of AI.

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
