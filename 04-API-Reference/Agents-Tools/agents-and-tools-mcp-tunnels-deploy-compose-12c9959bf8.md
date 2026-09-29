---
title: "Deploy MCP tunnels with Docker Compose - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:20Z"
tags: ["api", "docker", "mcp"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fdeploy-compose)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

[Overview](/docs/en/agents-and-tools/mcp-tunnels/overview)[Architecture and components](/docs/en/agents-and-tools/mcp-tunnels/concepts)[Quickstart](/docs/en/agents-and-tools/mcp-tunnels/quickstart)[Manage in the Console](/docs/en/agents-and-tools/mcp-tunnels/console)[Deploy with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)[Deploy with Docker Compose](/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)[Security](/docs/en/agents-and-tools/mcp-tunnels/security)[Troubleshooting](/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)[Reference](/docs/en/agents-and-tools/mcp-tunnels/reference)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)MCP tunnels

# Deploy MCP tunnels with Docker Compose

Copy page



Install the MCP tunnel stack on a VM using Docker Compose.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

This guide deploys the [tunnel stack](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) as hardened containers on a single host. The same configuration can be replicated across multiple hosts for availability.

## Before you begin

You need:

- **A tunnel.** With programmatic access, the [setup component](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) creates one for you when you don't supply a tunnel ID; to attach to an existing tunnel instead, [create it in the Console](/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel) and record the tunnel ID (`tnl_...`). Manual provisioning always starts from a Console-created tunnel.
- **A way for the host to authenticate to the Tunnels API.**
  - **Programmatic access (recommended).** Turn on **Set up programmatic access** when creating the tunnel (or create the federation rule directly under **Settings \> Workload identity** if you're letting the setup component create the tunnel) so the setup component can authenticate through Workload Identity Federation. Record the federation rule ID (`fdrl_...`) and your organization ID.
  - **Manual.** Skip programmatic access. You'll [get the tunnel token from the Console](/docs/en/agents-and-tools/mcp-tunnels/console#get-the-connection-details), generate a CA and server certificate yourself, and [register the CA in the Console](/docs/en/agents-and-tools/mcp-tunnels/console#add-a-ca-certificate).
- **A host with Docker and Docker Compose** installed. The manual flow also requires `openssl` (1.1.1 or later).
- **Outbound network connectivity** from the host to `api.anthropic.com` (443 TCP) and the [tunnel edge](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (7844 TCP and UDP). See the full [network requirements](/docs/en/agents-and-tools/mcp-tunnels/overview#network-requirements).
- **One or more MCP servers** running and reachable from the host on the addresses you'll configure under `routes`. If you don't have one yet, [use the sample server](#optional-use-a-sample-mcp-server).

## Optional: Use a sample MCP server

If you don't have an MCP server available for testing, use this minimal one:

```python
mkdir -p mcp-tunnel
cat > mcp-tunnel/hello_server.py <<'EOF'
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

The following Install steps `cd` into `mcp-tunnel/` and note where to add the corresponding service and route.

## Install

This guide provides one reference approach using Docker Compose. You are responsible for adapting it to meet your organization's security requirements.

With programmatic access

Without programmatic access

This path requires the host to have an OIDC identity provider (such as a cloud VM metadata server or SPIFFE). If it doesn't, use the **Without programmatic access** tab instead.

The setup component uses Workload Identity Federation to fetch the tunnel token, generate a CA and server certificate, and register the CA with Anthropic.

1.  1

    ### Prepare the deployment directory

    ``` shiki
    mkdir -p mcp-tunnel/{config,data}
    cd mcp-tunnel
    sudo chown 65532:65532 data
    ```

    

    The containers run as the non-root UID `65532` and need write access to `data/`.

2.  2

    ### Write docker-compose.yaml

    The compose file pins images by SHA-256 digest, runs every container as non-root with a read-only filesystem, drops all Linux capabilities, and disables privilege escalation.

    ``` shiki
    cat > docker-compose.yaml <<'EOF'
    services:
      setup:
        image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:efb27b299d627e4134815663cb8896641eeaee025d734c0f695582b4df38f013
        entrypoint: ["/setup"]
        command:
          - init
          - --api-url=https://api.anthropic.com
          - --output=dir:/data
          - --token-version=1
        environment:
          - TUNNEL_ID
          - ANTHROPIC_FEDERATION_RULE_ID
          - ANTHROPIC_ORGANIZATION_ID
          - ANTHROPIC_WORKSPACE_ID
          - ANTHROPIC_IDENTITY_TOKEN
        volumes:
          - ./data:/data
        user: "65532:65532"
        read_only: true
        security_opt:
          - no-new-privileges:true
        cap_drop:
          - ALL
        profiles: ["setup"]

      cloudflared:
        image: cloudflare/cloudflared@sha256:6b599ca3e974349ead3286d178da61d291961182ec3fe9c505e1dd02c8ac31b0
        command: tunnel --no-autoupdate run --url http://localhost:8080
        environment:
          - TUNNEL_TOKEN
        # Share the proxy's netns so localhost:8080 reaches it.
        network_mode: "service:mcp-proxy"
        restart: unless-stopped
        user: "65532:65532"
        read_only: true
        security_opt:
          - no-new-privileges:true
        cap_drop:
          - ALL
        stop_grace_period: 30s
        logging:
          options:
            max-size: "10m"
            max-file: "3"

      mcp-proxy:
        image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:efb27b299d627e4134815663cb8896641eeaee025d734c0f695582b4df38f013
        volumes:
          - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
          - ./data:/data:ro
        restart: unless-stopped
        user: "65532:65532"
        read_only: true
        security_opt:
          - no-new-privileges:true
        cap_drop:
          - ALL
        stop_grace_period: 30s
        logging:
          options:
            max-size: "10m"
            max-file: "3"
    EOF
    ```

    

    If you're using the [sample MCP server](#optional-use-a-sample-mcp-server), append it as a service:

    ``` shiki
    cat >> docker-compose.yaml <<'EOF'

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

3.  3

    ### Provision the tunnel

    Set the identifiers. Leave `TUNNEL_ID` unset to have the setup component create a tunnel; set it to attach to an existing tunnel from the [Console](/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel):

    ``` shiki
    # export TUNNEL_ID=tnl_...   # set to attach to an existing tunnel
    export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
    export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
    ```

    

    If your federation rule is scoped to a workspace other than your organization's default, also set `ANTHROPIC_WORKSPACE_ID=wrkspc_...`; the setup component uses the default workspace otherwise. An auto-created tunnel is created in that workspace.

    Set `ANTHROPIC_IDENTITY_TOKEN` to an OIDC JWT from this host's identity provider. Follow the [WIF guide for your provider](/docs/en/manage-claude/workload-identity-federation#identity-providers) to register the issuer, set the rule's subject, and mint the token; the rule's audience must match the audience you request when minting.

    Run the setup component:

    ``` shiki
    docker compose run --rm setup
    ```

    

    `setup init` is idempotent over `data/`: re-running it reuses the tunnel ID and CA already stored there and never creates a second tunnel. A new CA is generated and registered only when `data/` is empty or `TUNNEL_ID` has changed; in that case the cap of two active certificates applies, so revoke one in the Console first if both slots are filled.

    See [Setup component authentication failures](/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#setup-component-authentication-failures) if it errors.

    Retrieve your tunnel domain and export it for later steps:

    ``` shiki
    export TUNNEL_DOMAIN=$(sudo cat data/tunnel-domain)
    echo "$TUNNEL_DOMAIN"
    ```

    

    
    Workload Identity Federation tokens are short-lived (1 hour by default) and expire automatically; there is nothing to revoke after setup completes.

4.  4

    ### Write the proxy config

    `tunnel_domain` is **required**: the [proxy](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) uses it to strip the domain suffix from incoming hostnames before looking up the subdomain in `routes`. `routes` is a flat map from subdomain to upstream URL, not a list.

    ``` shiki
    cat > config/mcp-proxy.yaml <<EOF
    listen_addr: ":8080"
    log_level: info
    shutdown_timeout: 30s
    tunnel_domain: ${TUNNEL_DOMAIN}
    tls:
      cert_file: /data/tls.crt
      key_file: /data/tls.key
    routes:
      echo: http://hello-mcp:9000
    EOF
    ```

    

    The `echo:` route targets the [sample MCP server](#optional-use-a-sample-mcp-server); replace it with (or add) your own routes. See the [proxy configuration](/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration) reference for all available fields.

5.  5

    ### Start the deployment

    ``` shiki
    export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
    docker compose up -d
    ```

    

The compose file reads `TUNNEL_TOKEN` from the host environment with no default, so the export must be repeated in every fresh shell and after a reboot.

For a multi-VM deployment, copy the `mcp-tunnel/` directory to each host, set `TUNNEL_TOKEN`, and run `docker compose up -d`. In the programmatic flow `TUNNEL_TOKEN` is `$(sudo cat data/tunnel-token)`; in the manual flow it's the value you copied from the Console. The same tunnel token and certificates work across all replicas.

## Verify the deployment

Verify end to end by calling an [upstream MCP server](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) from Anthropic's side: see [Use the tunneled MCP servers](/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers). With the [sample MCP server](#optional-use-a-sample-mcp-server), the routed URL is `https://echo.<your-tunnel-domain>/mcp`. If verification fails, see [Troubleshooting](/docs/en/agents-and-tools/mcp-tunnels/troubleshooting).

## Upgrades

Run the commands in this section from inside the `mcp-tunnel/` deployment directory.

### Rotate the tunnel token

With programmatic access, increment `--token-version` in the `setup` service command, set the Workload Identity Federation identifiers, mint a fresh OIDC JWT, and re-run the setup component:

```python
# Edit docker-compose.yaml: increment the integer in the setup service's
# --token-version argument (for example, --token-version=1 to
# --token-version=2). The setup binary refuses to rotate when the value
# hasn't changed.

# export TUNNEL_ID=tnl_...   # set only if you set it during install
export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
# export ANTHROPIC_WORKSPACE_ID=wrkspc_...   # if your rule is workspace-scoped
# Re-mint ANTHROPIC_IDENTITY_TOKEN per the WIF provider guide for your
# environment (it will have expired since install).
export ANTHROPIC_IDENTITY_TOKEN=...

docker compose run --rm setup

export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
docker compose up -d cloudflared
```



The `--token-version` argument is edited in `docker-compose.yaml` rather than passed on the command line so the new value persists for future runs of the setup component. The setup component authenticates with Workload Identity Federation; there is no API token to revoke.

Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `TUNNEL_TOKEN` environment variable on each host and restart cloudflared (`docker compose up -d cloudflared`).



Clicking **Rotate token** invalidates the current token immediately. Between that moment and updating `TUNNEL_TOKEN` on every host and restarting cloudflared, any host whose cloudflared restarts (crash, host reboot) cannot reconnect. Update each host promptly after rotating.

### Certificate renewal

You're responsible for monitoring expiry and renewing the server certificate before it expires.

With programmatic access:

```python
docker compose run --rm setup renew-cert --output=dir:/data
```



The CLI arguments replace the `setup` service's `command` (the `init` arguments) but keep its `entrypoint`, so this runs `/setup renew-cert --output=dir:/data`.



Pass `--renew-before=720h` to make the command a no-op when more than 30 days of validity remain. This makes it safe to run on a fixed schedule.

Without programmatic access, sign a new server certificate with your existing CA (the CA registered in the Console doesn't change) and replace `data/tls.crt`. Set `TUNNEL_DOMAIN` first if you're running this from a fresh shell.

```python
export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 \
  -extfile data/tls.ext
```



In either flow the proxy polls `tls.cert_file` and reloads it automatically, so no restart is required.

## Next steps



[Use the tunneled MCP servers](/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers)

Attach an upstream MCP server to a Managed Agent or the Messages API.



[Security](/docs/en/agents-and-tools/mcp-tunnels/security)

Hardening guidance, credential rotation, and breach response.



[Troubleshooting](/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)

Diagnose connectivity, TLS, and routing issues.
