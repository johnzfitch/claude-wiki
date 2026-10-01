---
title: "Prompt engineering for business performance \\ Anthropic"
source_url: "https://www.anthropic.com/news/prompt-engineering-for-business-performance"
category: "19-Reference"
fetched_at: "2026-08-02T07:10:49Z"
tags: ["news-research", "prompting"]
---

# Prompt engineering for business performance

Feb 29, 2024

## Executive summary

- Prompt engineering is an important tool for any business seeking to optimize Claude. Good prompts improve Claude’s outputs, reduce deployment costs, and ensure customer-facing experiences are on-brand.
- A Fortune 500 company made use of effective prompt engineering to build a Claude-powered assistant that answers its customers’ questions with enhanced accuracy and speed.

## The power of prompting

As businesses build with generative AI models, crafting effective prompts has become critical for producing high-quality outputs. This post explains basic prompt engineering techniques that help our customers get the most value from Claude. With the right prompts, businesses can tap into the full potential of AI to increase productivity across a wide range of tasks.

We also share how our prompt engineering team has been helping a Fortune 500 company build a customer-facing chat assistant that answers complex questions quickly and accurately - and how you can apply those tips too.

To gain the most value from Claude, you can apply a variety of techniques to create prompts that accomplish your desired tasks. These include processing data, answering customer questions, or reviewing contracts with increasing efficiency, while providing useful, relevant, and accurate results aligned to your goals and standards.

### Here are some of the benefits of effective prompts:

- **Accuracy:** While we have made strides in [reducing Claude’s hallucination rates](claude-2-1.md), effective prompting helps further reduce the risk of inaccurate outputs
- **Consistency:** Providing a cohesive experience for end-users is crucial, and well thought out prompts ensure that Claude will produce consistent results in terms of quality, formatting, relevance, and tone
- **Usefulness:** Prompt engineering helps customers deliver targeted experiences for their desired audiences and industries. With careful prompting, you can cater to very specific personas and their needs
- **Cost savings:** Running inefficient inputs and outputs at scale can become costly. Optimizing your prompts helps minimize unnecessary back-and-forth, and saves money

## Three tips for your business

Here are three prompting techniques that we’ve seen unlock significant performance gains for businesses.

Before we dive in, remember that no matter which techniques you choose, always start by clearly describing the task. Think of Claude as an intern on their first day of the job: provide clear, explicit instructions with all the necessary detail. Keep in mind that prompt engineering is a science, and you should approach it like a scientist: test your prompts and iterate often.

### 1. Step by step

