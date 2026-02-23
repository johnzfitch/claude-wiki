---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:15Z"
source_url: "https://modelcontextprotocol.io/community/seps/2085-governance-succession-and-amendment"
title: "SEP-2085: Governance Succession and Amendment Procedures - Model Context Protocol"
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

SEP-2085: Governance Succession and Amendment Procedures

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
- [Succession](#succession)
- [Amendment](#amendment)
- [Rationale](#rationale)
- [Succession Process Design](#succession-process-design)
- [Amendment Process Design](#amendment-process-design)
- [Alternatives Considered](#alternatives-considered)
- [Backward Compatibility](#backward-compatibility)
- [Security Implications](#security-implications)
- [Reference Implementation](#reference-implementation)

Final

# SEP-2085: Governance Succession and Amendment Procedures

Copy page

Governance Succession and Amendment Procedures

Copy page

FinalProcess

| Field | Value |
|----|----|
| **SEP** | 2085 |
| **Title** | Governance Succession and Amendment Procedures |
| **Status** | Final |
| **Type** | Process |
| **Created** | 2025-12-05 |
| **Author(s)** | David Soria Parra ([@dsp-ant](https://github.com/dsp-ant)) |
| **Sponsor** | David Soria Parra ([@dsp-ant](https://github.com/dsp-ant)) |
| **PR** | [\#2085](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2085) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP establishes formal procedures for Lead Maintainer succession and governance amendment within the Model Context Protocol project. It defines clear processes for leadership transitions when a Lead Maintainer leaves their role and establishes requirements for proposing and approving changes to the governance structure itself.

## 

[​](#motivation)

Motivation

The current MCP governance structure defines roles and responsibilities but lacks explicit procedures for two critical scenarios:

1.  **Leadership Succession**: The governance document identifies Justin Spahr-Summers and David Soria Parra as Lead Maintainers (BDFLs) but does not specify what happens if one or both leave their roles. Without a defined succession process, an unexpected departure could create uncertainty about project leadership and decision-making authority.
2.  **Governance Evolution**: As the MCP project grows and the community evolves, the governance structure may need to adapt. Currently, there is no defined process for how the governance document itself can be amended, which could lead to ad-hoc changes without proper community input or unclear authority for making such changes.

Establishing these procedures now, while the project leadership is stable, ensures continuity and provides clear guidance for future scenarios.

## 

[​](#specification)

Specification

The following sections shall be added to the MCP Governance document.

### 

[​](#succession)

Succession

If a Lead Maintainer leaves their role for any reason, the succession process begins upon their written notice or, if unable to provide notice, upon a determination by the remaining Lead Maintainer(s) or Core Maintainers that the Lead Maintainer is unable to continue serving. If one or more Lead Maintainer(s) remain, they shall appoint a successor (by majority vote if multiple), and the remaining Lead Maintainer(s) will continue to govern until a successor is appointed. If no Lead Maintainers remain, the Core Maintainers shall appoint a successor by majority vote within 30 days, and the project operates by two-thirds vote of Core Maintainers until a new Lead Maintainer is appointed.

### 

[​](#amendment)

Amendment

Amendments to this governance structure may only be proposed by Lead Maintainers. Any proposed amendment must be approved by a two-thirds (2/3) majority of all Core Maintainers to take effect. Amendment proposals shall:

1.  Be submitted in writing with clear rationale for the proposed change
2.  Include specific language describing the modification to existing governance provisions
3.  Allow for a minimum comment period of five (5) days before voting
4.  Be decided by recorded vote of Core Maintainers

## 

[​](#rationale)

Rationale

### 

[​](#succession-process-design)

Succession Process Design

The succession process is designed with several principles in mind:

- **Continuity**: Remaining Lead Maintainers can continue operating and appoint successors without disruption to project governance.
- **Fallback Authority**: If all Lead Maintainers depart, Core Maintainers have clear authority to select new leadership, preventing a governance vacuum.
- **Time-Bound Process**: The 30-day requirement ensures succession happens promptly while allowing adequate time for deliberation.
- **Supermajority Interim Governance**: Two-thirds voting during interregnum periods ensures major decisions have broad support during transitional periods.

### 

[​](#amendment-process-design)

Amendment Process Design

The amendment process balances stability with adaptability:

- **Lead Maintainer Proposal Authority**: Limiting proposal authority to Lead Maintainers prevents governance churn from frequent amendment proposals while ensuring those with deepest project investment can drive necessary changes.
- **Core Maintainer Approval**: Requiring two-thirds Core Maintainer approval ensures amendments have broad support from those actively governing the project.
- **Comment Period**: The five-day minimum comment period allows affected parties to review and provide input before voting.
- **Recorded Votes**: Transparency in voting ensures accountability and provides a historical record of governance decisions.

### 

[​](#alternatives-considered)

Alternatives Considered

**Succession by Election**: An open election process was considered but rejected as potentially disruptive and slow during critical transition periods. The current proposal allows for quick succession while maintaining checks through the existing maintainer structure. **Amendment by Any Maintainer**: Allowing any maintainer to propose amendments was considered but could lead to governance instability. The current approach balances stability with the ability to evolve. **Longer Comment Periods**: Longer comment periods (e.g., 30 days) were considered but deemed excessive for a project that already has regular bi-weekly Core Maintainer meetings. Five days allows for at least one meeting cycle while enabling timely decisions.

## 

[​](#backward-compatibility)

Backward Compatibility

This SEP adds new procedures without modifying existing governance structures. No backward compatibility concerns exist.

## 

[​](#security-implications)

Security Implications

This SEP has no direct security implications. However, clear succession procedures indirectly support security by ensuring continuous responsible stewardship of the project, including security-related decisions.

## 

[​](#reference-implementation)

Reference Implementation

Upon acceptance, this SEP will be implemented by adding the Succession and Amendment sections to `docs/community/governance.mdx`. The new sections will be inserted after the “Lead Maintainers (BDFL)” section and before the “Decision Process” section. A draft pull request implementing these changes will be linked here once available.

Was this page helpful?

Yes

No

[SEP-1865: MCP Apps - Interactive User Interfaces…](/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)[SEP-2133: Extensions](/community/seps/2133-extensions)

[github](https://github.com/modelcontextprotocol)
