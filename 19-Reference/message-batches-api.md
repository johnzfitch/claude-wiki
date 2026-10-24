---
title: "Introducing the Message Batches API | Claude by Anthropic"
source_url: "https://www.anthropic.com/news/message-batches-api"
category: "19-Reference"
fetched_at: "2026-10-23T06:29:22Z"
tags: ["api", "news-research"]
---

# Introducing the Message Batches API

Claude now offers a Message Batches API that processes up to large volumes of queries asynchronously at lower cost.

- 

  Category[Announcements](https://www.anthropic.com/resources/product-announcements)
- 

  ProductClaude Platform
- 

  DateOctober 8, 2024
- 

  Reading time4 min
- 


***Update:** The Message Batches API is Generally Available on the Anthropic API. Customers using Claude in Amazon Bedrock can use batch inference. Batch predictions is also available in preview on Google Cloud’s Vertex AI. (December 17, 2024)*  
  
  
We’re introducing a new [Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)—a powerful, cost-effective way to process large volumes of queries asynchronously.

Developers can send batches of up to 10,000 queries per batch. Each batch is processed in less than 24 hours and costs 50% less than standard API calls. This makes processing non-time-sensitive tasks more efficient and cost-effective.

The Batches API is available today in public beta with support for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku on the Anthropic API. Customers using Claude in Amazon Bedrock can use [batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html). Support for batch processing for [Claude on Google Cloud’s Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) is coming soon.

## High throughput at half the cost

Developers often use Claude to process vast amounts of data—from analyzing customer feedback to translating languages—where real-time responses aren't necessary.

Instead of managing complex queuing systems or worrying about rate limits, you can use the Batches API to submit groups of up to 10,000 queries and let Anthropic handle the processing at a 50% discount. Batches will be processed within 24 hours, though often much quicker. Additional benefits include:

- **Enhanced throughput:** Enjoy higher rate limits to process much larger request volumes without impacting your standard API rate limits.
- **Scalability for big data:** Handle large-scale tasks such as dataset analysis, classification of large datasets, or extensive model evaluations without infrastructure concerns.

The Batches API unlocks new possibilities for large-scale data processing that were previously less practical or cost-prohibitive. For example, analyzing entire corporate document repositories—which might involve millions of files—becomes more economically viable by leveraging our batching discount.

## Pricing

The Batches API allows you to take advantage of infrastructure cost savings and is offered at a 50% discount for both input and output tokens.

[TABLE]

## Customer Spotlight: Quora

[Quora](https://cloud.google.com/customers/quora?hl=en), a user-based question-and-answer platform, leverages Anthropic's Batches API for summarization and highlight extraction to create new end-user features.

"Anthropic's Batches API provides cost savings while also reducing the complexity of running a large number of queries that don't need to be processed in real time," said Andy Edmonds, Product Manager at Quora. "It's very convenient to submit a batch and download the results within 24 hours, instead of having to deal with the complexity of running many parallel live queries to get the same result. This frees up time for our engineers to work on more interesting problems.”

## Get started

To start using the Batches API in public beta on the Anthropic API, explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/message-batches) and [pricing page](https://docs.anthropic.com/en/docs/build-with-claude/message-batches).

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleOct 22, 2026

### The full Claude Platform, available on Google Cloud

Use Claude Models on Google Cloud (Anthropic managed) to access Claude Platform features with Google Cloud authentication, billing, and commitment retirement.

Claude Platform


ArticleOct 21, 2026

### HCLTech joins the Claude Partner Network as a Global Premier partner

HCLTech will bring Claude into the solutions it provides for banks, hospitals, telecom companies, and manufacturers.


ArticleOct 21, 2026

### Introducing Claude Duet

A research preview is available by waitlist today, starting with US Pro and Max subscribers.


ArticleOct 21, 2026

### Claude Security now scans continuously and tracks fixes

Claude Security now keeps up with your repositories as code changes, tracks findings until they’re fixed, learns from the context your team adds, and connects to your tools through an API and MCP. Available in public beta for Claude Enterprise customers.

Claude Security
