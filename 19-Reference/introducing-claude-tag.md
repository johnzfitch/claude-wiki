---
title: "Introducing Claude Tag \\ Anthropic"
source_url: "https://www.anthropic.com/news/introducing-claude-tag"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:35Z"
tags: ["news-research"]
---

# Introducing Claude Tag

Jun 23, 2026

Claude Tag is a new way for teams to work with Claude.

We’re starting on Slack, which Claude can join as a team member. Grant Claude access to selected channels, and connect it to whichever tools, data—and even codebases—you choose. Then, anyone in the channel can tag **@Claude** in, and delegate tasks to it while they focus on other work. Claude builds context by remembering relevant information from the channels it’s in, and can plan out tasks to complete in the future.

We see Claude Tag as the beginning of an evolution of Claude Code: it makes the model even more proactive, and it works better with a full team. Tagging **@Claude** is now one of the main ways we get things done at Anthropic. Today, 65% of our product team’s code is created by our internal version of Claude Tag. The same pattern is now spreading well beyond engineering—we’re tagging Claude to chase down product metrics and data, work through support tickets, or even help find the root cause of tricky bugs.

We’re launching [Claude Tag on Slack](../14-Connectors/claude-for-slack.md), since it’s a natural home for collaborative work between teams and AI, and where much of Anthropic’s day-to-day work already happens. It’s available today in beta for Claude Enterprise and Team customers. Our goal is to expand where it’s available more widely, so that teams can tag @Claude in the many other places they work.

## Working with @Claude

If you’ve worked with Claude Code or Cowork before, Claude Tag will feel familiar. Tag @Claude with a request in simple terms and it’ll break its task down into stages and then work through them in turn, using the tools it has access to. Once it’s done, it’ll respond in a Slack thread with what it’s created.

But tagging Claude comes with a few new advantages:

**@Claude is multiplayer.** Within a given Slack channel, there’s one Claude that interacts with everyone. This means that anyone can see what it’s working on, and can pick up the conversation from where the last person left off. This makes tagging Claude very different from working within a single chat or for a single task—it’s much more like interacting collaboratively with a teammate.

**@Claude learns over time.** As Claude follows along with its channel, it builds more context about the work. This means that users don’t need to explain things to it from scratch over and over again. And Claude can even automatically learn from *other* Slack channels and data sources, if it’s granted permission. (It doesn’t report from private channels.) This gives it the tacit knowledge necessary for it to provide the best possible work.

**@Claude takes initiative.** If “ambient” behavior is enabled, Claude will proactively keep you updated about whatever it thinks you might need to know. It’ll flag relevant information from across the channels it’s in and the tools it’s connected to, and follow up on threads or tasks that have gone quiet without being resolved.

**@Claude works asynchronously.** Set Claude a task, and you can focus on your other priorities while it works. It can also schedule tasks for itself, pursuing a project autonomously over hours or days. We’ve found this particularly helpful at Anthropic: we now spend much more of our time delegating tasks to many Claudes in parallel.

You can also send Claude direct messages: it’ll respond privately, using the personal tools and connectors you’ve set up.

## Getting started

We’ve designed Claude Tag with teams and organizations in mind: @Claude’s access to sensitive data and task-specific tools can be very tightly controlled.

To get up and running, system administrators specify which tools and information the model should have access to, in which channels. Think of it as creating separate Claude identities for different uses: everything, including its memories, will stay scoped to the channels defined by the administrators. For example, a model set up for sales work won’t pass on memories to one set up for engineering; nor will it give engineers access to any sales data or tools. More information about provisioning access is [available here](https://claude.com/blog/agent-identity-access-model).

Once permissions are set, everyone can begin tagging right away. Administrators can set limits for token spend (both for the organization and for individual channels), and can view a log of everything that @Claude has done, along with who requested each task.

If you’re a Claude Enterprise or Team customer, you have access to Claude Tag in beta starting today. To get started, [visit here](http://claude.ai/redirect/website.v1.d49719c7-4833-4b64-a449-b5c02ac4e9f1/admin-settings/claude-in-slack) and follow these four steps:

1.  Pair Claude Tag with your Slack workspace
2.  Give Claude access to your tools
3.  Set a limit on your organization’s monthly spend
4.  Test Claude in a private channel to confirm it works.

Claude Tag replaces the existing [Claude in Slack](https://www.anthropic.com/14-Connectors/get-started-with-claude-in-slack-ad4d7e43e7.md) app. To migrate, administrators can opt in within 30 days. We’re issuing an introductory [launch credit](../13-Enterprise-Admin/claude-tag-launch-promo-for-claude-team-and-enterprise.md) to eligible Enterprise and Team organizations so that the whole company can try it out.

Claude Tag works with Opus 4.8. You can [read our docs](https://www.claude.com/docs/claude-tag/overview) and [product page](../14-Connectors/claude-for-slack.md).


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](investigating-incidents-cybersecurity-evals.md)

### Our position on open-weights models

[Read more](position-open-weights-models.md)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](cognizant-anthropic.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://www.anthropic.com/learn)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
