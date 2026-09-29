---
title: "Troubleshooting tool use - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:18Z"
tags: ["api", "prompting"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftroubleshooting-tool-use)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Tools

# Troubleshooting tool use

Copy page



Fix the most common tool-use errors with symptom-to-fix diagnostic tables.

Copy page



Symptom-to-fix tables for the most common tool-use errors. Each fix cross-references the page that owns the feature.

## Claude calls the wrong tool

| Symptom                                    | Likely cause                                 | Fix                                                                                                                                                        |
|--------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude calls tool A when you wanted tool B | Description ambiguity                        | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](agents-and-tools-tool-use-implement-tool-use.md). |
| Claude never calls your tool               | Tool name collision or overly-generic schema | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete.                                                   |
| Claude calls with wrong parameter types    | Model guessing at ambiguous schema           | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`.                                                                    |

## Claude invents tool parameters

| Symptom                                     | Likely cause                              | Fix                                                                                                                 |
|---------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Parameter that doesn't exist in your schema | Model over-generation without strict mode | Add `strict: true` if your schema is in the [supported subset](agents-and-tools-tool-use-strict-tool-use.md). |
| Parameter values outside your enum          | Missing strict mode or too-large enum     | Shrink the enum or add `input_examples` showing valid choices.                                                      |

## Parallel tool calls don't work

| Symptom                                                       | Likely cause                     | Fix                                                                                                                                                      |
|---------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude calls tools sequentially when parallel would be better | Message history formatting       | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md). |
| `disable_parallel_tool_use` seems ignored                     | Set too late in the conversation | Must be set on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls.                                   |

## Cache keeps invalidating

| Symptom                                     | Likely cause                                                                                  | Fix                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Every request is a cache miss               | `tool_choice`, the thinking configuration, or `output_config.effort` varying between requests | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point; hold the thinking configuration and effort level constant for the life of a cached conversation. See [Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md) and [Thinking and prompt caching](../Guides/build-with-claude-thinking.md#thinking-and-prompt-caching). |
| Adding a tool mid-conversation breaks cache | Tool prepended to the tools array                                                             | Use `defer_loading: true` with tool search to append the tool inline instead of modifying the array head.                                                                                                                                                                                                                                                                                              |

## Errors at request time

| Error                                                                  | Cause                                                                                                                                                                                                                                                                                                                                                                    | Fix                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tool_use ids were found without tool_result blocks immediately after` | Missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message                                                                                                                                                                                                                                                       | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md) and [Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md). |
| `was found without a corresponding <name>_tool_result block`           | The previous assistant turn has a `server_tool_use` block with no result block (most often, Claude called it alongside a client tool), and either your next user message ended that turn (for example, with text after the `tool_result` blocks) or the resume request no longer defines that server tool (the message then ends with `but no <name> tool was provided`) | Send a user message containing only the `tool_result` blocks for the client `tool_use` ids and keep the same `tools` array. See [Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md#tool-use).                                                               |
| `Unsupported regex feature in pattern field: ...`                      | A `pattern` in a strict tool's `input_schema` uses a regex feature that strict mode can't compile, such as a backreference, a lookaround, a word boundary, or a large `{n,m}` range                                                                                                                                                                                      | Simplify the pattern. Anchored patterns with basic quantifiers, character classes, and groups are supported; see [JSON Schema limitations](../Guides/build-with-claude-structured-outputs.md#json-schema-limitations).                                                                    |
| `All tools have defer_loading: true`                                   | No tools visible to the model                                                                                                                                                                                                                                                                                                                                            | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`.                                                                                                                                                                      |

## Error: thinking blocks cannot be modified

If a request fails with a 400 `invalid_request_error` whose message contains `` `thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified `` when continuing a conversation after a tool call, your application is altering the assistant's thinking blocks before sending them back. Send the entire assistant message back unchanged, then append your `tool_result`.

See [Thinking blocks cannot be modified](../Endpoints/errors.md#thinking-blocks-cannot-be-modified) for the full error and fix steps.

## Claude flags tool results as prompt injection

| Symptom                                                                                            | Likely cause                                                               | Fix                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude refuses to act on a tool result, or asks the user to confirm instructions that came from it | Your own instructions are being delivered inside the `tool_result` content | Claude is trained to treat instructions inside tool results as potentially untrusted third-party content. Move your instructions out of the tool result: send them in a `user` turn after the `tool_result` block, or, on supported models, in a [mid-conversation system message](../Guides/build-with-claude-mid-conversation-system-messages.md). Keep the tool result to just the data. See [Mitigate jailbreaks and prompt injections](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md#indirect-prompt-injection). |

## JSON escaping differences (Opus 4.6+)

| Symptom                                                  | Cause                                                             | Fix                                                                                            |
|----------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| String comparison on tool inputs fails with newer models | Unicode and forward-slash escaping differs between model versions | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input. |

## Next steps

[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Write schemas and descriptions that steer Claude toward the right tool.

[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)

Execute tools and return results in the required message format.

[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Full directory of Anthropic-provided tools and their version strings.
