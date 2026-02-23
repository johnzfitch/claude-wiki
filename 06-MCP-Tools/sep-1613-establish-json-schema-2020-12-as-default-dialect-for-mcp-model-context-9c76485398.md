---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:14Z"
source_url: "https://modelcontextprotocol.io/community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f"
title: "SEP-1613: Establish JSON Schema 2020-12 as Default Dialect for MCP - Model Context Protocol"
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

SEP-1613: Establish JSON Schema 2020-12 as Default Dialect for MCP

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
- [1. Default Dialect](#1-default-dialect)
- [2. Explicit Dialect Declaration](#2-explicit-dialect-declaration)
- [3. Schema Validation Requirements](#3-schema-validation-requirements)
- [4. Scope of Application](#4-scope-of-application)
- [5. Implementation Requirements](#5-implementation-requirements)
- [Rationale](#rationale)
- [Why 2020-12?](#why-2020-12)
- [Why allow explicit declaration?](#why-allow-explicit-declaration)
- [Alternatives considered](#alternatives-considered)
- [Backward Compatibility](#backward-compatibility)
- [Reference Implementation](#reference-implementation)
- [SDK Implementations](#sdk-implementations)
- [Security Implications](#security-implications)
- [Related Work](#related-work)
- [SEP-1330: Elicitation Enum Schema Improvements](#sep-1330-elicitation-enum-schema-improvements)
- [SEP-834: Full JSON Schema 2020-12 Support](#sep-834-full-json-schema-2020-12-support)
- [Open Questions](#open-questions)

Final

# SEP-1613: Establish JSON Schema 2020-12 as Default Dialect for MCP

Copy page

Establish JSON Schema 2020-12 as Default Dialect for MCP

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1613 |
| **Title** | Establish JSON Schema 2020-12 as Default Dialect for MCP |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-10-06 |
| **Author(s)** | Ola Hungerford |
| **Sponsor** | None |
| **PR** | [\#1613](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1613) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP establishes JSON Schema 2020-12 as the default dialect for embedded schemas within MCP messages (tool `inputSchema`/`outputSchema` and elicitation `requestedSchema` fields). Schemas may explicitly declare alternative dialects via the `$schema` field. This resolves ambiguity that has caused compatibility issues between implementations.

## 

[​](#motivation)

Motivation

The MCP specification does not explicitly state which JSON Schema version to use for embedded schemas. This has caused:

- Validation failures between clients and servers assuming different versions
- Implementation divergence across SDK ecosystems
- Developer uncertainty requiring arbitrary version choices

Community discussion (GitHub Discussion \#366, PR \#655) revealed that implementations were split between draft-07 and 2020-12, with multiple maintainers and community members expressing strong preference for 2020-12 as the default.

## 

[​](#specification)

Specification

### 

[​](#1-default-dialect)

1. Default Dialect

Embedded JSON schemas within MCP messages **MUST** conform to [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/schema) when no `$schema` field is present.

### 

[​](#2-explicit-dialect-declaration)

2. Explicit Dialect Declaration

Schemas **MAY** include an explicit `$schema` field to declare a different dialect:

Copy

``` shiki
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string" }
  }
}
```

### 

[​](#3-schema-validation-requirements)

3. Schema Validation Requirements

- Schemas **MUST** be valid according to their declared or default dialect
- The `inputSchema` field **MUST NOT** be `null`

**For tools with no parameters**, use one of these valid approaches:

- `true` - accepts any input (most permissive)
- `{}` - equivalent to `true`, accepts any input
- `{ "type": "object" }` - accepts any object with any properties
- `{ "type": "object", "additionalProperties": false }` - accepts only empty objects `{}`

**Example** for a tool with no parameters:

Copy

``` shiki
{
  "name": "get_current_time",
  "description": "Returns the current server time",
  "inputSchema": {
    "type": "object",
    "additionalProperties": false
  }
}
```

### 

[​](#4-scope-of-application)

4. Scope of Application

This specification applies to:

- `tools/list` response: `inputSchema` and `outputSchema`
- `prompts/elicit` request: `requestedSchema`
- Future MCP features embedding JSON Schema definitions

### 

[​](#5-implementation-requirements)

5. Implementation Requirements

**Servers MUST:**

- Generate schemas conforming to 2020-12 by default
- Include explicit `$schema` when using non-default dialects

**Clients MUST:**

- Validate schemas according to declared or default dialect
- Support at least JSON Schema 2020-12

## 

[​](#rationale)

Rationale

### 

[​](#why-2020-12)

Why 2020-12?

1.  **Ecosystem alignment**: Python SDK (via Pydantic) and Go SDK implementations prefer/use 2020-12
2.  **Modern features**: Better validation capabilities and composition support
3.  **Community preference**: Multiple maintainers and community members in PR \#655 discussion advocated for 2020-12 over draft-07
4.  **Current standard**: 2020-12 is the stable version as of 2025

### 

[​](#why-allow-explicit-declaration)

Why allow explicit declaration?

- Supports migration paths for existing schemas
- Provides flexibility without protocol changes
- Follows JSON Schema best practices

### 

[​](#alternatives-considered)

Alternatives considered

- **Draft-07 as default**: Rejected after community feedback; older version with less capability
- **No default**: Rejected as unnecessarily verbose; adds boilerplate
- **Multiple equal versions**: Rejected; creates unpredictability and fragmentation

## 

[​](#backward-compatibility)

Backward Compatibility

This is technically a **clarification**, and not a breaking change:

- Existing schemas without `$schema` default to 2020-12
- Servers can add explicit `$schema` during transition
- Basic schemas (type, properties, required) work across versions

**Migration may be needed for schemas assuming draft-07 by default:**

- Schemas using `dependencies` (→ `dependentSchemas` + `dependentRequired`)
- Positional array validation (→ `prefixItems`)

**Migration strategy:** Add explicit `$schema: "http://json-schema.org/draft-07/schema#"` during transition, then update to 2020-12 features.

## 

[​](#reference-implementation)

Reference Implementation

### 

[​](#sdk-implementations)

SDK Implementations

**Python SDK** - Already compatible:

- Uses Pydantic for schema generation
- Pydantic defaults to 2020-12 via `.model_json_schema()`

**Go SDK** - Implemented 2020-12:

- Explicit 2020-12 implementation completed
- Confirmed by @samthanawalla in PR \#655 discussion

**Other SDKs:**

- May require updates but based on other examples, there should be straightforward or out-of-the-box options to support this. I can add more examples here or we can create issues to follow up on these after acceptance.

## 

[​](#security-implications)

Security Implications

No specific security implications have been identified from establishing 2020-12 as the default dialect. The clarification reduces ambiguity that could lead to validation mismatches between implementations, which is a minor security improvement through increased predictability. Implementations should use well-maintained JSON Schema validator libraries and keep them updated, as with any dependency.

## 

[​](#related-work)

Related Work

### 

[​](#sep-1330-elicitation-enum-schema-improvements)

[SEP-1330: Elicitation Enum Schema Improvements](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1330)

**SEP-1330** proposes deprecating the non-standard `enumNames` property in favor of JSON Schema 2020-12 compliant patterns. This work is directly enabled by establishing 2020-12 as the default dialect. **Implementation Consideration:**\
As noted in SEP-1330 discussion, there is some concern about parsing complexity with advanced JSON Schema features like `oneOf` and `anyOf`. However, these features are part of the JSON Schema standard and well-supported by mature validator libraries. Implementations can balance standards compliance with their parsing needs by using well-tested JSON Schema validation libraries.

### 

[​](#sep-834-full-json-schema-2020-12-support)

[SEP-834: Full JSON Schema 2020-12 Support](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/834)

This SEP establishes the foundation (default dialect) while SEP-834 addresses comprehensive support for 2020-12 features.

## 

[​](#open-questions)

Open Questions

The schema for the spec itself references `draft-07` and the `typescript-json-schema` package we use to generate it only supports draft-07. Options:

1.  Update schema generation script to patch to 2020-12 after generation (this is what I did in the current PR)
2.  Switch to a different schema generator that supports 2020-12
3.  Leave as-is since it doesn’t actually conflict with the spec?

Personally I’d prefer (1) in the short term and then (2) as a follow-up.

Was this page helpful?

Yes

No

[SEP-1577: Sampling With Tools](/community/seps/1577--sampling-with-tools)[SEP-1686: Tasks](/community/seps/1686-tasks)

[github](https://github.com/modelcontextprotocol)
