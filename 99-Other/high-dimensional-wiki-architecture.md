---
title: "High-Dimensional Wiki Architecture"
category: "99-Other"
tags: ["authorization", "search"]
---

# High-Dimensional Wiki Architecture

Root: `/home/zack/claude-binary/mcp`

This file defines an end-to-end architecture for converting the MCP archive into a high-dimensional knowledgebase without losing information, provenance, or temporal governance.

## Purpose

The knowledgebase should answer, for any important MCP concept:

1. What matters today
2. What used to matter
3. What will matter next

It should do that while preserving:

- every original source file
- every version boundary
- every governance/proposal lineage
- every editorial synthesis decision

The core rule is:

- canonical pages reduce reading surface area
- source records preserve total information
- revision and proposal nodes preserve temporal governance

## System Model

The system is a graph-backed wiki with five primary node types:

1. `concept`
2. `source`
3. `revision`
4. `proposal`
5. `guidance`

Pages are projections of the graph, not the source of truth.

## Node Types

### `concept`

Stable thing the knowledgebase is about.

Examples:

- `authorization`
- `lifecycle`
- `registry-moderation-policy`
- `mcp-apps`

Responsibilities:

- define the enduring topic
- carry relevance and audience metadata
- connect revisions, proposals, guidance, and sources

### `source`

One original archive artifact.

Examples:

- a spec page
- a SEP page
- an archive mirror
- an internal analysis page

Responsibilities:

- preserve exact provenance
- preserve the original path and capture metadata
- remain immutable once ingested

### `revision`

A time-bound state of a concept.

Examples:

- `authorization@2025-03-26`
- `lifecycle@2025-11-25`
- `registry-moderation-policy@preview`

Responsibilities:

- preserve temporal governance
- describe how the concept changed over time
- connect to governing proposals and source records

### `proposal`

Governance or design proposal, usually a SEP.

Examples:

- `SEP-1046`
- `SEP-2133`
- `SEP-2260`

Responsibilities:

- preserve proposal identity and status
- connect governance history to current concepts
- make it explicit when a proposal is active, final, superseded, or absorbed

### `guidance`

Human-authored synthesis for readers.

Examples:

- `MCP Authorization`
- `Registry Publishing`
- `MCP Apps`

Responsibilities:

- answer `Now / Before / Next`
- recommend current least-resistance paths
- summarize old and emerging states
- link back to full provenance

## Graph Dimensions

Every important node should be positioned across these dimensions:

- `topic`
- `time`
- `authority`
- `status`
- `audience`
- `actionability`
- `impact`
- `confidence`
- `scope`

Suggested values:

- `authority`: `spec`, `sep`, `guide`, `policy`, `archive`, `analysis`
- `status`: `draft`, `final`, `active`, `historical`, `superseded`, `absorbed`
- `audience`: `builder`, `operator`, `governance`, `researcher`, `integrator`
- `actionability`: `low`, `medium`, `high`
- `impact`: `low`, `medium`, `high`
- `confidence`: `low`, `medium`, `high`
- `scope`: `core-protocol`, `registry`, `extensions`, `clients`, `integrations`, `community`

## Edge Schema

Use explicit edge types.

### Structural edges

- `has_revision`
- `has_source`
- `has_guidance`
- `has_proposal`

### Temporal edges

- `supersedes`
- `replaces`
- `obsolete_after`
- `valid_during`

### Governance edges

- `introduced_by`
- `amended_by`
- `absorbed_into`
- `governed_by`

### Meaning edges

- `explains`
- `depends_on`
- `constrains`
- `affects`
- `related_to`

### Provenance edges

- `derived_from`
- `mirrors`
- `duplicates`
- `evidence_for`

### Practical edges

- `recommended_for`
- `not_recommended_for`
- `least_resistance_path_to`

## Search Model

Search should retrieve `concepts` first, not files first.

Query flow:

1. Detect intent
2. Detect likely audience
3. Detect time horizon
4. Rank matching concepts
5. Traverse to current guidance, revisions, and evidence
6. Render answer as `Today / Before / Next`

Primary query intents:

- `understand`
- `do`
- `compare`
- `governance`
- `forecast`

Rendering contract for a good result:

- `What matters today`
- `Who does it matter to`
- `What can I do with it`
- `What can't I do with it`
- `Least-resistance path`
- `What used to matter`
- `Why it no longer matters`
- `What will matter next`
- `How much future impact it has`
- `Source trail`

## Filesystem Layout

Use a clean split between raw truth and rendered guidance.

```text
kb/
  concepts/
  revisions/
  proposals/
  guidance/
  sources/
  indexes/
  schemas/
```

