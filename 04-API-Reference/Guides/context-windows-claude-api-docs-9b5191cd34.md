---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:08Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/context-windows"
title: "Context windows - Claude API Docs"
---

Context management

# Context windows

Copy page

Copy page

As conversations grow, you'll eventually approach context window limits. This guide explains how context windows work and introduces strategies for managing them effectively.

For long-running conversations and agentic workflows, [server-side compaction](/docs/en/build-with-claude/compaction) is the primary strategy for context management. For more specialized needs, [context editing](/docs/en/build-with-claude/context-editing) offers additional strategies like tool result clearing and thinking block clearing.

## 

Understanding the context window

The "context window" refers to all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window allows the model to handle more complex and lengthy prompts. A smaller context window may limit the model's ability to maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests¹:

*¹For chat interfaces, such as for [claude.ai](https://claude.ai/), context windows can also be set up on a rolling "first in, first out" system.*

- **Progressive token accumulation:** As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
- **Linear growth pattern:** The context usage grows linearly with each turn, with previous turns preserved completely.
- **200K token capacity:** The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
- **Input-output flow:** Each turn consists of:
  - **Input phase:** Contains all previous conversation history plus the current user message
  - **Output phase:** Generates a text response that becomes part of a future input

## 

The context window with extended thinking

When using [extended thinking](/docs/en/build-with-claude/extended-thinking), all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits. With [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking), Claude dynamically decides its thinking allocation, so actual thinking token usage may vary per request.

However, previous thinking blocks are automatically stripped from the context window calculation by the Claude API and are not part of the conversation history that the model "sees" for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:

- **Stripping extended thinking:** Extended thinking blocks (shown in dark gray) are generated during each turn's output phase, **but are not carried forward as input tokens for subsequent turns**. You do not need to strip the thinking blocks yourself. The Claude API automatically does this for you if you pass them back.
- **Technical implementation details:**
  - The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
  - Extended thinking tokens are billed as output tokens only once, during their generation.
  - The effective context window calculation becomes: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
  - Thinking tokens include both `thinking` blocks and `redacted_thinking` blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

You can read more about the context window and extended thinking in the [extended thinking guide](/docs/en/build-with-claude/extended-thinking).

## 

The context window with extended thinking and tool use

The diagram below illustrates the context window token management when combining extended thinking with tool use:

1.  1

    First turn architecture

    - **Input components:** Tools configuration and user message
    - **Output components:** Extended thinking + text response + tool use request
    - **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.

2.  2

    Tool result handling (turn 2)

    - **Input components:** Every block in the first turn as well as the `tool_result`. The extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks.
    - **Output components:** After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next `user` message).
    - **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.

3.  3

    Third Step

    - **Input components:** All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next `User` turn.
    - **Output components:** Since there is a new `User` turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
    - **Token calculation:** Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current `Assistant` turn counts as part of the context window.

- **Considerations for tool use with extended thinking:**
  - When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
  - The effective context window calculation for extended thinking with tool use becomes: `context_window = input_tokens + current_turn_tokens`.
  - The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude's reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

Claude 4 models support [interleaved thinking](/docs/en/build-with-claude/extended-thinking#interleaved-thinking), which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

Claude Sonnet 3.7 does not support interleaved thinking, so there is no interleaving of extended thinking and tool calls without a non-`tool_result` user turn in between.

For more information about using tools with extended thinking, see the [extended thinking guide](/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use).

## 

1M token context window

Claude Opus 4.6, Sonnet 4.5, and Sonnet 4 support a 1-million token context window. This extended context window allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.

The 1M token context window is currently in beta for organizations in [usage tier](/docs/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Opus 4.6, Sonnet 4.5, and Sonnet 4.

To use the 1M token context window, include the `context-1m-2025-08-07` [beta header](/docs/en/api/beta-headers) in your API requests:

cURL

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: context-1m-2025-08-07" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Process this large document..."}
    ]
  }'
