---
title: "Our approach to rate limits for the Claude API | Claude Help Center"
source_url: "https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:32:32Z"
tags: ["api", "claude-ai"]
---

# Our approach to rate limits for the Claude API

June 26, 2026


Your rate limit depends on your usage tier, and is currently measured in three key metrics:

1.  Requests per minute (RPM)

2.  Input tokens per minute (ITPM)

3.  Output tokens per minute (OTPM)

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

Rate limits are set at the organization level and depend on your usage tier. There are three usage tiers: Start, Build, and Scale. Accounts whose limits are managed with their account team are on a separate Custom tier. Higher tiers have higher rate limits.

You can view your organization's current tier and limits in the **[Claude Console](../04-API-Reference/Other/usage-limits.md)**. If you need higher limits, you can request them there once you're using at least 50% of your current limits.

For more about usage tiers and rate limits, see the **[Rate limits page in our Claude Platform Docs](https://docs.claude.com/en/api/rate-limits)**.