Recommended structure:

```text
kb/
  concepts/
    authorization.md
    lifecycle.md
    registry-moderation-policy.md
  revisions/
    authorization/
      2025-03-26.md
      2025-06-18.md
      2025-11-25.md
    lifecycle/
      2024-11-05.md
      2025-03-26.md
      2025-06-18.md
      2025-11-25.md
  proposals/
    sep-1046.md
    sep-2133.md
    sep-2260.md
  guidance/
    authorization.md
    lifecycle.md
    registry-publishing.md
  sources/
    spec-2025-11-25-authorization.md
    sep-1046.md
    mcp-registry-authentication-2069fafb27.md
  indexes/
    topics.md
    timelines.md
    audiences.md
    least-resistance-paths.md
  schemas/
    concept.schema.md
    source.schema.md
    revision.schema.md
    proposal.schema.md
    guidance.schema.md
```

## Authoring Rules

### Rule 1

Every important MCP topic gets exactly one `concept`.

### Rule 2

Every original archive file becomes one `source`.

### Rule 3

Every meaningful dated or status-bound state becomes one `revision`.

### Rule 4

Every reader-facing synthesized page becomes one `guidance` page.

### Rule 5

Do not delete or overwrite source meaning. If content is collapsed, record the collapse through edges and provenance.

### Rule 6

If a SEP materially changes a concept, preserve the SEP as a `proposal` even if its outcome is absorbed into the spec.

### Rule 7

Canonical guidance pages must answer `Now / Before / Next` every time.

## Frontmatter Specification

### `concept` frontmatter

```yaml
id: concept:authorization
type: concept
title: Authorization
summary: How MCP authorizes access to protected servers and resources.
topics:
  - security
  - protocol
scope: core-protocol
audiences:
  - builder
  - operator
current_relevance: high
historical_relevance: high
future_relevance: high
stability: active
actionability: high
impact: high
confidence_now: high
confidence_future: medium
canonical_guidance: guidance:authorization
relations:
  has_revision:
    - revision:authorization:2025-03-26
    - revision:authorization:2025-06-18
    - revision:authorization:2025-11-25
  has_proposal:
    - proposal:sep-985
    - proposal:sep-991
    - proposal:sep-1046
  related_to:
    - concept:transports
    - concept:security-best-practices
```

### `source` frontmatter

```yaml
id: source:spec-2025-11-25-authorization
type: source
title: Authorization
source_path: /home/zack/claude-binary/mcp/spec-2025-11-25-authorization-model-context-protocol-51483c7a03.md
source_format: md
authority: spec
kind: normative
status: final
protocol_version: 2025-11-25
captured_at: 2026-03-16
is_mirror: false
mirror_of: null
source_family: spec-authorization
concepts:
  - concept:authorization
relations:
  evidence_for:
    - revision:authorization:2025-11-25
```

### `revision` frontmatter

```yaml
id: revision:authorization:2025-11-25
type: revision
concept_id: concept:authorization
title: Authorization (2025-11-25)
time_marker: 2025-11-25
authority: spec
status: final
currentness: current
impact: high
change_summary: Finalized current authorization guidance for HTTP-based transports.
relations:
  supersedes:
    - revision:authorization:2025-06-18
  governed_by:
    - proposal:sep-985
    - proposal:sep-991
    - proposal:sep-1046
  derived_from:
    - source:spec-2025-11-25-authorization
```

### `proposal` frontmatter

```yaml
id: proposal:sep-1046
type: proposal
title: SEP-1046 Support OAuth Client Credentials
proposal_number: 1046
track: authorization
status: final
authority: sep
current_relevance: medium
historical_relevance: high
future_relevance: low
relations:
  affects:
    - concept:authorization
  absorbed_into:
    - revision:authorization:2025-11-25
  derived_from:
    - source:sep-1046
```

### `guidance` frontmatter

```yaml
id: guidance:authorization
type: guidance
title: MCP Authorization
concept_id: concept:authorization
audiences:
  - builder
  - operator
canonical: true
answers:
  - now
  - before
  - next
recommended_path: Follow the current final authorization model for HTTP transports and use the latest revision as the normative source.
relations:
  summarizes:
    - concept:authorization
  derived_from:
    - revision:authorization:2025-03-26
    - revision:authorization:2025-06-18
    - revision:authorization:2025-11-25
    - proposal:sep-985
    - proposal:sep-991
    - proposal:sep-1046
```

## Guidance Page Template

Every `guidance` page should use this structure:

