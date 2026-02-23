---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/973-expose-additional-metadata-for-implementations-res"
title: "SEP-973: Expose additional metadata for Implementations, Resources, Tools and Prompts - Model Context Protocol"
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

SEP-973: Expose additional metadata for Implementations, Resources, Tools and Prompts

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
- [Current State](#current-state)
- [Proposed State](#proposed-state)
- [Rationale](#rationale)
- [Specification](#specification)
- [Backwards Compatibility](#backwards-compatibility)
- [Security Implications](#security-implications)

Final

# SEP-973: Expose additional metadata for Implementations, Resources, Tools and Prompts

Copy page

Expose additional metadata for Implementations, Resources, Tools and Prompts

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 973 |
| **Title** | Expose additional metadata for Implementations, Resources, Tools and Prompts |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-15 |
| **Author(s)** | [@jesselumarie](https://github.com/jesselumarie) |
| **Sponsor** | None |
| **PR** | [\#973](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/973) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes adding two optional fields—`icons` and `websiteUrl`. The `icons` and `websiteUrl` would be added to the `Implementation` schema so that clients can visually identify third-party implementations and link directly to their documentation. The `icons` parameter will also be added to the `Tool`, `Resource` and `Prompt` schemas. While this can be used by both servers and clients for all implementations, we expect it to be used initially for server-provided implementations.

## 

[​](#motivation)

Motivation

### 

[​](#current-state)

Current State

Current implementations only expose namespaced metadata, forcing clients to display generic labels with no visual cues.

### 

[​](#proposed-state)

Proposed State

The proposed implementation would allow us to add visual affordances and links to documentation, making it easier to visually identify which servers/clients are providing an implementation e.g. a tool in a slash command interface:

- **Visual Affordance:** Icons make it immediately clear to users which tool or resource source is in use.
- **Discoverability:** A link to documentation (`websiteUrl`) allows clients to direct users to more information with a single click.

## 

[​](#rationale)

Rationale

This design builds on prior work in web manifests (MDN) and consolidates community feedback:

- **Consolidation of PRs:** Merges the changes from PR \#417 and PR \#862 into a single, cohesive enhancement.
- **Flexible Icon Sizes:** Supports multiple icon sizes (e.g., `48x48`, `96x96`, or `any` for vector formats) to accommodate different client UI needs.
- **Optional Fields:** By making both fields optional, existing implementations remain fully compatible.

## 

[​](#specification)

Specification

Extend the `Implementation` object as follows:

Copy

``` shiki
/**
 * A url pointing to an icon URL or a base64-encoded data URI
 *
 * Clients that support rendering icons MUST support at least the following MIME types:
 * - image/png - PNG images (safe, universal compatibility)
 * - image/jpeg (and image/jpg) - JPEG images (safe, universal compatibility)
 *
 * Clients that support rendering icons SHOULD also support:
 * - image/svg+xml - SVG images (scalable but requires security precautions)
 * - image/webp - WebP images (modern, efficient format)
 */
export interface Icon {
  /**
   * A standard URI pointing to an icon resource.
   *
   * Consumers MUST takes steps to ensure URLs serving icons are from the
   * same domain as the client/server or a trusted domain.
   *
   * Consumers MUST take appropriate precautions when consuming SVGs as they can contain
   * executable JavaScript
   *
   * @format uri
   */
  src: string;
  /** Optional override if the server’s MIME type is missing or generic. */
  mimeType?: string;
  /** e.g. "48x48", "any" (for SVG), or "48x48 96x96" */
  sizes?: string;
}

/**
 * Describes the MCP implementation
 */
export interface Implementation extends BaseMetadata {
  version: string;
  /**
   * An optional list of icons for this implementation.
   * This can be used by clients to display the implementation in a user interface.
   * Each icon should have a `kind` property that specifies whether it is a data representation or a URL source, a `src` property that points to the icon file or data representation, and may also include a `mimeType` and `sizes` property.
   * The `mimeType` property should be a valid MIME type for the icon file, such as "image/png" or "image/svg+xml".
   * The `sizes` property should be a string that specifies one or more sizes at which the icon file can be used, such as "48x48" or "any" for scalable formats like SVG.
   * The `sizes` property is optional, and if not provided, the client should assume that the icon can be used at any size.
   */
  icons?: Icon[];
  /**
   * An optional URL of the website for this implementation.
   *
   * Consumers MUST takes steps to ensure URLs serving icons are from the
   * same domain as the client/server or a trusted domain.
   *
   * Consumers MUST take appropriate precautions when consuming SVGs as they can contain
   * executable JavaScript
   *
   * @format: uri
   */
  websiteUrl?: string;
}
```

Extend the `Tool`, `Resource` and `Prompt` interfaces with the following type:

Copy

``` shiki
  /**
   * An optional list of icons for a resource.
   * This can be used by clients to display the resource's icon in a user interface.
   * Each icon should have a `kind` property that specifies whether it is a data representation or a URL source, a `src` property that points to the icon file or data representation, and may also include a `mimeType` and `sizes` property.
   * The `mimeType` property should be a valid MIME type for the icon file, such as "image/png" or "image/svg+xml".
   * The `sizes` property should be a string that specifies one or more sizes at which the icon file can be used, such as "48x48" or "any" for scalable formats like SVG.
   * The `sizes` property is optional, and if not provided, the client should assume that the icon can be used at any size.
   */
  icons?: Icon[];
```

## 

[​](#backwards-compatibility)

Backwards Compatibility

Both icons and websiteUrl are optional fields; clients that ignore them will fall back to existing behavior.

## 

[​](#security-implications)

Security Implications

This shouldn’t introduce any new security implications.

Was this page helpful?

Yes

No

[SEP-932: Model Context Protocol Governance](/community/seps/932-model-context-protocol-governance)[SEP-985: Align OAuth 2.0 Protected Resource Meta…](/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf)

[github](https://github.com/modelcontextprotocol)
