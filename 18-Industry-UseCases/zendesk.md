---
title: "Zendesk Claude and AWS case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/zendesk"
category: "18-Industry-UseCases"
fetched_at: "2026-10-10T06:26:04Z"
tags: ["agents", "case-studies", "enterprise", "security"]
---

# Zendesk built custom agents on Claude and reached 1 million agent executions in 7 weeks

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
[Claude Platform](https://claude.com/platform/api)

Partner:  
AWS

Location:  
North America

1 million custom agent executions

in the first seven weeks of early access

Up to 80% reduction

in human handle times for customers running custom agents

Zendesk, which provides AI for customer and employee service, built a way for its customers to create their own AI agents for the parts of their service work that are specific to their business. The agents run on Claude, and they ran 1 million times in their first seven weeks of early access.

## With Claude, Zendesk:

- Built its custom agent builder with a five-person team, working with Claude Code and the Claude Agent SDK, going from proof of concept to early access in four months
- Went from zero to 1 million custom agent executions within seven weeks of early access
- Helped one customer that handles more than 14 million service requests a year automate duplicate merging at 99% accuracy in its pilot
- Raised automated resolution by up to 10% while cutting human handle times by up to 80% for customers running custom agents
- Runs Claude through Amazon Bedrock, inside the AWS environment and hosting regions it already operates

## The challenge

## The work that stayed manual

Zendesk already helps companies automate a large share of their customer requests with AI. The harder part is the work that happens between a customer’s first message and the final outcome, like exceptions to a return policy, complicated warranty claims, or detailed billing questions.

Smaller companies handled that work with people, one request at a time. Larger ones with AI teams built one-off automations, which took a lot of engineering time and only covered the easiest cases. “Every customer is so unique to what they do,” said Abhinay Kathuria, Director of AI/ML at Zendesk. “There’s a lot that happens behind-the-scenes, and a lot of this was being handled manually.”  

## The solution

## Powering custom agents with Claude Sonnet

Kathuria’s team tested models from Anthropic and other providers on the testing system they use across Zendesk products. It scores each model on 15 metrics using agents like the ones customers actually write, and the team runs it again whenever a new model comes out. Because these agents act on real customer requests, getting the answer right matters a lot.

Zendesk chose Claude Sonnet 4.6. Sonnet did “exceedingly well” on pilot tasks like reading PDFs, and in Zendesk’s testing, it needed fewer steps to reach a decision. “A competitor model might come to the same conclusion, but it might take four or five planning turns to get there,” Kathuria said. “Sonnet could handle a lot of those in one shot.”

Kathuria now makes the same argument to Zendesk customers. “You can’t just look at token price in isolation,” he said. “You have to look at the cost per task.”

Where Claude runs came down to security and data locality. Zendesk already runs its infrastructure on Amazon Web Services (AWS), so it serves Claude through Amazon Bedrock. Zendesk keeps model processing in the AWS hosting regions it already uses, which helps it meet customers’ data-residency and governance requirements. Zendesk says this also means its customers don’t have to approve or manage an additional cloud subprocessor. “Our most important security benefit is that Claude runs through the AWS environment we already operate and govern,” Kathuria shares.

## Agents written in English, connected to the tools teams already have

To set up a custom agent, a Zendesk customer writes instructions in plain English, then connects the agent to Zendesk actions and outside tools like Jira and Google Drive in a few clicks. It takes about 30 minutes to set up something that used to take months of engineering work.

Take incident triage. When a lot of similar tickets come in at once, the agent notices, files a Jira issue, posts in Slack to let engineers know, and tells the affected customers the problem is being worked on. Once the fix ships, it closes all the related tickets and adds a note explaining what went wrong.

Zendesk is also building a router to send each task to the right place. Simple requests, like working out what a customer is asking for, take one call to Sonnet. Harder ones go through a longer process where the agent plans its steps before acting. After each run, the agent reviews its own work and saves what it learned as a skill it can use next time.

Customers decide which actions each agent is allowed to take. Zendesk is also shipping ways to watch and test agents, including a log of every tool call, simulated conversations, and A/B testing. “Our customers are asking for exactly the same things we need internally,” Kathuria said. “A lot more agent observability, and how to test these agents in production.”

## The outcome

## 1 million agent executions in seven weeks

In the first seven weeks of early access, custom agents ran 1 million times. General availability is planned for Zendesk's AI Summit in November and several large customers are getting ready to move much more volume onto them. “We have four or five customers who are going to run 20 million tickets through these agents powered by Claude every year,” Kathuria said.

Across customers running custom agents, automated resolution has gone up by as much as 10%. Zendesk calls its long-term goal an Autonomous Service Workforce, where AI handles 80% or more of customer and employee requests and people handle the rest with help from AI. Next, it plans to offer more specialized agents built for specific industries and types of work.

“The era of generic, one-size-fits-all AI agents is over. The best agents are specialists: deeply grounded in the work, the industry, and the business they serve,” said Shashi Upadhyay, President of Product, Engineering and AI at Zendesk. “Our custom agents powered by Claude are taking on more complex work, earning trust, and driving more measurable impact for our customers.”

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
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

- [Overview](../17-Billing-Plans/pricing-enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial advisors](financial-advisors.md)
- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

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

- [Overview](https://www.claude.com/resources)
- [Articles](https://www.claude.com/resources/articles)
- [Webinars](https://www.claude.com/resources/webinars)
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
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
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

- [Overview](../17-Billing-Plans/pricing-enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial advisors](financial-advisors.md)
- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

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

- [Overview](https://www.claude.com/resources)
- [Articles](https://www.claude.com/resources/articles)
- [Webinars](https://www.claude.com/resources/webinars)
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
