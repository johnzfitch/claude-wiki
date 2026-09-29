---
title: "Memory tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:16Z"
tags: ["api", "prompting", "security"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fmemory-tool)

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

# Memory tool

Copy page



Let Claude store and retrieve information across conversations by implementing the memory tool's file operations in your application.

Copy page



The memory tool lets Claude store and retrieve information across conversations in a directory of memory files. Claude can create, read, update, and delete files that persist between sessions, building up knowledge over time without keeping everything in the context window.

Memory supports just-in-time context retrieval. Rather than loading all relevant information up front, an agent records what it learns in memory files and reads them back on demand. This keeps the active context focused on the current task, which matters for long-running sessions that would otherwise overwhelm the context window. See [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) for the broader pattern.

The memory tool operates client-side: Claude requests file operations, and your application executes them. You control where and how the data is stored through your own infrastructure.



Reach out through the [feedback form](https://forms.gle/YXC2EKGMhjN1c4L88) to share your feedback on this feature.



To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

## Use cases

- Maintain project context across multiple agent sessions
- Apply lessons from past interactions, decisions, and feedback to new tasks
- Build up a knowledge base over time

## How it works

When the memory tool is enabled, Claude automatically checks its memory directory before starting a task. As it works, Claude stores what it learns in files under `/memories` and reads them back in later conversations to continue earlier work.

Because the memory tool is client-side, Claude only requests memory operations. Your application executes each request against storage you control and returns the result in a `tool_result` block (see [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)). The `/memories` path is a prefix that your handler maps onto real storage, such as a per-user directory or keys in a database. Memory lives entirely in your application. A later conversation continues from the same memory when it sends the same `tools` entry and your handler serves the same store. For security, restrict all memory operations to the `/memories` directory (see [Path traversal protection](#path-traversal-protection)).

### Example: How memory tool calls work

A typical interaction looks like this:

**1. User request:**

``` block
"Help me respond to this customer service ticket."
```



**2. Claude checks the memory directory:**

``` block
"I'll help you respond to the customer service ticket. Let me check my memory for any previous context."
```



Claude calls the memory tool:

```python
{
  "type": "tool_use",
  "id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories"
  }
}
```



**3. Your application returns the directory contents:**

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Here're the files and directories up to 2 levels deep in /memories, excluding hidden items and node_modules:\n4.0K\t/memories\n1.5K\t/memories/customer_service_guidelines.xml\n2.0K\t/memories/refund_policies.xml"
}
```



**4. Claude reads relevant files:**

```python
{
  "type": "tool_use",
  "id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories/customer_service_guidelines.xml"
  }
}
```



**5. Your application returns the file contents:**

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": "Here's the content of /memories/customer_service_guidelines.xml with line numbers:\n     1\t<guidelines>\n     2\t<addressing_customers>\n     3\t- Always address customers by their first name\n     4\t- Use empathetic language\n..."
}
```



**6. Claude uses the memory to help:**

``` block
"Based on your customer service guidelines, I can help you craft a response. Please share the ticket details..."
```



The memory tool is available on all Claude 4 and later models. For the full list of Anthropic-provided tools, see the [Tool reference](agents-and-tools-tool-use-tool-reference.md).

## Getting started

Using the memory tool takes two steps:

1.  Add the memory tool to your request. The `tools` entry `{"type": "memory_20250818", "name": "memory"}` is the entire configuration: the `name` must be `memory`, and you don't define an input schema for an Anthropic-provided tool.
2.  Implement a client-side handler for each memory command. Your handler must reject paths outside `/memories`, so read [Path traversal protection](#path-traversal-protection) before you write it.

## Basic usage

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

```python
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": "Help me respond to this customer service ticket.",
        }
    ],
    tools=[{"type": "memory_20250818", "name": "memory"}],
)

print(message)
```

## Implement the memory handler

Claude's reply to a request like the previous one ends with a `tool_use` block that requests a memory operation, such as `view /memories`. Your application executes the operation and returns the result in a `tool_result` block, then sends the conversation back so Claude can continue: the standard [tool-use loop](agents-and-tools-tool-use-handle-tool-calls.md).

Four SDKs provide memory tool helpers that handle the tool interface and the loop. Subclass `BetaAbstractMemoryTool` (Python and C#), use `betaMemoryTool` (TypeScript), or implement `BetaMemoryToolHandler` (Java) to back memory with your own storage, such as files on disk, a database, cloud storage, or encrypted files. Python and TypeScript also ship a ready-made local-filesystem implementation, `BetaLocalFilesystemMemoryTool`. The helper and tool-runner surfaces live in each SDK's beta namespace even though the memory tool itself doesn't require a beta header. The Go and Ruby SDKs have no memory helper, so those examples run the tool-use loop themselves, and PHP wraps your handler closure in its generic `BetaRunnableTool`. All three use an in-memory store that you replace with your own storage.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import anthropic
from anthropic.tools import BetaLocalFilesystemMemoryTool

client = anthropic.Anthropic()
memory = BetaLocalFilesystemMemoryTool(base_path="./memory")

runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Remember that customer Acme Corp prefers email follow-ups.",
        }
    ],
    tools=[memory],
)

