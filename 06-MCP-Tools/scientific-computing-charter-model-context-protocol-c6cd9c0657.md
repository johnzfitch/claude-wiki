---
title: "Scientific Computing Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/interest-groups/scientific-computing"
category: "06-MCP-Tools"
fetched_at: "2026-09-24T06:28:05Z"
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
- [Operations](#operations)
- [Discussion Topics](#discussion-topics)
- [Changelog](#changelog)

Interest Group Charters

# Scientific Computing Charter

Copy pageCopy page

Charter for the MCP Scientific Computing Interest Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Interest Group**


[​](#mission-statement)

Mission Statement

The Scientific Computing Interest Group explores use cases for MCP in scientific and engineering workflows. The interest group gathers use cases from research and industry practitioners to understand any gaps that would warrant extension development or protocol improvements, which may lead to the formation of working groups.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Quantities, units, uncertainty**: representing physical quantities with units of measure, dimensional information, uncertainty in tool inputs and outputs, and quantity kinds, so that agents and clients can establish guardrails to enforce physical constraints
- **Reproducibility and provenance**: capturing the parameters, software and solver versions, and other inputs needed to reproduce computational results obtained through MCP
- **Arrays and numerical datasets**: conveying arrays, tensors, tabular data, and datasets that are too large for a model’s context, including how such payloads are referenced and passed to tools
- **Long-running computation**: simulations, solver runs, and batch or HPC job submission, and how they map onto MCP’s tasks architecture for asynchronous execution, progress, and cancellation mechanisms
- **Interoperability with existing scientific standards**: how MCP should relate to established domain formats, vocabularies, and ontologies rather than re-inventing them
- **Cross-domain use-case determination**: collecting requirements from physics, chemistry, biology, earth and climate science, astronomy, and engineering, and identifying recurring requirements


[​](#out-of-scope)

Out of Scope

- **Defining scientific data formats or vocabularies**: unit systems, file formats, and domain ontologies are maintained by existing standards bodies and communities; this group discusses how MCP interoperates with them, not how they should be designed
- **Building or maintaining domain MCP servers**: individual servers for a particular software package, code, or dataset are valuable inputs to the group’s use-case gathering, but building them is not protocol work
- **Authorization and identity mechanics**: OAuth flows, scopes, and token handling belong to the [Authorization IG](/community/interest-groups/auth)


[​](#related-groups)

Related Groups

- **[Agents WG](/community/working-groups/agents)**: Tasks are the foundation for the long-running simulation and job-submission workflows for high-performance computing
- **[Interceptors WG](/community/working-groups/interceptors)**: interceptors are a potential implementation path for validating correctness and normalizing units between clients and servers
- **[File Uploads WG](/community/working-groups/file-uploads)**: input datasets, mesh and geometry files, and other large files must be considered
- **[Primitive Grouping IG](/community/interest-groups/primitive-grouping)**: scientific servers often expose large, hierarchical tool surfaces that motivate organization beyond flat lists
- **[Registry WG](/community/working-groups/registry)**: publishing and discovering servers for shared scientific software and datasets intersects with registry metadata


[​](#leadership)

Leadership

| Role        | Name        | Organization | GitHub                                       | Term    |
|-------------|-------------|--------------|----------------------------------------------|---------|
| Facilitator | Cory Kinney | —            | [@corykinney](https://github.com/corykinney) | Initial |


[​](#operations)

Operations

| Meeting         | Frequency | Duration | Purpose                                |
|-----------------|-----------|----------|----------------------------------------|
| Working Session | TBD       | TBD      | Use-case sharing, technical discussion |

Open to anyone. Join the [\#scientific-computing-ig](https://discord.com/channels/1358869848138059966/1540132675174535228) channel on the [MCP Contributors Discord](/community/communication#discord).


[​](#discussion-topics)

Discussion Topics

The following themes form the IG’s initial agenda. This list is not exhaustive and will evolve as the group identifies new areas of interest.

| Item | Name                                                                                     | Status | Champion |
|------|------------------------------------------------------------------------------------------|--------|----------|
| —    | Quantities extension: units, dimensions, and semantics in tool schemas                   | Open   | —        |
| —    | Reproducibility: provenance and versioning metadata for computed results                 | Open   | —        |
| —    | Standards interoperability: relating MCP to existing scientific formats and vocabularies | Open   | —        |


[​](#changelog)

Changelog

| Date       | Change          |
|------------|-----------------|
| 2026-08-24 | Initial charter |
