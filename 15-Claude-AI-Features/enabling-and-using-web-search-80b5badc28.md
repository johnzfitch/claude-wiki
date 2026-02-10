---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/10684626-enabling-and-using-web-search"
---


You can have Claude search the internet to provide you with up-to-date information and insights when using the following models:

Opus 4.5

Haiku 4.5 

Sonnet 4.5

Sonnet 4

Web search expands Claude's knowledge with real-time data, helping you make better-informed decisions with current information.

To access this feature on a Team or Enterprise plan account:

An Owner or Primary Owner must first enable web search for the entire workspace. This can be found in Admin settings > Capabilities:

 

 

Once this is enabled at the workspace level, any member of the organization can switch it on while starting a chat by opening the “Search and tools” menu and toggling “Web search” on. Users can toggle this off for chats that don’t require web search capabilities.

 

How to enable web search in a chat

Click on the slider icon in your chat input interface.

Locate Web search in the dropdown.

Switch the toggle on.

You can disable the feature at any time by following the same steps and turning the toggle off.

 

How web search works

When you ask about topics that benefit from current information, Claude invokes a search tool to inform and ground its generated responses with content from the live web. Every response includes citations, so you can easily verify sources yourself.

 

During a search

When Claude searches the web:

You'll see an indicator that Claude is searching the web.

Claude processes multiple sources to find relevant content.

Claude provides a conversational response that includes:

Direct citations to sources

Source links for further reading

Relevant quotes when appropriate

 

Web fetch and direct links

When “Web search” is toggled on, Claude can also retrieve content directly from web pages when provided with specific URLs. This feature, called web fetch, allows Claude to access and analyze the full content of articles, blog posts, and other web pages you want to discuss.

Important note for free Claude accounts: When you provide Claude with a direct link to a long article or document and ask it to analyze or summarize the contents, the entire article is retrieved into Claude's context window. This can consume a significant portion of your usage capacity, especially for lengthy content. For example, asking Claude to summarize a 10,000-word article will use substantially more of your context window than a regular web search query.

 

Managing usage on free Claude accounts

As a free user, you have daily usage limits for Claude. Since web search and fetch both contribute to these limits, here are some tips to make the most of your capacity:

Be mindful of direct links: Before asking Claude to analyze a long article via its URL, consider whether you need the full analysis or just key points.

Toggle web search off when not needed: If you're having a conversation that doesn't require current information, disable web search to conserve your usage.

Use web search strategically: Focus on queries where up-to-date information is essential.

To disable web search and conserve your capacity:

Click on the slider icon in the lower left corner of your chat input.

Find Web search in the dropdown.

Toggle it off.

You can re-enable it anytime you need current information.

 

Tips for effective use

Ask about recent information: If you ask questions like "Are there any upcoming meteor showers?" or "What are the latest developments in quantum computing?", Claude will search the web for current data.

Specify in your prompt:

If you want to ensure that Claude uses web search, include "Search the web" or "Use web search" in your prompt to Claude.

You can also instruct Claude not to use web search in the prompt.

Request multiple sources: Claude can gather and synthesize information from various sources to give you a comprehensive view.

Verify important information: While Claude strives for accuracy:

Cross-reference cited sources to understand the full picture.

Use authoritative sources for critical decisions.

 

Limitations

Search availability may vary based on connectivity.

Occasionally, website links may not function.

Claude may use your location (inferred from your IP address) when responding to a request for localized results.

Search times may vary based on query complexity.

Usage of web search and web fetch counts toward your daily limits.

 

Support

For web search questions or support, please visit our Online Safety Contacts page.

For content removal requests, please visit our Blocking and Removing Content from Claude page.

Related Articles
How up-to-date is Claude's training data?
Claude Code Model Configuration
Release Notes
Getting the most out of Sonnet 4.5 in Claude.ai
Create professional results across tools with Claude Sonnet 4.5