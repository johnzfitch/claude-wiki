---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:17Z"
source_url: "https://support.claude.com/en/articles/10440198-custom-data-retention-controls-for-enterprise-plans"
title: "Custom Data Retention Controls for Enterprise Plans | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_b6421965c8)

[](#h_4ce44fc14b)

[](#h_9a7f8351d3)

[](#h_219c4bee62)

[](#h_219c4bee62)

[](#h_7f2562e784)

[](#h_744ab242dc)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Enterprise Plan](https://support.claude.com/en/collections/10351014-enterprise-plan)

Custom Data Retention Controls for Enterprise Plans

# Custom Data Retention Controls for Enterprise Plans

Updated this week

Table of contents

[](#h_b6421965c8)

[](#h_4ce44fc14b)

[](#h_9a7f8351d3)

[](#h_219c4bee62)

[](#h_219c4bee62)

[](#h_7f2562e784)

[](#h_744ab242dc)

This feature is available to Enterprise plan customers. To set custom retention periods for your organization, you must have either a Primary Owner or Owner role.

*This article is about our commercial products such as Claude for Work and the Anthropic API. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see [here](https://privacy.claude.com/en/collections/10663362-consumers).*

Custom data retention controls allow organizations to manage how long Claude stores conversation and project data. This article explains how to set up and manage data retention periods for your organization.

## How data retention works

Data retention is based on the last observed activity:

- **For chats:** Retention period starts from the time of the last message in the conversation.

- **For projects:** Retention period starts from the time the project was last updated (this includes chat creation or project knowledge base modifications).

  - Note that your custom data retention periods set for projects will supersede your custom retention periods for any chats.

The minimum retention period is 30 days, and each month is counted as 30 days. For example, a three-month retention period equals 90 days.

## What gets deleted

When data reaches the end of its retention period:

- **For chats:** All chats (including chats within projects) and any artifacts within those chats will be deleted.

- **For projects:** All projects will be deleted, including any chats and artifacts within those projects.

## Important considerations

- Deletion occurs at midnight UTC on the scheduled day.

- By default, data is retained indefinitely unless a custom retention period is set.

- When you modify retention settings, any data that falls outside the new retention period will be deleted immediately upon saving.

- Data past its retention period will be permanently deleted and cannot be recovered.

## Setting up data retention

## To set custom retention periods:

1.  Log in to your Owner Enterprise plan account.

2.  Navigate to [Admin settings \> Data and Privacy](https://claude.ai/admin-settings/data-privacy-controls).

3.  Set your desired retention period (minimum 30 days).

4.  Save your changes.

## Example retention calculation

If a conversation’s last message is at 3PM UTC on March 1 with a 30-day retention period, the deletion will occur at midnight UTC on March 31.

## Monitoring retention-related activities

All retention-related actions and changes are automatically tracked in [audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs). You can access these logs to monitor changes to retention settings and data deletion events.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans)

Can you delete data that I sent via Team and Enterprise plans?

[](https://support.claude.com/en/articles/11088779-using-google-drive-cataloging-on-the-enterprise-plan)

Using Google Drive Cataloging on the Enterprise Plan

[](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)

Using Claude’s chat search and memory to build on previous context

[](https://support.claude.com/en/articles/12260368-using-incognito-chats)

Using incognito chats

[](https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans)

Usage Analytics for Team and Enterprise Plans

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
