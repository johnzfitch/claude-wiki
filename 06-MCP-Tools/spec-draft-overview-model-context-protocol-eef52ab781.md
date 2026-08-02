---
title: "Overview - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/draft/basic/patterns"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:39:41Z"
tags: ["mcp"]
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

This page defines the message patterns of the core protocol: the ways a client and server compose JSON-RPC [requests, responses, and notifications](/specification/draft/basic/index#messages) into interactions. Every [transport](/specification/draft/basic/transports) carries all of these patterns; transports differ only in how messages are framed and delivered. Every interaction begins with the client:

- The **client** sends JSON-RPC *requests* and *notifications*.
- The **server** answers each request with a JSON-RPC *response* (a result or error), optionally preceded by *notifications* scoped to that request.

Servers **MUST NOT** initiate JSON-RPC requests, and clients do not send JSON-RPC responses.


[​](#request-and-response)

Request and Response

The client sends a request; the server answers it with a result or an error. While the request is in flight, the server **MAY** send notifications scoped to it, such as [`notifications/progress`](/specification/draft/basic/patterns/progress) and [`notifications/message`](/specification/draft/server/utilities/logging).


[​](#multi-round-trip-requests)

Multi Round-Trip Requests

When a server needs client input (sampling, elicitation, or roots) to complete a request, it answers with an [`InputRequiredResult`](/specification/draft/basic/patterns/mrtr#inputrequiredresult) and the client retries the request with the matching `inputResponses`. See [Multi Round-Trip Requests](/specification/draft/basic/patterns/mrtr).


[​](#subscribe-and-notify)

Subscribe and Notify

To receive change notifications (list changes, resource updates), the client sends a [`subscriptions/listen`](/specification/draft/basic/patterns/subscriptions) request; the reply is a long-lived stream of the requested notification types. Stream state is scoped to the request: if the underlying channel is lost, the client re-issues the request.


[​](#adding-patterns)

Adding Patterns

All core protocol features are built from these patterns. A protocol revision that adds a pattern defines it on this page. Transports carry new patterns without changes, because patterns are expressed entirely in terms of requests, responses, and notifications.
