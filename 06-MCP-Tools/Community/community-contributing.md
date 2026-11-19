---
title: "Contributing to MCP - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/community/contributing"
category: "06-MCP-Tools/Community"
fetched_at: "2026-11-13T06:32:55Z"
last_modified: "Fri, 13 Nov 2026 01:53:04 GMT"
tags: ["mcp", "mcp-community"]
---

## On this page

Back to top

- [Where to start](#where-to-start)
- [Report a problem](#report-a-problem)
- [Change the specification or docs](#change-the-specification-or-docs)
- [Work on an SDK or tool](#work-on-an-sdk-or-tool)
- [Propose a protocol change](#propose-a-protocol-change)
- [Other ways to help](#other-ways-to-help)
- [Growing your role](#growing-your-role)
- [Ground rules](#ground-rules)

Contributing

# Contributing to MCP

Copy pageCopy page

How to contribute to the Model Context Protocol specification, docs and SDKs.

Copy pageCopy page

MCP is an open source project that welcomes contributions from the community. You don’t need a change ready to get involved. You’ll find the specification, these docs and Specification Enhancement Proposals (SEPs) in the [specification repository](https://github.com/modelcontextprotocol/modelcontextprotocol). Each SDK and tool has its own repository in the [`modelcontextprotocol`](https://github.com/modelcontextprotocol) organization. To build with MCP, start with the [server](../Tutorials/develop-build-server.md) and [client](../Tutorials/develop-build-client.md) guides, the [SDK list](../General/sdk.md) or the [MCP Registry](../Registry/registry-about.md). If you want to invest some time in our discussions, the protocol work is organized in [working groups and interest groups](community-working-interest-groups.md). Their meetings are open to anyone and are listed on [meet.modelcontextprotocol.io](https://meet.modelcontextprotocol.io/). [Meetings and channels](community-working-interest-groups.md#meetings-and-channels) sets out how a meeting is announced and minuted. No invitation or role is needed to attend or speak at a meeting, to comment on a pull request, or to open an issue. These same working groups and interest groups are represented in the Discord space.


[​](#where-to-start)

Where to start

1

Join Discord

Contributors talk about the protocol on [Discord](community-communication.md#discord).

2

Find your group

Pick the [working group](community-working-interest-groups.md#current-groups) or Discord channel that covers your area. If none fits, use `#general`.To find work in the specification repository, read its [open issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues) or ask in the group’s channel what needs doing.The sections below cover each kind of change.

3

Talk to the lead

Each group’s page names its leads. Post what you want to work on in the group’s channel.

Anyone can join a group meeting, comment on a pull request or open an issue. Check the [calendar](https://meet.modelcontextprotocol.io/) and read the [Antitrust Policy](community-antitrust.md) before you attend.


[​](#report-a-problem)

Report a problem

[Report a vulnerability](community-policies.md#reporting-a-vulnerability) in private. For a bug, typo or unclear text in the specification or these docs, open an [issue](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/new/choose). For an SDK or tool, open it in that repository. Please don’t post usage questions in the repositories. We stopped taking them there because of spam.


[​](#change-the-specification-or-docs)

Change the specification or docs

Only members of the `modelcontextprotocol` GitHub organization can open pull requests on the specification repository. Membership comes from being active on issues or in working groups and interest groups. The [Member](community-contributor-ladder.md#member) role on the contributor ladder lists the requirements and who sponsors a new member. Members follow [CONTRIBUTING.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md#submitting-changes). Everyone else uses the steps below. For a small fix such as a typo, a broken link or a small specification bug, the first step is enough.

1

Raise the change

Open an issue with the [Report a bug](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/new?template=bug_report.yml) form and describe the fix. Raise anything else in the relevant working group’s channel or `#general`. A member or maintainer can pick it up from there.

2

Push a branch

To supply the change itself, push to a fork, or to a working group repository you can write to. Fixes to the specification go in `docs/specification/draft/` and fixes to the versioned guides in `docs/docs/draft/`. The dated folders hold released versions. Keep each change to one concern. [CONTRIBUTING.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md) covers setup and checks.

3

Ask for a pull request

Link the branch in that issue or channel and ask a member or maintainer to open a pull request that credits you.

A change to the protocol itself needs a [SEP](#propose-a-protocol-change).


[​](#work-on-an-sdk-or-tool)

Work on an SDK or tool

Inspector and the reference servers accept issues only.

1

Read the contributing guide

Each repository sets its own rules, and some close pull requests that have no assigned issue. If a repository has no guide, ask in its channel, such as `#python-sdk-dev`.

2

Pick an issue

Look for [`good first issue`](https://github.com/search?q=org%3Amodelcontextprotocol+is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22&type=issues) or `help wanted`, or open a new one. Ask to be assigned if the guide requires it.

3

Open a pull request

For anything larger than a small bug fix, agree on the approach in the issue before you write code.

The [SDK list](../General/sdk.md) shows each SDK’s [tier](community-sdk-tiers.md), which sets its issue triage times.


[​](#propose-a-protocol-change)

Propose a protocol change

Protocol changes go through a [SEP](community-sep-guidelines.md). Bug fixes and clarifications [do not need one](community-sep-guidelines.md#when-you-need-a-sep). A SEP needs a [sponsor](community-sep-guidelines.md#sponsors): a working group or the Core Maintainers.

1

Check the roadmap

See whether the idea fits the current focus on the [roadmap](../General/development-roadmap.md). SEPs within its priority areas get [expedited review](../General/development-roadmap.md#sep-prioritization).

2

Bring it to a working group

Raise the idea with the [working group](community-working-interest-groups.md#current-groups) that covers the area, in its channel or at a meeting. If the area belongs to an interest group, that interest group can start a working group through the [forming a group](community-working-interest-groups.md#forming-a-group) process, and that working group sponsors the SEP. The SEP pull request [must link to that discussion](community-sep-guidelines.md#workflow).

3

Draft a SEP the group sponsors

Once the group reaches consensus, write a SEP that it wants to [sponsor](community-sep-guidelines.md#sponsors). Until a group agrees to sponsor it, work in progress lives in a draft pull request. Include a prototype that meets the [Prototype Requirements](community-sep-guidelines.md#prototype-requirements), and consider shipping the idea as an [extension](../Extensions/extensions-overview.md) where its shape allows.

4

Bring it to the Core Maintainers

Follow the [workflow](community-sep-guidelines.md#workflow). By this point you should be a member of the working group and have access to open pull requests on the specification repository (see [Member](community-contributor-ladder.md#member)). If you do not have that access yet, the working group’s leads open the pull request. The SEP’s sponsor brings it to the Core Maintainers for review.


[​](#other-ways-to-help)

Other ways to help

- Review open SEPs and draft specification pull requests.
- Reproduce reported bugs.
- Test SDK release candidates against the draft specification.
- Write [conformance](https://github.com/modelcontextprotocol/conformance) scenarios. A Standards Track SEP with observable protocol behavior [needs one](community-sep-guidelines.md#conformance-test-requirement) to reach Final.


[​](#growing-your-role)

Growing your role

To take on a bigger role, see the [Contributor Ladder](community-contributor-ladder.md). [Governance](community-governance.md) covers who decides what, and [MAINTAINERS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) lists the current maintainers.


[​](#ground-rules)

Ground rules

- The [Code of Conduct](community-policies.md#code-of-conduct) applies in every repository, channel and meeting.
- [Disclose](community-policies.md#ai-assisted-contributions) any AI assistance in the pull request or issue.
- AI agents must follow [AGENTS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/AGENTS.md), which limits when they can open issues and pull requests.
- Contributions are [licensed](community-policies.md#licensing-and-intellectual-property) under Apache-2.0 for code and specifications and CC-BY-4.0 for other documentation.
