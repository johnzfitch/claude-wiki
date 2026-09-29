---
title: "Architecture and components - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:21Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fconcepts)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

[Overview](agents-and-tools-mcp-tunnels-overview.md)[Architecture and components](agents-and-tools-mcp-tunnels-concepts.md)[Quickstart](agents-and-tools-mcp-tunnels-quickstart.md)[Manage in the Console](agents-and-tools-mcp-tunnels-console.md)[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)[Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md)[Security](agents-and-tools-mcp-tunnels-security.md)[Troubleshooting](agents-and-tools-mcp-tunnels-troubleshooting.md)[Reference](agents-and-tools-mcp-tunnels-reference.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)MCP tunnels

# Architecture and components

Copy page



Canonical names for the parts of an MCP tunnel deployment, the two credential-provisioning modes, and the connection model.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

This page defines the terms used throughout the [MCP tunnels](agents-and-tools-mcp-tunnels-overview.md) documentation. Several components appear under different names in configuration files, container images, and prose; the following tables give one canonical name for each and list the aliases you may encounter.

## Components

| Term                    | Definition                                                                                                                                                                                                                                                                                                              | Also appears as                                                                                                                                                                                  |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tunnel stack**        | The two containers you run inside your network to attach to a tunnel: the proxy and cloudflared. One stack serves one tunnel and can be replicated across hosts for availability. With programmatic access, the setup component runs alongside the stack to provision credentials.                                      | the stack, the MCP tunnel stack, the tunnel deployment, your deployment                                                                                                                          |
| **Proxy**               | Anthropic's routing component. Terminates inner TLS, validates that upstream IPs fall within an allowed range, and routes each request to an upstream MCP server based on hostname.                                                                                                                                     | `mcp-proxy` (image name, Compose service name, and Helm container name), `mcp-gateway` (container-internal config path `/etc/mcp-gateway/config.yaml` and Helm `gateway.config.*` values prefix) |
| **cloudflared**         | Cloudflare's open-source tunnel connector. Initiates the outbound-only connections from your network to the tunnel edge and carries encrypted traffic between the edge and the proxy. Not related to a Managed Agent.                                                                                                   | the outbound connector, the tunnel connector                                                                                                                                                     |
| **Setup component**     | The `setup` binary, shipped inside the `mcp-proxy` image. With programmatic access it authenticates over Workload Identity Federation, fetches the tunnel token, generates a CA and server certificate, and registers the CA with Anthropic. Also provides `renew-cert`.                                                | setup Job (the Helm pre-install hook), `setup` service (the Compose profile), setup hook, setup binary, setup CLI                                                                                |
| **Tunnel edge**         | The Cloudflare edge servers that cloudflared dials out to (IP ranges `198.41.192.0/19` and `2606:4700:a0::/44`, port 7844 TCP and UDP). The tunnel that runs over them is provisioned and controlled by Anthropic; Cloudflare operates the underlying network.                                                          | the edge, the Anthropic-operated tunnel edge                                                                                                                                                     |
| **Inner TLS**           | A second TLS handshake carried inside the tunnel's plaintext WebSocket stream, between Anthropic's backend and your proxy. The proxy presents a server certificate signed by a CA you registered on the tunnel. Because only you hold the private key, the transport provider cannot read request or response payloads. | the inner TLS handshake                                                                                                                                                                          |
| **Upstream MCP server** | An MCP server running in your private network that the proxy routes to. Each upstream is exposed as one subdomain under your tunnel domain.                                                                                                                                                                             | upstream, routed MCP server, tunneled MCP server                                                                                                                                                 |

## Credential provisioning

The tunnel stack needs two credentials at runtime: the **tunnel token**, which authenticates cloudflared's outbound connection, and a **server certificate** signed by a CA registered on the tunnel, which the proxy presents during the inner TLS handshake. There are two ways to supply them, presented throughout this guide as a pair of tabs.

| Mode                    | How credentials reach the stack                                                                                                                                                                                                                                                                                                                                | Helm chart name                                   | Tab label                       |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|---------------------------------|
| **Programmatic access** | The setup component authenticates to the Tunnels API through [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md), fetches the tunnel token, generates a CA and server certificate locally, and registers the CA. No long-lived secret is copied by hand. Requires a federation rule with the `workspace:manage_tunnels` scope. | Managed mode (`setup.enabled: true`, the default) | **With programmatic access**    |
| **Manual**              | You copy the tunnel token from the Claude Console, generate a CA and server certificate yourself (for example with `openssl`), register the CA in the Console, and supply the token and certificate to the stack as secrets. No setup component runs.                                                                                                          | External mode (`setup.enabled: false`)            | **Without programmatic access** |

These modes are also referred to as **the programmatic flow** and **the manual flow** in the deploy guides.

## Connection model

Two directions are at work in a tunnel, and they point opposite ways:

- **Connection direction:** cloudflared dials **outbound** from your network to the tunnel edge. Your firewall sees only egress on port 7844; no inbound port is opened.
- **Request direction:** once that connection is established, MCP requests travel **from Anthropic toward your network** over it, through cloudflared to the proxy, and on to the upstream MCP server.

The phrase "outbound-only" describes the connection, not the requests carried over it.

Inner TLS spans Anthropic's backend and your proxy. cloudflared and the tunnel edge sit between them on the wire but see only ciphertext; the proxy is the first place inside your network where MCP request payloads are readable.

## See also

- [MCP tunnels](agents-and-tools-mcp-tunnels-overview.md) for the security model and shared-responsibility table.
- [MCP tunnels reference](agents-and-tools-mcp-tunnels-reference.md) for proxy configuration fields, certificate requirements, and the setup component.
