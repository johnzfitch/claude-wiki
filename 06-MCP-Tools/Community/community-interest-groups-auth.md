---
title: "Authorization Charter - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/interest-groups/auth"
category: "06-MCP-Tools/Community"
fetched_at: "2026-08-26T06:27:45Z"
tags: ["authorization", "mcp", "mcp-community"]
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
  - [One channel, threads per topic](#one-channel-threads-per-topic)
  - [Agenda-driven calls](#agenda-driven-calls)
  - [From problem to SEP](#from-problem-to-sep)
- [Deliverables & Success Metrics](#deliverables-%26-success-metrics)
  - [Consolidated channels](#consolidated-channels)
- [Changelog](#changelog)

Interest Group Charters

# Authorization Charter

Copy pageCopy page

Charter for the MCP Authorization Interest Group.

Copy pageCopy page


[​](#group-type)

Group Type

**Interest Group**


[​](#mission-statement)

Mission Statement

The Authorization Interest Group is the single chartered venue for MCP authorization work. It brings MCP implementers, identity-provider vendors, and security practitioners together to surface real-world authorization problems, decide whether they are worth solving and whether they belong in MCP, and give authors a reliable place to present [SEPs](community-sep-guidelines.md), [ext-auth](https://github.com/modelcontextprotocol/ext-auth) drafts, prototypes, and deployment results for cross-topic feedback. The charter defines the scope; discussion and rough consensus happen in one channel and one recurring call, and the work products are drafts and demos rather than new standing groups.


[​](#scope)

Scope


[​](#in-scope)

In Scope

- **Deployment experience reports**: how implementers have integrated the current authorization spec (OAuth 2.1, [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728) Protected Resource Metadata, [RFC 7591](https://www.rfc-editor.org/rfc/rfc7591) Dynamic Client Registration, Client ID Metadata Documents) with real authorization servers, and where it falls short
- **Extension interoperability reports**: results of pairing independent implementations of the [ext-auth](https://github.com/modelcontextprotocol/ext-auth) extensions end to end (for example IdP, client, and authorization server through the [Enterprise-Managed Authorization](../Extensions/extensions-auth-enterprise-managed-authorization.md) ID-JAG exchange), including IdP capability gaps, workarounds, and conformance scenario input
- **Enterprise identity integration**: requirements and friction points when connecting MCP servers to enterprise IdPs (Okta, Entra ID, Ping, Keycloak, etc.), including SSO, tenant isolation, and admin consent flows
- **Delegated and agentic access**: use cases for on-behalf-of token exchange, downstream resource access, audience restriction, and consent when an MCP client acts through chains of agents or tools
- **Scope and permission granularity**: whether and how MCP servers should advertise fine-grained scopes (per-tool, per-resource) and how clients should request and present them, and authorization granularity beyond scope strings (Rich Authorization Requests, structured denials, remediation hints)
- **Credentials for non-HTTP transports**: patterns for stdio, WebSocket, and future transports where the HTTP authorization spec does not directly apply
- **Client identity and registration**: operator experience with Dynamic Client Registration, Client ID Metadata Documents, software statements, and pre-registered clients
- **Threat modelling input**: cataloguing authorization-related attack surfaces (token confusion, confused-deputy, audience mismatch, redirect handling) to inform Security Best Practices documentation
- **SEP and draft feedback**: authorization-related SEPs, ext-auth drafts, reference implementations, and demos are presented on the call and in `#auth-ig` threads for feedback before and during the [SEP process](community-sep-guidelines.md); the IG’s rough consensus is recorded in meeting notes for sponsors and Core Maintainers to draw on
- **Problem statements and requirements**: use-case catalogues and recommendations shared in `#auth-ig` threads and on SEP pull requests for consumption by SEP authors


[​](#out-of-scope)

Out of Scope

- **Accepting SEPs or extensions**: the IG gives feedback and signals support; sponsorship and acceptance follow the [SEP guidelines](community-sep-guidelines.md) and remain with Maintainers and Core Maintainers
- **Authentication of end users to MCP clients**: how a host application authenticates its own users is a host concern, not a protocol concern
- **Transport security (TLS, mTLS, certificate handling)**: belongs to the Transports WG
- **Server identity, provenance, and trust signalling**: belongs to the Server Card / Registry efforts
- **End-user product configuration walk-throughs**: the IG discusses patterns, not step-by-step setup for individual IdP products. Vendor-reported constraints on what an authorization server or IdP can or cannot implement *are* in scope as deployment experience
- **Competitively sensitive or non-public business information**, per the [MCP Antitrust Policy](community-antitrust.md)


[​](#related-groups)

Related Groups

- **[Security IG](community-interest-groups-security.md)**: token-audience confusion, issuer validation, and account-linking risks sit at the boundary between the two groups
- **[Transports WG](community-working-groups-transports.md)**: authorization is currently specified at the HTTP transport level; changes to transports affect where credentials are carried
- **Agents WG**: delegated/on-behalf-of access and consent for multi-agent chains overlap heavily with agentic use cases
- **[Server Card WG](community-working-groups-server-card.md) / [Registry](community-working-groups-registry.md)**: client and server identity, discovery metadata, and trust establishment intersect with how authorization servers and resource servers are located and verified
- **SDK Maintainers**: SDKs ship the auth client implementations; IG findings should inform cross-SDK auth ergonomics and defaults


[​](#leadership)

Leadership

| Role        | Name          | Organization | GitHub                                     | Term    |
|-------------|---------------|--------------|--------------------------------------------|---------|
| Facilitator | Aaron Parecki | Okta         | [@aaronpk](https://github.com/aaronpk)     | Initial |
| Facilitator | Darin McAdams | Amazon       | [@D-McAdams](https://github.com/D-McAdams) | Initial |
| Facilitator | Paul Carleton | Anthropic    | [@pcarleton](https://github.com/pcarleton) | Initial |


[​](#membership)

Membership

Open to anyone; no formal membership or approval step is required to join the channel, attend calls, or contribute. The group particularly seeks identity-provider vendors, MCP client and server implementers shipping authorization support, and operators integrating MCP with enterprise IdPs. Join the `#auth-ig` channel on the [MCP Contributors Discord](community-communication.md#discord) and start or join a thread for your topic. Calls are open and attendance is optional — async participation in Discord threads is equally valued.


[​](#operations)

Operations

| Meeting      | Frequency     | Duration | Purpose                                                                           |
|--------------|---------------|----------|-----------------------------------------------------------------------------------|
| Auth IG Call | Every 2 weeks | 45 min   | Agenda-driven: problem pitches, SEP and draft progress, demos, deployment reports |

Discord: [\#auth-ig](https://discord.com/channels/1358869848138059966/1360835991749001368)


[​](#one-channel-threads-per-topic)

One channel, threads per topic

All authorization discussion happens in `#auth-ig`, with one Discord thread per topic (for example a SEP number, a draft name, or a deployment pairing). There are no per-topic channels. Meeting agendas and notes live in the channel’s per-call agenda thread, with a link cross-posted to [GitHub Discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions) as the [group governance rules](community-working-interest-groups.md) require.


[​](#agenda-driven-calls)

Agenda-driven calls

The call keeps a fixed biweekly slot, but each meeting is built from its agenda:

1.  A facilitator opens an agenda thread in `#auth-ig` ahead of each call. Anyone may request a slot by replying with the topic, the ask (feedback, decision, awareness), and the time needed.
2.  Facilitators agree the agenda and hand out time slots before the call.
3.  If the agenda is thin, the call is cancelled in the thread and the slot is kept for next time.

Typical slots are a problem pitch, a progress update on a SEP or ext-auth draft, a demo of a prototype or reference implementation, or a deployment or interoperability report from implementers of a shipped extension.


[​](#from-problem-to-sep)

From problem to SEP

Two standing questions are asked of every problem pitch before anyone invests in a SEP:

- **Is this a problem worth solving?** Is there real deployment demand, and is the gap in the protocol rather than in one product?
- **Does it belong here?** Is the right home the core specification, an official extension in ext-auth, an unofficial extension, or an upstream standards body?

When the answer to both is yes, the proposer drafts a SEP or ext-auth pull request through the normal [SEP process](community-sep-guidelines.md), finds a sponsor, and returns to the call to present progress and demos as the draft matures. The IG does not charter a sub-group, channel, or meeting series per topic. Contributors who already meet separately on a topic are welcome to keep doing so, and bring outcomes back to the call as agenda slots. A separate [Working Group](community-working-interest-groups.md) can still be proposed through the standard process when a deliverable genuinely needs its own decision rights, but that is the exception rather than the default path.


[​](#deliverables-&-success-metrics)

Deliverables & Success Metrics

The IG’s outputs are the drafts and demos that pass through it: authorization SEPs and ext-auth specifications with recorded IG feedback, reference implementations and conformance scenarios, interoperability and deployment reports, and published meeting notes. The IG stewards [modelcontextprotocol/ext-auth](https://github.com/modelcontextprotocol/ext-auth), where authorization extension specifications land via PR. Success looks like authorization proposals reaching Core Maintainer review with cross-topic feedback already incorporated, and shipped extensions accumulating independent interoperable implementations.


[​](#consolidated-channels)

Consolidated channels

The following Discord channels previously hosted authorization sub-groups. They are archived (read-only) as of this re-charter and their topics continue as `#auth-ig` threads and agenda slots. The [Enterprise-Managed Authorization IG](community-interest-groups-enterprise-managed-authorization.md) is folded into this group on the same basis: EMA implementers bring interoperability and deployment progress to the call as presentation slots rather than to a standing separate group.

| Former channel                 | Topic                                                                                                                   | State at consolidation | Continues as                                              |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------|-----------------------------------------------------------|
| `#auth-wg-client-registration` | Dynamic Client Registration, Client ID Metadata Documents, software statements, pre-registration                        | Completed              | `#auth-ig` threads as needed                              |
| `#auth-wg-mixup-protection`    | Authorization-server mix-up and token-audience confusion mitigations                                                    | Completed              | `#auth-ig` threads as needed                              |
| `#auth-wg-profiles`            | Client Credentials, Enterprise-Managed Authorization, DPoP, Workload Identity Federation extensions                     | Completed              | `#auth-ig` DPoP and Workload Identity Federation threads  |
| `#auth-wg-tool-scopes`         | Per-tool scope advertisement, step-up authorization, client-side scope accumulation                                     | Active                 | `#auth-ig` thread                                         |
| `#auth-wg-fine-grained-authz`  | Rich Authorization Requests ([RFC 9396](https://www.rfc-editor.org/rfc/rfc9396)), structured denials, remediation hints | Active                 | `#auth-ig` SEP-2643 / fine-grained authorization thread   |
| `#auth-wg-improve-devx`        | Best-practices guidance and tutorials beyond the normative spec                                                         | Dormant                | `#auth-ig` threads as needed                              |
| `#enterprise-managed-auth-ig`  | EMA extension interoperability (IdP, client, authorization server)                                                      | Active                 | `#auth-ig` EMA interop thread and deployment-report slots |


[​](#changelog)

Changelog

| Date       | Change                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2026-08-17 | Re-charter: single venue and channel for authorization work; agenda-driven calls; SEP feedback in scope; `#auth-wg-*` channels and the Enterprise-Managed Authorization IG folded in |
| 2026-06-02 | Initial charter                                                                                                                                                                      |
