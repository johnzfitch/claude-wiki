---
title: "Carvana Claude Tag case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/carvana"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:59Z"
tags: ["agents", "case-studies", "enterprise", "security"]
---

# Carvana turns Slack alerts into production fixes with Claude Tag

[Try Claude](https://claude.ai)

Industry:  
Retail Services

Company size:  
Large

Product:  
[Claude Tag](../14-Connectors/claude-for-slack.md)

Location:  
North America

56% fewer alerts

after Claude Tag began resolving the root causes behind them

Answers 65% faster

for the wholesale platform team's issue and alert triage

A production alert at [Carvana](https://www.carvana.com/) used to wait for an engineer. Now, Claude Tag can begin investigating as soon as the alert reaches Slack. It identifies the team that owns the affected code and posts a root-cause analysis in the team’s preferred format, all before an engineer begins manually working through the issue. Carvana, the online car retailer, had previously built two versions of this kind of Slack-based AI internally before adopting Claude Tag.

## With Claude Tag, Carvana:

- Cut alerts in its retail science channel by 56% by resolving the root causes
- Gets answers 65% faster for its wholesale platform team by checking tickets and code itself
- Automatically takes a production monitoring alert from Slack to a pull request, human review, and production
- Verifies every release against a log baseline from the hour before it shipped
- Replaced two homegrown Slackbots while giving each team its own scoped access to Carvana’s data warehouse
- Runs hourly checks that catch failing pipelines and stale feature flags and start the fixes

## The challenge

## Multiplayer AI Carvana had to maintain

Carvana wanted AI inside Slack, where entire teams could watch it work and jump in. It built that twice on its own. The first version was a homegrown agent loop: an API call wired to a few tools, sometimes looping back for a second pass. Then, about a year ago, came a second one: the Claude Agent SDK wrapped in a Slack app. Both shipped, and both did the job.

"Our internal tools demonstrated what was possible," said Alex Devkar, SVP of Engineering and Analytics at Carvana, "but maintaining them required time and resources that could be better spent running the business." A small team had to babysit the bots on top of its real work. Access controls presented a bigger challenge. The homegrown bots were limited, especially because connecting them to additional services while preserving team-specific permissions would have required significant additional work. Carvana’s wholesale platform team ultimately chose not to adopt the tools because the team was uncertain how long they would be supported, or whether another migration would soon follow.

## The solution

## Managed agents with per-team identities

When Claude Tag launched, Carvana didn’t hesitate. "Tag was an obvious next step for us," Devkar said. "It has all the might of Anthropic behind it, from hosting and authentication to the underlying infrastructure, allowing our teams to focus on applying the technology to meaningful business problems." What sold him was one feature in particular: the ability to drop a bundle, a packaged set of instructions, tools, and access scoped to one team's use case, into a single Slack channel. "Bundles are one of Claude Tag’s most valuable capabilities," he said. "They allow us to tailor the instructions, tools, and access to how each team works, making the experience both useful and scalable."

Customization made Tag easy to drop into a single channel. The way it handled access let Carvana deploy Claude Tag everywhere. Claude Tag can run under its own scoped identities, so Carvana set up one connection to its cloud data warehouse, plus separate identities that give individual teams their own slice. "Claude Tag gives us the flexibility to provide teams with access to the data they need while maintaining appropriate controls," Devkar noted. "Previously, we would have had to build and maintain those protections ourselves." The wholesale platform team now relies on Claude Tag in production. When a vehicle’s status needs to be found in an internal system, Claude Tag runs the VIN through Carvana’s data warehouse to trace where it is in the process and what state it is in.

Carvana’s internal testing group, known as the Pathfinders, has been testing Claude models since Sonnet 3.5, using them for coding and other complex, multi-step work. Claude Tag now defaults to Opus 5, which Carvana has found very well-suited to the range of tasks run through Tag. Across the company, teams use Opus, Sonnet, and Haiku based on the needs of each workflow.

Fable is also available to select power users beyond engineering. In one example, a senior attorney at Carvana used Fable to work across large transaction document sets, maintaining consistency even deep into lengthy reviews. The attorney particularly values Fable’s ability to distinguish between facts and estimates and to identify gaps in the source material rather than fill them with plausible answers. “In my work, a confident wrong answer is far worse than no answer,” the attorney said.

## From alert to merged fix

The retail science, verification, and wholesale platform teams all get initial alerts the same way: Slack. Claude Tag monitors the Slack channels where production monitoring warnings show up and automatically begins investigating. "Our teams are using Claude Tag to move from a production alert in Slack to investigation, a pull request, human review, and ultimately resolution," Devkar said.

On the retail science team, that flow runs on a standing prompt and a fixed format for root-cause write-ups. Alerts arrive already investigated: Claude Tag works out who owns the broken code, tags them, and lays out its analysis in the exact shape the team asked for. It picked that format up once, from a single prompt, and has kept to it since. Engineers now ask it to open the pull request straight from the analysis, so fixing a bug turns into one more message in the same thread.

Carvana's customer verification team wired Claude Tag into the Slack channel where software releases and errors already land. Every release gets checked against a baseline from the hour before it shipped, comparing errors, warnings, and log volume automatically, with no one asking. The comparison logic lives as a skill in the team's own repo, next to the runbooks and the notes for each alert, so knowledge that used to sit with a couple of senior engineers is now in version control and applied the same at 3 a.m. as at noon. One weekend, a strange deployment came through that the existing logs could not explain. Rather than give up, Claude Tag opened a pull request to add better logging, improving the system it was watching.

The wholesale platform team gave Claude Tag the hardest test: two weeks in its intake and alert channels. It had read-only access to the same resources an on-call engineer would typically consult, including work tickets, build history, and code. Across five cases, Claude Tag traced the initial report to its underlying cause and identified the relevant code rather than restating the symptom. In one case, it investigated an intermittent reporting gap and determined that the issue originated in a downstream service rather than the system initially suspected. It also handled work like: scoping a feature request down to a precise set of changes, catching a design trap the requester had missed, or triaging a build failure and then walking back its own first conclusion when a retry proved it wrong. Told an infrastructure outage was the likely cause of one alert, it stood down, checked that nothing bad had slipped through, and flagged the follow-up for once it cleared. Each case ended the way a careful engineer would, with a ticket filed, a pull request offered, or a fix deliberately not made. "They're letting Tag be a teammate," Devkar said.

Not every issue needs to interrupt an engineer in real time. Some teams schedule Claude Tag to check pipelines and feature flags hourly, identify problems, and initiate the appropriate follow-up. The approach costs less than continuous monitoring while helping engineers stay focused on higher-priority work, Devkar said.

## The outcome

## Alerts that stop firing

Claude Tag spread organically across Carvana. Teams shared successful investigations in open Slack channels, allowing others to see how it worked and identify additional use cases. The wholesale team that had declined to adopt the homegrown bots went all in on Claude Tag. "Once the team saw that Claude Tag had the capabilities and controls it needed, they were able to adopt with confidence," Devkar explained.

Even the migration off the old bots became a job for Claude Tag. One Pathfinder pointed it at the outgoing chatbot with a single instruction: "Watch all of the answers from that chatbot, which has skills to do the work, and pick up all the things you need to pick up in order to replace it." It spent a week or two working through the old bot's output, and the team switched over soon after.

In the retail science channel, alert volume declined 56% as Claude Tag helped teams address recurring root causes rather than repeatedly clearing the same alerts. On the wholesale platform team, Claude Tag reduced the time required to reach an answer by 65% by reviewing tickets, build history, and code that an engineer previously would have searched more manually.

The change shows up in more than the two numbers above. People filed issues before Tag, but they raise far more of them now, because they know Claude Tag will pick each one up and carry it toward a fix.

The next frontier for AI coding assistants is bigger than triage. Half a dozen teams inside Carvana are now building multiplayer flows on top of Claude Tag. "This evolution is a more collaborative environment where product managers and engineers can move from identifying a bug or proposing an idea to developing and shipping a solution together," he said. "That work can begin in the tools where teams already collaborate, without every step requiring someone to open a code editor. That's the key in a multiplayer environment."

## Related stories


### How can a Boston restaurant owner pay people what they deserve and still keep the lights on?


### Advantage Solutions gives frontline managers 70,000 hours back with Claude

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