final_message = runner.until_done()
print(final_message.content)
```

The in-memory stores in the Go, PHP, and Ruby examples keep them self-contained: each one dispatches on the `command` field in the `tool_use` block's `input` and returns the strings described under [Tool commands](#tool-commands). A production handler also needs the [path validation](#path-traversal-protection) these demonstration stores skip. For the SDKs' own complete examples, see:

- Python: [examples/memory/basic.py](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py)
- TypeScript: [examples/tools-helpers-memory.ts](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts)
- C#: [MemoryToolExample](https://github.com/anthropics/anthropic-sdk-csharp/tree/main/examples/MemoryToolExample)
- Java: [BetaMemoryToolExample.java](https://github.com/anthropics/anthropic-sdk-java/blob/main/anthropic-java-example/src/main/java/com/anthropic/example/BetaMemoryToolExample.java)

## Tool commands

Your client-side implementation must handle the following commands. These specifications describe the recommended behaviors and return strings: Claude reads whatever text your tool result contains, so you can return different strings if your application needs to.

### view

Shows directory contents or file contents with optional line ranges:

```python
{
  "command": "view",
  "path": "/memories/notes.txt",
  "view_range": [1, 10]
}
```



`view_range` is optional and applies to text-file views: `[start_line, end_line]` returns those lines, and `[start_line, -1]` returns everything from `start_line` to the end of the file.

#### Return values

**For directories:** Return a listing that shows files and directories with their sizes:

``` inline-block
Here're the files and directories up to 2 levels deep in {path}, excluding hidden items and node_modules:
{size}\t{path}
{size}\t{path}/{filename1}
{size}\t{path}/{filename2}
```



- Lists files up to 2 levels deep
- Shows human-readable sizes (for example, `5.5K`, `1.2M`)
- Excludes hidden items (files starting with `.`) and `node_modules`
- Uses a tab character between the size and the path

The first `view` of `/memories` on an empty store is not an error. The SDKs' local-filesystem memory tools (`BetaLocalFilesystemMemoryTool`) create the memory root before Claude's first call and return the listing header followed by a single size-and-path line for the empty directory itself.

**For files:** Return file contents with a header and line numbers:

``` block
Here's the content of {path} with line numbers:
{line_numbers}{tab}{content}
```



Line number formatting:

- **Width:** 6 characters, right-aligned with space padding
- **Separator:** Tab character between line number and content
- **Indexing:** 1-indexed (first line is line 1)
- **Line limit:** Files with more than 999,999 lines should return an error: `"File {path} exceeds maximum line limit of 999,999 lines."`

**Example output:**

``` inline-block
Here's the content of /memories/notes.txt with line numbers:
     1  Hello World
     2  This is line two
    10  Line ten
   100  Line one hundred
```



Claude's tool description also says that `view` displays image files (`.jpg`, `.jpeg`, and `.png`) and truncates the text view of files longer than 16,000 characters. Expect `view` calls on image paths and follow-up ranged views of long files.

#### Error handling

- **File or directory does not exist:** `"The path {path} does not exist. Please provide a valid path."`

### create

Creates a new file:

```python
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Meeting notes:\n- Discussed project timeline\n- Next steps defined\n"
}
```



#### Return values

- **Success:** `"File created successfully at: {path}"`

#### Error handling

- **File already exists:** `"Error: File {path} already exists"`

Claude's tool description says `create` "creates or overwrites" a file, so expect `create` calls on paths that already exist. Returning the error is the reference behavior, and overwriting instead is a valid implementation choice.

### str_replace

Replaces text in a file:

```python
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Favorite color: blue",
  "new_str": "Favorite color: green"
}
```



`new_str` is optional for `str_replace`: when it's omitted, `old_str` is deleted without a replacement.

#### Return values

- **Success:** `"The memory file has been edited."` followed by a snippet of the edited file with line numbers

#### Error handling

- **File does not exist:** `"Error: The path {path} does not exist. Please provide a valid path."`
- **Text not found:** `` "No replacement was performed, old_str `\{old_str}` did not appear verbatim in {path}." ``
- **Duplicate text:** When `old_str` appears multiple times, return: `` "No replacement was performed. Multiple occurrences of old_str `\{old_str}` in lines: {line_numbers}. Please ensure it is unique" ``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### insert

Inserts text at a specific line:

```python
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Review memory tool documentation\n"
}
```



`insert_text` is inserted after line `insert_line`, and `0` inserts at the beginning of the file.

#### Return values

- **Success:** `"The file {path} has been edited."`

#### Error handling

- **File does not exist:** `"Error: The path {path} does not exist"`
- **Invalid line number:** `` "Error: Invalid `insert_line` parameter: {insert_line}. It should be within the range of lines of the file: [0, {n_lines}]" ``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### delete

Deletes a file or directory:

```python
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```



#### Return values

- **Success:** `"Successfully deleted {path}"`

#### Error handling

- **File or directory does not exist:** `"Error: The path {path} does not exist"`

#### Directory handling

Deletes the directory and all its contents recursively. The tool description tells Claude it cannot delete the `/memories` directory itself, so reject a `delete` whose path is the memory root.

### rename

Renames or moves a file or directory:

```python
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```



#### Return values

- **Success:** `"Successfully renamed {old_path} to {new_path}"`

#### Error handling

- **Source does not exist:** `"Error: The path {old_path} does not exist"`
- **Destination already exists:** Return an error (do not overwrite): `"Error: The destination {new_path} already exists"`

#### Directory handling

Renames the directory. The tool description tells Claude it cannot rename the `/memories` directory itself, so reject a `rename` whose `old_path` is the memory root.

## Prompting guidance

When the memory tool is present in your request's `tools`, the API automatically adds this instruction to the system prompt. You don't need to send it yourself:

``` block
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
   - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.
