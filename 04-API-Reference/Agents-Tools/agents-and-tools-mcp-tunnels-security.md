---
title: "MCP tunnels security - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-05T06:35:30Z"
tags: ["api", "mcp", "security"]
---

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

- **Require OAuth on every MCP server.** Configure each [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components) to require OAuth as described in the [MCP authorization spec](../../06-MCP-Tools/Spec-Archive/2025-11-25-basic-authorization.md). OAuth provides defense in depth on top of the tunnel’s transport authentication and allows user-level authorization at the data layer.
- **Enable SSO for your organization.** Tunnels, federation rules, and service accounts are managed in the Claude Console. SSO enforces your identity provider’s session controls on the admins who can change them.
- **Restrict `upstream.allowed_ips`.** Use the smallest CIDR ranges that cover your MCP servers. This is the [proxy](agents-and-tools-mcp-tunnels-concepts.md#components)’s primary SSRF defense.
- **Monitor logs.** Alert on warnings, errors, and unusual traffic patterns from the tunnel stack.
- **Rotate credentials.** Rotate the server certificate and tunnel token on a regular schedule, and immediately if you suspect compromise.
- **Keep images updated.** Track new proxy releases and pin images by SHA-256 digest.
- **Limit network reach.** The proxy and [cloudflared](agents-and-tools-mcp-tunnels-concepts.md#components) should only be able to reach the destinations listed in the [network requirements](agents-and-tools-mcp-tunnels-overview.md#network-requirements). Use NetworkPolicy (Kubernetes) or host firewall rules (Compose).
- **Limit MCP server scope.** Each server should expose only the tools and data required for its purpose.
- **Protect credentials at rest.** Apply your organization’s secrets-management practices to private keys and tunnel tokens.

## Respond to a suspected breach

If you believe your tunnel token, TLS keys, or proxy host has been compromised:

1.  1

    ### Stop the tunnel stack

    Helm
    Docker Compose

    Helm

    ``` shiki
    helm uninstall mcp-tunnel -n mcp-tunnel
    ```

    

    Docker Compose

    ``` shiki
    docker compose down --timeout 0
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

    Helm

    ``` shiki
    helm uninstall mcp-tunnel -n mcp-tunnel
    ```

    

    Docker Compose

    ``` shiki
    docker compose down
    ```

    

2.  2

    ### Archive the tunnel

    In the Console, [archive the tunnel](agents-and-tools-mcp-tunnels-console.md#archive-a-tunnel) from the **MCP tunnels** list.

3.  3

    ### Remove stored credentials

    Helm
    Docker Compose

    Helm

    With programmatic access, the setup component created a single Secret named after the release. Without programmatic access, you created `mcp-tunnel-token` and `mcp-tunnel-cert` yourself. Delete whichever apply:

    ``` shiki
    kubectl -n mcp-tunnel delete secret \
      mcp-tunnel mcp-tunnel-token mcp-tunnel-cert \
      --ignore-not-found
    ```

    

    Docker Compose

    Private keys and certificates live in `data/`. The tunnel token lives in `data/tunnel-token` (programmatic flow) or in your shell environment (manual flow). The `config/` directory and `docker-compose.yaml` contain no secrets; keep them if you plan to re-provision, or remove them as well.

    ``` shiki
    sudo rm -rf data
    ```

    
