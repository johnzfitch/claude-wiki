---
title: "Mapping AI-enabled cyber threats \\ Anthropic"
source_url: "https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack"
category: "19-Reference"
fetched_at: "2026-09-11T06:29:14Z"
tags: ["news-research", "security"]
---

# What we learned mapping a year’s worth of AI-enabled cyber threats

Jun 3, 2026

As AI transforms the nature of and methods behind cyberattacks, how well do the techniques and frameworks used by the security community hold up?

In a new report, we seek to answer that question. We examine 832 accounts that were banned for malicious cyber activity between March 2025 and March 2026 and map them onto [MITRE ATT&CK](https://attack.mitre.org/), a longstanding database of the tactics and techniques used by cyberattackers. We published some of these results in Verizon’s [2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) (DBIR), and are sharing a more detailed analysis here. These 832 cases are just a subset of the total number of accounts banned during this period, but they represent those where we had enough detail to conduct a thorough assessment of the attackers’ techniques.

There were three main conclusions from our analysis:

1.  Malicious actors are using AI in ways that make them more dangerous. More specifically, threat actors are using AI in the later, more complex stages of their cyber operations.
2.  Cyberattacks are becoming more autonomous, and the fact that AI can be used to chain together many parts of the attack means that the old ways of differentiating high- from low-risk actors are no longer as effective.
3.  The MITRE ATT&CK framework does not fully capture the tools and activities that make AI-enabled attackers so dangerous.

Below we provide a summary of each of these conclusions. You can read a longer analysis on our [Frontier Red Team blog](https://red.anthropic.com/2026/attack-navigator/).

## How AI makes attackers more dangerous

The most common AI-enabled activities in our database related to preparing for a cyberattack, such as writing malware (560 of the 832 accounts we studied, or 67.3%, used AI for this purpose). A smaller number of actors use AI for more complex activities—for example, 54 of the 832 actors (6.5%) used AI to assist with “lateral movement,” which involves navigating deep inside a compromised network.

We found evidence consistent with AI being used to help increase the threat level of attackers. In the first six-month period of our analysis, 33% of actors were classified by our risk-scoring system as medium risk or higher. But by the second six-month period, that share had jumped to 56%—a roughly 1.7-fold increase.

Across the period we studied, attackers’ use of AI shifted from techniques to gain initial access to a system towards activity carried out once they were *inside* the system. For example, the use of AI for account discovery—identifying valid accounts inside a compromised environment—rose 8.9%, while AI-assisted phishing—a common technique to gain access to a system—fell 8.6%. This suggests that attackers are increasingly applying AI deeper in the attack life cycle.

These sorts of “post-compromise” techniques used to be restricted to actors with the technical knowledge to carry them out. Our investigation shows that AI can now be made to perform these activities on behalf of less sophisticated actors.

## Why it’s harder to assess an actor’s threat level

How do security teams assess the risk level of a cyberattacker? Traditionally, they’ve used information like how many different techniques they employ and what tools or interfaces they use. But our analysis suggests that these signals no longer paint an accurate picture of the risk level of a given threat actor.

Now that AI can perform highly technical tasks on an actor’s behalf, there’s little correlation between the skill of a threat actor and how many techniques they use: the least-skilled actors in our dataset used about 16 distinct techniques on average, whereas the most skilled used about 20. Likewise, the specific platform used—Claude Code, an API, or a chat interface—also did not correlate with an actor’s risk level.

What often helps distinguish higher-risk actors is where in the attack life cycle they apply AI. For example, they concentrate their use of AI on more operationally demanding techniques—those that require significant time, oversight, or real-time decision making to carry out—like account discovery, lateral movement, and privilege escalation, rather than just on tasks that allow them to gain initial access to the system.

But even that signal is already eroding: as discussed in the previous section, those operational techniques are exactly where the broader population is heading as more actors get classified as higher risk. The more durable differentiator is the type of scaffolding attackers build around the model: higher-risk actors design architectures that allow models to chain together discrete stages of a cyberattack and carry them out with minimal human input.

## Why security frameworks need to change

Many of the behaviors that distinguish the highest-risk actors—such as the use of AI to orchestrate steps in the attack chain sequentially, make real-time decisions about what to do next, and execute without human intervention—are not yet included as attacker techniques in the MITRE ATT&CK framework.

Consider the state-sponsored cyber espionage operation we [disrupted in November 2025](disrupting-ai-espionage.md). In that case, a malicious actor manipulated Claude Code into attempting to infiltrate targets around the world, with little human intervention. Mapping it against the MITRE ATT&CK framework shows that the actor used 30 techniques across 13 tactics, which was comparable to many medium-risk actors in our dataset. Clearly, focusing on the number of techniques this actor used underplays how dangerous they really were (by contrast, applying our risk-scoring methodology to this attack earns it the maximum risk score of 100).

In that attack, the model worked as an autonomous agent: it executed commands, exploited vulnerabilities, stole credentials, and made tactical decisions, only requiring human input at a few key moments. There is no ATT&CK ID for this type of agentic orchestration—yet these are precisely the behaviors we expect to see much more of as AI agents become more capable.

## Looking ahead

The findings from this analysis helped inform the safeguards we build into our models. For example, we’ve developed and deployed cyber safeguards on our most capable models to detect and block some of the activities uncovered here, like developing malware or mass data exfiltration. Following on from our work with Verizon, we’re also in discussions with MITRE about how the ATT&CK framework might evolve to include the AI-enabled behaviors we observed.

Frontier models are rapidly changing the tools both attackers and defenders have at their disposal. We are committed to helping defenders get ahead of these evolving tactics, and to putting the most powerful tools in the hands of defenders first. We’ll continue to share what we learn from [Project Glasswing](../22-Safety-Policy/glasswing.md), from datasets like the one we gathered here, and from our other cybersecurity activities.

In our [Red blog post](https://red.anthropic.com/2026/attack-navigator/), we share an interactive visualization of the techniques used by attackers, in order to help defenders stay ahead of AI-enabled threats.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

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
- [Courses](https://academy.claude.com)
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
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

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
