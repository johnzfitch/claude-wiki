---
title: "Supermetrics: manage ad campaigns in a Claude conversation | Claude by Anthropic"
source_url: "https://www.claude.com/customers/supermetrics"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:47Z"
tags: ["case-studies", "enterprise", "security"]
---

# Supermetrics lets marketers manage ad campaigns from a conversation with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
Europe

250% average month-over-month growth in active users

since Supermetrics' Claude connector launched in February

10-hour reports done in 20 minutes

when agency customer Layer runs client reporting through the connector

Answering a marketing question once meant exporting data from a half-dozen platforms and rebuilding the report by hand. Now a marketer can ask Claude why a campaign underperformed and get an answer pulled live from their ad and analytics platforms. With approval, Claude can then pause or adjust the campaign in the same conversation. [Supermetrics](https://supermetrics.com/) builds the infrastructure behind that answer, for more than 200,000 businesses.

## With Claude, Supermetrics:

- Grew active users of its Claude connector 250% month over month on average since its February launch
- Turned one agency customer's 10-hour client reports into 20-minute tasks through the connector
- Recorded zero hallucinations in that agency's multi-week validation of live marketing data
- Runs campaign creation and edits across Google Ads, Meta, Microsoft Advertising, TikTok, Linkedin and Snapchat with human approval before anything goes live
- Serves normalized data from hundreds of marketing sources, with source and timestamp attached to every figure
- Uses Claude company-wide, with Claude Code as the engineering default and Cowork for internal workflows, reporting, and research

## The challenge

## The questions dashboards can't answer

Supermetrics customers had no shortage of dashboards. "Dashboards are fixed: they answer the questions their designer anticipated, and nothing else," said Mikael Thuneberg, Founder and co-CEO of Supermetrics. Anything a dashboard didn't anticipate meant waiting on a technical colleague, or doing the export-and-reconcile work by hand. Layer, a 25-person Norwegian agency and Supermetrics customer, quoted a client 10 hours of billable work for one report that pulled from five different sources. AI assistants could have closed that gap for Layer, but a wrong number in a client report is expensive: someone spends real budget on it. That risk kept many agency teams from trusting AI with client-facing work.

## The solution

## Matching how marketers work

Because of that risk, Supermetrics put accuracy and consistency first in every round of model testing. The company shipped its MCP server across the major AI assistants, and it invested most heavily in Claude, where the experience matched how marketers work. Claude Cowork renders charts inline in conversation, so a marketer can read a report instead of parsing raw numbers, and Claude’s connector marketplace was far enough along for the team to build on with confidence. Supermetrics accesses Claude Sonnet 5 and Opus 5 through Google Cloud’s Agent Platform, and holds zero-retention agreements with its model and cloud providers.

The company held itself to the same standard first, testing Claude on its hardest internal problems. The hardest of those was its own monolith, years of accumulated code for realtime data crunching. "We can now use Claude against a very custom monolith with a fair amount of accuracy,” explained Duleepa Wijayawardhana, Supermetrics’ CTO. “Claude reasons over a sprawling code base where a small change in one part might have unexpected effects elsewhere."This is good for our customers and the sanity of our product team."

For the engineering team, Claude is also the first call during an incident, combing metadata and logs to find what broke and where. Elsewhere in the company, teams use Cowork for reporting and research. "If we're asking marketers to trust AI with their decisions, we have to prove we trust it with ours first," said Duleepa.

## From answers to actions, with a human in the loop

For customers, a marketer asks a question, Claude calls the relevant Supermetrics tools, and the server returns normalized data with a source, timestamp, and transformation logic. Claude reasons over the answers and recommends what to do next. "Combine our understanding of marketing with our clean data, and Claude went from being a passable marketing intern to a full-blown marketing data assistant," noted Mikael.

Where most data platforms stop at reading campaign data, Supermetrics also built write actions. Marketers can now create and edit campaigns on Google Ads, Meta, Microsoft Advertising, TikTok, Linkedin and Snapchat by having a conversation with Claude.

Importantly, the guardrails were designed up front rather than patched in after testing. "The system should never take an action that could surprise the user," Mikael added. "Campaigns get created in a paused state, not live, so nothing goes to market without a human actively choosing." Customers can set approval levels per account, and an approval page lays out each change rules for stakeholders to approve or reject.

## The outcome

## 250% growth month-over-month

Since its February launch, Supermetrics' Claude connector has averaged 250% month-over-month growth in active users. "Our Claude product has gained popularity faster than anything we've launched before," noted Mikael.

Before rolling the integration out to clients, Layer's Morten Kleven, a digital marketing strategist, spent weeks validating Claude's output. "When using AI for client reporting, trust is everything," said Kleven. "I have not found a single hallucination or incorrect data point." With that confidence, client reports that took 10 hours of manual spreadsheet work now take 20 minutes, and 17 of those minutes go into dropping the finished data into the client's Google Sheet. Annual media plans, once too time-consuming to build thoroughly, are now standard practice: Claude pulls historical cross-channel results directly into Layer's templates.

Supermetrics sees the same shift across its customer base: daily pacing checks arrive in Slack instead of marketing or data teams facing a monthly scramble, and anomaly alerts catch a click-through drop before a client asks. Teams that optimized weekly now optimize daily, freeing time for strategy and creative work. Solo marketers and small teams, who never had a data specialist to turn to, get the same capabilities as everyone else. Retention and expansion have followed, and customers now consistently ask Supermetrics how and where else they can take advantage of these capabilities.

Their recent product release Supermetrics Studio turns the same analysis into something clients can share and edit. Next, their customers will also have the ability to monitor performance across every channel, form recommendations, and act within guardrails that the marketer sets, rather than Claude waiting to be asked. "That's the expansion from insight to action we've been building toward," Mikael explained.

## Related stories


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


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
