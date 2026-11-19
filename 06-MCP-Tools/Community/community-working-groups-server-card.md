---
title: "Server Card Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/working-groups/server-card"
category: "06-MCP-Tools/Community"
fetched_at: "2026-11-11T06:25:22Z"
last_modified: "Wed, 11 Nov 2026 01:58:02 GMT"
tags: ["mcp", "mcp-community"]
---

## On this page

Back to top

- [Group Type](#group-type)
- [Mission Statement](#mission-statement)
- [Scope](#scope)
  - [In Scope](#in-scope)
  - [Out of Scope](#out-of-scope)
  - [Related Groups](#related-groups)
- [Leadership](#leadership)
- [Authority & Decision Rights](#authority-%26-decision-rights)
- [Membership](#membership)
- [Operations](#operations)
- [Resources](#resources)
- [Deliverables & Success Metrics](#deliverables-%26-success-metrics)
  - [Active Work Items](#active-work-items)
  - [Success Criteria](#success-criteria)
- [Changelog](#changelog)

Working Groups

# Server Card Charter

Copy pageCopy page

Charter for the MCP Server Card Working Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Working Group**


[​](#mission-statement)

Mission Statement

The Server Card Working Group exists to define mechanisms that facilitate discovery and usage of MCP servers via common discovery mechanisms, and to provide guidance on how this fits into broader AI standardization efforts around discovery. Concretely, the WG will define what constitutes an MCP Server Card, the standardized document format a Server Card must follow, and how clients discover a Server Card for a given server.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Specification Work**: SEPs or extensions defining what constitutes an MCP Server Card and the specific format of the Server Card document.
- **Discovery Mechanism**: Specification of how an MCP Server Card document is discovered (well-known URL, resource-based discovery, etc.).
- **Cross-Ecosystem Coordination**: A recommendation to the [AI Card](https://github.com/Agent-Card/ai-card) effort on how to interact with MCP Server Cards.
- **Documentation**: Specification sections and guidance covering Server Card authoring and consumption.


[​](#out-of-scope)

Out of Scope

- Changes to the MCP initialization handshake or transport layer.
- A general-purpose MCP server registry or catalog (owned by the Registry WG).
- Internationalization of Server Card content until an MCP-wide i18n approach is defined.


[​](#related-groups)

Related Groups

- **Registry WG** — Server Card format should stay as close as possible to a subset of `server.json`; coordination required to avoid divergence.
- **AI Card effort** (external) — ongoing discussion on whether and how an AI Catalog can link directly to an MCP Server Card.


[​](#leadership)

Leadership

| Role | Name | Organization | GitHub | Term |
|----|----|----|----|----|
| Lead | David Soria Parra | Anthropic | [@dsp-ant](https://github.com/dsp-ant) | 6 months (ends Aug 14, 2026) |
| Lead | Sam Morrow Drums | GitHub | [@SamMorrowDrums](https://github.com/SamMorrowDrums) | 6 months (ends Aug 14, 2026) |


[​](#authority-&-decision-rights)

Authority & Decision Rights

| Decision Type | Authority Level |
|----|----|
| Meeting logistics & scheduling | WG Leads (autonomous) |
| Proposal prioritization within WG | WG Leads (autonomous) |
| SEP triage & closure (in scope) | WG Leads (autonomous, with documented rationale) |
| Technical design within scope | WG consensus |
| Spec changes (additive) | WG consensus → Core Maintainer approval |
| Spec changes (breaking/fundamental) | WG consensus → Core Maintainer approval + wider review |
| Scope expansion | Core Maintainer approval required |
| WG Member approval | WG Member sponsors |


[​](#membership)

Membership

| Name | Organization | GitHub | Discord | Level |
|----|----|----|----|----|
| David Soria Parra | Anthropic | [@dsp-ant](https://github.com/dsp-ant) |  | Lead |
| Sam Morrow Drums | GitHub | [@SamMorrowDrums](https://github.com/SamMorrowDrums) |  | Lead |
| Tadas Antanavicius |  | [@tadasant](https://github.com/tadasant) |  | WG Member |


[​](#operations)

Operations

| Meeting         | Frequency | Duration | Purpose                               |
|-----------------|-----------|----------|---------------------------------------|
| Working Session | Weekly    | 60 min   | Technical discussion, proposal review |

Discord: [\#server-card-wg](https://discord.com/channels/1358869848138059966/1399986204405141534)


[​](#resources)

Resources

- Experimental extension repository: [modelcontextprotocol/experimental-ext-server-card](https://github.com/modelcontextprotocol/experimental-ext-server-card)


[​](#deliverables-&-success-metrics)

Deliverables & Success Metrics


[​](#active-work-items)

Active Work Items

| Item | Status | Target Date | Champion |
|----|----|----|----|
| [SEP-2127: MCP Server Cards](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127) | Draft | End March | @dsp-ant |
| Reference implementation in Tier-1 SDKs | — | End April | TBD |


[​](#success-criteria)

Success Criteria

- Spec changes accepted by Core Maintainers.
- SDK implementations available.
- Real-world clients with reach implementing the proposal.
- Real-world servers with reach implementing the proposal.


[​](#changelog)

Changelog

| Date       | Change          |
|------------|-----------------|
| 2026-03-26 | Initial charter |
