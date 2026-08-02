---
title: "Our framework for developing safe and trustworthy agents \\ Anthropic"
source_url: "https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents"
category: "19-Reference"
fetched_at: "2026-08-02T07:10:48Z"
tags: ["agents"]
---

# Our framework for developing safe and trustworthy agents

Aug 4, 2025

The most popular AI tools today are assistants that respond to specific questions or prompts. But we’re now seeing the emergence of [AI agents](https://www.youtube.com/watch?v=LP5OCa20Zpg), which pursue tasks autonomously when given a goal. Think of an agent like a virtual collaborator that can independently handle complex projects from start to finish — all while you focus on other priorities.

Agents direct their own processes and tool usage, maintaining control over how they accomplish tasks with minimum human input. If you ask an agent to "help plan my wedding" it might autonomously research venues and vendors, compare pricing and availability, and create detailed timelines and budgets. Or if you ask it to "prepare my company’s board presentation", it might search through your connected Google Drive for relevant sales reports and financial documents, extract key metrics from multiple spreadsheets, and produce a report.

Last year, we introduced [Claude Code](https://www.anthropic.com/claude-code), an agent that can autonomously write, debug, and edit code, and is used widely by software engineers. Many companies are also building their own agents using our models. [Trellix,](https://www.anthropic.com/customers/trellix) a cybersecurity firm, uses Claude to triage and investigate security issues. And [Block](https://www.anthropic.com/customers/block), a financial services company, has built an agent that allows non-technical staff to access its data systems using natural language, saving its engineers time.

## Principles for trustworthy agents

The rapid implementation of agents means it's crucial that developers like Anthropic build agents that are safe, reliable and trustworthy. Today, we're sharing an early framework for responsible agent development. We hope this framework can help establish emerging standards, offer adaptable guidance for different contexts, and contribute to building an ecosystem where agents align with human values.

We aim to adhere to the following principles when developing agents:

## Keeping humans in control while enabling agent autonomy

A central tension in agent design is balancing agent autonomy with human oversight. Agents must be able to work autonomously—their independent operation is exactly what makes them valuable. But humans should retain control over how their goals are pursued, particularly before high-stakes decisions are made. For example, an agent helping with expense management might identify that the company is overspending on software subscriptions. Before it starts cancelling subscriptions or downgrading service tiers, the company would likely want a human to give approval.

In Claude Code, humans can stop Claude whenever they want and redirect its approach. It has read-only permissions by default, meaning it can analyze and review information within the directory it's initialized in without asking for human approval, but must ask for human approval before taking any actions that modify code or systems. Users can grant persistent permissions for routine tasks they trust Claude to handle.

As agents become more powerful and prevalent, we’ll need even more robust technical solutions and intuitive user controls. The right balance between autonomy and oversight varies dramatically across scenarios and likely includes a mix of built-in and customizable oversight features.

## Transparency in agent behavior

Humans need visibility into agents’ problem-solving processes. Without transparency, a human asking an agent to "reduce customer churn" might be baffled when the agent starts contacting the facilities team about office layouts. But with good transparency design, the agent can explain its logic: "I found that customers assigned to sales reps in the noisy open office area have 40% higher churn rates, so I'm requesting workspace noise assessments and proposing desk relocations to improve call quality." This also provides an opportunity to nudge agents in the right direction, by fact-checking their data, or making sure they’re using the most relevant sources.

In Claude Code, Claude shows its planned actions through a real-time to-do checklist, and users can jump in at any time to ask about or adjust Claude’s workplan. The challenge is in finding the right level of detail. Too little information leaves humans unable to assess whether the agent is on track to achieve its goal. Too much can overwhelm them with irrelevant details. We try to take a middle ground but we’ll need to iterate on this further.

##  Aligning agents with human values and expectations

Agents don't always act as humans intend. Our research has shown that when AI systems pursue goals autonomously, they can sometimes take actions that seem reasonable to the system but aren't what humans actually wanted. If a human asks an agent to "organize my files," the agent might automatically delete what it considers duplicates and move files to new folder structures—going far beyond simple organization to completely restructuring the user's system. While this stems from the agent trying to be helpful, it demonstrates how agents may lack the context to act appropriately even when their goals do align.

More concerning are cases where agents pursue goals in ways that actively work against users' interests. [Our testing of extreme scenarios](https://www.anthropic.com/research/agentic-misalignment) has shown that when AI systems pursue goals autonomously, they can sometimes take action that seem reasonable to the system but violate what humans actually wanted. Users may also inadvertently prompt agents in ways that lead to unintended outcomes.

Building reliable measures of agents’ value alignment is challenging. It’s hard to evaluate both the malign and benign causes of the problem at once. But we’re actively figuring out how to resolve this problem. Until we have, the transparency and control principles above will be particularly important.

## Protecting privacy across extended interactions

Agents can retain information across different tasks and interactions. This creates several potential privacy problems. Agents might inappropriately carry sensitive information from one context to another. For example, an agent might learn about confidential internal decisions from one department while helping with organizational planning, then inadvertently reference this information when assisting another department – exposing sensitive matters that should remain compartmentalized.

Tools and processes that agents utilize should also be designed with the appropriate privacy protections and controls. The open-source [Model Context Protocol](https://www.anthropic.com/partners/mcp) (MCP) we created, which allows Claude to connect to other services, includes controls to enable users to allow or prevent Claude from accessing specific tools and processes, or what we call “connectors” in a given task. In implementing MCP, we included additional controls, such as the option to grant one-time or permanent access to information. Enterprise administrators can also set which connectors users in their organizations can connect to. We continue to explore ways to improve our privacy protection tooling.

We’ve also outlined steps our customers should take to [safeguard their data](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-integrations-using-remote-mcp) through measures like access permissions, authentication, and data segregation.

## Securing agents’ interactions

Agent systems should be designed to safeguard sensitive data and prevent misuse when interacting with other systems or agents. Since agents are tasked with achieving specific goals, attackers could trick an agent into ignoring its original instructions, revealing unauthorized information, or performing unintended actions by making it seem necessary to do so for the agent’s objectives (also referred to as "prompt injection"). Or attackers could exploit vulnerabilities in the tools or sub-agents that agents use.

Claude already uses a system of [classifiers](https://www.anthropic.com/research/constitutional-classifiers) to detect and guard against misuses such as prompt injections, in addition to several [other layers of security](https://docs.anthropic.com/en/docs/claude-code/security). Our Threat Intelligence team conducts ongoing monitoring to assess and mitigate new or emerging forms of malicious behaviour. In addition, we [provide guidance](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) on how organizations using Claude can further decrease these risks. Tools added to our [Anthropic-reviewed MCP directory](https://www.anthropic.com/news/connectors-directory) must adhere to our security, safety, and compatibility [standards](https://support.anthropic.com/en/articles/11697096-anthropic-mcp-directory-policy).

When we discover new malicious behaviors or vulnerabilities through our monitoring and research, we strive to address them quickly and continuously improve our security measures to stay ahead of evolving threats.

## Next steps

As we continue developing and improving our agents, we expect our understanding of their risks and trade-offs to also evolve. Over time, we’ll plan to revise and update this framework to reflect our view of best practices.

These principles will guide our current and future work on agent development, and we look forward to collaborating with other companies and organizations on this topic. Agents have tremendous potential for positive impacts in work, education, healthcare, and scientific discovery. That is why it is so important to ensure they are built to the highest standards.

  
## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](/news/investigating-incidents-cybersecurity-evals)

### Our position on open-weights models

[Read more](/news/position-open-weights-models)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](/news/cognizant-anthropic)

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
- [Claude for Chrome](https://claude.com/chrome)
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
- [Courses](/learn)
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
- [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
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
