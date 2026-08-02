---
title: "stdio - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:38:32Z"
tags: ["mcp"]
---

## On this page

- [Sending Messages](#sending-messages)
- [Receiving Messages](#receiving-messages)
- [Request Metadata](#request-metadata)
- [Cancellation](#cancellation)
- [Shutdown](#shutdown)
- [Unexpected Termination](#unexpected-termination)
- [Backward Compatibility](#backward-compatibility)

Transports

# stdio

Copy pageCopy page

Copy pageCopy page

In the **stdio** transport, the client launches the MCP server as a subprocess. The two ends communicate over the subprocess’s standard streams:

- The server reads JSON-RPC messages from `stdin` and writes JSON-RPC messages to `stdout`.
- Each message is a single JSON-RPC request, notification, or response.
- Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
- The server **MAY** write UTF-8 strings to `stderr` for any logging purposes including informational, debug, and error messages.
- The client **MAY** capture, forward, or ignore the server’s `stderr` output and **SHOULD NOT** assume `stderr` output indicates error conditions.
- The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
- The client **MUST NOT** write anything to the server’s `stdin` that is not a valid MCP message.

Standard streams are the canonical channel, but nothing in this binding depends on them except the process lifecycle. The wire format (one newline-delimited JSON-RPC message per line over a reliable bidirectional byte stream) works unchanged over Unix domain sockets, TCP connections, or any similar channel. [Custom transports](/specification/2026-07-28/basic/transports#custom-transports) built on such streams **SHOULD** reuse this framing and the message rules on this page; only the subprocess-specific aspects (launch, `stderr`, shutdown by closing the stream, process restart) need channel-specific equivalents.


[​](#sending-messages)

Sending Messages

The client sends messages by writing JSON-RPC *requests* and *notifications* to the server’s `stdin`, one message per line. The client **MUST NOT** write JSON-RPC *responses*.


[​](#receiving-messages)

Receiving Messages

The client reads server messages from `stdout`, one message per line. All messages share this single channel; there are no per-request streams. The server writes three kinds of messages:

1.  *Responses* to client requests, correlated by JSON-RPC `id`.
2.  *Notifications* that relate to an in-flight request, such as `notifications/progress` and `notifications/message`.
3.  *Notifications* delivered for an active [`subscriptions/listen`](/specification/2026-07-28/basic/patterns/subscriptions) request. Clients **MUST** correlate these using the `io.modelcontextprotocol/subscriptionId` field in `_meta`; see [`SubscriptionsListenRequest`](/specification/2026-07-28/schema#subscriptionslistenrequest).

The server **MUST NOT** write JSON-RPC *requests* to `stdout`. Server-to-client interactions are carried in [`InputRequiredResult`](/specification/2026-07-28/basic/patterns/mrtr#inputrequiredresult) replies; see [Multi Round-Trip Requests](/specification/2026-07-28/basic/patterns/mrtr).


[​](#request-metadata)

Request Metadata

All request metadata for the stdio transport is carried inline in the JSON-RPC message body. The protocol version, per-request capabilities, and optional client identity live in [`_meta.io.modelcontextprotocol/*`](/specification/2026-07-28/basic/index#meta); the method name and arguments live where JSON-RPC puts them. There is no header layer.


[​](#cancellation)

Cancellation

To cancel an in-flight request, the client **MUST** send a `notifications/cancelled` notification referencing the request’s ID. Because stdio is a single shared bidirectional channel, there is no per-request stream to close. Servers **SHOULD** stop work on a cancelled request as soon as practical and **MUST NOT** send any further messages for it. See [Cancellation](/specification/2026-07-28/basic/patterns/cancellation) for the full rules.


[​](#shutdown)

Shutdown

The client **SHOULD** initiate shutdown by:

1.  Closing the input stream to the child process (the server).
2.  Waiting for the server to exit.
3.  If the server does not exit within a reasonable time, forcibly terminating the process using the mechanism appropriate for the operating system.

On POSIX systems, forced termination typically escalates from [`SIGTERM`](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/signal.h.html) to `SIGKILL`. On Windows, where POSIX signals are not available, clients can use [`TerminateProcess`](https://learn.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess) or [Job Objects](https://learn.microsoft.com/windows/win32/procthread/job-objects). Servers **SHOULD** exit promptly when their standard input is closed or reads return end-of-file. This is the primary graceful-shutdown signal and the only portable one, so honoring it reduces the need for forced termination. The server **MAY** initiate shutdown by closing its output stream to the client and exiting.


[​](#unexpected-termination)

Unexpected Termination

If the server process exits unexpectedly, the client **SHOULD** restart it. Because the protocol is stateless, any in-flight requests are simply lost and the client can retry them against the fresh process. Active [`subscriptions/listen`](/specification/2026-07-28/basic/patterns/subscriptions) streams must also be re-established after restart.


[​](#backward-compatibility)

Backward Compatibility

A client that supports both modern (per-request-metadata) MCP versions and a legacy version that requires an `initialize` handshake **SHOULD** probe with [`server/discover`](/specification/2026-07-28/schema#discoverrequest) before sending any other request, setting its preferred modern version in `_meta`. The probe has three possible outcomes:

- The server returns a `DiscoverResult`: the server is modern. Select a mutually supported version from `supportedVersions` and continue.
- The server returns a recognized modern JSON-RPC error such as [`UnsupportedProtocolVersionError`](/specification/2026-07-28/schema#unsupportedprotocolversionerror): the server is modern but does not support the requested version. Use one of the versions in its advertised `supported` list. Do **not** fall back to `initialize`.
- The server returns any other error, or does not respond within a reasonable timeout: the server is legacy. Fall back to the `initialize` handshake.

The fallback **MUST NOT** be keyed to one specific error code: legacy servers respond to unknown pre-`initialize` requests with implementation-defined errors (commonly `-32601` or `-32602`) or not at all. A client that only supports modern versions does not need to probe, but probing is still **RECOMMENDED**: some legacy servers do not validate that a request arrives after `initialize` and would process an era-ambiguous method (such as `tools/call`) under legacy semantics. Probing yields a deterministic failure instead. See [Versioning: Backward Compatibility](/specification/2026-07-28/basic/versioning#backward-compatibility-with-initialization-based-versions) for the era model and a compatibility matrix for implementors.
