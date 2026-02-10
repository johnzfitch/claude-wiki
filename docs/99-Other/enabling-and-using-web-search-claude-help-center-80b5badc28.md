---
category: "99-Other"
fetched_at: "2026-02-10T10:49:18Z"
source_url: "https://support.claude.com/en/articles/10684626-enabling-and-using-web-search"
title: "Enabling and using web search | Claude Help Center"
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

[](#h_cf313cf6d7)

[](#h_24335cf586)

[](#h_1c190557d2)

[](#h_72e7287264)

[](#h_82182dd649)

[](#h_fa92937b2c)

[](#h_340f79ae09)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

Enabling and using web search

# Enabling and using web search

Updated this week

Table of contents

[](#h_cf313cf6d7)

[](#h_24335cf586)

[](#h_1c190557d2)

[](#h_72e7287264)

[](#h_82182dd649)

[](#h_fa92937b2c)

[](#h_340f79ae09)

You can have Claude search the internet to provide you with up-to-date information and insights when using the following models:

- Opus 4.6

- Opus 4.5

- Haiku 4.5

- Sonnet 4.5

- Sonnet 4

Web search expands Claude's knowledge with real-time data, helping you make better-informed decisions with current information.

**To access this feature on a Team or Enterprise plan account:**

An Owner or Primary Owner must first enable web search for the entire workspace. This can be found in **[Admin settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/2032032614/ad907328c4d9a26ee4bd9ca27a52/CleanShot+2026-02-05+at+09_01_42%402x.png?expires=1770722100&signature=667e7b7e5cdd8a20b45830d994f34e39925d18913ed31f6a9f493b86ebd4f706&req=diAkFMl9n4deXfMW1HO4zetvxbK9GsxRUJIbgsqS2%2BMeLhT43u1hUS79YpvZ%0AKwcyvbq51nfJSv70k5c%3D%0A)

Once this is enabled at the workspace level, any member of the organization can switch it on while starting a chat by clicking the “+” button in the lower left corner of the chat window and selecting “Web search." Users can toggle this off for chats that don’t require web search capabilities.

## How to enable web search in a chat

1.  Click on the slider icon in your chat input interface.

2.  Locate **Web search** in the dropdown.

3.  Switch the toggle on.

You can disable the feature at any time by following the same steps and turning the toggle off.

## How web search works

When you ask about topics that benefit from current information, Claude invokes a search tool to inform and ground its generated responses with content from the live web. Every response includes citations, so you can easily verify sources yourself.

### During a search

When Claude searches the web:

1.  You'll see an indicator that Claude is searching the web.

2.  Claude processes multiple sources to find relevant content.

3.  Claude provides a conversational response that includes:

    - Direct citations to sources

    - Source links for further reading

    - Relevant quotes when appropriate

### Web fetch and direct links

When “Web search” is toggled on, Claude can also retrieve content directly from web pages when provided with specific URLs. This feature, called web fetch, allows Claude to access and analyze the full content of articles, blog posts, and other web pages you want to discuss.

**Important note for free Claude accounts:** When you provide Claude with a direct link to a long article or document and ask it to analyze or summarize the contents, the entire article is retrieved into Claude's context window. This can consume a significant portion of your usage capacity, especially for lengthy content. For example, asking Claude to summarize a 10,000-word article will use substantially more of your context window than a regular web search query.

## Image results

When web search is enabled, Claude can also search for and display images directly in your conversation. You don't need to enable a separate setting — image results are part of web search.

For example, you might ask Claude to:

- Show you what a recipe looks like before you start cooking

- Find photos of a product you're considering

- Help identify a plant, insect, or object by searching for visual matches

- Compare what similar items look like side by side

Claude selects images from web search results, powered by Bing, and displays them alongside its text response. Each image includes a source link so you can visit the original page for more details.

Image search is powered by Bing ([https://www.microsoft.com/en-us/privacy/privacystatement](https://www.microsoft.com/en-us/privacy/privacystatement)).

Claude can also display interactive content in search results. For more detailed information, see here: **[Visual and interactive content](https://support.claude.com/en/articles/13641943-visual-responses-and-interactive-widgets)**.

## Managing usage on free Claude accounts

As a free user, you have daily usage limits for Claude. Since web search and fetch both contribute to these limits, here are some tips to make the most of your capacity:

- **Be mindful of direct links:** Before asking Claude to analyze a long article via its URL, consider whether you need the full analysis or just key points.

- **Toggle web search off when not needed:** If you're having a conversation that doesn't require current information, disable web search to conserve your usage.

- **Use web search strategically:** Focus on queries where up-to-date information is essential.

To disable web search and conserve your capacity:

1.  Click on the slider icon in the lower left corner of your chat input.

2.  Find **Web search** in the dropdown.

3.  Toggle it off.

You can re-enable it anytime you need current information.

## Tips for effective use

1.  **Ask about recent information**: If you ask questions like "Are there any upcoming meteor showers?" or "What are the latest developments in quantum computing?", Claude will search the web for current data.

2.  **Specify in your prompt:**

    - If you want to ensure that Claude uses web search, include "Search the web" or "Use web search" in your prompt to Claude.

    - You can also instruct Claude not to use web search in the prompt.

3.  **Request multiple sources**: Claude can gather and synthesize information from various sources to give you a comprehensive view.

4.  **Verify important information**: While Claude strives for accuracy:

    - Cross-reference cited sources to understand the full picture.

    - Use authoritative sources for critical decisions.

## Limitations

- Search availability may vary based on connectivity.

- Occasionally, website links may not function.

- Claude may use your location (inferred from your IP address) when responding to a request for localized results.

- Search times may vary based on query complexity.

- Usage of web search and web fetch counts toward your daily limits.

## Support

- For web search questions or support, please visit our **[Online Safety Contacts](https://support.claude.com/en/articles/11174660-online-safety-contacts)** page.

- For content removal requests, please visit our **[Blocking and Removing Content from Claude](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)** page.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)

How up-to-date is Claude's training data?

[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)

Claude Code model configuration

[](https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes)

Claude in Chrome Release Notes

[](https://support.claude.com/en/articles/12439373-getting-the-most-out-of-sonnet-4-5-in-claude-ai)

Getting the most out of Sonnet 4.5 in Claude.ai

[](https://support.claude.com/en/articles/12439380-create-professional-results-across-tools-with-claude-sonnet-4-5)

Create professional results across tools with Claude Sonnet 4.5

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
