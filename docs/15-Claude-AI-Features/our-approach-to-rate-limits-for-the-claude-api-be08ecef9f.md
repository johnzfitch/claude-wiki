---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api"
---


Your rate limit depends on your usage tier, and is currently measured in three key metrics:

Requests per minute (RPM)

Input tokens per minute (ITPM)

Output tokens per minute (OTPM)

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a retry-after header indicating how long to wait.

 

Rate limits are set at the organization level and are defined by usage tiers. Each tier has different spend and rate limits, with automatic tier advancement based on usage thresholds up to Tier 4.

 

You can view your organization's current tier and limits in the Claude Console.

 

More information on usage tiers and rate limits can be found in our Claude docs.

Related Articles
I’m encountering 429 errors, and I’m worried my rate limit is too low. What should I do?
Cost and Usage Reporting in the Claude Console
How can I advance my Claude API usage to Tier 2?
How am I billed for my Enterprise plan?
Extra usage for paid Claude plans