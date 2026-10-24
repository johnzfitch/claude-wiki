---
title: "Restrict web search and web fetch domains - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:28:16Z"
tags: ["agents", "api", "search"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Ftools-web-restrictions)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Define your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Restrict web search and web fetch domains

Copy page



Control which sites an agent's web search and web fetch tools can reach, cap fetched content, and localize search results.

Copy page



To control which sites the agent's web tools can reach, set a domain list on the `web_search` and `web_fetch` entries of the [agent toolset](managed-agents-tools.md#configuring-the-toolset). Each of these `configs` entries takes one of two lists:

- **`allowed_domains`:** The tool can reach only these hosts.
- **`blocked_domains`:** The tool can never reach these hosts.

Each tool carries its own list, so `web_search` and `web_fetch` can have different restrictions.



`web_search` and `web_fetch` run on Anthropic's servers, not in the sandbox. A cloud environment with `limited` [networking](managed-agents-environments.md#networking) also applies its `allowed_hosts` to them; see [Set domain lists on an agent](#set-domain-lists-on-an-agent). `unrestricted` networking and self-hosted environments do not limit them. The per-tool lists restrict these tools further.

Your organization's web search settings on the [**Capabilities**](playground.md) page of the Claude Console also apply to `web_search` in a session. If an administrator disables web search, `web_search` calls return an error result to the agent, and the session continues. If the organization restricts web search domains, the agent receives only the search results that both the organization's domain restrictions and the agent's per-tool lists allow.

Your organization's web fetch settings on the same page also apply to `web_fetch` in a session. If an administrator turns off web fetch, `web_fetch` calls return an error result to the agent, and the session continues. If the organization sets allowed or blocked domains for web fetch, a URL must pass the organization's list and the agent's per-tool lists, and so must any URL a redirect leads to. A `web_fetch` call for a URL that any of them excludes also returns an error result to the agent.

## Set domain lists on an agent

