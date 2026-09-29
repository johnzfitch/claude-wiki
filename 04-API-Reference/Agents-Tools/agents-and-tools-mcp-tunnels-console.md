---
title: "Manage tunnels in the Console - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:11Z"
tags: ["agents", "api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fconsole)

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

# Manage tunnels in the Console

Copy page



Create tunnels, register CA certificates, retrieve the tunnel token, and attach tunneled MCP servers to agents from the Claude Console.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

This page covers the Console side of an MCP tunnels deployment: creating a tunnel, registering your CA certificate, retrieving the tunnel token, and attaching the [upstream MCP servers](agents-and-tools-mcp-tunnels-concepts.md#components) to an agent. [Deploy MCP tunnels with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md) and [Deploy MCP tunnels with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md) cover running the [tunnel stack](agents-and-tools-mcp-tunnels-concepts.md#components) inside your network.

## Prerequisites

- **One or more MCP servers** running in your private network. The tunnel routes traffic to them; it does not host them. See [Remote MCP servers](agents-and-tools-remote-mcp-servers.md) for examples you can deploy.
- **A Console role with the Manage tunnels permission**, so you can create and archive tunnels, rotate the token, and manage certificates. Organization admins and owners have it by default; custom roles and per-account grants can also include it. Roles without it have read-only access to the **MCP tunnels** page and tunnel details.
- **A way for your stack to authenticate to the Tunnels API.** Choose one:
  - **[Programmatic access](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning) (recommended).** Set up [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md) during tunnel creation so your stack mints short-lived API tokens from your identity provider, fetches the tunnel token, and generates and registers a CA certificate automatically. Requires permission to manage federation rules, a registered OIDC issuer, and a federation rule with the `workspace:manage_tunnels` scope.
  - **[Manual](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning).** Skip programmatic access. After creating the tunnel, [get the tunnel token](#get-the-connection-details), generate and [register a CA certificate](#add-a-ca-certificate) yourself, and supply the token and your server certificate to your tunnel stack as secrets.

## Create a tunnel

1.  1

    ### Open the MCP tunnels page

    In the Console sidebar, go to **Manage \> MCP tunnels**. Tunnels are workspace-scoped; the new tunnel belongs to the workspace currently selected in the Console, so switch workspaces first if you want it elsewhere.

2.  2

    ### Name the tunnel

    Click **New tunnel** and enter a name in the **Create tunnel** dialog. The name is required and identifies the tunnel in the list, on the detail page, and in the agent MCP server picker. A domain of the form `abcd1234.tunnel.anthropic.com` is assigned automatically.

3.  3

    ### Optionally set up programmatic access

    If your role can manage federation rules, a **Set up programmatic access** toggle appears (off by default). If not, the Console shows a notice in its place and your tunnel stack uses the manual flow instead. The rest of the create flow is the same either way.

    Programmatic access relies on [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md); read that page first if federation issuers, rules, and service accounts are unfamiliar. To turn the toggle on you need:

    1.  **A registered OIDC issuer** for the identity provider your stack presents tokens from (such as a Kubernetes cluster, AWS IAM, Google Cloud, or GitHub Actions). Register one under **Settings \> Workload identity \> Issuers** if your organization doesn't have one.
    2.  **A federation rule with the `workspace:manage_tunnels` scope.** Turning on the toggle reveals a **Federation rule** picker. Choose an existing rule with that scope, or click **Create federation rule** to create one inline.
    3.  **The rule's service account added to this workspace.** The Tunnels API authorizes against the service account's workspace memberships. If you're creating the tunnel in a workspace other than the organization's default, add the service account under **Settings \> Workspaces** and pass the workspace ID at deploy time (`api.wif.workspaceId` for Helm, `ANTHROPIC_WORKSPACE_ID` for Compose).

    Skipping this step is fully supported; both deploy guides have a **Without programmatic access** tab.

4.  4

    ### Create the tunnel

    Click **Create tunnel**. The Console provisions the tunnel and opens the detail page.

5.  5

    ### Record the deployment identifiers

    Both deploy paths need:

    - The **tunnel ID** (`tnl_...`), shown on the tunnel detail page.
    - The **tunnel domain** (`abcd1234.tunnel.anthropic.com`), shown on the tunnel detail page. Used as the proxy's `tunnel_domain` and in the server certificate's SAN.

    What else you need depends on the [credential-provisioning mode](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning):

    | With programmatic access                                                                                                                                                     | Without programmatic access                                                                                                                                                 |
    |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | The **federation rule ID** (`fdrl_...`) of the rule you selected. The rule is org-level, not stored on the tunnel; find it under **Settings \> Workload identity \> Rules**. | The **tunnel token**, revealed with the eye icon next to **Token** on the detail page. Treat it as a secret. See [Get the connection details](#get-the-connection-details). |
    | The **organization ID** (a UUID), shown under **Settings \> Organization**.                                                                                                  | A **CA certificate** that you generate and [register on the tunnel](#add-a-ca-certificate).                                                                                 |

    With programmatic access, your stack fetches the tunnel token through the Tunnels API, generates the CA and server certificate locally (the private key never leaves your environment), and registers only the CA's public certificate with Anthropic. You're still responsible for securing the private keys and renewing the server certificate before it expires.

Your organization can have up to 10 active tunnels. Creating a tunnel does not establish any connectivity; that happens once your stack dials in with the tunnel token and a CA certificate is registered.

## Get the connection details

Open the tunnel. The detail page shows a **Connection** section with the domain and token and a **Certificates** section.

| Field      | Description                                                                                                                                                                                                         |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Domain** | Copy the assigned `abcd1234.tunnel.anthropic.com` value. Your proxy's routes are subdomains of this domain.                                                                                                         |
| **Token**  | Click the eye icon (**Show token**) to fetch the tunnel token, then use the copy icon to copy it into your tunnel stack's secret store. Click **Rotate token** to invalidate the current token and issue a new one. |



Every reveal and rotation is recorded in your organization's [Compliance API](../Other/manage-claude-compliance-api.md) activity log. Rotation does not sever cloudflared connections that are already established, so you can rotate, redeploy with the new value, and let the old connections drain.

## Add a CA certificate

Anthropic verifies [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components) to your [proxy](agents-and-tools-mcp-tunnels-concepts.md#components) against the CA certificates you register on the tunnel. A tunnel with no active certificates cannot accept connections, and does not appear in the agent MCP server picker until one is registered.

1.  1

    ### Find the Certificates section

    On the tunnel's detail page, scroll to the **Certificates** section and click **Add certificate**.

2.  2

    ### Provide the certificate

    Click **Choose file** to select a `.pem`, `.crt`, or `.cer` file, drag the file onto the text area, or paste the PEM block directly. The modal rejects private-key material and content that isn't a `-----BEGIN CERTIFICATE-----` block. The file must be 8 kB or smaller.

3.  3

    ### Add the certificate

    Click **Add certificate**. The fingerprint and expiry appear in the certificate list, and the slot count on the section header increments.

A tunnel holds up to two active certificates so you can rotate without downtime: register the new certificate alongside the old one, redeploy your proxy with the new key pair, confirm traffic is flowing, then click **Revoke** on the old certificate's row. Revoked certificates remain visible in the list with a **Revoked** badge.

## Deploy the tunnel stack

The tunnel exists in the Console, but no traffic flows until the tunnel stack is running inside your network and dialed in with the tunnel token. Follow one of the deploy guides:



[Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md)

Run the tunnel stack on a single host. Both programmatic-access and manual flows.



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Run the tunnel stack on a Kubernetes cluster. Both programmatic-access and manual flows.

## Use the tunnel in an agent

Once your stack is running and has one or more MCP servers configured, attach an upstream MCP server to a Managed Agent session. To call the same servers from the Messages API instead, see [Use the tunneled MCP servers](agents-and-tools-mcp-tunnels-overview.md#use-the-tunneled-mcp-servers).



The picker only shows tunnels with at least one active certificate. A tunnel that still shows **Needs certificate** in the **MCP tunnels** list does not appear in the dropdown; register a CA certificate first. The picker is also workspace-scoped: it lists tunnels in the same workspace as the session, not other workspaces.

1.  1

    ### Open the New session modal

    Go to **Managed Agents \> Sessions** and click **New session**.

2.  2

    ### Define an inline agent

    In the agent picker, choose **Create new agent** so you can edit the MCP server list directly.

3.  3

    ### Add the MCP server

    Click **+ MCP Server** and open the dropdown. Tunnels created in the current workspace appear at the top of the list, above the public connector catalog. Select the tunnel that fronts the server you want to reach.

4.  4

    ### Supply the routing

    The card shows two optional fields: **Subdomain** (prefixed to the tunnel domain) and **Path** (appended after it). Fill in one or both, depending on how your proxy's routes are configured. The **Resolves to** line shows the full MCP server URL that the agent connects to.



The tunnel carries traffic; it does not authenticate to the upstream MCP server. Configure OAuth or bearer auth on the MCP server the same way as for any other MCP server.

## Archive a tunnel

Archiving immediately stops the tunnel from accepting connections and is permanent.

In the **MCP tunnels** list, open the row menu for the tunnel and choose **Archive**. Archived tunnels remain visible when you filter the list by **Archived** or **All**.

## Next steps



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Install on a Kubernetes cluster using the Anthropic Helm chart.



[Security](agents-and-tools-mcp-tunnels-security.md)

Hardening guidance, credential rotation, and breach response.