```



Claude's tool description already tells it to keep the memory directory organized, so you don't need to repeat that instruction. If Claude still creates cluttered memory files, you can reinforce it in your prompt:

```python
Note: when editing your memory folder, always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary.
```



You can also guide what Claude writes to memory. For example: "Only write down information relevant to \<topic\> in your memory system."

## Security considerations

Your application executes every file operation Claude requests, so these safeguards are your responsibility:

### Sensitive information

Claude usually refuses to write sensitive information to memory files. For stronger guarantees, add validation that strips sensitive data before your handler writes the file.

### File storage size

Track memory file sizes and cap how large a file can grow. Consider capping how many characters the `view` command returns, and let Claude page through the rest with `view_range`.

### Memory expiration

Periodically delete memory files that haven't been accessed in a long time.

### Path traversal protection



A malicious path such as `/memories/../../secrets.env` can reach files outside the `/memories` directory. Your implementation must validate every path in every command to prevent directory traversal attacks.

Consider these safeguards:

- Validate that all paths start with `/memories`
- Resolve paths to their canonical form and verify they remain within the memory directory
- Reject paths containing sequences such as `../`, `..\\`, or other traversal patterns
- Watch for URL-encoded traversal sequences (`%2e%2e%2f`)
- Use your language's built-in path security utilities (for example, Python's `pathlib.Path.resolve()` and `relative_to()`)

## Error handling

The memory tool uses similar error-handling patterns to the [text editor tool](agents-and-tools-tool-use-text-editor-tool.md#handle-errors). Each command's error messages are listed under [Tool commands](#tool-commands). To return an error to Claude, set `is_error` to `true` on the tool result and put the message in `content`:

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Error: The path /memories/notes.txt does not exist",
  "is_error": true
}
```



## Context editing integration

The memory tool pairs with context editing to manage long-running conversations. For details, see [Context editing](../Guides/build-with-claude-context-editing.md).

## Using with compaction

The memory tool can also be paired with [compaction](../Guides/build-with-claude-compaction.md), which summarizes older conversation context server-side. Context editing clears specific tool results on the client. Compaction automatically summarizes the whole conversation on the server when the conversation approaches the context window limit.

For long-running agents, consider using both: compaction keeps the active context small without client-side bookkeeping, and memory preserves the information that must survive summarization.

## Multisession software development pattern

For software projects that span multiple agent sessions, set up memory files deliberately instead of writing them ad hoc as work progresses. The following pattern turns memory into a recovery mechanism: each new session resumes from the state the last one recorded.

### How the pattern works

1.  **Initializer session:** The first session sets up the memory files before any substantive work begins. This includes a progress log (tracking what has been done and what comes next), a feature checklist (defining the scope of work), and a reference to any startup or initialization script the project needs.

2.  **Subsequent sessions:** Each new session opens by reading those memory files. This restores the project state without re-exploring the code base or retracing earlier decisions.

3.  **End-of-session update:** Before a session ends, it updates the progress log with what was completed and what remains. This ensures the next session has an accurate starting point.

### Key principle

Work on one feature at a time. Mark a feature complete only after end-to-end verification confirms it works, not when the code is written. This keeps the progress log accurate from session to session.



For a detailed case study of this pattern in practice, including the initializer script, progress file structure, and git-based recovery, see [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).

## Next steps



[Bash tool](agents-and-tools-tool-use-bash-tool.md)

Execute shell commands in a persistent bash session.



[Context editing](../Guides/build-with-claude-context-editing.md)

Automatically manage conversation context as it grows with context editing.



[Compaction](../Guides/build-with-claude-compaction.md)

Server-side context compaction for managing long conversations that approach context window limits.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.
