---
title: "Deploy MCP tunnels with Helm - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:18Z"
tags: ["api", "mcp"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fdeploy-helm)

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

# Deploy MCP tunnels with Helm

Copy page



Install the tunnel stack on a Kubernetes cluster using the Anthropic Helm chart.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

The Anthropic Helm chart installs the [tunnel stack](agents-and-tools-mcp-tunnels-concepts.md#components) as a single Deployment and attaches it to your tunnel: one the chart's setup hook creates for you, or an existing tunnel you created in the [Console](agents-and-tools-mcp-tunnels-console.md#create-a-tunnel).

## Before you begin

You need:

- **A tunnel.** With programmatic access, the chart's setup hook creates one for you when you don't supply a tunnel ID; to attach to an existing tunnel instead, [create it in the Console](agents-and-tools-mcp-tunnels-console.md#create-a-tunnel) and record the tunnel ID (`tnl_...`). Manual provisioning always starts from a Console-created tunnel; you'll also need its tunnel token and tunnel domain.
- **A way for the chart to authenticate to the Tunnels API.**
  - **[Programmatic access](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning) (recommended).** The [setup component](agents-and-tools-mcp-tunnels-concepts.md#components) authenticates through Workload Identity Federation, fetches the tunnel token, generates a CA, registers it with Anthropic, and stores everything in a Secret. You'll need a federation rule scoped to `workspace:manage_tunnels`.
  - **[Manual](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning).** Skip programmatic access. You'll [get the tunnel token from the Console](agents-and-tools-mcp-tunnels-console.md#get-the-connection-details), generate a CA and server certificate yourself, [register the CA in the Console](agents-and-tools-mcp-tunnels-console.md#add-a-ca-certificate), and supply the credentials to the cluster as Secrets.
- **A Kubernetes cluster** you can deploy to with `helm` and `kubectl`. The **Without programmatic access** tab also uses `openssl` (1.1.1 or later).
- **Outbound network connectivity** from the cluster to `api.anthropic.com` (443 TCP) and the [tunnel edge](agents-and-tools-mcp-tunnels-concepts.md#components) (7844 TCP and UDP). See the full [network requirements](agents-and-tools-mcp-tunnels-overview.md#network-requirements).
- **One or more MCP servers** running and reachable from the cluster on the addresses you'll configure under `gateway.config.routes`. If you don't have one yet, [use the sample server](#optional-use-a-sample-mcp-server).

## Optional: Use a sample MCP server

If you don't have an MCP server available for testing, use this minimal one:

```python
kubectl create namespace mcp-tunnel --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel apply -f - <<'EOF'
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-mcp-src
data:
  hello_server.py: |
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)


    @mcp.tool()
    def hello(name: str = "world") -> str:
        """Say hello to someone."""
        return f"Hello, {name}!"


    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-mcp
spec:
  replicas: 1
  selector:
    matchLabels: { app: hello-mcp }
  template:
    metadata:
      labels: { app: hello-mcp }
    spec:
      containers:
        - name: hello-mcp
          image: python:3.13-slim
          command: ["sh", "-c", "pip install --quiet mcp && python /app/hello_server.py"]
          volumeMounts:
            - { name: src, mountPath: /app }
          ports:
            - { containerPort: 9000 }
      volumes:
        - name: src
          configMap: { name: hello-mcp-src }
---
apiVersion: v1
kind: Service
metadata:
  name: hello-mcp
spec:
  selector: { app: hello-mcp }
  ports:
    - { port: 9000, targetPort: 9000 }
EOF
```



The Install steps that follow note where to add the corresponding route.

## Install

With programmatic access

Without programmatic access

The setup component exchanges the cluster's projected ServiceAccount token through your federation rule, fetches the tunnel token, generates a CA and server certificate, and registers the CA with Anthropic. A daily CronJob renews the server certificate as needed, so you don't handle any secrets by hand.

1.  1

    ### Set up Workload Identity Federation for the cluster

    Follow [Use WIF with Kubernetes](../Other/manage-claude-wif-providers-kubernetes.md) to register your cluster's OIDC issuer and create a federation rule. The setup component runs under its own ServiceAccount in the release namespace; the exact name follows Helm's `fullname` convention, so for any release name other than `mcp-tunnel`, run `helm template <release> ... | grep -A2 'kind: ServiceAccount'` to confirm it before creating the rule. The rest of this guide assumes release name `mcp-tunnel` in namespace `mcp-tunnel`, where the ServiceAccount is `mcp-tunnel-setup`.

    | Field    | Value                                                |
    |----------|------------------------------------------------------|
    | Subject  | `system:serviceaccount:mcp-tunnel:mcp-tunnel-setup`  |
    | Audience | `api.anthropic.com` (the chart's default; no scheme) |
    | Scope    | `workspace:manage_tunnels`                           |

    
    The chart's default audience is `api.anthropic.com` with no scheme, but the Console's federation-rule form suggests `https://api.anthropic.com`. The two must match byte-for-byte or authentication fails. Either set the rule's audience to `api.anthropic.com`, or set `api.wif.audience` in `values.yaml` to `https://api.anthropic.com`.

    If the tunnel is in a workspace other than the organization's default, also add the rule's service account as a member of that workspace under **Settings \> Workspaces** (the Tunnels API authorizes against the service account's workspace memberships).

    Note the rule's ID (`fdrl_...`); you'll set it as `api.wif.federationRuleId`.

    
    The daily certificate-renewal CronJob uses a separate ServiceAccount (also derived from the Helm `fullname`) but does not call the Tunnels API; it renews the certificate locally and only needs Kubernetes RBAC, which the chart grants. The federation rule does not need to cover it.

2.  2

    ### Fetch the default values

    ``` shiki
    helm show values \
      oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
      --version 2.0.2 > values.yaml
    ```

    

3.  3

    ### Configure tunnel attachment and routes

    Edit `values.yaml` and set the `api.wif.*` keys with the federation rule ID and organization ID, plus a `routes` entry for each [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components):

    values.yaml

    

    ``` shiki
    api:
      wif:
        federationRuleId: "fdrl_..."
        organizationId: "00000000-0000-0000-0000-000000000000"
        # Set when the tunnel is in a non-default workspace and the
        # rule's service account is a member of that workspace.
        # workspaceId: "wrkspc_..."

    tunnel:
      # Leave empty to have the setup hook create a tunnel during install.
      # Set to attach to an existing tunnel from the Console.
      id: ""
      # Increment to rotate the tunnel token on the next upgrade.
      # See the "Rotate the tunnel token" section.
      tokenVersion: "1"

    gateway:
      config:
        routes:
          docs: http://docs-mcp.internal:8080
          search: http://search-mcp.internal:8080
    ```

    With these routes, Claude reaches the servers at `docs.<your-tunnel-domain>` and `search.<your-tunnel-domain>`. Some managed Kubernetes distributions allocate the Service CIDR outside the standard private ranges; if your routes target in-cluster Services, add `gateway.config.upstream.allowed_ips` here per [Upstream IP validation](agents-and-tools-mcp-tunnels-troubleshooting.md#upstream-ip-validation).

    
    If you're using the [sample MCP server](#optional-use-a-sample-mcp-server), set `routes` to `echo: http://hello-mcp:9000` instead.

4.  4

    ### Review the rendered manifests

    Render the chart and review the output according to your organization's vetting practices:

    ``` shiki
    helm template mcp-tunnel \
      oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
      --version 2.0.2 \
      -n mcp-tunnel \
      -f values.yaml > rendered.yaml
    ```

    

5.  5

    ### Install

    ``` shiki
    helm install mcp-tunnel \
      oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
      --version 2.0.2 \
      --namespace mcp-tunnel --create-namespace \
      -f values.yaml
    ```

    

    The setup component runs as a Helm pre-install hook Job, so `helm install` blocks until it completes. On success Helm deletes the Job automatically. If `helm install` fails with a hook error, see [Setup component authentication failures](agents-and-tools-mcp-tunnels-troubleshooting.md#setup-component-authentication-failures).

    When `tunnel.id` is empty, the setup component creates the tunnel in the workspace your federation rule targets (the organization's default workspace unless you set `api.wif.workspaceId`) and stores its ID and domain in the `mcp-tunnel` Secret. Find the domain you'll need for [verification](#verify-the-deployment) on the tunnel's detail page in the Console under **Manage \> MCP tunnels**, or read it from the Secret:

    ``` shiki
    kubectl -n mcp-tunnel get secret mcp-tunnel \
      -o jsonpath='{.data.tunnel-domain}' | base64 -d
    ```

    

    Re-running the setup component (during [upgrades](#upgrades) or [token rotation](#rotate-the-tunnel-token)) reuses the tunnel ID stored in this Secret; it never creates a second tunnel.

    
    The `api.wif.*` values are identifiers, not secrets, so storing them in Helm release-history Secrets is not a risk. The sensitive data at rest is the `mcp-tunnel` Secret the setup component creates, which holds the tunnel token and TLS private keys. Apply your organization's standard practices for protecting Kubernetes Secrets to this namespace.

## Verify the deployment

Verify end to end from Anthropic's side: use `https://<route>.<your-tunnel-domain>/<path>` in a Managed Agent session or a Messages API request, where `<route>` is a key from `gateway.config.routes` and `<path>` is whatever the upstream MCP server serves at. With the [sample MCP server](#optional-use-a-sample-mcp-server), that's `https://echo.<your-tunnel-domain>/mcp`. See [Use the tunneled MCP servers](agents-and-tools-mcp-tunnels-overview.md#use-the-tunneled-mcp-servers) for the request shapes.

If that fails, check the pod logs (`kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c mcp-proxy` and `-c cloudflared`) and consult [Troubleshooting](agents-and-tools-mcp-tunnels-troubleshooting.md).

## Optional configuration

### Restrict egress with NetworkPolicy

Ingress to the proxy pod is denied by default (`networkPolicy.ingress.enabled: true`). To additionally restrict pod egress, set `networkPolicy.egress.enabled: true` and populate `networkPolicy.egress.mcpServers` with pod label selectors or CIDR ranges that cover your upstream MCP servers. Egress from cloudflared to the tunnel edge is allowed separately through `networkPolicy.egress.cloudflaredEgressCIDRs`.

### Tune the proxy

Fields under `gateway.config.*` pass through to the proxy configuration file. Common adjustments include `upstream.allowed_ips`, `log_level`, and `upstream.tls`. See the [proxy configuration](agents-and-tools-mcp-tunnels-reference.md#proxy-configuration) reference for the full field list. The chart always sets `listen_addr`, `tls.cert_file`, and `tls.key_file`; setting them in `gateway.config` has no effect.

### Supply your own OIDC token

By default the chart projects a Kubernetes ServiceAccount token for the setup component. To use a token from a different identity provider (such as [SPIFFE](../Other/manage-claude-wif-providers-spiffe.md), Vault, or a cloud-SDK sidecar), mount it with `setup.extraVolumes` and `setup.extraVolumeMounts`. Then point `api.wif.tokenFile` at the mount path. The chart sets `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path, and the setup component reads the token from there.

## Upgrades

Always pass `--version` to `helm upgrade` so you don't pull a newer chart unexpectedly.

### Upgrade from chart 1.x

Chart 2.0.0 moves the tunnel ID from `api.wif.tunnelId` to `tunnel.id`. Before upgrading, edit your `values.yaml`: move the `tnl_...` value to `tunnel.id` and remove `api.wif.tunnelId`. Leaving `tunnel.id` unset is safe (the setup component reuses the tunnel ID already stored in the `mcp-tunnel` Secret on re-run), but the explicit move keeps your `values.yaml` accurate. Also update your federation rule's scope from `org:manage_tunnels` to `workspace:manage_tunnels` in the Console.

### Change configuration

For routine changes such as routes, replica count, or NetworkPolicy:

```python
helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 2.0.2 \
  -n mcp-tunnel \
  -f values.yaml
```





Maintain a complete `values.yaml` rather than relying on `--reuse-values`. Helm's deep-merge behavior can silently fail to remove deleted routes.

### Rotate the tunnel token

With programmatic access, increment `tunnel.tokenVersion` in `values.yaml` and upgrade with `--set setup.force=true`. The setup component only re-runs on upgrades when forced:

```python
helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 2.0.2 \
  -n mcp-tunnel \
  -f values.yaml \
  --set setup.force=true
```



The setup component authenticates with Workload Identity Federation; there is no API token to revoke.

Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `mcp-tunnel-token` Secret:

```python
kubectl -n mcp-tunnel create secret generic mcp-tunnel-token \
  --from-literal=tunnel-token='eyJ...' --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel rollout restart deploy/mcp-tunnel
```





Clicking **Rotate token** invalidates the current token immediately. Until the Secret is updated and the rollout completes, any pod that restarts with the old token (eviction, node drain, OOM) cannot reconnect. Update the Secret promptly after rotating; for stricter availability requirements, use programmatic access so the chart handles the rotation atomically.

### Certificate renewal

The chart provides automation, but you remain responsible for monitoring expiry and confirming renewal completes.

With programmatic access, certificate renewal is automatic. The chart deploys a CronJob (named after the Helm `fullname`, suffixed `-cert-renew`) that runs `setup renew-cert` daily (at `serverCert.cronSchedule`, default `0 0 * * *` UTC). The job is a no-op unless the certificate is within `serverCert.renewBefore` of expiry (default 30 days). Renewal is local: the job signs a fresh certificate with the CA already stored in the Secret, makes no API calls, and only needs the Kubernetes RBAC the chart grants. The proxy hot-reloads the certificate from the Secret mount, so no Deployment restart is needed.

Without programmatic access there is no CronJob. From inside the `mcp-tunnel/` directory you kept after install, sign a fresh server certificate with the existing CA (do not regenerate the CA):

```python
export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 -extfile data/tls.ext

kubectl -n mcp-tunnel create secret generic mcp-tunnel-cert \
  --from-file=tls.crt=data/tls.crt --from-file=tls.key=data/tls.key \
  --dry-run=client -o yaml | kubectl apply -f -
```



The proxy hot-reloads the certificate from the Secret mount.

## Next steps



[Use the tunneled MCP servers](agents-and-tools-mcp-tunnels-overview.md#use-the-tunneled-mcp-servers)

Attach an upstream MCP server to a Managed Agent or the Messages API.



[Security](agents-and-tools-mcp-tunnels-security.md)

Hardening guidance, credential rotation, and breach response.



[Troubleshooting](agents-and-tools-mcp-tunnels-troubleshooting.md)

Diagnose connectivity, TLS, and routing issues.
