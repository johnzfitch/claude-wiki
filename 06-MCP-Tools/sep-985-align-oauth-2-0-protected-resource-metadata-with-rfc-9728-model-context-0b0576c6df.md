---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf"
title: "SEP-985: Align OAuth 2.0 Protected Resource Metadata with RFC 9728 - Model Context Protocol"
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

SEP-985: Align OAuth 2.0 Protected Resource Metadata with RFC 9728

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
- [Rationale](#rationale)
- [Proposed State](#proposed-state)
- [Backward Compatibility](#backward-compatibility)

Final

# SEP-985: Align OAuth 2.0 Protected Resource Metadata with RFC 9728

Copy page

Align OAuth 2.0 Protected Resource Metadata with RFC 9728

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 985 |
| **Title** | Align OAuth 2.0 Protected Resource Metadata with RFC 9728 |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-16 |
| **Author(s)** | sunishsheth2009 |
| **Sponsor** | None |
| **PR** | [\#985](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/985) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This proposal brings the MCP spec’s handling of OAuth 2.0 Protected Resource Metadata in line with [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728#name-obtaining-protected-resourc). Currently, the MCP spec requires the use of the HTTP WWW-Authenticate header when returning a 401 Unauthorized to indicate the location of the protected resource metadata. However, [RFC 9728, Section 5](https://datatracker.ietf.org/doc/html/rfc9728#section-5) states: “A protected resource MAY use the WWW-Authenticate HTTP response header field, as discussed in RFC 9110, to return a URL to its protected resource metadata to the client.” This suggests that the MCP spec could be made more flexible while still maintaining RFC compliance.

## 

[​](#rationale)

Rationale

Many large-scale, dynamic, multi-tenant environments rely on a centralized authentication service separate from the backend resource servers. In such deployments, injecting WWW-Authenticate headers from backend services is non-trivial due to separation of concerns and infrastructure complexity. In these scenarios, having the option to discover metadata via a well-known URL provides a practical path forward for easier MCP adoption. Requiring only the header would impose significant communication overhead between components, especially when hundreds or thousands of MCP instances are created and destroyed dynamically. Also if there are specific managed MCP servers, adopting headers across centralized system would add significant overhead. While this increases complexity for clients—who must now implement logic to probe metadata endpoints—it reduces friction for server deployments and may encourage broader adoption. There are tradeoffs: Pros for Server Developers: Avoid complex header injection; simplifies integration in distributed environments. Cons for Client Developers: Clients must fall back to metadata discovery logic when the header is absent, increasing client complexity.

## 

[​](#proposed-state)

Proposed State

Update the MCP spec to:

Copy

``` shiki
Clients MUST interpret the WWW-Authenticate header, and fallback to probing for metadata if not present.
Servers SHOULD return the WWW-Authenticate header
```

**The reason for deviating a bit on the RFC:** Go with SHOULD over MAY for WWW-Authenticate is that it makes supporting other features, such as incremental authorization easier (e.g. you make a request for a tool, but need additional scopes, and receive a WWW-Authenticate challenge indicating the scopes). Based on the above, following the updated flow:

- Attempt the MCP request without a token.
- If a 401 Unauthorized response is received: Check for a WWW-Authenticate header. If present and includes the resource_metadata parameter, use it to locate the resource metadata.
- If the header is absent or does not include resource_metadata, fallback to requesting /.well-known/oauth-protected-resource.

This change allows more flexible deployment models without removing existing capabilities.

## 

[​](#backward-compatibility)

Backward Compatibility

This proposal is fully backward-compatible. It retains support for the WWW-Authenticate header (already in the spec) and introduces a fallback mechanism using the .well-known metadata path, which is already defined in MCP as a MUST-support location. Clients that already support metadata probing benefit from improved interoperability. Servers are not required to emit the WWW-Authenticate header if it is infeasible, but doing so is still encouraged to reduce client complexity and enable future extensibility.

Was this page helpful?

Yes

No

[SEP-973: Expose additional metadata for Implemen…](/community/seps/973-expose-additional-metadata-for-implementations-res)[SEP-986: Specify Format for Tool Names](/community/seps/986-specify-format-for-tool-names)

[github](https://github.com/modelcontextprotocol)
