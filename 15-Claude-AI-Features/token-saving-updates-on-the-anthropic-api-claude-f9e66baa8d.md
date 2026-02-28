---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T00:42:48Z"
last_modified: "Fri, 27 Feb 2026 20:34:35 GMT"
source_url: "https://claude.com/blog/token-saving-updates"
title: "Token-saving updates on the Anthropic API | Claude"
---
# Token-saving updates on the Anthropic API

Claude now offers cache-aware rate limits, simplified prompt caching, and token-efficient tool use to help developers increase throughput and cut costs.

[](#)

[](#)

- 

  Category

  [Product announcements](https://claude.com/blog/category/announcements)

- 

  Product

  Claude Developer Platform

- 

  Date

  March 13, 2025

- 

  Reading time

  5

  min

- 

  Share

  [Copy link](#)
  https://claude.com/blog/token-saving-updates

We've made several updates to the Anthropic API that let developers significantly increase throughput and reduce token usage with Claude 3.7 Sonnet. These include: cache-aware rate limits, simpler prompt caching, and token-efficient tool use.

Together, these updates will help you process more requests within your existing rate limits and reduce costs with minimal code changes.

### Increase your throughput with prompt caching

[Prompt caching](https://www.anthropic.com/news/prompt-caching) allows developers to store and reuse frequently accessed context between API calls. This lets Claude maintain knowledge of large documents, instructions, or examples without sending the same information with each request—reducing costs by up to 90% and latency by up to 85% for long prompts. We’ve released two improvements to prompt caching for Claude 3.7 Sonnet that work together to help you scale more efficiently.

#### Cache-aware rate limits

Prompt cache read tokens no longer count against your Input Tokens Per Minute (ITPM) limit for Claude 3.7 Sonnet on the Anthropic API. This means you can now optimize your prompt caching usage to increase throughput and get more out of your existing ITPM rate limits. Your Output Tokens Per Minute (OTPM) rate limit remains the same.

This makes Claude 3.7 Sonnet particularly powerful for applications that benefit from extensive context while requiring high throughput, such as:

- Document analysis platforms that need to maintain large knowledge bases in context
- Coding assistants that reference extensive codebases
- Customer support systems that leverage detailed product documentation

[Cache-aware ITPM limits](https://docs.anthropic.com/en/api/rate-limits#rate-limits) are available for Claude 3.7 Sonnet on the Anthropic API.

#### Simpler cache management

We've updated prompt caching to be easier to use. Now, when you set a cache breakpoint, Claude automatically reads from your longest previously cached prefix.

You no longer need to manually track and specify which cached segments to use as we automatically identify and use the most relevant cached content. This not only reduces your workload, but also frees up more tokens.

This feature is available on the Anthropic API and Google Cloud’s Vertex AI. Explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) to learn more.

### Token-efficient tool use

Claude is already capable of interacting with external client-side tools and functions. This update lets you equip Claude with your own custom tools to perform tasks—like extracting structured data from unstructured text or automating simple tasks via APIs. Claude 3.7 Sonnet now supports [calling tools in a token-efficient manner](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/token-efficient-tool-use), reducing output token consumption by up to 70%. On average, early users have seen a reduction of 14%.

To use this feature, simply add the beta header *token-efficient-tools-2025-02-19* to a tool use request with Claude 3.7 Sonnet. If you are using the SDK, ensure that you are using the beta SDK with *anthropic.beta.messages*.

Token-efficient tool use is currently available in beta on the Anthropic API, Amazon Bedrock, and Google Cloud’s Vertex AI.

#### Text_editor tool

We also introduced a new *text_editor* tool, designed for applications where users collaborate with Claude on documents. With the new tool, Claude can make targeted edits to specific portions of text within source code, documents, or research reports. This reduces token consumption and latency, all while increasing accuracy.

Developers can easily implement this tool in their applications by providing it in their API requests and handling the tool use responses.

The *text_editor* tool is available on the Anthropic API, Amazon Bedrock, and Google Cloud's Vertex AI. See our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/text-editor-tool) to get started.

### Customer Spotlight: Cognition

Early users, like Cognition, are leveraging these updates to improve token efficiency and response quality. Cognition is an applied AI lab and the maker of Devin, a collaborative AI teammate that helps ambitious engineering teams achieve more.

“Prompt caching allows us to provide more context about the codebase to get higher quality results while reducing cost and latency. With cache-aware ITPM limits, we are further optimizing our prompt caching usage to increase our throughput and get more out of our existing rate limits,” said Scott Wu, Co-founder and CEO at Cognition.

### Get started now

These features are available today to all Anthropic API customers. You can implement them immediately with minimal code changes:

1.  **Take advantage of cache-aware rate limits:** Use [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) with Claude 3.7 Sonnet.
2.  **Implement token-efficient tool use:** Add the beta header *token-efficient-tools-2025-02-19* to your requests and start saving tokens.
3.  **Try the *text_editor* tool:** Integrate it into your applications for more efficient document editing workflows.

No items found.

[Prev](#)

Prev

0/5

[Next](#)

Next

eBook

## 

[](#)

FAQ

No items found.

[](#)

## Related posts

Explore more product news and best practices for teams building with Claude.

Jan 26, 2026

### Your favorite work tools are now interactive connectors inside Claude

Product announcements

[Your favorite work tools are now interactive connectors inside Claude](#)

Your favorite work tools are now interactive connectors inside Claude

[Your favorite work tools are now interactive connectors inside Claude](/blog/interactive-tools-in-claude)

Your favorite work tools are now interactive connectors inside Claude

Feb 20, 2026

### Bringing automated preview, review, and merge to Claude Code on desktop

Claude Code

[Bringing automated preview, review, and merge to Claude Code on desktop](#)

Bringing automated preview, review, and merge to Claude Code on desktop

[Bringing automated preview, review, and merge to Claude Code on desktop](/blog/preview-review-and-merge-with-claude-code)

Bringing automated preview, review, and merge to Claude Code on desktop

Feb 17, 2026

### Increase web search accuracy and efficiency with dynamic filtering

Product announcements

[Increase web search accuracy and efficiency with dynamic filtering](#)

Increase web search accuracy and efficiency with dynamic filtering

[Increase web search accuracy and efficiency with dynamic filtering](/blog/improved-web-search-with-dynamic-filtering)

Increase web search accuracy and efficiency with dynamic filtering

Jan 12, 2026

### Cowork: Claude Code for the rest of your work

Product announcements

[Cowork: Claude Code for the rest of your work](#)

Cowork: Claude Code for the rest of your work

[Cowork: Claude Code for the rest of your work](/blog/cowork-research-preview)

Cowork: Claude Code for the rest of your work

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
