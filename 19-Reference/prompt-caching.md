---
title: "Prompt caching with Claude | Claude by Anthropic"
source_url: "https://www.anthropic.com/news/prompt-caching"
category: "19-Reference"
fetched_at: "2026-10-10T06:25:00Z"
tags: ["news-research", "prompting"]
---

# Prompt caching with Claude

Claude caches frequently used context between API calls, reducing costs and latency for long prompts.

- 

  Category[Announcements](https://www.anthropic.com/resources/product-announcements)
- 

  ProductClaude Platform
- 

  DateAugust 14, 2025
- 

  Reading time4 min
- 


***Update**: Prompt caching is Generally Available on the Anthropic API. Prompt caching is also available in preview in Amazon Bedrock and on Google Cloud’s Vertex AI. (December 17, 2024)*  
  
  
Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API. With prompt caching, customers can provide Claude with more background knowledge and example outputs—all while reducing costs by up to 90% and latency by up to 85% for long prompts. Prompt caching is available today in public beta for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.

## When to use prompt caching

Prompt caching can be effective in situations where you want to send a large amount of prompt context once and then refer to that information repeatedly in subsequent requests, including:

- **Conversational agents:** Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents.
- **Coding assistants:** Improve autocomplete and codebase Q&A by keeping a summarized version of the codebase in the prompt.
- **Large document processing:** Incorporate complete long-form material including images in your prompt without increasing response latency.
- **Detailed instruction sets:** Share extensive lists of instructions, procedures, and examples to fine-tune Claude's responses. Developers often include a few examples in their prompt, but with prompt caching you can get even better performance by including dozens of diverse examples of high quality outputs.
- **Agentic search and tool use:** Enhance performance for scenarios involving multiple rounds of tool calls and iterative changes, where each step typically requires a new API call.
- **Talk to books, papers, documentation, podcast transcripts, and other long-form content:** Bring any knowledge base alive by embedding the entire document(s) into the prompt, and letting users ask it questions.  

Early customers have seen substantial speed and cost improvements with prompt caching for a variety of use cases—from including a full knowledge base to 100-shot examples to including each turn of a conversation in their prompt.

| **Use case**                                                            | **Latency w/o caching (time to first token)** | **Latency w/ caching (time to first token)** | **Cost reduction** |
|-------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------|--------------------|
| Chat with a book (100,000 token cached prompt) \[1\]                    | 11.5s                                         | 2.4s (-79%)                                  | -90%               |
| Many-shot prompting (10,000 token prompt) \[1\]                         | 1.6s                                          | 1.1s (-31%)                                  | -86%               |
| Multi-turn conversation (10-turn convo with a long system prompt) \[2\] | ~10s                                          | ~2.5s (-75%)                                 | -53%               |

Prompt caching

### How we price cached prompts

Cached prompts are priced based on the number of input tokens you cache and how frequently you use that content. Writing to the cache costs 25% more than our base input token price for any given model, while using cached content is significantly cheaper, costing only 10% of the base input token price.

[TABLE]

Pricing

### Customer spotlight: Notion

[Notion](https://www.notion.so/product/ai) is adding prompt caching to Claude-powered features for its AI assistant, Notion AI. With reduced costs and increased speed, Notion is able to optimize internal operations and create a more elevated and responsive user experience for their customers.

— Simon Last, Co-founder at Notion

### Get started

To start using the prompt caching public beta on the Anthropic API, explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) and [pricing page](https://www.anthropic.com/pricing#anthropic-api).

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleOct 8, 2026

### Build live dashboards and animate explainers with Claude 

Claude Dashboards and Claude Motion are now in beta. Docs, Slides, and Design are out of beta and on every Claude plan, including Free.

Claude appsClaude Design

2 more: Claude Cowork and Claude CodeClaude CoworkClaude Code


ArticleOct 7, 2026

### Claude Haiku 5.5

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.

(opens in new tab)[](https://www.anthropic.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)

ArticleOct 6, 2026

### Claude now works with Google Docs, Sheets, and Slides

Teams that run on Google Workspace can now bring Claude into their files or work on their files directly from Claude, with our new add-on and Google Docs, Sheets, and Slides connectors (in beta).

Claude Enterprise


ArticleOct 6, 2026

### We’re expanding the Claude Startups program to help founders build
