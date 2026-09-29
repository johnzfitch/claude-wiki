---
title: "Registry Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/working-groups/registry"
category: "06-MCP-Tools"
fetched_at: "2026-08-03T07:17:08Z"
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
- [Authority & Decision Rights](#authority-%26-decision-rights)
- [Membership](#membership)
- [Emeritus Membership](#emeritus-membership)
- [Operations](#operations)
- [Resources](#resources)
- [Deliverables & Success Metrics](#deliverables-%26-success-metrics)
  - [Active Work Items](#active-work-items)
  - [Success Criteria](#success-criteria)
- [Changelog](#changelog)

Working Group Charters

# Registry Charter

Copy pageCopy page

Charter for the MCP Registry Working Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Working Group**


[​](#mission-statement)

Mission Statement

The Registry Working Group exists to build and maintain the official MCP Registry — an open catalog and API for publicly available MCP servers — so that clients, sub-registries, and end users can discover, evaluate, and install servers with confidence. The WG owns the registry service, the `server.json` schema, the registry API specification, and the sub-registry ecosystem that further distributes server metadata.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Registry Service**: Operation, reliability, and evolution of the hosted registry at `registry.modelcontextprotocol.io`, including uptime, monitoring, and incident response.
- **Registry API Specification**: The OpenAPI spec defining how any registry (official or private) exposes server metadata.
- **`server.json` Schema**: The standardized format for describing MCP server identity, packages, runtime configuration, and capabilities — coordinated with the Server Card WG to keep Server Card a coherent subset.
- **Client SDKs**: Generated or hand-maintained client libraries that make it easy for clients and sub-registries to integrate with the registry API.
- **Publishing & Trust**: Authentication flows (GitHub OAuth, GitHub OIDC, DNS/HTTP verification), namespace ownership, moderation tooling, and community-driven flagging.
- **Adoption & Outreach**: Documentation, onboarding guides, and outreach to drive catalog coverage.
- **Issue Triage & Automation**: Labeling system, triage, and contributor workflow for the registry repo.


[​](#out-of-scope)

Out of Scope

- Any runtime-related MCP protocol specification aspects (owned by Core Maintainers and other WGs).
- Server Card format and discovery mechanism (owned by the Server Card WG; this WG coordinates on `server.json` alignment).
- Ranking/choosing between MCP server implementations on behalf of MCP clients or end-users.
- Hosting, distributing, or executing MCP server code or binaries — the registry is a metadata catalog, not a package registry.
- Any commitment to delivering an enterprise-ready or reusable registry implementation. The codebase supports this instance only and is not intended for external deployments.


[​](#related-groups)

Related Groups

- **Server Card WG** — `server.json` and Server Card must stay aligned; the registry will expose Server Cards + local package-related metadata for published entries. Tight coordination required to avoid schema divergence.


[​](#leadership)

Leadership

| Role | Name              | Organization | GitHub                                     | Term    |
|------|-------------------|--------------|--------------------------------------------|---------|
| Lead | Radoslav Dimitrov | Stacklok     | [@rdimitrov](https://github.com/rdimitrov) | Initial |


[​](#authority-&-decision-rights)

Authority & Decision Rights

| Decision Type                       | Authority Level                                        |
|-------------------------------------|--------------------------------------------------------|
| Meeting logistics & scheduling      | WG Leads (autonomous)                                  |
| Proposal prioritization within WG   | WG Leads (autonomous)                                  |
| SEP triage & closure (in scope)     | WG Leads (autonomous, with documented rationale)       |
| Technical design within scope       | WG consensus                                           |
| Spec changes (additive)             | WG consensus → Core Maintainer approval                |
| Spec changes (breaking/fundamental) | WG consensus → Core Maintainer approval + wider review |
| Scope expansion                     | Core Maintainer approval required                      |
| WG Member approval                  | WG Member sponsors                                     |


[​](#membership)

Membership

| Name               | Organization | GitHub                                           | Discord    | Level     | Maintainer? |
|--------------------|--------------|--------------------------------------------------|------------|-----------|-------------|
| Radoslav Dimitrov  | Stacklok     | [@rdimitrov](https://github.com/rdimitrov)       | dimitrovr  | Lead      | Yes         |
| Tadas Antanavicius | PulseMCP     | [@tadasant](https://github.com/tadasant)         | tadasant\_ | WG Member | Yes         |
| Bob Dickinson      | TeamSpark    | [@BobDickinson](https://github.com/BobDickinson) | rddthree   | WG Member | Yes         |
| Preeti Dewani      | Ravenmail    | [@pree-dew](https://github.com/pree-dew)         | pree_dew   | WG Member | No          |


[​](#emeritus-membership)

Emeritus Membership

| Name         | Organization | GitHub                                     | Discord   | Level     | Maintainer? |
|--------------|--------------|--------------------------------------------|-----------|-----------|-------------|
| Adam Jones   | Anthropic    | [@domdomegg](https://github.com/domdomegg) | domdomegg | WG Member | Yes         |
| Toby Padilla | GitHub       | [@toby](https://github.com/toby)           |           | WG Member | Yes         |


[​](#operations)

Operations

| Meeting         | Frequency | Duration | Purpose                                           |
|-----------------|-----------|----------|---------------------------------------------------|
| Working Session | Weekly    | 30 min   | Technical discussion, triage, and proposal review |

Discord: `#registry-dev`


[​](#resources)

Resources

- Registry service repository: [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry)


[​](#deliverables-&-success-metrics)

Deliverables & Success Metrics


[​](#active-work-items)

Active Work Items

| Item                                                                  | Status      | Target Date | Champion                                 |
|-----------------------------------------------------------------------|-------------|-------------|------------------------------------------|
| Server Card / `server.json` alignment                                 | In Progress | Q2 2026     | [@tadasant](https://github.com/tadasant) |
| Uptime & monitoring automation                                        | Planned     | Q2 2026     | TBD                                      |
| Issue triage automation & labeling system                             | Planned     | Q2 2026     | TBD                                      |
| Adoption outreach to popular server maintainers                       | Ideating    | Q3 2026     | TBD                                      |
| Cataloging specification support by clients and sub-registry products | Ideating    | Q3 2026     | TBD                                      |
| Client SDK generation / publication                                   | Ideating    | Q3 2026     | TBD                                      |
| Registry API v1 GA                                                    | Ideating    | TBD         | TBD                                      |


[​](#success-criteria)

Success Criteria

- Registry uptime ≥ 99.9% with automated monitoring and alerting.
- `server.json` schema and Server Card format aligned with no unintentional divergence.
- Majority of popular, publicly available MCP servers published to the registry.
- At least one client SDK (generated or maintained) available for registry consumers.
- Registry API v1 specification finalized and stable.
- Active sub-registry ecosystem consuming the official registry API.


[​](#changelog)

Changelog

| Date       | Change                                                                                      |
|------------|---------------------------------------------------------------------------------------------|
| 2026-07-30 | @tadasant stepped down as Lead; @rdimitrov is now sole Lead (@tadasant remains a WG Member) |
| 2026-04-08 | Initial charter                                                                             |
