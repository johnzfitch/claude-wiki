---
title: "SEP-932: Model Context Protocol Governance - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/seps/932-model-context-protocol-governance"
category: "06-MCP-Tools/SEPs"
fetched_at: "2026-08-02T05:38:23Z"
tags: ["mcp", "mcp-seps"]
---

## On this page

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

Copy pageCopy page

Model Context Protocol Governance

Copy pageCopy page

FinalProcess

This SEP has reached Final status and is preserved as a historical record of the design as accepted. Changes made to the protocol after finalization are not reflected here. Refer to the [current specification](https://modelcontextprotocol.io/specification/latest) and its changelog for authoritative requirements.

| Field         | Value                                                                          |
|---------------|--------------------------------------------------------------------------------|
| **SEP**       | 932                                                                            |
| **Title**     | Model Context Protocol Governance                                              |
| **Status**    | Final                                                                          |
| **Type**      | Process                                                                        |
| **Created**   | 2025-07-08                                                                     |
| **Author(s)** | David Soria Parra                                                              |
| **Sponsor**   | None                                                                           |
| **PR**        | [\#931](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/931) |

------------------------------------------------------------------------


[​](#abstract)

Abstract

This SEP establishes the formal governance model for the Model Context Protocol (MCP) project. It defines the organizational structure, decision-making processes, and contribution guidelines necessary for transparent and effective project stewardship. The proposal introduces a hierarchical governance structure with clear roles and responsibilities, along with the Specification Enhancement Proposal (SEP) process for managing protocol changes.


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


[​](#rationale)

Rationale

The proposed governance model draws inspiration from successful open source projects like Python, PyTorch, and Rust. Key design decisions include:


[​](#hierarchical-structure)

Hierarchical Structure

We chose a hierarchical model (Contributors → Maintainers → Core Maintainers → Lead Maintainers) that is effectively how the project decisions are made today. From there we will continue to evolve governance in the best interest of the project.


[​](#individual-vs-corporate-membership)

Individual vs Corporate Membership

Membership is explicitly tied to individuals rather than companies to:

- Ensure decisions prioritize protocol integrity over corporate interests
- Prevent capture by any single organization
- Maintain continuity when individuals change employers


[​](#sep-process)

SEP Process

The Specification Enhancement Proposal process ensures:

- All protocol changes undergo thorough review
- Community input is systematically collected
- Design decisions are documented for posterity
- Implementation precedes finalization


[​](#specification)

Specification


[​](#governance-structure)

Governance Structure


[​](#contributors)

Contributors

- Any individual who files issues, submits pull requests, or participates in discussions
- No formal membership or approval required


[​](#maintainers)

Maintainers

- Responsible for specific components (SDKs, documentation, etc.)
- Appointed by Core Maintainers
- Have write/admin access to their repositories
- May establish component-specific processes


[​](#core-maintainers)

Core Maintainers

- Deep understanding of MCP specification required
- Responsible for protocol evolution and project direction
- Meet bi-weekly for decisions
- Can veto maintainer decisions by majority vote
- Current members listed in governance documentation


[​](#lead-maintainers)

Lead Maintainers

- Justin Spahr-Summers and David Soria Parra
- Can veto any decision
- Appoint/remove Core Maintainers
- Admin access to all infrastructure


[​](#backwards-compatibility)

Backwards Compatibility

N/A


[​](#reference-implementation)

Reference Implementation

See \#931

1.  **Documentation Files**:
    - `/docs/community/governance.mdx` - Full governance documentation
    - `/docs/community/sep-guidelines.mdx` - SEP process guidelines


[​](#security-implications)

Security Implications

N/A