It might sound overly simple, but often Claude will respond more accurately if you simply tell it to [think step by step](https://docs.anthropic.com/claude/docs/ask-claude-to-think-step-by-step) after you give it an instruction.

For example, if you wanted Claude to solve a logic puzzle, you could say:

*"Here is the information a customer provided for an automotive insurance claim. Based on our policy documents and the customer's profile, does this claim meet our requirements for qualification? Think step by step in \<thinking\> tags."*

### 2. Few-shot prompting

It’s helpful to give Claude realistic and specific examples of the inputs and ideal outputs you’re hoping to see. It’s useful to include challenging examples and edge cases to help Claude understand exactly what you’re looking for.

For a simple example, consider how Claude can help with removing personally-identifiable information (PII) from information, using 2 examples to help Claude understand different ways that PII could present itself in a prompt. A simplified example using [claude.ai](https://claude.ai/redirect/website.v1.a6954ffe-33ae-47f0-82bb-b50bc957faf1) may look something like this:

*You are an expert redactor. I am going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replaced with XXX.*

*Here are two synthetic examples of how this should be done:*

*\<examples\>  
\<example\>  
\<text\>  
My name is Jacob LaPont. My email address is jlp@geemail.com and my phone number is 555-492-1902. I am 43 years old. My account ID is 52777930.  
\</text\>  
The output should be:  
\<response\>  
My name is XXX. My email address is XXX@XXX.XXX and my phone number is XXX. I am XXX years old. My account ID is XXX.  
\</response\>  
\</example\>  
\<example\>  
\<text\>  
Bo Nguyen is a cardiologist at Mercy Health Medical Center. He can be reached at 925-123-456 or b@mercy.health.  
\</text\>  
The output should be:  
\<response\>  
XXX is a cardiologist at Mercy Health Medical Center. He can be reached at XXX-XXX-XXXX or XXX@XXX.  
\</response\>  
\</example\>  
\</examples\>*

*Now here is the text I’d like you to redact:*

*\<text\>  
The customer's name is Steven Smith with Customer ID 44201312. His email address is steven.smith@geemail.com, or reach him via telephone at 555-182-9942.  
\</text\>*

### 3. Prompt chaining

Sometimes Claude performs better on complex tasks if you break the task down into multiple prompts corresponding to each step. This is known as ‘prompt chaining’.

Prompt chaining allows you to iterate on a prompt over multiple steps. Each new prompt can include the previous prompt-response pairs to build on the context. This technique enables you to guide Claude through a process by repeatedly prompting, responding, and expanding the prompt with each interaction.

For example, if you want Claude to help with explaining tax situations, you could first prompt it to create a list of the tax codes that are related to the specific question, then prompt Claude to identify the relevant sections in each document, and finally, to respond to a user question based on the information Claude’s gathered.

## Case study: Prompting for enhanced accuracy and speed

A Fortune 500 company wanted to build an AI-powered chat assistant that could respond to customers’ questions about some unique and complex issues.

The company tried some other solutions in the market, but were unhappy with their wordiness, stilted tone, and overall lack of cohesion. They also wanted to see if they could achieve lower latency — i.e., provide faster responses — without affecting accuracy.

They turned to [Claude Instant](releasing-claude-instant-1-2.md) to power a friendly, concise chatbot that could answer customers’ questions quickly and accurately.

The company’s first efforts to deploy Claude fell short of their goal for accuracy. To remedy this, we sent in an Anthropic prompt engineer to partner with the company’s subject matter experts on improving Claude’s responses.

Our prompt engineers applied several techniques to improve Claude’s outputs, including:

- Telling Claude to use a scratchpad to show its work (customers don’t see the scratchpad, but it helps improve Claude’s accuracy)
- Providing few-shot examples of good answers, with a focus on training Claude to use the company’s desired format and style
- Directing Claude to use the data points and workflow recommended by subject matter experts (SMEs) — in this case, a set of factors that affect a customer’s legal situation

Below is an example prompt to help bring this guidance to life. In this example, the inclusion of “relevant_quotes” serves the purpose of telling Claude to use a scratchpad.

*"  
Human: You are an expert AI tax analyst. You help users understand the details of the tax code.*

*Here is the relevant section of the tax code.  
\<tax_code\>  
{{TAX_CODE}}  
\</tax_code\>*

*Here are some examples of questions and answers about this section of the tax code:*

*\<examples\>  
\<example\>  
\<question\>  
{{EXAMPLE QUESTION 1}}  
\</question\>  
\<answer\>  
{{EXAMPLE ANSWER 1}}  
\</answer\>  
\</example\>  
…  
\</examples\>*

*Now here is the user's question about the tax code that I’d like you to answer:  
\<question\>{{QUESTION}}\</question\>*

*First, pull relevant quotes from the tax code in \<relevant_quotes\> tags. Then write a concise, factual response to the user’s question in \<answer\> tags. Your answer should be fully grounded in the relevant quotes from the tax code that you extracted.*

*Assistant: \<relevant_quotes\>"*

By combining our prompt engineers’ knowledge of prompting best practices with the customer’s subject matter expertise, we **improved Claude’s accuracy by 20%** - and helped get their product to market faster and at a lower cost.

### Getting started with prompt engineering

There’s no single best technique for prompt engineering. Every LLM is different and the best way to prompt one model may not work as well for others. AI technology itself is nascent, and our collective understanding of how models work is evolving every day.

If you’re deploying an AI-powered solution within your business, prompt engineering is essential — and it should be a collaborative effort between prompt engineers and subject matter experts.

To get started on optimizing Claude for your use case, read our [prompt engineering guide](https://docs.anthropic.com/claude/docs/guide-to-anthropics-prompt-engineering-resources) or [contact our sales team](https://www.anthropic.com/earlyaccess).


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
