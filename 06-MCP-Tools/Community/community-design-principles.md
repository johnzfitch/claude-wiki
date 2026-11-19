---
title: "Design Principles - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/design-principles"
category: "06-MCP-Tools/Community"
fetched_at: "2026-11-10T06:31:50Z"
last_modified: "Tue, 10 Nov 2026 02:17:26 GMT"
tags: ["mcp", "mcp-community"]
---

## On this page

Back to top

- [Convergence over choice](#convergence-over-choice)
- [Composability over specificity](#composability-over-specificity)
- [Interoperability over optimization](#interoperability-over-optimization)
- [Stability over velocity](#stability-over-velocity)
- [Capability over compensation](#capability-over-compensation)
- [Demonstration over deliberation](#demonstration-over-deliberation)
- [Pragmatism over purity](#pragmatism-over-purity)
- [Standardization over innovation](#standardization-over-innovation)

Contributing

# Design Principles

Copy pageCopy page

The core design principles that guide the development of the Model Context Protocol.

Copy pageCopy page

These principles guide how we evaluate protocol proposals, weigh tradeoffs, and evolve MCP. They apply to [Specification Enhancement Proposals](community-sep-guidelines.md) (SEPs) and [extensions](../Extensions/extensions-overview.md), and are distinct from the specification’s [architectural design principles](https://modelcontextprotocol.io/specification/latest/architecture#design-principles), which describe how servers and clients are built. Core Maintainers cite them when accepting or rejecting SEPs. A proposal that cuts against a principle should say so and argue why. When two principles conflict, they are weighed against each other, not ranked.


[​](#convergence-over-choice)

Convergence over choice

There should be one way to solve a problem in MCP. Rather than supporting multiple approaches that fragment the ecosystem, we choose a single well-designed path, accepting harder decisions upfront to deliver a more cohesive protocol. [Extensions](../Extensions/extensions-overview.md) are where convergence gets tested; the specification is where it gets committed.


[​](#composability-over-specificity)

Composability over specificity

MCP provides foundational primitives: resources, tools, and prompts. We don’t add protocol features for use cases that can be constructed from these existing building blocks. This keeps the surface area small and implementations simple. Extensions like [MCP Apps](../Extensions/extensions-apps-overview.md) and [Tasks](../Extensions/extensions-tasks-overview.md) capture the patterns that emerge.


[​](#interoperability-over-optimization)

Interoperability over optimization

MCP runs across clients, servers, and models of widely varying sophistication. We favor features that degrade gracefully over those that only work when every participant is equally capable. Capability negotiation makes this concrete: participants declare what they support, and the protocol adapts rather than assumes.


[​](#stability-over-velocity)

Stability over velocity

Adding to a protocol as widely adopted as MCP is easy. Removing from it is nearly impossible. Every addition is a permanent commitment and a cost for client implementers to support. We move deliberately, knowing that “no” today leaves the door open while “yes” closes it forever. We optimize for decades, not quarters. Removal, when it happens, follows [Feature Lifecycle and Deprecation](community-feature-lifecycle.md).


[​](#capability-over-compensation)

Capability over compensation

Models improve faster than protocols evolve. We avoid adding permanent structure to work around limitations that are likely temporary: the limitation fades, but the complexity remains. This is not license to ignore today’s reality. Optional context that weaker models lean on and stronger ones ignore costs nothing. But when a proposal exists primarily because current models struggle without it, we ask whether they will outgrow the need before we can shed the weight.


[​](#demonstration-over-deliberation)

Demonstration over deliberation

MCP values working implementations over theoretical debates, and evidence from real usage over hypothetical arguments. We encourage contributors to prototype rather than design by committee. A SEP needs a working [prototype](community-sep-guidelines.md#prototype-requirements) before it can be accepted.


[​](#pragmatism-over-purity)

Pragmatism over purity

MCP makes practical tradeoffs in service of adoption and usability. We don’t pursue theoretical elegance at the cost of real-world utility. When a “correct” design creates friction for implementers, we consider whether a “good enough” design better serves the ecosystem. This means accepting some inconsistency, some historical accidents, and some decisions we might make differently with hindsight.


[​](#standardization-over-innovation)

Standardization over innovation

MCP standardizes patterns that have already proven valuable. We look for conventions that work across multiple implementations and codify them, rather than inventing new paradigms and hoping they’ll be adopted. New patterns are best tried in [extensions](../Extensions/extensions-overview.md) first.
