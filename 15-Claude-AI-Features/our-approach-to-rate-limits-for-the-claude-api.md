---
title: "Our approach to rate limits for the Claude API | Claude Help Center"
source_url: "https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api"
category: "15-Claude-AI-Features"
fetched_at: "2026-10-23T06:29:37Z"
tags: ["api", "claude-ai"]
---

# Our approach to rate limits for the Claude API


Your rate limit depends on your usage tier, and is currently measured in three key metrics:

1.  Requests per minute (RPM)

2.  Input tokens per minute (ITPM)

3.  Output tokens per minute (OTPM)

If you exceed any of these rate limits, you'll get a 429 error describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

Rate limits are set at the organization level and depend on your usage tier. There are three standard usage tiers: Start, Build, and Scale. New organizations and organizations with limited usage history may start in the Evaluation tier, with limits below the standard tiers while account history is established. Accounts whose limits are managed with their account team are on a separate Custom tier. Higher tiers have higher rate limits.

You can view your organization's current tier and limits in the **[Claude Console](../04-API-Reference/Other/playground.md)**. If you need higher limits, you can request them there once you're using at least 50% of your current limits.

For more about usage tiers and rate limits, see **[Rate limits](../04-API-Reference/Endpoints/rate-limits.md)** in Claude Platform Docs.
