---
title: "MCP tunnels quickstart - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-13T06:32:59Z"
tags: ["api", "mcp"]
---

# MCP tunnels quickstart

Copy page



Connect Claude to a private MCP server using a local Docker Compose deployment.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

This quickstart takes you from creating a tunnel to Claude calling a private MCP server through it. It uses Docker Compose with [manual](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning) credential provisioning, which is the shortest path for local testing. For production deployments, see [Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md) or [Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md).

## What you’ll build

A two-container [tunnel stack](agents-and-tools-mcp-tunnels-concepts.md#components) (the [proxy](agents-and-tools-mcp-tunnels-concepts.md#components) and [cloudflared](agents-and-tools-mcp-tunnels-concepts.md#components)) plus a sample MCP server running alongside it. When everything is running, the sample server is reachable from Claude at `https://echo.<your-tunnel-domain>/mcp` even though nothing is listening on a public port.

## What you need

- [Docker and Docker Compose](https://docs.docker.com/get-docker/) on a machine with outbound internet access.
- A role in the [Claude Console](../Other/playground.md) that can manage MCP tunnels. See the [Console guide prerequisites](agents-and-tools-mcp-tunnels-console.md#prerequisites).
- [OpenSSL](https://openssl-library.org/source/) 1.1.1 or later. Preinstalled on macOS and most Linux distributions. On Windows, install it separately (the `openssl` binary must be on your `PATH`).

1.  1

    ### Create a tunnel

    In the Claude Console, go to the [MCP tunnels](https://platform.claude.com/settings/workspaces/default/mcp-tunnels) page (`platform.claude.com/settings/workspaces/default/mcp-tunnels`). Each tunnel belongs to one workspace. Select the workspace you want in the workspace picker in the sidebar. Click **New tunnel** and give it a name. Leave **Set up programmatic access** off; this quickstart uses manual credential provisioning.

    After it’s created, open the tunnel. Copy two values from the **Connection** section:

    - **Domain** (looks like `abcd1234.tunnel.anthropic.com`)
    - **Token** (click the eye icon, then copy)

2.  2

    ### Set up the deployment directory

    macOS / Linux
    Windows (PowerShell)

    macOS / Linux

    ``` shiki
    mkdir -p mcp-tunnel/{config,data}
    cd mcp-tunnel
    export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE   # from step 1
    export TUNNEL_TOKEN='eyJ...'            # from step 1
    ```

    

    Windows (PowerShell)

    ``` shiki
    New-Item -ItemType Directory -Force -Path mcp-tunnel/config, mcp-tunnel/data | Out-Null
    Set-Location mcp-tunnel
    $env:TUNNEL_DOMAIN = "YOUR_TUNNEL_DOMAIN_HERE"   # from step 1
    $env:TUNNEL_TOKEN  = "eyJ..."             # from step 1
    ```

    

3.  3

    ### Generate a CA and server certificate

    The proxy terminates [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components) using a certificate signed by a CA you control. Generate both:

    macOS / Linux
    Windows (PowerShell)

    macOS / Linux

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

    Windows (PowerShell)

    ``` shiki
    openssl req -x509 -newkey rsa:2048 -nodes `
      -keyout data/ca.key -out data/ca.crt `
      -days 3650 -subj "/CN=mcp-tunnel-ca" `
      -addext "basicConstraints=critical,CA:TRUE" `
      -addext "keyUsage=critical,keyCertSign,cRLSign" `
      -addext "subjectKeyIdentifier=hash"

    @"
    subjectAltName = DNS:$env:TUNNEL_DOMAIN,DNS:*.$env:TUNNEL_DOMAIN
    authorityKeyIdentifier = keyid,issuer
    extendedKeyUsage = serverAuth
    "@ | Set-Content -NoNewline -Encoding ascii -Path data/tls.ext

    openssl req -newkey rsa:2048 -nodes `
      -keyout data/tls.key -out data/server.csr `
      -subj "/CN=$env:TUNNEL_DOMAIN"
    openssl x509 -req -in data/server.csr `
      -CA data/ca.crt -CAkey data/ca.key -CAcreateserial `
      -out data/tls.crt -days 90 -extfile data/tls.ext
    ```

    

    Back in the Console, on the tunnel detail page, click **Add certificate** and upload `data/ca.crt` (or paste its contents). The **Needs certificate** badge next to the tunnel’s name goes away.

4.  4

    ### Write the sample MCP server

    macOS / Linux
    Windows (PowerShell)

    macOS / Linux

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

    Windows (PowerShell)

    ``` shiki
    @'
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)


    @mcp.tool()
    def hello(name: str = "world") -> str:
        """Say hello to someone."""
        return f"Hello, {name}!"


    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
    '@ | Set-Content -NoNewline -Encoding ascii -Path hello_server.py
    ```

    

5.  5

    ### Write the proxy config and compose file

    macOS / Linux
    Windows (PowerShell)

    macOS / Linux

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
        image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:d243d30642d39857a0579e465cb3b9bf3ae7c1141e83143bb6856777a31467a5
        volumes:
          - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
          - ./data:/data:ro
        restart: unless-stopped

      cloudflared:
        image: cloudflare/cloudflared@sha256:0e56c13c7058fcef9c4f0e7d83372f82330548dbf8f8b366f3d8b506526d93b2
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

    Windows (PowerShell)

    ``` shiki
    @"
    listen_addr: ":8080"
    tunnel_domain: $env:TUNNEL_DOMAIN
    tls:
      cert_file: /data/tls.crt
      key_file: /data/tls.key
    routes:
      echo: http://hello-mcp:9000
    "@ | Set-Content -NoNewline -Encoding ascii -Path config/mcp-proxy.yaml

    @'
    services:
      mcp-proxy:
        image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:d243d30642d39857a0579e465cb3b9bf3ae7c1141e83143bb6856777a31467a5
        volumes:
          - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
          - ./data:/data:ro
        restart: unless-stopped

      cloudflared:
        image: cloudflare/cloudflared@sha256:0e56c13c7058fcef9c4f0e7d83372f82330548dbf8f8b366f3d8b506526d93b2
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
    '@ | Set-Content -NoNewline -Encoding ascii -Path docker-compose.yaml
    ```

    

6.  6

    ### Start it

    macOS / Linux
    Windows (PowerShell)

    macOS / Linux

    ``` shiki
    docker compose up -d
    docker compose logs mcp-proxy | grep "route configured"
    docker compose logs cloudflared | grep "Registered tunnel connection"
    ```

    

    Windows (PowerShell)

    ``` shiki
    docker compose up -d
    docker compose logs mcp-proxy | Select-String "route configured"
    docker compose logs cloudflared | Select-String "Registered tunnel connection"
    ```

    

    You should see one `route configured` line for `echo` and four `Registered tunnel connection` lines. The containers take a few seconds to start; rerun the log commands if they come back empty.

7.  7

    ### Call it from Claude

    In the Console, go to the [Sessions](../Other/playground.md) page (`platform.claude.com/sessions`) and click **Create session**. From the **Agent** dropdown menu, select **Create new agent**, give the agent a name, and keep the prefilled model. Under **MCP servers**, click **MCP server**, select your tunnel, and set **Subdomain** to `echo` and **Path** to `mcp`. The sample server requires no authentication, so ignore **Connect** or **Needs vault** on the card. Select an environment. If a warning says that the environment blocks MCP servers, see [Use the tunnel in an agent](agents-and-tools-mcp-tunnels-console.md#use-the-tunnel-in-an-agent). Click **Create session**, then ask:

    > Use the hello tool to greet tunnel.

    You should see a tool call followed by its result.

## Next steps

The tunnel is verified end to end. To swap in your own MCP server, add it to `docker-compose.yaml` (or run it on the same Docker network), add a route for it in `config/mcp-proxy.yaml`, then restart the proxy (`docker compose restart mcp-proxy`).

For production deployments:



[Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md)

Hardened single-host deployment, with or without programmatic access.



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Kubernetes deployment with automatic credential management.
