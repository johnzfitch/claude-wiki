---
title: "Tool reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:17Z"
tags: ["api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftool-reference)

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

[Messages](../../01-Getting-Started/intro.md)Tool infrastructure

# Tool reference

Copy page



Directory of Anthropic-provided server tools, client tools, and client toolsets, plus reference for optional tool definition properties.

Copy page



This page is a reference for the tools Anthropic provides and the optional properties you can set on any tool definition. For a conceptual introduction to tool use, see [Tool use with Claude](agents-and-tools-tool-use-overview.md). For guidance on implementing tool use in your application, see [Define tools](agents-and-tools-tool-use-implement-tool-use.md).

## Anthropic-provided tools

Anthropic provides two kinds of tools: **server tools** that execute on Anthropic's infrastructure, and **client tools** where Anthropic defines the schema but your application handles execution. Both kinds appear in your request's `tools` array alongside any user-defined tools.

[TABLE]

For model compatibility, see each tool's page. Supported models vary by tool and by tool version.



The tool search `type` values also accept undated aliases: `tool_search_tool_regex` and `tool_search_tool_bm25`. These resolve to the latest dated version.

### Tool versioning

Most Anthropic-provided tools carry a `_YYYYMMDD` suffix in the `type` string. A new version is released when the tool's behavior, schema, or model support changes. Older versions remain available so that existing integrations continue to work.

When a tool has multiple active versions, the relationship between them varies:

- **Capability-keyed:** `web_search_20260209` and `web_fetch_20260209` add dynamic content filtering over their predecessors; `web_fetch_20260309` adds a cache-bypass option; `web_search_20260318` and `web_fetch_20260318` add response-inclusion control. `code_execution_20260120` adds [programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md) from within the sandbox; `code_execution_20260521` discloses the per-cell time limit in the tool description. In each case, both the new and old versions are current; which one you use depends on whether you need the new capability.
- **Model-keyed:** `text_editor_20250728` is for Claude 4 and later models and `text_editor_20250124` is for earlier models. The version you use depends on the model you target.
- **Variant, not version:** `tool_search_tool_regex_20251119` and `tool_search_tool_bm25_20251119` are two search algorithms released together. Neither supersedes the other.
- **Legacy:** `code_execution_20250522` supports only Python. `code_execution_20250825` adds Bash and file operations.
- **Successor:** `computer_toolset_20260801` is the stable successor to the beta `computer_20251124` and `computer_20250124` versions, which remain available on the models listed for them under [Earlier tool versions](agents-and-tools-tool-use-computer-use-tool.md#earlier-tool-versions). `browser_toolset_20260801` is the first version of the browser use tool. Both are [client toolsets](#client-toolsets).

The `mcp_toolset` type is not date-versioned; versioning is carried in the `anthropic-beta` header instead.

### Client toolsets

The [computer use tool](agents-and-tools-tool-use-computer-use-tool.md) and [browser use tool](agents-and-tools-tool-use-browser-use-tool.md) are Anthropic-defined client toolsets: one entry in `tools` declares a fixed set of member tools whose names, descriptions, and input schemas Anthropic defines, and your application executes every call. The entry takes no `name`, because the dated `type` fixes the member names. `configs`, `cache_control`, and `allowed_callers` (which accepts only `["direct"]`) are optional.

Client toolsets are Messages API tools. They aren't currently available as agent tools in [Claude Managed Agents](../Other/managed-agents-tools.md), which provides its own built-in agent toolset, MCP toolsets, and custom tools.

```python
{
  "type": "browser_toolset_20260801",
  "configs": {
    "javascript_exec": { "enabled": true }
  },
  "cache_control": { "type": "ephemeral" }
}
```



`configs` adjusts individual members:

- Keys are member names, and each value accepts only `enabled` and `defer_loading`.
- A member you omit keeps its defaults. An absent value, `{}`, and a restated default are equivalent.
- An unknown member name or any other field in a member's value is rejected, as is a `configs` that disables every member (omit the entry instead).
- A disabled member is removed from the tools Claude sees. If Claude still names it, return an error `tool_result`.

Set `defer_loading` per member, never on the entry, and give every enabled member the same value: under [tool search](agents-and-tools-tool-use-tool-search-tool.md#deferred-tool-loading) the toolset loads and expands as one definition. When every enabled member defers, only a [tool search tool](agents-and-tools-tool-use-tool-search-tool.md) that isn't itself deferred can surface the toolset, so declare one in the same request. Don't put `cache_control` on a toolset entry whose members defer; set the breakpoint on a non-deferred tool instead, because deferred definitions are not part of the cached prefix.

`cache_control` goes on the entry only; to learn where the breakpoint lands, including markers inside a batch action, see [Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md#cache-control-on-tool-definitions).

**Handle member tool calls.** Claude calls a member with a `tool_use` block whose `name` is the member name and whose `toolset_name` is `computer` or `browser`; `input` holds that member's parameters and no `action` field. Dispatch on the `toolset_name` and `name` pair, because a custom tool may share a member's name and the two toolsets share names such as `screenshot`. Only member results echo `toolset_name`. Several member calls in one turn form a batch action that you run in order ([computer use](agents-and-tools-tool-use-computer-use-tool.md#batch-actions), [browser use](agents-and-tools-tool-use-browser-use-tool.md#batch-actions)). New members arrive only with a new dated `type`.

**Not supported on toolset entries.** The API rejects each of these with an `invalid_request_error`:

- `strict: true` or `input_examples`.
- `defer_loading` on the entry, or enabled members whose `defer_loading` values differ (set it per member in `configs`, all to the same value).
- A code execution caller in `allowed_callers` (no [programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)).
- The legacy `fine-grained-tool-streaming-2025-05-14` beta header. When you stream, each member's `input` arrives as one complete `input_json_delta`.
- A `tool_choice` of type `tool` that names the toolset or a member (use `auto`, `any`, or `none`).
- Two entries of the same toolset, or another tool that carries that toolset's name: a tool named `computer` alongside `computer_toolset_20260801`, or a tool named `browser` alongside `browser_toolset_20260801`. The two toolsets can be declared together.

## Tool definition properties

Every tool in the `tools` array, including user-defined tools, accepts optional properties that control how the tool is loaded, who can call it, and how its inputs are validated. These properties compose: you can set `defer_loading` and `cache_control` and `strict` on the same tool.

| Property                | Purpose                                                                                                               | Available on                                                                                                                                                                                                                                           | Detailed guide                                                                                                      |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `cache_control`         | Set a prompt-cache breakpoint at this tool definition                                                                 | All tools (on `computer_toolset_20260801` and `browser_toolset_20260801`, set it on the toolset entry itself, not inside member `configs`)                                                                                                             | [Prompt caching](../Guides/build-with-claude-prompt-caching.md)                                                         |
| `strict`                | Guarantee schema validation on tool names and inputs                                                                  | All tools except `mcp_toolset`, `computer_toolset_20260801`, and `browser_toolset_20260801`                                                                                                                                                            | [Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)                                               |
| `defer_loading`         | Exclude the tool from the initial system prompt; load it on demand when tool search returns a `tool_reference` for it | All tools (for `mcp_toolset`, see [tool configuration](agents-and-tools-mcp-connector.md#mcp-toolset-configuration)). On the computer use and browser use toolsets, set it per member inside `configs`; see [Client toolsets](#client-toolsets). | [Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)                                             |
| `allowed_callers`       | Restrict which callers can call the tool                                                                              | All tools except `mcp_toolset` (on `computer_toolset_20260801` and `browser_toolset_20260801`, only `["direct"]` is accepted; see [Client toolsets](#client-toolsets))                                                                                 | [Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md#the-allowed-callers-field) |
| `input_examples`        | Provide example input objects to help Claude understand how to call the tool                                          | User-defined and Anthropic-schema client tools, except `computer_toolset_20260801` and `browser_toolset_20260801`. Not available on server tools.                                                                                                      | [Define tools](agents-and-tools-tool-use-implement-tool-use.md#providing-tool-use-examples)                         |
| `eager_input_streaming` | Enable fine-grained input streaming (`true`) or keep standard buffered streaming (`false`) for this tool              | User-defined tools only                                                                                                                                                                                                                                | [Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)                       |

### `allowed_callers` values

`allowed_callers` is an array that accepts any combination of:

| Value                       | Meaning                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------|
| `"direct"`                  | The model can call this tool directly in a `tool_use` block. This is the default if `allowed_callers` is omitted. |
| `"code_execution_20260120"` | Code running inside a `code_execution_20260120` or later sandbox can call this tool.                              |

Both `"code_execution_20260120"` and `"code_execution_20260521"` are accepted in `allowed_callers` and are interchangeable: a request using either code-execution tool version satisfies tools that list either caller. Response blocks always tag the caller as `code_execution_20260120` regardless of which version the request declared.

Omitting `"direct"` from the array (for example, `"allowed_callers": ["code_execution_20260120"]`) guides Claude to call the tool only from within code execution. The response's `tool_use` block includes a `caller` field that identifies which caller called the tool. See [Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md#the-allowed-callers-field) for the full treatment, including the `caller` response shape and error behavior.

### `defer_loading` and prompt caching

Tools with `defer_loading: true` are stripped from the rendered tools section before the cache key is computed. They don't appear in the system-prompt prefix at all. When tool search discovers a deferred tool and returns a `tool_reference` for it, the tool's full definition is expanded inline at that point in the conversation body, not in the prefix.

This means `defer_loading: true` preserves your prompt cache. You can add deferred tools to a request without invalidating an existing cache entry, and the cache remains valid across the turn where the tool is discovered and the turn where it's called.

To learn how to combine `defer_loading` with `cache_control` breakpoints, see the [Tool search tool prompt caching guidance](agents-and-tools-tool-use-tool-search-tool.md#prompt-caching).
