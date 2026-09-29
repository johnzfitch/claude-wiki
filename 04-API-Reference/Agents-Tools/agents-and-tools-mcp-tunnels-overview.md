---
title: "MCP tunnels - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:22Z"
tags: ["api", "mcp", "security"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Foverview)

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

# MCP tunnels

Copy page



Securely connect Claude to MCP servers running in your private network without opening inbound ports or exposing services to the public internet.

Copy page



MCP tunnels let you connect Claude to Model Context Protocol (MCP) servers that run inside your private network. Traffic flows over an outbound-only connection, so you don't need to open inbound firewall ports, expose services to the public internet, or allowlist Anthropic's IP ranges on your origin.



MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them. They are provided "as-is" without any uptime, support, or continuity commitment, and they depend on a third-party network provider (Cloudflare) that makes no availability commitment for the underlying transport. Anthropic may modify or discontinue MCP tunnels at any time.

For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](../Other/manage-claude-api-and-data-retention.md#feature-eligibility).

## How it works

The [tunnel stack](agents-and-tools-mcp-tunnels-concepts.md#components) is two components that run inside your network:

- **[cloudflared](agents-and-tools-mcp-tunnels-concepts.md#components):** Cloudflare's open-source tunnel connector. It initiates outbound-only connections to the [tunnel edge](agents-and-tools-mcp-tunnels-concepts.md#components) and carries encrypted traffic from Anthropic to your proxy.
- **[Proxy](agents-and-tools-mcp-tunnels-concepts.md#components):** Anthropic's routing component. It terminates [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components), validates that upstream IPs fall within an allowed range, and routes each request to the correct [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components) based on hostname.

Each MCP server you expose gets a hostname under your tunnel domain (for example, `docs.<your-tunnel-domain>`). You attach these hostnames to a Managed Agent session in the Claude Console, or pass them to the Messages API through the [MCP connector](agents-and-tools-mcp-connector.md).

## Prerequisites

Before deploying, make sure you have:

- A deployment target: a Kubernetes cluster, or a VM with Docker and Docker Compose.
- A tunnel. Create one in the Claude Console (see [Create a tunnel](agents-and-tools-mcp-tunnels-console.md#create-a-tunnel)) or through the API; the Helm chart's setup hook can also create one for you during install.
- A way for your stack to authenticate to the Tunnels API. Choose one:
  - **[Programmatic access](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning) (recommended).** Set up [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md) when you create the tunnel. Your stack mints short-lived API tokens from your identity provider, fetches the tunnel token, and generates and registers a CA certificate automatically. Requires permission to manage federation rules, a registered OIDC issuer, and a federation rule with the `workspace:manage_tunnels` scope.
  - **[Manual](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning).** Supply static credentials yourself: the tunnel token from the Console and a server certificate signed by a CA you register there. See [Get the connection details](agents-and-tools-mcp-tunnels-console.md#get-the-connection-details) and [Add a CA certificate](agents-and-tools-mcp-tunnels-console.md#add-a-ca-certificate).
- One or more MCP servers running in your private network. See [Remote MCP servers](agents-and-tools-remote-mcp-servers.md) for examples.
- Outbound connectivity as listed under [Network requirements](#network-requirements).

### Network requirements

| Component       | Destination                                          | Port / protocol  | Used during                     |
|-----------------|------------------------------------------------------|------------------|---------------------------------|
| Setup component | `api.anthropic.com`                                  | 443 TCP          | Provisioning and token rotation |
| cloudflared     | Tunnel edge (`198.41.192.0/19`, `2606:4700:a0::/44`) | 7844 TCP and UDP | Runtime                         |
| Proxy           | Your upstream MCP servers                            | As configured    | Runtime                         |

## Security model

### Security layers

Three independent layers protect every request:

| Layer                                                                       | Protects against                                                         |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Outer mTLS between Anthropic and the transport provider, with IP validation | Unauthorized clients reaching the tunnel                                 |
| Inner TLS from Anthropic's back end to your proxy                           | Payload inspection by the transport provider or any network intermediary |
| OAuth on each MCP server                                                    | Unauthorized use of MCP tools by authenticated tunnel traffic            |

The tunnel transport runs on Cloudflare's network. Because the proxy terminates inner TLS using a certificate that only you hold, Cloudflare cannot read request or response payloads. Anthropic does not connect to a tunnel until a CA certificate is registered, so payloads are always encrypted when they cross Cloudflare's network. Cloudflare does receive connection metadata; see [What the transport provider can observe](#what-the-transport-provider-can-observe).

### Shared responsibility model

| Anthropic handles                                                         | Your organization handles                                                                                                                      |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Tunnel access control                                                     | All content and traffic that transits your tunnel, and compliance with applicable third-party acceptable-use policies (including Cloudflare's) |
| Validating your CA certificate before connecting to your proxy            | Adherence to the deployment guidance on these pages                                                                                            |
| Ensuring Claude only sends requests to tunnels owned by your organization | Securing tunnel tokens and TLS private keys                                                                                                    |
|                                                                           | Managing the server certificate and renewing it before it expires                                                                              |
|                                                                           | Configuring OAuth on each MCP server                                                                                                           |
|                                                                           | Restricting network access for the proxy and MCP servers                                                                                       |
|                                                                           | Notifying Anthropic if you suspect a breach                                                                                                    |



If an attacker obtains your tunnel token **and** one of your TLS private keys, they could impersonate your proxy and read MCP request payloads. Treat both as high-value secrets. See [MCP tunnels security](agents-and-tools-mcp-tunnels-security.md) for hardening guidance.

### What the transport provider can observe

Cloudflare provides the outbound transport. It cannot read MCP request or response payloads, but it does receive the following connection metadata:

- the egress IP address of the host running cloudflared
- a cloudflared host fingerprint
- connection timing and byte-volume
- the `*.tunnel.anthropic.com` subdomain assigned to your tunnel

Anthropic's agreement with Cloudflare restricts Cloudflare's use of this telemetry. Cloudflare acts as a subprocessor for this research preview.

## Deploy a tunnel

If you're new to MCP tunnels, start with the quickstart to get a working tunnel locally before configuring a production deployment.

[Quickstart](agents-and-tools-mcp-tunnels-quickstart.md)

The shortest path to a working tunnel: Docker Compose with a sample MCP server.



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Install on a Kubernetes cluster using the Anthropic Helm chart.



[Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md)

Install on a VM using Docker Compose.

Choosing between them:

- **Deployment target**
  - **Helm** when deploying to Kubernetes.
  - **Docker Compose** for a single host or local testing.
- **Authentication for setup**
  - **Programmatic access** (through Workload Identity Federation) when you have an OIDC identity provider such as a Kubernetes cluster, cloud IAM, or SPIFFE.
  - **Manual credentials** when you don't, or when you're testing.

## Use the tunneled MCP servers

Once your tunnel is active (it has an active CA certificate and your tunnel stack is connected), the upstream MCP servers are reachable from Claude Managed Agents and the Messages API.



MCP tunnels created through the Console are not available as connectors in claude.ai.

In both cases, the tunnel carries encrypted traffic to your MCP server but does not authenticate to it. If the upstream MCP server requires its own authentication (OAuth, bearer token), supply it the same way you would for any other MCP server; it is independent of the tunnel.

### Managed Agents (Console)

1.  In **Managed Agents \> Sessions**, create a session and choose **Create new agent** so you can edit the MCP server list.
2.  Click **+ MCP Server** and open the dropdown. Tunnels in the session's workspace that have at least one active certificate appear at the top of the list, above the public connector catalog.
3.  Select the tunnel and supply the **Subdomain** that your proxy routes to a specific MCP server, and the **Path** the upstream MCP server expects. The **Resolves to** line shows the exact URL.

### Messages API

Pass the upstream MCP server's URL in the `mcp_servers` array, the same way as any other remote MCP server. The request body and `anthropic-beta` header follow the standard [MCP connector](agents-and-tools-mcp-connector.md) format; only the `url` is tunnel-specific. The following example uses the MCP connector's `mcp-client` beta header, which is separate from the `mcp-tunnels` beta used by the [Tunnels API](agents-and-tools-mcp-tunnels-reference.md). Make the request in the workspace the tunnel was created in by using an API key for that workspace or, if your key has access to multiple workspaces, by setting the [`anthropic-workspace-id` header](../Other/manage-claude-authentication.md#select-a-workspace) to that workspace.

The URL's host is `<subdomain>.<your-tunnel-domain>`. The path depends on your upstream MCP server, not the tunnel: FastMCP's `streamable-http` transport serves at `/mcp`, and other servers may use `/` or a custom path (check the server's documentation). The proxy forwards the path untouched.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Use the hello tool to greet tunnel."}],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://echo.YOUR_TUNNEL_DOMAIN_HERE/mcp",
            "name": "echo",
        }
    ],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "echo"}],
    betas=["mcp-client-2025-11-20"],
)

print(response)
```

For authenticating to the upstream MCP server (`authorization_token`) and other `mcp_servers` options, see [MCP connector](agents-and-tools-mcp-connector.md).

## Next steps



[Security](agents-and-tools-mcp-tunnels-security.md)

Hardening guidance, credential rotation, and breach response.



[Troubleshooting](agents-and-tools-mcp-tunnels-troubleshooting.md)

Diagnose connectivity, TLS, and routing issues.



[Reference](agents-and-tools-mcp-tunnels-reference.md)

Proxy config fields, the Tunnels API, certificate requirements, and the setup component.



[MCP connector](agents-and-tools-mcp-connector.md)

Use tunneled servers from the Messages API.
