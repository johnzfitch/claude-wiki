---
title: "Claude 3 Haiku: our fastest model yet \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-3-haiku"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:20Z"
tags: ["news-research"]
---

# **Claude 3 Haiku: **our fastest model yet

- Published

  Mar 13, 2024

- Category

  [Models](models.md)

- Topics

  - [Claude Haiku](https://www.anthropic.com/search?topic=claude-haiku)
  - [Claude Developer Platform](https://www.anthropic.com/search?topic=claude-developer-platform)
  - [Claude for Enterprise](https://www.anthropic.com/search?topic=claude-for-enterprise)
  - [Safeguards](https://www.anthropic.com/search?topic=safeguards)
  - [Partnerships](https://www.anthropic.com/search?topic=partnerships)

  See more...

Related articles

- Product

  Nov 18, 2025

  [Claude now available in Microsoft Foundry and Microsoft 365 Copilot](claude-in-microsoft-foundry.md)

[View more](https://www.anthropic.com/search?topic=claude-haiku)

Today we’re releasing Claude 3 Haiku, the fastest and most affordable model in its intelligence class. With state-of-the-art vision capabilities and strong performance on industry benchmarks, Haiku is a versatile solution for a wide range of enterprise applications. The model is now available alongside Sonnet and Opus in the Claude API and on claude.ai for our Claude Pro subscribers.

Speed is essential for our enterprise users who need to quickly analyze large datasets and generate timely output for tasks like customer support. Claude 3 Haiku is three times faster than its peers for the vast majority of workloads, processing 21K tokens (~30 pages) per second for prompts under 32K tokens \[1\]. It also generates swift output, enabling responsive, engaging chat experiences and the execution of many small tasks in tandem.

Haiku's pricing model, with a 1:5 input-to-output token ratio, was designed for enterprise workloads which often involve longer prompts. Businesses can rely on Haiku to quickly analyze large volumes of documents, such as quarterly filings, contracts, or legal cases, for half the cost of other models in its performance tier. For instance, Claude 3 Haiku can process and analyze 400 Supreme Court cases \[2\] or 2,500 images \[3\] for just one US dollar.

Alongside its speed and affordability, Claude 3 Haiku prioritizes enterprise-grade security and robustness. We conduct rigorous testing to reduce the likelihood of harmful outputs and jailbreaks of our models so they are as safe as possible. Additional layers of defense include continuous systems monitoring, endpoint hardening, secure coding practices, strong data encryption protocols, and stringent access controls to protect sensitive data. We also conduct regular security audits and work with experienced penetration testers to proactively identify and address vulnerabilities. More information about these measures can be found in the [Claude 3 model card](https://www.anthropic.com/claude-3-model-card).

Starting today, customers can use Claude 3 Haiku through our [API](https://www.anthropic.com/api) or with a Claude Pro subscription on claude.ai. Claude 3 Haiku is available on Amazon Bedrock and will be coming soon to Google Cloud Vertex AI.

## Footnotes

01Prompts containing over 32K tokens may experience 30-60% slower ingestion speeds, which we expect to improve in the coming weeks. Customers may also experience additional latency when processing images.

02Each Supreme Court case is estimated at 10K tokens each. [Source](https://www.supremecourt.gov/opinions/slipopinion/23).

03Each image is estimated at 1.6K tokens.
