---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:13Z"
source_url: "https://modelcontextprotocol.io/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti"
title: "SEP-1319: Decouple Request Payload from RPC Methods Definition - Model Context Protocol"
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

SEP-1319: Decouple Request Payload from RPC Methods Definition

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
- [Current Approach (Inline Definition):](#current-approach-inline-definition-)
- [Proposed Approach (Decoupled Definition):](#proposed-approach-decoupled-definition-)
- [Rationale](#rationale)
- [Backward Compatibility](#backward-compatibility)

Final

# SEP-1319: Decouple Request Payload from RPC Methods Definition

Copy page

Decouple Request Payload from RPC Methods Definition

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1319 |
| **Title** | Decouple Request Payload from RPC Methods Definition |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-08-08 |
| **Author(s)** | [@kurtisvg](https://github.com/kurtisvg) |
| **Sponsor** | None |
| **PR** | [\#1319](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1319) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes a structural refactoring of the Model Context Protocol (MCP) specification. The core change is to define payload of requests (e.g., CallToolRequest) as independent definitions and have the RPC method definitions refer to these models. This decouples the definition of the data payload from the definition of the remote procedure that transports it, leading to a clearer, more modular, and more maintainable specification.

## 

[​](#motivation)

Motivation

The current MCP specification tightly couples the data payload of a request with the JSON-RPC method that transports it. This design presents several challenges:

- **Reduced Clarity:** It forces developers to mentally parse the JSON-RPC transport structure just to understand the core data being exchanged. This increases cognitive load and makes the specification difficult to read and implement correctly.
- **Hindered Maintainability:** Defining data structures inline prevents their reuse across different methods, leading to redundancy and making future updates to the protocol more complex and error-prone.
- **Tightly Coupled to JSON-RPC:** Most critically, this tight coupling to JSON-RPC is the primary blocker for defining bindings for other transport protocols. To support transports like **gRPC** (which is currently a [popular ask from the community](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/966)), a transport-agnostic definition of its request and response messages. The current structure makes this practically impossible.

By refactoring the specification to separate the data model (the “what”) from the RPC method (the “how”), this proposal will create a clearer, more modular specification. This change will immediately improve the developer experience and, most importantly, pave the way for the future evolution of MCP across multiple transports.

## 

[​](#specification)

Specification

The proposal introduces the following principle: All data structures used as parameters (params) or results (result) for RPC methods should be defined as standalone, named schemas. The RPC method definitions will then use references to these schemas.

### 

[​](#current-approach-inline-definition-)

Current Approach (Inline Definition):

The RPC method definition contains the full structure of its parameters and results.

Copy

``` shiki
export interface CallToolRequest extends Request {
  method: "tools/call";
  params: {
    name: string;
    arguments?: { [key: string]: unknown };
  };
}
```

### 

[​](#proposed-approach-decoupled-definition-)

Proposed Approach (Decoupled Definition):

First, the data models for the request and response are defined as top-level schemas.

Copy

``` shiki
/**
 * Parameters for a `tools/call` request.
 *
 * @category tools/call
 */
export interface CallToolRequestParams extends RequestParams {
  name: string;
  arguments?: { [key: string]: unknown };
}
```

Then, the RPC method definition becomes much simpler, merely referring to these models.

Copy

``` shiki
export interface CallToolRequest extends Request {
  method: "tools/call";
  params: CallToolRequestParams;
}
```

## 

[​](#rationale)

Rationale

The proposed solution—separating payload definitions from the RPC method—was chosen as the most direct and non-disruptive path to achieving the goals outlined in the motivation. This approach establishes a clear architectural boundary between two distinct concerns:

1.  **The Data Layer:** The transport-agnostic payload definition (e.g., `CallToolRequestParams`), which represents the core information being exchanged.
2.  **The Transport Layer:** The protocol-specific wrapper (e.g., the JSON-RPC `CallToolRequest` object), which describes how the data is sent.

This architectural separation is superior to maintaining separate, parallel specifications for each transport (e.g., one for JSON-RPC, another for gRPC), which would introduce significant maintenance overhead and risk inconsistencies. Crucially, this design refactors the specification document itself but intentionally **leaves the on-the-wire format unchanged**. This makes the proposal fully backward-compatible, requiring no changes from existing, compliant clients and servers. In short, this change is a strategic, foundational improvement that enables future growth without penalizing the current ecosystem.

## 

[​](#backward-compatibility)

Backward Compatibility

This proposal is a **non-breaking change** for existing implementations. It is a refactoring of the *specification document itself* and does not alter the on-the-wire JSON format of the protocol messages. A client or server that is compliant with the old specification structure will remain compliant with the new one, as the resulting JSON payloads are identical. The primary impact is on developers who read the specification and on tools that parse the specification to generate code or documentation.

Was this page helpful?

Yes

No

[SEP-1303: Input Validation Errors as Tool Executi…](/community/seps/1303-input-validation-errors-as-tool-execution-errors)[SEP-1330: Elicitation Enum Schema Improvements an…](/community/seps/1330-elicitation-enum-schema-improvements-and-standards)

[github](https://github.com/modelcontextprotocol)
