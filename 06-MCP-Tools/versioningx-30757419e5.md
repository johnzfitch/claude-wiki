---
category: "06-MCP-Tools"
fetched_at: "2026-02-23T00:45:47Z"
source_url: "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/docs/specification/versioning.mdx"
title: "Versioningx"
---

--- title: Versioning type: docs weight: 10 --- The Model Context Protocol uses string-based version identifiers following the format \`YYYY-MM-DD\`, to indicate the last date backwards incompatible changes were made. The protocol version will \_not\_ be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability. \## Revisions Revisions may be marked as: - \*\*Draft\*\*: in-progress specifications, not yet ready for consumption. - \*\*Current\*\*: the current protocol version, which is ready for use and may continue to receive backwards compatible changes. - \*\*Final\*\*: past, complete specifications that will not be changed. The \*\*current\*\* protocol version is \[\*\*2025-11-25\*\*\](/specification/2025-11-25/). \## Negotiation Version negotiation happens during \[initialization\](/specification/latest/basic/lifecycle#initialization). Clients and servers \*\*MAY\*\* support multiple protocol versions simultaneously, but they \*\*MUST\*\* agree on a single version to use for the session. The protocol provides appropriate error handling if version negotiation fails, allowing clients to gracefully terminate connections when they cannot find a version compatible with the server.