```

**Important considerations:**

- **Beta status:** This is a beta feature subject to change. Features and pricing may be modified or removed in future releases.
- **Usage tier requirement:** The 1M token context window is available to organizations in [usage tier](/docs/en/api/rate-limits) 4 and organizations with custom rate limits. Lower tier organizations must advance to usage tier 4 to access this feature.
- **Availability:** The 1M token context window is currently available on the Claude API, [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry), [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock), and [Google Cloud's Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai).
- **Pricing:** Requests exceeding 200K tokens are automatically charged at premium rates (2x input, 1.5x output pricing). See the [pricing documentation](/docs/en/about-claude/pricing#long-context-pricing) for details.
- **Rate limits:** Long context requests have dedicated rate limits. See the [rate limits documentation](/docs/en/api/rate-limits#long-context-rate-limits) for details.
- **Multimodal considerations:** When processing large numbers of images or pdfs, be aware that the files can vary in token usage. When pairing a large prompt with a large number of images, you may hit [request size limits](/docs/en/api/overview#request-size-limits).

## 

Context awareness in Claude Sonnet 4.5 and Haiku 4.5

Claude Sonnet 4.5 and Claude Haiku 4.5 feature **context awareness**. This capability lets these models track their remaining context window (i.e. "token budget") throughout a conversation. This enables Claude to execute tasks and manage context more effectively by understanding how much space it has to work. Claude is trained to use this context precisely, persisting in the task until the very end rather than guessing how many tokens remain. For a model, lacking context awareness is like competing in a cooking show without a clock. Claude 4.5 models change this by explicitly informing the model about its remaining context, so it can take maximum advantage of the available tokens.

**How it works:**

At the start of a conversation, Claude receives information about its total context window:

``` inline-block
<budget:token_budget>200000</budget:token_budget>
```

The budget is set to 200K tokens (standard), 500K tokens (claude.ai Enterprise), or 1M tokens (beta, for eligible organizations).

After each tool call, Claude receives an update on remaining capacity:

``` inline-block
<system_warning>Token usage: 35000/200000; 165000 remaining</system_warning>
```

This awareness helps Claude determine how much capacity remains for work and enables more effective execution on long-running tasks. Image tokens are included in these budgets.

**Benefits:**

Context awareness is particularly valuable for:

- Long-running agent sessions that require sustained focus
- Multi-context-window workflows where state transitions matter
- Complex tasks requiring careful token management

For prompting guidance on leveraging context awareness, see the [prompting best practices guide](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#context-awareness-and-multi-window-workflows).

## 

Managing context with compaction

If your conversations regularly approach context window limits, [server-side compaction](/docs/en/build-with-claude/compaction) is the recommended approach. Compaction provides server-side summarization that automatically condenses earlier parts of a conversation, enabling long-running conversations beyond context limits with minimal integration work. It is currently available in beta for Claude Opus 4.6.

For more specialized needs, [context editing](/docs/en/build-with-claude/context-editing) offers additional strategies:

- **Tool result clearing** - Clear old tool results in agentic workflows
- **Thinking block clearing** - Manage thinking blocks with extended thinking

## 

Context window management with newer Claude models

Newer Claude models (starting with Claude Sonnet 3.7) return a validation error when prompt and output tokens exceed the context window, rather than silently truncating. This change provides more predictable behavior but requires more careful token management.

Use the [token counting API](/docs/en/build-with-claude/token-counting) to estimate token usage before sending messages to Claude. This helps you plan and stay within context window limits.

See the [model comparison](/docs/en/about-claude/models/overview#latest-models-comparison) table for a list of context window sizes by model.

## 

Next steps

[](/docs/en/build-with-claude/compaction)

Compaction

The recommended strategy for managing context in long-running conversations.

[](/docs/en/build-with-claude/context-editing)

Context editing

Fine-grained strategies like tool result clearing and thinking block clearing.

[](/docs/en/about-claude/models/overview#latest-models-comparison)

Model comparison table

See the model comparison table for a list of context window sizes and input / output token pricing by model.

[](/docs/en/build-with-claude/extended-thinking)

Extended thinking overview

Learn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.

Was this page helpful?

- 

- [Understanding the context window](#understanding-the-context-window)

- [The context window with extended thinking](#the-context-window-with-extended-thinking)

- [The context window with extended thinking and tool use](#the-context-window-with-extended-thinking-and-tool-use)

- [1M token context window](#1-m-token-context-window)

- [Context awareness in Claude Sonnet 4.5 and Haiku 4.5](#context-awareness-in-claude-sonnet-4-5-and-haiku-4-5)

- [Managing context with compaction](#managing-context-with-compaction)

- [Context window management with newer Claude models](#context-window-management-with-newer-claude-models)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
