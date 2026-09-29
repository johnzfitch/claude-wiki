---
title: "MCP tunnels reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:21Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Freference)

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

# MCP tunnels reference

Copy page



Proxy configuration fields, the Tunnels REST API, certificate requirements, and the setup component.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

## Proxy configuration

The [proxy](agents-and-tools-mcp-tunnels-concepts.md#components) reads its configuration from `/etc/mcp-gateway/config.yaml` (Compose) or the rendered ConfigMap (Helm, populated from `gateway.config.*`).

| Field                             | Description                                                                                                                                                                                                     | Default                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `listen_addr`                     | Address and port to listen on.                                                                                                                                                                                  | Required                                        |
| `log_level`                       | Logging verbosity: `debug`, `info`, `warn`, or `error`.                                                                                                                                                         | `info`                                          |
| `shutdown_timeout`                | How long to wait for in-flight requests during graceful shutdown.                                                                                                                                               | `30s`                                           |
| `tunnel_domain`                   | Base domain assigned to the tunnel. When set, route lookup strips this suffix from incoming hostnames so `routes` keys can be bare subdomains (`wiki`). When empty, `routes` keys must be exact full hostnames. | Required when `routes` keys are bare subdomains |
| `tls.cert_file`                   | Path to the server TLS certificate.                                                                                                                                                                             | Required                                        |
| `tls.key_file`                    | Path to the server TLS private key.                                                                                                                                                                             | Required                                        |
| `routes`                          | Map of subdomain or full hostname to upstream URL. See [Route matching](#route-matching).                                                                                                                       | Required                                        |
| `upstream.allowed_ips`            | IPv4 CIDR ranges or single addresses the proxy is permitted to connect to. Mutually exclusive with `disable_ip_validation`.                                                                                     | RFC1918 private ranges                          |
| `upstream.disable_ip_validation`  | Disable upstream IP validation entirely. Mutually exclusive with `allowed_ips`.                                                                                                                                 | `false`                                         |
| `upstream.tls.ca_file`            | CA bundle for validating upstream TLS.                                                                                                                                                                          | None                                            |
| `upstream.tls.include_system_cas` | Also trust the system CA bundle for upstream TLS.                                                                                                                                                               | `false`                                         |

For `https://` upstream routes, set at least one of `upstream.tls.ca_file` or `upstream.tls.include_system_cas`; otherwise the proxy has no trust anchor for the upstream certificate.

### Route matching

`routes` is a flat string map (`map[string]string`), not a list. The proxy looks up the incoming hostname by exact match first, then by stripping the `tunnel_domain` suffix and matching the remaining subdomain. The match considers only the hostname; the request path and query string are forwarded to the [upstream MCP server](agents-and-tools-mcp-tunnels-concepts.md#components) unchanged.

Each upstream value must be exactly `scheme://host:port`. The port is mandatory. Including a path is rejected at config load with `invalid upstream (must be scheme://host:port)`.

## Tunnels API

The Tunnels REST API lives at `/v1/tunnels` and supports creating, listing, and archiving tunnels, registering CA certificates, and revealing or rotating the tunnel token. See the [Tunnels API reference](../Endpoints/http-beta-tunnels-list.md) for all endpoints, request and response schemas, and examples.



The previous Admin API surface at `/v1/organizations/tunnels` (beta header `mcp-tunnels-2026-05-19`, scope `org:manage_tunnels`) continues to work during a migration window and remains documented in the [Admin API reference](../Admin/beta-organization-mcp-tunnels.md) with a deprecation notice. To migrate, update the path to `/v1/tunnels`, the beta header to `mcp-tunnels-2026-06-22`, and your WIF token scope to `workspace:manage_tunnels`.



All MCP tunnels endpoints require a bearer token with the `workspace:manage_tunnels` scope obtained through [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md). Admin API keys are not accepted.

Required headers on every request:

| Header              | Value                                      |
|---------------------|--------------------------------------------|
| `Authorization`     | `Bearer <token>` (the WIF-exchanged token) |
| `anthropic-version` | `2023-06-01`                               |
| `anthropic-beta`    | `mcp-tunnels-2026-06-22`                   |

## Certificate requirements

The [setup component](agents-and-tools-mcp-tunnels-concepts.md#components) generates compliant certificates automatically. These requirements apply only if you issue certificates through your own PKI.

### CA certificate

Upload with `POST /v1/tunnels/{tunnel_id}/certificates`. A tunnel can hold up to two active CA certificates at a time, which allows zero-downtime rotation.

- PEM-encoded, single certificate, up to 8 kB.
- `BasicConstraints` extension present with `CA:TRUE`, marked critical.
- `SubjectKeyIdentifier` extension present.
- `KeyUsage` includes `keyCertSign`.
- Within its validity period.
- RSA 2048-bit or larger, or ECDSA P-256 or larger, with a SHA-256 or stronger signature.

### Server certificate

Presented by the proxy during [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components).

- Signed directly by a registered CA (no intermediates).
- `AuthorityKeyIdentifier` extension present and matching the CA's `SubjectKeyIdentifier`.
- Subject Alternative Name includes a DNS name matching `<route>.<tunnel-domain>`. A wildcard `*.<tunnel-domain>` covers all routes.
- If the `ExtendedKeyUsage` extension is present, it includes `serverAuth`.
- Within its validity period.
- RSA 2048-bit or larger, or ECDSA P-256 or larger, with a SHA-256 or stronger signature.

The setup component generates an ECDSA P-256 CA with five-year validity and an RSA 4096-bit server certificate with a wildcard SAN and 90-day validity.

## Setup component

The setup component ships inside the `mcp-proxy` image as the `setup` binary. Run it with `docker compose run --rm setup <subcommand>` (Compose) or rely on the chart's hooks and CronJobs (Helm).

### `setup init`

Attaches to an existing tunnel (or creates one when no tunnel ID is supplied), then generates a CA and server certificate, registers the CA, retrieves the tunnel token, and writes all outputs to the destination.

| Flag              | Description                                                                                                                                                           | Default                                                                                      |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `--api-url`       | Claude API base URL. Also read from `API_URL`.                                                                                                                        | Required                                                                                     |
| `--tunnel-id`     | Tunnel ID to attach to (`tnl_...`). Also read from `TUNNEL_ID`. When omitted, a new tunnel is created; a tunnel ID already stored in the output is reused on re-runs. | None (create a tunnel)                                                                       |
| `--output`        | Output destination: `dir:/path` or `k8s-secret:NAME`. The Helm chart passes `k8s-secret:<release>`.                                                                   | `k8s-secret:mcp-tunnel` (auto-detected when running in a Kubernetes pod; required otherwise) |
| `--cert-duration` | Server certificate validity period.                                                                                                                                   | `2160h` (90 days)                                                                            |
| `--token-version` | Change-detection string. A new value triggers token rotation on re-run. The Helm chart and the Compose example both pass `1` as the initial value.                    | None                                                                                         |

The command authenticates through [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md). It reads `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_WORKSPACE_ID` (optional), and exactly one of `ANTHROPIC_IDENTITY_TOKEN_FILE` or `ANTHROPIC_IDENTITY_TOKEN`. See the [WIF reference](../Other/manage-claude-wif-reference.md) for the current semantics of these variables; the setup component derives the service account from the federation rule, so it does not require `ANTHROPIC_SERVICE_ACCOUNT_ID` separately.

### `setup renew-cert`

Issues a new server certificate signed by the stored CA. Makes no API calls.

| Flag              | Description                                                                                         | Default                                                                                      |
|-------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `--output`        | Output destination: `dir:/path` or `k8s-secret:NAME`. The Helm chart passes `k8s-secret:<release>`. | `k8s-secret:mcp-tunnel` (auto-detected when running in a Kubernetes pod; required otherwise) |
| `--cert-duration` | New certificate validity period.                                                                    | `2160h` (90 days)                                                                            |
| `--renew-before`  | Skip renewal if the existing certificate has more than this duration remaining.                     | `0` (always renew)                                                                           |

Setting `--renew-before=720h` makes the command a no-op when more than 30 days of validity remain, so it's safe to run on a fixed schedule.
