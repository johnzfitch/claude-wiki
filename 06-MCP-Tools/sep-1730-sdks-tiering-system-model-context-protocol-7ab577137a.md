---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:14Z"
source_url: "https://modelcontextprotocol.io/community/seps/1730-sdks-tiering-system"
title: "SEP-1730: SDKs Tiering System - Model Context Protocol"
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

SEP-1730: SDKs Tiering System

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
- [Tier Definitions](#tier-definitions)
- [Tier 1: fully supported](#tier-1-fully-supported)
- [Tier 2: commitment to be fully supported](#tier-2-commitment-to-be-fully-supported)
- [Tier 3: Experimental](#tier-3-experimental)
- [Conformance Testing](#conformance-testing)
- [Tier Advancement Process](#tier-advancement-process)
- [Tier Relegation Process](#tier-relegation-process)
- [Requirements matrix](#requirements-matrix)
- [Rationale](#rationale)
- [Why Three Tiers?](#why-three-tiers)
- [Why Time-Based Commitments?](#why-time-based-commitments)
- [Why Not Just Feature Matrices?](#why-not-just-feature-matrices)
- [Alternatives Considered](#alternatives-considered)
- [1. Feature Matrix Only](#1-feature-matrix-only)
- [2. Percentage-Based Scoring](#2-percentage-based-scoring)
- [3. Properties-Based System](#3-properties-based-system)
- [4. Latest Version Listing Only](#4-latest-version-listing-only)
- [5. No Formal System](#5-no-formal-system)
- [Backward Compatibility](#backward-compatibility)
- [Security Implications](#security-implications)
- [Implementation Plan](#implementation-plan)
- [Community Impact](#community-impact)
- [SDK Maintainers](#sdk-maintainers)
- [SDK Users](#sdk-users)
- [Ecosystem](#ecosystem)
- [References](#references)
- [Appendix](#appendix)
- [Simplified conformance tests](#simplified-conformance-tests)

Final

# SEP-1730: SDKs Tiering System

Copy page

SDKs Tiering System

Copy page

FinalStandards Track

| Field | Value |
|----|----|
| **SEP** | 1730 |
| **Title** | SDKs Tiering System |
| **Status** | Final |
| **Type** | Standards Track |
| **Created** | 2025-10-29 |
| **Author(s)** | Inna Harper, Felix Weinberger |
| **Sponsor** | None |
| **PR** | [\#1730](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1730) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP proposes a tiering system for Model Context Protocol (MCP) SDKs to establish clear expectations for feature support, maintenance commitments, and quality standards. The system defines three tiers of SDK support with objective, measurable criteria for classification.

## 

[​](#motivation)

Motivation

The MCP ecosystem needs SDK harmonization to help users make informed decisions. Users currently face challenges:

- **Feature Support Uncertainty**: No standardized way to know which SDKs support specific MCP features (OAuth, client/server/system features, like sampling, transports)
- **Maintenance Expectations**: Unclear commitment levels for bug fixes, security patches, and feature updates
- **Implementation Timelines**: No visibility into when SDKs will support new protocol versions and features

## 

[​](#specification)

Specification

### 

[​](#tier-definitions)

Tier Definitions

#### 

[​](#tier-1-fully-supported)

Tier 1: fully supported

SDKs in this tier provides full protocol implementation and is well supported **Requirements:**

- **Feature complete and full support of the protocol**
  - All conformance tests pass
  - New protocol features before the new spec version release. (There is two week window between Release Candidate and the new protocol version release)
- **SDK maintenance**
  - Acknowledge and triage issues within two business days
  - Resolve security and critical bugs within seven days
  - Stable release and SDK versioning clearly documented
- **Documentation**
  - Comprehensive documentation with examples for all features
  - Published dependency update policy

#### 

[​](#tier-2-commitment-to-be-fully-supported)

Tier 2: commitment to be fully supported

SDKs with established implementations actively working toward full protocol support. **Requirements:**

- **Feature complete and full support of the protocol**
  - 80% of conformance tests pass
  - New protocol features implemented within six months
- **SDK maintenance**
  - Active issue tracking and management
  - At least one stable release
- **Documentation**
  - Basic documentation covering core features
  - Published dependency update policy
- **Commitment to move to Tier1**
  - Published roadmap showing intent to achieve Tier 1 or, if SDK will remain in Tier 2 indefinitely, a transparent roadmap about the direction of the SDK and reasons for not being feature complete

#### 

[​](#tier-3-experimental)

Tier 3: Experimental

Early-stage or specialized SDKs exploring the protocol space. **Characteristics:**

- No feature completeness guarantees
- No stable release requirement
- May focus on specific use cases or experimental features
- No timeline commitments for updates
- Suitable for niche implementations that may remain at this tier

### 

[​](#conformance-testing)

Conformance Testing

All SDKs must undergo conformance testing using protocol trace validation: for details see [Conformance Testing RFC (forthcoming)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1627). This SEP is not focusing on Conformance testing. For the initial version of tiering, we will go with the simplified version where we would have an Example server for each SDK and run simplified conformance tests against those. **Compliance Scoring:**

- SDKs receive a percentage score based on test results
- Scores can be displayed as badges (e.g., “90% MCP Compliant”)
- Tier 1: 100% compliance required
- Tier 2: 80% compliance required
- Tier 3: No minimum requirement

### 

[​](#tier-advancement-process)

Tier Advancement Process

1.  **Self-Assessment:** Maintainers evaluate their SDK against tier criteria
2.  **Application:** Submit tier advancement request with evidence
3.  **Review:** Community review period (2 weeks)
4.  **Validation:** Automated conformance testing, github stats on issues
5.  **Decision:** Tier assignment by MCP maintainers

### 

[​](#tier-relegation-process)

Tier Relegation Process

1.  **Auto validation:**
    1.  compliance tests continuously not passing for four week for Tier 1
    2.  20% of compliance tests continuously not passing for four week for Tier 2
2.  Issues:
    1.  Issues are not addressed within two months

### 

[​](#requirements-matrix)

Requirements matrix

| Feature                                           | SDK A   | SDK B    | SDK C  |
|:--------------------------------------------------|:--------|:---------|:-------|
| **Protocol Features support (Conformance tests)** | 85%     | 60%%     | 100%   |
| **GitHub support stats**                          | 10 days | 100 days | 5 days |
| **Documentation (self reported)**                 | Good    | Minimal  | Good   |
| **Tier (computed from above)**                    | Tier 2  | Tier 3   | Tier 1 |

## 

[​](#rationale)

Rationale

### 

[​](#why-three-tiers)

Why Three Tiers?

- **Tier 1** ensures users have well supported, fully-featured SDK
- **Tier 2** provides a clear pathway for improving SDKs
- **Tier 3** allows experimentation without creating barriers to entry

### 

[​](#why-time-based-commitments)

Why Time-Based Commitments?

While the community raised concerns about rigid timelines, they provide:

- Clear expectations for users
- Measurable goals for maintainers
- Flexibility through tier progression

### 

[​](#why-not-just-feature-matrices)

Why Not Just Feature Matrices?

Feature matrices alone don’t communicate:

- Maintenance commitment
- Quality standards
- Support expectations

The tiering system combines feature support with quality guarantees.

## 

[​](#alternatives-considered)

Alternatives Considered

### 

[​](#1-feature-matrix-only)

1. Feature Matrix Only

**Rejected because:** Doesn’t communicate maintenance commitments or quality standards

### 

[​](#2-percentage-based-scoring)

2. Percentage-Based Scoring

**Rejected because:** Too granular and doesn’t capture qualitative aspects like support

### 

[​](#3-properties-based-system)

3. Properties-Based System

**Rejected because:** Multiple overlapping properties could confuse users

### 

[​](#4-latest-version-listing-only)

4. Latest Version Listing Only

**Rejected because:** Simply listing “supports MCP date” fails to capture critical information:

- Version support may be incomplete (e.g., supports \<date\> except OAuth)
- No indication of maintenance commitment or issue response times
- Lacks information about security patch timelines
- Doesn’t communicate dependency update policies
- Version numbers alone don’t indicate production readiness

### 

[​](#5-no-formal-system)

5. No Formal System

**Rejected because:** Current ad-hoc approach creates uncertainty for users

## 

[​](#backward-compatibility)

Backward Compatibility

This proposal introduces a new classification system with no breaking changes:

- Existing SDKs continue to function
- Classification is opt-in initially
- Grace period for existing SDKs to achieve tier status

## 

[​](#security-implications)

Security Implications

- Tier 1 SDKs must address security issues within 7 days
- All tiers encouraged to follow security best practices
- Conformance tests include security validation

## 

[​](#implementation-plan)

Implementation Plan

- [ ] Finalize simplified conformance test suite - Nov 4, 2025
- [ ] SDK maintainers self-assess and apply for tiers - Nov 14, 2025
- [ ] Initial tier assignments - before the November spec release
- [ ] Implement full compliance tests
- [ ] Implement automatic issue tracking analysis for SDKs

## 

[​](#community-impact)

Community Impact

### 

[​](#sdk-maintainers)

SDK Maintainers

- Clear goals for improvement
- Recognition for quality implementations
- Structured pathway for advancement

### 

[​](#sdk-users)

SDK Users

- Informed selection of SDKs
- Clear expectations for support
- Confidence in tier 1 implementations

### 

[​](#ecosystem)

Ecosystem

- Improved overall SDK quality
- Standardized feature support
- Healthy competition between implementations

## 

[​](#references)

References

- [SDK Maintainer Meeting Notes (#1648)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1648)
- [SDK Harmonization Goals (#1444)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1444)
- [Conformance Testing SEP (DRAFT)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1627)

## 

[​](#appendix)

Appendix

### 

[​](#simplified-conformance-tests)

Simplified conformance tests

While we are working on a [comprehensive proposal for conformance testing](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1627) which will take some time to implement, we want to move forward with at least some automated way to check if SDK has a full set of features. We will start from Servers features set, as we have many more servers than clients and the vast majority of developers using SDKs are Server implementers. The most straightforward approach is to have an Example Server for each SDK, similar to to [Everything Server](https://github.com/modelcontextprotocol/servers/tree/main/src/everything). Then we will have Conformance Test Client with all the test cases we want to be able to test, for example:

- execute “hello world” tool
- Get prompt
- Get completion
- Get resource template
- Receive notifications

**What is needed form SDKs maintainers:** implement everything server based on a spec. Spec will look like:

- Tool “say_hello” to return simple text
- Tool “show_image” to return and image
- Tool “tool_with_logging” to return structured output in a format \<\> and log three events: start, process, end
- Tool “tool_with_notifications” to return structured output in a format \<\> and have two notifications \<\>

Given well defined spec for the server and SDK documentation, it should be easy to implement it with the help of any coding agent. We want to check it into each SDKs repo as it will serve as an example for server implementers. Once each SDK has an Everything server, we will run the Conformance Test Client against it.

Was this page helpful?

Yes

No

[SEP-1699: Support SSE polling via server-side dis…](/community/seps/1699-support-sse-polling-via-server-side-disconnect)[SEP-1850: PR-Based SEP Workflow](/community/seps/1850-pr-based-sep-workflow)

[github](https://github.com/modelcontextprotocol)
