---
title: "Browser use tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-28T06:33:12Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fbrowser-use-tool)

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

# Browser use tool

Copy page



Let Claude navigate, read, and interact with webpages in your own browser environment with the browser use tool.

Copy page



Browser use tool

[ZDR](/docs/en/manage-claude/api-and-data-retention)

Eligible

excludes [Covered Models](/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements)

The browser use tool lets Claude navigate, read, and interact with webpages in a browser that your application runs. Claude works with the page both through its structure (the accessibility tree, elements, forms, and tabs) and through screenshots and viewport coordinates.

The tool is an Anthropic-defined [client toolset](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets): one `browser_toolset_20260801` entry in `tools` gives Claude 27 member tools by default, such as `navigate`, `read_page`, `left_click`, and `screenshot`, plus four more when you [enable them](#enable-optional-member-tools). Your application runs every call against its own browser automation; nothing runs on Anthropic's side. The tool isn't currently available in [Claude Managed Agents](/docs/en/managed-agents/tools).

Choose browser use when the task stays inside webpages and means acting on them, or when pages build their content with JavaScript. When a task needs a whole desktop, use the [computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool), which works through screenshots and coordinates alone. For reading pages you can point Claude to, or finding sources on the web, the [web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool) and [web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool) are lighter. They're [server tools](/docs/en/agents-and-tools/tool-use/server-tools) that the API runs for you, with no browser to operate.

With browser use, Claude reads and acts on live webpages, so everything a page supplies is untrusted input and the actions Claude takes can have real effects. See [Security considerations](#security-considerations) before you deploy.

## Quick start

The browser use tool is available on the Claude API and [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai): add one entry of type `browser_toolset_20260801`, with no `name`, to the `tools` array of a [Messages API](/docs/en/api/messages/create) request.

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
    max_tokens=2048,
    tools=[{"type": "browser_toolset_20260801"}],
    messages=[
        {
            "role": "user",
            "content": "Open example.com/docs and tell me how to get started.",
        }
    ],
)
print(response)
```

Claude's first response ends with `stop_reason: "tool_use"` and carries one or more member `tool_use` blocks, each naming a member tool in `name` and carrying `"toolset_name": "browser"`:

Output



```python
{
  "id": "msg_01HCDu4XSTLzTAcodEQ58vDo",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5-5",
  "content": [
    {
      "type": "text",
      "text": "I'll open the documentation and read the page to find the getting-started instructions."
    },
    {
      "type": "tool_use",
      "id": "toolu_01NRLabsLyVHZPKxbKvkfSMn",
      "name": "navigate",
      "toolset_name": "browser",
      "input": { "url": "https://example.com/docs" }
    },
    {
      "type": "tool_use",
      "id": "toolu_01UvHU5cDyTZ2vXKf5wCkPqR",
      "name": "read_page",
      "toolset_name": "browser",
      "input": { "filter": "interactive" }
    }
  ],
  "stop_reason": "tool_use",
  "stop_sequence": null
}
```

Your executor (the part of your application that drives the browser and produces tool results) runs `navigate`, then `read_page`. Your application returns one `tool_result` per block in its next request, echoing `toolset_name` on each. The `navigate` result reports the tab it loaded in a `browser_state` block; the `read_page` result is text in which every element carries a reference:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01NRLabsLyVHZPKxbKvkfSMn",
      "toolset_name": "browser",
      "content": [
        { "type": "text", "text": "Navigated to https://example.com/docs" },
        {
          "type": "browser_state",
          "tabs": [
            {
              "tab_id": "tab-1",
              "title": "Documentation",
              "url": "https://example.com/docs",
              "active": true
            }
          ]
        }
      ]
    },
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01UvHU5cDyTZ2vXKf5wCkPqR",
      "toolset_name": "browser",
      "content": [
        {
          "type": "text",
          "text": "link \"Documentation\" [ref_1]\nlink \"Getting started\" [ref_2]\ntextbox \"Search docs\" [ref_3]\nbutton \"Search\" [ref_4]\nlink \"Pricing\" [ref_5]"
        }
      ]
    }
  ]
}
```



Claude now holds references it can act on, so its next turn can click `ref_2` to open the getting-started page, with no need to locate the link in a screenshot first.

## How browser use works

Browser use runs as an agent loop in your application: Claude returns member tool calls, your executor runs them against the browser, and you return the results until Claude answers in text.

1.  1

    ### Provide Claude with the browser use tool and a user prompt

    - Add the `browser_toolset_20260801` entry, and optionally other tools, to your API request.
    - Include a user prompt that calls for working with webpages, for example, "Open example.com/docs and tell me how to get started."

2.  2

    ### Claude responds with member tool calls

    - Claude returns one or more `tool_use` blocks in a single assistant turn; several in one turn form a batch action, for example, `left_click`, then `type`, then `key`.
    - Each block's `name` is the member name, each carries `"toolset_name": "browser"`, and `input` holds only that member's parameters, with no `action` field. The response's `stop_reason` is `tool_use`.

3.  3

    ### Run the calls in order and return results

    - Iterate every `tool_use` block in `response.content` (don't assume there's exactly one) and run them sequentially, in the order they appear, because later calls usually depend on earlier ones.
    - Return one `tool_result` per block in a new `user` message, matched by `tool_use_id`, and echo `"toolset_name": "browser"` on each. Every call must be answered or the next request is rejected.
    - If a call fails, return `is_error: true` with a text description for that block, then apply the halt rule in [Batch actions](#batch-actions) to every later block in the turn.

4.  4

    ### Claude continues until the task is complete

    - Claude reads the results (page text, accessibility trees, screenshots, tab state) and, if it needs more, returns further member calls, which takes you back to step 3.
    - Otherwise, it returns a text response to the user.

Here's a skeleton of that loop's tool-call step in two parts. First, stub member handlers stand in for your browser automation. Five members (`navigate`, `read_page`, `left_click`, `type`, and `screenshot`) return the text, or for `screenshot` the image block, that becomes the result content, and the dispatcher raises an error for any member it doesn't implement.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# Placeholder image data; a real executor captures the viewport and returns the PNG bytes
PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="


def navigate(url):
    return f"navigated to {url}"


def read_page():
    return 'link "Docs" [ref_1]\nbutton "Search" [ref_2]'


def click(target):
    # A target is an element reference from read_page or find, or a viewport coordinate
    if target["type"] == "ref":
        return f"clicked {target['ref']}"
    return f"clicked at ({target['x']}, {target['y']})"


def type_text(text):
    return f"typed: {text}"


def capture_screenshot() -> list[ImageBlockParam]:
    # screenshot answers with an image block rather than text: return the result content list
    return [
        {
            "type": "image",
            "source": {"type": "base64", "media_type": "image/png", "data": PLACEHOLDER_PNG},
        }
    ]


def handle_browser_action(name, tool_input):
    if name == "navigate":
        return navigate(tool_input["url"])
    elif name == "read_page":
        return read_page()
    elif name == "left_click":
        return click(tool_input["target"])
    elif name == "type":
        return type_text(tool_input["text"])
    elif name == "screenshot":
        return capture_screenshot()
    # Handle other actions as needed
    raise ValueError(f"Unknown or unimplemented member: {name}")
```

The second part runs a batch in order, dispatches each block to those handlers, echoes `toolset_name` on every result, and applies the halt rule from [Batch actions](#batch-actions), turning a handler error into an error result. The sampling loop that calls it is the one shown in [Understand the agent loop](/docs/en/agents-and-tools/tool-use/computer-use-tool#understanding-the-agentic-loop), with the browser toolset in `tools`.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
NOT_EXECUTED = "Not executed: an earlier action in this turn failed."


def process_tool_calls(response: Message) -> list[ToolResultBlockParam]:
    """
    Run the browser actions in Claude's response in order and answer each
    one. After the first failure the rest are skipped, because Claude planned
    them assuming the earlier actions succeeded.
    """
    tool_results: list[ToolResultBlockParam] = []
    failed = False
    for block in response.content:
        # Only the browser toolset is declared; route other tools here if you add them
        if block.type != "tool_use" or block.toolset_name != "browser":
            continue
        result: ToolResultBlockParam = {
            "type": "tool_result",
            "tool_use_id": block.id,
            "toolset_name": "browser",
        }
        if failed:
            result["content"] = NOT_EXECUTED
            result["is_error"] = True
        else:
            try:
                # A string or a list of content blocks; a real executor also adds a
                # browser_state block to navigation and tab-management results
                result["content"] = handle_browser_action(block.name, block.input)
            except Exception as err:
                result["content"] = f"Error: {err}"
                result["is_error"] = True
                failed = True
        tool_results.append(result)
    return tool_results
```

Dispatch each block on the pair (`toolset_name`, `name`) rather than on `name` alone, because a custom tool in the same request may share a member's name; [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets) describes the parts of this contract both toolsets share. If Claude names a member your executor doesn't implement, or one you disabled, answer that block with an [error result](#return-errors-from-your-executor) rather than dropping it.

When you stream the response, each member's `input` arrives as one complete `input_json_delta` rather than as fragments, so wait for the turn to finish before running the batch.

### Batch actions

A turn with several member calls is a batch action: run the calls in the order they appear, stop at the first failure, and answer every later call with `is_error: true` and the exact text `Not executed: an earlier action in this turn failed.` A batch uses the same response shape as [parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use); the difference is that you run the blocks in order rather than concurrently. Here Claude clicks the search box it found earlier, types a query, and presses Enter in one turn:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "left_click",
      "toolset_name": "browser",
      "input": { "target": { "type": "ref", "ref": "ref_3" } }
    },
    {
      "type": "tool_use",
      "id": "toolu_01Ez4kLb1nQ2vXo8sJ9pWm3c",
      "name": "type",
      "toolset_name": "browser",
      "input": { "text": "install" }
    },
    {
      "type": "tool_use",
      "id": "toolu_01FkP8rTz6uYh2mNq4LsXw7v",
      "name": "key",
      "toolset_name": "browser",
      "input": { "text": "Enter" }
    }
  ]
}
```



Your application returns three `tool_result` blocks in one `user` message, each carrying `toolset_name` and a short text acknowledgment such as `Clicked element ref_3.` Pressing Enter loads a results page, so the `key` result also carries a `browser_state` block with the tab's updated URL ([Tab context on other results](#tab-context-on-other-results)). If the click had failed instead, its result would carry your error text and the other two results would carry the halt text, as shown under [Return errors from your executor](#return-errors-from-your-executor).

You don't need to return a screenshot after every call. Claude typically ends a batch with an observation call (`screenshot`, `read_page`, or `get_page_text`), and your application can also attach its own observation, such as a fresh screenshot or accessibility tree, as an extra content block on the last result in the batch to save a round trip. Because a tab-management result must be exactly one `browser_state` block, attach it to the last result that isn't a tab-management call.

If your executor can run only one call per round trip, set `disable_parallel_tool_use` to `true` in `tool_choice` and Claude returns at most one member call per turn, at the cost of more round trips ([Disable parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use#disable-parallel-tool-use)). The rest of the contract under [Batch actions for the computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool#batch-actions) carries over, including one `tool_result` for every `tool_use` in the next `user` message, except for two things: the halt text and what a successful result's `content` holds. Result content follows [Member tools](#member-tools) on this page instead: a `new_tab`, `switch_tab`, `close_tab`, or `list_tabs` result is exactly one `browser_state` block with no text or image ([Tab management results](#tab-management-results)), and any other member's result may add a `browser_state` block to its text or image ([Tab context on other results](#tab-context-on-other-results)). Where cache breakpoints inside a batch take effect is described in the `cache_control` row of the computer use tool's [Tool parameters](/docs/en/agents-and-tools/tool-use/computer-use-tool#tool-parameters).

### Targets and coordinates

Member tools that act on a location take a `target` object, which is either a viewport-pixel coordinate or a reference to an element that `read_page` or `find` returned. The [Member tools](#member-tools) tables write `Target` for a parameter that accepts either shape.

| Shape              | `target.type`  | Fields                                         | Accepted by                                                                                                                                                                               |
|:-------------------|:---------------|:-----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CoordinateTarget` | `"coordinate"` | `x`, `y` (integers, viewport pixels)           | `left_click`, `right_click`, `middle_click`, `double_click`, `triple_click`, `hover`, `left_click_drag` (`from` and `target`), `left_mouse_down`, `left_mouse_up`, `mouse_move`, `scroll` |
| `RefTarget`        | `"ref"`        | `ref` (an element reference such as `"ref_2"`) | `left_click`, `right_click`, `middle_click`, `double_click`, `triple_click`, `hover`, `scroll_to`, `form_input`, `file_upload`                                                            |

