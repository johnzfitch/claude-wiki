---
title: "Box Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/box"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:11Z"
tags: ["api", "case-studies", "enterprise", "security", "skills"]
---

# Box builds document creation into its AI agent with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Large

Product:  
[Claude Platform](https://claude.com/platform/api)

Location:  
North America

Concept to customer-facing capability in weeks using the Claude Skills API

instead of building document generation in-house

2-minute contract redline

when Box's team tested jurisdiction changes on a contract

[Box](https://www.box.com/) securely connects enterprise content to AI, enabling organizations to manage files and automate business processes. Its agent, the Box Agent, recently gained the ability to support document creation through Anthropic's Skills API.

## With Claude, Box:

- Saved months of development time by using the Skills API instead of building document generation in-house
- Went from concept to customer-facing document creation in weeks by using the Skills API instead of building in-house
- Redlined a contract in 2 minutes instead of an afternoon of manual review
- Generates multiple document formats from a single conversation: the same source material returned as a slide, a spreadsheet, or a written brief
- Creates PowerPoint, Excel, Word, and PDF files inside the Box agent without a separate code-execution environment
- Analyzes spreadsheets using their full structure rather than extracted text
- Maintains enterprise security through Box's existing LLM gateway, with only 2 new data paths added

## The challenge

## Bringing document creation inside Box

Box customers could already create, collaborate on, and sign documents inside the platform. Early customers of the new Box Agent consistently requested the ability to generate presentations, documents, and other file formats. Building that capability in-house didn’t make sense from a timing, effort, or focus standpoint. It would have meant standing up a distributed code-execution environment across Box's data centers and meeting the 5-nines reliability bar Box's customers expect. Box's team estimated the work for the in-house path would take months of engineering time.

“Box's strength is in how enterprise content is managed, governed, and put to work,” said Darryl Sladden, Staff Product Manager for AI at Box. “The intelligence to make a good slide is a different problem, and it's one Anthropic has already solved.”

2 minutes

Redlined a contract vs. an afternoon of manual review

## The solution

## Pre-built skills connected to the path Box already trusted

Box turned to Anthropic's Skills API for the generation itself. Anthropic's pre-built skills for PowerPoint, Excel, Word, and PDF deliver packaged expertise: they encode what makes a slide visually appealing, how to structure analytical spreadsheets, and how to handle complex Word edits cleanly.

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly,” Darryl says.

The integration principle was to change as little as possible. Box already routes all LLM requests through a production gateway that handles logging, request counting, and access control. Rather than create a separate path for document generation, the team added exactly two things: file upload on the way in, file download on the way out.

“We ran this through our main production path and added the file upload, file download capabilities,” Darryl says. “Everything else: the same file versioning, the same ownership. The only difference we have to talk about is those two paths.”

Inside the agent, Box routes work across Claude models by difficulty. Sonnet typically interprets the user's request, searches Box for relevant source files, and assembles context, while file generation often goes to the more capable Opus model. That flips the common pattern of using the larger model as planner and a smaller one as executor, but it matches where the difficulty sits: orchestrating over Box content is well-bounded, while producing a document that looks right demands more from the model.

The pre-built skills are also what made the speed possible. Spreadsheet analysis benefits from the full structure of a spreadsheet rather than just text extracted by RAG, and PowerPoint generation depends on judgment that's hard to specify, let alone replicate. “PowerPoint files have a lot of taste,” Darryl said. “It's really the designer's mind that I always find is most valuable, that it's actually been trained in.”

The capability runs under Box's existing Anthropic agreement, which contractually ensures customer data isn't used for training. Containers that execute skill code are short-lived, lasting only minutes. For Box's security team, the review was about two new data paths, not a new trust boundary.

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## Redlining a contract in 2 minutes

Using the Skills API, Box went from concept to customer-facing capability in weeks. A member of Box's internal team tested the agent on a real contract, asking it to show redlines for changing the governing jurisdiction from New York to California. “We just waited two minutes, and it output the entire document,” Darryl said. “It was smart enough to change not only the state, but the city and all the additional clauses that talked about court.”

The financial summary flow works the same way: a user asks for a slide summarizing a company's financial position; the agent searches their Box folders, finds the previous quarterly report and recent monthly updates, pulls the relevant figures, and returns a formatted draft slide with the initial work done, ready for the team to add insights. A follow-up request for the same output as a spreadsheet reuses what the agent already found.

Box went from concept to customer-facing document creation capability in about a month, a timeline that wouldn't have been possible building from scratch. The time that didn't go into infrastructure went into making the agent actively useful inside the enterprise.

The principle that emerged: use pre-built skills where the expertise is general and already trained in; build your own where the knowledge is yours. “The trajectory of AI is really what we're betting on for this,” Darryl said. “Our advice is to look at each capability not only how it is now, but how it will be in six months.”

How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

[Read more](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026)

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
