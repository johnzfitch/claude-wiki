---
title: "Introducing 100K context windows \\ Anthropic"
source_url: "https://www.anthropic.com/news/100k-context-windows"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:16Z"
tags: ["news-research"]
---

# Introducing 100K context windows

- Published

  May 11, 2023

- Category

  [Product](product.md)

- Topics

  - [Context engineering](https://www.anthropic.com/search?topic=context-engineering)
  - [Claude Developer Platform](https://www.anthropic.com/search?topic=claude-developer-platform)
  - [Productivity](https://www.anthropic.com/search?topic=productivity)
  - [Partnerships](https://www.anthropic.com/search?topic=partnerships)

  See more...

Related articles

- Announcements

  Sep 28, 2026

  [Introducing Claude Sonnet 5.5](../15-Claude-AI-Features/claude-sonnet-5-5.md)

[View more](https://www.anthropic.com/search?topic=context-engineering)

We’ve expanded Claude’s context window from 9K to 100K tokens, corresponding to around 75,000 words! This means businesses can now submit **hundreds of pages** of materials for Claude to digest and analyze, and conversations with Claude can go on for hours or even days.

The average person can read 100,000 tokens of text in ~5+ hours\[1\], and then they might need substantially longer to digest, remember, and analyze that information. Claude can now do this in less than a minute. For example, we loaded the entire text of The Great Gatsby into Claude-Instant (72K tokens) and modified one line to say Mr. Carraway was “a software engineer that works on machine learning tooling at Anthropic.” When we asked the model to spot what was different, it responded with the correct answer in **22 seconds**.

Beyond just reading long texts, Claude can help retrieve information from the documents that help your business run. You can drop multiple documents or even a book into the prompt and then ask Claude questions that require synthesis of knowledge across many parts of the text. For complex questions, this is likely to work substantially better than vector search based approaches. Claude can follow your instructions and return what you’re looking for, as a human assistant would!

Our partners are excited about what larger context windows means for their business. 100K translates into roughly 6 hours of audio - AssemblyAI put out a great demonstration of this where they transcribed a long podcast into 58K words and then used Claude for summarization and Q&A. You can watch the full demo [here](https://youtu.be/2kFhloXz5_E). With 100K context windows, you can:

- Digest, summarize, and explain dense documents like financial statements or research papers
- Analyze strategic risks and opportunities for a company based on its annual reports
- Assess the pros and cons of a piece of legislation
- Identify risks, themes, and different forms of argument across legal documents.
- Read through hundreds of pages of developer documentation and surface answers to technical questions
- Rapidly prototype by dropping an entire codebase into the context and intelligently build on or modify it

100K context windows are now available in our API. If you are working with Claude, you can read more about what model versions to call [here](https://console.anthropic.com/docs/api/reference#-v1-complete). If you’re not working with Claude yet, you can request access [here](../15-Claude-AI-Features/product-overview.md).

## Footnotes

01[https://www.sciencedirect.com/...](https://www.sciencedirect.com/science/article/abs/pii/S0749596X19300786)
