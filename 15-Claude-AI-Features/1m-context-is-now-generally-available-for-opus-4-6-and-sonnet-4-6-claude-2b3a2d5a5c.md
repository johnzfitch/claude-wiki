---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-14T10:16:27Z"
last_modified: "Sat, 14 Mar 2026 03:45:16 GMT"
source_url: "https://claude.com/blog/1m-context-ga"
title: "1M context is now generally available for Opus 4.6 and Sonnet 4.6 | Claude"
---

# 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Standard pricing now applies across the full 1M window for both models, with no long-context premium. Media limits expand to 600 images or PDF pages.

‍

[](#)

[](#)

- 

  Category

  [Product announcements](https://claude.com/blog/category/announcements)

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

- 

  Product

  Claude Platform

  Claude Code

- 

  Date

  March 13, 2026

- 

  Reading time

  5

  min

- 

  Share

  [Copy link](#)
  https://claude.com/blog/1m-context-ga

Claude Opus 4.6 and Sonnet 4.6 now include the full 1M context window at standard pricing on the Claude Platform. Standard pricing applies across the full window — \$5/\$25 per million tokens for Opus 4.6 and \$3/\$15 for Sonnet 4.6. There's no multiplier: a 900K-token request is billed at the same per-token rate as a 9K one.

**What's new with general availability:**

- **One price, full context window.** No long-context premium. 
- **Full rate limits at every context length.** Your standard account throughput applies across the entire window.
- **6x more media per request**. Up to 600 images or PDF pages, up from 100. Available today on Claude Platform natively, Microsoft Azure Foundry, and Google Cloud’s Vertex AI.
- ​​**No beta header required.** Requests over 200K tokens work automatically. If you're already sending the beta header, it's ignored so no code changes are required.

**1M context is now included in Claude Code for Max, Team, and Enterprise users with Opus 4.6.** Opus 4.6 sessions can use the full 1M context window automatically, meaning fewer compactions and more of the conversation kept intact. 1M context previously required extra usage.

### **Long context that holds up**

A million tokens of context only matters if the model can recall the right details and reason across them. Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length.

That means you can load an entire codebase, thousands of pages of contracts, or the full trace of a long-running agent — tool calls, observations, intermediate reasoning — and use it directly. The engineering work, lossy summarization, and context clearing that long-context work previously required are no longer needed. The full conversation stays intact.

Claude Code can burn 100K+ tokens searching Datadog, Braintrust, databases, and source code. Then compaction kicks in. Details vanish. You're debugging in circles. With 1M context, I search, re-search, aggregate edge cases, and propose fixes — all in one window.

Anton Biryukov, Software Engineer

Before Opus 4.6's 1M context window, we had to compact context as soon as users loaded large PDFs, datasets, or images — losing fidelity on exactly the work that mattered most. We've seen a 15% decrease in compaction events. Now our agents hold it all and run for hours without forgetting what they read on page one.

Jon Bell, CPO

Opus 4.6 with 1M context window made our Devin Review agent significantly more effective. Large diffs didn't fit in a 200K context window so the agent had to chunk context, leading to more passes and loss of cross-file dependencies. With 1M context, we feed the full diff and get higher-quality reviews out of a simpler, more token-efficient harness.

Adhyyan Sekhsaria, Founding Engineer

Eve defaults to 1M context because plaintiff attorneys' hardest problems demand it. Whether it's cross-referencing a 400-page deposition transcript or surfacing key connections across an entire case file, the expanded context window lets us deliver materially higher-quality answers than before.

Mauricio Wulfovich, ML Engineer

Scientific discovery requires reasoning across research literature, mathematical frameworks, databases, and simulation code simultaneously. Claude Opus 4.6’s 1M context and expanded media limits let our agentic systems synthesize hundreds of papers, proofs, and codebases in a single pass, helping us dramatically accelerate fundamental and applied physics research.

Dr. Alex Wissner-Gross, Co-Founder

With Claude's 1M context, an in-house lawyer can bring five turns of a 100-page partnership agreement into one session and finally see the full arc of a negotiation. No more toggling between versions or losing track of what changed three rounds ago.

Bardia Pourvakil, Co-founder and CTO

Large-scale production systems have endless context, and production incidents can get very complex. With Claude's 1M context window, we are able to keep every entity, signal, and working theory in view from first alert to remediation without having to repeatedly compact or compromise the nuances of these systems.

Mayank Agarwal, Founder & CTO

We raised our Opus context window from 200k to 500k and the agent runs more efficiently — it actually uses fewer tokens overall. Less overhead, more focus on the goal at hand.

Izzy Miller, AI Research Lead

Real-world spreadsheet tasks require deep research and complex multi-step plans. Claude's 1M context window let’s us maintain task adherence and attention to detail.

Tarun Amasa, CEO

[Prev](#)

Prev

0/5

[Next](#)

Next

eBook

## 

[](#)

### **Getting started**

1M context is available today on the Claude Platform natively and through Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry. Claude Code Max, Team, and Enterprise users on Opus 4.6 will default to 1M context automatically.

See our [documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [pricing](https://platform.claude.com/docs/en/about-claude/pricing) for details.

‍

FAQ

No items found.

[](#)

## Related posts

Explore more product news and best practices for teams building with Claude.

Mar 11, 2026

### Advancing Claude for Excel and PowerPoint

Enterprise AI

[Advancing Claude for Excel and PowerPoint](#)

Advancing Claude for Excel and PowerPoint

[Advancing Claude for Excel and PowerPoint](/blog/claude-excel-powerpoint-updates)

Advancing Claude for Excel and PowerPoint

Mar 12, 2026

### Claude now creates interactive charts, diagrams and visualizations

Product announcements

[Claude now creates interactive charts, diagrams and visualizations](#)

Claude now creates interactive charts, diagrams and visualizations

[Claude now creates interactive charts, diagrams and visualizations](/blog/claude-builds-visuals)

Claude now creates interactive charts, diagrams and visualizations

Feb 17, 2026

### Increase web search accuracy and efficiency with dynamic filtering

Product announcements

[Increase web search accuracy and efficiency with dynamic filtering](#)

Increase web search accuracy and efficiency with dynamic filtering

[Increase web search accuracy and efficiency with dynamic filtering](/blog/improved-web-search-with-dynamic-filtering)

Increase web search accuracy and efficiency with dynamic filtering

Mar 9, 2026

### Bringing Code Review to Claude Code

Claude Code

[Bringing Code Review to Claude Code](#)

Bringing Code Review to Claude Code

[Bringing Code Review to Claude Code](/blog/code-review)

Bringing Code Review to Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)

See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)

Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)

Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
