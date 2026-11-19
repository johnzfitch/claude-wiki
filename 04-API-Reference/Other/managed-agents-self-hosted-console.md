---
title: "Use the console on your server - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted/console"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:35:11Z"
tags: ["agents", "api"]
---

# Use the console on your server

Copy page



Set up sign-in for the console on your self-hosted Claude Managed Agents server, then create agents and run sessions in a browser.

Copy page





To request access to self-hosted Claude Managed Agents, contact your Anthropic account team.

The console on your server is a webpage that a self-hosted Claude Managed Agents server serves at the same address as its API. In it, you create agents, run sessions, and manage environments, credential vaults, memory stores, and skills, with no SDK or CLI.

It isn’t the Claude Console at platform.claude.com. It shows only what is on your server.

## Set up sign-in

An administrator sets up sign-in once. To try the console on one machine instead, follow [Try the console on your server](managed-agents-self-hosted-quickstart.md#try-the-console-on-your-server), which uses the release’s mock sign-in provider.

1.  1

    ### Set up single sign-on and the terminal login

    Follow [Single sign-on](managed-agents-self-hosted-configure.md#single-sign-on), including [Let developers log in from a terminal](managed-agents-self-hosted-configure.md#let-developers-log-in-from-a-terminal). The console signs people in through the application that you registered for the terminal login. It checks each token against the first entry of `audiences` in the issuer entry, so list that application’s audience first.

2.  2

    ### Serve the console over HTTPS

    Put a proxy that terminates TLS in front of port 8400. [Put TLS in front of the server](managed-agents-self-hosted-kubernetes.md#put-tls-in-front-of-the-server) lists what the proxy must do. Over plain HTTP, sign-in works only at `localhost` or `127.0.0.1`.

3.  3

    ### Add the console’s address to the application

    In your identity provider, add your server’s HTTPS address as a second redirect URI of that application, with a trailing slash: `https://cma.example.com/`. Also allow its origin, `https://cma.example.com`, for cross-origin (CORS) requests.

To check the setup, [open the console](#open-the-console) and sign in.

## Open the console

If your applications call `https://cma.example.com`, open `https://cma.example.com/` in a browser, and click **Continue with SSO**.

You sign in through your identity provider. The console doesn’t accept the server API key. If the console says that logging in isn’t set up on this server, an administrator needs to [set up sign-in](#set-up-sign-in).

## Run an agent from the console

A blank agent’s built-in tools, such as `bash`, run on a worker, so select an environment that a worker is polling. [What runs where](managed-agents-self-hosted.md#what-runs-where) says what a worker is. With no worker, the first tool call waits until one runs it. Administrators create environments, and they can see an environment’s workers on its **Workers** tab.

1.  1

    ### Create an agent

    In the sidebar, select **Agents**, and click **Create agent**. Select a starting point, such as **Blank agent**, and enter a name.

    Click **Create agent**. The agent’s page opens.

2.  2

    ### Start a session

    On the agent’s page, click **Start session**. Select an environment, and click **Create session**. The session’s page opens.

3.  3

    ### Send a message

    Enter a message in the box at the bottom of the page, and send it. The page updates as the agent works. If a tool call waits for you, its card shows **Approve** and **Deny**.

While a tool call waits for you, the session’s badge says **Idle**.

To open any other session, such as one that an application started through the API, select **Sessions** in the sidebar, and then select the session.

## Who sees what

Your role determines what the console shows, as it does in the API:

- **Administrators** see and change everything on the server.
- **People with the `developer` or `user` role** see every environment. Of the agents, sessions, vaults, memory stores, and skills, they see only what they created under their own sign-in.

An agent or session that was created with the server API key, such as the quickstart’s, appears only to administrators. For the full table, see [What each role can do](managed-agents-self-hosted-configure.md#what-each-role-can-do).

## Turn off the console

The server serves the console by default. To turn it off, set `console.serve: false` in the [settings file](managed-agents-self-hosted-configuration-reference.md#where-settings-go), and restart the server. The server then stops serving the console. Agents and sessions keep working through the API.

## Next steps

- [Call the API on a self-hosted server](managed-agents-self-hosted-call-the-api.md): Do the same work from your code or the `ant` CLI.
- [Data and access in self-hosted Claude Managed Agents](managed-agents-self-hosted-data-and-access.md#who-can-reach-the-server): See who can reach the server and its console.
