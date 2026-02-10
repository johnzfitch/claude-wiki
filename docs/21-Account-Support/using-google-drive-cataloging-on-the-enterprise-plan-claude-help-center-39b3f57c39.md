---
category: "21-Account-Support"
fetched_at: "2026-02-10T10:49:18Z"
source_url: "https://support.claude.com/en/articles/11088779-using-google-drive-cataloging-on-the-enterprise-plan"
title: "Using Google Drive Cataloging on the Enterprise Plan | Claude Help Center"
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

[](#h_e5ae69458d)

[](#h_66e966a800)

[](#h_11ee27e0f2)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Enterprise Plan](https://support.claude.com/en/collections/10351014-enterprise-plan)

Using Google Drive Cataloging on the Enterprise Plan

# Using Google Drive Cataloging on the Enterprise Plan

Updated this week

Table of contents

[](#h_e5ae69458d)

[](#h_66e966a800)

[](#h_11ee27e0f2)

Google Drive Cataloging is available to users on the Claude Enterprise plan.

Enterprise users can catalog their Google Drive content\* with RAG (Retrieval Augmented Generation) Search. This system works by first indexing the content of your Google Drive, and then using that index to match queries to results. With this setting enabled, Claude will provide accurate contextual responses based on your indexed documents, and will provide direct citations to the relevant sources.

*\*Supported file types:* Google Docs (text extraction only, up to 10MB).

## Enabling Google Drive Cataloging

Before individual users can start using indexed content from their Drive, an Owner or Primary Owner must enable the feature at the account level. To enable:

1.  Navigate to [Settings \> Integrations](https://claude.ai/settings/integrations)

2.  Toggle to “Organization integrations” at the top of the page

3.  Locate “Google Drive cataloging”

4.  Click Enable and follow the instructions to authenticate

**For Individual Users:**

Once the global setting has been turned on, individual users can toggle Google Drive search on from the chat interface:

1.  Click on the slider icon in the chat interface

2.  Toggle “Drive search” on

    - *Note:* If this is your first time using the integration, you will be redirected to Google to authenticate

## After Enabling

Once enabled, Claude will index your Google Docs and leverage that index during your conversations to provide relevant context and citations in his responses.

Periodically Claude will re-index documents that have changed and de-index documents that have been deleted. It may take several hours for Claude to recognize that a document has been updated or deleted.

## Privacy & Security

This infrastructure builds upon and augments the Claude for Work security infrastructure:

- Data retrieved while using integrations is stored in Anthropic servers, which is protected by Anthropic's security infrastructure (see more details in our [Trust Center](https://trust.anthropic.com/controls#organizational-security)). This data is retained with its associated chat, so you can delete any retrieved data by deleting the chat.

- Data is encrypted at rest and in transit using Google’s managed encryption services

- Each user has access to their protected index:

  - This index fully respects access controls and underlying user level permissions

  - Each user can only access their own index

- All document edits, deletions, and access changes are propagated promptly

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)

What is the Enterprise plan?

[](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration)

Using the Google Drive integration

[](https://support.claude.com/en/articles/11088742-using-the-gmail-and-google-calendar-integrations)

Using the Gmail and Google Calendar Integrations

[](https://support.claude.com/en/articles/11139094-getting-started-with-claude-for-education-at-your-university-for-owners-admins)

Getting Started with Claude for Education at Your University (for Owners/Admins)

[](https://support.claude.com/en/articles/12489464-using-enterprise-search)

Using Enterprise Search

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