The following example creates an agent that limits `web_search` to two sites and blocks one host for `web_fetch`. It also sets `user_location` and `max_content_tokens`, which [Settings](#settings) describes. The response echoes the `configs` array.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

CLI



```python
ant apply agent.md
```

agent.md





```python
---
name: Research Agent
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
    configs:
      - type: web_search
        name: web_search
        allowed_domains: [docs.example.com, arxiv.org]
        user_location:
          type: approximate
          country: US
          timezone: America/Los_Angeles
      - type: web_fetch
        name: web_fetch
        blocked_domains: [ads.example.com]
        max_content_tokens: 50000
---
```

[`ant apply`](cli-sdks-libraries-cli-apply.md) creates the agent and prints its ID, not the `configs` array.

In a cloud environment with `limited` [networking](managed-agents-environments.md#networking), the environment's `allowed_hosts` also applies to `web_search` and `web_fetch`. Creating a session fails with a 400 error when an enabled web tool's `allowed_domains` has an entry that is not within `allowed_hosts`. So does a session update that adds such an entry. To fix it, add the host to `allowed_hosts` or remove the entry from `allowed_domains`. At runtime, a `web_fetch` call for a URL on a host that `allowed_hosts` does not match returns a `url_not_allowed` error result. `web_search` omits results from such hosts. The two lists match differently: a tool's entry covers its subdomains, but an `allowed_hosts` entry matches one exact host unless it starts with `*.`. For example, the tool entry `docs.example.com` is not within an `allowed_hosts` of `["example.com"]`, but it is within `["docs.example.com"]` or `["*.example.com"]`.

In the Claude Console, set allowed or blocked domains from the `web_search` and `web_fetch` rows of the **Built-in tools** card on the agent form. Set `max_content_tokens` and `user_location` in the **Raw** view of the agent's configuration.

## Settings

In addition to `enabled` and `permission_policy`, the web tool entries accept the following settings:

| Setting              | Applies to                | Description                                                                                                                                                                          |
|----------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allowed_domains`    | `web_search`, `web_fetch` | The only hosts the tool can reach. See [Domain list rules](#domain-list-rules).                                                                                                      |
| `blocked_domains`    | `web_search`, `web_fetch` | Hosts the tool cannot reach. See [Domain list rules](#domain-list-rules).                                                                                                            |
| `max_content_tokens` | `web_fetch`               | Caps the amount of fetched page content included in the context. Must be a positive integer. See [content limits](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md#content-limits). |
| `user_location`      | `web_search`              | Localizes search results. An object with the same fields as the Messages API [`user_location`](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md#localization) parameter.           |

For the types the SDK uses for these entries, see [Config entry types in the SDKs](managed-agents-tools.md#config-entry-types-in-the-sdks).

## When a domain is not allowed

`web_search` omits results that its domain list does not allow. A `web_fetch` call for a URL that its domain list does not allow returns an error result to the agent. The `agent.tool_result` event has `is_error: true`, and its content names the error code `url_not_allowed`.

## Domain list rules

These rules apply to `allowed_domains` and `blocked_domains` alike. A request that breaks one is rejected, as [Validation errors](#validation-errors) describes.

- **One list for each entry:** Set either `allowed_domains` or `blocked_domains` on an entry, not both.
- **List size:** Each list holds 1 to 64 domains, each 1 to 255 characters.
- **No empty lists:** To apply no restriction, omit the field or send `null`.
- **No duplicates:** A domain can appear only once in a list. `www.example.com` and `example.com` count as different domains.

### What a listed domain matches

A listed domain matches that host and all of its subdomains. `example.com` covers `docs.example.com`, but `docs.example.com` does not cover `example.com` or `api.example.com`.

A leading `www.` is a subdomain like any other, so `www.example.com` does not cover `example.com`. List the bare domain to cover both.

Hostnames are compared without regard to case.

### Domain format

Each domain is a registrable domain name, or a subdomain of one, written as a plain hostname. It can contain ASCII letters, digits, hyphens, underscores, and dots. A single trailing `/` is ignored. A `web_search` domain can also carry a path, as [Path suffixes on web search domains](#path-suffixes-on-web-search-domains) describes.

| Not accepted                                                                   | Example                  | Use instead                           |
|--------------------------------------------------------------------------------|--------------------------|---------------------------------------|
| A scheme                                                                       | `https://example.com`    | `example.com`                         |
| A port                                                                         | `example.com:443`        | `example.com`                         |
| A wildcard                                                                     | `*.example.com`          | `example.com`                         |
| A path on a `web_fetch` domain                                                 | `example.com/*`          | `example.com`                         |
| An IP address in any form, whether IPv4, IPv6, bracketed, or numeric shorthand | `127.1`                  | The site's domain name                |
| A bare top-level domain or registry suffix                                     | `com`, `co.uk`, `gov.uk` | A full domain such as `example.co.uk` |
| A single-label name                                                            | `intranet`               | A full domain such as `example.co.uk` |
| Non-ASCII characters, as in an internationalized domain name                   |                          | The `xn--` (Punycode) form            |

A domain is also rejected if it contains credentials or whitespace, or if one of its labels starts or ends with a hyphen. `localhost` and hosts ending in `.localhost`, `.local`, `.internal`, `.localdomain`, or `.invalid` are rejected too.

### Path suffixes on web search domains

A `web_search` domain can carry a path suffix, such as `example.com/blog`. The path cannot contain spaces, `?`, `#`, or any of the characters `$ , | ^ !`.

Prefer plain hostnames for `web_search` too. The search provider matches path suffixes as URL patterns rather than as strict host rules.

## Validation errors

The API validates these settings when you [create an agent](managed-agents-agent-setup.md#create-an-agent) or [update an agent](managed-agents-agent-setup.md#update-an-agent). It also validates them when you create or update a session that supplies `tools`.

Format and limit violations are rejected with a 400 `invalid_request_error`:

| Violation                      | Error message                                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| An entry sets both lists.      | Includes `Only one of allowed_domains or blocked_domains may be set.`                                                                                          |
| A list is empty.               | Includes `allowed_domains: Empty list of domains is ambiguous. Provide at least one domain or null.`                                                           |
| A domain breaks a format rule. | Names the domain's list and zero-based position. For example, `allowed_domains.0: IP addresses are not supported; provide a plain hostname like "example.com"` |

On the same requests, the API also rejects three settings that depend on the search and fetch providers:

- A domain in `allowed_domains` that Anthropic's crawler is not allowed to access.
- A `user_location.country` that the search provider does not support. The message ends in `user_location.country: not a country the search provider supports`.
- A `user_location.timezone` that is not a valid IANA name.

In a cloud environment with `limited` [networking](managed-agents-environments.md#networking), session create and update also check `allowed_domains` against the environment's `allowed_hosts`. See the rule in [Set domain lists on an agent](#set-domain-lists-on-an-agent).

### When an accepted setting is no longer valid

The session checks the configuration again when it first initializes the tool. If a setting that was accepted earlier is no longer valid at that point, the session emits a [`session.error`](managed-agents-events-and-streaming.md) event. It then returns to `idle` without retrying.

To continue the session:

1.  Fix the setting by [updating the session's tools](managed-agents-session-operations.md#updating-the-agent-configuration).
2.  Update the agent as well, so that new sessions start with the corrected configuration.
3.  Send a new `user.message`.

## Multiagent and outcome-driven sessions

In a [multiagent session](managed-agents-multiagent-orchestration.md), every domain list that applies to a thread is enforced at the same time. An agent listed in the `predefined_agents` list of `subagents` is bound by three sets of per-tool lists:

- Its own `allowed_domains` and `blocked_domains`
- Those of any agent that called it
- The current lists of the agent that the session runs

The settings combine as follows:

| Setting                               | How it combines                                                                                                                                                                                          |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allowed_domains`                     | The tool can reach a host only if every list covers it.                                                                                                                                                  |
| `blocked_domains`                     | The lists add together.                                                                                                                                                                                  |
| `max_content_tokens`, `user_location` | Not combined. A thread uses the value from its own tool configuration if set. Otherwise it uses the value from the agent that called it, and otherwise the current configuration of the session's agent. |

A listed agent can therefore narrow what a tool reaches but never widen it:

- A listed agent that sets `blocked_domains` keeps the `allowed_domains` of the session's agent and blocks those hosts within it.
- A listed agent that sets its own `allowed_domains` can reach only the hosts that both its list and the list of the session's agent cover.

A `{"type": "self"}` entry in the `predefined_agents` list of `subagents` has no web settings of its own and follows the current settings of the session's agent.

If the combined `allowed_domains` lists have no domain in common, the tool stays available to that agent, but every call fails. Each call returns a `url_not_allowed` error stating that no domain is allowed. The tool description tells the model the same. To avoid this, keep each listed agent's `allowed_domains` inside the `allowed_domains` of the session's agent.

The grader in [outcome-driven sessions](managed-agents-define-outcomes.md) runs without `web_search` and `web_fetch`, regardless of these settings.

## Change the lists mid-session

You can change the lists on an idle session by [updating its tools](managed-agents-session-operations.md#updating-the-agent-configuration). The new lists apply to the rest of the session.

In a multiagent session, every thread applies the new lists from its next turn. For an agent listed in the `predefined_agents` list of `subagents`, the update does not change the agent's own lists. Those stay as the agent's definition set them when the session was created.

## Differences from the Messages API tools

These settings use the same `allowed_domains` and `blocked_domains` fields as [domain filtering](../Agents-Tools/agents-and-tools-tool-use-server-tools.md#domain-filtering) on the Messages API server tools. Managed Agents differs in four ways:

- Each list is [capped at 64 domains](#domain-list-rules).
- Domains listed for `web_fetch` [cannot include a path](#domain-format).
- Domains [must be ASCII](#domain-format). The Messages API accepts Unicode entries, though it recommends against them.
- `max_uses`, `citations`, and `cache_control` are not available on the toolset.

## Next steps



[Tools](managed-agents-tools.md)

See the built-in tools, enable or disable them, and define custom tools.



[Permission policies](managed-agents-permission-policies.md)

Control when agent and MCP tools run.



[Cloud environment setup](managed-agents-environments.md)

Control the sandbox's own outbound network access.

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)

Coordinate multiple agents within a single session.
