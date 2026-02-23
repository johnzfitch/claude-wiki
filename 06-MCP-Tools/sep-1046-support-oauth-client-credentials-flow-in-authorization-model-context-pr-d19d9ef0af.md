---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:13Z"
source_url: "https://modelcontextprotocol.io/community/seps/1046-support-oauth-client-credentials-flow-in-authoriza"
title: "SEP-1046: Support OAuth client credentials flow in authorization - Model Context Protocol"
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

SEP-1046: Support OAuth client credentials flow in authorization

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
- [Security Implications](#security-implications)

Final

# SEP-1046: Support OAuth client credentials flow in authorization

Copy page

Support OAuth client credentials flow in authorization

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1046 |
| **Title** | Support OAuth client credentials flow in authorization |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-23 |
| **Author(s)** | Darin McAdams ([@D-McAdams](https://github.com/D-McAdams) ) |
| **Sponsor** | None |
| **PR** | [\#1046](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1046) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

Recommends adding the OAuth client credentials flow to the authorization spec to enable machine-to-machine scenarios.

### 

[​](#motivation)

Motivation

The original authorization spec mentioned the client credentials flow, but it was dropped in subsequent revisions. Therefore, the spec is currently silent on how to solve machine-to-machine scenarios where an end-user is unavailable for interactive authorization.

### 

[​](#specification)

Specification

The authorization spec would be amended to list the OAuth client credentials flow as being allowed. Adhering to the patterns established by OAuth 2.1, the specification would RECOMMEND the use of asymmetric methods defined in RFC 753 (JWT Assertions), but also allow client secrets. As guidance to implementors, the spec overview would also be updated to describe the different flows and when each is applicable. In addition, to address a common question, the spec would be updated to indicate that implementors may implement other authorization scenarios beyond what’s defined; emphasizing that the specification defines the baseline requirements.

### 

[​](#rationale)

Rationale

To maximize interoperability (and minimize SDK complexity), this change would intentionally constrain the client credentials flow to two options:

1.  JWT Assertions as per RFC 7523 (RECOMMENDED)
2.  Client Secrets via HTTP Basic authentication (Allowed for maximum compatibility with existing systems)

Other options, such as mTLS, are not included. While the spec encourages the use of RFC 7523 (JWT Assertions), it does not yet specify how to populate the JWT contents nor how to discover the client’s JWKS URI to validate the JWT. In future iterations of the spec, it will be beneficial to do so. However, this was currently left unspecified pending maturity of other RFCs that can define these profiles. The other RFCs include [WIMSE Headless JWT Authentication](https://www.ietf.org/archive/id/draft-levy-wimse-headless-jwt-authentication-01.html) (for specifying JWT contents) and [Client ID Metadata](https://datatracker.ietf.org/doc/draft-parecki-oauth-client-id-metadata-document/) (for specifying the JWKS URI). This revision intentionally leaves extensibility for these future profiles. As a practical matter, this means implementers needing to ship solutions ASAP will most likely use client secrets which are widely supported today, whereas the JWT Assertion pattern represents the longer-term direction.

### 

[​](#backward-compatibility)

Backward Compatibility

This change is fully backward compatible. It introduces a new authorization flow, but does not alter the existing flows.

### 

[​](#security-implications)

Security Implications

The specification refers to the existing OAuth security guidance.

Was this page helpful?

Yes

No

[SEP-1036: URL Mode Elicitation for secure out-of-…](/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera)[SEP-1302: Formalize Working Groups and Interest G…](/community/seps/1302-formalize-working-groups-and-interest-groups-in-mc)

[github](https://github.com/modelcontextprotocol)
