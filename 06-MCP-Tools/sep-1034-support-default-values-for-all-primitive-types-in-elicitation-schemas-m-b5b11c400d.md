---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:12Z"
source_url: "https://modelcontextprotocol.io/community/seps/1034--support-default-values-for-all-primitive-types-in"
title: "SEP-1034: Support default values for all primitive types in elicitation schemas - Model Context Protocol"
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

SEP-1034: Support default values for all primitive types in elicitation schemas

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
- [Real-World Example](#real-world-example)
- [Implementation](#implementation)
- [Specification](#specification)
- [Schema Changes](#schema-changes)
- [Behavior](#behavior)
- [Rationale](#rationale)
- [Alternatives Considered](#alternatives-considered)
- [Backwards Compatibility](#backwards-compatibility)
- [Security Implications](#security-implications)

Final

# SEP-1034: Support default values for all primitive types in elicitation schemas

Copy page

Support default values for all primitive types in elicitation schemas

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1034 |
| **Title** | Support default values for all primitive types in elicitation schemas |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-22 |
| **Author(s)** | Tapan Chugh (chugh.tapan[@gmail](https://github.com/gmail).com) |
| **Sponsor** | None |
| **PR** | [\#1034](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1034) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP recommends adding support for default values to all primitive types in the MCP elicitation schema (StringSchema, NumberSchema, and EnumSchema), extending the existing support that only covers BooleanSchema.

## 

[​](#motivation)

Motivation

Elicitations in MCP offer a way to mitigate complex API designs: tools can request information on-demand rather than resorting to convoluted parameter handling. The challenge however is that users must manually enter obvious information that could be pre-populated for more natural interactions. Currently, only `BooleanSchema` supports default values in elicitation requests. This limitation prevents servers from providing sensible defaults for text inputs, numbers, and enum selections leading to more user overhead.

### 

[​](#real-world-example)

Real-World Example

Consider implementing an email reply function. Without elicitation, the tool becomes unwieldy:

Copy

``` shiki
def reply_to_email_thread(
    thread_id: str,
    content: str,
    recipient_list: List[str] = [],
    cc_list: List[str] = []
) -> None:
    # Ambiguity: Does empty list mean "no recipients" or "use defaults"?
    # Complex logic needed to handle different combinations
```

With elicitation, the tool signature itself can be much simpler

Copy

``` shiki
def reply_to_email_thread(
    thread_id: str,
    content: Optional[str] = ""
) -> None:
    # Code can lookup the participants from the original thread
    # and prepare an elicitation request with the defaults setup
```

Copy

``` shiki
const response = await client.request("elicitation/create", {
  message: "Configure email reply",
  requestedSchema: {
    type: "object",
    properties: {
      recipients: {
        type: "string",
        title: "Recipients",
        default: "alice@company.com, bob@company.com"  // Pre-filled
      },
      cc: {
        type: "string",
        title: "CC",
        default: "john@company.com"  // Pre-filled
      },
      content: {
        type: "string",
        title: "Message"
        default: "" // If provided in the tool above
      }
    }
  }
});
```

### 

[​](#implementation)

Implementation

A working implementation demonstrating clients require minimal changes to display defaults (~10 lines of code):

- Implementation PR: [https://github.com/chughtapan/fast-agent/pull/2](https://github.com/chughtapan/fast-agent/pull/2)
- A demo with the above email reply workflow: [https://asciinema.org/a/X7aQZjT2B5jVwn9dJ9sqQVkOM](https://asciinema.org/a/X7aQZjT2B5jVwn9dJ9sqQVkOM)

## 

[​](#specification)

Specification

### 

[​](#schema-changes)

Schema Changes

Extend the elicitation primitive schemas to include optional default values:

Copy

``` shiki
export interface StringSchema {
  type: "string";
  title?: string;
  description?: string;
  minLength?: number;
  maxLength?: number;
  format?: "email" | "uri" | "date" | "date-time";
  default?: string; // NEW
}

export interface NumberSchema {
  type: "number" | "integer";
  title?: string;
  description?: string;
  minimum?: number;
  maximum?: number;
  default?: number; // NEW
}

export interface EnumSchema {
  type: "string";
  title?: string;
  description?: string;
  enum: string[];
  enumNames?: string[];
  default?: string; // NEW - must be one of enum values
}

// BooleanSchema already has default?: boolean
```

### 

[​](#behavior)

Behavior

1.  The `default` field is optional, maintaining full backward compatibility
2.  Default values must match the schema type
3.  For EnumSchema, the default must be one of the valid enum values
4.  Clients that support defaults SHOULD pre-populate form fields. Clients that don’t support defaults MAY ignore the field entirely.

## 

[​](#rationale)

Rationale

1.  The high-level rationale is to follow the precedent set by BooleanSchema rather than creating new mechanisms.
2.  Making defaults optional ensures backward compatibility.
3.  This maintains the high-level intuition of keeping the client implementation simple.

### 

[​](#alternatives-considered)

Alternatives Considered

1.  **Server-side Templates**: Servers could maintain templates separately, but this adds complexity
2.  **New Request Type**: A separate request type for forms with defaults would fragment the API
3.  **Required Defaults**: Making defaults required would break existing implementations

## 

[​](#backwards-compatibility)

Backwards Compatibility

This change is fully backward compatible with no breaking changes. Clients that don’t understand defaults will ignore them, and existing elicitation requests continue to work unchanged. Clients can adopt default support at their own pace

## 

[​](#security-implications)

Security Implications

No new security concerns:

1.  **No Sensitive Data**: The existing guidance against requesting sensitive information still applies
2.  **Client Control**: Clients retain full control over what data is sent to servers
3.  **User Visibility**: Default values are visible to users who can modify them before submission

Was this page helpful?

Yes

No

[SEP-1024: MCP Client Security Requirements for Lo…](/community/seps/1024-mcp-client-security-requirements-for-local-server-)[SEP-1036: URL Mode Elicitation for secure out-of-…](/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera)

[github](https://github.com/modelcontextprotocol)
