---
title: "Migrating to Claude Mythos 5 and Claude Fable 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5/migration-guide"
category: "20-Models"
fetched_at: "2026-09-26T06:39:45Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5%2Fmigration-guide)





SearchCtrlK

[Console](../04-API-Reference/Other/usage-limits.md)

Documentation

# Migrating to Claude Mythos 5 and Claude Fable 5

Copy page



Migrate to Claude Mythos 5 and Claude Fable 5 from Claude Mythos Preview, Claude Opus 5, or Claude Opus 4.8: model IDs, API changes, and migration checklists.

Copy page





This guide covers migrating [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) code. If you use [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-fable-5
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

[Claude Fable 5](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md) is built for demanding reasoning and long-horizon agentic work. [Claude Fable 5.1](models-fable-5-1-migration-guide.md) builds on it. Claude Fable 5 is available on the Claude API, [Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md). [Claude Mythos 5](../22-Safety-Policy/glasswing.md) shares the same capabilities and is offered only to approved customers in Project Glasswing.

The baseline settings shared by `claude-fable-5` and `claude-mythos-5`:

- **Thinking:** [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on. The model determines when and how much to think on each request, and no `thinking` configuration is required. Both `thinking: {type: "disabled"}` and manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) return a 400 error.
- **Prefill:** Prefilling the assistant message returns a 400 error. Use system prompt instructions instead.
- **Context window and output:** A [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, and up to 128k output tokens per request.
- **Pricing:** \$10 USD per million input tokens and \$50 USD per million output tokens. See [Claude pricing](../17-Billing-Plans/about-claude-pricing.md).
- **Data retention:** Both models require 30-day data retention and are not available under zero data retention (ZDR) arrangements unless expressly authorized by Anthropic. Both are designated Covered Models. On the Claude API, a request to Claude Fable 5 from an organization whose data retention configuration does not meet this requirement returns a 400 `invalid_request_error`. Organizations with a ZDR arrangement should contact their Anthropic account team to discuss data retention configuration, or configure data retention per workspace. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements) for per-platform details.

Where the two models diverge:

- **Availability:** Claude Fable 5 does not require access approval. Claude Mythos 5 is available only to approved customers in [Project Glasswing](../22-Safety-Policy/glasswing.md).
- **Safety classifiers:** Claude Fable 5 runs safety classifiers that can decline requests with `stop_reason: "refusal"`. Claude Mythos 5 does not include these classifiers. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- **Priority Tier:** [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is supported on Claude Fable 5 but not on Claude Mythos 5.

## Migrating to Claude Mythos 5 and Claude Fable 5 from Claude Mythos Preview

[Claude Mythos 5](../22-Safety-Policy/glasswing.md) is the access-gated successor to [Claude Mythos Preview](../22-Safety-Policy/glasswing.md), the invitation-only research preview. [Claude Fable 5](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md) offers the same capabilities and does not require access approval. The changes in this section apply equally to both targets.

Migration is mostly drop-in. Claude Mythos 5 and Claude Fable 5 use the same [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) and the same [tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) patterns as Claude Mythos Preview, and token counts are roughly unchanged because all three models use the same tokenizer. The key changes to check are the features that are no longer available (listed in the next section) and thinking output. If you migrate to Claude Fable 5, also plan for safety classifier refusals, which Claude Mythos Preview and Claude Mythos 5 do not have; see [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

For the Claude Mythos Preview retirement timeline, see [Model deprecations](about-claude-model-deprecations.md).

### Update your model name

```python
model = "claude-mythos-preview"  # Before
model = "claude-mythos-5"  # After

# Or, for the model with the same capabilities and no access approval requirement:
model = "claude-fable-5"  # After
```



### Features not available on Claude Mythos 5 and Claude Fable 5

1.  **Extended thinking and thinking token budgets:** Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported on `claude-mythos-5` or `claude-fable-5` and returns a 400 error. [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on: the model determines when and how much to think on each request, and no `thinking` configuration is required. `thinking: {type: "disabled"}` returns an error. `budget_tokens` has no direct replacement: thinking is adaptive, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is a separate output-level control, not a thinking budget.

    Before (Claude Mythos Preview):

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
    client.messages.create(
        model="claude-mythos-preview",
        max_tokens=16000,
        thinking={"type": "enabled", "budget_tokens": 10000},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    After (Claude Mythos 5):

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
    client.messages.create(
        model="claude-mythos-5",
        max_tokens=16000,
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    The change for Claude Fable 5 is identical, with `claude-fable-5` as the model name.

2.  **Assistant prefill:** Prefilling the assistant message is not supported on `claude-mythos-5` or `claude-fable-5` and returns a 400 error, the same as on Claude Mythos Preview. Use system prompt instructions instead.

3.  **Thinking output:** On `claude-mythos-5` and `claude-fable-5`, the raw chain of thought is never returned, but thinking blocks still carry readable summarized text when `thinking.display` is set to `summarized`. Pass thinking blocks back unchanged when continuing a conversation on the same model. See [Thinking output on Claude Fable and Claude Mythos models](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5).

### Token counting and billing

`claude-mythos-5` and `claude-fable-5` use the same tokenizer as `claude-mythos-preview` (the tokenizer introduced with Claude Opus 4.7). Token counts are roughly unchanged when migrating from `claude-mythos-preview`. Compared with models before Claude Opus 4.7, the same content can tokenize to roughly 30% more tokens, varying by content and workload shape.

[`/v1/messages/count_tokens`](../04-API-Reference/Guides/build-with-claude-token-counting.md) returns roughly unchanged values for `claude-mythos-5` and `claude-fable-5` compared with `claude-mythos-preview`. Re-baseline cost and latency on your own workloads.

### Migration checklist

- Update the model name from `claude-mythos-preview` to `claude-mythos-5`, or to `claude-fable-5`, which offers the same capabilities and does not require access approval.
- Remove manual extended thinking configuration (`thinking: {type: "enabled", budget_tokens: N}`). Adaptive thinking is always on, and no `thinking` field is required.
- Remove any `thinking: {type: "disabled"}` configuration. Disabling thinking returns an error on `claude-mythos-5` and `claude-fable-5`.
- Remove `budget_tokens`. It has no direct replacement: thinking is adaptive, and the `effort` parameter is a separate output-level control, not a thinking budget.
- Verify any code that parses the `thinking` field treats it as display text only and passes thinking blocks back unchanged when continuing on the same model. `thinking.display` defaults to `"omitted"` on `claude-mythos-5` and `claude-fable-5`, the same as on Claude Mythos Preview. Set `display: "summarized"` to receive readable summaries. See [Thinking output on Claude Fable and Claude Mythos models](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5).
- If you replay conversation history on an earlier model, strip `thinking` and `redacted_thinking` blocks from prior assistant turns first. Thinking blocks from `claude-fable-5` and `claude-mythos-5` are readable only by the model that produced them or a newer one: earlier models silently ignore them, while Claude Fable 5.1 and Claude Mythos 5.1 read them, so keep them when you move a conversation up to those models (see [Switching models mid-conversation](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models)). Stripping keeps requests to earlier models minimal and uniform.
- If you migrate to Claude Fable 5, handle `stop_reason: "refusal"` and read the `stop_details.category` field. Claude Fable 5 runs safety classifiers that Claude Mythos Preview and Claude Mythos 5 do not have. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- Re-baseline token counts and costs on your own workloads. Token counts are roughly unchanged when migrating from `claude-mythos-preview`.

## Migrating to Claude Mythos 5 and Claude Fable 5 from Claude Opus 5

Claude Fable 5 and Claude Mythos 5 use the same [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) and the same [tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) patterns as Claude Opus 5, with the same [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default and the same [128k max output tokens](about-claude-models-overview.md). The prefill and sampling-parameter restrictions, and the thinking display behavior, carry over from Claude Opus 5 unchanged. The changes to check are always-on thinking, pricing, Priority Tier, and data retention.

### Update your model name

```python
model = "claude-opus-5"  # Before
model = "claude-fable-5"  # After

# Or, for the Project Glasswing model with the same capabilities:
model = "claude-mythos-5"  # After
```



### What changed

1.  **Thinking can no longer be disabled:** On Claude Opus 5, thinking is on by default and can be turned off with `thinking: {type: "disabled"}` at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or below. On `claude-fable-5` and `claude-mythos-5`, [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is always on, and `thinking: {type: "disabled"}` returns a 400 error at any effort level. Remove the `thinking: {type: "disabled"}` configuration and use lower effort levels to control token spend instead.

    If your Claude Opus 5 requests disabled thinking, the response shape changes: a response can begin with one or more `thinking` blocks before the first `text` block, returned with an empty `thinking` field at the default `display: "omitted"` (the same default as Claude Opus 5). Code that reads the reply by position, such as `content[0].text` or a stream handler that treats the first content block as text, must select content blocks by their `type` field instead, and tool-use loops must pass `thinking` blocks back complete and unmodified with their tool results. The API rejects edited, reordered, or partially dropped thinking blocks with a 400 error (see [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks)). Thinking tokens are billed as output tokens even when the thinking text is not returned.

2.  **Pricing:** Claude Fable 5 and Claude Mythos 5 are priced at \$10 USD per million input tokens and \$50 USD per million output tokens, compared with \$5 USD and \$25 USD for Claude Opus 5. See [Claude pricing](../17-Billing-Plans/about-claude-pricing.md).

3.  **Priority Tier:** [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is not supported on Claude Opus 5, so no existing traffic is affected. If your organization has a Priority Tier commitment, Claude Fable 5 supports it; Claude Mythos 5 does not.

4.  **Data retention:** Claude Fable 5 and Claude Mythos 5 require 30-day data retention and are not available under zero data retention (ZDR) arrangements unless expressly authorized by Anthropic. Both are designated Covered Models. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).

### Migration checklist

- Update the model name from `claude-opus-5` to `claude-fable-5` (or `claude-mythos-5`).
- Remove any `thinking: {type: "disabled"}` configuration; it returns a 400 error on `claude-fable-5` and `claude-mythos-5`. Use lower [effort](../04-API-Reference/Guides/build-with-claude-effort.md) levels to control token spend instead, and revisit `max_tokens` for workloads that ran with thinking disabled on Claude Opus 5.
- If those workloads read content by position, such as `content[0].text`, update them to select content blocks by `type`: `thinking` blocks now arrive before `text` blocks. Pass `thinking` blocks back complete and unmodified in tool-use loops; modified blocks return a 400 error.
- If your organization has a zero data retention (ZDR) arrangement, confirm eligibility before migrating: these models are not available under ZDR unless expressly authorized by Anthropic. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- Re-baseline cost on your own workloads. Token counts are roughly unchanged; per-token pricing differs, and workloads that ran with thinking disabled now produce thinking tokens, which are billed as output tokens.

## Migrating to Claude Mythos 5 and Claude Fable 5 from Claude Opus 4.8



If your code is on Claude Opus 4.7 or earlier, first apply the relevant [Migrating to Claude Opus 5.5](models-opus-5-5-migration-guide.md) from-section for the API-level changes from your current model, then the remaining delta in this section.

Migration is mostly drop-in. Claude Fable 5 and Claude Mythos 5 use the same [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) and the same [tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) patterns as Claude Opus 4.8, with the same [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default and the same [128k max output tokens](about-claude-models-overview.md). Token counts are roughly unchanged because the models use the same tokenizer. The key changes to check are always-on [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), thinking output, safety classifier refusals (Claude Fable 5 only), and pricing.

### Update your model name

```python
model = "claude-opus-4-8"  # Before
model = "claude-fable-5"  # After

# Or, for the Project Glasswing model with the same capabilities:
model = "claude-mythos-5"  # After
```



### What changed

The items in this section describe the API and behavior differences worth checking after you swap the model ID. Except where noted, they apply equally to `claude-fable-5` and `claude-mythos-5`.

1.  **Adaptive thinking is always on:** [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is the only thinking mode on `claude-fable-5` and `claude-mythos-5`. The model determines when and how much to think on each request, and no `thinking` configuration is required. `thinking: {type: "disabled"}` returns an error. Use the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) to control thinking depth.

    The behavior change to check: on Claude Opus 4.8, requests without a `thinking` field run without thinking; on `claude-fable-5` and `claude-mythos-5`, those same requests run with adaptive thinking. `max_tokens` remains a hard limit on total output, thinking plus response text, so revisit it for workloads that ran without thinking on Claude Opus 4.8. See [Cost control](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md#cost-control). Responses can also begin with one or more `thinking` blocks before the first `text` block, so code that reads the reply by position (for example, `content[0].text`, or a stream handler that treats the first content block as text) must select content blocks by their `type` field instead. Thinking tokens are billed as output tokens even when the thinking text is not returned to you, so a workload that ran without thinking on Claude Opus 4.8 produces more output tokens per request, in addition to the per-token price difference.

    If you run a tool-use loop, pass the `thinking` blocks from each assistant response back to the API complete and unmodified when you return tool results, including blocks whose `thinking` field is empty. Echo the assistant message as received rather than filtering its content blocks by type or rebuilding it: the API rejects edited, reordered, or partially dropped thinking blocks with a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).

    Before (Claude Opus 4.8):

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
    client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    After (Claude Fable 5):

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
    client.messages.create(
        model="claude-fable-5",
        max_tokens=16000,
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    The change for Claude Mythos 5 is identical, with `claude-mythos-5` as the model name.

2.  **Extended thinking and thinking budgets (unchanged):** Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported on `claude-fable-5` or `claude-mythos-5` and returns a 400 error, the same as on Claude Opus 4.8. `budget_tokens` has no direct replacement: thinking is adaptive, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is a separate output-level control, not a thinking budget.

3.  **Assistant prefill (unchanged):** Prefilling the assistant message is not supported on `claude-fable-5` or `claude-mythos-5` and returns a 400 error, the same as on Claude Opus 4.8. Use system prompt instructions instead.

4.  **Thinking output:** On `claude-fable-5` and `claude-mythos-5`, the raw chain of thought is never returned, but thinking blocks still carry readable summarized text when `thinking.display` is set to `summarized`. Pass thinking blocks back unchanged when continuing a conversation on the same model. See [Thinking output on Claude Fable and Claude Mythos models](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5).

5.  **Safety classifiers and the `refusal` stop reason (Claude Fable 5 only):** `claude-fable-5` runs safety classifiers on requests and during response generation. Claude Mythos 5 does not include these classifiers. When a classifier declines a request, the Messages API returns `stop_reason: "refusal"` as a successful HTTP 200 response, not an error. The `stop_details.category` field reports which classifier fired, with categories such as `"cyber"`, `"bio"`, and `"reasoning_extraction"`, or `null` when the refusal maps to no named category. See the [refusal category table](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full set.

    A refusal that arrives before any output is billed when its category is `"bio"`, `"frontier_llm"`, or `"reasoning_extraction"`. A refusal before any output in any other category, or with a `null` category, is not billed ([How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed)). Before September 24, 2026, no refusal before any output was billed on Claude Fable 5. When a classifier fires mid-stream, the input and already-streamed output are billed; discard the partial output.

    To re-run refused requests on another model automatically, pass the opt-in `fallbacks` parameter, which is in beta on the Claude API. The parameter is not available on the Message Batches API or on Amazon Bedrock, Google Cloud, and Microsoft Foundry; on those three platforms, run the retry client-side or use the SDK refusal-fallback middleware. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

6.  **Start at `high` effort:** The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) default remains `high`. On Claude Opus 4.8, the recommendation for coding and high-autonomy work is to set `xhigh` explicitly. On `claude-fable-5` and `claude-mythos-5`, use `high` as the default for most tasks and reserve `xhigh` for the most capability-sensitive workloads. Lower effort settings still perform well and often exceed `xhigh` performance on prior models. Reduce effort if a task completes but takes longer than necessary. See [Prompting Claude Fable 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md#consider-all-effort-levels).

7.  **Lower prompt caching minimum:** The minimum cacheable prompt length on `claude-fable-5` and `claude-mythos-5` is 512 tokens, lower than the 1,024 tokens on Claude Opus 4.8. Prompts that were too short to cache on Claude Opus 4.8 can now create cache entries, with no code changes required. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations) for per-model minimums.

### Migration checklist

- If your organization has a zero data retention (ZDR) arrangement, confirm eligibility before migrating. `claude-fable-5` and `claude-mythos-5` require 30-day data retention and are not available under ZDR unless expressly authorized by Anthropic. On the Claude API, requests to `claude-fable-5` that don't meet this requirement return a 400 `invalid_request_error`. Claude Opus 4.8 is available under ZDR. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- Update the model name from `claude-opus-4-8` to `claude-fable-5` (or `claude-mythos-5`).
- Remove any `thinking: {type: "disabled"}` configuration. Disabling thinking returns an error on `claude-fable-5` and `claude-mythos-5`, and requests without a `thinking` field run with adaptive thinking.
- Update response parsing that reads content by position, such as `content[0].text`: with adaptive thinking always on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead, and pass `thinking` blocks back complete and unmodified in tool-use loops; modified blocks return a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).
- If you removed manual extended thinking and assistant prefills during earlier migrations, no action is needed: both remain unsupported on `claude-fable-5` and `claude-mythos-5`.
- Verify any code that parses the `thinking` field treats it as display text only and passes thinking blocks back unchanged when continuing on the same model. `thinking.display` defaults to `"omitted"` on `claude-fable-5` and `claude-mythos-5`, the same as on Claude Opus 4.8. Set `display: "summarized"` to receive readable summaries. See [Thinking output on Claude Fable and Claude Mythos models](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5).
- If you replay conversation history on an earlier model, strip `thinking` and `redacted_thinking` blocks from prior assistant turns first. Thinking blocks from `claude-fable-5` and `claude-mythos-5` are readable only by the model that produced them or a newer one: earlier models silently ignore them, while Claude Fable 5.1 and Claude Mythos 5.1 read them, so keep them when you move a conversation up to those models (see [Switching models mid-conversation](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#switching-models)). Stripping keeps requests to earlier models minimal and uniform. The exception is redeeming a [fallback credit](../04-API-Reference/Guides/build-with-claude-fallback-credit.md), which requires the request body echoed under that feature's exact rules.
- If you migrate to Claude Fable 5, handle `stop_reason: "refusal"` and read the `stop_details.category` field. To re-run refused requests on another model automatically, consider the opt-in `fallbacks` parameter (beta). See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- Re-evaluate your `effort` setting. Start at `high` for most tasks, including workloads that ran at `xhigh` on Claude Opus 4.8.
- Re-baseline cost and latency on your own workloads. Token counts are roughly unchanged when migrating from `claude-opus-4-8`; per-token pricing differs, and thinking tokens are billed as output tokens, so workloads that ran without thinking produce more output tokens per request.
