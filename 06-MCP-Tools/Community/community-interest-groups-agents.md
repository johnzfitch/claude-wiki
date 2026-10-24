---
title: "Agents Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/interest-groups/agents"
category: "06-MCP-Tools/Community"
fetched_at: "2026-10-21T06:29:00Z"
tags: ["agents", "mcp", "mcp-community"]
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
- [Resources](#resources)
- [Discussion Topics](#discussion-topics)
  - [Planned Outputs](#planned-outputs)
- [Changelog](#changelog)

Interest Group Charters

# Agents Charter

Copy pageCopy page

Charter for the MCP Agents Interest Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Interest Group**


[​](#mission-statement)

Mission Statement

The Agents Interest Group exists to make interactions with agent-backed systems interoperable over MCP. Today, these systems are typically exposed as ordinary tools or through framework-specific integrations, leaving durable execution, capability discovery, delegation, and multi-turn interaction to ad hoc conventions. The IG evaluates which remaining gaps require protocol support. Based on production use cases and prototypes, the group will recommend how to evolve the protocol, create additional extensions or document how existing MCP primitives should be used consistently.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Agents Extension Evaluation**: Evaluate agent-backed MCP use cases, including agent-as-tool, remote-agent, and supervisor/sub-agent patterns, to determine whether an Agents Extension is needed to complement Tasks.
- **Prototypes and Proposals**: Develop narrowly scoped proofs of concept where they help determine whether to introduce an Agents Extension, evolve Tasks, or rely on existing MCP primitives.
- **Cross-Cutting Concerns**: Coordinate with relevant groups when evaluated agent use cases raise tasks, transport, events, skills, authorization, metadata, or external-interoperability questions.
- **Documentation**: Document agent-backed MCP use cases, findings, and any recommendations produced by the group.


[​](#out-of-scope)

Out of Scope

- Building or standardizing general-purpose agent frameworks and runtimes, including internal choices about planning, memory, model selection, and orchestration. The group focuses on behavior at MCP interoperability boundaries rather than host or server implementation internals.
- Transport wire formats and session mechanics, which are owned by the Transports WG.
- Tasks, general event delivery, and callback mechanisms, which are owned by the Tasks and Events WG.

The charter does not predetermine where inference or agent loops run, or whether a particular capability belongs in Tasks, an Agents Extension, or existing MCP primitives. The IG evaluates those questions through its discussions.


[​](#related-groups)

Related Groups

- **[Transports WG](community-working-groups-transports.md)** - Task polling, multi-round-trip requests, stateless operation, and request association depend on transport and message-flow semantics.
- **[Tasks and Events WG](community-working-groups-tasks-events.md)** - Tasks and proactive task-status and completion notifications are owned by that group. The IG provides use cases and requirements as input.


[​](#leadership)

Leadership

| Role        | Name       | Organization        | GitHub                                             | Term    |
|-------------|------------|---------------------|----------------------------------------------------|---------|
| Facilitator | Luca Chang | Amazon Web Services | [@LucaButBoring](https://github.com/LucaButBoring) | Initial |


[​](#membership)

Membership

| Name       | Organization        | GitHub                                             | Discord | Level       |
|------------|---------------------|----------------------------------------------------|---------|-------------|
| Luca Chang | Amazon Web Services | [@LucaButBoring](https://github.com/LucaButBoring) |         | Facilitator |


[​](#operations)

Operations

| Meeting         | Frequency | Duration   | Purpose                                             |
|-----------------|-----------|------------|-----------------------------------------------------|
| Working Session | Weekly    | 30 minutes | Technical discussion, research, and proposal review |

Meetings are published at [meet.modelcontextprotocol.io](https://meet.modelcontextprotocol.io). Discord: `#agents-wg`


[​](#resources)

Resources

- Group repository: [modelcontextprotocol/agents-wg](https://github.com/modelcontextprotocol/agents-wg)


[​](#discussion-topics)

Discussion Topics

| Item                                           | Status      | Target Date | Champion                                                                                       |
|------------------------------------------------|-------------|-------------|------------------------------------------------------------------------------------------------|
| Agents Extension evaluation and recommendation | In Progress |             | TBD                                                                                            |
| Two-level agent definition proof of concept    | In Progress |             | [@LucaButBoring](https://github.com/LucaButBoring), [@madhaviai](https://github.com/madhaviai) |


[​](#planned-outputs)

Planned Outputs

- The group publishes an evaluation of whether an Agents Extension is needed to complement Tasks, supported by documented use cases and relevant prototype evidence.
- Based on that evaluation, the group recommends evolving Tasks, recommends an Agents Extension, or documents how existing MCP primitives are sufficient.
- Proposed agent protocol surface is evaluated through prototypes and implementation feedback before being advanced.


[​](#changelog)

Changelog

| Date       | Change                                                                        |
|------------|-------------------------------------------------------------------------------|
| 2026-08-04 | Initial charter (as the Agents WG)                                            |
| 2026-10-16 | Converted to an Interest Group. Tasks scope moved to the Tasks and Events WG. |
