---
title: "Migrating to Claude Fable 5.1 and Claude Mythos 5.1 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5-1/migration-guide"
category: "20-Models"
fetched_at: "2026-09-26T06:39:44Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5-1%2Fmigration-guide)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Overview](models-fable-5-1-overview.md)[What's new](models-fable-5-1-whats-new-fable-5-1.md)[Migration guide](models-fable-5-1-migration-guide.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Fable 5.1

# Migrating to Claude Fable 5.1 and Claude Mythos 5.1

Copy page



Migrate to Claude Fable 5.1 and Claude Mythos 5.1 from Claude Fable 5, Claude Mythos 5, Claude Opus 5, or Claude Opus 4.8: model IDs, breaking changes, and migration checklists.

Copy page





This guide covers migrating [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) code. If you use [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-fable-5-1
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

[Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md) succeeds Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost. It's available on the Claude API, [Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md). [Claude Mythos 5.1](../22-Safety-Policy/glasswing.md) shares the same capabilities and is offered only to approved customers in Project Glasswing. For behavioral differences and prompting patterns, see [Prompting Claude Fable 5.1](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md).

The baseline settings shared by `claude-fable-5-1` and `claude-mythos-5-1`:

- **Thinking:** [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on, unchanged from Claude Fable 5. The model decides when and how much to think. No `thinking` configuration is required. Both `thinking: {type: "disabled"}` and manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) return a 400 error.
- **Prefill:** Prefilling the assistant message returns a 400 error, unchanged from Claude Fable 5. Use system prompt instructions instead.
- **Tool choice:** `{type: "auto"}` (the default) and `{type: "none"}` are supported. Forcing a tool call with `{type: "any"}` or `{type: "tool", name: "..."}` returns a 400 error. See [Breaking changes](#fable-5-1-breaking-changes).
- **Preserved thinking across models:** Claude Fable 5.1 reads thinking blocks from Claude Opus 5, Claude Fable 5, Claude Mythos 5, and earlier Claude models. None of those models can read Claude Fable 5.1's blocks. See [Breaking changes](#fable-5-1-breaking-changes).
- **Context window and output:** A [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, and up to 128k output tokens per request.
- **Pricing:** \$10 USD per million input tokens and \$50 USD per million output tokens, the same as Claude Fable 5. Prompt cache reads are \$0.25 USD per million tokens, a quarter of the Claude Fable 5 rate. See [Claude pricing](../17-Billing-Plans/about-claude-pricing.md).
- **Data retention:** Both models require 30-day data retention, aren't available under zero data retention (ZDR) arrangements unless expressly authorized by Anthropic, and are designated Covered Models, the same as Claude Fable 5 and Claude Mythos 5. On the Claude API, a request from an organization or workspace without 30-day retention returns a 400 `invalid_request_error`. Organizations with a ZDR arrangement should contact their Anthropic account team, or configure retention per workspace. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements) for per-platform details.

Where the two models diverge:

- **Availability:** Claude Fable 5.1 doesn't require access approval. Claude Mythos 5.1 is available only to approved customers in [Project Glasswing](../22-Safety-Policy/glasswing.md). Contact your Anthropic account team for access.
- **Safety classifiers:** Claude Fable 5.1 runs safety classifiers covering the same `stop_details` categories as Claude Fable 5. A declined request returns `stop_reason: "refusal"` with a `stop_details.category`, and can fall back to another model with the `fallbacks` parameter or a client-side retry. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- **Priority Tier:** Neither model is supported on [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models). Claude Fable 5 is.

## Migrating to Claude Fable 5.1 from Claude Fable 5

Migration is mostly drop-in. The API surface, limits, per-token pricing, tokenizer, always-on adaptive thinking, refusal handling, and `stop_details` categories all match Claude Fable 5. What changes: forced tool choice returns a 400 error, thinking blocks are preserved only for the model that produced them or a newer one and only in the conversation that produced them, cache reads cost less, and agent-loop behavior differs in three ways. The same changes apply to [Claude Mythos 5.1](#migrating-from-claude-mythos-5-to-claude-mythos-5-1), except the conversation check on thinking blocks, which Claude Mythos 5.1 doesn't run.

### Update your model name

```python
model = "claude-fable-5"  # Before
model = "claude-fable-5-1"  # After

# Or, for the Project Glasswing model with the same capabilities:
model = "claude-mythos-5-1"  # After
```



### Breaking changes

1.  **Forced tool choice is not supported:** Claude Fable 5 accepts `tool_choice` `auto`, `none`, `any`, and `tool`. On `claude-fable-5-1`, `{type: "any"}` and `{type: "tool", name: "..."}` return a 400 `invalid_request_error`:

    ``` block
    tool_choice: type "tool" and "any" are not supported for this model.
    ```

    

    The check applies on the Messages API, the Message Batches API, and the [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) endpoint.

    Before (Claude Fable 5):

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    record_summary_tool = {
        "name": "record_summary",
        "description": "Record the structured summary of the document.",
        "input_schema": {
            "type": "object",
            "properties": {"summary": {"type": "string"}},
            "required": ["summary"],
        },
    }

    response = client.messages.create(
        model="claude-fable-5",
        max_tokens=16000,
        tools=[record_summary_tool],
        tool_choice={"type": "tool", "name": "record_summary"},
        messages=[{"role": "user", "content": "Summarize: The meeting moved to Thursday."}],
    )
    print(response.content)
    ```

    After (Claude Fable 5.1): leave `tool_choice` at `auto`, name the tool in the instruction, and set `strict: true` so the call matches your schema. (In a [CMEK](../04-API-Reference/Other/manage-claude-cmek.md) organization, where [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md), including `strict: true`, are not available on Claude Fable models, rely on the instruction alone.) For example:

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    record_summary_tool = {
        "name": "record_summary",
        "description": "Record the structured summary of the document.",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {"summary": {"type": "string"}},
            "required": ["summary"],
            "additionalProperties": False,
        },
    }

    response = client.messages.create(
        model="claude-fable-5-1",
        max_tokens=16000,
        tools=[record_summary_tool],
        tool_choice={"type": "auto"},
        messages=[
            {
                "role": "user",
                "content": "Summarize: The meeting moved to Thursday. Call the record_summary tool with your result.",
            }
        ],
    )
    print(response.content)
    ```

    See [Strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md) and [Forcing tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md#forcing-tool-use). If you forced a tool only to get schema-conformant JSON, use [JSON outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md#json-outputs) (`output_config.format`) instead.

    If your application, rather than the user, requires a specific tool call on the current turn of a multi-turn conversation, append a [mid-conversation system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) after the latest `user` turn. Name the tool, say the call is required for this turn, and tell Claude to open its response with it. Because the message is appended rather than written into the top-level `system` prompt, earlier turns stay byte-identical and keep their [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits:

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    search_help_center_tool = {
        "name": "search_help_center",
        "description": "Search the help center for policy and troubleshooting articles.",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
            "additionalProperties": False,
        },
    }

    response = client.messages.create(
        model="claude-fable-5-1",
        max_tokens=16000,
        system="You are a customer support assistant for an online electronics store.",
        tools=[search_help_center_tool],
        messages=[
            {
                "role": "user",
                "content": "My headphones from order A1234 arrived yesterday.",
            },
            {
                "role": "assistant",
                "content": "Thanks for confirming. How can I help with order A1234?",
            },
            {"role": "user", "content": "I opened the box. Can I still return them?"},
            # The application requires a help center lookup before any policy
            # answer. Appending the requirement as a system message leaves the
            # earlier turns unchanged.
            {
                "role": "system",
                "content": "Tool-use requirement for the current turn: the application requires a call to the search_help_center tool in your response to the user's latest message. Begin your response with the search_help_center tool call. Do not reply with text only.",
            },
        ],
    )
    print(response.content)
    ```

    Keep the `role: "system"` message in the history on later requests, as with any other turn. Mid-conversation system messages need no beta header. `tool_choice: {"type": "none"}` still works for a turn that must not call tools.

2.  **Thinking blocks are preserved only for the model that produced them, or a newer one:** Every `thinking` block records which model produced it. Claude Fable 5.1 reads its own blocks and those from Claude Mythos 5.1, Claude Opus 5, Claude Fable 5, Claude Mythos 5, and earlier Claude models. A conversation moving onto `claude-fable-5-1` from any of those keeps its earlier reasoning. The condition is one-way: apart from Claude Mythos 5.1, none of those models can read Claude Fable 5.1's blocks.

    A conversation that ran on Claude Fable 5.1 can land on an older model through a router switch, a client-side retry, or a [classifier refusal fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md), including a [server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback). The API removes the blocks that model can't read before it sees them, the request succeeds, and you aren't billed for the dropped input tokens. The target model re-plans without that reasoning, which can raise cost and latency on the first turn after the switch. To see what was dropped, send the `thinking-binding-controls-2026-08-01` [beta header](../04-API-Reference/Endpoints/beta-headers.md): responses then carry an `input_transformations` array naming each dropped block with `reason: "model_binding_mismatch"`. See [Switching models mid-conversation](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models).

3.  **Editing earlier turns invalidates thinking blocks:** Each `thinking` block from Claude Fable 5.1 is valid only against the `system` prompt, `tools`, and conversation history that preceded it. If Claude Code, claude.ai, [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), or the [Claude Agent SDK](https://platform.claude.com/docs/en/models/09-Agents-Patterns/agent-sdk-overview-b27888bae2.md) manages your conversation history, it already keeps that prefix intact. If your code builds the `messages` array itself, this item applies to you, and [Preserved thinking](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md) is the full integration guide. Where the check is enforced, a request that sends the block back after any of those changed is rejected with a 400 error:

    ``` shiki
    messages.5.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block". That setting requires the `thinking-binding-controls-2026-08-01` value in the `anthropic-beta` header.
    ```

    

    The API enforces the check for new accounts created on or after August 31, 2026. For accounts created earlier, the API records the mismatch but doesn't act on it unless the request sets `thinking.block_binding.prefix_mismatch_behavior`, which opts into enforcement. On those accounts, if you send the `thinking-binding-controls-2026-08-01` beta header and leave that field unset, the response lists each block that failed the check in `input_transformations` as a `thinking_mismatch_allowed` entry. Make your application compatible with the check regardless of your account's age: the same patterns keep the prompt cache warm, and you can test against the check from any account by sending `prefix_mismatch_behavior`. If you ship a tool or framework that people run with their own API key, test that way before launch: your key is probably on an older account, and your users on new ones hit the check before you do. To see whether your own account is enforced by default, send a request that edits history without the beta header: a 400 that names the header means it is.

    The error is permanent for that request body: an automatic retry loop won't clear it. To continue without the invalidated reasoning instead of failing, strip the `thinking` blocks from the history and retry once, or send the `thinking-binding-controls-2026-08-01` [beta header](../04-API-Reference/Endpoints/beta-headers.md) and set `prefix_mismatch_behavior` to `"drop_block"` (the default is `"error"`). With `"drop_block"`, the API drops the mismatched block and every thinking block after it in the conversation, and reports each with `reason: "prefix_binding_mismatch"` in the response's `input_transformations` array:

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    response = client.beta.messages.create(
        model="claude-fable-5-1",
        max_tokens=16000,
        thinking={
            "type": "adaptive",
            "block_binding": {"prefix_mismatch_behavior": "drop_block"},
        },
        messages=[
            {
                "role": "user",
                "content": "What is the greatest common divisor of 1071 and 462?",
            }
        ],
        betas=["thinking-binding-controls-2026-08-01"],
    )

    for block in response.content:
        if block.type == "text":
            print(block.text)

    print(f"Input transformations: {len(response.input_transformations or [])}")
    ```

    The [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) endpoint runs the same check. See [Controls for blocks that aren't preserved (beta)](../04-API-Reference/Guides/build-with-claude-thinking.md#preserved-thinking-controls) for the response shape and streaming placement.

    Patterns that invalidate later thinking blocks, and what to do instead:

    - Editing, reordering, or removing earlier turns. This includes deleting old tool results, snipping turns out of the middle of the transcript, and client-side compaction that keeps recent turns and their thinking blocks verbatim behind a summary (including background compaction that swaps its summary in a few turns later). Instead, use server-side [compaction](../04-API-Reference/Guides/build-with-claude-compaction.md) or [context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md) ([tool result clearing](../04-API-Reference/Guides/build-with-claude-context-editing.md#tool-result-clearing) for old tool results), or one of the client-side compaction shapes in [Trim context on the server](#fable-5-1-trim-context).
    - Injecting content you don't persist, for example a per-turn reminder appended after the `tool_result` blocks and removed on the next request. Instead, send the reminder as a [turn-scoped system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#turn-scoped-system-messages) and leave it in the history.
    - Rebuilding the top-level `system` prompt or the `tools` array between requests in the same conversation, for example to update the current date or to add or remove a tool. Instead, append a [mid-conversation system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) that carries the new instruction ("The current date is 2026-09-14.") or `tool_addition` and `tool_removal` blocks. A tool that wasn't declared in `tools` at the start can be [defined inside the `tool_addition` block](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta) (beta header `inline-tools-2026-09-15`).
    - An image or document URL that serves different bytes on a later request. The check covers the bytes, not the URL string, so a rotating signed URL for the same file is fine. For content you reference across turns, upload it once with the [Files API](../04-API-Reference/Guides/build-with-claude-files.md) and send the `file_id`, or send base64.

    Each replacement also keeps earlier turns byte-identical and preserves the [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits that editing the history, `system` prompt, or `tools` array would lose.

    Patterns that keep working:

    - Append-only histories: adding turns and passing earlier turns back exactly as sent and received, including appended `role: "system"` messages.
    - Removing thinking blocks from earlier assistant turns, oldest first.
    - Changing `effort`, `max_tokens`, or any other request parameter outside `system`, `tools`, and `messages`, and adding or moving `cache_control` markers.
    - Server-side compaction and context editing, including [thinking block clearing](../04-API-Reference/Guides/build-with-claude-context-editing.md#thinking-block-clearing). They don't count as edits, because the check compares the conversation as you sent it.

    To check an existing integration:

    1.  Capture the exact request bodies it sends over a few normal turns, including a compaction or a tool change if your product has them. For each pair of consecutive requests, compare the `system` prompt, the `tools` array, and the shared prefix of `messages`. They should be byte-identical up to the newly appended turns. An expected exception is a request that swaps in a signed `compaction` block from [on-demand compaction](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md): the block replaces the messages it summarizes at the front of `messages`, and everything after it should still match.
    2.  Run a normal multi-turn session against `claude-fable-5-1` with the `thinking-binding-controls-2026-08-01` beta header and `prefix_mismatch_behavior: "drop_block"`, and log `input_transformations` on every response. An empty array on every turn means the history is intact. An entry with `reason: "prefix_binding_mismatch"` means something before the block at `path` changed since the previous request. An entry with `reason: "model_binding_mismatch"` means the conversation switched models, which isn't a bug in your code. This works from any account, because setting the field opts the request into enforcement. In CI, set `"error"` instead so an edit fails the run.
    3.  Choose a production setting. Leave the default `"error"` if a prefix mismatch can only mean a bug in your code, or set `"drop_block"` to drop the affected blocks instead of failing, and monitor the 400s or the `input_transformations` entries either way.

    Dropping thinking blocks once, at a compaction boundary for example, has little effect. An integration that invalidates prior thinking on every request restarts the prompt cache each time, which can raise cost per task (see [Keep the conversation history append-only](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#keep-the-conversation-history-append-only)).

### Behavior changes

1.  **Fewer parallel tool calls in long agent loops:** In long-running loops where the next independent reads are only implied by the task (custom coding agents, bash-and-editor harnesses, computer use), Claude Fable 5.1 may issue one tool call per turn. Each extra turn costs tokens, a round trip, and wall-clock time. Append a one-sentence batching instruction after each user message as a [turn-scoped system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#turn-scoped-system-messages) (`clear_at: "next_user_message"`, beta), or, without the beta, in a text block after the `tool_result` blocks, and leave the earlier copies in the history on later requests. See [Batch independent tool calls in agent loops](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#batch-independent-tool-calls-in-agent-loops).

2.  **Fewer progress messages between tool calls:** Claude Fable 5.1 writes fewer status updates during long tool sequences than Claude Fable 5, and its agentic coding summaries are shorter. If your interface renders those updates, set `thinking.display` to `"updates"` (beta) or `"summarized"` and prompt for them explicitly. See [Progress updates between tool calls](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates) and [Ask for user-facing progress updates](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#ask-for-user-facing-progress-updates).

3.  **Fewer search and retrieval calls at low effort:** At `low` effort Claude Fable 5.1 answers from memory more often than Claude Fable 5 instead of calling a search or retrieval tool. If your product relies on retrieval at low effort, raise effort for those requests or tell the model when to search. See [Search triggering at low effort](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#search-triggering-at-low-effort).

For the differences in prose density, chat formatting, quoting in summaries, and file edits, which don't affect API integration, see [Changed from Claude Fable 5](models-fable-5-1-whats-new-fable-5-1.md#changed-from-claude-fable-5).

### Recommended changes

These changes aren't required, but each one lowers cost or latency or removes a failure mode:

1.  **Change effort mid-conversation (beta):** On Claude Fable 5, `output_config.effort` is request-level, and changing it between requests drops cached prefixes from earlier turns. On `claude-fable-5-1`, a `role: "system"` message carrying only `output_config` raises effort for a hard step or lowers it for routine ones without invalidating the [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md):

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    client = anthropic.Anthropic()

    response = client.beta.messages.create(
        model="claude-fable-5-1",
        max_tokens=4096,
        output_config={"effort": "high"},
        messages=[
            {
                "role": "user",
                "content": "Plan a migration from SQLite to PostgreSQL in three short steps.",
            },
            {
                "role": "assistant",
                "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.",
            },
            # Effort-only system message: the new level takes effect from the next user turn.
            {"role": "system", "content": [], "output_config": {"effort": "low"}},
            {"role": "user", "content": "Summarize the plan in one sentence."},
        ],
        betas=["mid-conversation-output-config-2026-07-01"],
    )

    for block in response.content:
        if block.type == "text":
            print(block.text)
    ```

    The value applies to the following user turn and every later turn until another `role: "system"` message changes it. Only the named levels are accepted (`low`, `medium`, `high`, `xhigh`, `max`), and the `mid-conversation-output-config-2026-07-01` beta header is required. See [Per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta).

2.  **Change instructions and tools with mid-conversation system messages:** To change instructions or tools partway through a session, append a [`role: "system"` message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md), with `tool_addition` and `tool_removal` blocks for tool changes (beta header `inline-tools-2026-09-15` on the Claude API). A `tool_addition` block can name a tool declared in `tools` at session start or [carry the tool's full definition](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta), so a tool that is unknown at session start doesn't need to be in `tools`. This preserves prompt cache hits on earlier turns and keeps the conversation history append-only. The older `mid-conversation-tool-changes-2026-07-01` header still works for changes that name a tool by reference, on the Claude API, Amazon Bedrock, and Google Cloud. The same message replaces forced `tool_choice` when a specific tool must run on the current turn (see [Breaking changes](#fable-5-1-breaking-changes)). For a reminder that applies to one turn only, send it as a separate text-only `role: "system"` message with `clear_at: "next_user_message"` ([turn-scoped system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#turn-scoped-system-messages), beta header `mid-conversation-system-clear-at-2026-08-21`) and leave it in the history: it stops rendering after the next user message and costs no tokens once cleared. A message that carries `tool_addition` or `tool_removal` blocks can't be turn-scoped.

3.  **Use `fallbacks: "default"` for refusals:** Keep handling `stop_reason: "refusal"` and reading `stop_details.category` before response content. To re-run refused requests on another model automatically, set `fallbacks: "default"` (beta, `server-side-fallback-2026-07-01` header). `"default"` retries a declined request on the model Anthropic recommends for that category. The permitted fallback targets for Claude Fable 5.1 are Claude Opus 4.8 (`claude-opus-4-8`) and Claude Opus 5 (`claude-opus-5`). An explicit `fallbacks` list may name either. The fallback model doesn't receive Claude Fable 5.1's thinking blocks. If you build the retry yourself, [fallback credit](../04-API-Reference/Guides/build-with-claude-fallback-credit.md) applies on the same terms as Claude Fable 5. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

4.  **Start at `high` effort and sweep:** The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) default is `high`, and all five levels are supported. Keep the Claude Fable 5 guidance: `high` for most work, and `medium` as a cost control worth testing. Claude Fable 5.1's gains over Claude Fable 5 are largest at `xhigh` and `max`, but those levels also add thinking time and time-to-first-response, so step up to them for the most capability-sensitive tasks and where your evals show the gain. Run a fresh sweep on your own evals rather than carrying over a setting tuned for Claude Fable 5. See [Recommended effort levels for Claude Fable 5.1](../04-API-Reference/Guides/build-with-claude-effort.md#recommended-effort-levels-for-claude-fable-5-1).

5.  **Trim context on the server, or compact in a shape that carries no stale thinking:** If your code truncates or summarizes older turns on the client, the simplest fix is to move that work to server-side [compaction](../04-API-Reference/Guides/build-with-claude-compaction.md) or [context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md). Neither counts as an edit, because the [history check](#fable-5-1-preserved-thinking) compares the conversation as you sent it, so nothing they remove invalidates later thinking blocks, and compaction's [`instructions` parameter](../04-API-Reference/Guides/build-with-claude-compaction-threshold.md#custom-summarization-instructions) accepts your own summarization prompt. If you keep recent turns verbatim behind the summary, or summarize in the background while the conversation continues, use [on-demand compaction](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md) (beta header `compact-2026-09-04`) rather than a client-written summary. The API writes a signed summary block that you put in place of the messages it summarizes. The thinking blocks in the turns you keep can stay valid, under the conditions in [Compaction and preserved thinking](../04-API-Reference/Guides/build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid). If you keep compaction on the client, pick one of three shapes:

    - **Simple compaction (recommended):** replace the whole history with one summary message plus the new user turn and replay nothing else. No thinking blocks are carried over, so nothing fails. Claude models are trained on long-horizon tasks with this scheme, and it performs comparably to more elaborate ones for most workloads.
    - **Keep-tail compaction:** if you keep the most recent turns verbatim behind a summary, strip the `thinking` and `redacted_thinking` blocks from those turns (text and tool calls can stay), or set `prefix_mismatch_behavior: "drop_block"`. Their thinking was produced against the full history and fails behind the summary otherwise.
    - **Background compaction:** if you build the summary off the critical path and swap it in later, every turn produced in the meantime carries thinking that predates the swap. Send `"drop_block"` on every request that still carries thinking blocks produced before the swap (or strip those blocks yourself; `input_transformations` on the first response after the swap lists exactly which ones), or compact synchronously.

    Don't snip individual turns out of the middle of the transcript: that invalidates every later thinking block and no client-side shape avoids it. Use a [mid-conversation system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) for the instruction change you were making, or server-side [context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md) for selective removal. See [Passing compaction blocks back](../04-API-Reference/Guides/build-with-claude-compaction-threshold.md#passing-compaction-blocks-back).

### Migration checklist

- Update the model name from `claude-fable-5` to `claude-fable-5-1` (or `claude-mythos-5` to `claude-mythos-5-1`).
- Replace forced `tool_choice` (`{type: "any"}` or `{type: "tool", ...}`). It returns a 400 error. Use `{type: "auto"}` plus an explicit instruction and `strict: true` tools, or JSON outputs. Put the instruction in the `user` turn, or in a mid-conversation `role: "system"` message when your application requires the call.
- Keep passing `thinking` blocks back unchanged on every turn, including empty ones. Claude Fable 5.1 reads blocks from Claude Opus 5, Claude Fable 5, Claude Mythos 5, and earlier models. Moving a conversation from Claude Fable 5.1 to an earlier model drops its blocks (Claude Mythos 5.1 reads them).
- If your code builds the `messages` array itself, check whether it [edits earlier turns](#fable-5-1-preserved-thinking): run a session with the `thinking-binding-controls-2026-08-01` beta header and `prefix_mismatch_behavior: "drop_block"`, log `input_transformations`, and fix every `prefix_binding_mismatch`. `model_binding_mismatch` entries after a model switch are expected.
- Keep conversation history append-only: freeze `system` and `tools` at session start and move mid-session changes to `role: "system"` messages and `tool_addition` / `tool_removal` blocks, send per-turn reminders as turn-scoped system messages you never remove, trim context server-side or strip thinking blocks from any turns you carry across a client-side summary, and reference cross-turn files by `file_id`.
- Pick a production `prefix_mismatch_behavior` (`"error"` by default, or `"drop_block"`) and monitor it. If you maintain a tool that others run with their own API key, test with the field set: new accounts are enforced by default even if yours isn't.
- Review agent loops for one-tool-call-per-turn behavior and add the batching instruction.
- If your interface renders progress text between tool calls, set `thinking.display` to `"updates"` (beta) or `"summarized"` and prompt for updates.
- If you change effort between requests, move the change to a [per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta) `role: "system"` message (beta) to keep cache hits.
- Handle `stop_reason: "refusal"` and read `stop_details.category`. Consider `fallbacks: "default"` (beta).
- Re-evaluate `effort` with a fresh sweep, starting at `high`, and re-baseline cost and latency on your own workloads. The tokenizer is unchanged. Prompt cache reads cost a quarter of the Claude Fable 5 rate.

## Migrating to Claude Fable 5.1 from Claude Opus 5

Claude Fable 5.1 uses the same [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) and [tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) patterns as Claude Opus 5. It keeps the [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, [128k max output tokens](about-claude-models-overview.md), the 512-token prompt caching minimum, and [mid-conversation system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) support. The prefill restriction, the sampling-parameter restriction, and the `"omitted"` default for `thinking.display` also carry over. Apply everything in [Migrating to Claude Fable 5.1 from Claude Fable 5](#migrating-from-claude-fable-5-to-claude-fable-5-1), plus the following.

### Update your model name

```python
model = "claude-opus-5"  # Before
model = "claude-fable-5-1"  # After

# Or, for the Project Glasswing model with the same capabilities:
model = "claude-mythos-5-1"  # After
```



### What changed

1.  **Thinking can no longer be disabled:** Claude Opus 5 accepts `thinking: {type: "disabled"}` at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or lower. On `claude-fable-5-1` and `claude-mythos-5-1`, [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on, and `thinking: {type: "disabled"}` returns a 400 error at any effort level. Remove the field, control token spend with lower effort levels, and revisit `max_tokens` for workloads that ran with thinking disabled.

2.  **Forced tool choice is not supported:** Claude Opus 5 accepts `tool_choice` `any` and `tool`. `claude-fable-5-1` returns a 400 error. See [Breaking changes](#fable-5-1-breaking-changes).

3.  **Preserved thinking across models:** Claude Fable 5.1 reads Claude Opus 5's thinking blocks: conversations moving from `claude-opus-5` to `claude-fable-5-1` keep their reasoning. Claude Opus 5 can't read Claude Fable 5.1's blocks. Claude Fable 5.1's blocks also [stop being valid when earlier turns change](#fable-5-1-preserved-thinking): if your code edits earlier messages, rebuilds `system` or `tools`, or compacts on the client between requests, Claude Opus 5 didn't object, but `claude-fable-5-1` rejects or drops every later thinking block. Run the three-step check in that section before switching traffic. See [Breaking changes](#fable-5-1-breaking-changes).

4.  **Text between tool calls is returned in thinking blocks:** On Claude Opus 5, text the model writes between tool calls comes back as `text` blocks. On `claude-fable-5-1`, as on Claude Fable 5, that narration comes back as progress-update `thinking` blocks, one before each tool call. Under the default `thinking.display` of `"omitted"`, they carry no readable text. If your interface renders that narration, set `display: "updates"` (beta) to receive progress updates as text while reasoning stays hidden, or `"summarized"` to receive both. Then render the non-empty `thinking` blocks between `tool_use` blocks. See [Progress updates between tool calls](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates).

5.  **Safety classifiers and fallback routing:** Claude Fable 5.1 runs safety classifiers covering the same `stop_details` categories as Claude Fable 5, a broader set than Claude Opus 5's cybersecurity-only classifiers. Expect `stop_details.category` values beyond `"cyber"`, such as `"bio"` and `"reasoning_extraction"`; see the [refusal category table](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full set. For `fallbacks` configuration and permitted targets, see [Use `fallbacks: "default"` for refusals](#fable-5-1-recommended-changes).

6.  **Pricing:** \$10 USD per million input tokens and \$50 USD per million output tokens, compared with \$5 USD and \$25 USD for Claude Opus 5. Prompt cache reads are \$0.25 USD per million tokens, half the Claude Opus 5 rate. See [Claude pricing](../17-Billing-Plans/about-claude-pricing.md).

7.  **Data retention:** Claude Fable 5.1 and Claude Mythos 5.1 require 30-day data retention, aren't available under zero data retention (ZDR) arrangements unless expressly authorized by Anthropic, and are designated Covered Models. Claude Opus 5 is available under ZDR. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).

### Migration checklist

- If your organization has a zero data retention (ZDR) arrangement, confirm eligibility first: these models aren't available under ZDR unless expressly authorized by Anthropic. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- Update the model name from `claude-opus-5` to `claude-fable-5-1` (or `claude-mythos-5-1`).
- Remove any `thinking: {type: "disabled"}` configuration: it returns a 400 error on `claude-fable-5-1`. Control token spend with lower [effort](../04-API-Reference/Guides/build-with-claude-effort.md) levels, and revisit `max_tokens`.
- Replace forced `tool_choice` (`any` or `tool`) with `auto` plus an explicit instruction (`user` turn or mid-conversation system message) and `strict: true` tools, or with JSON outputs.
- If your interface renders text between tool calls, set `display: "updates"` (beta) or `"summarized"` and render the non-empty `thinking` blocks.
- Apply the preserved-thinking, history-editing, behavior, effort, and fallback items from the [Claude Fable 5 checklist](#migration-checklist-fable-5-1-from-fable-5).
- Re-baseline cost on your own workloads. The tokenizer is unchanged. Per-token pricing differs.

## Migrating to Claude Fable 5.1 from Claude Opus 4.8 or earlier

First apply [Migrating to Claude Mythos 5 and Claude Fable 5 from Claude Opus 4.8](models-fable-5-migration-guide.md#migrating-from-claude-opus-48) for the API-level changes from Claude Opus 4.8. It covers adaptive thinking, thinking output, refusals, effort, the caching minimum, pricing, and data retention. Then apply the remaining delta in [Migrating to Claude Fable 5.1 from Claude Fable 5](#migrating-from-claude-fable-5-to-claude-fable-5-1). On Claude Opus 4.7 or earlier, start with the matching [Migrating to Claude Opus 5.5](models-opus-5-5-migration-guide.md) section.

### Update your model name

```python
model = "claude-opus-4-8"  # Before
model = "claude-fable-5-1"  # After

# Or, for the Project Glasswing model with the same capabilities:
model = "claude-mythos-5-1"  # After
```



### Migration checklist

- If your organization has a zero data retention (ZDR) arrangement, confirm eligibility first: these models aren't available under ZDR unless expressly authorized by Anthropic. Claude Opus 4.8 is available under ZDR.
- Update the model name from `claude-opus-4-8` to `claude-fable-5-1` (or `claude-mythos-5-1`).
- Remove any `thinking: {type: "disabled"}` configuration and revisit `max_tokens`. Requests without a `thinking` field run with adaptive thinking.
- Replace forced `tool_choice` (`any` or `tool`) with `auto` plus an explicit instruction (`user` turn or mid-conversation system message) and `strict: true` tools, or with JSON outputs.
- Pass `thinking` blocks back unchanged and treat their text as display-only. Claude Fable 5.1 reads Claude Opus 4.8's thinking blocks: a conversation that moves onto `claude-fable-5-1` keeps its earlier reasoning. Claude Opus 4.8 can't read Claude Fable 5.1's blocks.
- If your code builds the `messages` array itself, check whether it [edits earlier turns](#fable-5-1-preserved-thinking). Integrations written for Claude Opus 4.8 and earlier often truncate old turns, strip or rebuild earlier messages, or refresh the `system` prompt each request, and Claude Opus 4.8 never objected. On `claude-fable-5-1` each of those invalidates later thinking blocks.
- Handle `stop_reason: "refusal"`, read `stop_details.category`, and consider `fallbacks: "default"` (beta).
- Apply the preserved-thinking, history-editing, behavior, per-message effort, and progress-update items from the [Claude Fable 5 checklist](#migration-checklist-fable-5-1-from-fable-5).
- Re-evaluate `effort` (start at `high`), review prompts near the 512-token caching minimum, and re-baseline cost and latency. Per-token pricing differs.

## Migrating to Claude Mythos 5.1 from Claude Mythos 5

[Claude Mythos 5.1](../22-Safety-Policy/glasswing.md) is the access-gated counterpart to Claude Fable 5.1. Confirm your organization's access with your Anthropic account team before switching model IDs.

The API-level delta matches [Migrating to Claude Fable 5.1 from Claude Fable 5](#migrating-from-claude-fable-5-to-claude-fable-5-1): forced tool choice returns a 400 error, and thinking blocks are preserved only for the model that produced them or a newer one (Claude Mythos 5.1 reads Claude Mythos 5's blocks, not the reverse). Unlike Claude Fable 5.1, Claude Mythos 5.1 doesn't run the conversation check, so editing earlier turns doesn't [invalidate thinking blocks](#fable-5-1-preserved-thinking), though it still restarts the prompt cache.

### Update your model name

```python
model = "claude-mythos-5"  # Before
model = "claude-mythos-5-1"  # After
```



### Migration checklist

- Update the model name from `claude-mythos-5` to `claude-mythos-5-1`.
- Replace forced `tool_choice` (`any` or `tool`) with `auto` plus an explicit instruction (`user` turn or mid-conversation system message) and `strict: true` tools, or with JSON outputs.
- Handle `stop_reason: "refusal"` and read `stop_details.category` before response content. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- Keep passing `thinking` blocks back unchanged on every turn, including empty ones.
- If your code builds the `messages` array itself, keep conversation history append-only to keep the prompt cache warm. Claude Mythos 5.1 doesn't run the [conversation check](../04-API-Reference/Guides/build-with-claude-thinking.md#preserved-in-conversation), so edits don't invalidate its thinking blocks.
- Apply the behavior and recommended changes from the [Claude Fable 5 section](#migrating-from-claude-fable-5-to-claude-fable-5-1), except the history-editing items, which don't apply to Claude Mythos 5.1.
- Re-evaluate `effort` with a fresh sweep and re-baseline cost and latency. Prompt cache reads cost a quarter of the Claude Mythos 5 rate.
