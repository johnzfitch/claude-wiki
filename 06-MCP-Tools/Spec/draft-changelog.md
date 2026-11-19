---
title: "Changelog - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/draft/changelog"
category: "06-MCP-Tools/Spec"
fetched_at: "2026-11-10T06:32:02Z"
last_modified: "Tue, 10 Nov 2026 00:48:45 GMT"
tags: ["mcp", "mcp-spec"]
---

## On this page

Back to top

- [Minor changes](#minor-changes)
- [Other schema changes](#other-schema-changes)

# Changelog

Copy pageCopy page

Copy pageCopy page

Changes since the most recent release will accumulate here.


[​](#minor-changes)

Minor changes

1.  Update the referenced version of [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-03) from `draft-ietf-oauth-client-id-metadata-document-00` to `draft-ietf-oauth-client-id-metadata-document-03`. MCP implementations that support Client ID Metadata Documents **MUST** follow this version.


[​](#other-schema-changes)

Other schema changes

1.  Restore the optional `_meta` field on `CreateMessageRequestParams`, `ElicitRequestFormParams`, `ElicitRequestURLParams`, `ElicitResult`, and `ListRootsResult`. It was unintentionally dropped in 2026-07-28 when these types stopped extending `TaskAugmentedRequestParams` and `Result`, leaving `ListRootsRequest` as the only input request that could carry `_meta` ([\#3468](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3468)).
