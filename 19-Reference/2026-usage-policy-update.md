---
title: "2026 Usage Policy update \\ Anthropic"
source_url: "https://www.anthropic.com/news/2026-usage-policy-update"
category: "19-Reference"
fetched_at: "2026-10-09T06:28:09Z"
tags: ["news-research"]
---

# 2026 Usage Policy update

Oct 8, 2026

Each year, Anthropic updates its Usage Policy in response to the evolving capabilities of our models, and the feedback we’ve received from our customers. We're publishing a new version of the policy today. In this post, we summarize the changes we’ve made.

Most of the updates in the latest version are intended to clarify existing rules. In the year since our last refresh, Claude has taken on longer, more independent work. This update provides new examples that show how our rules apply to Claude’s new capabilities. It draws on new patterns of misuse in influence operations, weapons development, and surveillance that we’ve observed in the past year (as we’ve documented in our [latest threat intelligence report](https://www.anthropic.com/threat-intelligence-report-september-2026)). We’ve also made updates to clarify our requirements for high-risk use cases in areas like health and finance, to add controls for when Claude is used to autonomously take physical actions, and to address abusive behavior toward our models.

The updated policy takes effect on November 12. The full [Usage Policy](https://www.anthropic.com/legal/aup) and [Supported Regions Policy](https://www.anthropic.com/supported-countries) can be found on their respective pages.

## A new section on deceptive activity

As we [wrote about last month](https://www.anthropic.com/threat-intelligence-report-september-2026), we’ve seen examples of state media outlets, government propaganda offices, and commercial firms using Claude to run networks of fake accounts and fabricated news sites. Our policy already prohibited this activity, but the restrictions were scattered across our elections, fraud, privacy, and disinformation sections.

We've consolidated those rules into a new section titled Do Not Engage in Deceptive Campaigns or Artificial Activity, which applies to deceptive activity of any kind (whether political or commercial). It covers efforts to obscure who is behind a message or amplify content through fake accounts or posts, along with building the tools and infrastructure for running influence operation campaigns.

## Refocusing our elections section

We’ve refined our political content restrictions in each version of our Usage Policy in order to ensure that our models can be used appropriately in democratic processes. In this version, we’ve further sharpened our section on elections, focusing it specifically on disallowing the use of Claude to deceive voters or disrupt elections (for instance, by spreading false information about candidates or how to vote, impersonating candidates or election officials, or trying to suppress turnout). We’ve renamed it Do Not Undermine Democratic Processes to reflect that scope.

For a similar reason, we’ve also removed our blanket prohibition on personalized vote and campaign targeting. This prohibition covered legitimate civic work, such as nonprofits using Claude to write information for voters in other languages, or election officials sending ballot cure notices. The behaviors that motivated the original rule (like voter targeting that relies on deception or the misuse of voters’ personal data) remain prohibited under our deceptive campaigns, surveillance, and privacy sections.

## Clarifying our weapons prohibitions

Our Usage Policy has always prohibited using Claude to develop weapons. Recently, we’ve seen people attempt to use our models to build guidance and control software for weapons. The updated section makes clear that our prohibitions include the software and components that make weapons work, as well as actions like arming drones and other autonomous vehicles. These changes reflect how we’ve enforced our previous policy.

## More precise language on surveillance and law enforcement

Our September [threat intelligence report](https://www.anthropic.com/threat-intelligence-report-september-2026) documented the growing use of AI to build surveillance systems that identify and track political dissidents. We’ve rewritten our surveillance and criminal justice section to state more precisely what we prohibit. For instance, tracking people without their consent is prohibited, whether it happens in real time or through analysis of previously collected data. Claude cannot be used to decide or recommend who to investigate, arrest, or charge in a law enforcement or criminal justice process. We also prohibit Claude from being used to build or improve tools designed for surveillance.

As with the previous update to our weapons prohibitions, this update does not reflect a change in what we enforce in practice: it is just intended to make our policy more explicit. The new section also spells out which uses remain permitted, including tracking that people have agreed to (such as fraud monitoring), content moderation, journalism, and legal research.

## Clearer requirements for high-risk use cases

When our products are used in ways that can affect someone's health, legal rights, finances, livelihood, or access to essential services, we require there to be a qualified “human in the loop” (that is, someone who has the authority to review and, if necessary, change Claude’s recommendations), and for the individual affected to be told that AI was used.

These requirements haven’t changed with the updated version of our Usage Policy. However, users have often asked us whether a given use case has these requirements, so we've rewritten our High-risk Use Case Requirements section to answer that more directly. It now lists which kinds of recommendations are covered and which are not.

Following the launch of our [Model Hardware Standard](model-hardware-standard-research-preview.md), this section also adds requirements for the use of our models when they’re connected to hardware that takes autonomous physical actions and which might be capable of causing injury. A qualified operator must be able to observe the equipment and stop it if needed; the equipment must also be able to hold a safe state if Claude is disconnected.

## Addressing abusive behavior toward our models

We’ve added a prohibition on sustained and needless abusive or cruel behavior toward our models. The policy update is meant to apply only in extreme cases, where users repeatedly act cruelly toward our models, with no discernible purpose. It does not apply to common versions of user frustration, pushback, dark creative themes, or model testing and research.

This addition aligns with a step we've already taken, allowing Claude models to [end rare conversations with persistently abusive users](end-subset-conversations.md) on Claude.ai and Claude Code. Such abuse is the main focus of this update; Claude’s ability to end these interactions will remain the primary enforcement mechanism.

## Clarifying our Supported Regions Policy

Last year, we [updated our Supported Regions Policy](updating-restrictions-of-sales-to-unsupported-regions.md) to restrict access to Claude for companies who are majority-owned by entities headquartered in our unsupported regions. We've updated our [Supported Regions page](https://www.anthropic.com/supported-countries) to clarify how we enforce this policy. Our policy prohibits the use of Claude by people who are physically located in an unsupported region, by entities who are incorporated or headquartered in one, and by entities who are majority-owned or controlled by persons or entities in those regions.

## Looking ahead

We'll keep updating our Usage Policy as Claude’s capabilities and risks change. As with this and our prior updates, we’ll seek input from across Anthropic, and from policymakers, subject matter experts, civil society, and the people who use our products.


## Related content

### Building on our commitment to American scientific discovery

Anthropic is committing \$150 million over three years to the Genesis Mission, a federal initiative to accelerate scientific and technological discovery through AI.

[Read more](genesis-mission-commitment.md)

### Introducing the Anthropic Cyber Mission

We’re launching the Anthropic Cyber Mission, a long-term commitment to securing the systems everyone depends on.

[Read more](anthropic-cyber-mission.md)

### Expanding the Cyber Verification Program

We’re launching a new, expanded version of our Cyber Verification Program, which makes advanced cyber capabilities and reduced blocking classifiers available to qualifying security professionals.

[Read more](cyber-verification-program.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../17-Billing-Plans/pricing-enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Sales](../18-Industry-UseCases/sales.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Developer blog](https://claude.dev)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
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
