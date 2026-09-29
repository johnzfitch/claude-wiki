---
title: "Computer use tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:25Z"
tags: ["api", "security"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fcomputer-use-tool)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Tools

# Computer use tool

Copy page



Give Claude screenshot, mouse, and keyboard control of a desktop environment with the computer use tool, the computer_toolset_20260801 client toolset.

Copy page



Computer use tool

[ZDR](/docs/en/manage-claude/api-and-data-retention)

Eligible

excludes [Covered Models](/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements)

Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction.

The computer use tool is an Anthropic-defined [client toolset](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets): one `{"type": "computer_toolset_20260801"}` entry in `tools` gives Claude 17 member tools such as `screenshot`, `left_click`, `type`, and `zoom`, and your application runs every call in an environment you control. It isn't currently available in [Claude Managed Agents](/docs/en/managed-agents/tools). Claude's calls are `tool_use` blocks whose `name` is the member and which carry `"toolset_name": "computer"`, often several per turn (a [batch action](#batch-actions)).

For tasks that stay inside webpages, the [browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool) is the closer fit: its member tools read and act on the page itself, and it doesn't need a full desktop environment.



Computer use is available on the Claude API and [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai) as the `computer_toolset_20260801` toolset; see [Compatibility](#compatibility) for the supported models.

Existing `computer_20251124` integrations keep working on the models listed for it under [Earlier tool versions](#earlier-tool-versions), and earlier tool versions remain available in beta for models and platforms that don't support the toolset. See [Migrate from `computer_20251124`](#migrate-from-computer-20251124) to upgrade, or [Earlier tool versions](#earlier-tool-versions) for the beta headers.

## Security considerations

Computer use has unique risks distinct from standard API features. These risks are heightened when interacting with the internet.



To minimize risks, consider taking precautions such as:

1.  Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
2.  Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft.
3.  Limiting internet access to an allowlist of domains to reduce exposure to malicious content.
4.  Asking a human to confirm decisions that might result in meaningful real-world consequences and any tasks requiring affirmative consent, such as accepting cookies, completing financial transactions, or agreeing to terms of service.

In some circumstances, Claude will follow commands found in content even when they conflict with your instructions. For example, instructions on webpages or contained in images might override your instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the computer use tools, classifiers will automatically scan what the tools return, such as screenshots, to flag potential prompt injections. When these classifiers identify a potential prompt injection, they will automatically steer the model to check whether the instruction really came from you before acting on it.

This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, [contact support](https://support.claude.com/en/). The precautions above remain important even with these classifiers in place.

Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.

## Quick start

Add the computer use toolset to the `tools` array of a [Messages API](/docs/en/api/messages/create) request as `{"type": "computer_toolset_20260801"}`. The request needs no beta header. This example also declares the [text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool) and [bash tool](/docs/en/agents-and-tools/tool-use/bash-tool), which Claude typically uses alongside computer use:

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

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[
        {"type": "computer_toolset_20260801"},
        {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
        {"type": "bash_20250124", "name": "bash"},
    ],
    messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
)
print(response)
```

When Claude acts on the desktop, the response has a `stop_reason` of `tool_use` and contains one or more member `tool_use` blocks, each naming a member tool and carrying `"toolset_name": "computer"`. Partway through this task, after Claude has seen a screenshot of the desktop, a response might look like this:

Output



```python
{
  "id": "msg_01UZ3bXcQH8mTqNhVfL9eK2p",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5-5",
  "content": [
    {
      "type": "text",
      "text": "I'll open the web browser to find a picture of a cat."
    },
    {
      "type": "tool_use",
      "id": "toolu_01WkoTUvSHDzTBu2xnGk8Ep8",
      "name": "left_click",
      "toolset_name": "computer",
      "input": { "coordinate": [512, 742] }
    },
    {
      "type": "tool_use",
      "id": "toolu_017nJn3RgSCkTMwuZDb4uUov",
      "name": "screenshot",
      "toolset_name": "computer",
      "input": {}
    }
  ],
  "stop_reason": "tool_use",
  "stop_sequence": null
}
```

Your application runs each call in order in your own environment, returns one `tool_result` block per `tool_use` block, and calls the API again; [How computer use works](#how-computer-use-works) describes that loop, and the rest of this page shows how to implement it.

------------------------------------------------------------------------

## How computer use works

1.  1

    ### Provide Claude with the computer use tool and a user prompt

    - Add the computer use toolset (and optionally other tools) to the `tools` array of your API request.
    - Include a user prompt that requires desktop interaction, for example, "Save a picture of a cat to my desktop."

2.  2

    ### Claude responds with member tool calls

    - Claude assesses whether acting on the desktop can help with the user's query.
    - If so, Claude responds with one or more member `tool_use` blocks, such as `screenshot`, `left_click`, or `type`, each carrying `"toolset_name": "computer"`. A response with several of these blocks is a [batch action](#batch-actions).
    - The API response has a `stop_reason` of `tool_use`, signaling a tool use request.

3.  3

    ### Run the calls in order and return results

    - Iterate over every `tool_use` block in the response, in order. For each one, dispatch on the member `name` together with `toolset_name`, and perform that action with the block's `input` on your container or virtual machine.
    - Continue the conversation with a new `user` message that contains one `tool_result` block per `tool_use` block, matched by `tool_use_id` and each echoing `"toolset_name": "computer"`. Return an image for `screenshot` and `zoom`; a short text such as `OK` is enough for the other actions.
    - If an action fails, return `is_error: true` for that block and answer the rest of the batch as described in [Batch actions](#batch-actions).

4.  4

    ### Claude continues until the task is complete

    - Claude analyzes the tool results to determine if more actions are needed or the task has been completed.
    - If Claude determines more actions are needed, it responds with another `tool_use` `stop_reason` and you should return to step 3.
    - Otherwise, it returns a text response to the user.

The repetition of steps 3 and 4 without user input is referred to as the "agent loop" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request).

### Batch actions

Claude can plan a short sequence of actions, such as click, type, and then take a screenshot, and return them together in one response. This is called a batch action; it uses the same response shape as [parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use) with one difference: you run the blocks in order rather than concurrently.

A response with a three-action batch looks like this:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_01HqCF3nJ4Vzr8sTkPZ2wxYA",
      "name": "left_click",
      "toolset_name": "computer",
      "input": { "coordinate": [640, 60] }
    },
    {
      "type": "tool_use",
      "id": "toolu_01Ppr3sZ3TnE9m6VUu4RyH2K",
      "name": "type",
      "toolset_name": "computer",
      "input": { "text": "pictures of cats" }
    },
    {
      "type": "tool_use",
      "id": "toolu_01Xf5W1sD8Q9aBcJ7kLmN2pQ",
      "name": "screenshot",
      "toolset_name": "computer",
      "input": {}
    }
  ]
}
```



Return one `tool_result` block for each `tool_use` block, matched by `tool_use_id`, all in the next `user` message. Every result for a member tool must carry `"toolset_name": "computer"`; a result that omits it, or that names a different toolset than its `tool_use` block, is rejected. Only `screenshot` and `zoom` results need an image; for the other members, a short text acknowledgment such as `OK` is enough (`cursor_position` returns the coordinates as text):

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01HqCF3nJ4Vzr8sTkPZ2wxYA",
      "toolset_name": "computer",
      "content": [{ "type": "text", "text": "OK" }]
    },
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01Ppr3sZ3TnE9m6VUu4RyH2K",
      "toolset_name": "computer",
      "content": [{ "type": "text", "text": "OK" }]
    },
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01Xf5W1sD8Q9aBcJ7kLmN2pQ",
      "toolset_name": "computer",
      "content": [
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": "iVBORw0KGgo..."
          }
        }
      ]
    }
  ]
}
```



**Run blocks in order and stop at the first failure.** Later actions in a batch usually depend on earlier ones: the `type` in this example enters text into whatever the preceding click focused. Run the blocks sequentially in the order they appear in `content`, and if one fails, don't run the rest. Every `tool_use` block still needs a `tool_result`, so answer the batch as follows:

- For each action that succeeded, return its normal result.
- For the action that failed, return `is_error: true` with a text description of what went wrong.
- For every later action in the batch, return `is_error: true` with exactly this text (the browser use tool uses its own [halt text](/docs/en/agents-and-tools/tool-use/browser-use-tool#batch-actions)):

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01Xf5W1sD8Q9aBcJ7kLmN2pQ",
  "toolset_name": "computer",
  "is_error": true,
  "content": "Not executed: an earlier computer action in this turn failed."
}
```



