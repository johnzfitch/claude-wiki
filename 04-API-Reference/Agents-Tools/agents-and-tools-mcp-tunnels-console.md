---
title: "Manage tunnels in the Claude Console - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-06T06:26:38Z"
tags: ["agents", "api"]
---

# Manage tunnels in the Claude Console

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

    In the Claude Console, go to the [MCP tunnels](https://platform.claude.com/settings/workspaces/default/mcp-tunnels) page (`platform.claude.com/settings/workspaces/default/mcp-tunnels`). Tunnels are workspace-scoped; the new tunnel belongs to the workspace currently selected in the Console. Select the workspace you want in the workspace picker in the sidebar.

2.  2

    ### Name the tunnel

    Click **New tunnel** and enter a name in the **Create tunnel** dialog box. The name is required and identifies the tunnel in the list, on the detail page, and in the agent MCP server picker. A domain of the form `abcd1234.tunnel.anthropic.com` is assigned automatically.

3.  3

    ### Optionally set up programmatic access

    If your role can manage federation rules, a **Set up programmatic access** toggle appears (off by default). If not, the Console shows a notice in its place and your tunnel stack uses the manual flow instead. The rest of the create flow is the same either way.

    Programmatic access relies on [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md); read that page first if federation issuers, rules, and service accounts are unfamiliar. To turn the toggle on you need:

    1.  **A registered OIDC issuer** for the identity provider your stack presents tokens from (such as a Kubernetes cluster, AWS IAM, Google Cloud, or GitHub Actions). Register one on the **Issuers** tab of the [Workload identity](https://platform.claude.com/settings/workload-identity-federation) page (`platform.claude.com/settings/workload-identity-federation`) in the Claude Console if your organization doesn’t have one.
    2.  **A federation rule with the `workspace:manage_tunnels` scope.** Turning on the toggle reveals a **Federation rule** picker. Select an existing rule with that scope, or click **Create federation rule** to create one inline.
    3.  **The rule’s service account added to this workspace.** The Tunnels API authorizes against the service account’s workspace memberships. If you’re creating the tunnel in a workspace other than the organization’s default, [add the service account to that workspace](../Other/manage-claude-workspaces.md#role-inheritance) and pass the workspace ID at deploy time (`api.wif.workspaceId` for Helm, `ANTHROPIC_WORKSPACE_ID` for Compose).

    Skipping this step is fully supported; both deploy guides have a **Without programmatic access** tab.

4.  4

    ### Create the tunnel

    Click **Create tunnel**. The Console provisions the tunnel and opens the detail page.

5.  5

    ### Record the deployment identifiers

    Both deploy paths need:

    - The **tunnel ID** (`tnl_...`), shown on the tunnel detail page.
    - The **tunnel domain** (`abcd1234.tunnel.anthropic.com`), shown on the tunnel detail page. Used as the proxy’s `tunnel_domain` and in the server certificate’s SAN.

    What else you need depends on the [credential-provisioning mode](agents-and-tools-mcp-tunnels-concepts.md#credential-provisioning):

    | With programmatic access | Without programmatic access |
    |----|----|
    | The **federation rule ID** (`fdrl_...`) of the rule you selected. The rule is org-level, not stored on the tunnel; find it on the **Rules** tab of the [Workload identity](https://platform.claude.com/settings/workload-identity-federation?tab=rules) page (`platform.claude.com/settings/workload-identity-federation?tab=rules`) in the Claude Console. | The **tunnel token**, revealed with the eye icon next to **Token** on the detail page. Treat it as a secret. See [Get the connection details](#get-the-connection-details). |
    | The **organization ID** (a UUID), shown on the [Organization](../Other/playground.md) page (`platform.claude.com/settings/organization`) in the Claude Console. | A **CA certificate** that you generate and [register on the tunnel](#add-a-ca-certificate). |

    With programmatic access, your stack fetches the tunnel token through the Tunnels API, generates the CA and server certificate locally (the private key never leaves your environment), and registers only the CA’s public certificate with Anthropic. You’re still responsible for securing the private keys and renewing the server certificate before it expires.

Your organization can have up to 10 active tunnels. Creating a tunnel does not establish any connectivity; that occurs once your stack dials in with the tunnel token and a CA certificate is registered.

## Get the connection details

Open the tunnel. The detail page shows a **Connection** section with the domain and token and a **Certificates** section.

| Field | Description |
|----|----|
| **Domain** | Copy the assigned `abcd1234.tunnel.anthropic.com` value. Your proxy’s routes are subdomains of this domain. |
| **Token** | Click the eye icon (**Show token**) to fetch the tunnel token, then use the copy icon to copy it into your tunnel stack’s secret store. Click **Rotate token** to invalidate the current token and issue a new one. |



Every reveal and rotation is recorded in your organization’s [Compliance API](../Other/manage-claude-compliance-api.md) activity log. Rotation does not sever cloudflared connections that are already established, so you can rotate, redeploy with the new value, and let the old connections drain.

## Add a CA certificate

Anthropic verifies [inner TLS](agents-and-tools-mcp-tunnels-concepts.md#components) to your [proxy](agents-and-tools-mcp-tunnels-concepts.md#components) against the CA certificates you register on the tunnel. A tunnel with no active certificates cannot accept connections, and does not appear in the agent MCP server picker until one is registered.

1.  1

    ### Find the Certificates section

    On the tunnel’s detail page, scroll to the **Certificates** section and click **Add certificate**.

2.  2

    ### Provide the certificate

    Click **Choose file** to select a `.pem`, `.crt`, or `.cer` file, drag the file onto the text area, or paste the PEM block directly. The modal window rejects private-key material and content that isn’t a `-----BEGIN CERTIFICATE-----` block. The file must be 8 kB or smaller.

3.  3

    ### Add the certificate

    Click **Add certificate**. The fingerprint and expiry appear in the certificate list, and the slot count on the section header increments.

A tunnel holds up to two active certificates so you can rotate without downtime: register the new certificate alongside the old one, redeploy your proxy with the new key pair, confirm traffic is flowing, then click **Revoke** on the old certificate’s row. Revoked certificates remain visible in the list with a **Revoked** badge.

## Deploy the tunnel stack

The tunnel exists in the Console, but no traffic flows until the tunnel stack is running inside your network and dialed in with the tunnel token. Follow one of the deploy guides:



[Deploy with Docker Compose](agents-and-tools-mcp-tunnels-deploy-compose.md)

Run the tunnel stack on a single host. Both programmatic-access and manual flows.



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Run the tunnel stack on a Kubernetes cluster. Both programmatic-access and manual flows.

## Use the tunnel in an agent

Once your stack is running, add a tunneled MCP server to an agent when you create a [Claude Managed Agents](../Other/managed-agents-overview.md) session. To call the same servers from the Messages API instead, see [Use the tunneled MCP servers](agents-and-tools-mcp-tunnels-overview.md#use-the-tunneled-mcp-servers).

1.  1

    ### Open the Create session dialog box

    In the Claude Console, go to the [Sessions](../Other/playground.md) page (`platform.claude.com/sessions`). In the workspace picker in the sidebar, select the workspace that holds the tunnel. Click **Create session**.

2.  2

    ### Create a new agent

    From the **Agent** dropdown menu, select **Create new agent**, because the dialog box can add MCP servers only to a new agent. Enter a name for the agent in the **Name** field.

3.  3

    ### Add the MCP server

    Under **MCP servers**, click **MCP server**. On the card that appears, open the **Select a server** dropdown menu and select your tunnel from the top of the list. Only tunnels in the selected workspace that have an [active CA certificate](#add-a-ca-certificate) are listed.

4.  4

    ### Enter the subdomain and path

    In the **Subdomain** field, enter the subdomain that your proxy’s `routes` map sends to the MCP server, such as `wiki`. In the **Path** field, enter the path that the MCP server expects, such as `mcp`. Check that the **Resolves to** line shows your subdomain and path under the tunnel domain, such as `https://wiki.abcd1234.tunnel.anthropic.com/mcp`.

5.  5

    ### Add a credential if the MCP server needs one

    The tunnel carries traffic to the upstream MCP server but does not authenticate to it. If the server requires OAuth or a bearer token, click **Connect** on the card and save a credential in a vault. If the card shows **Needs vault** instead, go to **Credential vaults** and add a vault that holds a credential for the **Resolves to** URL. If the server requires no authentication, ignore **Connect** or **Needs vault** on the card. To learn how vaults work, see [Authenticate with vaults](../Other/managed-agents-vaults.md).

6.  6

    ### Select an environment

    In the **Environment** field, above **MCP servers**, select an environment. If no warning appears below the field, go to the next step. If a warning says that the environment blocks MCP servers, click **Edit environment**, which opens the environment in a new browser tab. Under **Networking**, add the host from the **Resolves to** line, such as `wiki.abcd1234.tunnel.anthropic.com`, to **Allowed hosts**. Leave the **Allow MCP servers** checkbox unchecked, as the [Limit the network](../Other/managed-agents-secure-deployment.md#limit-the-network) section recommends. Click **Save** and return to the browser tab with the dialog box.

7.  7

    ### Create the session

    Under **Credential vaults**, remove any vault that the session does not need. If a vault remains, select the checkbox that confirms you are authorized to use it. In the dialog box, click **Create session**. The Console saves the agent and opens the session.

8.  8

    ### Test the connection

    Ask the agent to use one of the MCP server’s tools. You should see a tool call followed by its result. If the agent can’t reach the server, see [Troubleshoot MCP tunnels](agents-and-tools-mcp-tunnels-troubleshooting.md).

## Archive a tunnel

Archiving immediately stops the tunnel from accepting connections and is permanent.

In the Claude Console, go to the [MCP tunnels](https://platform.claude.com/settings/workspaces/default/mcp-tunnels) page (`platform.claude.com/settings/workspaces/default/mcp-tunnels`). In the workspace picker in the sidebar, select the workspace that holds the tunnel. Open the row menu for the tunnel and select **Archive**. Archived tunnels remain visible when you filter the list by **Archived** or **All**.

## Next steps



[Deploy with Helm](agents-and-tools-mcp-tunnels-deploy-helm.md)

Install on a Kubernetes cluster using the Anthropic Helm chart.



[Security](agents-and-tools-mcp-tunnels-security.md)

Hardening guidance, credential rotation, and breach response.
