---
title: "Overview - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns"
category: "06-MCP-Tools/Spec"
fetched_at: "2026-09-29T06:30:45Z"
tags: ["mcp", "mcp-spec"]
---

## On this page

- [Request and Response](#request-and-response)
- [Multi Round-Trip Requests](#multi-round-trip-requests)
- [Subscribe and Notify](#subscribe-and-notify)
- [Adding Patterns](#adding-patterns)

Message Patterns

# Overview

Copy pageCopy page

Copy pageCopy page

This page defines the message patterns of the core protocol: the ways a client and server compose JSON-RPC [requests, responses, and notifications](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#messages) into interactions. Every [transport](draft-basic-transports.md) carries all of these patterns; transports differ only in how messages are framed and delivered. Every interaction begins with the client:

- The **client** sends JSON-RPC *requests* and *notifications*.
- The **server** answers each request with a JSON-RPC *response* (a result or error), optionally preceded by *notifications* scoped to that request.

Servers **MUST NOT** initiate JSON-RPC requests, and clients do not send JSON-RPC responses.


[​](#request-and-response)

Request and Response

The client sends a request; the server answers it with a result or an error. While the request is in flight, the server **MAY** send notifications scoped to it, such as [`notifications/progress`](draft-basic-patterns-progress.md) and [`notifications/message`](2026-07-28-server-utilities-logging.md).


[​](#multi-round-trip-requests)

Multi Round-Trip Requests

When a server needs client input (sampling, elicitation, or roots) to complete a request, it answers with an [`InputRequiredResult`](2026-07-28-basic-patterns-mrtr.md#inputrequiredresult) and the client retries the request with the matching `inputResponses`. See [Multi Round-Trip Requests](2026-07-28-basic-patterns-mrtr.md).


[​](#subscribe-and-notify)

Subscribe and Notify

To receive change notifications (list changes, resource updates), the client sends a [`subscriptions/listen`](2026-07-28-basic-patterns-subscriptions.md) request; the reply is a long-lived stream of the requested notification types. Stream state is scoped to the request: if the underlying channel is lost, the client re-issues the request.


[​](#adding-patterns)

Adding Patterns

All core protocol features are built from these patterns. A protocol revision that adds a pattern defines it on this page. Transports carry new patterns without changes, because patterns are expressed entirely in terms of requests, responses, and notifications.
