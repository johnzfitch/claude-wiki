---
title: "Smartsheet Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/smartsheet"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:48Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# Smartsheet builds conversational AI into work management with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)[Claude Enterprise](enterprise.md)

Partner:  
AWS

Location:  
North America

1.76 million MCP tool calls

in the first 30 days of launching the Smartsheet connector for Claude

31% more pull requests merged by engineers

than peers on the same teams

[Smartsheet](https://www.smartsheet.com/) is a work management platform used by more than 120,000 organizations, including over 85% of the Fortune 500 work in Smartsheet. In early 2026, the company deployed Claude across three surfaces: a conversational AI layer for customers, Claude Code for its engineering team, and Claude Enterprise for every employee.

## With Claude, Smartsheet achieved:

- 1.76 million tool calls in the first 30 days to the Smartsheet MCP Connector for Claude, with 1,400+ organizations utilizing the new integration during that time.
- 500+ engineers using Claude Code ship 3x more code and merge 31% more pull requests than peers on the same teams
- 49% of employees actively using Claude Enterprise within 2.5 weeks of the company-wide launch
- 48% of MCP connector usage goes beyond asking questions: users create new sheets, update rows, and flag risks through conversation, not just query existing data
- 30% of IT helpdesk tickets are now handled automatically by Claude-powered agents, reducing the ticket queue for the support team
- 60% operational cost reduction through prompt caching across the API integration

## The challenge

## Bringing conversational AI to 120,000 organizations

Smartsheet's customers run business critical projects on its platform and need to extract insights from their data, while ensuring that governance, auditability, and security of that data persist. Many enterprises operate across multiple systems, data warehouses, and project repositories, creating silos that make a unified view of work difficult to achieve.

“Here's the thing most companies get wrong about AI adoption: they think it's a tools problem,” said Drew Garner, SVP of AI & Data Platform at Smartsheet. “It's not. It's a knowledge problem."

Inside the company, the engineering team faced its own version of the same challenge: existing AI coding tools stopped at line-level code completion, and data sat fragmented across Snowflake, service databases, and internal APIs. Any AI deployment, whether customer-facing or internal, would need to work across those boundaries.

"You have to change your culture to be OK with letting the tool write code for you, and then go further: teaching it your team's patterns so it gets better at the team and org level, not just individually," Garner said.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The solution

## Selecting Claude for conversational quality

Smartsheet evaluates models individually for each use case. For the customer-facing surfaces, Claude won. The team tested multiple providers and found Claude's output quality strongest for the conversational, action-oriented work their product required. Claude Sonnet now powers both new AI features within Smartsheet and the Smartsheet MCP Connector.

“When we made the decision to deploy AI company-wide, the question wasn’t just which model performed best. It was whether we could govern it the way we govern everything else,” said Ravi Soin, Chief Information & Security Officer. “Routing through Amazon Bedrock meant Claude inherited our existing controls: auditability, data residency, and the access policy as code our enterprise customers already rely on. That’s what made a company-wide rollout something we could stand behind.”

The same infrastructure gives the team full visibility into how AI is being used, connecting token consumption directly to engineering output.

"We didn't just deploy an AI tool,” Garner explained. “We built dedicated reporting that links token usage to code written, PRs merged, and code deployed—the full cycle. That's how we surface what patterns are working and share them across the org."

## Claude across the product, codebase, and company

The Smartsheet MCP Connector for Claude lets users view, create, and manage their Smartsheet work directly from a Claude conversation. Launched in March 2026, it reached 1,400+ organizations within the first 30 days. The connector supports 36+ operations, and users discovered 27 distinct capabilities with zero documentation or training, finding them through natural conversation alone. The signal that stood out to the team: 48% of all connector usage went beyond querying data. Users were not just asking questions about their work. They were creating sheets, updating rows, and flagging risks through Claude. "That's not chat," Garner said. "That's execution."

Inside engineering, Claude Code became central to what Garner described as "a mental model shift from writing code to directing an AI team." The team built a 9-agent SDLC template covering architecture planning, implementation, code review, merge request processing, and accessibility remediation.

"The best thing about Claude Code is that it works the way engineers already think,” Garner noted. "Engineers picked that up organically, which tells you the tool design is right."

Code documentation that previously took two weeks now takes four hours. The team built an AWS cost management analysis tool in 30 minutes that is projected to save hundreds of thousands of dollars annually.

Claude Enterprise launched company-wide on the same day as Smartsheet's fiscal year kickoff, with 272 employees completing training on Day 1. Within 2.5 weeks, 49% of the employee base was actively using the platform. Use cases emerged across functions: a technical account manager built a predictive churn scoring pipeline connecting Snowflake health data to Smartsheet, sales teams scaled personalized outreach, and routine IT requests are now handled by Claude-powered agents, reducing helpdesk volume by 30%.

"Once a few early adopters started shipping at 5x their previous rate, demand pulled itself," said Soin. "This stopped being an individual productivity story. It's a team-level and now a customer-facing capability.”

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The outcome

## 3x more code shipped

Across engineering, Claude Code users ship 3x more code and merge 31% more pull requests than peers on the same teams. The highest-performing engineers reach 5 to 7x their previous output. Cycle time across the org dropped 28%.

On the API side, prompt caching reduced operational costs by 60% and improved response latency by 20%, with cache hit rates reaching 70% overall and 90% on follow-up queries.

One unexpected use case surfaced on its own: Smartsheet's corporate social responsibility team used the MCP connector to evaluate 3,200+ nonprofit applications in under an hour, a use case nobody had planned for that appeared within days of the connector's early access launch.

## Looking ahead

Smartsheet is expanding its MCP server toward parity with what users can do inside the product, and growing its internal connector ecosystem from five to more than 20. The engineering team continues to deepen agent-first workflows across 52 teams. "Most AI integrations start from zero every time. Ours doesn't," Garner said. "Smartsheet is where our customers' business logic, project structures, and institutional knowledge already live. When you connect Claude to that, the AI already knows your business."

Soin added: “The endgame is simple: every corporate system, reachable through Claude. MCP is how we get there."

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
