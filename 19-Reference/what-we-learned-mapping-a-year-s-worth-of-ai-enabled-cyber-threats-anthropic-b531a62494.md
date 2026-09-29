---
title: "Mapping AI-enabled cyber threats \\ Anthropic"
source_url: "https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack"
category: "19-Reference"
fetched_at: "2026-09-11T06:29:14Z"
tags: ["security"]
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

Consider the state-sponsored cyber espionage operation we [disrupted in November 2025](https://www.anthropic.com/news/disrupting-AI-espionage). In that case, a malicious actor manipulated Claude Code into attempting to infiltrate targets around the world, with little human intervention. Mapping it against the MITRE ATT&CK framework shows that the actor used 30 techniques across 13 tactics, which was comparable to many medium-risk actors in our dataset. Clearly, focusing on the number of techniques this actor used underplays how dangerous they really were (by contrast, applying our risk-scoring methodology to this attack earns it the maximum risk score of 100).

In that attack, the model worked as an autonomous agent: it executed commands, exploited vulnerabilities, stole credentials, and made tactical decisions, only requiring human input at a few key moments. There is no ATT&CK ID for this type of agentic orchestration—yet these are precisely the behaviors we expect to see much more of as AI agents become more capable.

## Looking ahead

The findings from this analysis helped inform the safeguards we build into our models. For example, we’ve developed and deployed cyber safeguards on our most capable models to detect and block some of the activities uncovered here, like developing malware or mass data exfiltration. Following on from our work with Verizon, we’re also in discussions with MITRE about how the ATT&CK framework might evolve to include the AI-enabled behaviors we observed.

Frontier models are rapidly changing the tools both attackers and defenders have at their disposal. We are committed to helping defenders get ahead of these evolving tactics, and to putting the most powerful tools in the hands of defenders first. We’ll continue to share what we learn from [Project Glasswing](https://www.anthropic.com/glasswing), from datasets like the one we gathered here, and from our other cybersecurity activities.

In our [Red blog post](https://red.anthropic.com/2026/attack-navigator/), we share an interactive visualization of the techniques used by attackers, in order to help defenders stay ahead of AI-enabled threats.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](/news/enterprise-frontier-safeguards)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](/news/improving-alignment-security-efforts)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](/news/model-hardware-standard-research-preview)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Commerce](https://claude.com/solutions/commerce)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](https://academy.claude.com)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Scientists](https://claude.com/programs/team-plan-for-scientists)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Leadership](/company/leadership)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