```text
# <Title>

## Summary

## What Matters Today
- Who does it matter to?
- What should I know?
- What can I do with it?
- What can't I do with it?
- How do I use it now?
- What's the least path of resistance?

## What Used To Matter
- What used to be true?
- Why doesn't it matter anymore?
- What replaced it?
- What breaks if someone still follows it?

## What Will Matter Next
- What is likely to change?
- How much future impact will it have?
- Who will feel it first?
- What should I prepare for now?

## Source Trail
- Revisions
- Proposals
- Source records
```

## End-to-End Example: Authorization

This is one fully modeled topic from the current archive.

### Concept

`concept:authorization`

- enduring topic
- high current relevance
- high builder/operator relevance
- tied to spec revisions and SEP lineage

### Revisions

- `revision:authorization:2025-03-26`
- `revision:authorization:2025-06-18`
- `revision:authorization:2025-11-25`

These preserve the temporal state changes.

### Proposals

- `proposal:sep-985`
- `proposal:sep-991`
- `proposal:sep-1046`

These preserve the governance and change lineage.

### Source records

Relevant sources include:

- [spec-2025-11-25-authorization-model-context-protocol-51483c7a03.md](/home/zack/claude-binary/mcp/spec-2025-11-25-authorization-model-context-protocol-51483c7a03.md)
- [spec-2025-06-18-authorization-model-context-protocol-d2811bcffa.md](/home/zack/claude-binary/mcp/spec-2025-06-18-authorization-model-context-protocol-d2811bcffa.md)
- [spec-2025-03-26-authorization-model-context-protocol-8bba414c28.md](/home/zack/claude-binary/mcp/spec-2025-03-26-authorization-model-context-protocol-8bba414c28.md)
- [understanding-authorization-in-mcp-model-context-protocol-5e9bbaa2fc.md](/home/zack/claude-binary/mcp/understanding-authorization-in-mcp-model-context-protocol-5e9bbaa2fc.md)
- [mcp-docs-tutorials-security-authorization-409c957cd5.md](/home/zack/claude-binary/mcp/mcp-docs-tutorials-security-authorization-409c957cd5.md)
- [sep-985-align-oauth-2-0-protected-resource-metadata-with-rfc-9728-model-context-a7d372ab65.md](/home/zack/claude-binary/mcp/sep-985-align-oauth-2-0-protected-resource-metadata-with-rfc-9728-model-context-a7d372ab65.md)
- [sep-991-enable-url-based-client-registration-using-oauth-client-id-metadata-docu-63243fee3b.md](/home/zack/claude-binary/mcp/sep-991-enable-url-based-client-registration-using-oauth-client-id-metadata-docu-63243fee3b.md)
- [sep-1046-support-oauth-client-credentials-flow-in-authorization-model-context-pr-cf703567ed.md](/home/zack/claude-binary/mcp/sep-1046-support-oauth-client-credentials-flow-in-authorization-model-context-pr-cf703567ed.md)

### Guidance page behavior

The final `guidance:authorization` page should answer:

- Today:
  - builders and operators should use the latest final spec revision
  - authorization is transport-level and version-sensitive
  - the least-resistance path is to follow the current final spec plus one practical guide
- Before:
  - older revision language and proposal states mattered during adoption and transition
  - those older states no longer govern current behavior after later spec absorption
- Next:
  - authorization remains high-impact because it is a moving edge where protocol, policy, and implementation constraints continue to evolve

### Result

A search for `authorization` should return:

1. the `guidance` page first
2. the current `revision` second
3. related `proposal` nodes third
4. raw `source` records as evidence

That is the intended reader experience.

## Minimal Implementation Rules

To keep this tractable:

1. Create `concept` nodes only for topics that matter to real readers.
2. Ingest every original file as a `source`.
3. Create `revision` nodes only when time or status materially changes the meaning.
4. Create `proposal` nodes for SEPs that change protocol understanding or governance.
5. Write one `guidance` page per reader-important concept.
6. Make `guidance` the only place that answers `Now / Before / Next`.

## First Build Order

If this is implemented in phases, build in this order:

1. `sources`
2. `concepts`
3. `revisions`
4. `proposals`
5. `guidance`
6. `indexes`

Recommended first concepts:

- authorization
- lifecycle
- tools
- resources
- prompts
- sampling
- registry-publishing
- registry-moderation-policy
- mcp-apps
- governance

## Final Recommendation

Treat the archive as governed source material and the wiki as a graph of understanding.

Do not optimize for:

- one file path per idea
- raw duplication removal alone
- static folder hierarchy alone

Optimize for:

- one durable concept node per topic
- one current answer per concept
- one explicit history per concept
- one future-facing signal per concept
- full source preservation underneath
