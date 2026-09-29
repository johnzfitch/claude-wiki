---
title: "Troubleshoot MCP tunnels - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:22Z"
tags: ["api", "authentication", "mcp", "oauth"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Ftroubleshooting)

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

# Troubleshoot MCP tunnels

Copy page



Diagnose connectivity, TLS, IP validation, and OAuth routing issues in a tunnel stack.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

A request through the tunnel can fail at one of three layers; diagnose them in order: the outbound connection to the [tunnel edge](agents-and-tools-mcp-tunnels-concepts.md#components), the [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components) from Anthropic to your [proxy](agents-and-tools-mcp-tunnels-concepts.md#components), then routing and IP validation toward the [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components).

## Quick reference

| Symptom                                                                                                                             | Cause                                                                                               | Fix                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Tunnel doesn't appear in the agent **+ MCP Server** picker                                                                          | The picker only lists tunnels in the session's workspace that have at least one active certificate. | Register a CA certificate, or open the session in the workspace the tunnel was created in.                                                 |
| Caller sees HTTP 500; [cloudflared](agents-and-tools-mcp-tunnels-concepts.md#components) logs `No ingress rules were defined` | cloudflared has no local target.                                                                    | Add `--url http://localhost:8080` and `network_mode: "service:mcp-proxy"` to the cloudflared service.                                      |
| Proxy logs `no route for host`                                                                                                      | `tunnel_domain` doesn't match the assigned domain, or `config.yaml` was edited without restarting.  | Set `tunnel_domain` to the exact domain shown on the tunnel detail page, then restart the proxy (`docker compose restart mcp-proxy`).      |
| Proxy logs `IP validation failed: <ip> is not a private address`                                                                    | Upstream MCP server resolves outside RFC1918.                                                       | See [Upstream IP validation](#upstream-ip-validation).                                                                                     |
| Proxy exits with `cannot unmarshal !!seq into map[string]string`                                                                    | `routes` is a YAML list.                                                                            | Use `routes: { name: http://host:port }`.                                                                                                  |
| Proxy exits with `open /data/tls.key: permission denied`                                                                            | The key is `0600`; the proxy container runs non-root.                                               | `chmod 644 data/tls.key`.                                                                                                                  |
| `curl https://<proxy>:8080` fails with `wrong version number`                                                                       | Expected; the listener is plaintext WebSocket. TLS happens inside the WS stream.                    | Verify through a [Managed Agent or the Messages API](agents-and-tools-mcp-tunnels-overview.md#use-the-tunneled-mcp-servers) instead. |

The following sections cover failures that need more than a one-line fix.

## OAuth fails behind a source-IP allowlist

OAuth flows fail when your authorization server's source-IP allowlist blocks Anthropic's backend from reaching `/token`, `/register`, and the discovery endpoints. If you'd rather not allowlist Anthropic's egress ranges, you can route the backend-to-backend OAuth calls through the tunnel while keeping the browser-facing `/authorize` endpoint on your existing public hostname.

1.  1

    ### Add a proxy route for the authorization server

    ``` shiki
    routes:
      mcp: http://your-mcp-server:8080
      auth: http://your-auth-server:8080
    ```

    

    Restart the proxy after editing `routes` (`docker compose restart mcp-proxy`, or `helm upgrade`).

2.  2

    ### Serve split-endpoint discovery metadata

    Your authorization server's `/.well-known/oauth-authorization-server` response should point `authorization_endpoint` at your existing allowlisted hostname and everything else at the tunnel:

    ``` shiki
    {
      "issuer": "https://auth.<tunnel-domain>",
      "authorization_endpoint": "https://<your-allowlisted-host>/authorize",
      "token_endpoint": "https://auth.<tunnel-domain>/token",
      "registration_endpoint": "https://auth.<tunnel-domain>/register",
      "code_challenge_methods_supported": ["S256"]
    }
    ```

    

3.  3

    ### Point the MCP server at the tunnel issuer

    Your MCP server's `/.well-known/oauth-protected-resource` response should reference the tunnel hostname as its authorization server:

    ``` shiki
    {
      "resource": "https://mcp.<tunnel-domain>",
      "authorization_servers": ["https://auth.<tunnel-domain>"]
    }
    ```

    

With this configuration, the user's browser hits `/authorize` on your existing hostname (which your allowlist already permits), while Anthropic's backend reaches `/token`, `/register`, and the discovery documents through the tunnel.

## Setup component authentication failures

The [setup component](agents-and-tools-mcp-tunnels-concepts.md#components) (Helm Job or Compose `setup` service) authenticates to the Tunnels API by exchanging an OIDC JWT through your federation rule. When the exchange fails, see [Troubleshoot a failed exchange](../Other/manage-claude-wif-reference.md#troubleshoot-a-failed-exchange) in the Workload Identity Federation reference; the failure modes (subject, audience, issuer, JWKS, lifetime) are the same.

Tunnels-specific causes:

- The chart's default audience is `api.anthropic.com` (no scheme). If your rule's audience is `https://api.anthropic.com`, set `api.wif.audience` to match.
- A `403` from the Tunnels API after a successful exchange means the rule's scope doesn't include `workspace:manage_tunnels`, or the rule's service account isn't a member of the tunnel's workspace. Set the scope and add the service account to the workspace.

On Helm, the setup component runs as a pre-install hook Job. On failure, the Job is left behind for inspection (`kubectl logs job/mcp-tunnel-setup -n mcp-tunnel`). Helm doesn't manage hook resources, so delete it before retrying:

```python
helm uninstall mcp-tunnel -n mcp-tunnel
kubectl -n mcp-tunnel delete job mcp-tunnel-setup
```



## Tunnel won't connect

Check the cloudflared logs first. Common causes:

- The `TUNNEL_TOKEN` is missing, expired, or copied incorrectly.
- A firewall is blocking outbound TCP/UDP on port 7844 to the tunnel edge.

cloudflared may also log warnings about UDP receive buffer sizes; this is a QUIC tuning hint, not an error.

## Certificate errors

When Anthropic rejects the proxy's certificate during inner TLS, the proxy logs `tls handshake failed`. Verify that:

- The server certificate has not expired.
- The certificate's Subject Alternative Name matches `*.<tunnel-domain>`.
- The signing CA is registered with Anthropic for this tunnel.

See the [certificate requirements](agents-and-tools-mcp-tunnels-reference.md#certificate-requirements) for the full validation rules.

## Upstream IP validation

For SSRF protection, the proxy only dials addresses in the RFC1918 private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) by default. Only IPv4 is supported for the proxy-to-upstream connection. (The cloudflared-to-edge egress range in [Network requirements](agents-and-tools-mcp-tunnels-overview.md#network-requirements) is a different hop.)

If the proxy logs `IP validation failed: <ip> is not a private address`, the upstream hostname resolved outside that set. On Kubernetes, some managed distributions allocate the Service CIDR outside RFC1918; if `kubectl get svc kubernetes -n default -o jsonpath='{.spec.clusterIP}'` returns an address outside the private ranges, look up your cluster's Service CIDR and add it.

If the address is legitimate, add the narrowest covering CIDR to `upstream.allowed_ips`. Setting `allowed_ips` **replaces** the RFC1918 default rather than extending it, so include the private ranges your other upstream MCP servers use:

config/mcp-proxy.yaml



```python
upstream:
  allowed_ips:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16
    - 127.0.0.0/8       # loopback, for local testing only
```



Avoid `0.0.0.0/0` outside of local testing; it disables SSRF protection entirely.
