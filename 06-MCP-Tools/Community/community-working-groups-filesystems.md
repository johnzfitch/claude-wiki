---
title: "Filesystems Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/working-groups/filesystems"
category: "06-MCP-Tools/Community"
fetched_at: "2026-10-31T06:24:42Z"
last_modified: "Fri, 30 Oct 2026 20:34:13 GMT"
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
- [Deliverables & Success Metrics](#deliverables-%26-success-metrics)
  - [Active Work Items](#active-work-items)
  - [Success Criteria](#success-criteria)
- [Changelog](#changelog)

Working Group Charters

# Filesystems Charter

Copy pageCopy page

Charter for the MCP Filesystems Working Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Working Group**


[​](#mission-statement)

Mission Statement

The Filesystems Working Group exists to align MCP Resources with general filesystem semantics, so that MCP clients have one interface for discovering, retrieving and modifying filesystem-shaped resources across sources, and can do so efficiently. Agent platforms are converging on presenting services to models as filesystems, and Resources already addresses content by URI under a [`file://` scheme the specification defines as identifying “resources that behave like a filesystem”](../Spec/2026-07-28-server-resources.md#common-uri-schemes). The WG will determine which filesystem semantics fit MCP and produce one or more Extensions Track SEPs that apply those semantics consistently to Resources.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Specification Work**: One or more Extensions Track SEPs defining resource operations, covering:
  1.  **Scoped listing and directory traversal.** Investigate hierarchy-aware listing scoped to a URI, including an operation that enumerates one level below a URI, analogous to `readdir`, traversal of a whole subtree, and how both relate to the existing flat `resources/list` operation.
  2.  **Server-side search.** Investigate search and glob matching evaluated by the server, so a client can find content without listing and reading every resource. This goes beyond resource templates, which describe the URIs a server accepts. Together with scoped listing and traversal, this covers how a client discovers content on a server.
  3.  **Read semantics.** Investigate which filesystem read semantics fit MCP, including bulk reads of several URIs in one request and whether the protocol can support a `seek` operation.
  4.  **Write and metadata operations.** Define create, update, delete, and a metadata read (`stat`) that answers existence, size and last-modified for one URI without fetching the body.
  5.  **Optimistic concurrency control.** Specify how two writers avoid a lost update, and how a client creates a resource under a create-if-absent precondition.
  6.  **Typed errors.** Define errors for resource operations, e.g. not found, already exists, precondition failed and permission denied, so a client handles a failure the same way across servers. Currently, a missing resource returns the generic `-32602` (Invalid Params).
  7.  **Change notification and caching.** Specify how filesystem operations interact with `notifications/resources/updated`, the time-to-live and cache scope fields `ttlMs` and `cacheScope`, and the `lastModified` annotation.
- **Cross-Cutting Concerns**: Reconcile the proposals that extend this primitive into one coherent design. [SEP-2571, Resource Submission for Agent Coordination](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2571) proposes `resources/create` and `resources/delete`. [SEP-2532, Resource Streaming for Binary Content Delivery](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2532) proposes `resources/stream`. [SEP-1708, MCP Client-Brokered Filesystem Access](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1708) proposed a `files/*` method family standing beside Resources, and closed on 23 January 2026.
- **Documentation**: Document the adopted filesystem semantics in the specification, and give server authors guidance on choosing between a resource operation and a tool-based one.


[​](#out-of-scope)

Out of Scope

- A parallel `files/*` primitive standing beside Resources. The WG broadens the existing Resources primitive.
- A complete mapping of POSIX or another operating system’s filesystem API. The WG will select the semantics that fit a client-server protocol and document the rationale for any exclusions.
- Host-side sandbox and local-disk semantics. The WG standardizes the client and server wire format. How a host materializes resources into a filesystem for the model stays a host concern.
- Authorization policy for filesystem operations, beyond stating where the existing MCP authorization specification applies.


[​](#related-groups)

Related Groups

- **File Uploads WG.** Both groups transfer content to a server. Coordination is needed on where an upload-oriented flow ends and a resource write operation begins. Discovery, search, metadata and small inline writes do not depend on large-content transfer, and can progress independently of it. Tools already return resource links, so the groups should also agree on whether a tool input that takes a file can take a reference to a Resource.
- **[Skills Over MCP WG](community-working-groups-skills-over-mcp.md).** The published [Skills extension](../Extensions/extensions-skills-overview.md) uses Resources for file reads and defines optional directory reading. It does not depend on filesystem write operations; coordinate on future resource operations that affect skills.
- **Agents IG.** Multi-agent and job orchestration systems are the motivating consumers of shared filesystem semantics.


[​](#leadership)

Leadership

| Role | Name | Organization | GitHub | Term |
|----|----|----|----|----|
| Lead | Sambhav Kothari | Bloomberg | [@sambhav](https://github.com/sambhav) | Initial |
| Lead | Ola Hungerford | Nordstrom | [@olaservo](https://github.com/olaservo) | Initial |
| Lead | Daniel Temesgen | Bloomberg | [@DanielTemesgen](https://github.com/DanielTemesgen) | Initial |


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
| Michael Cheah | Bloomberg | [@michaelcheah](https://github.com/michaelcheah) |  | WG Member |


[​](#operations)

Operations

| Meeting         | Frequency | Duration   | Purpose                               |
|-----------------|-----------|------------|---------------------------------------|
| Working Session | Biweekly  | 60 minutes | Technical discussion, proposal review |

Discord: `#filesystems-wg`. **Note** The cadence above is provisional. This is subject to change once the first working session sets it.


[​](#deliverables-&-success-metrics)

Deliverables & Success Metrics


[​](#active-work-items)

Active Work Items

| Item                                     | Status   | Target Date | Champion |
|------------------------------------------|----------|-------------|----------|
| SEP: Filesystem Operations for Resources | Ideating |             | TBD      |
| Take up SEP-2571 with its author         | Ideating |             | TBD      |

The group’s first act is to take up SEP-2571 with its author, since it already covers create and delete.


[​](#success-criteria)

Success Criteria

- One or more accepted Extensions Track SEPs defining scoped listing and directory traversal, server-side search, and the supported read, write and metadata semantics, including bulk reads. The accepted work must record the WG’s conclusion on `seek`, define an optimistic concurrency control mechanism and a set of typed errors, and specify the interaction with `notifications/resources/updated`, `ttlMs`, `cacheScope` and `lastModified`.
- Each proposal in this space resolved. SEP-2571 and SEP-2532 are open at time of writing, and each should end up folded in, superseded, or explicitly scoped out.
- Reference implementations in at least two Tier 1 SDKs.
- Two independent server implementations exercising the adopted filesystem operations against a common client.


[​](#changelog)

Changelog

| Date       | Change                                                    |
|------------|-----------------------------------------------------------|
| 2026-10-27 | Add search, bulk reads and typed errors to resource scope |
| 2026-09-10 | Broaden scope to filesystem semantics                     |
| 2026-08-24 | Initial charter                                           |
