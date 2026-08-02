---
title: "MCP tunnels quickstart - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-08-02T05:39:49Z"
tags: ["api", "mcp"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

[Overview](/docs/en/agents-and-tools/mcp-tunnels/overview)[Architecture and components](/docs/en/agents-and-tools/mcp-tunnels/concepts)[Quickstart](/docs/en/agents-and-tools/mcp-tunnels/quickstart)[Manage in the Console](/docs/en/agents-and-tools/mcp-tunnels/console)[Deploy with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)[Deploy with Docker Compose](/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)[Security](/docs/en/agents-and-tools/mcp-tunnels/security)[Troubleshooting](/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)[Reference](/docs/en/agents-and-tools/mcp-tunnels/reference)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Quickstart

Messages/MCP tunnels

# MCP tunnels quickstart




Connect Claude to a private MCP server using a local Docker Compose deployment.






MCP tunnels are in research preview. [Request access](https://claude.com/form/claude-managed-agents) to try them.

This quickstart takes you from zero to Claude calling a private MCP server through a tunnel. It uses Docker Compose with [manual](/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning) credential provisioning, which is the shortest path for local testing. For production deployments, see [Deploy with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm) or [Deploy with Docker Compose](/docs/en/agents-and-tools/mcp-tunnels/deploy-compose).




What you'll build

A two-container [tunnel stack](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (the [proxy](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) and [cloudflared](/docs/en/agents-and-tools/mcp-tunnels/concepts#components)) plus a sample MCP server running alongside it. When everything is running, the sample server is reachable from Claude at `https://echo.<your-tunnel-domain>/mcp` even though nothing is listening on a public port.




What you need

- [Docker and Docker Compose](https://docs.docker.com/get-docker/) on a machine with outbound internet access.
- A role in the [Claude Console](https://platform.claude.com) that can manage MCP tunnels. See the [Console guide prerequisites](/docs/en/agents-and-tools/mcp-tunnels/console#prerequisites).
- [OpenSSL](https://openssl-library.org/source/) 1.1.1 or later. Preinstalled on macOS and most Linux distributions; on Windows, install it separately (the `openssl` binary must be on your `PATH`).

1.  1

    Create a tunnel

    In the Claude Console sidebar, go to **Manage \> MCP tunnels** and click **New tunnel**. Give it a name. Leave **Set up programmatic access** off; this quickstart uses manual credential provisioning.

    After it's created, open the tunnel. Copy two values from the **Connection** section:

    - **Domain** (looks like `abcd1234.tunnel.anthropic.com`)
    - **Token** (click the eye icon, then copy)

2.  2

    Set up the deployment directory

    macOS / Linux

    macOS / Linux

    Windows (PowerShell)

    Windows (PowerShell)

    ``` shiki
    mkdir -p mcp-tunnel/{config,data}
    cd mcp-tunnel
    export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE   # from step 1
    export TUNNEL_TOKEN='eyJ...'            # from step 1
    ```

    

3.  3

    Generate a CA and server certificate

    The proxy terminates [inner TLS](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) using a certificate signed by a CA you control. Generate both:

    macOS / Linux

    macOS / Linux

    Windows (PowerShell)

    Windows (PowerShell)

    ``` shiki
    openssl req -x509 -newkey rsa:2048 -nodes \
      -keyout data/ca.key -out data/ca.crt \
      -days 3650 -subj "/CN=mcp-tunnel-ca" \
      -addext "basicConstraints=critical,CA:TRUE" \
      -addext "keyUsage=critical,keyCertSign,cRLSign" \
      -addext "subjectKeyIdentifier=hash"

    cat > data/tls.ext <<EOF
    subjectAltName = DNS:${TUNNEL_DOMAIN},DNS:*.${TUNNEL_DOMAIN}
    authorityKeyIdentifier = keyid,issuer
    extendedKeyUsage = serverAuth
    EOF

    openssl req -newkey rsa:2048 -nodes \
      -keyout data/tls.key -out /tmp/server.csr \
      -subj "/CN=${TUNNEL_DOMAIN}"
    openssl x509 -req -in /tmp/server.csr \
      -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
      -out data/tls.crt -days 90 -extfile data/tls.ext

    chmod 644 data/tls.key
    ```

    

    Back in the Console, on the tunnel detail page, click **Add certificate** and upload `data/ca.crt` (or paste its contents). The tunnel status flips to **Active**.

4.  4

    Write the sample MCP server

    macOS / Linux

    macOS / Linux

    Windows (PowerShell)

    Windows (PowerShell)

    ``` shiki
    cat > hello_server.py <<'EOF'
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)


    @mcp.tool()
    def hello(name: str = "world") -> str:
        """Say hello to someone."""
        return f"Hello, {name}!"


    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
    EOF
    ```

    

5.  5

    Write the proxy config and compose file

    macOS / Linux

    macOS / Linux

    Windows (PowerShell)

    Windows (PowerShell)

    ``` shiki
    cat > config/mcp-proxy.yaml <<EOF
    listen_addr: ":8080"
    tunnel_domain: ${TUNNEL_DOMAIN}
    tls:
      cert_file: /data/tls.crt
      key_file: /data/tls.key
    routes:
      echo: http://hello-mcp:9000
    EOF

    cat > docker-compose.yaml <<'EOF'
    services:
      mcp-proxy:
        image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:efb27b299d627e4134815663cb8896641eeaee025d734c0f695582b4df38f013
        volumes:
          - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
          - ./data:/data:ro
        restart: unless-stopped

      cloudflared:
        image: cloudflare/cloudflared@sha256:6b599ca3e974349ead3286d178da61d291961182ec3fe9c505e1dd02c8ac31b0
        command: tunnel --no-autoupdate run --url http://localhost:8080
        environment:
          - TUNNEL_TOKEN
        network_mode: "service:mcp-proxy"
        restart: unless-stopped

      hello-mcp:
        image: python:3.13-slim
        working_dir: /app
        volumes:
          - ./hello_server.py:/app/hello_server.py:ro
        command: sh -c "pip install --quiet mcp && python hello_server.py"
        restart: unless-stopped
    EOF
    ```

    

6.  6

    Start it

    macOS / Linux

    macOS / Linux

    Windows (PowerShell)

    Windows (PowerShell)

    ``` shiki
    docker compose up -d
    docker compose logs mcp-proxy | grep "route configured"
    docker compose logs cloudflared | grep "Registered tunnel connection"
    ```

    

    You should see one `route configured` line for `echo` and four `Registered tunnel connection` lines. The containers take a few seconds to start; rerun the log commands if they come back empty.

7.  7

    Call it from Claude

    In the Console, go to **Managed Agents \> Sessions** and create a session. In the agent picker choose **Create new agent**, give the agent a name, and keep the pre-filled model. Click **+ MCP Server**, select your tunnel, set **Subdomain** to `echo` and **Path** to `mcp`. Then ask:

    > Use the hello tool to greet tunnel.

    You should see a tool call followed by its result.




Next steps

The tunnel is verified end to end. To swap in your own MCP server, add it to `docker-compose.yaml` (or run it on the same Docker network), add a route for it in `config/mcp-proxy.yaml`, then restart the proxy (`docker compose restart mcp-proxy`).

For production deployments:


Deploy with Docker Compose

Hardened single-host deployment, with or without programmatic access.


Deploy with Helm

Kubernetes deployment with automatic credential management.
