---
title: "Financial Services Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/interest-groups/financial-services"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:38:06Z"
tags: ["mcp"]
---

## On this page

- [Group Type](#group-type)
- [Mission Statement](#mission-statement)
- [Scope](#scope)
  - [In Scope](#in-scope)
  - [Out of Scope](#out-of-scope)
  - [Related Groups](#related-groups)
- [Leadership](#leadership)
- [Membership](#membership)
- [Operations](#operations)
- [Discussion Topics](#discussion-topics)
- [Changelog](#changelog)

Interest Group Charters

# Financial Services Charter

Copy pageCopy page

Charter for the MCP Financial Services Interest Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Interest Group**


[​](#mission-statement)

Mission Statement

The Financial Services Interest Group brings together stakeholders from regulated financial institutions to identify where MCP needs to adapt for compliance, auditability, and risk-controlled deployment. It gathers use cases and requirements from the financial sector, develops and validates domain-specific extensions, and scopes problems with broad applicability into [SEPs](/community/sep-guidelines) or Working Groups so that innovations proven in regulated environments can benefit the wider MCP ecosystem.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Compliance and auditability**: requirements for tamper-evident, portable records of what a tool call did, under what authority, and against which policy, so that MCP interactions can satisfy regulatory audit and incident-review obligations
- **Data lineage and provenance**: source attribution, citation, and consent metadata for data surfaced through MCP, so that downstream consumers can establish where information came from and on what basis it may be used
- **Guardrails and attestation**: verification frameworks and cryptographic attestations that let a regulated institution gain assurance about server identity, tool behavior, and the integrity of responses before acting on them
- **Policy enforcement**: declarative policies for tool usage and data handling, and the points at which they are enforced, so that institutions can encode regulatory and internal-control constraints as machine-checkable rules
- **Finance-specific extensions**: developing, maintaining, and gathering implementation experience on MCP extensions that address the above in the FSIG repository, including reference implementations and conformance testing
- **Interoperability across institutions**: common patterns and standards that allow regulated institutions to interoperate without each reinventing compliance plumbing
- **SEP promotion**: identifying extensions with applicability beyond financial services and shepherding them toward the core specification with core-maintainer sponsorship
- **Regulatory liaison**: translating constraints from regulators and industry bodies into concrete technical requirements and input for other groups


[​](#out-of-scope)

Out of Scope

- **Competitively sensitive or non-public business information**: pricing, costs, margins, customer lists, market segmentation, and competitive strategy, per the [MCP Antitrust Policy](/community/antitrust)
- **General security threat modeling**: MCP-wide attack-surface analysis belongs to the [Security IG](/community/interest-groups/security). This group provides financial-sector requirements as input and consumes its threat models
- **Authorization protocol mechanics**: OAuth flows, scopes, client registration, and token handling belong to the [Authorization IG](/community/interest-groups/auth)
- **Product-specific compliance guides**: step-by-step configuration for an individual host application, cloud platform, or institution is documentation for that product rather than protocol work
- **Non-technical business discussions**: legal interpretation, procurement, and commercial terms


[​](#related-groups)

Related Groups

- **[Security IG](/community/interest-groups/security)**: attestation, auditability, and guardrails are shared concerns; the FSIG supplies regulated-deployment requirements and consumes the IG’s threat models
- **[Authorization IG](/community/interest-groups/auth)**: identity and access control for sensitive financial data sit at the boundary between the two groups
- **[Tool Annotations IG](/community/interest-groups/tool-annotations)**: trust and sensitivity annotations are directly relevant to financial tool exposure; the FSIG provides requirements as input
- **[Interceptors WG](/community/working-groups/interceptors)**: interceptors are a primary enforcement point for the policy and guardrail requirements surfaced here
- **[Registry WG](/community/working-groups/registry)**: server provenance and publishing metadata intersect with financial supply-chain and admission concerns


[​](#leadership)

Leadership

| Role        | Name                     | Organization | GitHub                                 | Term    |
|-------------|--------------------------|--------------|----------------------------------------|---------|
| Facilitator | Sambhav Kothari          | Bloomberg    | [@sambhav](https://github.com/sambhav) | Initial |
| Facilitator | Peder Holdgaard Pedersen | Saxo Bank    | [@PederHP](https://github.com/PederHP) | Initial |


[​](#membership)

Membership

| Name       | Organization | GitHub                               | Discord | Level       |
|------------|--------------|--------------------------------------|---------|-------------|
| Xin Fu     | Bloomberg    | [@imfing](https://github.com/imfing) | *TBD*   | Participant |
| Kengo Arao | Bloomberg    | [@KengoA](https://github.com/KengoA) | *TBD*   | Participant |

Open to anyone. Join the `#financial-services-ig` channel on the [MCP Contributors Discord](/community/communication#discord). Calls are open and no approval is required to attend or contribute. The group especially welcomes contributors from regulated institutions who can bring real-world deployment constraints and help drive proposals forward.


[​](#operations)

Operations

| Meeting         | Frequency     | Duration | Purpose                                                   |
|-----------------|---------------|----------|-----------------------------------------------------------|
| Working Session | Every 2 weeks | 60 min   | Use-case review, extension and proposal work, SEP scoping |

Meetings are held 16:00–17:00 London (BST/GMT). An agenda is shared in `#financial-services-ig` ahead of each call, and notes with decisions and action items are published afterwards. Discord: [\#financial-services-ig](https://discord.gg/NzkBHsrGf)


[​](#discussion-topics)

Discussion Topics

The following items form the IG’s current agenda. This list is not exhaustive and will evolve as the group identifies new areas of interest.

| Item | Name                                                                          | Status | Champion |
|------|-------------------------------------------------------------------------------|--------|----------|
| —    | Regulatory audit & attestation: portable, verifiable event/claim models       | Open   | —        |
| —    | Data lineage & citation: provenance, consent metadata, source attribution     | Open   | —        |
| —    | Guardrails & security: verification frameworks and cryptographic attestations | Open   | —        |
| —    | Policy enforcement: declarative policies for tool usage and data handling     | Open   | —        |


[​](#changelog)

Changelog

| Date       | Change          |
|------------|-----------------|
| 2026-06-25 | Initial charter |
