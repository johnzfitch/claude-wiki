---
title: "Migrating to Claude Opus 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5/migration-guide"
category: "20-Models"
fetched_at: "2026-09-18T06:38:06Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5%2Fmigration-guide)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5](models-opus-5-overview.md)

[Overview](models-opus-5-overview.md)[What's new](models-opus-5-whats-new-opus-5.md)[Migration guide](models-opus-5-migration-guide.md)

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

[Models & pricing](about-claude-models-overview.md)Claude Opus 5

# Migrating to Claude Opus 5

Copy page



Migrate to Claude Opus 5 from earlier Claude models: model IDs, breaking changes, recommended changes, and migration checklists.

Copy page





This guide covers migrating [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) code. If you use [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-opus-5
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

Claude Opus 5 is a step-change improvement over Claude Opus 4.8, strong on deep reasoning, agentic and long-horizon tasks, and test-time compute scaling. For behavioral differences and model-specific prompting patterns, see [Prompting Claude Opus 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md).

Claude Opus 5 is a drop-in upgrade for Claude Opus 4.8 at the same pricing of \$5 USD per million input tokens and \$25 USD per million output tokens; see [Claude pricing](../17-Billing-Plans/about-claude-pricing.md). There are two breaking changes for code already running on Claude Opus 4.8, covered under [Breaking changes](#breaking-changes). Claude Opus 5 supports the same set of features as Claude Opus 4.8, including the [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) (the default, with no beta header), [128k max output tokens](about-claude-models-overview.md), [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md), [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md), the [Files API](../04-API-Reference/Guides/build-with-claude-files.md), [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md), [vision](../04-API-Reference/Guides/build-with-claude-vision.md), and server-side and client-side [tools](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md), with two exceptions: [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) is not available on Claude Opus 5, and [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is not supported on Claude Opus 5. See each tool page for model availability.

## Migrating to Claude Opus 5 from Claude Opus 4.8



This section covers the delta from Claude Opus 4.8 only. If your code is on Claude Opus 4.7 or earlier, use these sections instead: [Migrating to Claude Opus 5 from Claude Opus 4.7](#migrating-from-claude-opus-47) or [Migrating to Claude Opus 5 from Claude Opus 4.6 and earlier Opus models](#migrating-from-claude-opus-46). They include this delta plus the breaking changes from earlier models (sampling parameters rejected, manual extended thinking rejected, prefill removed, new tokenizer).

### Update your model name

```python
# Opus migration
model = "claude-opus-4-8"  # Before
model = "claude-opus-5"  # After
```



`claude-opus-5` is a fixed model ID with no date suffix, the same scheme as `claude-opus-4-8` and `claude-sonnet-5`.

### Breaking changes

1.  **Thinking on by default:** On Claude Opus 4.8, requests without a `thinking` field run without thinking; on Claude Opus 5, the same requests run with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md). `max_tokens` remains a hard limit on total output, thinking plus response text, so revisit it for workloads that ran without thinking on Claude Opus 4.8. Thinking tokens are billed as output tokens even when the thinking text is not returned to you, so although per-token pricing is unchanged, a workload that ran without thinking on Claude Opus 4.8 can produce more output tokens per request on Claude Opus 5; see [Cost control](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md#cost-control). To preserve the old behavior, pass `thinking: {type: "disabled"}`, subject to the effort cap in the next item; note that with thinking disabled the model can occasionally emit tool calls as plain text or include internal XML tags in its visible output, so prefer lower effort levels with thinking enabled where you can, and see [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for mitigations where you can't.

    The response shape changes with it. With thinking on, a response can begin with one or more `thinking` blocks before the first `text` block, and because `thinking.display` defaults to `"omitted"` on Claude Opus 5, those blocks arrive with an empty `thinking` field alongside their `signature`. Code that reads the reply by position, such as `content[0].text` or a stream handler that treats the first `content_block_start` event as text, breaks on these responses. Select content blocks by their `type` field instead: read `text` from the blocks whose `type` is `"text"`, and branch on the block type when handling stream events. To receive readable thinking summaries instead of an empty `thinking` field, set `display: "summarized"`; see [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display).

    If you run a tool-use loop, pass the `thinking` blocks from each assistant response back to the API complete and unmodified when you return tool results, including blocks whose `thinking` field is empty. Echo the assistant message as received rather than filtering its content blocks by type or rebuilding it: the API rejects edited, reordered, or partially dropped thinking blocks with a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).

2.  **Disabling thinking is capped at `high` effort:** You can still turn thinking off with `thinking: {type: "disabled"}`, but only at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or below. A request that combines `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error. Claude Opus 4.8 accepts this combination, so audit requests that disable thinking before you migrate.

    The check is enforced on each request: every request's effort and thinking configuration is validated independently, so a request that raises effort to `xhigh` or `max` while thinking is disabled is rejected even if earlier requests in the conversation were accepted.

    Before (accepted on Claude Opus 4.8, rejected on Claude Opus 5):

    ``` shiki
    client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "disabled"},
        output_config={"effort": "xhigh"},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

    After (Claude Opus 5), either remove the `thinking` field to re-enable thinking:

    ``` shiki
    client.messages.create(
        model="claude-opus-5",
        max_tokens=16000,
        output_config={"effort": "xhigh"},  # thinking is on by default
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

    or keep thinking disabled and lower the effort:

    ``` shiki
    client.messages.create(
        model="claude-opus-5",
        max_tokens=16000,
        thinking={"type": "disabled"},
        output_config={"effort": "high"},  # or "medium", "low"
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

### Recommended changes

These are not required but will improve your experience:

1.  **Test `max` effort for capability-critical work:** Claude Opus 5 supports the full set of [effort levels](../04-API-Reference/Guides/build-with-claude-effort.md) (`low`, `medium`, `high`, `xhigh`, `max`). Where maximum capability matters more than token spend, test `max` effort. It can deliver gains on the most demanding tasks but may show diminishing returns from increased token usage and can be prone to overthinking on simpler ones. If you run at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act; start at 64k tokens and tune from there.

2.  **Consider automatic fallbacks:** Claude Opus 5 ships with cybersecurity safety classifiers whose cyber-category refusals can fall back to Claude Opus 4.8. To re-run refused requests on another model automatically, consider the `fallbacks` parameter with the `"default"` mode (`fallbacks: "default"`), which selects a recommended fallback model based on the refusal category instead of a hand-maintained model list. Server-side fallback is in beta; the `"default"` mode requires the `server-side-fallback-2026-07-01` beta header. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

3.  **Cache shorter prompts:** The minimum cacheable prompt length on Claude Opus 5 is 512 tokens, down from 1,024 tokens on Claude Opus 4.8. Prompts that were too short to cache on Claude Opus 4.8 can now create cache entries, with no code changes required. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations) for per-model minimums.

4.  **Change tools mid-conversation (beta):** You can add or remove tools between turns of a conversation without invalidating [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits on earlier turns. Send the beta header `mid-conversation-tool-changes-2026-07-01`. This is useful for agentic workloads that expose tools progressively or retire them as a task advances; without it, a changed tool list invalidates the cached prefix.

5.  **Re-tune length and verbosity prompts:** Default visible responses and written deliverables run longer on Claude Opus 5 than on Claude Opus 4.8, and lowering effort reduces thinking volume without reliably shortening the visible response. Prompt explicitly for conciseness or a target length instead. See [Response length and verbosity](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity) and [Written deliverable length](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#written-deliverable-length).

6.  **Remove carried-over verification instructions and constrain scope:** Claude Opus 5 verifies its own work without being told to, so remove explicit verification or self-check instructions carried over from prompts tuned for earlier models; leaving them in causes over-verification. For narrow tasks, constrain the task scope explicitly. In multi-agent frameworks, give explicit guidance on which scenarios warrant delegation or cap the number of subagents, because Claude Opus 5 delegates more readily than earlier models. See [Task scope and over-verification](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#task-scope-and-over-verification) and [Controlling subagent spawning](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#controlling-subagent-spawning).

### Migration checklist

- Update the model name from `claude-opus-4-8` to `claude-opus-5`.
- Review workloads that ran without a `thinking` field: they run with thinking on Claude Opus 5. Revisit `max_tokens`, which remains a hard limit on total output (thinking plus response text), or pass `thinking: {type: "disabled"}` at effort `high` or below to preserve the old behavior. If you disable thinking, review [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for the output artifacts that can appear and their prompting mitigations.
- Update response parsing that reads content by position, such as `content[0].text` or a stream handler that assumes the first content block is text: with thinking on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead.
- If you run a tool-use loop, pass `thinking` blocks back complete and unmodified when you return tool results; modified blocks return a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).
- Verify any code that parses the `thinking` field treats it as display text only. `thinking.display` defaults to `"omitted"` on Claude Opus 5, the same as on Claude Opus 4.8, so thinking blocks arrive with an empty `thinking` field; set `display: "summarized"` to receive readable summaries. See [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display).
- Audit requests that disable thinking: `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error, enforced on each request. Re-enable thinking or lower the effort to `high` or below.
- Re-evaluate your `effort` setting: run a fresh [effort](../04-API-Reference/Guides/build-with-claude-effort.md) sweep on your own evals rather than carrying over a setting tuned for an earlier model. `low` and `medium` effort are worth testing as cost and latency controls, and test `max` effort where maximum capability matters more than token spend. If you run at `xhigh` or `max` effort, raise `max_tokens` to at least 64k as a starting point.
- Review prompts near the caching minimum: prompts of 512 tokens or more can now create cache entries, down from 1,024 tokens on Claude Opus 4.8.
- Handle `stop_reason: "refusal"`, and consider `fallbacks: "default"` (beta) to re-run refused requests on a recommended fallback model automatically.
- If your organization has a [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) commitment, plan capacity separately: Priority Tier is not supported on Claude Opus 5, while Claude Opus 4.8 keeps it.
- For agentic workloads, consider [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) (beta) and mid-conversation tool changes (beta).
- Re-tune length and verbosity prompts: default visible responses and written deliverables run longer on Claude Opus 5, and lowering effort reduces thinking volume without reliably shortening the visible response. Prompt explicitly for conciseness or a target length. See [Response length and verbosity](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity) and [Written deliverable length](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#written-deliverable-length).
- Remove verification and self-check instructions carried over from prompts tuned for earlier models (they cause over-verification on Claude Opus 5), constrain task scope explicitly for narrow tasks, and in multi-agent frameworks steer or cap subagent delegation. See [Task scope and over-verification](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#task-scope-and-over-verification) and [Controlling subagent spawning](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#controlling-subagent-spawning).
- Re-baseline cost and latency on your own workloads. Per-token pricing is unchanged from Claude Opus 4.8, but thinking tokens are billed as output tokens, so workloads that ran without thinking can produce more output tokens per request.

## Migrating to Claude Opus 5 from Claude Opus 4.7

Claude Opus 5 should have strong out-of-the-box performance on existing Claude Opus 4.7 prompts and evals, at the same pricing of \$5 USD per million input tokens and \$25 USD per million output tokens. It supports the same set of features as Claude Opus 4.7, including the [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md), [128k max output tokens](about-claude-models-overview.md), [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md), [batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md), the [Files API](../04-API-Reference/Guides/build-with-claude-files.md), [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md), [vision](../04-API-Reference/Guides/build-with-claude-vision.md), and server-side and client-side [tools](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md), with two exceptions: [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) is not available on Claude Opus 5, and [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is not supported on Claude Opus 5. It also adds [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) and publicly documents [refusal stop details](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response). On the Claude API and Google Cloud, Claude Opus 5 also supports [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) as the stable `computer_toolset_20260801` toolset and the [browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) for tasks inside webpages, neither of which Claude Opus 4.7 supports; existing integrations on the earlier `computer_20251124` version continue to work unchanged on both models. To upgrade an existing integration, see [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124).



If your code is on Claude Opus 4.6 or earlier, use [Migrating to Claude Opus 5 from Claude Opus 4.6 and earlier Opus models](#migrating-from-claude-opus-46) instead. That section includes breaking changes (sampling parameters rejected, manual extended thinking rejected, new tokenizer) that the upgrade from Claude Opus 4.7 alone does not cover.

### Update your model name

```python
# Opus migration
model = "claude-opus-4-7"  # Before
model = "claude-opus-5"  # After
```



### Breaking changes

1.  **Thinking on by default:** On Claude Opus 4.7, requests without a `thinking` field run without thinking; on Claude Opus 5, the same requests run with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md). `max_tokens` remains a hard limit on total output, thinking plus response text, so revisit it for workloads that ran without thinking on Claude Opus 4.7. Thinking tokens are billed as output tokens even when the thinking text is not returned to you, so although per-token pricing is unchanged, a workload that ran without thinking on Claude Opus 4.7 can produce more output tokens per request on Claude Opus 5; see [Cost control](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md#cost-control). To preserve the old behavior, pass `thinking: {type: "disabled"}`, subject to the effort cap in the next item; note that with thinking disabled the model can occasionally emit tool calls as plain text or include internal XML tags in its visible output, so prefer lower effort levels with thinking enabled where you can, and see [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for mitigations where you can't.

    The response shape changes with it. With thinking on, a response can begin with one or more `thinking` blocks before the first `text` block, and because `thinking.display` defaults to `"omitted"` on Claude Opus 5, those blocks arrive with an empty `thinking` field alongside their `signature`. Code that reads the reply by position, such as `content[0].text` or a stream handler that treats the first `content_block_start` event as text, breaks on these responses. Select content blocks by their `type` field instead: read `text` from the blocks whose `type` is `"text"`, and branch on the block type when handling stream events. To receive readable thinking summaries instead of an empty `thinking` field, set `display: "summarized"`; see [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display).

    If you run a tool-use loop, pass the `thinking` blocks from each assistant response back to the API complete and unmodified when you return tool results, including blocks whose `thinking` field is empty. Echo the assistant message as received rather than filtering its content blocks by type or rebuilding it: the API rejects edited, reordered, or partially dropped thinking blocks with a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).

2.  **Disabling thinking is capped at `high` effort:** You can turn thinking off with `thinking: {type: "disabled"}`, but only at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or below. A request that combines `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error. Claude Opus 4.7 accepts this combination, so audit requests that disable thinking before you migrate.

    The check is enforced on each request: every request's effort and thinking configuration is validated independently, so a request that raises effort to `xhigh` or `max` while thinking is disabled is rejected even if earlier requests in the conversation were accepted.

    Before (accepted on Claude Opus 4.7, rejected on Claude Opus 5):

    ``` shiki
    client.messages.create(
        model="claude-opus-4-7",
        max_tokens=16000,
        thinking={"type": "disabled"},
        output_config={"effort": "xhigh"},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

    After (Claude Opus 5), either remove the `thinking` field to run with thinking:

    ``` shiki
    client.messages.create(
        model="claude-opus-5",
        max_tokens=16000,
        output_config={"effort": "xhigh"},  # thinking is on by default
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

    or keep thinking disabled and lower the effort:

    ``` shiki
    client.messages.create(
        model="claude-opus-5",
        max_tokens=16000,
        thinking={"type": "disabled"},
        output_config={"effort": "high"},  # or "medium", "low"
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    

### What changed

The following items are not breaking changes; they describe behavior differences worth checking after you swap the model ID.

1.  **Sampling parameters (unchanged):** Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 5, the same as on Claude Opus 4.7. Most SDKs still define these fields for compatibility with earlier models, so code that sets them type-checks even though the API rejects the request. The Python SDK (v1.0 and later) does not define them, and passing them raises a `TypeError`. If you removed these parameters when migrating to Opus 4.7, no further changes are needed.

2.  **Effort default is `high`:** The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) default on Claude Opus 5 is `high` on the Claude API and Claude Code. If you already set effort explicitly, your setting is unchanged.

3.  **Effort levels recalibrated:** The token allocation behind each effort level changes on Claude Opus 5 compared to Claude Opus 4.7, and Claude Opus 5 supports the full set of effort levels (`low`, `medium`, `high`, `xhigh`, `max`). Run a fresh effort sweep on your own evals rather than carrying over a setting tuned for Claude Opus 4.7. `low` and `medium` effort are worth testing as cost and latency controls, and test `max` effort where maximum capability matters more than token spend. If you run at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act; start at 64k tokens and tune from there. See [Effort](../04-API-Reference/Guides/build-with-claude-effort.md).

4.  **1M context window is the default:** Claude Opus 5 serves the full 1M token [context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default with no beta header and no long-context premium. If your client passes a context-window beta header for compatibility with older models, you can remove it on Claude Opus 5.

5.  **Mid-conversation system messages:** Claude Opus 5 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#limitations)). Use the top-level `system` field for instructions that apply from the start. Claude Opus 4.7 rejects `role: "system"` in `messages` with a 400 error. If you maintain code paths that rebuild the full message history to update instructions, you can simplify them and preserve [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits on earlier turns.

6.  **Refusal stop details:** The `stop_details` object on refusal responses (available since Claude Opus 4.7) is now publicly documented. When the model declines a request, it identifies the category of refusal, in addition to the existing `refusal` stop reason. No beta header is required, and there is no opt-out. See [Handling stop reasons](../04-API-Reference/Guides/build-with-claude-handling-stop-reasons.md).

7.  **Lower prompt caching minimum:** The minimum cacheable prompt length on Claude Opus 5 is 512 tokens, lower than on Claude Opus 4.7. Prompts that were too short to cache on Claude Opus 4.7 can now create cache entries, with no code changes required. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations) for per-model minimums.

8.  **Fast mode:** Claude Opus 5 supports [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview); fast mode is not available on Claude Opus 4.7, where requests with `speed: "fast"` return an error. The `speed: "fast"` parameter and `fast-mode-2026-02-01` beta header work unchanged on Claude Opus 5.

### Recommended changes

These are not required but will improve your experience:

1.  **Consider automatic fallbacks:** Claude Opus 5 ships with cybersecurity safety classifiers whose cyber-category refusals can fall back to Claude Opus 4.8. To re-run refused requests on another model automatically, consider the `fallbacks` parameter with the `"default"` mode (`fallbacks: "default"`), which selects a recommended fallback model based on the refusal category instead of a hand-maintained model list. Server-side fallback is in beta; the `"default"` mode requires the `server-side-fallback-2026-07-01` beta header. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

2.  **Change tools mid-conversation (beta):** You can add or remove tools between turns of a conversation without invalidating [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits on earlier turns. Send the beta header `mid-conversation-tool-changes-2026-07-01`. This is useful for agentic workloads that expose tools progressively or retire them as a task advances; without it, a changed tool list invalidates the cached prefix.

3.  **Re-tune length and verbosity prompts:** Default visible responses and written deliverables run longer on Claude Opus 5 than on earlier Opus models, and lowering effort reduces thinking volume without reliably shortening the visible response. Prompt explicitly for conciseness or a target length instead. See [Response length and verbosity](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity) and [Written deliverable length](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#written-deliverable-length).

4.  **Remove carried-over verification instructions and constrain scope:** Claude Opus 5 verifies its own work without being told to, so remove explicit verification or self-check instructions carried over from prompts tuned for earlier models; leaving them in causes over-verification. For narrow tasks, constrain the task scope explicitly. In multi-agent frameworks, give explicit guidance on which scenarios warrant delegation or cap the number of subagents, because Claude Opus 5 delegates more readily than earlier models. See [Task scope and over-verification](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#task-scope-and-over-verification) and [Controlling subagent spawning](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#controlling-subagent-spawning).

### Migration checklist

- Update model name from `claude-opus-4-7` to `claude-opus-5` (or update aliases).
- Review workloads that ran without a `thinking` field: they run with thinking on Claude Opus 5. Revisit `max_tokens`, which remains a hard limit on total output (thinking plus response text), or pass `thinking: {type: "disabled"}` at effort `high` or below to preserve the old behavior. If you disable thinking, review [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for the output artifacts that can appear and their prompting mitigations.
- Update response parsing that reads content by position, such as `content[0].text` or a stream handler that assumes the first content block is text: with thinking on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead.
- If you run a tool-use loop, pass `thinking` blocks back complete and unmodified when you return tool results; modified blocks return a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).
- Verify any code that parses the `thinking` field treats it as display text only. `thinking.display` defaults to `"omitted"` on Claude Opus 5, the same as on Claude Opus 4.7, so thinking blocks arrive with an empty `thinking` field; set `display: "summarized"` to receive readable summaries. See [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display).
- Audit requests that disable thinking: `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error, enforced on each request. Re-enable thinking or lower the effort to `high` or below.
- If you removed sampling parameters during the Opus 4.7 migration, no action is needed. If you re-added them with a 400-retry path, remove that retry path.
- Re-evaluate your `effort` setting: run a fresh [effort](../04-API-Reference/Guides/build-with-claude-effort.md) sweep on your own evals rather than carrying over a setting tuned for Claude Opus 4.7. Test `low` and `medium` effort as cost and latency controls, and `max` effort where maximum capability matters more than token spend. If you run at `xhigh` or `max` effort, raise `max_tokens` to at least 64k as a starting point.
- Remove any context-window beta header. The 1M context window is the default on the Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry.
- If you rebuild conversation history to update instructions, consider switching to a mid-conversation system message to preserve prompt cache hits.
- Verify your stop-reason handling reads `stop_details` on refusals (available since Claude Opus 4.7; now publicly documented), and consider `fallbacks: "default"` (beta) to re-run refused requests on a recommended fallback model automatically.
- Review prompts near the caching minimum: prompts of 512 tokens or more can now create cache entries.
- If you use [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md), plan an alternative: it is not available on Claude Opus 5.
- If your organization has a [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) commitment, note that Priority Tier is not supported on Claude Opus 5.
- If you used fast mode on Claude Opus 4.7, no request changes are needed beyond the model ID: `speed: "fast"` and the `fast-mode-2026-02-01` beta header work unchanged on Claude Opus 5.
- For agentic workloads, consider [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) (beta) and mid-conversation tool changes (beta).
- Re-tune length and verbosity prompts, and remove verification and self-check instructions carried over from prompts tuned for earlier models.
- Re-baseline cost and latency at your chosen effort level. Per-token pricing is unchanged from Claude Opus 4.7, but thinking tokens are billed as output tokens, so workloads that ran without thinking can produce more output tokens per request.

## Migrating to Claude Opus 5 from Claude Opus 4.6 and earlier Opus models

Claude Opus 5 should have strong out-of-the-box performance on existing Claude Opus 4.6 prompts and evals at the same pricing, but there are a handful of behavioral and API changes worth knowing about as you migrate. Most of these changes took effect in Claude Opus 4.7; two more, thinking on by default and an effort cap on disabling thinking, take effect on Claude Opus 5. All of them are covered in this section, so it is complete for code coming straight from Claude Opus 4.6. Claude Opus 5 supports the same set of features as Claude Opus 4.6, including:

- [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) at standard API pricing with no long-context premium
- [128k max output tokens](about-claude-models-overview.md)
- [Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)
- [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md)
- [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md)
- [Files API](../04-API-Reference/Guides/build-with-claude-files.md)
- [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md)
- [Vision](../04-API-Reference/Guides/build-with-claude-vision.md)
- Server-side and client-side [tools](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) ([bash](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-bash-tool.md), [code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md), [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md), [text editor](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md), [web search](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md), [MCP connector](../04-API-Reference/Agents-Tools/agents-and-tools-mcp-connector.md), [memory](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-memory-tool.md))

Two exceptions: [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) is not available on Claude Opus 5, and [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is not supported on Claude Opus 5. On the Claude API and Google Cloud, Claude Opus 5 also supports [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) as the stable `computer_toolset_20260801` toolset and the [browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) for tasks inside webpages, neither of which Claude Opus 4.6 or earlier Opus models support; existing integrations on the earlier `computer_20251124` version continue to work unchanged on Claude Opus 5. To upgrade an existing integration, see [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124).

### Update your model name

```python
# Opus migration
model = "claude-opus-4-6"  # Before
model = "claude-opus-5"  # After
```



### Breaking changes

1.  **Extended thinking removed:** `thinking: {type: "enabled", budget_tokens: N}` is no longer supported on Claude Opus 4.7 or later models and returns a 400 error. Switch to [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) (`thinking: {type: "adaptive"}`) and use the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) to control thinking depth. On Claude Opus 5, adaptive thinking is **on by default**: `thinking: {type: "adaptive"}` is valid and equivalent to omitting the `thinking` field entirely (see the next item).

    Before (Claude Opus 4.6):

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
        model="claude-opus-4-6",
        max_tokens=16000,
        thinking={"type": "enabled", "budget_tokens": 10000},
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    After (Claude Opus 5):

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
        model="claude-opus-5",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},  # or "max", "xhigh", "medium", "low"
        messages=[{"role": "user", "content": "..."}],
    )
    ```

    Adaptive thinking is steerable through prompting and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md); see [Choosing an effort level](#choosing-an-effort-level).

2.  **Thinking on by default:** On Claude Opus 4.6 and Claude Opus 4.7, requests without a `thinking` field run without thinking; on Claude Opus 5, the same requests run with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md). `max_tokens` remains a hard limit on total output, thinking plus response text, so revisit it for workloads that ran without thinking. Thinking tokens are billed as output tokens even when the thinking text is not returned to you, so although per-token pricing is unchanged, a workload that ran without thinking can produce more output tokens per request on Claude Opus 5; see [Cost control](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md#cost-control). To preserve the old behavior, pass `thinking: {type: "disabled"}`, subject to the effort cap in the next item; note that with thinking disabled the model can occasionally emit tool calls as plain text or include internal XML tags in its visible output, so prefer lower effort levels with thinking enabled where you can, and see [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for mitigations where you can't.

    The response shape changes with it. With thinking on, a response can begin with one or more `thinking` blocks before the first `text` block, and because thinking content is omitted by default on Claude Opus 5 (item 5 in this list), those blocks arrive with an empty `thinking` field alongside their `signature`. Code that reads the reply by position, such as `content[0].text` or a stream handler that treats the first `content_block_start` event as text, breaks on these responses. Select content blocks by their `type` field instead: read `text` from the blocks whose `type` is `"text"`, and branch on the block type when handling stream events.

    If you run a tool-use loop, pass the `thinking` blocks from each assistant response back to the API complete and unmodified when you return tool results, including blocks whose `thinking` field is empty. Echo the assistant message as received rather than filtering its content blocks by type or rebuilding it: the API rejects edited, reordered, or partially dropped thinking blocks with a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).

3.  **Disabling thinking is capped at `high` effort:** You can turn thinking off with `thinking: {type: "disabled"}`, but only at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or below. A request that combines `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error on Claude Opus 5, enforced on each request. Audit requests that disable thinking before you migrate: re-enable thinking or lower the effort to `high` or below.

4.  **Sampling parameters removed:** Setting `temperature`, `top_p`, or `top_k` to any non-default value on Claude Opus 4.7 or later models, including Claude Opus 5, returns a 400 error. The Python SDK (v1.0 and later) does not define them, and passing them raises a `TypeError`. The safest migration path is to omit these parameters entirely from request payloads. Prompting is the recommended way to guide model behavior on Claude Opus 5. If you were using `temperature = 0` for determinism, note that it never guaranteed identical outputs on prior models.

5.  **Thinking content omitted by default:** Thinking blocks still appear in the response stream on Claude Opus 4.7 and later models, but their `thinking` field is empty unless you explicitly opt in. This is a silent change from Claude Opus 4.6, where the default was to return summarized thinking text. To restore summarized thinking content, set `thinking.display` to `"summarized"`:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    thinking = {
        "type": "adaptive",
        "display": "summarized",
    }
    ```

    The default is `"omitted"` on Claude Opus 4.7 and later models. If your product streams reasoning to users, the new default appears as a long pause before output begins; set `display: "summarized"` to restore visible progress during thinking. See [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display) for details.

6.  **Updated token counting:** Claude Opus 4.7 introduced a new tokenizer, which later Opus models, including Claude Opus 5, also use. It contributes to improved performance on a wide range of tasks, and it may use roughly 1x to 1.35x as many tokens when processing text compared to models before Claude Opus 4.7 (up to ~35% more, varying by content).

    [`/v1/messages/count_tokens`](../04-API-Reference/Guides/build-with-claude-token-counting.md) returns a different number of tokens for Claude Opus 5 than it did for Claude Opus 4.6. Token efficiency can vary by workload shape.

    Prompting interventions, `task_budget`, and `effort` can help control costs and ensure appropriate token usage. These controls may trade off model intelligence. Update your `max_tokens` parameters to give additional headroom, including compaction triggers. Claude Opus 5 provides a 1M context window at standard API pricing with no long-context premium.

7.  **Prefill removal (carried over from Opus 4.6):** Prefilling assistant messages returns a 400 error on Claude Opus 4.7 and later models, including Claude Opus 5. Use [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md), system prompt instructions, or `output_config.format` instead.

### Choosing an effort level

The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) allows you to tune Claude's intelligence versus token spend, trading off capability for faster speed and lower costs. Claude Opus 5 supports the full set of effort levels and defaults to `high`. Run a fresh effort sweep on your own evals rather than carrying over a setting tuned for an earlier model:

- **`max`:** Can deliver gains on the most demanding tasks but may show diminishing returns from increased token usage and can be prone to overthinking on simpler ones. Test it where maximum capability matters more than token spend.
- **`xhigh`:** Extended capability for long-running agentic and coding work that needs more depth than the default.
- **`high`:** The default. Balances token usage and intelligence for most tasks.
- **`medium`:** Cost-saving step-down from the default, worth testing as a cost and latency control.
- **`low`:** Most efficient. Reserve for short, scoped tasks and latency-sensitive workloads.

If you run at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act; start at 64k tokens and tune from there. Effort is more important for this model than for any prior Opus. Experiment with it actively when you upgrade.

### Behavior changes

Claude Opus 4.7 introduced several behavioral differences from Claude Opus 4.6 that are not API breaking changes but may require prompt updates or scaffolding removal. They carry forward to Claude Opus 5, with the adjustments noted in this list.

1.  **Response length varies by use case:** Claude Opus 4.7 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis.

    If your product depends on a certain style or verbosity of output, you may need to tune your prompts. For example, to decrease verbosity, add: "Provide concise, focused responses. Skip non-essential context, and keep examples minimal." If you see specific kinds of over-explaining, add targeted instructions in your prompt to prevent them.

    Positive examples showing how Claude can communicate with the appropriate level of concision tend to be more effective than negative examples or instructions that tell the model what not to do. On Claude Opus 5, default visible responses and written deliverables run longer than on earlier Opus models, and lowering effort reduces thinking volume without reliably shortening the visible response; prompt explicitly for conciseness or a target length. See [Response length and verbosity](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity).

2.  **More literal instruction following:** Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It does not silently generalize an instruction from one item to another, and it does not infer requests you didn't make. The upside of this literalism is precision and less thrash. It generally performs better for API use cases with carefully tuned prompts, structured extraction, and pipelines where you want predictable behavior. A prompt and harness review may be especially helpful for migration to Claude Opus 5.

3.  **More direct tone:** As with any new model, prose style on long-form writing may shift. Claude Opus 4.7 is more direct and opinionated, with less validation-forward phrasing and fewer emoji than Claude Opus 4.6's warmer style. If your product relies on a specific voice, re-evaluate style prompts against the new baseline.

4.  **Built-in progress updates in agentic traces:** Claude Opus 4.7 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages ("After every 3 tool calls, summarize progress"), try removing it. If you find that the length or contents of Claude Opus 4.7's user-facing updates are not well-calibrated to your use case, explicitly describe what these updates should look like in the prompt and provide examples.

5.  **Subagent spawning changed:** Claude Opus 4.7 tends to spawn fewer subagents by default than Claude Opus 4.6, while Claude Opus 5 delegates to subagents more readily than earlier models. The behavior is steerable through prompting in either direction; give explicit guidance around when subagents are desirable, or cap the number of subagents. See [Controlling subagent spawning](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#controlling-subagent-spawning).

6.  **Stricter effort calibration:** Meaningfully changing from Claude Opus 4.6, Claude Opus 4.7 respects [effort levels](../04-API-Reference/Guides/build-with-claude-effort.md) strictly, especially at the low end. At `low` and `medium`, the model scopes its work to what was asked rather than doing more than requested.

    This is good for latency and cost, but on moderately complex tasks running at `low` effort there is some risk of under-thinking. If you observe shallow reasoning on complex problems, raise effort to `high` or `xhigh` rather than prompting around it.

    If you need to keep effort at `low` for latency, add targeted guidance: "This task involves multistep reasoning. Think carefully through the problem before responding." See [Recommended effort levels for Claude Opus 4.7](../04-API-Reference/Guides/build-with-claude-effort.md#recommended-effort-levels-for-claude-opus-4-7).

7.  **Fewer tool calls by default:** Claude Opus 4.7 has a tendency to use tools less often than Claude Opus 4.6 and to use reasoning more. This produces better results in most cases.

    To increase tool usage, raise the effort setting. `high` or `xhigh` effort settings show substantially more tool usage in agentic search and coding. You can also adjust your prompt to explicitly instruct the model about when and how to properly use its tools.

8.  **Real-time cybersecurity safeguards:** Newly added in Claude Opus 4.7, requests that involve prohibited or high-risk topics may lead to refusals. For legitimate security work such as penetration testing, vulnerability research, or red-teaming, apply to the [Cyber Verification Program](real-time-cyber-safeguards-on-claude-opus-and-sonnet.md) to request reduced restrictions. The application route depends on how you access Claude.

9.  **High-resolution image support:** Claude Opus 4.7 is the first Claude model with high-resolution image support. Maximum image resolution is 2,576 pixels on the long edge, up from 1,568 pixels on prior models. This unlocks gains on vision-heavy workloads and is particularly valuable for computer use, screenshot understanding, and document analysis.

    High-resolution support is automatic and requires no beta header or client-side opt-in. Two things to plan for:

    - Full-resolution images can use up to approximately 3x more image tokens than on prior models (up to 4,784 tokens per image, compared to the previous cap of roughly 1,600 tokens per image). Re-budget `max_tokens` and cost expectations for image-heavy workloads, or downsample before sending if you do not need the additional fidelity.
    - Pointing and bounding-box coordinates returned by the model are 1:1 with actual image pixels on Claude Opus 4.7, so no scale-factor conversion is required.

    See [High-resolution image support on Claude Opus 4.7](../04-API-Reference/Guides/build-with-claude-vision.md#high-resolution-image-support-on-claude-opus-4-7) for details.

### Recommended changes

These are not required but will improve your experience:

1.  **Re-evaluate `max_tokens`:** Because the same text produces a higher token count on Claude Opus 4.7 and later models, update your `max_tokens` parameters to give additional headroom, including compaction triggers. Prompting interventions, [`task_budget`](../04-API-Reference/Guides/build-with-claude-task-budgets.md), and [`effort`](../04-API-Reference/Guides/build-with-claude-effort.md) can help control costs and ensure appropriate token usage.

2.  **Audit token-count expectations:** Any code path that estimates tokens client-side or assumes a fixed token-to-character ratio should be re-tested against Claude Opus 5. Use the [Token counting endpoint](../04-API-Reference/Guides/build-with-claude-token-counting.md) to verify.

3.  **Adopt [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) (beta):** Claude Opus 4.7 introduces task budgets. These budgets let you inform Claude how many tokens it has for a full agentic loop, including thinking, tool calls, tool results, and final output. The model sees a running countdown and uses it to prioritize work and finish the task gracefully as the budget is consumed. To use, set the beta header `task-budgets-2026-03-13` and add the following to your output config:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    output_config = {
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 128000},
    }
    ```

    You may need to experiment with different task budgets for your use case. If the model is given a task budget that is too restrictive, it may complete the task less thoroughly, referencing its budget as the constraint.

    For open-ended agentic tasks where quality matters more than speed, do not set a task budget. Reserve task budgets for workloads where you need the model to scope its work to a token allowance. The minimum value for a task budget is 20k tokens.

    A task budget is not a hard cap; it's a suggestion that the model is aware of. It differs from `max_tokens`:

    - **`task_budget`:** an advisory cap across the full agentic loop. The model sees it and uses it to pace itself.
    - **`max_tokens`:** a hard per-request ceiling on generated tokens. It is not passed to the model, so the model is not aware of it.

    Use `task_budget` when you want the model to self-moderate, and `max_tokens` as a hard ceiling to cap usage.

4.  **Set a large `max_tokens` at `max` or `xhigh` effort:** If you are running Claude Opus 4.7 or a later model at `max` or `xhigh` effort, set a large max output token budget so the model has room to think and act across its subagents and tool calls. Start at 64k tokens and tune from there.

5.  **Downsample images if high resolution is unnecessary:** Claude Opus 4.7 and later models support images up to 2576px / 3.75MP. High-res images use more tokens. If the additional image fidelity is unnecessary, downsample images before sending to Claude to avoid token-usage increases. See [Images and vision](../04-API-Reference/Guides/build-with-claude-vision.md).

6.  **Consider automatic fallbacks:** Claude Opus 5 ships with cybersecurity safety classifiers whose cyber-category refusals can fall back to Claude Opus 4.8. To re-run refused requests on another model automatically, consider the `fallbacks` parameter with the `"default"` mode (`fallbacks: "default"`), which selects a recommended fallback model based on the refusal category instead of a hand-maintained model list. Server-side fallback is in beta; the `"default"` mode requires the `server-side-fallback-2026-07-01` beta header. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

7.  **Cache shorter prompts:** The minimum cacheable prompt length on Claude Opus 5 is 512 tokens, lower than on earlier Opus models. Prompts that were too short to cache can now create cache entries, with no code changes required. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations) for per-model minimums.

8.  **Change tools mid-conversation (beta):** You can add or remove tools between turns of a conversation without invalidating [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits on earlier turns. Send the beta header `mid-conversation-tool-changes-2026-07-01`. This is useful for agentic workloads that expose tools progressively or retire them as a task advances; without it, a changed tool list invalidates the cached prefix.

9.  **Remove carried-over verification instructions and constrain scope:** Claude Opus 5 verifies its own work without being told to, so remove explicit verification or self-check instructions carried over from prompts tuned for earlier models; leaving them in causes over-verification. For narrow tasks, constrain the task scope explicitly. See [Task scope and over-verification](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#task-scope-and-over-verification).

### Migration checklist

- Update model name from `claude-opus-4-6` to `claude-opus-5` (or update aliases).
- Remove `temperature`, `top_p`, and `top_k` from request payloads.
- Replace `thinking: {type: "enabled", budget_tokens: N}` with `thinking: {type: "adaptive"}` plus the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md), or remove the `thinking` field entirely; adaptive thinking is on by default on Claude Opus 5.
- Review workloads that ran without a `thinking` field: they run with thinking on Claude Opus 5. Revisit `max_tokens`, which remains a hard limit on total output (thinking plus response text), or pass `thinking: {type: "disabled"}` at effort `high` or below to preserve the old behavior.
- Update response parsing that reads content by position, such as `content[0].text` or a stream handler that assumes the first content block is text: with thinking on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead.
- If you run a tool-use loop, pass `thinking` blocks back complete and unmodified when you return tool results; modified blocks return a 400 error. See [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).
- Audit requests that disable thinking: `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error, enforced on each request. Re-enable thinking or lower the effort to `high` or below.
- Remove any assistant-message prefills.
- If your UI displays thinking content, explicitly opt in to thinking summarization.
- Re-benchmark end-to-end cost and latency under the updated tokenization; thinking tokens are billed as output tokens, so workloads that ran without thinking can also produce more output tokens per request.
- Re-tune `max_tokens` to account for the updated tokenization.
- Re-test any client-side token-count estimations.
- If your application sends images, re-budget for [high-resolution image support](../04-API-Reference/Guides/build-with-claude-vision.md#high-resolution-image-support-on-claude-opus-4-7) (up to approximately 3x more image tokens per full-resolution image). Downsample before sending if you do not need the additional fidelity.
- If you consume pointing or bounding-box coordinates from the model, remove any scale-factor conversion; coordinates are 1:1 with actual image pixels on Claude Opus 4.7 and later models.
- Review prompts for the behavior changes (response length, literalism, tone, progress updates, subagents, effort calibration, tool triggering, cyber safeguards, high-resolution image handling).
- Re-baseline response length with existing length-control prompts removed, then tune explicitly.
- If using `xhigh` or `max` effort, raise `max_tokens` to at least 64k as a starting point.
- Consider adopting task budgets (beta) and mid-conversation tool changes (beta) for agentic workflows.
- Handle `stop_reason: "refusal"`, and consider `fallbacks: "default"` (beta) to re-run refused requests on a recommended fallback model automatically.
- Review prompts near the caching minimum: prompts of 512 tokens or more can now create cache entries on Claude Opus 5.
- If you use [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md), plan an alternative: it is not available on Claude Opus 5.
- If your organization has a [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) commitment, note that Priority Tier is not supported on Claude Opus 5.
- Remove verification and self-check instructions carried over from prompts tuned for earlier models; they cause over-verification on Claude Opus 5.
- If your product does legitimate security work, apply to the [Cyber Verification Program](real-time-cyber-safeguards-on-claude-opus-and-sonnet.md) for access to lower restrictions on cyber content.

### Migrating from Claude Opus 4.5 or earlier

If you are migrating from Claude Opus 4.5, Opus 4.1, or an earlier model directly to Claude Opus 5, apply **all of the changes earlier in this section** plus the following cumulative changes, which took effect between Opus 4.5 and Opus 4.7. If you are migrating from Opus 4.6, the changes earlier in this section are all you need.

#### Update your model name

```python
# Opus migration
model = "claude-opus-4-5"  # Before
model = "claude-opus-5"  # After
```



#### Breaking changes

1.  **Prefill removal** is covered in the [breaking changes for migrating from Claude Opus 4.6](#opus-46-breaking-changes).

2.  **Tool parameter quoting:** Claude Opus 4.6 and later models may produce slightly different JSON string escaping in tool call arguments (for example, different handling of Unicode escapes or forward slash escaping). If you parse tool call `input` as a raw string rather than using a JSON parser, verify your parsing logic. Standard JSON parsers (such as `json.loads()` or `JSON.parse()`) handle these differences automatically.

#### Recommended changes

These changes improve your experience on Claude Opus 4.7 and later models. Items marked **(required on Opus 4.7)** were optional recommendations when Opus 4.6 launched but are now mandatory; the rest remain recommended.

1.  **Migrate to adaptive thinking (required on Opus 4.7):** `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error on Claude Opus 4.7 and later models. Switch to `thinking: {type: "adaptive"}` and use the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) to control thinking depth; on Claude Opus 5, `thinking: {type: "adaptive"}` is equivalent to omitting the `thinking` field, which runs with adaptive thinking by default. See [Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md).

    cURL
    Before
    After
    CLI
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    response = client.beta.messages.create(
        model="claude-opus-4-5",
        max_tokens=16000,
        thinking={"type": "enabled", "budget_tokens": 32000},
        betas=["interleaved-thinking-2025-05-14"],
        messages=[{"role": "user", "content": "Your prompt here"}],
    )
    ```

    Note that the migration also moves from `client.beta.messages.create` to `client.messages.create`. Adaptive thinking and effort do not require the beta SDK namespace or any beta headers.

2.  **Remove effort beta header:** The effort parameter does not require a beta header. Remove `betas=["effort-2025-11-24"]` from your requests.

3.  **Remove fine-grained tool streaming beta header:** Fine-grained tool streaming does not require a beta header. Remove `betas=["fine-grained-tool-streaming-2025-05-14"]` from your requests.

4.  **Remove interleaved thinking beta header:** Adaptive thinking automatically enables interleaved thinking on Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. Remove `betas=["interleaved-thinking-2025-05-14"]` from your requests. The header is still functional on Sonnet 4.6 with manual extended thinking, but manual mode is deprecated.

5.  **Migrate to output_config.format:** If using structured outputs, update `output_format={...}` to `output_config={"format": {...}}`. The API still accepts the deprecated `output_format` parameter, but it will be removed in a future model release. The Python SDK (v1.0 and later) does not accept `output_format={...}` on `client.beta.messages.create()` or `count_tokens()`. The `output_format=Model` argument of the `parse()` and `stream()` helpers is unchanged.

### Migrating from Claude 4.1 or earlier

If you're migrating from Opus 4.1 or earlier models directly to Claude Opus 5, apply all of the changes earlier in this section, plus the additional changes in this sub-section.

```python
# From Opus 4.1
model = "claude-opus-4-1-20250805"  # Before
model = "claude-opus-5"  # After

# From Sonnet 3.7
model = "claude-3-7-sonnet-20250219"  # Before
model = "claude-opus-5"  # After
```



#### Additional breaking changes

1.  **Remove sampling parameters**

    

    This is a breaking change when migrating from Claude 3.x models.

    Starting with Claude Opus 4.7, setting `temperature`, `top_p`, or `top_k` to any non-default value returns a 400 error. The Python SDK (v1.0 and later) does not define them, and passing them raises a `TypeError`. The safest migration path is to omit these parameters entirely from requests, and to use prompting to guide the model's behavior. If you were using `temperature = 0` for determinism, note that it never guaranteed identical outputs.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    # Before - This will error in Claude 4+ models
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        temperature=0.7,
        top_p=0.9,  # Non-default sampling params return 400 on Opus 4.7
        # ...
    )

    # After
    response = client.messages.create(
        model="claude-opus-5",
        # ...
    )
    ```

2.  **Update tool versions**

    

    This is a breaking change when migrating from Claude 3.x models.

    Update to the latest tool versions. Remove any code using the `undo_edit` command.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    # Before
    tools = [{"type": "text_editor_20250124", "name": "str_replace_editor"}]

    # After
    tools = [{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
    ```

    - **Text editor:** Use `text_editor_20250728` and `str_replace_based_edit_tool`. See [Text editor tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md) documentation for details.
    - **Code execution:** Upgrade to `code_execution_20260521`. See [Code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#upgrade-to-latest-tool-version) documentation for migration instructions.

3.  **Handle the `refusal` stop reason**

    Update your application to [handle `refusal` stop reasons](../04-API-Reference/Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md):

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    response = client.messages.create(...)

    if response.stop_reason == "refusal":
        # Handle refusal appropriately
        pass
    ```

4.  **Handle the `model_context_window_exceeded` stop reason**

    Claude 4.5+ models return a `model_context_window_exceeded` stop reason when generation stops because of hitting the context window limit, rather than the requested `max_tokens` limit. Update your application to handle this new stop reason:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    response = client.messages.create(...)

    if response.stop_reason == "model_context_window_exceeded":
        # Handle context window limit appropriately
        pass
    ```

5.  **Verify tool parameter handling (trailing newlines)**

    Claude 4.5+ models preserve trailing newlines in tool call string parameters that were previously stripped. If your tools rely on exact string matching against tool call parameters, verify your logic handles trailing newlines correctly.

6.  **Update your prompts for behavioral changes**

    Claude 4+ models have a more concise, direct communication style and require explicit direction. Review [prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md) for optimization guidance.

#### Additional recommended changes

- **Remove legacy beta headers:** Remove `token-efficient-tools-2025-02-19` and `output-128k-2025-02-19`. All Claude 4+ models have built-in token-efficient tool use and these headers have no effect.

### Migration checklist (from Claude Opus 4.5 or earlier)

- Update model ID to `claude-opus-5`
- Apply all of the [breaking changes for migrating from Claude Opus 4.6](#opus-46-breaking-changes) (extended thinking removed, thinking on by default, effort cap on disabling thinking, sampling parameters removed, thinking display omitted by default, updated tokenization)
- **BREAKING:** Remove assistant message prefills (returns 400 error); use structured outputs or `output_config.format` instead
- **BREAKING on Opus 4.7:** Replace `thinking: {type: "enabled", budget_tokens: N}` with `thinking: {type: "adaptive"}` plus the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) (returns 400 on Opus 4.7)
- Verify tool call JSON parsing uses a standard JSON parser
- Remove `effort-2025-11-24` beta header (the effort parameter does not require it)
- Remove `fine-grained-tool-streaming-2025-05-14` beta header
- Remove `interleaved-thinking-2025-05-14` beta header (adaptive thinking enables interleaved thinking automatically)
- Migrate `output_format` to `output_config.format` (if applicable)
- If migrating from Claude 4.1 or earlier: remove `temperature`, `top_p`, and `top_k` (non-default values return 400 on Opus 4.7)
- If migrating from Claude 4.1 or earlier: update tool versions (`text_editor_20250728`, `code_execution_20260521`)
- If migrating from Claude 4.1 or earlier: handle `refusal` stop reason
- If migrating from Claude 4.1 or earlier: handle `model_context_window_exceeded` stop reason
- If migrating from Claude 4.1 or earlier: verify tool string parameter handling for trailing newlines
- If migrating from Claude 4.1 or earlier: remove legacy beta headers (`token-efficient-tools-2025-02-19`, `output-128k-2025-02-19`)
- Review and update prompts following [prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)
- Test in development environment before production deployment

## Migrating to Claude Opus 5 from Claude Sonnet 5

Claude Opus 5 and Claude Sonnet 5 share the same API surface: both run with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) on by default, both default the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) to `high` on the Claude API and Claude Code, both serve a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default with [128k max output tokens](about-claude-models-overview.md), and neither supports [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models). Manual extended thinking and non-default sampling parameters return a 400 error on both models, as does assistant prefill.

### Update your model name

```python
model = "claude-sonnet-5"  # Before
model = "claude-opus-5"  # After
```



### What changed

1.  **Pricing:** Claude Opus 5 is priced at \$5 USD per million input tokens and \$25 USD per million output tokens. Claude Sonnet 5 is priced at \$2/\$10 USD per million input/output tokens. See [Claude pricing](../17-Billing-Plans/about-claude-pricing.md) for complete pricing.

2.  **Disabling thinking is capped at `high` effort:** On Claude Sonnet 5, `thinking: {type: "disabled"}` is accepted at any effort level. On Claude Opus 5, it is accepted only at an [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level of `high` or below; a request that combines `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error, enforced on each request. Audit requests that disable thinking before you migrate.

3.  **Mid-conversation system messages:** Claude Opus 5 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#limitations)). This feature is not available on Claude Sonnet 5. If you maintain code paths that rebuild the full message history to update instructions, you can simplify them and preserve [prompt cache](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) hits on earlier turns.

4.  **Web fetch is not available:** The [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) tool is available on Claude Sonnet 5 but not on Claude Opus 5.

### Migration checklist

- Update the model name from `claude-sonnet-5` to `claude-opus-5`.
- Audit requests that disable thinking: `thinking: {type: "disabled"}` with effort `xhigh` or `max` returns a 400 error on Claude Opus 5. Re-enable thinking or lower the effort to `high` or below.
- If you use [web fetch](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md), plan an alternative: it is not available on Claude Opus 5.
- Re-run [token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) against Claude Opus 5 rather than reusing counts measured against Claude Sonnet 5, and re-baseline cost and latency on your own workloads; per-token pricing differs.
