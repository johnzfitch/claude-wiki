---
title: "Versioning - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/docs/2024-11-05/learn/versioning"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:38:32Z"
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

The **current** protocol version is [**2025-11-25**](/specification/2025-11-25).


[​](#feature-states)

Feature States

Individual features of the specification may additionally be marked as **Deprecated** under the [feature lifecycle and deprecation policy](/community/feature-lifecycle): the feature remains part of the specification, but is scheduled for removal. Deprecated features document a migration path (or state that none is required) and remain in the specification for at least twelve months, or at least ninety days under the policy’s [expedited-removal exception](/community/feature-lifecycle#expedited-removal), before they become eligible for removal, after which they may be **Removed** in a future revision.


[​](#negotiation)

Negotiation

Version negotiation happens during [initialization](/specification/2024-11-05/basic/lifecycle#initialization). Clients and servers **MAY** support multiple protocol versions simultaneously, but they **MUST** agree on a single version to use for the session. The protocol provides appropriate error handling if version negotiation fails, allowing clients to gracefully terminate connections when they cannot find a version compatible with the server.
