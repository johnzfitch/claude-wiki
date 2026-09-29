---
title: "Supermetrics: manage ad campaigns in a Claude conversation | Claude by Anthropic"
source_url: "https://www.claude.com/customers/supermetrics"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:47Z"
tags: ["enterprise", "security"]
---

# Supermetrics lets marketers manage ad campaigns from a conversation with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Cowork](https://claude.com/product/cowork)[Claude Code](https://claude.com/product/claude-code)

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
