---
title: "Block Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/block"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:11Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# Block improves employee productivity and data access with Claude in Databricks

[Try Claude](https://claude.ai)

Industry:  
Financial services

Company size:  
Large

Product:  
Claude Platform

Location:  
North America

75% of engineers

saving 8-10+ hours weekly

100% success

on benchmark tests with Claude 3.5 Sonnet

Block—the company behind Square, Cash App, Afterpay, and other financial services—uses Claude on the Databricks Data Intelligence Platform as the default model to power the internal deployment of its open source AI agent, codename goose. This solution enables employees across all roles to interconnect internal tools and systems, analyze complex data, create SQL queries without technical knowledge, and automate workflows—transforming how their organization operates.

With Claude in Databricks, Block has seen:

- 75% of engineers saving 8 to 10+ hours every week using codename goose — accelerating velocity and cutting down on busywork
- codename goose adoption doubling in just one month with user engagement increasing 40-50% weekly as employees discover new use cases
- Claude 3.5 Sonnet becoming the only model to consistently achieve 100% success on [their benchmark tests](https://block.github.io/goose/blog/2025/03/31/goose-benchmark/)

## Giving more employees access to data insights

Block has vast data resources and needed a way to make them accessible to employees regardless of their technical background. The company had long used Databricks for data engineering but recognized an opportunity to combine these capabilities with large language models and their internally built technology to democratize data access throughout the organization.

Bradley Axen, Principal Data and Machine Learning Engineer, explained, "We've worked with Databricks for years as our primary data engineering platform, using their Spark capabilities for our data processing needs."

The company initially created an AI coding assistant, codename goose, but quickly realized its potential extended far beyond software development. Axen said, "goose started as a simple tool to help my team write better code. It began as a basic feedback loop. Since then, it has evolved dramatically. This might sound exaggerated, but it's true—90% of my lines of code are now written by goose. Part of that is because I want to use the tools I'm building, but it's also because the tool has become that effective."

From design to product development, thousands of Block employees across all job categories are now using Claude via Databricks, sometimes without even realizing it, and it’s freeing them up for bigger, more creative thinking.

## Superior performance and security with Claude in Databricks

After rigorous benchmarking, Block found Claude has consistently outperformed other models in codename goose, to date. "For the tasks we care about measuring specifically, the Claude family has performed the best," noted Axen.

Security was another critical factor in their decision. "We care deeply about secure data integrations. When we connect to Databricks, we can use OAuth with short-lived credentials. So every employee now has access to these LLMs without us having to distribute and manage API keys," Axen emphasized. This security infrastructure allows Block to "flip a switch and make new models available to everybody," providing immense flexibility for their platform team.

Block particularly values Claude's tool use and code generation capabilities. They strategically employ different Claude models based on the specific task at hand—choosing Claude 3.5 Sonnet for complex data analysis requiring sophisticated reasoning, and Claude 3.7 Sonnet for requests that require more steps and planning.

## Transforming data access through agentic workflows

Block integrated Claude in Databricks with goose to create an ecosystem connecting multiple data sources and tools. "With our agent-based approach, we've created a complete workflow loop," said Axen. "We run the LLM through a Databricks endpoint, connect it to our agent system goose, and then goose can call back to Databricks to access our databases and datasets."

This approach allows employees across departments to interact with data more efficiently:

- SQL generation without technical knowledge: The model writes SQL, sends it to the data endpoint, and brings back insights. Someone without SQL knowledge can solve their own data problems, enabling product teams and non-technical employees to answer data questions without waiting for data scientists.
- Complex data feature engineering: Engineers created a system that teaches Claude to write code for Block's internal Beacon service. An MCP server teaches the LLMs on Databricks how to submit code to Beacon, allowing machine learning engineers to create sophisticated data features without deep knowledge of Block's backend systems.
- Multi-tool data workflows: codename goose uses MCP to connect diverse systems. Block can build an MCP server for any internal tool and connect it to workflows. This allows the operations team to use AI to close case tickets and helps departments access the data they need.

This agentic approach aligns with Block's broader vision. "The big opportunity is having an LLM translate someone's intent into actions on our systems. That's going to change how we offer products to customers and how we work internally," Axen noted.

## Creating a data-driven culture with measurable results

Block's Claude in Databricks implementation has gained significant traction internally. Around 4,000 of Block's 10,000 employees actively use goose, with adoption across 15 different job profiles from sales, design, product, to customer success, operations, and beyond.

The impact on productivity is substantial, particularly in how quickly teams can access insights. It's been a huge deal for Block because someone who doesn't know SQL can now solve their own data problems.

One team that also benefits is design. Axen explained, "The barrier to entry for a designer to turn their idea into a working prototype was too high, so they often wouldn't. Now that barrier is almost entirely gone. You can say, 'Here's a web page in Figma. Let's make a functioning version,' and it does it." This has fundamentally changed the design workflow, enabling designers to build and test functional prototypes before sharing them.

## Building a future powered by accessible data and agentic AI

Block envisions a future where data access is fully democratized through agentic AI systems. "The ceiling isn't saving 100% of your time. It's actually higher because you can have a whole team of agents working on your behalf, doing more than you could alone," said Axen.

While Block aims to save 30% of employee time through AI in 2025, their vision goes beyond efficiency. "It's about enabling our people to act on all our good ideas. Over the coming years, jobs will change. People will still solve challenging problems, but they'll spend less time writing code," Axen explains. Block's goal is to shift from being constrained by delivery speed to being limited only by how fast they can innovate.

While focused on internal productivity today, Block is strategically developing customer-facing AI products. "We're learning what works and how to make it easier for people to pick it up," explains Axen. Though some agentic products already exist in their ecosystem, Block is prioritizing quality before wider deployment. Their internal implementation of codename goose serves as both a productivity tool and a vital testing ground, developing the infrastructure and design principles that will power their next generation of customer offerings.

Block is creating a future where every employee can unlock the full potential of their company's data by combining Claude's advanced reasoning capabilities with the Databricks Data Intelligence Platform through codename goose. This partnership enables Block’s workforce to embrace AI-assisted workflows, turning their vision of economic empowerment into reality through technology that makes sophisticated data analysis accessible to all.

## Related stories


### How Qonto delegates financial admin for small businesses with Claude on Amazon Bedrock


### Pictet turns weeks of work into hours with Claude Code


### How Satispay's engineers write 75% of their code with Claude


### OffDeal powers every stage of M&A advisory with one Claude-based agent

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
