---
title: "Protocol eras - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/docs/draft/tools/inspector/protocol-eras"
category: "06-MCP-Tools/General"
fetched_at: "2026-10-09T06:27:34Z"
tags: ["mcp"]
---

## On this page

- [The Protocol Era setting](#the-protocol-era-setting)
- [Reproducing each era locally](#reproducing-each-era-locally)
- [Logging](#logging)
- [Resource subscriptions](#resource-subscriptions)
- [Tasks](#tasks)
- [Multi-round tool results (MRTR)](#multi-round-tool-results-mrtr)
- [Tools: mirrored headers and excluded tools](#tools-mirrored-headers-and-excluded-tools)
  - [-32602 error panels](#32602-error-panels)
- [Network and Protocol: headers and the error taxonomy](#network-and-protocol-headers-and-the-error-taxonomy)
- [Cancellation](#cancellation)
- [Sessions](#sessions)

Inspector

# Protocol eras

Copy pageCopy page

How the Inspector negotiates legacy vs. modern MCP, and how every feature is handled between protocol eras

Copy pageCopy page

The 2026-07-28 revision of MCP made substantial changes to the protocol. The Inspector therefore treats **protocol era** (legacy or modern, meaning before or as of that revision) as a first-class, per-server setting, orthogonal to the transport: the same HTTP URL can be inspected as a legacy server or as a modern one. Several tabs render meaningfully different UI and traffic depending on which era is in effect.


[​](#the-protocol-era-setting)

The `Protocol Era` setting

Each server carries a `protocolEra` of `legacy`, `auto`, or `modern`. In the web client it lives in **Server Settings**; in a catalog or config file it is the `protocolEra` field; the CLI and TUI read it from that same file, and their `--protocol-era <legacy|auto|modern>` flag overrides it for a single run.

| Era      | What the Inspector does at connect                                                      |
|----------|-----------------------------------------------------------------------------------------|
| `legacy` | **The default.** Plain `initialize`, no probing at all.                                 |
| `auto`   | Probe `server/discover` first, and fall back to `initialize` on any non-modern outcome. |
| `modern` | Pin exactly `2026-07-28`. No fallback, so a non-modern server fails loudly.             |

**Why `legacy` is the default, and not `auto`.** A debugging tool must not auto-probe. A `server/discover` probe stalls against silent legacy stdio servers, and it pollutes the recorded transcript you came here to read. Opting into `auto` or `modern` is a deliberate act, so what you see in the Protocol tab is what your server would have seen from a client behaving the way you configured.

Once connected, the negotiated era is shown as a badge on the **Protocol** tab’s Messages header and in **Connection Info**. On a modern connection, `server/discover` also supplies `capabilities` (including `extensions`), `instructions`, and the list of `supportedVersions`. The server’s name and version arrive in the result `_meta` under `io.modelcontextprotocol/serverInfo`.


[​](#reproducing-each-era-locally)

Reproducing each era locally

Every section below ends with a **Reproduce with …** pointer to a JSON config for one of the **composable test servers** shipped in the Inspector repository. Clone the repo and build the test servers:

```python
git clone https://github.com/modelcontextprotocol/inspector
cd inspector && npm install && npm run build
cd clients/web && npm run test-servers:build && cd ../..
```

Then, from the repo root, start a server from the config a section names:

```python
node test-servers/build/server-composable.js --config test-servers/configs/<name>.json
```

The server prints its URL on stderr. If the config’s port is already in use, it binds the next free port, so use the printed URL rather than assuming the port. Add that URL as a server in the Inspector, with the Protocol Era the section names.

------------------------------------------------------------------------


[​](#logging)

Logging

- Legacy

- Modern

Logging is **session-scoped**. The client sends `logging/setLevel` once, and the server emits `notifications/message` at or above that level for the rest of the session.The **Logs** tab shows a **Set Active Level** selector plus a **Set** button. Choose a level, click Set, and subsequent server logs stream into the panel.Reproduce with `test-servers/configs/logging-legacy-http.json`.

`logging/setLevel` is **gone**. Instead the client opts in **per request**, by stamping `_meta["io.modelcontextprotocol/logLevel"]` on each outgoing request. A server MUST NOT emit `notifications/message` for a request that did not opt in.The **Logs** tab therefore shows a **Log Level per Request** control instead. Pick a level and every subsequent request carries the stamp, visible in the Network tab’s request body. Logs emitted while handling a request ride that request’s SSE response stream.Set the control to **Off** and the `logLevel` key is omitted entirely, so the same tool call produces no logs at all. That silence is correct behavior, not a bug.The per-server default is `debug` (opted in at the most verbose level, since the Inspector is a debugging tool); set `modernLogLevel: "off"` on a server to opt back out by default.Reproduce with `test-servers/configs/logging-modern-http.json`.

------------------------------------------------------------------------


[​](#resource-subscriptions)

Resource subscriptions

- Legacy

- Modern

Clicking **Subscribe** on a resource sends `resources/subscribe`. The Subscriptions section lists the URI with no stream chrome. When the resource changes, the server emits `notifications/resources/updated` and the subscribed tile’s last-updated time is stamped.Reproduce with `test-servers/configs/subscriptions-legacy-http.json`, which also serves an `update_resource` tool so you can drive the notification round-trip yourself.

The same **Subscribe** button instead sends **`subscriptions/listen`**, with a filter carrying `resourceSubscriptions` plus whichever `*ListChanged` opt-ins apply (such as `resourcesListChanged`). The subscription is confirmed when the server sends `notifications/subscriptions/acknowledged`.Because the subscription is now a long-lived stream rather than a session flag, the Subscriptions section grows a **stream-status badge** in its header that moves from `Connecting...` to `Listening`. If the stream drops, the badge shows `Reconnecting...` while the Inspector re-sends `subscriptions/listen`. It shows `Stream ended` once the stream closes for good. It shows `Not acknowledged` when the server answers the listen with a plain result and never sends the acknowledgement; the Inspector does not retry in that case.Reproduce with `test-servers/configs/subscriptions-modern-http.json`. To see the `Not acknowledged` state, use `test-servers/configs/subscriptions-never-acknowledged-http.json`. That server acknowledges your first subscription, then refuses every later listen, so subscribing to a second resource trips the badge.

------------------------------------------------------------------------


[​](#tasks)

Tasks

Tasks change the most between protocol eras, including *how the Inspector UI tab is gated*.

- Legacy

- Modern

The **Tasks** tab appears when the server advertises `capabilities.tasks`. Run a tool with **Run as task** enabled and the tab lists it, populated by `tasks/list` and polled with `tasks/get`. The completed payload is fetched with a **blocking `tasks/result`**, and **Cancel** sends `tasks/cancel`.Reproduce with `test-servers/configs/tasks-legacy-http.json`.

Tasks are an **extension** (`io.modelcontextprotocol/tasks`, [SEP-2663](../SEPs/seps-2663-tasks-extension.md)), so the tab is gated on the server *advertising that extension* rather than on `capabilities.tasks`.Run a tool as a task and `tools/call` returns a `CreateTaskResult` (`resultType: "task"`, visible in the Protocol and Network tabs). The Inspector polls **`tasks/get`** only; there is no `tasks/list`, so **Refresh** re-polls the handles the client already knows about. A completed task **inlines its result**, with no blocking `tasks/result` call.A task that needs more information moves to `input_required` and surfaces an embedded [elicitation](../Spec/2026-07-28-client-elicitation.md) in the pending-request modal (the dialog the web client opens whenever a request is waiting on you). Answering it sends **`tasks/update`** carrying the `inputResponses`, and the next poll completes.Reproduce with `test-servers/configs/tasks-modern-http.json` (tools `modern_task` and `modern_input_task`).

------------------------------------------------------------------------


[​](#multi-round-tool-results-mrtr)

Multi-round tool results (MRTR)

On the modern era a tool can return `input_required` instead of a final result, embedding an [elicitation](../Spec/2026-07-28-client-elicitation.md), a [sampling](../Spec/2026-07-28-client-sampling.md) request, or a [`roots/list`](../Spec/draft-client-roots.md) request. The client answers that embedded request and retries the `tools/call` under a fresh JSON-RPC id until the call reaches `complete`. The Inspector drives MRTR **manually**, so each round pauses at the **pending-request modal**, tagged `input_required`, for you to answer. The Protocol view groups the whole exchange as one MRTR conversation rather than as unrelated calls. `test-servers/configs/mrtr-showcase-http.json` bundles every shape in one modern server:

| Tool            | What it exercises                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------|
| `mrtr_confirm`  | A single elicitation round.                                                                        |
| `mrtr_two_step` | Two elicitation rounds, threaded through `requestState`.                                           |
| `mrtr_sample`   | An embedded sampling request, routed to the Sampling panel.                                        |
| `mrtr_roots`    | An embedded `roots/list`, answered silently from configured roots (no modal).                      |
| `mrtr_edge`     | An `inputRequests`-only round, then a `requestState`-only round.                                   |
| `mrtr_empty`    | One elicitation round, then completes with an empty result (no `content`, no `structuredContent`). |
| `mrtr_loop`     | Never completes, so the client stops at its `MRTR_MAX_ROUNDS` limit.                               |

The legacy pattern of a server calling `server.elicitInput` (the test servers’ `collect_elicitation` preset) **errors** on a 2026-07-28 connection, because server-to-client requests aren’t allowed there. MRTR is its modern replacement.

------------------------------------------------------------------------


[​](#tools-mirrored-headers-and-excluded-tools)

Tools: mirrored headers and excluded tools

[SEP-2243](../SEPs/seps-2243-http-standardization.md) lets a tool annotate an argument with `x-mcp-header`, asking a Streamable HTTP client to mirror that argument’s value into an `Mcp-Param-*` request header. The Inspector surfaces both halves of that contract in the **Tools** tab:

- A tool with a **valid** annotation shows a **“Mirrored request headers (SEP-2243)”** section in its detail panel, for example `city -> Mcp-Param-City`.
- A tool with an **invalid** annotation (say, a header name of `"Bad Header"`, where the space makes it an invalid RFC 9110 token) appears struck through in the sidebar under an **“Excluded (SEP-2243)”** divider, with the reason on hover. A conforming client MUST drop such a tool from `tools/list`; the Inspector shows you *why* it was dropped instead of silently hiding it.

Reproduce with `test-servers/configs/xmcpheader-modern-http.json`.

On a modern connection the Inspector mirrors `x-mcp-header` arguments into `Mcp-Param-*` headers itself, in all three clients. In the **web** client the headers are added by the Inspector’s Node backend, which issues the upstream request, so they reach the server even though the browser never sends them.


[​](#32602-error-panels)

`-32602` error panels

A `tools/call` that rejects with `-32602` renders as a distinct **error panel**, on either era:

- **Unknown Tool**: when the message names a tool the server does not list. Reproduce by calling any name absent from the server’s `tools/list`.
- **Invalid Parameters**: any other `-32602`. Reproduce with the `trigger_invalid_params` tool in the config above.

The two share one error code, so the Inspector reads the message to tell them apart. Any other error code renders as a generic failure.

------------------------------------------------------------------------


[​](#network-and-protocol-headers-and-the-error-taxonomy)

Network and Protocol: headers and the error taxonomy

The modern era standardizes a set of `Mcp-*` HTTP headers and introduces a richer JSON-RPC error taxonomy ([SEP-2243](../SEPs/seps-2243-http-standardization.md) / [SEP-2575](../SEPs/seps-2575-stateless-mcp.md)). The two monitoring tabs divide the work:

- The **Network** tab is the HTTP view: mirrored `Mcp-*` headers are highlighted and sentinel values decoded.
- The **Protocol** tab is the JSON-RPC view: each spec error renders distinctly rather than as a generic failure.

`test-servers/configs/modern-network-http.json` serves four tools that produce a real HTTP status plus a JSON-RPC error body, one per class:

| Tool                          | HTTP  | JSON-RPC code | Meaning                                                      |
|-------------------------------|-------|---------------|--------------------------------------------------------------|
| `trigger_header_mismatch`     | `400` | `-32020`      | A required mirrored header was missing or wrong.             |
| `trigger_missing_capability`  | `400` | `-32021`      | The request omitted a client capability the server requires. |
| `trigger_unsupported_version` | `400` | `-32022`      | Unsupported version; supported versions in `data.supported`. |
| `trigger_method_not_found`    | `404` | `-32601`      | Method not found.                                            |

------------------------------------------------------------------------


[​](#cancellation)

Cancellation

On a legacy connection, cancelling an in-flight tool call sends `notifications/cancelled`. On a modern Streamable HTTP connection the Inspector instead closes that request’s own SSE response stream, which is the 2026-07-28 cancellation signal. Over stdio, cancellation is still `notifications/cancelled`. Reproduce with `test-servers/configs/cancellation-modern-http.json`: run `slow_task`, click **Cancel** after a few seconds, and the server’s terminal prints how far the task got before it stopped.

------------------------------------------------------------------------


[​](#sessions)

Sessions

A legacy Streamable HTTP connection may carry a server-assigned session id (`Mcp-Session-Id`), which the client tears down with an HTTP `DELETE`. A modern connection is **sessionless and per-request**: with no session id the client SDK sends no `DELETE` to the server, so disconnect is purely local. A legacy connection also opens a standalone `GET` notification stream after `initialize`, to carry notifications that do not belong to any request. The legacy-only **Suppress Notification Stream** option in **Server Settings** skips that stream, so you can inspect a server that cannot serve a second concurrent request. Modern connections never open the stream, so the option does not apply to them. This has a practical consequence for your own test servers. A stateless modern handler constructed per request cannot hold state between calls, which is why `test-servers/configs/subscriptions-modern-http.json`, unlike its legacy counterpart, omits an `update_resource` tool: the mutation would run against a throwaway server instance and be invisible to the next read.
