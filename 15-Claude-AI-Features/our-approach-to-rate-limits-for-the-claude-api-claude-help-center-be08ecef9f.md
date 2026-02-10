---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:52:08Z"
source_url: "https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api"
title: "Our approach to rate limits for the Claude API | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

[All Collections](/en/)

[Claude API and Console](https://support.claude.com/en/collections/5370014-claude-api-and-console)

[Claude API Usage and Best Practices](https://support.claude.com/en/collections/9811458-claude-api-usage-and-best-practices)

Our approach to rate limits for the Claude API

# Our approach to rate limits for the Claude API

Updated yesterday

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

[](https://support.claude.com/en/articles/8114527-i-m-encountering-429-errors-and-i-m-worried-my-rate-limit-is-too-low-what-should-i-do)

I’m encountering 429 errors, and I’m worried my rate limit is too low. What should I do?

[](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console)

Cost and Usage Reporting in the Claude Console

[](https://support.claude.com/en/articles/10366389-how-can-i-advance-my-claude-api-usage-to-tier-2)

How can I advance my Claude API usage to Tier 2?

[](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)

How am I billed for my Enterprise plan?

[](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)

Extra usage for paid Claude plans

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
