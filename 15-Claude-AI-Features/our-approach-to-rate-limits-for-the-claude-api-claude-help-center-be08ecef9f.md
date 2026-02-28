---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T11:22:20Z"
source_url: "https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api"
title: "Our approach to rate limits for the Claude API | Claude Help Center"
---

4.  Our approach to rate limits for the Claude API

# Our approach to rate limits for the Claude API


Your rate limit depends on your usage tier, and is currently measured in three key metrics:

1.  Requests per minute (RPM)

2.  Input tokens per minute (ITPM)

3.  Output tokens per minute (OTPM)

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

Rate limits are set at the organization level and are defined by usage tiers. Each tier has different spend and rate limits, with automatic tier advancement based on usage thresholds up to Tier 4.

You can view your organization's current tier and limits in the [Claude Console](https://platform.claude.com).

More information on usage tiers and rate limits can be found in [our Claude docs](https://docs.claude.com/en/api/rate-limits).

------------------------------------------------------------------------

Related Articles


I’m encountering 429 errors, and I’m worried my rate limit is too low. What should I do?


Cost and Usage Reporting in the Claude Console


How can I advance my Claude API usage to Tier 2?


Extra usage for paid Claude plans


Claude Enterprise Analytics API reference guide
