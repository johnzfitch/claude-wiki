---
title: "Introducing Claude 2.1 \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-2-1"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:28Z"
tags: ["news-research"]
---

# Introducing Claude 2.1

Nov 21, 2023

  
Our latest model, Claude 2.1, is now available over API in our Console and is powering our [claude.ai](https://claude.ai/redirect/website.v1.3b41a8b2-a27a-46a1-a132-0949af4dfa75) chat experience. Claude 2.1 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and our new beta feature: tool use. We are also updating our [pricing](https://www-cdn.anthropic.com/1b1ea2c43d8dd058f6a331a8097e05ea40d626c6/model_pricing_nov2023.pdf) to improve cost efficiency for our customers across models.  
  
**200K Context Window**  
  
Since our launch earlier this year, Claude has been used by millions of people for a wide range of applications—from translating academic papers to drafting business plans and analyzing complex contracts. In discussions with our users, they’ve asked for larger context windows and more accurate outputs when working with long documents.  
  
In response, we’re doubling the amount of information you can relay to Claude with a limit of 200,000 tokens, translating to roughly 150,000 words, or over 500 pages of material. Our users can now upload technical documentation like entire codebases, financial statements like S-1s, or even long literary works like The Iliad or The Odyssey. By being able to talk to large bodies of content or data, Claude can summarize, perform Q&A, forecast trends, compare and contrast multiple documents, and much more.  
  

Processing a 200K length message is a complex feat and an industry first. While we’re excited to get this powerful new capability into the hands of our users, tasks that would typically require hours of human effort to complete may take Claude a few minutes. We expect the latency to decrease substantially as the technology progresses.  
  
**2x Decrease in Hallucination Rates**  
  
Claude 2.1 has also made significant gains in honesty, with a 2x decrease in false statements compared to our previous Claude 2.0 model. This enables enterprises to build high-performing AI applications that solve concrete business problems and deploy AI across their operations with greater trust and reliability.  
  
We tested Claude 2.1’s honesty by curating a large set of complex, factual questions that probe known weaknesses in current models. Using a rubric that distinguishes incorrect claims (“The fifth most populous city in Bolivia is Montero”) from admissions of uncertainty (“I’m not sure what the fifth most populous city in Bolivia is”), Claude 2.1 was significantly more likely to demur rather than provide incorrect information.  

Claude 2.1 has also made meaningful improvements in comprehension and summarization, particularly for long, complex documents that demand a high degree of accuracy, such as legal documents, financial reports and technical specifications. In our evaluations, Claude 2.1 demonstrated a 30% reduction in incorrect answers and a 3-4x lower rate of mistakenly concluding a document supports a particular claim.  
  

While we are encouraged by these accuracy improvements, enhancing the precision and dependability of outputs for our users remains a top priority for our product and research teams.  
  
**API Tool Use**  
  
By popular demand, we’ve also added tool use, a new beta feature that allows Claude to integrate with users' existing processes, products, and APIs. This expanded interoperability aims to make Claude more useful across our users’ day-to-day operations.  
  
Claude can now orchestrate across developer-defined functions or APIs, search over web sources, and retrieve information from private knowledge bases. Users can define a set of tools for Claude to use and specify a request. The model will then decide which tool is required to achieve the task and execute an action on their behalf, such as:

- Using a calculator for complex numerical reasoning
- Translating natural language requests into structured API calls
- Answering questions by searching databases or using a web search API
- Taking simple actions in software via private APIs
- Connecting to product datasets to make recommendations and help users complete purchases

Tool use is currently in early development—we are building developer features and prompting guidelines for easier integration into your applications. We encourage users to share feedback on tool use to help shape and improve the product.  
  
**Developer Experience**  
  
We’ve been working to simplify our developer Console experience for Claude API users while making it easier to test new prompts for faster learning. Our new Workbench product enables developers to iterate on prompts in a playground-style experience and access new model settings to optimize Claude’s behavior. They can create multiple prompts and navigate between them for different projects, and revisions are saved as they go to retain historical context. Developers can also generate code snippets to use their prompts directly in one of our SDKs.  
  

We’re also introducing [system prompts](https://docs.anthropic.com/claude/docs/how-to-use-system-prompts), which allow users to provide custom instructions to Claude in order to improve performance. System prompts set helpful context that enhances Claude’s ability to take on specified personalities and roles or structure responses in a more customizable, consistent way aligned with user needs.

[Claude 2.1](https://www-cdn.anthropic.com/5c49cc247484cecf107c699baf29250302e5da70/ModelCardClaudev2_with_appendix_v1.pdf) is available now in our API, and is also powering our chat interface at [claude.ai](https://claude.ai/redirect/website.v1.3b41a8b2-a27a-46a1-a132-0949af4dfa75) for both the free and Pro tiers. Usage of the 200K token context window is reserved for Claude Pro users, who can now upload larger files than ever before. We can't wait to see the use cases these new features inspire as we work to build the safest and most technically sophisticated AI systems in the industry.


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
