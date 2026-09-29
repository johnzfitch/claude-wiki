---
title: "Migrating to Claude Sonnet 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/sonnet-5/migration-guide"
category: "20-Models"
fetched_at: "2026-09-26T06:39:47Z"
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fsonnet-5%2Fmigration-guide)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Overview](/docs/en/models/sonnet-5/overview)[What's new](/docs/en/models/sonnet-5/whats-new-sonnet-5)[Migration guide](/docs/en/models/sonnet-5/migration-guide)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

[Models & pricing](/docs/en/models/overview)Claude Sonnet 5

# Migrating to Claude Sonnet 5

Copy page



Migrate to Claude Sonnet 5 from earlier Claude models: model IDs, breaking changes, and migration checklists.

Copy page





This guide covers migrating [Messages API](/docs/en/build-with-claude/working-with-messages) code. If you use [Claude Managed Agents](/docs/en/managed-agents/overview), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-sonnet-5
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

Claude Sonnet 5 offers the best combination of speed and intelligence in the Claude model family. It builds on Claude Sonnet 4.6.

Claude Sonnet 5 is a drop-in upgrade for Claude Sonnet 4.6, priced at \$2/\$10 USD per million input/output tokens; see [Pricing](/docs/en/about-claude/pricing) for details. There are two breaking API changes for code already running on Claude Sonnet 4.6. First, [adaptive thinking](/docs/en/build-with-claude/thinking) is on by default and manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) returns a 400 error, so requests that ran without thinking can now return `thinking` blocks before the first `text` block and code that reads content by position must select content blocks by `type`. Second, sampling parameters (`temperature`, `top_p`, `top_k`) set to non-default values return a 400 error. Use adaptive thinking with the [effort parameter](/docs/en/build-with-claude/effort) to control thinking depth. Claude Sonnet 5 supports the same set of features as Claude Sonnet 4.6, including the [1M token context window](/docs/en/build-with-claude/context-windows), [adaptive thinking](/docs/en/build-with-claude/thinking), [prompt caching](/docs/en/build-with-claude/prompt-caching), [batch processing](/docs/en/build-with-claude/batch-processing), the [Files API](/docs/en/build-with-claude/files), [PDF support](/docs/en/build-with-claude/pdf-support), [vision](/docs/en/build-with-claude/vision), and the full set of server-side and client-side [tools](/docs/en/agents-and-tools/tool-use/overview). On the Claude API and Google Cloud, Claude Sonnet 5 also supports [computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) as the stable `computer_toolset_20260801` toolset and the [browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool) for tasks inside webpages, neither of which Claude Sonnet 4.6 supports; existing integrations on the earlier `computer_20251124` version continue to work unchanged on both models. To upgrade an existing integration, see [Migrate from `computer_20251124`](/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124). [Priority Tier](/docs/en/api/service-tiers#supported-models) is not available on Claude Sonnet 5. Claude Sonnet 5 also uses a new tokenizer.

## Migrating to Claude Sonnet 5 from Claude Sonnet 4.6



If your code is on Claude Sonnet 4.5 or earlier, also apply [Migrating to Claude Sonnet 5 from Claude Sonnet 4.5 and earlier Sonnet models](#migrating-from-sonnet-45). Those steps include breaking changes (assistant message prefilling rejected, tool parameter JSON escaping differences) that this section alone does not cover.

### Update your model name

```python
# Sonnet migration
model = "claude-sonnet-4-6"  # Before
model = "claude-sonnet-5"  # After
```



### What changed

Items 4 and 5 in the following list are breaking changes. `max_tokens` remains a hard limit on total output (thinking plus response text), so revisit it for workloads that ran without thinking on Claude Sonnet 4.6.

1.  **New tokenizer:** Claude Sonnet 5 uses a new tokenizer. The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6. The exact increase depends on the content. Requests, responses, and streaming events keep the same shape, and no code changes are required, but anything you measure or budget in tokens shifts: `usage` fields and [token counting](/docs/en/build-with-claude/token-counting) results for the same text are higher, the 1M token context window holds less text, and a `max_tokens` limit tuned for Claude Sonnet 4.6 may truncate equivalent output. Per-token pricing is lower (\$2/\$10 USD versus Claude Sonnet 4.6's \$3/\$15 USD per million input/output tokens), but the cost of an equivalent request does not drop in direct proportion. Re-run token counting against Claude Sonnet 5 rather than reusing counts measured against earlier models.

2.  **128k max output tokens (unchanged):** Claude Sonnet 5 supports up to 128k output tokens, the same as Claude Sonnet 4.6. Existing `max_tokens` values remain valid. Account for the new tokenizer when sizing them.

3.  **Assistant message prefilling (unchanged):** Prefilling the assistant message returns a `400` error on Claude Sonnet 5, the same as on Claude Sonnet 4.6. If you removed prefill when migrating to Claude Sonnet 4.6, no further changes are needed. Use [structured outputs](/docs/en/build-with-claude/structured-outputs), system prompt instructions, or `output_config.format` instead.

4.  **Adaptive thinking on by default:** On Claude Sonnet 4.6, requests without a `thinking` field run without thinking; on Claude Sonnet 5, the same requests run with [adaptive thinking](/docs/en/build-with-claude/thinking). To turn thinking off, pass `thinking: {type: "disabled"}`. Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported and returns a 400 error. Use the [effort parameter](/docs/en/build-with-claude/effort) (default `high`) to control thinking depth.

    With thinking on, a response can begin with one or more `thinking` blocks before the first `text` block, returned with an empty `thinking` field at the default `display: "omitted"`. Code that reads the reply by position, such as `content[0].text` or a stream handler that treats the first content block as text, must select content blocks by their `type` field instead, and tool-use loops must pass `thinking` blocks back complete and unmodified with their tool results (see [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks)). Thinking tokens are billed as output tokens even when the thinking text is not returned. If you used thinking on Claude Sonnet 4.6 and display the returned thinking text, note that `thinking.display` defaulted to `"summarized"` there and defaults to `"omitted"` on Claude Sonnet 5; set `display: "summarized"`, as the following example does, to keep receiving readable summaries (see [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display)).

    Claude Sonnet 5
    Claude Sonnet 4.6

    
    Adaptive thinking is on by default for Claude Sonnet 5. The `thinking` field is shown explicitly here to set `display: "summarized"`; if you omit `thinking`, Claude Sonnet 5 omits thinking content from the response by default. For per-model defaults, see [Configurations each model rejects](/docs/en/build-with-claude/thinking-troubleshooting#rejected-configurations).

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

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=16000,
        thinking={"type": "adaptive", "display": "summarized"},
        output_config={"effort": "high"},
        messages=[
            {
                "role": "user",
                "content": "Find all pairs of positive integers (x, y) such that x^2 - y^2 = 2024.",
            }
        ],
    )

    # The response contains summarized thinking blocks and text blocks
    for block in response.content:
        match block.type:
            case "thinking":
                print(f"\nThinking summary: {block.thinking}")
            case "text":
                print(f"\nResponse: {block.text}")
    ```

5.  **Sampling parameters removed:** Sampling parameters (`temperature`, `top_p`, `top_k`) set to a non-default value are not accepted and return a 400 error.

6.  **Cybersecurity safeguards:** Claude Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards. Requests that involve prohibited or high-risk cybersecurity topics may be refused. Refusals return as a successful HTTP 200 response with `stop_reason: "refusal"`, not an error. See [Real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet) for what the safeguards block and how legitimate security work can apply to the Cyber Verification Program.

### Migration checklist

- Update model name from `claude-sonnet-4-6` to `claude-sonnet-5`.
- Re-run [token counting](/docs/en/build-with-claude/token-counting) against Claude Sonnet 5. The new tokenizer produces approximately 30% more tokens for the same text, which can change per-request cost even though per-token pricing is lower. The exact increase depends on the content and workload shape.
- Revisit `max_tokens` limits sized close to your expected output length, and raise them up to the 128k maximum (unchanged from Claude Sonnet 4.6) where useful.
- Remove `thinking: {type: "enabled", budget_tokens: N}` configuration (returns a 400 error). Adaptive thinking is on by default; pass `{type: "disabled"}` to turn it off, or use the [effort parameter](/docs/en/build-with-claude/effort) to control depth.
- Update response parsing that reads content by position, such as `content[0].text`: with thinking on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead, and pass `thinking` blocks back unmodified in tool-use loops; modified blocks return a 400 error.
- Verify any code that parses the `thinking` field treats it as display text only. `thinking.display` defaults to `"omitted"` on Claude Sonnet 5 (it defaulted to `"summarized"` on Claude Sonnet 4.6), so thinking blocks arrive with an empty `thinking` field; set `display: "summarized"` to receive readable summaries. See [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display).
- Remove `temperature`, `top_p`, and `top_k` parameters set to non-default values (they return a 400 error on Claude Sonnet 5).
- Add handling for `stop_reason: "refusal"` if your workload may touch cybersecurity topics.
- Re-baseline cost on your typical workload before production deployment.
- Review `max_tokens` for workloads that previously ran without thinking.

## Migrating to Claude Sonnet 5 from Claude Sonnet 4.5 and earlier Sonnet models

If you are migrating from Claude Sonnet 4.5 or an earlier Sonnet model directly to Claude Sonnet 5, apply the [Migrating to Claude Sonnet 5 from Claude Sonnet 4.6](#migrating-from-claude-sonnet-4-6-to-claude-sonnet-5) changes plus the changes in this section.



Claude Sonnet 5 defaults to an effort level of `high`, in contrast to Sonnet 4.5 which had no effort parameter. Consider adjusting the [effort parameter](/docs/en/build-with-claude/effort) as you migrate. If not explicitly set, you may experience higher latency with the default effort level.

### Breaking changes

#### When migrating from Sonnet 4.5

1.  **Prefilling assistant messages is no longer supported**

    

    This is a breaking change when migrating from Sonnet 4.5 or earlier.

    Prefilling assistant messages returns a `400` error on Claude Sonnet 4.6 and later models, including Claude Sonnet 5. Use [structured outputs](/docs/en/build-with-claude/structured-outputs), system prompt instructions, or `output_config.format` instead.

    **Common prefill use cases and migrations:**

    - **Controlling output formatting** (forcing JSON/YAML output): Use [structured outputs](/docs/en/build-with-claude/structured-outputs) or tools with enum fields for classification tasks.

    - **Eliminating preambles** (removing "Here is..." phrases): Add direct instructions in the system prompt: "Respond directly without preamble. Do not start with phrases like 'Here is...', 'Based on...', etc."

    - **Avoiding bad refusals:** Claude is much better at appropriate refusals now. Clear prompting in the user message without prefill should be sufficient.

    - **Continuations** (resuming interrupted responses): Move the continuation to the user message: "Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off."

    - **Context hydration / role consistency** (refreshing context in long conversations): Inject what were previously prefilled-assistant reminders into the user turn instead.

2.  **Tool parameter JSON escaping may differ**

    

    This is a breaking change when migrating from Sonnet 4.5 or earlier.

    JSON string escaping in tool parameters may differ from previous models. Standard JSON parsers handle this automatically, but custom string-based parsing may need updates.

**Extended thinking changes:** `budget_tokens` configurations from Claude Sonnet 4.5 (`thinking: {type: "enabled", budget_tokens: N}`) are not supported on Claude Sonnet 5 and return a 400 error. Adaptive thinking is on by default, so most workloads need no `thinking` configuration at all; use the [effort parameter](/docs/en/build-with-claude/effort) to control thinking depth. If you ran Claude Sonnet 4.5 without extended thinking, pass `thinking: {type: "disabled"}` to preserve that behavior.

#### When migrating from Claude 3.x

3.  **Remove sampling parameters**

    

    This is a breaking change when migrating from Claude 3.x models.

    Sampling parameters (`temperature`, `top_p`, `top_k`) set to a non-default value return a 400 error on Claude Sonnet 5. Remove them from requests, and use prompting to guide the model's behavior instead.

4.  **Update tool versions**

    

    This is a breaking change when migrating from Claude 3.x models.

    Update to the latest tool versions (`text_editor_20250728`, `code_execution_20260521`). Remove any code using the `undo_edit` command.

5.  **Handle the `refusal` stop reason**

    Update your application to [handle `refusal` stop reasons](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

6.  **Update your prompts for behavioral changes**

    Claude 4 models have a more concise, direct communication style. Review [prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for optimization guidance.

## Migrating to Claude Sonnet 5 from Claude Haiku 4.5

Claude Haiku 4.5 and Claude Sonnet 5 differ more at the API level than adjacent models within one class: Claude Haiku 4.5 uses manual [extended thinking](/docs/en/build-with-claude/extended-thinking) (off by default), a 200k token context window, and up to 64k output tokens, while Claude Sonnet 5 runs with [adaptive thinking](/docs/en/build-with-claude/thinking) on by default, serves a [1M token context window](/docs/en/build-with-claude/context-windows) by default, and supports up to [128k output tokens](/docs/en/models/overview).

### Update your model name

```python
model = "claude-haiku-4-5-20251001"  # Before
model = "claude-sonnet-5"  # After
```



### What changed

1.  **Thinking configuration:** Claude Haiku 4.5 supports manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) and rejects `thinking: {type: "adaptive"}`. On Claude Sonnet 5, the support is reversed: adaptive thinking is on by default, and manual extended thinking returns a 400 error. Remove `thinking: {type: "enabled", budget_tokens: N}` configurations and rely on the default, or pass `thinking: {type: "disabled"}` to turn thinking off. `budget_tokens` has no direct replacement; use the [effort parameter](/docs/en/build-with-claude/effort) to control thinking depth. Effort is not available on Claude Haiku 4.5 and defaults to `high` on Claude Sonnet 5.

    The response shape changes for both kinds of Claude Haiku 4.5 request. Requests that ran without extended thinking can now return one or more `thinking` blocks before the first `text` block, so code that reads the reply by position, such as `content[0].text`, must select content blocks by their `type` field instead, and tool-use loops must pass `thinking` blocks back complete and unmodified with their tool results (see [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks)). Requests that used extended thinking keep receiving `thinking` blocks, but `thinking.display` defaults to `"omitted"` on Claude Sonnet 5 rather than `"summarized"`, so those blocks arrive with an empty `thinking` field; set `display: "summarized"` to keep receiving readable summaries (see [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display)). Thinking tokens are billed as output tokens even when the thinking text is not returned.

2.  **Sampling parameters removed:** `temperature` and `top_p` work on Claude Haiku 4.5 (one at a time, not both). On Claude Sonnet 5, setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error. Remove these parameters and use prompting to guide the model's behavior.

3.  **Assistant prefill removed:** Prefilling the assistant message works on Claude Haiku 4.5 but returns a 400 error on Claude Sonnet 5. Use [structured outputs](/docs/en/build-with-claude/structured-outputs), system prompt instructions, or `output_config.format` instead.

4.  **Larger context window and output:** Claude Sonnet 5 serves a 1M token context window by default, up from 200k tokens on Claude Haiku 4.5, and supports up to 128k output tokens, up from 64k. Claude Sonnet 5 also uses a different tokenizer, so re-run [token counting](/docs/en/build-with-claude/token-counting) rather than reusing counts measured against Claude Haiku 4.5.

5.  **Pricing:** Claude Haiku 4.5 is priced at \$1/\$5 USD per million input/output tokens. Claude Sonnet 5 is priced at \$2/\$10 USD per million input/output tokens. See [Claude pricing](/docs/en/about-claude/pricing).

6.  **Cybersecurity safeguards:** Claude Sonnet 5 has real-time cybersecurity safeguards. Requests that involve prohibited or high-risk cybersecurity topics may be refused, returned as a successful HTTP 200 response with `stop_reason: "refusal"`. See [Real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet) for what the safeguards block and how legitimate security work can apply to the Cyber Verification Program.

### Migration checklist

- Update the model name from `claude-haiku-4-5-20251001` (or the `claude-haiku-4-5` alias) to `claude-sonnet-5`.
- Remove `thinking: {type: "enabled", budget_tokens: N}` configuration (returns a 400 error). Adaptive thinking is on by default; pass `thinking: {type: "disabled"}` to preserve no-thinking behavior, and revisit `max_tokens` for workloads that ran without thinking.
- Update response parsing that reads content by position, such as `content[0].text`: with thinking on, `thinking` blocks arrive before `text` blocks. Select content blocks by `type` instead, and pass `thinking` blocks back unmodified in tool-use loops; modified blocks return a 400 error.
- If your UI displays thinking content, set `display: "summarized"`. `thinking.display` defaults to `"omitted"` on Claude Sonnet 5, so thinking blocks otherwise arrive with an empty `thinking` field. See [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display).
- Use the [effort parameter](/docs/en/build-with-claude/effort) (default `high`) to control thinking depth and token spend; it is not available on Claude Haiku 4.5, so no existing setting carries over.
- Remove `temperature` and `top_p` settings (non-default values return a 400 error on Claude Sonnet 5).
- Remove any assistant-message prefills (they return a 400 error on Claude Sonnet 5).
- Re-run [token counting](/docs/en/build-with-claude/token-counting) against Claude Sonnet 5, and revisit `max_tokens` limits, which you can raise up to the 128k maximum.
- Add handling for `stop_reason: "refusal"` if your workload may touch cybersecurity topics.
- Re-baseline cost on your typical workload before production deployment; per-token pricing differs.
