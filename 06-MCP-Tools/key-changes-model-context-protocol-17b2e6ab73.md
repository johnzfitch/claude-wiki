---
category: "06-MCP-Tools"
fetched_at: "2026-02-27T09:27:01Z"
source_url: "https://modelcontextprotocol.io/specification/draft/changelog"
title: "Key Changes - Model Context Protocol"
---
# Key Changes


This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2025-11-25](/specification/2025-11-25).

## 

[​](#major-changes)

Major changes

N/A

## 

[​](#minor-changes)

Minor changes

1.  Add `extensions` field to `ClientCapabilities` and `ServerCapabilities` to support optional [extensions](/docs/extensions/overview) beyond the core protocol.
2.  Document OpenTelemetry trace context propagation conventions for `_meta` keys (`traceparent`, `tracestate`, `baggage`) ([SEP-414](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/414)).

## 

[​](#other-schema-changes)

Other schema changes

N/A

## 

[​](#governance-and-process-updates)

Governance and process updates

N/A

## 

[​](#process-changes)

Process changes

1.  Formalize PR-based SEP workflow with markdown files in `seps/` directory, PR-derived numbering, sponsor responsibilities, and status management via PR labels ([SEP-1850](https://github.com/modelcontextprotocol/specification/pull/1850)).

## 

[​](#full-changelog)

Full changelog

For a complete list of all changes that have been made since the last protocol revision, [see GitHub](https://github.com/modelcontextprotocol/specification/compare/2025-11-25...draft).
