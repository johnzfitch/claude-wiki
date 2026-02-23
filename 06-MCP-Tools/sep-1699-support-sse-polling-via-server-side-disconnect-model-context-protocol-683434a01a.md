---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:14Z"
source_url: "https://modelcontextprotocol.io/community/seps/1699-support-sse-polling-via-server-side-disconnect"
title: "SEP-1699: Support SSE polling via server-side disconnect - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Final

SEP-1699: Support SSE polling via server-side disconnect

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/community/contributing)
  Contributing to MCP

&nbsp;

- [](/community/communication)
  Contributor Communication

##### Governance

- [](/community/governance)
  Governance and Stewardship
- [](/community/sep-guidelines)
  SEP Guidelines
- [](/community/sdk-tiers)
  SDK Tiering System
- [](/community/working-interest-groups)
  Working and Interest Groups
- [](/community/antitrust)
  Antitrust Policy

##### SEPs

- [](/community/seps)
  SEP Index

- Final

  - [](/community/seps/932-model-context-protocol-governance)
    SEP-932: Model Context Protocol Governance
  - [](/community/seps/973-expose-additional-metadata-for-implementations-res)
    SEP-973: Expose additional metadata for Implemen…
  - [](/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf)
    SEP-985: Align OAuth 2.0 Protected Resource Meta…
  - [](/community/seps/986-specify-format-for-tool-names)
    SEP-986: Specify Format for Tool Names
  - [](/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o)
    SEP-990: Enable enterprise IdP policy controls d…
  - [](/community/seps/991-enable-url-based-client-registration-using-oauth-c)
    SEP-991: Enable URL-based Client Registration us…
  - [](/community/seps/994-shared-communication-practicesguidelines)
    SEP-994: Shared Communication Practices/Guidelin…
  - [](/community/seps/1024-mcp-client-security-requirements-for-local-server-)
    SEP-1024: MCP Client Security Requirements for Lo…
  - [](/community/seps/1034--support-default-values-for-all-primitive-types-in)
    SEP-1034: Support default values for all primitiv…
  - [](/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera)
    SEP-1036: URL Mode Elicitation for secure out-of-…
  - [](/community/seps/1046-support-oauth-client-credentials-flow-in-authoriza)
    SEP-1046: Support OAuth client credentials flow i…
  - [](/community/seps/1302-formalize-working-groups-and-interest-groups-in-mc)
    SEP-1302: Formalize Working Groups and Interest G…
  - [](/community/seps/1303-input-validation-errors-as-tool-execution-errors)
    SEP-1303: Input Validation Errors as Tool Executi…
  - [](/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti)
    SEP-1319: Decouple Request Payload from RPC Metho…
  - [](/community/seps/1330-elicitation-enum-schema-improvements-and-standards)
    SEP-1330: Elicitation Enum Schema Improvements an…
  - [](/community/seps/1577--sampling-with-tools)
    SEP-1577: Sampling With Tools
  - [](/community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f)
    SEP-1613: Establish JSON Schema 2020-12 as Defaul…
  - [](/community/seps/1686-tasks)
    SEP-1686: Tasks
  - [](/community/seps/1699-support-sse-polling-via-server-side-disconnect)
    SEP-1699: Support SSE polling via server-side dis…
  - [](/community/seps/1730-sdks-tiering-system)
    SEP-1730: SDKs Tiering System
  - [](/community/seps/1850-pr-based-sep-workflow)
    SEP-1850: PR-Based SEP Workflow
  - [](/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)
    SEP-1865: MCP Apps - Interactive User Interfaces…
  - [](/community/seps/2085-governance-succession-and-amendment)
    SEP-2085: Governance Succession and Amendment Pro…
  - [](/community/seps/2133-extensions)
    SEP-2133: Extensions

- Draft

##### Roadmap

- [](/development/roadmap)
  Roadmap

##### Examples

- [](/clients)
  Example Clients
- [](/examples)
  Example Servers

On this page

- [Abstract](#abstract)
- [Motivation](#motivation)
- [Specification](#specification)
- [Rationale](#rationale)
- [Backward Compatibility](#backward-compatibility)
- [Additional Information](#additional-information)

Final

# SEP-1699: Support SSE polling via server-side disconnect

Copy page

Support SSE polling via server-side disconnect

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1699 |
| **Title** | Support SSE polling via server-side disconnect |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-10-22 |
| **Author(s)** | Jonathan Hefner ([@jonathanhefner](https://github.com/jonathanhefner)) |
| **Sponsor** | None |
| **PR** | [\#1699](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1699) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes changes to the Streamable HTTP transport in order to mitigate issues regarding long-running connections and resumability.

## 

[​](#motivation)

Motivation

The Streamable HTTP transport spec [does not allow](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/04c6e1f0ea6544c7df307fb2d7c637efe34f58d3/docs/specification/draft/basic/transports.mdx?plain=1#L109-L111) servers to close a connection while computing a result. In other words, barring client-side disconnection, servers must maintain potentially long-running connections.

## 

[​](#specification)

Specification

When a server starts an SSE stream, it MUST immediately send an SSE event consisting of an [`id`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22id%22) and an empty [`data`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22data%22) string in order to prime the client to reconnect with that event ID as the `Last-Event-ID`. Note that the SSE standard explicitly [permits setting `data` to an empty string](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=data%20buffer%20is%20an%20empty%20string), and says that the appropriate client-side handling is to record the `id` for `Last-Event-ID` but otherwise ignore the event (i.e., not call the event handler callback). At any point after the server has sent an event ID to the client, the server MAY disconnect at will. Specifically, [this part of the MCP spec](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/04c6e1f0ea6544c7df307fb2d7c637efe34f58d3/docs/specification/draft/basic/transports.mdx?plain=1#L109-L111) will be changed from:

> The server **SHOULD NOT** close the SSE stream before sending the JSON-RPC *response* for the received JSON-RPC *request*

To:

> The server **MAY** close the connection before sending the JSON-RPC *response* if it has sent an SSE event with an event ID to the client

If a server disconnects, the client will interpret the disconnection the same as a network failure, and will attempt to reconnect. In order to prevent clients from reconnecting / polling excessively, the server SHOULD send an SSE event with a [`retry`](https://html.spec.whatwg.org/multipage/server-sent-events.html#:~:text=field%20name%20is%20%22retry%22) field indicating how long the client should wait before reconnecting. Clients MUST respect the `retry` field.

## 

[​](#rationale)

Rationale

Servers may disconnect at will, avoiding long-running connections. Sending a `retry` field will prevent the client from hammering the server with inappropriate reconnection attempts.

## 

[​](#backward-compatibility)

Backward Compatibility

- **New Client + Old Server**: No changes. No backward incompatibility.
- **Old Client + New Server**: Client should interpret an at-will disconnect the same as a network failure. `retry` field is part of the SSE standard. No backward incompatibility if client already implements proper SSE resuming logic.

## 

[​](#additional-information)

Additional Information

This SEP supersedes (in part) [SEP-1335](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1335).

Was this page helpful?

Yes

No

[SEP-1686: Tasks](/community/seps/1686-tasks)[SEP-1730: SDKs Tiering System](/community/seps/1730-sdks-tiering-system)

[github](https://github.com/modelcontextprotocol)
