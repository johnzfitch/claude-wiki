---
title: "Manage tunnels in the Console - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:11Z"
tags: ["agents", "api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-tunnels%2Fconsole)

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

# Manage tunnels in the Console

Copy page



Create tunnels, register CA certificates, retrieve the tunnel token, and attach tunneled MCP servers to agents from the Claude Console.

Copy page





MCP tunnels are in research preview. [Request access](https://claude.com/form/mcp-tunnels) to try them.

This page covers the Console side of an MCP tunnels deployment: creating a tunnel, registering your CA certificate, retrieving the tunnel token, and attaching the [upstream MCP servers](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) to an agent. [Deploy MCP tunnels with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm) and [Deploy MCP tunnels with Docker Compose](/docs/en/agents-and-tools/mcp-tunnels/deploy-compose) cover running the [tunnel stack](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) inside your network.

## Prerequisites

- **One or more MCP servers** running in your private network. The tunnel routes traffic to them; it does not host them. See [Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers) for examples you can deploy.
- **A Console role with the Manage tunnels permission**, so you can create and archive tunnels, rotate the token, and manage certificates. Organization admins and owners have it by default; custom roles and per-account grants can also include it. Roles without it have read-only access to the **MCP tunnels** page and tunnel details.
- **A way for your stack to authenticate to the Tunnels API.** Choose one:
  - **[Programmatic access](/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning) (recommended).** Set up [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation) during tunnel creation so your stack mints short-lived API tokens from your identity provider, fetches the tunnel token, and generates and registers a CA certificate automatically. Requires permission to manage federation rules, a registered OIDC issuer, and a federation rule with the `workspace:manage_tunnels` scope.
  - **[Manual](/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning).** Skip programmatic access. After creating the tunnel, [get the tunnel token](#get-the-connection-details), generate and [register a CA certificate](#add-a-ca-certificate) yourself, and supply the token and your server certificate to your tunnel stack as secrets.

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

    Programmatic access relies on [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation); read that page first if federation issuers, rules, and service accounts are unfamiliar. To turn the toggle on you need:

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

    What else you need depends on the [credential-provisioning mode](/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning):

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

Every reveal and rotation is recorded in your organization's [Compliance API](/docs/en/manage-claude/compliance-api) activity log. Rotation does not sever cloudflared connections that are already established, so you can rotate, redeploy with the new value, and let the old connections drain.

## Add a CA certificate

Anthropic verifies [inner TLS](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) to your [proxy](/docs/en/agents-and-tools/mcp-tunnels/concepts#components) against the CA certificates you register on the tunnel. A tunnel with no active certificates cannot accept connections, and does not appear in the agent MCP server picker until one is registered.

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

[Deploy with Docker Compose](/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)

Run the tunnel stack on a single host. Both programmatic-access and manual flows.



[Deploy with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)

Run the tunnel stack on a Kubernetes cluster. Both programmatic-access and manual flows.

## Use the tunnel in an agent

Once your stack is running and has one or more MCP servers configured, attach an upstream MCP server to a Managed Agent session. To call the same servers from the Messages API instead, see [Use the tunneled MCP servers](/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers).

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

[Deploy with Helm](/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)

Install on a Kubernetes cluster using the Anthropic Helm chart.



[Security](/docs/en/agents-and-tools/mcp-tunnels/security)

Hardening guidance, credential rotation, and breach response.