**Coordinates are viewport pixels**, the pixel space of a full-viewport `screenshot` with the origin at the top left of the rendered page; there's no surrounding desktop or window frame. The toolset declares no display dimensions and Claude infers the viewport size from the screenshots you return, so keep them one consistent size. A `zoom` doesn't change the frame, so its `region` and any coordinates Claude emits after seeing the zoomed image are still full-viewport pixels.

**Screenshots must fit the image limits.** The API doesn't downscale toolset images: a screenshot or zoom image over your model's [image size limits](/docs/en/build-with-claude/vision#evaluate-image-size), or over the stricter per-image limit that applies once a request holds [more than 20 images](/docs/en/build-with-claude/vision#request-limits), is rejected. Resize before returning, and scale Claude's coordinates back up by the inverse of your factor before dispatching them ([Size screenshots to fit image limits](/docs/en/agents-and-tools/tool-use/computer-use-tool#handle-coordinate-scaling-for-higher-resolutions)).

**Element references come from `read_page` and `find`.** Each element in their output carries a tag such as `[ref_2]`, as in the Quick start result:

``` block
link "Documentation" [ref_1]
link "Getting started" [ref_2]
textbox "Search docs" [ref_3]
button "Search" [ref_4]
link "Pricing" [ref_5]
```



Claude passes a reference back as a `{"type": "ref", "ref": "ref_2"}` target on a later click, `hover`, `scroll_to`, `form_input`, or `file_upload` call, or as the `ref` parameter on `read_page` to read a subtree. Your executor assigns the references, keeps the mapping from each one to the underlying node (an accessibility-node ID, a stored selector, or equivalent), and acts on that node when a reference comes back.

References are scoped to the tab that produced them and stay valid until that tab navigates or its DOM changes materially. The API can't detect a stale or unknown reference, so when Claude passes a reference your executor no longer recognizes, return an error result such as `Error: ref_3 is stale or not found on the current page. Re-read the page to get fresh references.` Claude then reads the page again. Don't renumber references you've already handed out for a tab until it navigates, because that silently invalidates references Claude still holds.

Claude uses both targeting styles and switches between them based on what the page exposes; your prompt and what your executor returns steer the choice:

- **Prefer references where the page has a usable accessibility tree.** A reference survives layout shifts and reflows that make pixel coordinates fragile, and lets Claude act on controls that are hard to hit with a pointer.
- **Fall back to coordinates for content the tree doesn't describe.** Canvas-rendered interfaces, embedded video or remote-desktop surfaces, heavily virtualized lists, and elements inside cross-origin iframes often have no useful node, so Claude works from `screenshot` and `zoom` and clicks by coordinate; your executor resolves which frame a coordinate lands in.
- **Scope reads, and read the tree before you screenshot.** On large pages, `read_page` with `filter: "interactive"` or the `ref` of a container returns a focused subtree, and a tree read of a typical page often costs fewer input tokens than a screenshot while giving Claude references it can act on immediately. Screenshots remain the right observation when visual layout, images, or rendering state matter.

## Security considerations

Browser use carries risks that standard API features don't, because Claude reads and acts on content from the open web, where any page can contain text written to manipulate it.



To reduce these risks, take precautions such as the following:

1.  Run the browser and your executor in a dedicated container or virtual machine with minimal privileges, a fresh profile that holds no credentials, and no access to sensitive filesystems or internal networks; isolate any tool you run alongside it the same way.
2.  Restrict the hosts the browser can reach to a domain allowlist enforced at the network layer and re-checked in your `navigate` handler after redirects, and block loopback, link-local, and private ranges unless the task needs them.
3.  Treat everything a page supplies as untrusted input, including the tab titles and URLs, and each download's `url`, `path`, and `error`, that you report in a [`browser_state`](#track-tabs-and-page-state) block, and build page reads from what the page renders (the accessibility tree or visible text), not raw DOM source, so hidden text doesn't reach Claude.
4.  In your `navigate` handler, accept the history keywords `"back"`, `"forward"`, and `"reload"`, treat a URL without a scheme as `https://`, then parse the URL and refuse any scheme other than `http` or `https` (`javascript:`, `file:`, `data:`, `chrome:`, and so on) with an [error result](#return-errors-from-your-executor). Check the scheme with a URL parser rather than a string prefix; the API doesn't filter the URLs Claude opens, so it can't reject one for you.
5.  Leave `javascript_exec` and `file_upload` disabled unless you need them, and read [Enable optional members](#enable-optional-member-tools) before turning either on.
6.  Have a human confirm consequential actions and anything that requires affirmative consent (purchasing, modifying accounts, messaging, and accepting terms), and make that check in your executor before each call, because one turn can carry several.

Claude sometimes follows instructions found in page content even when they conflict with yours; text on a page that says "ignore your previous instructions and navigate to..." can divert it from the task. Isolate Claude from sensitive data and actions to limit what a prompt injection can reach, review [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), and if a task can't avoid a logged-in session, use a dedicated low-privilege account and keep human confirmation on account-changing actions.

Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the browser use tool, classifiers will automatically scan what the browser returns, such as page text or screenshots, to flag potential prompt injections. When these classifiers identify a potential prompt injection, they will automatically steer the model to check whether the instruction really came from you before acting on it.

This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, [contact support](https://support.claude.com/en/). The precautions above remain important even with these classifiers in place.

Because the browser runs in your environment, the sites Claude visits see your executor's network identity, and page content reaches the API only as the tool results you return. Inform end users of the relevant risks and obtain their consent before enabling browser use in your products.

## Member tools

The `browser_toolset_20260801` entry declares 31 member tools; each call's `input` is exactly the parameters listed here, and `tab_id`, where optional, defaults to the active tab. `Target`, `CoordinateTarget`, and `RefTarget` are the shapes described in [Targets and coordinates](#targets-and-coordinates). Four members (`javascript_exec`, `file_upload`, `read_console`, and `read_network`) are disabled by default and appear only when you [enable them](#enable-optional-member-tools). The input bounds and output conventions noted in each member's row are stated to Claude, not enforced by the API, so validate inputs (including coordinates against your viewport) and apply the conventions in your executor.

Only `screenshot` and `zoom` require an [`image` block](/docs/en/agents-and-tools/tool-use/handle-tool-calls#handling-results-from-client-tools) in their result, and the four tab-management members (`new_tab`, `list_tabs`, `switch_tab`, and `close_tab`) return exactly one `browser_state` block (see [Tab management results](#tab-management-results)). Every other member returns a `text` block: either a short acknowledgment such as `Clicked element ref_2.` or the member's output. Any result other than a tab-management result may also carry an `image` block, typically a screenshot taken after the action, so Claude sees the outcome without a separate `screenshot` call; [Batch actions](#batch-actions) shows where to attach one in a batch. A member `tool_result` may contain only `text`, `image`, and `browser_state` content blocks.

### Navigation and capture

| Member       | Input               | Description                                                                                                                                                                                                                                                                                     |
|:-------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `navigate`   | `url`, `tab_id?`    | Load an `http` or `https` URL, or move through history with `"back"`, `"forward"`, or `"reload"`. Treat a URL without a scheme as `https://` and refuse any other scheme with an error result. Return a short acknowledgment, plus a `browser_state` block when the tab's URL or title changed. |
| `screenshot` | `tab_id?`           | Capture the viewport and return an `image` block.                                                                                                                                                                                                                                               |
| `zoom`       | `region`, `tab_id?` | Return a cropped, upscaled `image` of `region`, given as `[x0, y0, x1, y1]` in viewport pixels, for closer inspection of small text or controls.                                                                                                                                                |

### Pointer

| Member            | Input                                                                       | Description                                                                                                                                                    |
|:------------------|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `left_click`      | `target: Target`, `modifiers?`, `tab_id?`                                   | Left-click a coordinate or a referenced element. `modifiers` is a chord held during the click, for example, `"shift"` or `"ctrl+shift"`.                       |
| `right_click`     | `target: Target`, `modifiers?`, `tab_id?`                                   | Right-click a coordinate or element.                                                                                                                           |
| `middle_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Middle-click a coordinate or element.                                                                                                                          |
| `double_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Double left-click a coordinate or element.                                                                                                                     |
| `triple_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Triple left-click a coordinate or element, which typically selects a line or paragraph.                                                                        |
| `hover`           | `target: Target`, `tab_id?`                                                 | Move the pointer over a coordinate or element without clicking.                                                                                                |
| `left_click_drag` | `from: CoordinateTarget`, `target: CoordinateTarget`, `tab_id?`             | Press at `from`, drag to `target`, and release.                                                                                                                |
| `left_mouse_down` | `target: CoordinateTarget`, `tab_id?`                                       | Press and hold the left button at a coordinate; pair with `left_mouse_up` for a custom drag.                                                                   |
| `left_mouse_up`   | `target: CoordinateTarget`, `tab_id?`                                       | Release the left button at a coordinate.                                                                                                                       |
| `mouse_move`      | `target: CoordinateTarget`, `tab_id?`                                       | Move the pointer to a coordinate.                                                                                                                              |
| `scroll`          | `target: CoordinateTarget`, `scroll_direction`, `scroll_amount?`, `tab_id?` | Scroll at a viewport position. `scroll_direction` is `"up"`, `"down"`, `"left"`, or `"right"`; `scroll_amount` is in scroll-wheel notches, 1 to 10, default 3. |
| `scroll_to`       | `target: RefTarget`, `tab_id?`                                              | Scroll a referenced element into view.                                                                                                                         |

### Keyboard and timing

| Member     | Input                         | Description                                                                                                                                                                               |
|:-----------|:------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`     | `text`, `tab_id?`             | Type a literal string at the current focus.                                                                                                                                               |
| `key`      | `text`, `repeat?`, `tab_id?`  | Press a key or chord. `text` is a single key (`"Enter"`), a chord joined with `+` (`"ctrl+a"`), or a space-separated sequence (`"Backspace Backspace"`); `repeat` is 1 to 100, default 1. |
| `hold_key` | `text`, `duration`, `tab_id?` | Hold a key or chord for `duration` seconds, 0 to 30.                                                                                                                                      |
| `wait`     | `duration`, `tab_id?`         | Pause for `duration` seconds, 0 to 30.                                                                                                                                                    |

### Page reading

| Member          | Input                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------------|:---------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `read_page`     | `filter?`, `depth?`, `ref?`, `tab_id?` | Return the page's accessibility tree as text with each element tagged with a reference such as `[ref_2]`. With `filter` omitted, return every visible element; with `"interactive"`, only visible interactive elements; with `"all"`, also elements outside the viewport. `depth` caps the tree depth (minimum 1, default 15) and `ref` scopes the read to that element's subtree. Cap the output at 50,000 characters and say so in the text; Claude then narrows with a smaller `depth` or a `ref`. |
| `find`          | `query`, `tab_id?`                     | Search for elements matching a natural-language description such as `"search field"` or `"add to cart button"`, and return up to 20 matches in the same tagged format as `read_page`.                                                                                                                                                                                                                                                                                                                 |
| `get_page_text` | `tab_id?`                              | Return the page's visible text as plain text, prioritizing the main article content; suited to articles, documentation, and other text-heavy pages.                                                                                                                                                                                                                                                                                                                                                   |

### Forms and files

| Member                              | Input                                                     | Description                                                                                                                                                                                        |
|:------------------------------------|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `form_input`                        | `target: RefTarget`, `value`, `tab_id?`                   | Set a form element's value directly. `value` is a `string`, `number`, or `boolean`; use a `boolean` for checkboxes and an option's value or visible text for selects.                              |
| `file_upload` (disabled by default) | `target: RefTarget`, `paths?`, `document_ids?`, `tab_id?` | Set the files on a file-input element from `paths` on the executor's filesystem, `document_ids` your application has staged, or both; at least one is required. See [Upload files](#upload-files). |

### Diagnostics and scripting

| Member                                  | Input             | Description                                                                                                                                                                                        |
|:----------------------------------------|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `read_console` (disabled by default)    | `tab_id?`         | Return the tab's console entries (log, warning, and error lines) accumulated since the last read, one line per entry. See [Read console and network activity](#read-console-and-network-activity). |
| `read_network` (disabled by default)    | `tab_id?`         | Return the tab's network requests (method, URL, status, MIME type, timing) since the last read, one line per entry.                                                                                |
| `javascript_exec` (disabled by default) | `text`, `tab_id?` | Run `text` as JavaScript in the page context and return the value of the last expression as text. See [Enable optional members](#enable-optional-member-tools).                                    |

### Tab management

| Member       | Input               | Description                            |
|:-------------|:--------------------|:---------------------------------------|
| `new_tab`    | (none)              | Open a tab and make it the active tab. |
| `list_tabs`  | (none)              | Report the tab inventory.              |
| `switch_tab` | `tab_id` (required) | Make `tab_id` the active tab.          |
| `close_tab`  | `tab_id` (required) | Close `tab_id`.                        |

On success, each of these returns exactly one `browser_state` block and no text or image; see [Tab management results](#tab-management-results).

## Configure the toolset

Besides `type`, the toolset entry accepts `configs`, `cache_control`, and `allowed_callers`; the rules these fields share with the computer use toolset are listed under [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets), and this section covers the browser-specific defaults. `configs` is an object keyed by member name, and each member's value accepts two fields:

| Field           | Default                                                                               | Meaning                                                                                                                                                                                                                                                                                                               |
|:----------------|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enabled`       | `true`, except `false` for the four [optional members](#enable-optional-member-tools) | Whether the member is offered to Claude.                                                                                                                                                                                                                                                                              |
| `defer_loading` | `false`                                                                               | Whether the toolset's definition is deferred for tool search. Must resolve to the same value on every enabled member. With the four optional members left disabled, deferring the toolset means setting it on the other 27; see [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets). |

### Enable or disable member tools

List only the members you want to change in `configs`; every member you omit keeps its default. For example, an executor that implements console reads but not low-level pointer or key-hold control turns `read_console` on and withholds three members:

```python
{
  "type": "browser_toolset_20260801",
  "configs": {
    "read_console": { "enabled": true },
    "left_mouse_down": { "enabled": false },
    "left_mouse_up": { "enabled": false },
    "hold_key": { "enabled": false }
  }
}
```



A disabled member disappears from the definition Claude sees; that doesn't guarantee Claude never names it, so your executor still answers such a call with an [error result](#return-errors-from-your-executor).

### Combine with other tools

Declare the browser use tool alongside your own tools and other Anthropic-provided tools in the same `tools` array. A custom tool may share a member's name (your own `navigate`, for example), because `toolset_name` distinguishes Claude's calls, but no other entry may be named `browser`, and a request may contain only one browser toolset entry.

You can also declare it alongside the [computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool), either the toolset or an earlier computer use tool version. The two work independently, each in its own coordinate frame (viewport pixels here, desktop screenshot pixels there), and Claude's calls to members that share a name, such as `screenshot` or `key`, are told apart by `toolset_name`.

## Enable optional members

Four member tools are disabled by default: `javascript_exec` and `file_upload` because they widen what a manipulated page could make Claude do, and `read_console` and `read_network` because not every browser automation stack can supply those logs and they widen what page-controlled content reaches Claude. Enable each one with `configs` (for example, `"configs": {"file_upload": {"enabled": true}}`) only when your executor implements it and the task needs it.

### Upload files

`file_upload` sets the files on an `<input type="file">` element directly, which is more reliable than driving a native file chooser. Its `target` is a reference only, because the call needs the element's identity, and it takes `paths`, `document_ids`, or both:

- `paths` are file paths on the executor's filesystem, for deployments where the executor can read your application's files directly (the same condition under which you populate a download's `path`).
- `document_ids` are identifiers for files your application has staged for the browser, for deployments where it can't. Your application defines what the identifiers mean; scope their resolution the way you scope `paths`, to files staged for this task.

```python
{
  "type": "tool_use",
  "id": "toolu_01N7gVzFEfZjLjgsYwnrPgrF",
  "name": "file_upload",
  "toolset_name": "browser",
  "input": {
    "target": { "type": "ref", "ref": "ref_12" },
    "paths": ["/home/user/uploads/summary.pdf"],
    "tab_id": "tab-2"
  }
}
```



Claude writes these paths while it's reading untrusted pages, so an unrestricted implementation would let a malicious page direct the upload of any file the executor can read to a site the page controls. Enable the member only when your executor resolves each path (following symlinks and `..` segments) and accepts nothing outside a dedicated, allowlisted upload directory that holds only files meant for the task. Don't reuse the browser's download directory for this; if you do, every file a page causes the browser to download becomes uploadable.

### Run JavaScript in the page

`javascript_exec` runs the expression Claude writes in the page's context and returns the value of the last expression as text; Claude writes an expression, not a `return` statement. The code runs with the page's full privileges, including its cookies, storage, and same-origin requests. Enable the member only in sessions that hold no credentials, keep the domain allowlist from [Security considerations](#security-considerations) in force, treat the returned value as untrusted input, and log the code Claude emits.

### Read console and network activity

`read_console` returns the tab's console entries and `read_network` returns its network requests, each as text with one line per entry accumulated since the previous read of that tab. A console line carries a log, warning, or error entry; a network line carries the method, URL, status, MIME type, and timing. Entries exist only from the moment your browser automation attached to the tab, so an empty result doesn't mean a tab that was already open had no traffic.

These members let Claude diagnose a misbehaving page (a failed request behind a spinner, a script error behind a dead button) without repeated screenshots. Console and network entries are page-controlled and often contain secrets such as tokens in request URLs, so redact credential-like values you don't want in Claude's context and truncate very long entries before returning them.

## Track tabs with `browser_state`

Claude addresses tabs by `tab_id`, your application is the source of truth for which tabs exist, and you report that state in a `browser_state` content block that Claude never sees directly: the API renders the text Claude reads from it.

```python
{
  "type": "browser_state",
  "tabs": [
    {
      "tab_id": "tab-1",
      "title": "Documentation",
      "url": "https://example.com/docs",
      "active": true
    },
    { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" }
  ]
}
```



- `tabs` is the full inventory of open tabs after the call, not a delta. It may be empty; whenever it isn't, exactly one entry carries `"active": true`.
- `state_changes` (not shown here) reports side effects of the call: a `tab_opened` entry for each tab the call opened that's still open when it finishes, whose `tab_id` must also appear in `tabs`, and [download events](#report-downloads). Omit the field when there's nothing to report; an empty array is rejected.
- Send the block only on results that answer a browser member call, at most once per `tool_result`, and never on a result with `is_error: true`. You express "no tab state to report" by omitting the block.
- The API renders `tabs`, and any download entries in `state_changes`, into text for Claude. The next two sections and [Report downloads](#report-downloads) show that text.

**You assign `tab_id` values.** Any stable string works, such as your automation library's page identifier or your own counter, as long as you don't reuse a `tab_id` while a tab with that identifier is still listed as open in an earlier result. The API enforces these limits on the block:

- Each `tab_id`, `title`, and `url` may be at most 4,096 characters, `tab_id` must be non-empty, and none may contain control characters (including newlines) or Unicode line or paragraph separators.
- A block may list at most 100 tabs and 200 state changes.
- The same limits apply to the `tab_id` Claude passes to `switch_tab` and `close_tab`, because the API renders it into the result text, so answer a call whose `tab_id` violates them with an error result instead of a `browser_state` block.



Tab titles and URLs come from the page and render into text Claude reads, so they're a prompt-injection surface. The API renders tab URLs verbatim, so sanitize page-supplied URLs before populating `tabs`. It escapes double quotes and backslashes in titles when it renders them, so don't pre-escape titles (a pre-escaped title reaches Claude double-escaped); truncating or dropping suspicious titles is still worthwhile. A download entry's `url`, `path`, and `error` also render into text Claude reads, so treat them as untrusted too; the API quotes and escapes them as it does titles. The length and character limits the API enforces are a floor, not a defense.

### Tab management results

For `new_tab`, `switch_tab`, `close_tab`, and `list_tabs`, a successful result's `content` is exactly one `browser_state` block with no text or image, and the API writes the text Claude sees. A `new_tab` result's block must also carry exactly one `tab_opened` state change whose `tab_id` matches the entry marked `active: true`.

| Member       | Text Claude sees                                                                                                            |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------|
| `switch_tab` | `Switched to tab {tab_id}`, taken from the call's `input.tab_id`                                                            |
| `close_tab`  | `Closed tab {tab_id}`, taken from the call's `input.tab_id`                                                                 |
| `new_tab`    | `Created new tab with tab_id: {tab_id}, URL: {url}. It is now the current tab.`, taken from the entry marked `active: true` |
| `list_tabs`  | `Available tabs:` followed by one line per tab, or `No tabs available` when `tabs` is empty                                 |

A `list_tabs` result whose block lists two tabs with the first one active renders as follows, with each line indented two spaces and ` (current)` appended to the active tab only:

``` block
Available tabs:
  • tab_id tab-1: "Documentation" (https://example.com/docs) (current)
  • tab_id tab-2: "Pricing" (https://example.com/pricing)
```



An error result for one of these members is the reverse: ordinary error text in `content`, `is_error: true`, and no `browser_state` block.

For example, when Claude calls `new_tab` (its `input` is empty), your executor opens the tab, makes it active, and returns the inventory with one `tab_opened` entry:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01WvHSbQVV9j5nWGvTmk4vNL",
      "toolset_name": "browser",
      "content": [
        {
          "type": "browser_state",
          "tabs": [
            { "tab_id": "tab-1", "title": "Documentation", "url": "https://example.com/docs" },
            { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" },
            { "tab_id": "tab-3", "title": "", "url": "about:blank", "active": true }
          ],
          "state_changes": [{ "type": "tab_opened", "tab_id": "tab-3" }]
        }
      ]
    }
  ]
}
```



Claude sees `Created new tab with tab_id: tab-3, URL: about:blank. It is now the current tab.` Report the URL the tab was opened at, as here, not one it later redirects to; later results report the tab's then-current URL.

### Tab context on other results

On every other member the block is optional: send it when the set of open tabs, the active tab, or a tab's title or URL changed, or when there are `state_changes` to report, and always include the full `tabs` inventory. When a result carries both text and a `browser_state` block, the API appends a `Tab Context` footer to that result's text, separated from your text by a blank line, so Claude receives the new state without a separate `list_tabs` call:

```python
Tab Context:
- Executed on tab_id: tab-1
- Available tabs:
  • tab_id tab-1: "Documentation" (https://example.com/docs)
  • tab_id tab-2: "Pricing" (https://example.com/pricing)
```



`Executed on` names the tab the call ran on, which is its `tab_id` input when present and otherwise the active tab, and the footer's tab lines carry no `(current)` marker. Don't append this text yourself; send the structured block and let the API render it. The footer is deduplicated, so identical tab state isn't rendered again on later results and populating the block liberally costs nothing.

Three cases render no footer even when the block is present:

- Any `zoom` result.
- A result with no `text` block (an image-only `screenshot` result, for example). Nothing is rendered or remembered for that result; the tab context appears on the next result that carries both text and a `browser_state` block, so include a short text block alongside the image when you want Claude to see a tab change on that same result. The exception is a result whose block reports a [download event](#report-downloads). The API adds the download lines as a text block, and the footer follows them as it would on any result with text.
- A result whose `tabs` list is empty on a call that carried no `tab_id`, because there's no tab to name.

For example, when Claude clicked the "Pricing" link (`ref_5`) earlier in this session, the page opened it in a new tab Claude didn't ask for, and without a report Claude would have to call `list_tabs` to discover it. Return the click's acknowledgment plus a block whose `state_changes` names the opened tab, marking whichever tab your executor left active:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01EgTXj1FjE2FCTt2zNFWLao",
      "toolset_name": "browser",
      "content": [
        { "type": "text", "text": "Clicked element ref_5." },
        {
          "type": "browser_state",
          "tabs": [
            {
              "tab_id": "tab-1",
              "title": "Documentation",
              "url": "https://example.com/docs",
              "active": true
            },
            { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" }
          ],
          "state_changes": [{ "type": "tab_opened", "tab_id": "tab-2" }]
        }
      ]
    }
  ]
}
```



Claude sees `Clicked element ref_5.` followed by the Tab Context footer shown earlier. A tab opened during a call that failed gets no `tab_opened` entry, because error results carry no `browser_state`; it appears in the `tabs` inventory of the next successful result instead. In a batch, attach the block to the result of the call during which the change happened, and give every successful tab-management result its own block even when an earlier result in the same turn reported the same state.

### Report downloads

When a click or navigation starts a file download, report it in `state_changes` on the result of the call during which it happened, correlated across results by a `download_id` you assign. Downloads run asynchronously and can span several results, so there are three event types:

| `type`               | Fields                                       | When to send                                                                                                                                                                                                                                                                                                                 |
|:---------------------|:---------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `download_started`   | `download_id`, `url`                         | On the result of the call during which the download began. `url` is the final URL the file is served from, after redirects.                                                                                                                                                                                                  |
| `download_completed` | `download_id`, `url`, `path?`, `size_bytes?` | On the result of whichever later call is running when the download finishes. Include `path` only when another tool in the same environment (for example, the [bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) or `file_upload`) can read the file there; otherwise `download_id` is the download's only identifier. |
| `download_failed`    | `download_id`, `url`, `error?`               | When the download fails or is canceled, with the reason in `error` if the browser provides one.                                                                                                                                                                                                                              |

The API renders each entry as one line of text for Claude, in the order the entries appear. It adds the lines after the result's text, separated by a blank line, and before any Tab Context footer. Every kind of member result carries the lines, including `zoom` and tab-management results. A result with no `text` block gets them as a text block of its own. Each line gives the `download_id` and `url`, plus `path` and `size_bytes` (for `download_completed`) or `error` (for `download_failed`) when you send them. You don't need to describe the download in your own text. The API wraps `url`, `path`, and `error` in double quotes and escapes double quotes and backslashes inside them, so don't pre-escape these values.

For example, a click on "Download price list (CSV)" (`ref_8`) in the Pricing tab starts a download, so the click's result carries a `download_started` entry with `download_id` `"dl-1"` and the file's URL. The download finishes while a later `screenshot` call is running, so that result's `content` holds the image, a text block such as `Screenshot captured.`, and this `browser_state` block reporting the completion under the same `download_id`:

```python
{
  "type": "browser_state",
  "tabs": [
    { "tab_id": "tab-1", "title": "Documentation", "url": "https://example.com/docs" },
    {
      "tab_id": "tab-2",
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "active": true
    }
  ],
  "state_changes": [
    {
      "type": "download_completed",
      "download_id": "dl-1",
      "url": "https://example.com/pricing/price-list.csv",
      "path": "/home/user/downloads/price-list.csv",
      "size_bytes": 48213
    }
  ]
}
```



Claude sees `Screenshot captured.` followed by a blank line and a line like this:

```python
Download completed with download_id: dl-1, URL: "https://example.com/pricing/price-list.csv". Saved to "/home/user/downloads/price-list.csv". Size: 48213 bytes.
```



Download reports follow these rules:

- At most one entry per `download_id` in a single block, so a download that starts and finishes during the same call reports only `download_completed`.
- Never send `state_changes` on an `is_error: true` result; report a download event that occurred during a failed call on the next successful result.
- `state_changes` isn't an inventory of downloads in progress; report each event once.
- Each entry carries only the fields its `type` declares. `size_bytes` is a non-negative integer, `download_id` is non-empty, and `download_id`, `url`, `path`, and `error` are each at most 4,096 characters with no control characters or Unicode line or paragraph separators. The `url` comes from the remote server and often carries signed query-string credentials after redirects, so strip query parameters you don't want in Claude's context and sanitize it before reporting it or using it in a filesystem path.

## Handle errors

Report a failed call to Claude as an ordinary error result: `is_error: true`, text content that says what went wrong, `toolset_name` echoed, and no `browser_state` block.

### Return errors from your executor

Make error text specific, because Claude reads it and adapts: `Error: Navigation to https://example.com/status timed out after 30 seconds. The page may be unavailable.` gives Claude something to act on where a bare `Error: navigation failed` doesn't. Other common cases:

### Refused navigation scheme

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01LeUTyqkhRxBFq1QTG3pkwN",
  "toolset_name": "browser",
  "is_error": true,
  "content": "Error: Navigation refused. Only http and https URLs are allowed."
}
```



### Stale or unknown element reference

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
  "toolset_name": "browser",
  "is_error": true,
  "content": "Error: ref_3 is stale or not found on the current page. Re-read the page to get fresh references."
}
```



### Disabled or unimplemented member

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_013h2Q55HcNwVyapSpy2s5ZG",
  "toolset_name": "browser",
  "is_error": true,
  "content": "Error: javascript_exec is not enabled in this environment."
}
```



### Skipped after an earlier failure in the turn

When the `left_click` on `ref_3` from [Batch actions](#batch-actions) fails with the stale-reference error shown earlier, the `type` and `key` calls after it each get this result:

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01FkP8rTz6uYh2mNq4LsXw7v",
  "toolset_name": "browser",
  "is_error": true,
  "content": "Not executed: an earlier action in this turn failed."
}
```



### Request errors

The API validates the toolset entry and every member `tool_use` and `tool_result` block in the conversation. When one is malformed, the API returns an `invalid_request_error` before Claude runs. In the following table, the left column names what you sent.

| Request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Why it fails and what to do                                                                                                                                                                                                         |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| An option or combination the toolset entry doesn't accept, for example, a `name`, `strict: true`, `input_examples`, `defer_loading` on the entry itself, a `configs` key that isn't a member name, a field other than `enabled` or `defer_loading` in a member's `configs` value ([Configure the toolset](#configure-the-toolset)), enabled members whose `defer_loading` values differ ([Configure the toolset](#configure-the-toolset)), a `configs` that leaves no member enabled, a code execution caller in `allowed_callers`, the legacy `fine-grained-tool-streaming-2025-05-14` beta header on the request, a `tool_choice` of type `tool` naming `browser` or a member, or a second browser toolset entry or another tool named `browser` | These aren't supported on client toolsets. See [Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets) for each rule and its alternative.                                                              |
| A `tool_result` answering a member call without `"toolset_name": "browser"` or with a different value, or `toolset_name` on a result whose call wasn't a member call                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Echo `toolset_name` exactly on member results, and only on them.                                                                                                                                                                    |
| A member `tool_use` from an earlier turn with no matching `tool_result`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Answer every member call, including the ones you didn't run after a failure.                                                                                                                                                        |
| A content block other than `text`, `image`, or `browser_state` in a member result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Member results accept only those three block types.                                                                                                                                                                                 |
| A `browser_state` block that breaks a rule in [Track tabs with `browser_state`](#track-tabs-and-page-state), for example, one on an `is_error: true` result or on a result that doesn't answer a browser member call, more than one in a result, a non-empty `tabs` without exactly one `active: true` entry, a duplicate `tab_id`, an empty `state_changes` array, a `tab_opened` whose `tab_id` isn't in `tabs`, two state changes for one `download_id` or a state-change field its `type` doesn't declare ([Report downloads](#report-downloads)), or a field over its limits                                                                                                                                                                  | Fix the block. "Nothing to report" is expressed by omitting the block or the `state_changes` field, never by an empty value.                                                                                                        |
| A successful `new_tab`, `switch_tab`, `close_tab`, or `list_tabs` result whose `content` isn't exactly one `browser_state` block, or a `new_tab` result without exactly one `tab_opened` matching the active tab                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The API renders these results from the block and needs it in that exact shape; see [Tab management results](#tab-management-results).                                                                                               |
| An `image` in a result over your model's [image size limits](/docs/en/build-with-claude/vision#evaluate-image-size), or over the stricter per-image limit that applies once the request holds [more than 20 images](/docs/en/build-with-claude/vision#request-limits), counting screenshots and `zoom` images in earlier results                                                                                                                                                                                                                                                                                                                                                                                                                   | The API doesn't downscale toolset images. Resize screenshots before returning them ([Size screenshots to fit image limits](/docs/en/agents-and-tools/tool-use/computer-use-tool#handle-coordinate-scaling-for-higher-resolutions)). |
| A `model` that doesn't support `browser_toolset_20260801`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | See [Compatibility](#compatibility) for the supported models.                                                                                                                                                                       |

## Limitations

- **Platform availability:** Browser use is available on the Claude API and [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai).
- **Whole-input streaming only:** When you stream, each member's `input` arrives as one complete `input_json_delta` ([Client toolsets](/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets)).
- **Element references are best-effort:** Highly dynamic pages (virtualized lists, canvas-rendered interfaces, pages that re-render on scroll) might not expose stable references, and Claude falls back to screenshots and coordinate clicks there.
- **`read_console` and `read_network` depend on your browser automation:** They report only what it can capture, and only from the moment it attached to a tab.
- **General agent limitations apply:** Latency, vision accuracy, and prompt-injection risks carry over from computer use (see the computer use tool's [Limitations](/docs/en/agents-and-tools/tool-use/computer-use-tool#understand-computer-use-limitations)), and its guidance under [Optimize model performance with prompting](/docs/en/agents-and-tools/tool-use/computer-use-tool#optimize-model-performance-with-prompting), [Manage screenshot history](/docs/en/agents-and-tools/tool-use/computer-use-tool#manage-screenshot-history), and [Follow implementation best practices](/docs/en/agents-and-tools/tool-use/computer-use-tool#follow-implementation-best-practices) (action delays, action validation, and logging) applies to browser executors too.

## Pricing and data retention

Browser use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the browser use tool:

**Toolset definition overhead:** Declaring `browser_toolset_20260801` with its default members adds about 6,600 input tokens to a request (about 6,610 on Claude Fable 5, Claude Mythos 5, Claude Opus 5, and Claude Opus 4.8, and about 6,670 on Claude Sonnet 5), which covers the member tool definitions and the tool use system prompt. Enabling all four optional members adds about 880 tokens, and disabling members with `configs` reduces the count. The exact count for a request is reported in the response `usage`, and you can estimate it in advance with the [token counting endpoint](/docs/en/build-with-claude/token-counting).

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Vision pricing](/docs/en/build-with-claude/vision#evaluate-image-size))
- Text tool results returned to Claude, such as accessibility trees, page text, and console or network entries



If you also use the computer use tool, bash tool, text editor tool, or your own tools alongside browser use, those tools have their own token costs as documented on their respective pages.

The browser session, downloads, and uploaded files stay in your environment; the screenshots, page text, and tab state you return are part of your API request content and follow the standard retention policy, or your ZDR arrangement if you have one. The browser use tool is ZDR eligible; see [API and data retention](/docs/en/manage-claude/api-and-data-retention) for retention periods and eligibility across features.

## Next steps



[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)

Give Claude control of a full desktop when the task leaves the browser; its implementation guidance applies to browser executors too.



[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)

Format `tool_result` blocks, return images and errors, and continue the conversation.



[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)

Browse client toolsets and every other Anthropic-provided tool, with their versions and parameters.

## Compatibility

Supported models  
- Fable 5 and 5.1
- Mythos 5 and 5.1
- Opus 4.8, 5, and 5.5
- Sonnet 5

Supported platforms  
- Claude API
- Google Cloud
