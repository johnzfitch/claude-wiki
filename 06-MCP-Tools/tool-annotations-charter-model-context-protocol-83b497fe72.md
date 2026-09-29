---
title: "Tool Annotations Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/interest-groups/tool-annotations"
category: "06-MCP-Tools"
fetched_at: "2026-08-07T06:37:38Z"
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
  - [Active SEPs Under Discussion](#active-seps-under-discussion)
  - [Open Questions](#open-questions)
- [Resources](#resources)
- [Changelog](#changelog)

Interest Group Charters

# Tool Annotations Charter

Copy pageCopy page

Charter for the MCP Tool Annotations Interest Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Interest Group**


[​](#mission-statement)

Mission Statement

The Tool Annotations Interest Group explores the role of tool annotations in enabling safe, usable agentic systems across the MCP ecosystem. Today, six independent SEPs propose annotation changes, each solving real problems but lacking the coherent, cross-cutting perspective that a dedicated group can bring. The IG gathers use cases from server and client authors, evaluates existing and proposed annotations, and considers the long-term future of the annotation model, including whether runtime annotations, tool response annotations, and other extensions belong in the protocol.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Evaluation of existing annotations**: Assess whether the current set of tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) adequately serves server and client authors
- **Discussion of proposed annotations**: Review and provide feedback on SEPs proposing new or modified tool annotations (trust/sensitivity, agency, model preferences, and others)
- **Future of the annotation model**: Explore whether runtime annotations, tool response annotations, or structural changes to the annotation system are worth adding to the protocol
- **Use-case gathering**: Collect real-world use cases from server authors, client authors, and host applications to ground annotation decisions in practical needs
- **Problem statements and recommendations**: Produce recommendations for Working Groups or SEP authors on annotation design, coherence, and prioritization


[​](#out-of-scope)

Out of Scope

- **Binding specification changes**: The IG produces recommendations, not binding decisions; specification changes are made through the SEP process
- **Implementation work**: Building SDK features or reference implementations (may be explored in the [experimental repo](https://github.com/modelcontextprotocol/experimental-ext-tool-annotations) but is not the IG’s primary purpose)
- **Non-annotation tool changes**: Changes to tool discovery, invocation, or lifecycle that do not relate to annotations
- **Resource annotations**: While related, resource-level annotation work is tracked separately unless it directly intersects with tool annotation design


[​](#related-groups)

Related Groups

- **Security IG** - Trust and sensitivity annotations ([SEP-1913](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1913)) span both groups’ interests
- **[Skills Over MCP WG](/community/working-groups/skills-over-mcp)** - Skill-level metadata may interact with tool annotations for discovery and filtering


[​](#leadership)

Leadership

| Role        | Name           | Organization | GitHub                                               | Term    |
|-------------|----------------|--------------|------------------------------------------------------|---------|
| Facilitator | Sam Morrow     | GitHub       | [@SamMorrowDrums](https://github.com/SamMorrowDrums) | Initial |
| Facilitator | Robert Reichel | OpenAI       | [@rreichel3](https://github.com/rreichel3)           | Initial |


[​](#membership)

Membership

| Name                    | Organization | GitHub                                               | Discord  | Level       |
|-------------------------|--------------|------------------------------------------------------|----------|-------------|
| Sam Morrow              | GitHub       | [@SamMorrowDrums](https://github.com/SamMorrowDrums) |          | Facilitator |
| Robert Reichel          | OpenAI       | [@rreichel3](https://github.com/rreichel3)           |          | Facilitator |
| Matt Carey              | Cloudflare   | [@mattzcarey](https://github.com/mattzcarey)         |          | Participant |
| Kapil Sharma            | Microsoft    | [@kapil8811](https://github.com/kapil8811)           |          | Participant |
| Connor Peet             | Microsoft    | [@connor4312](https://github.com/connor4312)         |          | Participant |
| Ola Hungerford          | Nordstrom    | [@olaservo](https://github.com/olaservo)             |          | Participant |
| Gökhan Arkan            | GitHub       | [@gokhanarkan](https://github.com/gokhanarkan)       |          | Participant |
| Joanna Krzek-Lubowiecka | GitHub       | [@joannakl](https://github.com/joannakl)             |          | Participant |
| Maxi Boch               | Independent  | [@maxiboch](https://github.com/maxiboch)             | maxiboch | Participant |


[​](#operations)

Operations

| Meeting    | Frequency | Duration | Purpose                                       |
|------------|-----------|----------|-----------------------------------------------|
| Discussion | TBD       | TBD      | Use-case sharing, annotation review, open Q&A |

Discord: [\#tool-annotations-ig](https://discord.com/channels/1358869848138059966/1482836798517543073)


[​](#discussion-topics)

Discussion Topics

The following SEPs and themes form the IG’s initial discussion agenda. This list is not exhaustive and will evolve as the group identifies new areas of interest.


[​](#active-seps-under-discussion)

Active SEPs Under Discussion

| SEP                                                                                | Title                              | Status | Author                                                                                           |
|------------------------------------------------------------------------------------|------------------------------------|--------|--------------------------------------------------------------------------------------------------|
| [SEP-1862](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1862) | Tool Resolution (preflight checks) | Draft  | [@SamMorrowDrums](https://github.com/SamMorrowDrums)                                             |
| [SEP-1913](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1913) | Trust and Sensitivity Annotations  | Draft  | [@SamMorrowDrums](https://github.com/SamMorrowDrums), [@rreichel3](https://github.com/rreichel3) |
| [SEP-1984](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1984) | Comprehensive Tool Annotations     | Draft  | [@sambhav](https://github.com/sambhav)                                                           |
| [SEP-2417](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2417) | Model Preferences for Tools        | Draft  | [@ProductOfAmerica](https://github.com/ProductOfAmerica)                                         |


[​](#open-questions)

Open Questions

- Should runtime annotations (annotations that change between invocations) be added to the protocol?
- Are additional static annotations worth standardizing, and which serve both server and client authors?
- Should tool *response* annotations be added to the protocol?
- How should annotations interact with trust, security, and human-in-the-loop requirements?
- What is the right level of granularity - a few well-defined hints vs. a richer, extensible vocabulary?


[​](#resources)

Resources

- [Tool Annotations as Risk Vocabulary](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/) - blog post framing the motivation for this work
- [Experimental repo](https://github.com/modelcontextprotocol/experimental-ext-tool-annotations) - repository for the Tool Annotations Interest Group


[​](#changelog)

Changelog

| Date       | Change          |
|------------|-----------------|
| 2026-04-20 | Initial charter |
