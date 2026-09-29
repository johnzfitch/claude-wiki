---
title: "Versioning - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/docs/draft/learn/versioning"
category: "06-MCP-Tools/General"
fetched_at: "2026-09-29T06:30:36Z"
tags: ["mcp"]
---

## On this page

- [Revisions](#revisions)
- [Feature States](#feature-states)
- [Negotiation](#negotiation)

About MCP

# Versioning

Copy pageCopy page

Copy pageCopy page

The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.

The protocol version will *not* be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability.


[​](#revisions)

Revisions

Revisions may be marked as:

- **Draft**: in-progress specifications, not yet ready for consumption.
- **Current**: the current protocol version, which is ready for use and may continue to receive backwards compatible changes.
- **Final**: past, complete specifications that will not be changed.

The **current** protocol version is [**2026-07-28**](../Spec/draft.md).


[​](#feature-states)

Feature States

Individual features of the specification may additionally be marked as **Deprecated** under the [feature lifecycle and deprecation policy](../Community/community-feature-lifecycle.md): the feature remains part of the specification, but is scheduled for removal. Deprecated features document a migration path (or state that none is required) and remain in the specification for at least twelve months, or at least ninety days under the policy’s [expedited-removal exception](../Community/community-feature-lifecycle.md#expedited-removal), before they become eligible for removal, after which they may be **Removed** in a future revision. Features that are currently Deprecated are listed in the [deprecated features registry](../Spec/draft-deprecated.md).


[​](#negotiation)

Negotiation

Every request declares the protocol version it is using via the `io.modelcontextprotocol/protocolVersion` key in its [`_meta`](https://modelcontextprotocol.io/specification/draft/basic/index#meta) field, and the server accepts or rejects each request independently. On Streamable HTTP, the same value is also carried in the [`MCP-Protocol-Version` header](../Spec/draft-basic-transports-streamable-http.md#protocol-version-header). Clients and servers **MAY** support multiple protocol versions simultaneously. If the server does not support the requested version, it responds with an [`UnsupportedProtocolVersionError`](../Spec/draft-basic-versioning.md#protocol-version-negotiation) listing the versions it does support. The client can then retry the request with a mutually supported version, or surface an error to the user if none exists. Clients that want to select a version up front can call [`server/discover`](../Spec/2026-07-28-server-discover.md), a mandatory RPC that returns the server’s supported protocol versions, capabilities, and identity in a single request. Calling it is optional: a client is free to send any request directly and handle a version error if one comes back. For interoperability with servers and clients that implement the handshake-based protocol revisions (`2025-11-25` and earlier), see [Backward Compatibility](../Spec/draft-basic-versioning.md#backward-compatibility-with-initialization-based-versions).
