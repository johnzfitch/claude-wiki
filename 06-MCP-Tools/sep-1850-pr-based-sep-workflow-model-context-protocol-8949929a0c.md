---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:14Z"
source_url: "https://modelcontextprotocol.io/community/seps/1850-pr-based-sep-workflow"
title: "SEP-1850: PR-Based SEP Workflow - Model Context Protocol"
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

SEP-1850: PR-Based SEP Workflow

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
- [1. Canonical Location](#1-canonical-location)
- [2. Author Workflow](#2-author-workflow)
- [3. Sponsor Responsibilities](#3-sponsor-responsibilities)
- [4. Review Flow](#4-review-flow)
- [5. Documentation](#5-documentation)
- [6. SEP File Structure](#6-sep-file-structure)
- [7. Status Management via PR Labels](#7-status-management-via-pr-labels)
- [8. Legacy Considerations](#8-legacy-considerations)
- [Rationale](#rationale)
- [Why File-Based?](#why-file-based)
- [Why PR Numbers?](#why-pr-numbers)
- [Why PR Labels?](#why-pr-labels)
- [Making This the Primary Process](#making-this-the-primary-process)
- [Backward Compatibility](#backward-compatibility)
- [Security Implications](#security-implications)
- [Reference Implementation](#reference-implementation)
- [Vote](#vote)

Final

# SEP-1850: PR-Based SEP Workflow

Copy page

PR-Based SEP Workflow

Copy page

FinalProcess

| Field | Value |
|----|----|
| **SEP** | 1850 |
| **Title** | PR-Based SEP Workflow |
| **Status** | Final |
| **Type** | Process |
| **Created** | 2025-11-20 |
| **Accepted** | 2025-11-28, 8 Yes, 0 No, 0 Absent per vote in Discord. |
| **Author(s)** | Nick Cooper ([@nickcoai](https://github.com/nickcoai)), David Soria Parra ([@davidsp](https://github.com/davidsp)) |
| **Sponsor** | David Soria Parra ([@davidsp](https://github.com/davidsp)) |
| **PR** | [\#1850](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1850) |

------------------------------------------------------------------------

## 

[​](#abstract)

Abstract

This SEP formalizes the pull request-based SEP workflow that stores proposals as markdown files in the `seps/` directory of the Model Context Protocol specification repository. The workflow assigns SEP numbers from pull request numbers, maintains version history in Git, and replaces the previous GitHub Issues-based process. This establishes a file-based approach as the canonical way to author, review, and accept SEPs.

## 

[​](#motivation)

Motivation

The issue-based SEP process introduced several challenges:

- **Dispersed content**: Proposal content was scattered across GitHub issues, linked documents, and pull requests, making review and archival difficult.
- **Difficult collaboration**: Maintaining long-form specifications in issue bodies made iterative edits and multi-contributor collaboration harder.
- **Limited version control**: GitHub issues don’t provide the same version control capabilities as Git-managed files.
- **Unclear status management**: The process lacked clear mechanisms for tracking status transitions and ensuring consistency between different sources of truth.

A file-based workflow addresses these issues by:

- Keeping every SEP in version control alongside the specification itself
- Providing Git’s built-in review tooling, history, and searchability
- Linking SEP numbers to pull requests to eliminate manual bookkeeping
- Surfacing all discussion in the pull request thread
- Using PR labels in conjunction with file status for better discoverability

## 

[​](#specification)

Specification

### 

[​](#1-canonical-location)

1. Canonical Location

- Every SEP lives in `seps/{NUMBER}-{slug}.md` in the specification repository
- The SEP number is always the pull request number that introduces the SEP file
- The `seps/` directory serves as the single source of truth for all SEPs

### 

[​](#2-author-workflow)

2. Author Workflow

1.  **Draft the proposal** in `seps/0000-{slug}.md` using `0000` as a placeholder number
2.  **Open a pull request** containing the draft SEP and any supporting materials
3.  **Request a sponsor** from the Maintainers list; tag potential sponsors from [MAINTAINERS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md)
4.  **After the PR number is known**, amend the commit to rename the file to `{PR-number}-{slug}.md` and update the header (`SEP-{PR-number}` and `PR: #{PR-number}`)
5.  **Wait for sponsor assignment**: Once a sponsor agrees, they will assign themselves and update the status to `Draft`

### 

[​](#3-sponsor-responsibilities)

3. Sponsor Responsibilities

A Sponsor is a Core Maintainer or Maintainer who champions the SEP through the review process. The sponsor’s responsibilities include:

- **Reviewing the proposal** and providing constructive feedback
- **Requesting changes** based on community input
- **Managing status transitions** by:
  - Ensuring that the `Status` field in the SEP markdown file is accurate
  - Applying matching PR labels to keep them in sync with the file status
  - Communicating status changes via PR comments
- **Initiating formal review** when the SEP is ready (moving from `Draft` to `In-Review`)
- **Raising to Core-Maintainers** ensuring the SEP is presented at the Core Maintainer meeting and that author and sponsor present.
- **Ensuring quality standards** are met before advancing the proposal
- **Tracking implementation** progress and ensuring reference implementations are complete before `Final` status

### 

[​](#4-review-flow)

4. Review Flow

Status progression follows: `Draft → In-Review → Accepted → Final` Additional terminal states: `Rejected`, `Withdrawn`, `Superseded`, `Dormant` **Dormant status**: If a SEP does not find a sponsor within six months, Core Maintainers may close the PR and mark the SEP as `dormant`. Reference implementations must be tracked via linked pull requests or issues and must be complete before marking a SEP as `Final`.

### 

[​](#5-documentation)

5. Documentation

- `docs/community/sep-guidelines.mdx` serves as the contributor-facing instructions
- `seps/README.md` provides the concise reference for formatting, naming, sponsor responsibilities, and acceptance criteria
- Both documents must reflect this workflow and be kept in sync

### 

[​](#6-sep-file-structure)

6. SEP File Structure

Each SEP must include:

Copy

``` shiki
# SEP-{NUMBER}: {Title}

- **Status**: Draft | In-Review | Accepted | Rejected | Withdrawn | Final | Superseded | Dormant
- **Type**: Standards Track | Informational | Process
- **Created**: YYYY-MM-DD
- **Author(s)**: Name <email> (@github-username)
- **Sponsor**: @github-username (or "None" if seeking sponsor)
- **PR**: https://github.com/modelcontextprotocol/specification/pull/{NUMBER}

## Abstract

## Motivation

## Specification

## Rationale

## Backward Compatibility

## Security Implications

## Reference Implementation
```

### 

[​](#7-status-management-via-pr-labels)

7. Status Management via PR Labels

To improve discoverability and filtering:

- Sponsors must apply PR labels that match the SEP status (`draft`, `in-review`, `accepted`, `final`, etc.)
- Both the markdown `Status` field and PR labels should be kept in sync
- The markdown file serves as the canonical record (versioned with the proposal)
- PR labels enable easy filtering and searching for SEPs by status
- Only sponsors should modify status fields and labels; authors should request changes through their sponsor

### 

[​](#8-legacy-considerations)

8. Legacy Considerations

- Contributors may optionally open a GitHub Issue for early discussion, but the authoritative SEP text lives in `seps/`
- Issues should link to the relevant file once a pull request exists
- SEP numbers are derived from PR numbers, not issue numbers

## 

[​](#rationale)

Rationale

### 

[​](#why-file-based)

Why File-Based?

Storing SEPs as files keeps authoritative specs versioned with the code, mirroring successful processes used by PEPs (Python Enhancement Proposals) and other standards bodies. This approach:

- Provides built-in version control via Git
- Enables standard code review workflows
- Maintains clear history of all changes
- Supports multi-contributor collaboration
- Integrates naturally with the specification repository

### 

[​](#why-pr-numbers)

Why PR Numbers?

Using pull request numbers:

- Eliminates race conditions around manual numbering
- Creates natural traceability between proposal and discussion
- Prevents number conflicts
- Simplifies the contribution process
- Maintains a single discussion thread for review

### 

[​](#why-pr-labels)

Why PR Labels?

Adding PR labels alongside the file status:

- Enables quick filtering of SEPs by status without opening files
- Provides immediate visibility of SEP states in PR lists
- Supports GitHub’s search and filter capabilities
- Complements the canonical markdown status field
- Reduces friction for maintainers managing multiple SEPs

### 

[​](#making-this-the-primary-process)

Making This the Primary Process

Maintaining two overlapping canonical processes risked divergence and created confusion for contributors. Establishing the file-based approach as the primary method:

- Reduces cognitive overhead for new contributors
- Ensures consistency in the SEP corpus
- Simplifies maintenance for sponsors
- Aligns with industry best practices

## 

[​](#backward-compatibility)

Backward Compatibility

- Existing issue-based SEPs remain valid and require no migration
- Historical GitHub Issue links continue to work
- Future SEPs should reference the new file locations in `seps/`
- Maintainers may optionally backfill historical SEPs into `seps/` for archival purposes

## 

[​](#security-implications)

Security Implications

No new security considerations beyond the standard code review process for pull requests.

## 

[​](#reference-implementation)

Reference Implementation

- This pull request (#1850) implements the canonical instructions in both `seps/README.md` and `docs/community/sep-guidelines.mdx`
- The process has been updated to reflect the PR-based workflow with status management via labels
- This SEP document itself serves as an example of the new format

# 

[​](#vote)

Vote

This SEP was accepted unanimously by the MCP Core Maintainers with a vote of 8 yes’s, 0 no’s and 0 absent votes on Friday December 28th, 2025 in a Discord poll.

Was this page helpful?

Yes

No

[SEP-1730: SDKs Tiering System](/community/seps/1730-sdks-tiering-system)[SEP-1865: MCP Apps - Interactive User Interfaces…](/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)

[github](https://github.com/modelcontextprotocol)
