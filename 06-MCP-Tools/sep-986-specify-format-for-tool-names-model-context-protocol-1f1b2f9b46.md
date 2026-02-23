---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/986-specify-format-for-tool-names"
title: "SEP-986: Specify Format for Tool Names - Model Context Protocol"
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

SEP-986: Specify Format for Tool Names

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
- [Rationale](#rationale)
- [Specification](#specification)
- [Backwards Compatibility](#backwards-compatibility)
- [Reference Implementation](#reference-implementation)
- [Security Implications](#security-implications)

Final

# SEP-986: Specify Format for Tool Names

Copy page

Specify Format for Tool Names

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 986 |
| **Title** | Specify Format for Tool Names |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-16 |
| **Author(s)** | kentcdodds |
| **Sponsor** | None |
| **PR** | [\#986](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/986) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

The Model Context Protocol (MCP) currently lacks a standardized format for tool names, resulting in inconsistencies and confusion for both implementers and users. This SEP proposes a clear, flexible standard for tool names: tool names should be 1–64 characters, case-sensitive, and may include alphanumeric characters, underscores (\_), dashes (-), dots (.), and forward slashes (/). This aims to maximize compatibility, clarity, and interoperability across MCP implementations while accommodating a wide range of naming conventions.

## 

[​](#motivation)

Motivation

Without a prescribed format for tool names, MCP implementations have adopted a variety of naming conventions, including different separators, casing, and character sets. This inconsistency can lead to confusion, errors in tool invocation, and difficulties in documentation and automation. Standardizing the allowed characters and length will:

- Make tool names predictable and interoperable across clients.
- Allow for hierarchical and namespaced tool names (e.g., using / and .).
- Support both human-readable and machine-generated names.
- Avoid unnecessary restrictions that could block valid use cases.

## 

[​](#rationale)

Rationale

Community discussion highlighted the need for flexibility in tool naming. While some conventions (like lower-kebab-case) are common, many tools and clients use uppercase, underscores, dots, and slashes for namespacing or clarity. The proposed pattern—allowing a-z, A-Z, 0-9, \_, -, ., and /—is based on patterns used in major clients (e.g., VS Code, Claude) and aligns with common conventions in programming and APIs. Restricting spaces and commas avoids parsing issues and ambiguity. The length limit (1–64) is generous enough for most use cases but prevents abuse.

## 

[​](#specification)

Specification

- Tool names SHOULD be between 1 and 64 characters in length (inclusive).
- Tool names are case-sensitive.
- Allowed characters: uppercase and lowercase ASCII letters (A-Z, a-z), digits (0-9), underscore (\_), dash (-), dot (.), and forward slash (/).
- Tool names SHOULD NOT contain spaces, commas, or other special characters.
- Tool names SHOULD be unique within their namespace.
- Example valid tool names:
  - getUser
  - user-profile/update
  - DATA_EXPORT_v2
  - admin.tools.list

## 

[​](#backwards-compatibility)

Backwards Compatibility

This change is not backwards compatible for existing tools that use disallowed characters or exceed the new length limits. To minimize disruption:

- Existing non-conforming tool names SHOULD be supported as aliases for at least one major version, with a deprecation warning.
- Tool authors SHOULD update their documentation and code to use the new format.
- A migration guide SHOULD be provided to assist implementers in updating their tool names.

## 

[​](#reference-implementation)

Reference Implementation

A reference implementation can be provided by updating the MCP core library to enforce the new tool name validation rules at registration time. Existing tools can be updated to provide aliases for their new conforming names, with warnings for deprecated formats. Example code and migration scripts can be included in the MCP repository.

## 

[​](#security-implications)

Security Implications

None. Standardizing tool name format does not introduce new security risks.

Was this page helpful?

Yes

No

[SEP-985: Align OAuth 2.0 Protected Resource Meta…](/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf)[SEP-990: Enable enterprise IdP policy controls d…](/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o)

[github](https://github.com/modelcontextprotocol)
