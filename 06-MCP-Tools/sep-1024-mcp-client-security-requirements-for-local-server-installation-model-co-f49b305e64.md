---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:12Z"
source_url: "https://modelcontextprotocol.io/community/seps/1024-mcp-client-security-requirements-for-local-server-"
title: "SEP-1024: MCP Client Security Requirements for Local Server Installation - Model Context Protocol"
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

SEP-1024: MCP Client Security Requirements for Local Server Installation

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
- [Client Security Requirements](#client-security-requirements)
- [Pre-Configuration Consent](#pre-configuration-consent)
- [Rationale](#rationale)
- [Design Decisions](#design-decisions)
- [Backward Compatibility](#backward-compatibility)
- [Reference Implementation](#reference-implementation)
- [Security Implications](#security-implications)
- [Security Benefits](#security-benefits)
- [Residual Risks](#residual-risks)
- [Risk Mitigation](#risk-mitigation)

Final

# SEP-1024: MCP Client Security Requirements for Local Server Installation

Copy page

MCP Client Security Requirements for Local Server Installation

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1024 |
| **Title** | MCP Client Security Requirements for Local Server Installation |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-07-22 |
| **Author(s)** | Den Delimarsky |
| **Sponsor** | None |
| **PR** | [\#1024](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1024) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP addresses critical security vulnerabilities in MCP client implementations that support one-click installation of local MCP servers. The current MCP specification lacks explicit security requirements for client-side installation flows, allowing malicious actors to execute arbitrary commands on user systems through crafted MCP server configurations distributed via links or social engineering. This proposal establishes a best practice for MCP clients, requiring explicit user consent before executing any local server installation commands and complete command transparency.

## 

[​](#motivation)

Motivation

The existing MCP specification does not address client-side security concerns related to streamlined (“one-click”) local server configuration. Current MCP clients that implement these configuration experiences create significant attack vectors:

1.  **Silent Command Execution**: MCP clients can automatically execute embedded commands without user review or consent when installing local servers via one-click flows.
2.  **Lack of Visibility**: Users have no insight into what commands are being executed on their systems, creating opportunities for data exfiltration, system compromise, and privilege escalation.
3.  **Social Engineering Vulnerabilities**: Users become comfortable executing commands labeled as “MCP servers” without proper scrutiny, making them susceptible to malicious configurations.
4.  **Arbitrary Code Execution**: Attackers can embed harmful commands in MCP server configurations and distribute them through legitimate channels (repositories, documentation, social media).

Visual Studio Code [addressed this](https://den.dev/blog/vs-code-mcp-install-consent/) by implementing consent dialogs. Similarly, Cursor also supports a consent dialog for one-click local MCP server installation. Without explicit security requirements in the specification, MCP client implementers may unknowingly create vulnerable installation flows, putting end users at risk of system compromise.

## 

[​](#specification)

Specification

### 

[​](#client-security-requirements)

Client Security Requirements

MCP clients that support one-click local MCP server configuration **MUST** implement the following security controls:

#### 

[​](#pre-configuration-consent)

Pre-Configuration Consent

Before executing any command to install or configure a local MCP server, the MCP client **MUST**:

1.  Display a clear consent dialog that shows:
    - The exact command that will be executed, without truncation
    - All arguments and parameters
    - A clear warning that this operation may be potentially dangerous
2.  Require explicit user approval through an affirmative action (button click, checkbox, etc.)
3.  Provide an option for users to cancel the installation
4.  Not proceed with installation if consent is denied or not provided

## 

[​](#rationale)

Rationale

### 

[​](#design-decisions)

Design Decisions

**Mandatory Consent Dialogs**: The requirement for explicit consent dialogs balances security with usability. While this adds friction to the MCP server configuration process, it prevents potential breaches from silent command execution.

## 

[​](#backward-compatibility)

Backward Compatibility

This SEP introduces new **requirements** for MCP client implementations but does not change the core MCP protocol or wire format. **Impact Assessment:**

- **Low Impact**: Existing MCP servers and the core protocol remain unchanged
- **Client Implementation Required**: MCP clients must update their local server installation flows to comply with new security requirements
- **User Experience Changes**: Users will see consent dialogs where none existed before

**Migration Path:**

1.  MCP clients can implement these changes in new versions without breaking existing functionality
2.  Existing installed MCP servers continue to work normally
3.  Only new installation flows require the consent mechanisms

No protocol-level backward compatibility issues exist, as this SEP addresses client behavior rather than the MCP wire protocol.

## 

[​](#reference-implementation)

Reference Implementation

N/A

## 

[​](#security-implications)

Security Implications

### 

[​](#security-benefits)

Security Benefits

This SEP directly addresses:

- **Arbitrary Code Execution**: Prevents silent execution of malicious commands
- **Social Engineering**: Forces users to consciously review commands before execution
- **Supply Chain Attacks**: Creates visibility into MCP server installation commands
- **Privilege Escalation**: Users can identify and reject commands requesting elevated privileges

### 

[​](#residual-risks)

Residual Risks

Even with these controls, risks remain:

- **User Override**: Users may approve malicious commands despite warnings
- **Sophisticated Obfuscation**: Advanced attackers may craft commands that appear legitimate
- **Implementation Gaps**: Clients may implement controls incorrectly

### 

[​](#risk-mitigation)

Risk Mitigation

These residual risks are addressed through:

- Clear warning language in consent dialogs
- Recommendation for additional security layers (sandboxing, signatures)
- Ongoing security research and community awareness

Was this page helpful?

Yes

No

[SEP-994: Shared Communication Practices/Guidelin…](/community/seps/994-shared-communication-practicesguidelines)[SEP-1034: Support default values for all primitiv…](/community/seps/1034--support-default-values-for-all-primitive-types-in)

[github](https://github.com/modelcontextprotocol)
