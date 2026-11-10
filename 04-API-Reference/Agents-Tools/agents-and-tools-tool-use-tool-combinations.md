---
title: "Tool combinations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-05T06:35:14Z"
tags: ["agents", "api", "search"]
---

# Tool combinations

Copy page



Common Anthropic tool pairings for research agents, coding agents, and long-running agents.

Copy page



Anthropic-provided tools are designed to work together. Common agent patterns pair tools that cover complementary stages of a workflow: one tool gathers or discovers, another processes or acts. The following combinations are starting points, not prescriptions. Mix them to fit your task.

Each snippet shows only the `tools` array. See [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md) for the full request shape.

## Research agent: web_search + code_execution

Search finds sources; code execution analyzes and synthesizes. Claude searches for data, then writes Python to process, tabulate, or visualize it. This pairing is a good fit for questions that require both up-to-date information and nontrivial computation over that information, such as “compare this quarter’s earnings across the top five cloud providers.”

```python
{
  "tools": [
    { "type": "web_search_20260209", "name": "web_search" },
    { "type": "code_execution_20260521", "name": "code_execution" }
  ]
}
```



The flow is typically search, then run code, then optionally search again if the first pass surfaced a gap. Code execution runs server-side, so there’s no client-side sandbox to manage.

## Coding agent: text_editor + bash

The text editor reads and modifies files; bash runs tests and build commands. This is the canonical software-development loop: inspect the code, make an edit, run the tests, repeat. Both tools are client-executed, so your application controls which files and commands are accessible.

```python
{
  "tools": [
    { "type": "text_editor_20250728", "name": "str_replace_based_edit_tool" },
    { "type": "bash_20250124", "name": "bash" }
  ]
}
```



Pair this with a constrained working directory and a command allowlist if the agent operates on untrusted code. See [Text editor tool](agents-and-tools-tool-use-text-editor-tool.md) and [Bash tool](agents-and-tools-tool-use-bash-tool.md) for the execution contracts.

## Cite-then-fetch: web_search + web_fetch

Search surfaces candidate URLs; fetch retrieves full page content for the relevant ones. This avoids fetching everything upfront. Claude runs a search, inspects the snippets, picks the two or three results that actually look relevant, and fetches only those.

```python
{
  "tools": [
    { "type": "web_search_20260209", "name": "web_search" },
    { "type": "web_fetch_20260209", "name": "web_fetch" }
  ]
}
```



This pairing is useful when the answer lives in long-form content (documentation pages, articles, specifications) that a search snippet can’t fully capture. Fetch pulls the complete page so Claude can cite specific passages.

## Long-running agent: memory + any other tools

Memory persists state across conversations; the other tools do the work. Add memory to any agent that needs to remember prior sessions, such as a support agent that recalls a customer’s earlier issues or a project assistant that tracks decisions made last week.

```python
{
  "tools": [{ "type": "memory_20250818", "name": "memory" }]
}
```



Add your other tools alongside `memory` in the same array.

Memory is orthogonal to your other tools. It doesn’t change how they behave; it gives Claude a place to write down and later retrieve facts that would otherwise be lost when the context window resets. See [Memory tool](agents-and-tools-tool-use-memory-tool.md) for the storage model.

## All-in-one: computer_use

The computer use tool subsumes most others by operating a full desktop. Claude receives screenshots and issues mouse and keyboard actions, which means it can drive any application a human can. Use this when the task requires arbitrary GUI interaction that more specific tools can’t reach: legacy software without an API, visual verification steps, or workflows that span multiple desktop apps.

```python
{
  "tools": [{ "type": "computer_toolset_20260801" }]
}
```



The toolset entry takes no `name` or display dimensions: coordinates are expressed in the pixel space of the screenshots you return, and you can turn individual actions off through the entry’s `configs` field.

Computer use is the most general option and also the slowest, because Claude typically needs a fresh screenshot after each batch of actions. Prefer narrower tools when they cover your use case, and reach for computer use when nothing else fits. If the task stays inside a web browser, use the browser agent pattern in the next section. See [Computer use tool](agents-and-tools-tool-use-computer-use-tool.md) for the sandbox setup.

## Browser agent: browser_use

When the whole task occurs inside webpages (filling forms, reading page content, working across tabs), the browser use tool is a closer fit than computer use. Your application drives a browser it controls and returns screenshots or page state; Claude calls page-aware member tools such as `read_page`, `find`, `form_input`, and `get_page_text` alongside clicks and typing, so it can act on element references in addition to pixel coordinates.

```python
{
  "tools": [{ "type": "browser_toolset_20260801" }]
}
```



Like the computer use toolset, the entry takes no `name`, and you turn individual member tools off through its `configs` field. See [Browser use tool](agents-and-tools-tool-use-browser-use-tool.md) for the execution contract.

## Next steps



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Full catalog of Anthropic-provided tools with type strings and parameters.

[Tool use overview](agents-and-tools-tool-use-overview.md)

How tool use works and when to use Anthropic tools versus defining your own.
