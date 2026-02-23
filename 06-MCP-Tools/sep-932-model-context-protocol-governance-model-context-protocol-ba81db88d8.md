---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/932-model-context-protocol-governance"
title: "SEP-932: Model Context Protocol Governance - Model Context Protocol"
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

SEP-932: Model Context Protocol Governance

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
- [Hierarchical Structure](#hierarchical-structure)
- [Individual vs Corporate Membership](#individual-vs-corporate-membership)
- [SEP Process](#sep-process)
- [Specification](#specification)
- [Governance Structure](#governance-structure)
- [Contributors](#contributors)
- [Maintainers](#maintainers)
- [Core Maintainers](#core-maintainers)
- [Lead Maintainers](#lead-maintainers)
- [Backwards Compatibility](#backwards-compatibility)
- [Reference Implementation](#reference-implementation)
- [Security Implications](#security-implications)

Final

# SEP-932: Model Context Protocol Governance

Copy page

Model Context Protocol Governance

Copy page

FinalProcess

| Field | Value |
|----|----|
| **SEP** | 932 |
| **Title** | Model Context Protocol Governance |
| **Status** | Final |
| **Type** | Process |
| **Created** | 2025-07-08 |
| **Author(s)** | David Soria Parra |
| **Sponsor** | None |
| **PR** | [\#931](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/931) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP establishes the formal governance model for the Model Context Protocol (MCP) project. It defines the organizational structure, decision-making processes, and contribution guidelines necessary for transparent and effective project stewardship. The proposal introduces a hierarchical governance structure with clear roles and responsibilities, along with the Specification Enhancement Proposal (SEP) process for managing protocol changes.

## 

[​](#motivation)

Motivation

As the Model Context Protocol grows in adoption and complexity, the need for formal governance becomes critical. The current informal decision-making process lacks:

1.  **Transparency**: Community members have no clear visibility into how decisions are made
2.  **Participation Pathways**: Contributors lack defined ways to influence project direction
3.  **Accountability**: No formal structure exists for resolving disputes or contentious issues
4.  **Scalability**: Ad-hoc processes cannot scale with growing community and technical complexity

Without formal governance, the project risks:

- Fragmentation of the ecosystem
- Unclear or inconsistent technical decisions
- Reduced community trust and participation
- Inability to effectively manage contributions at scale

## 

[​](#rationale)

Rationale

The proposed governance model draws inspiration from successful open source projects like Python, PyTorch, and Rust. Key design decisions include:

### 

[​](#hierarchical-structure)

Hierarchical Structure

We chose a hierarchical model (Contributors → Maintainers → Core Maintainers → Lead Maintainers) that is effectively how the project decisions are made today. From there we will continue to evolve governance in the best interest of the project.

### 

[​](#individual-vs-corporate-membership)

Individual vs Corporate Membership

Membership is explicitly tied to individuals rather than companies to:

- Ensure decisions prioritize protocol integrity over corporate interests
- Prevent capture by any single organization
- Maintain continuity when individuals change employers

### 

[​](#sep-process)

SEP Process

The Specification Enhancement Proposal process ensures:

- All protocol changes undergo thorough review
- Community input is systematically collected
- Design decisions are documented for posterity
- Implementation precedes finalization

## 

[​](#specification)

Specification

### 

[​](#governance-structure)

Governance Structure

#### 

[​](#contributors)

Contributors

- Any individual who files issues, submits pull requests, or participates in discussions
- No formal membership or approval required

#### 

[​](#maintainers)

Maintainers

- Responsible for specific components (SDKs, documentation, etc.)
- Appointed by Core Maintainers
- Have write/admin access to their repositories
- May establish component-specific processes

#### 

[​](#core-maintainers)

Core Maintainers

- Deep understanding of MCP specification required
- Responsible for protocol evolution and project direction
- Meet bi-weekly for decisions
- Can veto maintainer decisions by majority vote
- Current members listed in governance documentation

#### 

[​](#lead-maintainers)

Lead Maintainers

- Justin Spahr-Summers and David Soria Parra
- Can veto any decision
- Appoint/remove Core Maintainers
- Admin access to all infrastructure

## 

[​](#backwards-compatibility)

Backwards Compatibility

N/A

## 

[​](#reference-implementation)

Reference Implementation

See \#931

1.  **Documentation Files**:
    - `/docs/community/governance.mdx` - Full governance documentation
    - `/docs/community/sep-guidelines.mdx` - SEP process guidelines

## 

[​](#security-implications)

Security Implications

N/A

Was this page helpful?

Yes

No

[SEP Index](/community/seps)[SEP-973: Expose additional metadata for Implemen…](/community/seps/973-expose-additional-metadata-for-implementations-res)

[github](https://github.com/modelcontextprotocol)
