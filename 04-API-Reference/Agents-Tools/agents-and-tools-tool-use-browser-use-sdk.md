---
title: "Browser and computer use with the SDK toolsets - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-sdk"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-10-08T06:24:45Z"
tags: ["api", "sdk"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fbrowser-use-sdk)

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

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Browser and computer use (SDK)](agents-and-tools-tool-use-browser-use-sdk.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

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

# Browser and computer use with the SDK toolsets

Copy page



Run the browser use tool or the computer use tool from the Python or TypeScript SDK. The SDK runs the loop and the checks you configure, and you supply the browser or the desktop.

Copy page



The Python and TypeScript SDKs include a class for the [browser use tool](agents-and-tools-tool-use-browser-use-tool.md) and a class for the [computer use tool](agents-and-tools-tool-use-computer-use-tool.md). You subclass one and write one method per member tool, such as `navigate` or `left_click`, against your own browser or desktop automation. The SDK routes each call, runs the policies you pass, asks your approval callback, and builds each `tool_result`.

Most of this page uses the browser class. [Computer toolset](#computer-toolset) covers the computer class and what differs for it.

The SDK doesn't include a browser, a desktop, a ready-made driver, or a URL policy. The [minimal CDP example](https://github.com/anthropics/claude-quickstarts/tree/main/browser-toolset) is in the claude-quickstarts repository, in Python and TypeScript. It controls Chromium through the Chrome DevTools Protocol (CDP), and it isn't production code.



The browser toolset class is in beta and available in the [Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/browser-toolset.md) and the [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/browser-toolset.md). The computer toolset class is in beta in the same SDKs, which have a [Python computer toolset guide](https://github.com/anthropics/anthropic-sdk-python/blob/main/computer-toolset.md) and a [TypeScript computer toolset guide](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/computer-toolset.md). Each class runs with the [tool runner](agents-and-tools-tool-use-tool-runner.md) or in a loop you write.

## Partner integrations

Browser Use, Browserbase, Daytona, and E2B publish their own integrations with the SDK toolsets.

### Browser Use

- [Browser Use docs](https://docs.browser-use.com/open-source/customize/integrations/toolsets-for-claude)
- [Browser Use quickstart](https://github.com/browser-use/browser-use/tree/main/examples/integrations/toolsets-for-claude)

### Browserbase

- [Browserbase Stagehand docs](https://docs.stagehand.dev/v4/integrations/agent-frameworks/claude-cua-toolset-quickstart)
- [Browserbase toolset](https://github.com/browserbase/claude-cua-toolset)

### Daytona

- [Daytona guide](https://www.daytona.io/docs/en/guides/claude/claude-draws-daytona-sandbox/)

### E2B

- [E2B docs](https://docs.e2b.dev/agents/claude-toolsets)
- [E2B example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/anthropic-computer-use-orangehrm-js)

## Quick start

A driver is your subclass of `BetaAbstractBrowserToolset20260801`. This one implements `navigate`, `screenshot`, and `left_click`, plus `_browser_state`, the state report that every driver needs. In the example, `backend` stands for your own wrapper around a browser automation library, such as Playwright. The URL policy is an example. [Write a URL policy](#write-a-url-policy) explains it.

Python

TypeScript



```python
import re
from urllib.parse import urlsplit

from anthropic import Anthropic
from anthropic.tools import ToolError
from anthropic.tools.browser import (
    BetaAbstractBrowserToolset20260801,
    BetaBrowserNavigateResult,
    BetaBrowserState,
    BetaScreenshotResult,
    BetaToolsetCallContext,
    BetaURLContext,
)
from anthropic.types.beta import (
    BetaBrowserLeftClickInput,
    BetaBrowserNavigateInput,
    BetaBrowserScreenshotInput,
    BetaBrowserStateTabEntryParam,
)


class MyBrowser(BetaAbstractBrowserToolset20260801):
    def __init__(self, backend, **options):
        super().__init__(**options)
        self.backend = backend

    def _browser_state(self, context: BetaToolsetCallContext) -> BetaBrowserState:
        return BetaBrowserState(
            tabs=[
                BetaBrowserStateTabEntryParam(
                    tab_id=tab.id,
                    title=tab.title,
                    url=tab.url,
                    active=tab.id == self.backend.active,
                )
                for tab in self.backend.tabs()
            ],
            state_changes=self.backend.drain_changes(),
        )

    def navigate(
        self, context: BetaToolsetCallContext, input: BetaBrowserNavigateInput
    ) -> BetaBrowserNavigateResult:
        # input.url is "back", "forward", "reload", or a URL that your URL policy
        # allowed, as Claude wrote it. Like is_allowed, backend.goto adds https://
        # to a URL that doesn't start with a scheme.
        page = self.backend.goto(input.url, input.tab_id)
        return BetaBrowserNavigateResult(
            url=page.url, status=page.status, title=page.title
        )

    def screenshot(
        self, context: BetaToolsetCallContext, input: BetaBrowserScreenshotInput
    ) -> BetaScreenshotResult:
        data = self.backend.png_base64(input.tab_id)
        return BetaScreenshotResult(data=data, media_type="image/png")

    def left_click(
        self, context: BetaToolsetCallContext, input: BetaBrowserLeftClickInput
    ) -> None:
        # Nothing to return: Claude reads "Clicked."
        self.backend.click(input.target, input.tab_id)

    def close(self) -> None:
        super().close()  # first, so no call is still using the browser when it closes
        if not self.backend.closed:
            self.backend.close()


ALLOWED_HOSTS = ("example.com", "iana.org")
SCHEME_PREFIX = re.compile(r"[a-z][a-z0-9+.-]*:", re.IGNORECASE)


def is_allowed(url: str) -> bool:
    # An example, not a production policy. See "Write a URL policy".
    if url.lower() == "about:blank":
        return True
    with_scheme = url if SCHEME_PREFIX.match(url) else f"https://{url}"
    # A browser reads "\" as "/" in a web URL.
    try:
        parts = urlsplit(with_scheme.replace("\\", "/"))
    except ValueError:
        return False
    host = parts.hostname or ""
    listed = any(host == name or host.endswith(f".{name}") for name in ALLOWED_HOSTS)
    return parts.scheme in ("http", "https") and listed


def url_policy(context: BetaURLContext, url: str) -> None:
    if not is_allowed(url):
        raise ToolError(f"blocked: {url} is not on an allowed host")


client = Anthropic()
with MyBrowser(backend, url_policy=url_policy) as browser:
    runner = client.beta.messages.tool_runner(
        model="claude-opus-5-5",
        max_tokens=1024,
        tools=[browser],
        messages=[
            {
                "role": "user",
                "content": "Open example.com and tell me the page heading.",
            }
        ],
        stream=True,
        run_tools_eagerly=True,  # so a call can start before the response ends
    )
    for stream in runner:
        print(stream.get_final_message())
```

Pass the driver instance itself as the `tools` entry. A member you don't implement is sent to the API as disabled. If Claude calls it anyway, the SDK returns an error, and the run continues. Overriding `execute` changes which members are sent as disabled ([Add before and after hooks](#add-before-and-after-hooks)). The runner never closes the toolset, so one instance can serve several runs. Close it when you're done.

The example turns on early start. See [Start calls while the response streams](#start-calls-while-the-response-streams).



Do these two things before you run a driver against anything but a throwaway browser:

- [Write a URL policy](#write-a-url-policy), and block private network ranges and the cloud metadata address `169.254.169.254` with [egress rules on the container](#put-egress-policy-on-the-container). Without a URL policy, the SDK checks no URL. Egress rules outside the container don't see loopback, so a page can still reach anything listening in the browser's container.
- Use a browser profile that isn't signed in to any account whose data or actions you wouldn't hand to Claude. See [Isolate the browser host](#isolate-the-browser-host).

## Customize a driver

### Enable or disable members

`configs` takes the per-member settings described under [Configure the toolset](agents-and-tools-tool-use-browser-use-tool.md#configure-the-toolset). List only the members you change:

Python

TypeScript



```python
# A MyBrowser that also implements read_console
browser = MyBrowser(
    backend, configs={"read_console": {"enabled": True}, "navigate": {"enabled": False}}
)
```

The SDK refuses a call to a disabled member before your code runs. Enabling a member your class doesn't implement is a configuration error, unless the class overrides `execute`.

### Add before and after hooks

Override `execute` and call the parent's `execute`. Code before that call runs after the [URL policy](#write-a-url-policy), the [file policy](#confine-uploads-and-downloads), and [`confirm`](#gate-consequential-members), and it can change the input. The SDK doesn't check the changed input again. Code after the call receives the result, and it can change the result. Raise `ToolError` (throw it in TypeScript) to refuse the call.

Overriding `execute` changes which members Claude is offered. The SDK counts every member as implemented, so Claude is offered every member that's on by default. The quick start's `MyBrowser` serves three members, so the following `TracedBrowser` offers Claude members it can't serve. Turn those members off with `configs` before you use it.

Python

TypeScript



```python
import time


class TracedBrowser(MyBrowser):
    def execute(self, context, name, input):
        started = time.monotonic()
        result = super().execute(context, name, input)
        elapsed_ms = (time.monotonic() - started) * 1000
        call_id = context.tool_use.id if context.tool_use else "-"
        log.info("%s %s %.0fms", call_id, name, elapsed_ms)
        return redact(result) if name == "get_page_text" else result
```

## Implement a driver

Override the members your browser supports. Each member receives the call context and the member's input as a typed object, such as `BetaBrowserNavigateInput`. The input types come from `anthropic.types.beta`. [Member tools](agents-and-tools-tool-use-browser-use-tool.md#member-tools) lists each input's fields.

In TypeScript, write members as methods, not arrow-function fields, because the SDK finds them on the prototype. Spell the `type` member `type_` in TypeScript. In Python, it's `type`.

### Return results

What a member returns determines what Claude reads. A successful result ends with a `browser_state` block built from your state report. An error result carries no block.

| Member                                                                                  | Returns                                                                                              | Claude reads                                                                                |
|:----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| `screenshot`, `zoom`                                                                    | `BetaScreenshotResult`                                                                               | One image block                                                                             |
| `navigate`                                                                              | `BetaBrowserNavigateResult`                                                                          | `Navigated to {url} — {title} (HTTP {status})`                                              |
| `new_tab`, `switch_tab`, `list_tabs`, `close_tab`                                       | A tab entry (`new_tab`, `switch_tab`), a list of tab entries (`list_tabs`), or nothing (`close_tab`) | The `browser_state` block alone                                                             |
| `read_page`, `get_page_text`, `find`, `read_console`, `read_network`, `javascript_exec` | A string                                                                                             | The string, or `(empty)` for an empty string                                                |
| Every other member                                                                      | Nothing, or one line of text                                                                         | A short confirmation, such as `Clicked.`, then the returned line in a text block of its own |

### Report browser state

The SDK calls `_browser_state` after each call that returns a result, including refused and failed calls. Return every open tab, and what changed since the last report:

- Opened tabs and download events.
- A `BetaNavigationRefused` for each navigation your [request hook](#intercept-requests-in-the-driver) blocked.
- A `BetaDialogDismissed` for each native dialog your driver dismissed.

Put all of these in `state_changes`. In Python, `BetaNavigationRefused()` and `BetaDialogDismissed(kind=..., message=...)` come from `anthropic.tools.browser`. In TypeScript, they're `{ type: "navigation_refused" }` and `{ type: "dialog_dismissed", kind, message }`.

The last two aren't API state changes. The SDK reports them to Claude as text outside the `browser_state` block: one line for all refused navigations, which doesn't name a URL, and a line for each of the first three dismissed dialogs, then a count of any others.

When any tab is open, exactly one must be active. Every member that takes a `tab_id` must act on the tab it names. The API's limits on the report are listed under [Track tabs with `browser_state`](agents-and-tools-tool-use-browser-use-tool.md#track-tabs-and-page-state).

Claude reads each tab's URL, each download's URL, and the URL that your `navigate` returns, as your driver wrote them. The SDK doesn't parse these URLs. It turns line breaks and other control characters into spaces, trims the ends, and cuts each URL at 4,096 characters. So a `data:` URL's contents, a `file:` URL's path, and a user name or password in a URL all reach Claude.

### Handle errors

| Raised by a member or the SDK | Claude reads                                                                         | The run   |
|:------------------------------|:-------------------------------------------------------------------------------------|:----------|
| `ToolError`                   | Its message, as an error result                                                      | Continues |
| `ToolsetUsageError`           | Nothing                                                                              | Stops     |
| Any other exception           | `ClassName: message` in Python or `Error: message` in TypeScript, as an error result | Continues |

The SDK raises `ToolsetUsageError` for a configuration error, a misuse of the SDK during a call, or a call after `close`. It also raises one when `_browser_state` raises any exception, even a `ToolError`. The tool runner and `tool_result` don't catch it, so it reaches their caller.

The SDK doesn't hide local paths in a member's error text, in the line an action such as `left_click` returns, in a failed download's error, or in a dismissed dialog's message.

A `ToolError` from your URL policy, file policy, or `confirm` callable reaches Claude as written, so leave local paths out of its text. Catch exceptions in your members, and raise `ToolError` (throw it in TypeScript) with your own text.

### Start calls while the response streams

By default, the tool runner runs a turn's calls after Claude's response ends. With early start, it can start a browser or computer call while the response is still streaming.

To turn it on, pass `stream=True` and `run_tools_eagerly=True` to the tool runner, as the quick start does. With `stream`, each pass through your loop over the runner gives you a stream instead of a message.

Early start changes when a call can start, not how the toolset runs it:

- **The checks still run first:** The SDK calls your URL policy, your file policy, and `confirm` before a call runs. With early start, it can call `confirm` while the response is still streaming.
- **Calls still run one at a time:** A toolset runs its calls in the order Claude wrote them. A failed call still stops that toolset's later calls in the turn.
- **A call that has started can't be taken back:** If the response is then cut off, for example at `max_tokens`, or your loop stops early, the action still happens, and Claude never reads its result.

### Run without the tool runner

Pass the instance in `tools` (`browser.toJSON()` in TypeScript), and answer each member call with `tool_result`. The browser use tool requires you to stop at the first failed call ([Batch actions](agents-and-tools-tool-use-browser-use-tool.md#batch-actions)). After a failed call, this loop answers the turn's later calls without running them:

Python

TypeScript



```python
from anthropic.types.beta import BetaMessageParam, BetaToolResultBlockParam

NOT_EXECUTED = "Not executed: an earlier action in this turn failed."
MAX_TURNS = 10

with MyBrowser(backend, url_policy=url_policy) as browser:
    messages: list[BetaMessageParam] = [{"role": "user", "content": "Open example.com"}]
    for _ in range(MAX_TURNS):
        response = client.beta.messages.create(
            model="claude-opus-5-5",
            max_tokens=1024,
            tools=[browser],
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})
        calls = [
            block
            for block in response.content
            if block.type == "tool_use" and block.toolset_name == browser.toolset_name
        ]
        if not calls:
            break
        results: list[BetaToolResultBlockParam] = []
        failed = False
        for call in calls:
            if failed:
                # After a failed call, the rest of the turn is answered, not run.
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": call.id,
                        "toolset_name": call.toolset_name,
                        "content": NOT_EXECUTED,
                        "is_error": True,
                    }
                )
                continue
            result = browser.tool_result(call)
            failed = bool(result.get("is_error"))
            results.append(result)
        messages.append({"role": "user", "content": results})
```

Each answer to a skipped call carries `is_error`, the call's `toolset_name`, and the exact text that [Batch actions](agents-and-tools-tool-use-browser-use-tool.md#batch-actions) requires. The tool runner sends the same answer.

## Run the toolset safely

Claude's next action depends on the pages it reads. A page, or text injected into one, can try to reach internal services or pull files off the host. It can also try to trigger actions with real effects. Before you run a driver against anything but a throwaway browser, take these six steps:

1.  [Write a URL policy](#write-a-url-policy) that refuses every `navigate` URL the task doesn't need.
2.  [Intercept requests in the driver](#intercept-requests-in-the-driver), and check each request with the same rules.
3.  [Put egress policy on the container](#put-egress-policy-on-the-container), so the network blocks what the driver can't see.
4.  [Confine uploads and downloads](#confine-uploads-and-downloads), or leave uploads off.
5.  [Gate consequential members](#gate-consequential-members) with `confirm`.
6.  [Isolate the browser host](#isolate-the-browser-host) in a dedicated container or VM for each session.

The SDK applies steps 1, 4, and 5 through the policies and the callable you pass. Steps 2, 3, and 6 are up to your driver and your deployment. The precautions under [Security considerations](agents-and-tools-tool-use-browser-use-tool.md#security-considerations) apply as well.



Anthropic's prompt-injection classifiers, described under [Security considerations](agents-and-tools-tool-use-browser-use-tool.md#security-considerations), don't currently run on browser toolset requests sent through Amazon Bedrock.

### Write a URL policy



Without a URL policy, the SDK checks no URL, and the API doesn't filter the URLs Claude opens. Even with a policy, a link Claude clicks or a redirect can take the browser to loopback (`localhost`, `127.0.0.1`), to link-local addresses such as the cloud metadata address `169.254.169.254`, and to private network ranges. [Egress rules on the container](#put-egress-policy-on-the-container) can block the link-local and private addresses. Rules enforced outside the container can't block loopback.

The SDK doesn't check a URL's scheme, so your driver must refuse every scheme it doesn't mean to open, such as `javascript:`, `view-source:`, `data:`, and `file:`. Most drivers need only `http` and `https`. The example policy below allows only `http` and `https` URLs, plus `about:blank`.

A `file:` URL lets Claude read files on the browser host. A `javascript:` URL runs script in the current page, even when `javascript_exec` is off. Egress rules don't stop either one.

A URL policy is a function that you pass as `url_policy`. You write the policy, and you're responsible for making it ready for production. Before your `navigate` runs, the SDK calls the policy with the call's context and the URL as Claude wrote it.

Return nothing to allow the URL. To refuse it, raise `ToolError` (throw it in TypeScript). Claude reads the error's message, and `navigate` doesn't run. The policy checks only the URL in each `navigate` call. It isn't a network control.

This is the policy from the quick start. It allows `about:blank`, plus two sites and their subdomains over `http` and `https`:

Python

TypeScript



```python
import re
from urllib.parse import urlsplit

from anthropic.tools import ToolError
from anthropic.tools.browser import BetaURLContext

ALLOWED_HOSTS = ("example.com", "iana.org")
SCHEME_PREFIX = re.compile(r"[a-z][a-z0-9+.-]*:", re.IGNORECASE)


def is_allowed(url: str) -> bool:
    # An example, not a production policy.
    if url.lower() == "about:blank":
        return True
    with_scheme = url if SCHEME_PREFIX.match(url) else f"https://{url}"
    # A browser reads "\" as "/" in a web URL.
    try:
        parts = urlsplit(with_scheme.replace("\\", "/"))
    except ValueError:
        return False
    host = parts.hostname or ""
    listed = any(host == name or host.endswith(f".{name}") for name in ALLOWED_HOSTS)
    return parts.scheme in ("http", "https") and listed


def url_policy(context: BetaURLContext, url: str) -> None:
    if not is_allowed(url):
        raise ToolError(f"blocked: {url} is not on an allowed host")


browser = MyBrowser(backend, url_policy=url_policy)
```

The SDK calls the policy only for `navigate`, and not for `"back"`, `"forward"`, or `"reload"`. Claude can leave out the scheme, as in `example.com`, so before it reads the host, the example adds `https://` to a URL that doesn't start with a scheme. Your `navigate` gets the URL as Claude wrote it. Add the scheme there with the same test, so that the browser opens the URL your policy checked.

The example isn't production grade. A production policy needs much more, in areas such as these:

- Links Claude clicks, forms it submits, redirects, and the requests a page makes on its own. Only your driver sees them. See [Intercept requests in the driver](#intercept-requests-in-the-driver).
- Hostnames and URLs that come from page content, which an attacker can choose.
- Parsing each URL the way the browser does, not finding the hostname with a plain string split.
- URL schemes. The SDK doesn't check them, so refuse every scheme your driver doesn't mean to open.
- Egress rules on the container, for what no URL check can see. See [Put egress policy on the container](#put-egress-policy-on-the-container).

If you pass `url_policy=None`, the SDK refuses every `navigate` to a URL, so a `None` read from your configuration can't leave URLs unchecked by accident. In TypeScript, `undefined` leaves the option unset, the same as not passing it.

### Intercept requests in the driver

The URL policy judges only the URL in a `navigate` call. A link Claude clicks, a form it submits, a redirect, or an image or script on an allowed page can still reach a host the policy would refuse. Use [egress rules](#put-egress-policy-on-the-container) to block those hosts.

A driver with request interception can also check those requests in its request hook, the function your automation library calls before each request. Call the function that your policy uses, so that you write the rules once:

Python

TypeScript



```python
class MyBrowser(BetaAbstractBrowserToolset20260801):
    ...

    # Registered on a Playwright browser context with context.route("**/*", self._guard)
    def _guard(self, route):
        # is_allowed is the function from "Write a URL policy"
        if not is_allowed(route.request.url):
            return route.abort("blockedbyclient")
        route.continue_()
```

A request hook like this one doesn't see WebSocket handshakes, service-worker requests, or redirect hops. Block service workers. Check WebSocket handshakes and redirect hops with a hook that sees them. The example policy refuses `ws://` and `wss://` URLs, so change `ws://` to `http://` and `wss://` to `https://` before you pass a WebSocket URL to `is_allowed`.

### Put egress policy on the container

Interception can't see every request the browser makes, and the URL policy doesn't see where a name resolves. An egress policy that the container's network enforces covers both:

- Block link-local and private address ranges in IPv4 and IPv6. That includes the cloud metadata address `169.254.169.254`.
- Allow outbound connections only to the hosts the task needs. If your rules match IP addresses, resolve the hostnames you allow when the container starts.
- Allow DNS only to the container's resolver.

Rules enforced outside the browser's container, such as a Kubernetes NetworkPolicy or a cloud firewall, don't see loopback inside it. With only those rules, a page can reach anything listening there, including a DevTools port, which shows a list of the browser's open tabs and the address that controls each one.

### Confine uploads and downloads

`file_upload` is off by default. With no `file_policy`, the SDK refuses every upload that names a path or a [document ID](agents-and-tools-tool-use-browser-use-tool.md#upload-files). To enable uploads, pass a `BetaLocalFilePolicy` with one upload directory that holds only the task's files:

Python

TypeScript



```python
from anthropic.tools.browser import BetaLocalFilePolicy

# A MyBrowser that also implements file_upload
browser = MyBrowser(
    backend,
    configs={"file_upload": {"enabled": True}},
    confirm=make_confirm(),  # required for file_upload; see Gate consequential members
    url_policy=url_policy,
    file_policy=BetaLocalFilePolicy(
        upload_roots=["/task/uploads"],
        download_dir="/task/downloads",
        expose_download_paths=False,
    ),
)
```

The SDK resolves each upload path, following symlinks, and refuses any path outside the upload roots. The file policy raises a configuration error for a download directory that is an upload root, is inside one, or contains one. That check can miss a symlink, so don't let one make the download directory the same as an upload root, or put one inside the other. The SDK includes a download's `path` in the state report only when `expose_download_paths` is true and the file is inside the download directory.

The shipped file policy checks paths on the filesystem of the process that runs the SDK. It protects only a browser that shares that filesystem. For a remote browser, follow [Remote and hosted browsers](#remote-and-hosted-browsers) instead.

Set up downloads this way:

- Create the download directory yourself with mode `0700`, and mount it `noexec,nosuid,nodev`.
- Keep the directory out of reach of other tools that Claude can call, such as a shell or a file tool.
- In a `download_failed` state change, write `error` as a fixed phrase. An exception's text can contain the path or the URL.
- Don't read a downloaded file into the conversation, or run it, until a person decides to.

### Gate consequential members

`javascript_exec` and `file_upload` are off by default. If you enable either one without a `confirm` callable, the constructor raises a configuration error. With a `confirm` callable, the SDK calls it before every call that's about to run. Without one, nothing is asked. In TypeScript, `confirm: null` doesn't raise the configuration error, and the SDK refuses every call to any member.

Return `True` to run the call, or `False` to refuse it. When your callable asks a person, show them the member, the page's URL, and the call's input. First, escape every character outside printable ASCII in the URL and the input, because both can carry text from the page.

This example asks about the two gated members through your own `ask_user` function, and approves the rest:

Python

TypeScript



```python
import json
from collections.abc import Callable
from urllib.parse import urlsplit

from anthropic.tools.browser import BetaConfirmContext

GATED = {"javascript_exec", "file_upload"}


def shown(value: object) -> str:
    """A value as JSON, with every character outside printable ASCII escaped."""
    return json.dumps(value, ensure_ascii=True, indent=2)


def make_confirm() -> Callable[[BetaConfirmContext], bool]:
    granted: set[tuple[str, str, str]] = set()

    def confirm(context: BetaConfirmContext) -> bool:
        name = context.member
        if name not in GATED:
            return True
        detail = shown(context.input.to_dict())
        page = context.tab_url
        where = shown(page) if page else "a tab with no URL"
        question = f"Allow {name} on {where}?\n{detail}"
        if page is None or urlsplit(page).scheme not in ("http", "https"):
            return ask_user(question)  # no web origin: ask every time
        # An approval covers only this exact input on this page.
        key = (name, page, detail)
        if key not in granted and ask_user(question):
            granted.add(key)
        return key in granted

    return confirm


# A MyBrowser that also implements javascript_exec and file_upload
# file_upload also needs the file_policy from "Confine uploads and downloads"
browser = MyBrowser(
    backend,
    configs={"javascript_exec": {"enabled": True}, "file_upload": {"enabled": True}},
    confirm=make_confirm(),
    url_policy=url_policy,
)
```

Each call to `make_confirm()` returns a callable with no approvals. Call it once for each toolset, and give each user their own toolset.

An approval covers the page as the last state report showed it, and the page can change before the call runs. Purchases, sent messages, and accepted terms happen through ordinary members such as `left_click` and `type`, so `confirm` can't pick them out by name. To have a person approve them, ask about those members too.

Don't enable `javascript_exec` unless [egress rules](#put-egress-policy-on-the-container) limit the browser's outbound connections to the hosts the task needs. A script can send the page's content to any address that the browser can reach.

A `javascript:` URL in a `navigate` call also runs script in the current page, even when `javascript_exec` is off. `confirm` sees that call as a `navigate`, so the example's `confirm` callable would approve it. Your driver must refuse `javascript:` URLs. In the example, the [URL policy](#write-a-url-policy) refuses them before `confirm` runs.

### Isolate the browser host

Run the browser in a dedicated, minimal-privilege container or VM for each session:

- Run as a non-root user, with a read-only root filesystem where the browser allows it.
- Mount nothing from the host beyond the upload and download directories you configured, if any.
- Keep credentials out of the environment, and start from a fresh browser profile.
- Share no filesystem with other tools Claude can call.



The browser profile must not be signed in to any account whose data or actions you wouldn't hand to Claude. `javascript_exec` runs with the page's own authority: its cookies, its storage, and its signed-in sessions.

Run the code that calls the API outside the browser's container, because that code holds your API key and the conversation. The tool runner and `tool_result` both run the toolset in that code's process, so the browser doesn't share the toolset's filesystem. Treat the browser as remote: [Remote and hosted browsers](#remote-and-hosted-browsers) applies.

Treat everything a page returns as untrusted, including page text, screenshots, console and network entries, tab titles, and download names.

### Remote and hosted browsers

Some browsers don't share a filesystem with the process that runs the SDK. Examples are a browser in another container, one you reach at a DevTools URL, and one from a hosted browser service. With these, the URL policy, request interception, and `confirm` still run in your process.

With a hosted browser, the provider controls egress and host isolation. Your own egress policy doesn't apply there, so the driver's request hook is your only check on the browser's requests. Find out what the browser's network can reach.

The shipped path checks don't protect a remote browser. `BetaLocalFilePolicy` checks paths on the filesystem of the process that runs the SDK, and the browser reads and writes its own filesystem.

The SDK can't detect that a browser is remote. So for a remote browser, keep `file_upload` off unless your driver checks upload paths where the browser runs, with a `BetaFilePolicy` of its own. A `BetaFilePolicy` vets each upload's paths and document IDs, and decides whether Claude sees a download's path.

Have a remote browser refuse downloads, unless its own host has the download setup from [Confine uploads and downloads](#confine-uploads-and-downloads).

Keep the provider's API key and the session's connection URL, which can contain a key, out of logs, tool results, and error text. If the provider records sessions, the recording is another copy of everything Claude saw and typed, and the provider's retention terms apply to it.

## Computer toolset

`BetaAbstractComputerToolset20260801` is the class for the [computer use tool](agents-and-tools-tool-use-computer-use-tool.md). You subclass it and write one method per tool, such as `screenshot` or `left_click`, against your own desktop automation. Your subclass is the driver. The SDK doesn't include a desktop or a ready-made driver. The [minimal VNC example](https://github.com/anthropics/claude-quickstarts/tree/main/computer-toolset) is in the claude-quickstarts repository, in Python and TypeScript. It controls a desktop over VNC, and it isn't production code.

The class takes `configs`, `confirm`, and `tool_configs`, and you pass them as you do for the browser class. [Customize a driver](#customize-a-driver), [Handle errors](#handle-errors), [Start calls while the response streams](#start-calls-while-the-response-streams), and [Run without the tool runner](#run-without-the-tool-runner) apply to it too, with these differences:

- **Browser-only options:** The class has no [URL policy](#write-a-url-policy), no [file policy](#confine-uploads-and-downloads), and no [state report](#report-browser-state).
- **`configs`:** Every tool you implement is on by default. The per-tool settings are listed under [Tool parameters](agents-and-tools-tool-use-computer-use-tool.md#tool-parameters).
- **`confirm`:** If your class implements `type`, `key`, or `hold_key`, the constructor raises a configuration error unless you pass a `confirm` callable or turn those tools off with `configs`. A class that overrides `execute` counts as implementing all three.
- **Skipped calls:** After a failed computer call, the tool runner answers the turn's later computer calls with `Not executed: an earlier computer action in this turn failed.` Browser calls get a different text. In a loop you write, answer the skipped computer calls with that exact text ([Batch actions](agents-and-tools-tool-use-computer-use-tool.md#batch-actions)).
- **`execute`:** In TypeScript, an `execute` override types `name` as `BetaComputerMemberName` and `input` as `BetaComputerMemberInput`. Both come from `@anthropic-ai/sdk/resources/beta`.
- **Error text:** The SDK doesn't hide local paths in a computer tool's error text or in the text a tool returns. Claude reads both, cut at 4,096 characters. Catch exceptions in your tools, and raise `ToolError` (throw it in TypeScript) with your own text.

### Write a desktop driver

This driver implements five of the 17 tools listed under [Available actions](agents-and-tools-tool-use-computer-use-tool.md#available-actions). A tool you don't implement is sent to the API as disabled, as [Quick start](#quick-start) explains. In the example, `display` stands for your own wrapper around whatever controls the desktop, such as a VNC client or `xdotool`, and `ask_user` stands for your own function that asks a person.

Python

TypeScript



```python
from anthropic import Anthropic
from anthropic.tools.computer import (
    BetaAbstractComputerToolset20260801,
    BetaComputerCursorPositionResult,
    BetaScreenshotResult,
    BetaToolsetCallContext,
)
from anthropic.types.beta import (
    BetaComputerCursorPositionInput,
    BetaComputerKeyInput,
    BetaComputerLeftClickInput,
    BetaComputerScreenshotInput,
    BetaComputerTypeInput,
)


class MyDesktop(BetaAbstractComputerToolset20260801):
    def __init__(self, display, **options):
        super().__init__(**options)
        self.display = display

    def screenshot(
        self, context: BetaToolsetCallContext, input: BetaComputerScreenshotInput
    ) -> BetaScreenshotResult:
        # Claude's coordinates are pixel positions in this image.
        data = self.display.png_base64()
        return BetaScreenshotResult(data=data, media_type="image/png")

    def cursor_position(
        self, context: BetaToolsetCallContext, input: BetaComputerCursorPositionInput
    ) -> BetaComputerCursorPositionResult:
        x, y = self.display.cursor()
        return BetaComputerCursorPositionResult(x=x, y=y)

    def left_click(
        self, context: BetaToolsetCallContext, input: BetaComputerLeftClickInput
    ) -> None:
        # input.coordinate is [x, y], or None to click at the cursor. input.text is a
        # modifier to hold, such as "shift". Nothing to return: Claude reads "Clicked."
        self.display.click(input.coordinate, input.text)

    def type(
        self, context: BetaToolsetCallContext, input: BetaComputerTypeInput
    ) -> None:
        self.display.type(input.text)

    def key(self, context: BetaToolsetCallContext, input: BetaComputerKeyInput) -> None:
        self.display.press(input.text, input.repeat or 1)

    def close(self) -> None:
        super().close()  # first, so no call is still using the desktop when it closes
        self.display.close()


client = Anthropic()
with MyDesktop(
    display,
    # required for type and key; see Run the computer toolset safely
    confirm=lambda context: ask_user(f'Allow the "{context.member}" tool?'),
) as desktop:
    runner = client.beta.messages.tool_runner(
        model="claude-opus-5-5",
        max_tokens=1024,
        tools=[desktop],
        messages=[
            {"role": "user", "content": "Open the calculator and compute 17 * 23."}
        ],
    )
    for message in runner:
        print(message)
```



The `confirm` in this example asks a person before every call the driver runs. Before you run the driver against anything but a throwaway machine, read [Run the computer toolset safely](#run-the-computer-toolset-safely).

Four tools have no input fields: `screenshot`, `cursor_position`, `left_mouse_down`, and `left_mouse_up`. Every input type, including theirs, comes from `anthropic.types.beta`.

In TypeScript, write tools as methods, not arrow-function fields. [Implement a driver](#implement-a-driver) gives the reason.

### Scale coordinates and size images

Every point Claude sends is a pixel position in the screenshots you return: each `coordinate` and `start_coordinate`, and both corners of a `zoom` `region`. The SDK passes them to your tools unchanged.

If your screenshots are a different size from the display, convert in both directions in your driver: Claude's points to display pixels, and the cursor position you report to screenshot pixels. Keep the screenshot size the same for the whole session, and give it the display's aspect ratio:

Python

TypeScript



```python
from anthropic.tools import ToolError

SCREENSHOT_SIZE = (1280, 720)  # the size of every full screenshot the driver returns
DISPLAY_SIZE = (2560, 1440)


def to_display(coordinate: list[int]) -> tuple[int, int]:
    x, y = coordinate
    width, height = SCREENSHOT_SIZE
    if not (0 <= x < width and 0 <= y < height):
        # Refuse the point. Moving it into range would click where Claude didn't choose.
        raise ToolError(f"[{x}, {y}] is outside the {width}x{height} screenshot")
    return x * DISPLAY_SIZE[0] // width, y * DISPLAY_SIZE[1] // height


def to_screenshot(x: int, y: int) -> tuple[int, int]:
    width, height = DISPLAY_SIZE
    return x * SCREENSHOT_SIZE[0] // width, y * SCREENSHOT_SIZE[1] // height


to_display([640, 360])  # (1280, 720)
```

Call `to_display` on each `coordinate` and `start_coordinate` before you act on it, and `to_screenshot` on the position that `cursor_position` reports. A click or scroll with no `coordinate` acts at the cursor, so it has nothing to convert. Scale a `zoom` `region` by the same factor. A `zoom` image doesn't change this: the next points Claude sends are still pixel positions in the full screenshot.

The SDK never reads or resizes an image. The API rejects an image over the model's limits, which ends the run. Scale each screenshot and `zoom` image in the driver. See [Size screenshots to fit image limits](agents-and-tools-tool-use-computer-use-tool.md#handle-coordinate-scaling-for-higher-resolutions). On a long run, one request can hold more than 20 images, and the API then holds each one to a stricter limit. See [Manage screenshot history](agents-and-tools-tool-use-computer-use-tool.md#manage-screenshot-history).

### Input checks and results

Don't rely on the SDK to check a call's input. Have your driver check the fields it uses and refuse a call it can't run: raise `ToolError` (throw it in TypeScript). Claude reads the message and can send a corrected call.

Neither SDK limits a `duration`, a `repeat` count, or a `scroll_amount`. Step 4 under [Run the computer toolset safely](#run-the-computer-toolset-safely) covers them.

What a tool returns determines what Claude reads:

| Tool                 | Returns                            | Claude reads                                                                                |
|:---------------------|:-----------------------------------|:--------------------------------------------------------------------------------------------|
| `screenshot`, `zoom` | `BetaScreenshotResult`             | One image block                                                                             |
| `cursor_position`    | `BetaComputerCursorPositionResult` | `X={x},Y={y}`                                                                               |
| Every other tool     | Nothing, or one line of text       | A short confirmation, such as `Clicked.`, then the returned line in a text block of its own |

### Run the computer toolset safely

What's on the screen steers Claude's next action. A page or a notification can try to make Claude type into the wrong window, or trigger an action with real effects.



A driver that implements `type`, `key`, or `hold_key` needs a `confirm` callable. Without one, the constructor raises a configuration error, unless `configs` turns those tools off. The SDK itself asks no one: it runs every call that your `confirm` approves, and with no `confirm` it runs every call, including every click. Every computer tool you implement is on by default.

Before you run a driver against anything but a throwaway machine, take these five steps:

1.  Isolate the desktop. Run it in a dedicated, minimal-privilege container or VM for each session, with no credentials and no host mounts. Install only the applications the task needs. Run the code that calls the API outside it.
2.  Gate actions that have real effects with `confirm`. A purchase or a sent message is an ordinary `left_click`, `type`, or `key`, and `confirm` receives the tool and its input, not the screen. So choose which tools need approval based on the applications Claude can reach on the desktop.
3.  Keep terminals, run dialogs, and launchers off the desktop unless the task needs one. When one has keyboard focus, `type`, `key`, and `hold_key` run whatever Claude types, and a click can start a program. If the task needs one, ask a person before keyboard input and clicks, and isolate the desktop so that a command can reach no further than the task needs.
4.  Refuse input your desktop shouldn't honor, such as a point outside the screenshot, a `wait` of several minutes, or a very large `repeat` or `scroll_amount`. Raise `ToolError` (throw it in TypeScript) instead of moving the value into range.
5.  Treat everything on the screen as untrusted, including window titles and clipboard text. Don't run it or pass it on unchecked.

The SDK applies step 2 through the callable you pass. The other steps are up to your driver and your deployment. The precautions under [Security considerations](agents-and-tools-tool-use-computer-use-tool.md#security-considerations) apply as well.

The following `confirm` asks a person before any keyboard input, through your own `ask_user` function, and approves every other call. `context.member` is the tool's name. To have a person approve clicks too, set `ASK_FIRST` to `KEYBOARD | CLICKS`.

Python

TypeScript



```python
from anthropic.tools.computer import BetaComputerConfirmContext

KEYBOARD = {"type", "key", "hold_key"}
CLICKS = {
    "left_click",
    "right_click",
    "middle_click",
    "double_click",
    "triple_click",
    "left_click_drag",
    "left_mouse_down",
    "left_mouse_up",
}
ASK_FIRST = KEYBOARD


def confirm(context: BetaComputerConfirmContext) -> bool:
    if context.member not in ASK_FIRST:
        return True
    # shown is the function from "Gate consequential members".
    detail = shown(context.input.to_dict())
    return ask_user(f'Allow the "{context.member}" tool with this input?\n{detail}')


desktop = MyDesktop(display, confirm=confirm)
```

A refused call gets an error result, and the run continues. For a refused `type` call, Claude reads `The user did not grant permission to run 'type'. Do not retry it unless the user asks you to.`

This `confirm` approves every tool that isn't in `ASK_FIRST`, including any tool you add later. To fail closed, approve only the tools with no effect on the desktop (`screenshot`, `zoom`, `cursor_position`, and `wait`) and ask about every other tool.

### Use both toolsets in one request

Pass both instances in `tools`. Each call carries its `toolset_name`, `browser` or `computer`, and the tool runner sends the call to the matching instance. After a failed call, the tool runner skips only the turn's later calls to the same toolset, so a failed computer call doesn't skip the turn's browser calls.

Python

TypeScript



```python
# MyBrowser, backend, and url_policy are from the quick start.
# confirm is the function from "Run the computer toolset safely".
with (
    MyBrowser(backend, url_policy=url_policy) as browser,
    MyDesktop(display, confirm=confirm) as desktop,
):
    runner = client.beta.messages.tool_runner(
        model="claude-opus-5-5",
        max_tokens=1024,
        tools=[browser, desktop],
        messages=[
            {
                "role": "user",
                "content": "Copy the heading on example.com into the open text editor.",
            }
        ],
        stream=True,
        run_tools_eagerly=True,  # so a call can start before the response ends
    )
    for stream in runner:
        print(stream.get_final_message())
```

In a loop you write, answer each call with `tool_result` on the instance whose `toolset_name` matches the call's `toolset_name`. In each turn, track failed calls for each toolset separately, and answer a skipped call with that toolset's own text. [Run without the tool runner](#run-without-the-tool-runner) has the browser's text, and the Skipped calls bullet at the top of this section has the computer's.

## Reference

The constructor options have the same meaning in both SDKs:

| Python                      | TypeScript     | Sets                                                                 |
|:----------------------------|:---------------|:---------------------------------------------------------------------|
| `configs`                   | `configs`      | Which members are enabled                                            |
| `confirm`                   | `confirm`      | The callable that approves or refuses each call                      |
| `url_policy`                | `urlPolicy`    | Your URL policy, which the SDK calls before each `navigate` to a URL |
| `file_policy`               | `filePolicy`   | Upload roots and download path exposure                              |
| `tool_configs`              | `toolConfigs`  | Fields for the `tools` entry, such as `cache_control`                |
| The `_browser_state` method | `browserState` | The state report                                                     |

The browser class takes every option in the table. The computer class takes `configs`, `confirm`, and `tool_configs`.

You can't change an option after construction. The [Python browser toolset guide](https://github.com/anthropics/anthropic-sdk-python/blob/main/browser-toolset.md), the [TypeScript browser toolset guide](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/browser-toolset.md), the [Python computer toolset guide](https://github.com/anthropics/anthropic-sdk-python/blob/main/computer-toolset.md), and the [TypeScript computer toolset guide](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/computer-toolset.md) describe each option. The Python guides also cover the async classes, `BetaAsyncAbstractBrowserToolset20260801` and `BetaAsyncAbstractComputerToolset20260801`.

## Limitations

- **The URL policy sees only `navigate` calls:** It doesn't see the requests a page makes, or pages that open any other way, such as from a link Claude clicks or a redirect. See [Intercept requests in the driver](#intercept-requests-in-the-driver).
- **An approval is based on the last state report:** The page can change after that report. The SDK doesn't check the page again before the call runs.
- **Calls on one toolset run one at a time:** You can't turn this off.
- **The SDK doesn't check that tab IDs are unique or how many tabs there are, and doesn't always check that one tab is active:** The API rejects a report that breaks those rules.
- **For a computer call, `confirm` receives the tool and its input, not the screen:** You can't tell from them what a click at a given point does.
- **The SDK doesn't resize a computer toolset's images:** The API rejects an image over the model's limits. See [Scale coordinates and size images](#scale-coordinates-and-size-images).

## Next steps

[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)

The member tools, the `browser_state` block, and the tool's security considerations.



[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)

The 17 tools, coordinates and image limits, and the tool's security considerations.



[Tool runner (SDK)](agents-and-tools-tool-use-tool-runner.md)

How the SDK runs the loop, and how to change the messages it sends.



[Mitigate jailbreaks and prompt injections](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md)

Guardrails for any application that reads untrusted content.