Claude then sees which actions succeeded, which one failed, and which were skipped, and replans on its next turn. A request that leaves any `tool_use` block in the batch unanswered is rejected with an `invalid_request_error`, so an agent loop that reads only the first block fails on its next call. If your application asks a human to confirm consequential actions, make that check before each block runs, because a batch can complete a multistep action within one turn.

Claude typically finishes a batch with `screenshot` so it can observe the outcome before deciding what to do next. When a batch doesn't end with one, your application can attach a screenshot as an extra `image` block on the last result in the batch so that Claude always sees the current state of the screen, which saves a round trip compared with waiting for Claude to ask. You can also prompt Claude to end every batch with a screenshot (see [Optimize model performance with prompting](#optimize-model-performance-with-prompting)).

### The computing environment

Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:

1.  **Virtual display:** A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.

2.  **Desktop environment:** A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.

3.  **Applications:** Pre-installed Linux applications such as Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.

4.  **Tool implementations:** Integration code that translates Claude's abstract tool requests (such as "move mouse" or "take screenshot") into actual operations in the virtual environment.

5.  **Agent loop:** A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:

1.  Receives Claude's tool use requests
2.  Translates them into actions in your computing environment
3.  Captures the results (such as screenshots and command outputs)
4.  Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.

------------------------------------------------------------------------

## How to implement computer use

