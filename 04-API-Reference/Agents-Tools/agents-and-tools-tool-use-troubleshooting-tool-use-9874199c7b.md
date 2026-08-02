---
title: "Troubleshooting tool use - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-08-02T05:38:50Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Troubleshooting

Messages/Tools

# Troubleshooting tool use




Fix the most common tool-use errors with symptom-to-fix diagnostic tables.




Symptom-to-fix tables for the most common tool-use errors. Each fix cross-references the page that owns the feature.




Claude calls the wrong tool

| Symptom                                    | Likely cause                                 | Fix                                                                                                                                                        |
|--------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude calls tool A when you wanted tool B | Description ambiguity                        | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](/docs/en/agents-and-tools/tool-use/define-tools). |
| Claude never calls your tool               | Tool name collision or overly-generic schema | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete.                                                   |
| Claude calls with wrong parameter types    | Model guessing at ambiguous schema           | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`.                                                                    |




Claude invents tool parameters

| Symptom                                     | Likely cause                              | Fix                                                                                                                 |
|---------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Parameter that doesn't exist in your schema | Model over-generation without strict mode | Add `strict: true` if your schema is in the [supported subset](/docs/en/agents-and-tools/tool-use/strict-tool-use). |
| Parameter values outside your enum          | Missing strict mode or too-large enum     | Shrink the enum or add `input_examples` showing valid choices.                                                      |




Parallel tool calls don't work

| Symptom                                                       | Likely cause                     | Fix                                                                                                                                                      |
|---------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude calls tools sequentially when parallel would be better | Message history formatting       | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `disable_parallel_tool_use` seems ignored                     | Set too late in the conversation | Must be set on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls.                                   |




Cache keeps invalidating

| Symptom                                     | Likely cause                                                                                  | Fix                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Every request is a cache miss               | `tool_choice`, the thinking configuration, or `output_config.effort` varying between requests | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point; hold the thinking configuration and effort level constant for the life of a cached conversation. See [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) and [Thinking and prompt caching](/docs/en/build-with-claude/thinking#thinking-and-prompt-caching). |
| Adding a tool mid-conversation breaks cache | Tool prepended to the tools array                                                             | Use `defer_loading: true` with tool search to append the tool inline instead of modifying the array head.                                                                                                                                                                                                                                                                                              |




Errors at request time

| Error                                                                                | Cause                                                                                                                                                                                                                                                                                                                                                                    | Fix                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tool_use ids were found without tool_result blocks immediately after`               | Missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message                                                                                                                                                                                                                                                       | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls) and [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `was found without a corresponding <name>_tool_result block`                         | The previous assistant turn has a `server_tool_use` block with no result block (most often, Claude called it alongside a client tool), and either your next user message ended that turn (for example, with text after the `tool_result` blocks) or the resume request no longer defines that server tool (the message then ends with `but no <name> tool was provided`) | Send a user message containing only the `tool_result` blocks for the client `tool_use` ids and keep the same `tools` array. See [Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons#tool-use).                                                               |
| `Input schema is not compatible with strict mode: string patterns are not supported` | Using `pattern` with `strict: true`                                                                                                                                                                                                                                                                                                                                      | Remove the pattern or drop `strict: true`. The `pattern` keyword is not in the supported JSON Schema subset yet.                                                                                                                                                                      |
| `All tools have defer_loading: true`                                                 | No tools visible to the model                                                                                                                                                                                                                                                                                                                                            | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`.                                                                                                                                                                      |




Error: thinking blocks cannot be modified

If a request fails with a 400 `invalid_request_error` whose message contains `` `thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified `` when continuing a conversation after a tool call, your application is altering the assistant's thinking blocks before sending them back. Send the entire assistant message back unchanged, then append your `tool_result`.

See [Thinking blocks cannot be modified](/docs/en/api/errors#thinking-blocks-cannot-be-modified) for the full error and fix steps.




Claude flags tool results as prompt injection

| Symptom                                                                                            | Likely cause                                                               | Fix                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Claude refuses to act on a tool result, or asks the user to confirm instructions that came from it | Your own instructions are being delivered inside the `tool_result` content | Claude is trained to treat instructions inside tool results as potentially untrusted third-party content. Move your instructions out of the tool result: send them in a `user` turn after the `tool_result` block, or, on supported models, in a [mid-conversation system message](/docs/en/build-with-claude/mid-conversation-system-messages). Keep the tool result to just the data. See [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection). |




JSON escaping differences (Opus 4.6+)

| Symptom                                                  | Cause                                                             | Fix                                                                                            |
|----------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| String comparison on tool inputs fails with newer models | Unicode and forward-slash escaping differs between model versions | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input. |




Next steps


Define tools

Write schemas and descriptions that steer Claude toward the right tool.


Handle tool calls

Execute tools and return results in the required message format.


Tool reference

Full directory of Anthropic-schema tools and their version strings.
