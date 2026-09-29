---
title: "MCP tunnels security - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:18Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fsecurity)

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

# MCP tunnels security

Copy page



Hardening guidance, credential rotation, breach response, and teardown for MCP tunnel deployments.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

The tunnel architecture provides strong defaults (outbound-only connectivity, end-to-end encryption, and IP validation), but the overall security of your [tunnel stack](agents-and-tools-mcp-tunnels-concepts.md#components) also depends on how you configure and operate it. This page covers recommended hardening, breach response, and how to decommission a tunnel.

## Best practices

- **Require OAuth on every MCP server.** Configure each [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components) to require OAuth as described in the [MCP authorization spec](../../06-MCP-Tools/Spec-Archive/2025-11-25-basic-authorization.md). OAuth provides defense in depth on top of the tunnel's transport authentication and enables user-level authorization at the data layer.
- **Enable SSO for your organization.** Tunnels, federation rules, and service accounts are managed in the Claude Console. SSO enforces your identity provider's session controls on the admins who can change them.
- **Restrict `upstream.allowed_ips`.** Use the smallest CIDR ranges that cover your MCP servers. This is the [proxy](agents-and-tools-mcp-tunnels-concepts.md#components)'s primary SSRF defense.
- **Monitor logs.** Alert on warnings, errors, and unusual traffic patterns from the tunnel stack.
- **Rotate credentials.** Rotate the server certificate and tunnel token on a regular schedule, and immediately if you suspect compromise.
- **Keep images updated.** Track new proxy releases and pin images by SHA-256 digest.
- **Limit network reach.** The proxy and [cloudflared](agents-and-tools-mcp-tunnels-concepts.md#components) should only be able to reach the destinations listed in the [network requirements](agents-and-tools-mcp-tunnels-overview.md#network-requirements). Use NetworkPolicy (Kubernetes) or host firewall rules (Compose).
- **Limit MCP server scope.** Each server should expose only the tools and data required for its purpose.
- **Protect credentials at rest.** Apply your organization's secrets-management practices to private keys and tunnel tokens.

## Respond to a suspected breach

If you believe your tunnel token, TLS keys, or proxy host has been compromised:

1.  1

    ### Stop the tunnel stack

    Helm
    Docker Compose

    ``` shiki
    helm uninstall mcp-tunnel -n mcp-tunnel
    ```

    

2.  2

    ### Detach the upstream MCP servers

    Remove the upstream MCP servers from any Managed Agent sessions that use them, and stop passing their URLs in the `mcp_servers` block of Messages API requests.

3.  3

    ### Archive the tunnel

    Archiving invalidates the tunnel token and detaches the domain. In the Console, [archive the tunnel](agents-and-tools-mcp-tunnels-console.md#archive-a-tunnel) from the **MCP tunnels** list. To archive over the API instead, see [Archive a tunnel](../Endpoints/http-beta-tunnels-archive.md).

4.  4

    ### Contact Anthropic

    Report the suspected compromise to Anthropic support.

5.  5

    ### Rotate downstream credentials

    Re-provision a fresh tunnel and rotate any OAuth tokens that the affected MCP servers issued.

6.  6

    ### Review logs before restoring service

    Inspect proxy, cloudflared, and MCP server logs for the window of suspected compromise before bringing the new tunnel online.

## Tear down a tunnel

Follow these steps to decommission a tunnel and remove all stored credentials.

1.  1

    ### Stop the tunnel stack

    Helm
    Docker Compose

    ``` shiki
    helm uninstall mcp-tunnel -n mcp-tunnel
    ```

    

2.  2

    ### Archive the tunnel

    In the Console, [archive the tunnel](agents-and-tools-mcp-tunnels-console.md#archive-a-tunnel) from the **MCP tunnels** list.

3.  3

    ### Remove stored credentials

    Helm
    Docker Compose

    With programmatic access, the setup component created a single Secret named after the release. Without programmatic access, you created `mcp-tunnel-token` and `mcp-tunnel-cert` yourself. Delete whichever apply:

    ``` shiki
    kubectl -n mcp-tunnel delete secret \
      mcp-tunnel mcp-tunnel-token mcp-tunnel-cert \
      --ignore-not-found
    ```

    