Upgrading an existing `computer_20251124` integration? Start with [Migrate from `computer_20251124`](#migrate-from-computer-20251124); the rest of this section applies to both new and migrated integrations.



The [computer use reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is a complete working example: a [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use, implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools), an [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that calls the Claude API and runs the tools, and a web interface for the container, loop, and tools.

### Understand the agent loop

The core of computer use is the "agent loop": a cycle where Claude requests tool actions, your application runs them, and returns results to Claude. The loop uses the client you created in the [Quick start](#quick-start), a `tools` array that declares only the computer use toolset, and the tool-call processing helper under [Implement the computer use tool](#implement-the-computer-use-tool). If you also declare other tools, such as the Quick start's bash and text editor tools, dispatch their `tool_use` blocks in the same pass; the helper answers only computer use member calls, and the loop treats a turn with no answered calls as finished. Here's a simplified example:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def sampling_loop(model: str, messages: list[MessageParam], max_iterations: int = 10):
    """
    Run the computer-use agent loop until Claude stops requesting tools
    or the iteration limit is reached.
    """
    for _ in range(max_iterations):
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=messages,
            tools=TOOLS,
        )

        # Add Claude's response to the conversation history
        messages.append({"role": "assistant", "content": response.content})

        # Run the actions Claude requested, in order, and collect the results
        tool_results = process_tool_calls(response)
        if not tool_results:
            return messages  # No more tool use; task complete

        # Send every result back to Claude in a single user message
        messages.append({"role": "user", "content": tool_results})

    return messages
```

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.

### Optimize model performance with prompting

1.  Specify simple, well-defined tasks and provide explicit instructions for each step.
2.  Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
3.  Some UI elements (such as dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
4.  For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
5.  If you need the model to log in, provide it with the username and password in your prompt inside XML tags such as `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Review [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.
6.  When constructing a user turn's `content` array, place the instruction text *before* the screenshot image. Providing the target description before the image is processed improves click accuracy.
7.  Claude uses the `zoom` action to inspect a region at full resolution when asked about small text or specific UI elements that aren't legible at the screenshot's default resolution, such as file names in a sidebar, tab titles, status-bar text, line numbers, or button labels. If Claude isn't zooming when you expect, ask about a specific region or element rather than the screen as a whole.
8.  If you want every [batch action](#batch-actions) to end with a screenshot, say so in the system prompt, for example, `End each group of actions with a screenshot so you can verify the result before continuing.`



If you repeatedly encounter a clear set of issues or know in advance the tasks Claude will need to complete, use the system prompt to provide Claude with explicit tips or instructions on how to do the tasks successfully.



For agents that span multiple sessions, run end-to-end verification at the start of each session, not only after implementation. Browser-based checks catch regressions from prior sessions that code-level review alone misses. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) for details.

### System prompts

When you include the computer use tool in a request, the API generates a computer use-specific system prompt. It's similar to the [tool use system prompt](/docs/en/agents-and-tools/tool-use/define-tools#tool-use-system-prompt) but starts with:

> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.

As with regular tool use, the user-provided `system` parameter is still respected and used in the construction of the combined system prompt.

### Available actions

Each action is a member tool of the computer use toolset: Claude names the member in a `tool_use` block that carries `"toolset_name": "computer"`, and the block's `input` holds only that member's parameters, with no `action` field. The toolset has 17 member tools:

| Member                                                        | Input                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `screenshot`                                                  | None (`{}`)                                                                                                                                                                                                  | Capture the full display and return it as an image.                                                                                                                                                                                                                           |
| `zoom`                                                        | `region`: `[x0, y0, x1, y1]`, the top-left and bottom-right corners of the area to inspect                                                                                                                   | Capture only that region of the display at full resolution and return it as an image, scaled to fit within your usual screenshot dimensions with its aspect ratio preserved. This lets Claude read small text or dense UI that isn't legible in a downscaled full screenshot. |
| `left_click`                                                  | `coordinate` (optional): `[x, y]`; `text` (optional): modifier keys to hold during the click: `shift`, `ctrl`, `alt`, `super` (the Command or Windows key), or a `+`-joined combination such as `ctrl+shift` | Click the left mouse button at `coordinate`, or at the current cursor position when `coordinate` is omitted.                                                                                                                                                                  |
| `right_click`, `middle_click`, `double_click`, `triple_click` | Same as `left_click`                                                                                                                                                                                         | Other mouse buttons and multiple clicks.                                                                                                                                                                                                                                      |
| `left_click_drag`                                             | `start_coordinate`: `[x, y]`; `coordinate`: `[x, y]`; `text` (optional): modifier keys                                                                                                                       | Press at `start_coordinate`, drag to `coordinate`, and release.                                                                                                                                                                                                               |
| `mouse_move`                                                  | `coordinate`: `[x, y]`                                                                                                                                                                                       | Move the cursor without clicking, for example, to hover.                                                                                                                                                                                                                      |
| `left_mouse_down`, `left_mouse_up`                            | None (`{}`)                                                                                                                                                                                                  | Press or release the left mouse button at the current cursor position, for drags that `left_click_drag` can't express. Move the cursor with `mouse_move` first.                                                                                                               |
| `cursor_position`                                             | None (`{}`)                                                                                                                                                                                                  | Report the cursor's current `[x, y]` position as text.                                                                                                                                                                                                                        |
| `scroll`                                                      | `scroll_direction`: `"up"`, `"down"`, `"left"`, or `"right"`; `scroll_amount`: number of scroll-wheel clicks; `coordinate` (optional): `[x, y]`; `text` (optional): modifier keys                            | Scroll at `coordinate`, or at the current cursor position.                                                                                                                                                                                                                    |
| `type`                                                        | `text`: the string to type                                                                                                                                                                                   | Type literal text at the current keyboard focus.                                                                                                                                                                                                                              |
| `key`                                                         | `text`: a key or a `+`-joined combination such as `"Return"`, `"ctrl+s"`, or `"alt+Tab"`; `repeat` (optional): 1 to 100, default 1                                                                           | Press a key or key combination, `repeat` times.                                                                                                                                                                                                                               |
| `hold_key`                                                    | `text`: a key or combination; `duration`: seconds, up to 300                                                                                                                                                 | Hold a key down for the given duration.                                                                                                                                                                                                                                       |
| `wait`                                                        | `duration`: seconds, up to 300                                                                                                                                                                               | Pause before the next action, for example, while an application loads.                                                                                                                                                                                                        |

Keep the following in mind when implementing the members:

- **Coordinates are in screenshot pixels.** Every `coordinate`, `start_coordinate`, and `region` value, and the position that `cursor_position` reports, is in the pixel space of the full-display screenshots you return, with the origin at the top left. Zoom images don't change this: after a `zoom`, Claude still expresses coordinates in the full screenshot's space, never relative to the zoomed image. If you scale screenshots down before returning them, scale Claude's coordinates back up before applying them to the real display (see [Size screenshots to fit image limits](#handle-coordinate-scaling-for-higher-resolutions)).
- **All members are enabled by default, including `zoom`.** If your environment can't produce zoom images, withhold the member with `configs` (see [Tool parameters](#tool-parameters)) rather than leaving it enabled and returning errors. If Claude calls a member that you have withheld or don't implement, return a `tool_result` with `is_error: true` for that block.
- **Dispatch on the pair (`toolset_name`, `name`).** `toolset_name` is what marks a block as a computer action: a custom tool in the same request can share a member's name, and a later toolset version can add members (see [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets)).

### Example actions

Each example is a complete `tool_use` block as it appears in Claude's response.

Shift+click at a position, for example, to extend a selection. Unlike `hold_key`, `text` holds the modifiers only for the duration of that click or scroll:

```python
{
  "type": "tool_use",
  "id": "toolu_01Qg8m3XqC5aRy7tD2eS4jUg",
  "name": "left_click",
  "toolset_name": "computer",
  "input": { "coordinate": [500, 300], "text": "shift" }
}
```



Drag from one point to another:

```python
{
  "type": "tool_use",
  "id": "toolu_01Ed6j9VnA3yPw5rB8cQ2gSe",
  "name": "left_click_drag",
  "toolset_name": "computer",
  "input": {
    "start_coordinate": [200, 300],
    "coordinate": [600, 300]
  }
}
```



Scroll down three clicks of the wheel:

```python
{
  "type": "tool_use",
  "id": "toolu_01Yc5h8UmZ2xNv4qA7bP9fRd",
  "name": "scroll",
  "toolset_name": "computer",
  "input": {
    "coordinate": [500, 400],
    "scroll_direction": "down",
    "scroll_amount": 3
  }
}
```



Press Tab four times:

```python
{
  "type": "tool_use",
  "id": "toolu_01Sb4g7TkY9wLu3pX6zM8eQc",
  "name": "key",
  "toolset_name": "computer",
  "input": { "text": "Tab", "repeat": 4 }
}
```



Zoom in to inspect a region at full resolution:

```python
{
  "type": "tool_use",
  "id": "toolu_01Kf7k2WpB4zQx6sC9dR3hTf",
  "name": "zoom",
  "toolset_name": "computer",
  "input": { "region": [100, 200, 400, 350] }
}
```



Report the cursor position. Answer this call with a short text result that gives the position in screenshot pixels, for example, `X=512, Y=384`:

```python
{
  "type": "tool_use",
  "id": "toolu_01Ekh3vqB6yTs2mNc4Rw8pLd",
  "name": "cursor_position",
  "toolset_name": "computer",
  "input": {}
}
```



### Tool parameters

The toolset entry in the `tools` array accepts four parameters; the rules they share with the browser use toolset are listed under [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets).

| Parameter         | Required | Description                                                                                                                                                                                                                                                                                                                                                  |
|-------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`            | Yes      | `computer_toolset_20260801`                                                                                                                                                                                                                                                                                                                                  |
| `configs`         | No       | Per-member settings keyed by member name; each member accepts `enabled` (default `true` for all 17, including `zoom`) and `defer_loading` (default `false`, for [tool search](/docs/en/agents-and-tools/tool-use/tool-search-tool#deferred-tool-loading)), and members you omit keep their defaults.                                                         |
| `cache_control`   | No       | [Prompt caching](/docs/en/build-with-claude/prompt-caching) breakpoint at the toolset definition; entry only. A breakpoint on any `tool_use` or `tool_result` block in a batch takes effect at the end of that batch; see [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#cache-control-on-tool-definitions). |
| `allowed_callers` | No       | `["direct"]` only.                                                                                                                                                                                                                                                                                                                                           |

For example, this entry withholds `zoom` for an environment that doesn't implement it and sets a cache breakpoint at the toolset definition:

```python
{
  "type": "computer_toolset_20260801",
  "configs": {
    "zoom": { "enabled": false }
  },
  "cache_control": { "type": "ephemeral" }
}
```



If your agent loop can run only one action per round trip, set `disable_parallel_tool_use` to `true` in `tool_choice`; Claude then returns at most one member `tool_use` block per turn (see [Disable parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use#disable-parallel-tool-use)).

The entry rejects these parameters from earlier tool versions, and a request that includes any of them returns an `invalid_request_error`:

- `name`: member names are fixed by the toolset version.
- `display_width_px`, `display_height_px`, and `display_number`: coordinates are always in the pixel space of the screenshots you return.
- `enable_zoom`: zoom is a member tool that you control through `configs`.

The entry also can't be declared in the same request as a `computer_20251124` entry or another tool named `computer`. For `strict`, `input_examples`, `defer_loading` placement, `tool_choice`, streaming, and caller restrictions, see [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets).

### Combining with thinking

To combine computer use with thinking, see [Thinking](/docs/en/build-with-claude/thinking).



For the earlier `computer_20251124` tool, internal benchmarking on the models that use it suggests these `effort` settings:

- **Claude Opus 4.7:** use `high` as the default; use `low` for high-throughput or cost-sensitive workloads.
- **Claude Sonnet 4.6 and Claude Opus 4.6:** use `medium` as the default (best accuracy-to-cost ratio). Avoid `max`, which adds token cost without improving accuracy on UI tasks. On these models, `low` uses *fewer* output tokens than disabling thinking entirely (fewer mistakes mean fewer retries), making it a strong option for cost-sensitive loops.

### Augmenting computer use with other tools

To add other tools alongside computer use, include them in the same `tools` array. The [Quick start](#quick-start) section shows this pattern with the [bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) and [text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool). You can add your own [custom tool definitions](/docs/en/agents-and-tools/tool-use/define-tools) the same way.

For tasks that stay inside webpages, you can also [declare the browser use tool in the same request](/docs/en/agents-and-tools/tool-use/browser-use-tool#combine-with-other-tools): the two toolsets work independently, each in its own coordinate frame, and calls to members that share a name, such as `screenshot` or `key`, are told apart by `toolset_name`.

### Build a custom computer use environment

The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed to have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:

- A virtualized or containerized environment suitable for computer use with Claude
- An implementation of the computer use tool's actions
- An agent loop that interacts with the Claude API and runs the `tool_use` results using your tool implementations
- An API or UI that allows user input to start the agent loop

### Implement the computer use tool

The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

1.  1

    ### Set up your computing environment

    Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.

2.  2

    ### Implement action handlers

    Create functions to handle each action type that Claude might request:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    # Placeholder image data; a real executor captures the screen and returns the PNG bytes
    PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="


    def capture_screenshot() -> list[ImageBlockParam]:
        # screenshot answers with an image block rather than text: return the result content list
        return [
            {
                "type": "image",
                "source": {"type": "base64", "media_type": "image/png", "data": PLACEHOLDER_PNG},
            }
        ]


    def click(coordinate=None):
        if coordinate is None:
            return "clicked at current cursor"
        x, y = coordinate
        return f"clicked at ({x}, {y})"


    def type_text(text):
        return f"typed: {text}"


    def handle_computer_action(name, tool_input):
        match name:
            case "screenshot":
                return capture_screenshot()
            case "left_click":
                # coordinate is optional; without it, click where the cursor already is
                return click(tool_input.get("coordinate"))
            case "type":
                return type_text(tool_input["text"])
        # Handle other actions as needed
        raise ValueError(f"Unknown or unimplemented member: {name}")
    ```

3.  3

    ### Process Claude's tool calls

    Extract and run tool calls from Claude's responses:

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    

    ``` shiki
    NOT_EXECUTED = "Not executed: an earlier computer action in this turn failed."


    def process_tool_calls(response: Message) -> list[ToolResultBlockParam]:
        """
        Run the computer actions in Claude's response in order and answer each
        one. After the first failure the rest are skipped, because Claude planned
        them assuming the earlier actions succeeded.
        """
        tool_results: list[ToolResultBlockParam] = []
        failed = False
        for block in response.content:
            # Only the computer toolset is declared; route other tools here if you add them
            if block.type != "tool_use" or block.toolset_name != "computer":
                continue
            result: ToolResultBlockParam = {
                "type": "tool_result",
                "tool_use_id": block.id,
                "toolset_name": "computer",
            }
            if failed:
                result["content"] = NOT_EXECUTED
                result["is_error"] = True
            else:
                try:
                    # A string, or a list of content blocks such as the screenshot image
                    result["content"] = handle_computer_action(block.name, block.input)
                except Exception as err:
                    result["content"] = f"Error: {err}"
                    result["is_error"] = True
                    failed = True
            tool_results.append(result)
        return tool_results
    ```

4.  4

    ### Implement the agent loop

    Wrap the two previous steps in a loop that sends the results back and repeats until Claude returns no member tool calls; [Understand the agent loop](#understanding-the-agentic-loop) shows this loop in each language.

### Handle errors

Report a failed action to Claude as a `tool_result` with `is_error: true` and a short description, and include `"toolset_name": "computer"` as on any other member result. If the failed action was part of a [batch action](#batch-actions), answer the remaining blocks in the batch with the halt text shown there instead of running them.

For example, when screenshot capture fails:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "toolset_name": "computer",
      "content": "Error: Failed to capture screenshot. Display may be locked or unavailable.",
      "is_error": true
    }
  ]
}
```



Use the same shape for coordinates outside the display bounds and for actions that fail to run, with a message that says what went wrong.

### Size screenshots to fit image limits

Screenshots and zoom images that you return to the computer use toolset must already fit within your model's [image size limits](/docs/en/build-with-claude/vision#evaluate-image-size): the toolset takes no display dimensions and the API doesn't downscale for you, so an oversized `tool_result` image is rejected with a validation error. Because Claude returns coordinates in the pixel space of the image it sees, keep the scale factor you used so you can map those coordinates back to your screen.



Limits vary by model. Claude Opus 4.7 and later models, including every model that supports `computer_toolset_20260801`, accept up to 2576 pixels on the long edge and 4784 visual tokens total (`⌈width / 28⌉ × ⌈height / 28⌉`, approximately 3.75 megapixels); earlier models accept up to 1568 pixels on the long edge and approximately 1.15 megapixels total (see [Resolution and token cost](/docs/en/build-with-claude/vision#evaluate-image-size) for each model's tier). The following example uses the earlier-model 1568 px / 1.15 MP limits. For a high-resolution-tier model, size to the visual-token limit rather than a pixel total, for example with the resize helper in [Resize your image before uploading](/docs/en/build-with-claude/vision-coordinates#resize-your-image-before-uploading).

If your screen is larger than the limit, resize each screenshot before returning it and scale Claude's returned coordinates back to the original screen space. Because the toolset takes no display dimensions, the resize and the coordinate scaling in your application code are all you need:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import math

screen_width, screen_height = 1512, 982


def get_scale_factor(width, height):
    """Calculate scale factor to meet API constraints."""
    long_edge = max(width, height)
    total_pixels = width * height

    long_edge_scale = 1568 / long_edge
    total_pixels_scale = math.sqrt(1_150_000 / total_pixels)

    return min(1.0, long_edge_scale, total_pixels_scale)


# When capturing screenshot
scale = get_scale_factor(screen_width, screen_height)
scaled_width = int(screen_width * scale)
scaled_height = int(screen_height * scale)

# Resize image to scaled dimensions before sending to Claude
screenshot = capture_and_resize(scaled_width, scaled_height)


# When handling Claude's coordinates, scale them back up
def execute_click(x, y):
    screen_x = x / scale
    screen_y = y / scale
    perform_click(screen_x, screen_y)
```



**macOS Retina displays** capture screenshots at a device pixel ratio of 2, so the image is twice the resolution of the logical screen coordinates. Either downscale the screenshot by 2x before sending, or halve the coordinates Claude returns before issuing the click.

When you choose a display resolution and return screenshots:

- For general desktop tasks, use 1024x768 or 1280x720; for web applications, use 1280x800 or 1366x768.
- Avoid resolutions above 1920x1080 to prevent performance issues.
- Encode screenshots as base64 PNG or JPEG, and consider compressing large screenshots to improve performance.
- Include relevant metadata such as timestamp or display state.
- If you use higher resolutions, ensure coordinates are accurately scaled.

### Manage screenshot history

Long agent loops accumulate screenshots quickly (roughly 1,000–1,800 input tokens each). The API's [request limits](/docs/en/build-with-claude/vision#request-limits) also apply. Once a single request carries more than 20 images, every image in it is held to a stricter per-side limit. A loop that keeps its screenshot history reaches that count within a few dozen turns, so either resize each screenshot so that neither side exceeds 2000 px or prune older screenshots to keep 20 or fewer in the request.

To keep [Prompt caching](/docs/en/build-with-claude/prompt-caching) effective while bounding context:

- Place one `cache_control` breakpoint after the system prompt and tool definitions, and up to three more on the last `tool_result` block of each of the most recent turns, advancing them each turn. Within a [batch action](#batch-actions), markers on several blocks act as a single breakpoint but each still counts toward the limit of four, so use one per turn.
- Prune old screenshots in *batches*, not one each turn. Dropping a screenshot every turn changes the prefix every turn and invalidates the cache. A reasonable default is to keep the last three screenshots and prune every 25 turns, so the prefix stays byte-identical between prune events; if your screenshots exceed 2000 px on either side, choose an interval that keeps each request at 20 or fewer images.
- On Claude Fable 5.1 and Claude Opus 5.5, avoid pruning on the client: removing an earlier screenshot [invalidates every later thinking block](/docs/en/build-with-claude/thinking#preserved-in-conversation) in every request that still carries those turns. Resize screenshots to 2000 px or less per side instead, and use server-side [tool result clearing](/docs/en/build-with-claude/context-editing#tool-result-clearing) to drop old ones from the context. If you must prune, keep [`prefix_mismatch_behavior: "drop_block"`](/docs/en/build-with-claude/thinking#preserved-thinking-controls) set from then on; after each prune, Claude continues without the thinking produced since the pruned screenshot, on that request and every later one.

### Diagnose click issues

If clicks miss their targets, the cause is usually one of the following:

| Symptom                                           | Likely cause                                                                                                                                         | Try                                                                                                                                                                                                                                                             |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clicks consistently offset in one direction       | Claude's coordinates, which are in the pixel space of the screenshots you return, are being applied to a display of a different size without scaling | Scale each coordinate by the ratio of your screen size to your screenshot size before clicking (see [Size screenshots to fit image limits](#handle-coordinate-scaling-for-higher-resolutions)); on macOS Retina displays, account for the 2x device pixel ratio |
| Clicks land in the right area but miss the target | Target is very small, detail was lost downscaling a 4K+ source, or aspect ratio was distorted                                                        | Keep the `zoom` member enabled and implement it so Claude can inspect the region at full resolution; capture at lower DPI or crop to the relevant region; preserve aspect ratio when resizing                                                                   |
| Claude clicks the wrong element entirely          | Ambiguous instruction, or visually similar elements nearby                                                                                           | Use positional prompts ("the blue Submit button in the bottom-right"); break the interaction into smaller steps                                                                                                                                                 |
| Accuracy is consistently poor                     | Resolution too low                                                                                                                                   | Try 1280x720 as a baseline                                                                                                                                                                                                                                      |



**Model choice affects click precision.** Among the models that use the earlier `computer_20251124` tool, Claude Sonnet 4.6 is more mechanically precise at clicking than Claude Opus 4.6 and is more robust when screenshots require heavy downscaling. Claude Opus 4.7 narrows that gap: its click precision is roughly comparable to Sonnet 4.6, and its higher resolution limit means less downscaling is needed.

### Follow implementation best practices

### Add action delays

Some applications need time to respond to actions:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
def click_and_wait(x, y, wait_time=0.5):
    click_at(x, y)
    time.sleep(wait_time)  # Allow UI to update
```

### Validate actions before running them

Check that requested actions are safe and valid:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
display_width, display_height = 1024, 768


def validate_action(action_type, params):
    if action_type == "left_click" and "coordinate" in params:
        x, y = params["coordinate"]
        if not (0 <= x < display_width and 0 <= y < display_height):
            return False, "Coordinates out of bounds"
    return True, None
```

### Log actions for debugging

Keep a log of all actions for troubleshooting:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import logging


def log_action(action_type, params, result):
    logging.info(f"Action: {action_type}, Params: {params}, Result: {result}")
```

------------------------------------------------------------------------

## Migrate from `computer_20251124`

Upgrading from `computer_20251124` to the toolset is optional: the models listed for `computer_20251124` under [Earlier tool versions](#earlier-tool-versions) keep accepting it with its beta header, so an existing integration keeps working until you change it. Claude 5.5 and later models are the exception on the Claude API and Google Cloud: there they accept only the toolset. Upgrade an integration before you move it to one of them. On Amazon Bedrock, Claude Opus 5.5 keeps accepting `computer_20251124`. To upgrade, make the following changes together:

1.  **Remove the beta header.** Drop `anthropic-beta: computer-use-2025-11-24` from your requests. In the SDKs, remove the `betas` parameter and call the Messages API through the standard client rather than the beta namespace.
2.  **Change the `tools` entry.** Set `type` to `computer_toolset_20260801` and delete `name`, `display_width_px`, `display_height_px`, `display_number`, and `enable_zoom`. The toolset rejects each of these fields.
3.  **Choose whether to keep zoom enabled.** Zoom is enabled by default on the toolset, whereas `enable_zoom` defaults to `false`. If your environment doesn't implement zoom, add `"configs": {"zoom": {"enabled": false}}` to keep the previous behavior; otherwise implement it (see [Available actions](#available-actions)).
4.  **Handle every block in a turn.** Update your agent loop to iterate over every `tool_use` block in a response rather than reading only the first, and to dispatch on the block's `name` together with `toolset_name` instead of on `input.action`. Member inputs no longer contain an `action` field; the remaining fields are unchanged.
5.  **Run blocks in order and use the halt text.** Run the blocks sequentially, stop at the first failure, and answer the remaining blocks with `Not executed: an earlier computer action in this turn failed.` as described in [Batch actions](#batch-actions). If your loop can't run batches yet, [Tool parameters](#tool-parameters) explains how to limit Claude to one action per turn.
6.  **Echo `toolset_name` on results.** Add `"toolset_name": "computer"` to every `tool_result` that answers a member call. Results may contain only `text` and `image` content.
7.  **Support `repeat` on `key`.** The `key` member accepts an optional `repeat` count from 1 to 100. A handler that ignores unrecognized fields would press the key once, so make your `key` handler honor `repeat`.
8.  **Resize screenshots yourself.** The toolset rejects a screenshot or zoom image that exceeds the model's image limits instead of downscaling it. Resize before returning the image and keep scaling coordinates as described in [Size screenshots to fit image limits](#handle-coordinate-scaling-for-higher-resolutions).
9.  **Remove unsupported options.** Move any `defer_loading` from the entry into `configs`, with the same value on every enabled member. The other options not supported on toolset entries are listed under [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets).

This is the `tools` entry before the change, sent with the `anthropic-beta: computer-use-2025-11-24` header:

```python
{
  "type": "computer_20251124",
  "name": "computer",
  "display_width_px": 1024,
  "display_height_px": 768,
  "display_number": 1
}
```



This is the `tools` entry after the change, sent with no beta header. The `configs` object keeps zoom off to match the earlier entry, which doesn't set `enable_zoom`; omit `configs` entirely to accept the default and let Claude zoom:

```python
{
  "type": "computer_toolset_20260801",
  "configs": {
    "zoom": { "enabled": false }
  }
}
```



The following pair shows a `tool_use` block before and after the change. The action name moves from `input.action` to `name`, and the block gains `toolset_name`:

```python
{
  "type": "tool_use",
  "id": "toolu_01A9r5kQm2LxWc7vT3nZ4bJs",
  "name": "computer",
  "input": { "action": "left_click", "coordinate": [500, 300] }
}
```



```python
{
  "type": "tool_use",
  "id": "toolu_01A9r5kQm2LxWc7vT3nZ4bJs",
  "name": "left_click",
  "toolset_name": "computer",
  "input": { "coordinate": [500, 300] }
}
```



## Earlier tool versions

Two earlier versions of the computer use tool remain available in beta for existing integrations, for models that don't support the toolset, and on platforms where the toolset isn't currently available. Each requires its [beta header](/docs/en/api/beta-headers) on every request, and their parameters are documented in the [beta Messages API reference](/docs/en/api/beta/messages/create). In the SDKs, pass the header through the `betas` parameter and use the beta namespace; only the computer use tool needs the header, not the bash or text editor tools in the same request.

| Tool version        | Beta header               | Use with                                                                                                                                                                                                                                                                                                                                                   | Parameters                                         |
|---------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `computer_20251124` | `computer-use-2025-11-24` | Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5; on Amazon Bedrock, also Claude Opus 5.5                                                                                                                   | [API reference](/docs/en/api/beta/messages/create) |
| `computer_20250124` | `computer-use-2025-01-24` | Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.1 ([retired, except on Bedrock and Google Cloud](/docs/en/about-claude/model-deprecations)), Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](/docs/en/about-claude/model-deprecations)), and Claude Opus 4 ([retired, except on Google Cloud](/docs/en/about-claude/model-deprecations)) | [API reference](/docs/en/api/beta/messages/create) |

------------------------------------------------------------------------

## Limitations

1.  **Latency:** The current computer use latency for human-AI interactions might be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments.
2.  **Computer vision accuracy and reliability:** Claude might make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude's [summarized thinking](/docs/en/build-with-claude/thinking#summarized-thinking) output can help you understand the model's reasoning and identify potential issues; set `display: "summarized"` on the thinking configuration, because the models that support the toolset omit thinking text by default.
3.  **Tool selection accuracy and reliability:** Claude might make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability might be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks.
4.  **Scrolling reliability:** The scroll action supports direction control (up, down, left, right) and a specified amount. In applications where scrolling doesn't take effect, keyboard alternatives such as Page Down can help.
5.  **Spreadsheet interaction:** Use the fine-grained mouse control actions (`left_mouse_down`, `left_mouse_up`) and modifier-key combinations to select individual cells. Complex spreadsheet operations might still require multiple attempts.
6.  **Account creation and content generation on social and communications platforms:** Although Claude visits websites, its ability to create accounts, generate and share content, or otherwise engage in human impersonation across social media websites and platforms is limited.
7.  **Vulnerabilities:** Jailbreaks and prompt injection can affect computer use as they can any frontier AI system, including through instructions embedded in webpages or images; apply the precautions in [Security considerations](#security-considerations).
8.  **Inappropriate or illegal actions:** Under Anthropic's Terms of Service, you must not employ computer use to violate any laws or the Acceptable Use Policy.

Always carefully review and verify Claude's computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.

## Data retention

Computer use is a client-side tool. All screenshots, mouse actions, keyboard inputs, and any files involved in a session are captured and stored in your environment, not by Anthropic. Anthropic processes the screenshot images and action requests in real time as part of the API call. Retention for those API requests is governed by [API and data retention](/docs/en/manage-claude/api-and-data-retention).

Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Pricing

Computer use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**Toolset definition overhead:** Declaring `computer_toolset_20260801` with its default members adds about 4,500 input tokens to a request (about 4,520 on Claude Fable 5, Claude Mythos 5, Claude Opus 5, and Claude Opus 4.8, and about 4,590 on Claude Sonnet 5), which covers the member tool definitions and the tool use system prompt. Disabling `zoom` with `configs` removes about 410 of those tokens. The exact count for a request is reported in the response `usage`, and you can estimate it in advance with the [token counting endpoint](/docs/en/build-with-claude/token-counting).

**Earlier tool versions:** The following figures apply to the `computer_20251124` and `computer_20250124` tool versions, not to `computer_toolset_20260801`:

- System prompt overhead: 466–499 tokens added to the system prompt
- Tool definition: about 735 input tokens per tool definition (measured with `computer_20250124`)

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Vision pricing](/docs/en/build-with-claude/vision#evaluate-image-size))
- Tool execution results returned to Claude



If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.

## Next steps



[Troubleshooting tool use](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Fix the most common tool-use errors with symptom-to-fix diagnostic tables.

[Reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)

Get started with the complete Docker-based implementation



[Tool use with Claude](/docs/en/agents-and-tools/tool-use/overview)

Connect Claude to external tools and APIs. See where tools execute, when Claude calls them, and which tool fits your task.



[Best practices in detail](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude)

Benchmarked recommendations for resolution, thinking effort, and context management

[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)

Let Claude navigate, read, and interact with webpages in your own browser environment, for tasks that stay inside the browser.

## Compatibility

Supported models  
- Fable 5 and 5.1
- Mythos 5 and 5.1
- Opus 4.8, 5, and 5.5
- Sonnet 5

Supported platforms  
- Claude API
- Claude Platform on AWSBeta
- Amazon BedrockBeta
- Google Cloud
- Microsoft FoundryBeta

- On the Claude API and Google Cloud, Claude 5.5 and later models support computer use only through the `computer_toolset_20260801` toolset and return an error for the earlier `computer_20251124` tool version. To move an existing integration, see [Migrate from `computer_20251124`](#migrate-from-computer-20251124).
- On Amazon Bedrock, Claude Opus 5.5 accepts the earlier `computer_20251124` tool version as Claude Opus 5 does.
- Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5 support computer use only through the earlier `computer_20251124` tool version, which requires a beta header; see [Earlier tool versions](#earlier-tool-versions).
- Platforms other than the Claude API and Google Cloud currently offer only the [earlier beta tool versions](#earlier-tool-versions).
