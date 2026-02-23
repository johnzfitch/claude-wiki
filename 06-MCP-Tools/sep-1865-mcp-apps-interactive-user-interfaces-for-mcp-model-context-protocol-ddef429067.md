---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp"
title: "SEP-1865: MCP Apps - Interactive User Interfaces for MCP - Model Context Protocol"
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

SEP-1865: MCP Apps - Interactive User Interfaces for MCP

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
- [Predeclared resources vs. inline embedding](#predeclared-resources-vs-inline-embedding)
- [Reusing MCP JSON-RPC instead of a custom protocol](#reusing-mcp-json-rpc-instead-of-a-custom-protocol)
- [HTML-only MVP](#html-only-mvp)
- [Backward Compatibility](#backward-compatibility)
- [Security Implications](#security-implications)
- [Reference Implementation](#reference-implementation)

Final

# SEP-1865: MCP Apps - Interactive User Interfaces for MCP

Copy page

MCP Apps - Interactive User Interfaces for MCP

Copy page

FinalExtensions Track

| Field | Value |
|----|----|
| **SEP** | 1865 |
| **Title** | MCP Apps - Interactive User Interfaces for MCP |
| **Status** | Final |
| **Type** | Extensions Track |
| **Created** | 2025-11-21 |
| **Author(s)** | Ido Salomon ([@idosal](https://github.com/idosal)), Liad Yosef ([@liadyosef](https://github.com/liadyosef)), Olivier Chafik ([@olivierchafik](https://github.com/olivierchafik)), |
| **Sponsor** | None (seeking sponsor) |
| **PR** | [\#1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes an extension to MCP (per SEP-1724) that enables servers to deliver interactive user interfaces to hosts. MCP Apps introduces a standardized pattern for declaring UI resources via the `ui://` URI scheme, associating them with tools through metadata, and facilitating bi-directional communication between the UI and the host using MCP’s JSON-RPC base protocol. This extension addresses the growing community need for rich, interactive experiences in MCP-enabled applications, maintaining security, auditability, and alignment with MCP’s core architecture. The initial specification focuses on HTML resources (`text/html;profile=mcp-app`) with a clear path for future extensions.

## 

[​](#motivation)

Motivation

MCP lacks a standardized way for servers to deliver rich, interactive user interfaces to hosts. This gap blocks many use cases that require visual presentation and interactivity that go beyond plain text or structured data. As more hosts adopt this capability, the risk of fragmentation and interoperability challenges grows. [MCP-UI](https://mcpui.dev/) has demonstrated the viability and value of MCP apps built on UI resources and serves as a community playground for the UI spec and SDK. Fueled by a dedicated community, it developed the bi-directional communication model and the HTML, external URL, and remote DOM content types. MCP-UI’s adopters, including hosts and providers such as Postman, HuggingFace, Shopify, Goose, and ElevenLabs, have provided critical insights and contributions to the community. OpenAI’s [Apps SDK](https://developers.openai.com/apps-sdk/), launched in November 2025, further validated the demand for rich UI experiences within conversational AI interfaces. The Apps SDK enables developers to build rich, interactive applications inside ChatGPT using MCP as its backbone. The architecture of both the Apps SDK and MCP-UI has significantly informed the design of this specification. However, without formal standardization:

- Servers cannot reliably expect UI support via MCP
- Each host may implement slightly different behaviors
- Security and auditability patterns are inconsistent
- Developers must maintain separate implementations or adapters for different hosts (e.g., MCP-UI vs. Apps SDK)

This SEP addresses the current limitations through an optional, backwards-compatible extension that unifies the approaches pioneered by MCP-UI and the Apps SDK into a single, open standard.

## 

[​](#specification)

Specification

The full specification can be found at [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx). At a high level, MCP Apps extends the Model Context Protocol to enable servers to deliver interactive user interfaces to hosts. This extension introduces:

- **UI Resources:** Predeclared resources using the `ui://` URI scheme
- **Resource Discovery:** Tools reference UI resources via metadata
- **Bi-directional Communication:** UI iframes communicate with hosts using standard MCP JSON-RPC protocol
- **Security Model:** Mandatory iframe sandboxing with auditable communication

This specification focuses on HTML content (`text/html;profile=mcp-app`) as the initial content type, with extensibility for future formats. As an extension, MCP Apps is optional and must be explicitly negotiated between clients and servers through the extension capabilities mechanism (see Capability Negotiation section in the [full specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx)).

## 

[​](#rationale)

Rationale

### 

[​](#predeclared-resources-vs-inline-embedding)

Predeclared resources vs. inline embedding

UI is modeled as predeclared resources (`ui://`), referenced by tools via metadata. This allows:

- Hosts to prefetch templates before tool execution, improving performance
- Separation of presentation (template) from data (tool results), facilitating caching
- Security review of UI resources

**Alternatives considered:**

- **Embedded resources:** Current MCP-UI approach, where resources are returned in tool results. Although it’s more convenient for server development, it was deferred due to the gaps in performance optimization and the challenges in the UI review process.
- **Resource links:** Predeclare the resources but return links in tool results. Deferred due to the gaps in performance optimization.

### 

[​](#reusing-mcp-json-rpc-instead-of-a-custom-protocol)

Reusing MCP JSON-RPC instead of a custom protocol

Reuses existing MCP infrastructure (type definitions, SDKs, etc.). JSON-RPC offers advanced capabilities (timeouts, errors, etc.). **Alternatives considered:**

- **Custom message protocol:** Current MCP-UI approach with message types like tool, intent, prompt, etc. These message types can be translated to a subset of the proposed JSON-RPC messages.
- **Global API object:** Rejected because it requires host-specific injection and doesn’t work with external iframe sources. Syntactic sugar may still be added on the server/UI side.

### 

[​](#html-only-mvp)

HTML-only MVP

- HTML is universally supported and well-understood
- Simplest security model (standard iframe sandbox)
- Allows screenshot/preview generation (e.g., via html2canvas)
- Sufficient for most observed use cases
- Provides a clear baseline for future extensions

**Alternatives considered:**

- **Include external URLs in MVP:** This is one of the easiest content types for servers to adopt, as it’s possible to embed regular apps. However, it was deferred due to concerns around model visibility, inability to screenshot content, and review process. It may effectively be supported with the SEP’s new `externalIframes` capability.

## 

[​](#backward-compatibility)

Backward Compatibility

The proposal is an optional extension to the core protocol. Existing implementations continue working without changes.

## 

[​](#security-implications)

Security Implications

Hosting interactive UI content from potentially untrusted MCP servers requires careful security consideration. Based on the threat model, MCP Apps proposes the following mitigations:

- **Iframe sandboxing**: All UI content runs in sandboxed iframes with restricted permissions
- **Predeclared templates**: Hosts can review HTML content before rendering
- **Auditable messages**: All UI-to-host communication goes through loggable JSON-RPC
- **User consent**: Hosts can require explicit approval for UI-initiated tool calls

A full threat model analysis and mitigations are available in the [full specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/draft/apps.mdx).

## 

[​](#reference-implementation)

Reference Implementation

- [MCP-UI](https://github.com/idosal/mcp-ui) client and server SDKs support the patterns proposed in this spec.
- [ext-apps](https://github.com/modelcontextprotocol/ext-apps) repository contains a prototype implementation by Olivier Chafik.

Was this page helpful?

Yes

No

[SEP-1850: PR-Based SEP Workflow](/community/seps/1850-pr-based-sep-workflow)[SEP-2085: Governance Succession and Amendment Pro…](/community/seps/2085-governance-succession-and-amendment)

[github](https://github.com/modelcontextprotocol)
