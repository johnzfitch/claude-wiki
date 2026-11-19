---
title: "Get started with self-hosted Claude Managed Agents - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:35:12Z"
tags: ["agents", "api"]
---

# Get started with self-hosted Claude Managed Agents

Copy page



Start self-hosted Claude Managed Agents on one machine with Docker Compose and run a first session in a sandbox container.

Copy page





To request access to self-hosted Claude Managed Agents, contact your Anthropic account team.

In this quickstart, you start self-hosted Claude Managed Agents on one machine with Docker Compose. The Compose stack is the server, its PostgreSQL database, and a set of workers that run each session in a sandbox container of its own. You then chat with an agent from your terminal and confirm that its tool calls ran in a sandbox container. You can then open the session in the [console on your server](managed-agents-self-hosted-console.md).



The Compose stack is for development, not for production. It serves plain HTTP, and by default publishes port 8400 only on the Docker host’s loopback address, `127.0.0.1`. Under some Docker Engine releases before 28.3.3, machines on the host’s local network can reach that port too. Agent tools run in containers on that host, so use a machine that holds nothing you need to protect.

For production, Anthropic recommends the release’s two Helm charts. See [Deploy on Kubernetes](managed-agents-self-hosted-kubernetes.md).

Claude Code

Let Claude Code run this quickstart for you

Run in

`❯``Set up self-hosted Claude Managed Agents on this machine by following https://platform.claude.com/docs/en/managed-agents/self-hosted/quickstart.md. I've already downloaded the release archive.`



## Prerequisites

- **The release archive:** To request access to the download, contact your Anthropic account team.
- **A Claude API key:** The server uses it for model calls. Create one in the [Claude Console](playground.md).
- **Docker:** The [latest version of Docker Engine](https://docs.docker.com/engine/install/) with the Compose plugin (`docker compose`, not the older `docker-compose`).
- **A host with at least two CPUs:** x86-64 or Arm. On a smaller host, set `CMA_SANDBOX_CPUS` to its CPU count when you create `.env`.
- **Network access on first start:** The first build pulls from Docker Hub, the Alpine package repositories, and GitHub releases.
- **Tools:** On the machine where you run Docker, you need `openssl` and the [`ant` CLI](cli-sdks-libraries-cli-quickstart.md#installation).

## Start the stack

1.  1

    ### Extract the archive

    Extract the archive, and work from its `compose` directory. In the command, replace `<archive>` with your archive’s name, without `.tar.gz`.

    ``` shiki
    tar -xzf <archive>.tar.gz && cd <archive>/compose
    ```

    

    If your umask is stricter than `022`, the binaries lose their execute permission for other users, and the server container can’t start them. In that case, set it to `022` and extract the archive again.

2.  2

    ### Create the .env file

    Compose reads the stack’s secrets from a `.env` file beside `docker-compose.yml`. Create the file:

    ``` shiki
    cat > .env <<EOF
    CMA_PG_PASSWORD=$(openssl rand -hex 32)
    ANTHROPIC_API_KEY=sk-ant-...
    CMA_SERVER__API_KEY=$(openssl rand -hex 32)
    CMA_STORE__CREDENTIALS_ENCRYPTION_KEY=$(openssl rand -base64 32)
    EOF
    chmod 600 .env
    ```

    

    Open `.env` in an editor and replace `sk-ant-...` with your Claude API key. The block generates the rest: the database password, the server API key that your applications send, and the key that encrypts the server’s stored secrets.

3.  3

    ### Start the containers

    Build and start the stack, and then follow the server’s log:

    ``` shiki
    docker compose up --build -d
    docker compose logs -f cma-server
    ```

    

    When the log shows a line with `msg="cma-server listening"`, press Ctrl+C to stop following it.

4.  4

    ### Check that the server is ready

    ``` shiki
    curl -s http://127.0.0.1:8400/cma-server/readyz
    ```

    

    A ready server answers with `"status":"ready"`. Right after start, it can answer `"status":"degraded"` for a few seconds while its first checks run. If it stays `degraded` or answers `"status":"not_ready"`, see [Troubleshooting](#troubleshooting).

## Run your first session

Create an agent and chat with it from your terminal with the `ant` CLI.

1.  1

    ### Point the CLI at your server

    Open a second terminal in the same directory, and keep it for `ant`. The following commands set `ANTHROPIC_API_KEY` to your server API key, not your Claude API key, as [Call the API on a self-hosted server](managed-agents-self-hosted-call-the-api.md) explains:

    ``` shiki
    export ANTHROPIC_BASE_URL=http://127.0.0.1:8400
    export ANTHROPIC_API_KEY=$(grep '^CMA_SERVER__API_KEY=' .env | cut -d= -f2)
    ```

    

    Keep `docker compose` commands in the first terminal. If you run `docker compose up` in this terminal, Compose passes these variables to the server, and the server calls itself instead of the Claude API.

2.  2

    ### Create an agent

    Save the file that follows the command as `quickstart-agent.md`, and then run the command. The file gives the agent the built-in tools and lets it run them without asking you first.

    CLI

    

    ``` shiki
    ant apply --yes quickstart-agent.md
    ```

    quickstart-agent.md
    
    

    ``` shiki
    ---
    name: Quickstart agent
    model: claude-opus-5-5
    tools:
      - type: agent_toolset_20260401
    ---

    You are a helpful assistant.
    ```

    The command first prints a warning that it `could not determine the organization and workspace`, with a `404` error, and then creates the agent. That’s expected on your own server.

3.  3

    ### Start a session

    These commands find the agent and the stack’s environment, start a session, and keep the session’s ID in `SESSION_ID`. The stack names its environment `compose-sandbox`.

    ``` shiki
    AGENT_ID=$(ant beta:agents list --format raw \
      --transform 'data.#(name=="Quickstart agent").id' --raw-output)
    ENVIRONMENT_ID=$(ant beta:environments list --format raw \
      --transform 'data.#(name=="compose-sandbox").id' --raw-output)
    SESSION_ID=$(ant beta:sessions create --agent "$AGENT_ID" \
      --environment-id "$ENVIRONMENT_ID" --transform id --raw-output)
    ```

    

4.  4

    ### Ask the agent to run a command

    Connect your terminal to the session:

    ``` shiki
    ant beta:sessions connect "$SESSION_ID"
    ```

    

    The command opens a [chat view](cli-sdks-libraries-cli-sessions-connect.md) of the session. Send this message:

    ``` block
    Run `hostname` with the bash tool and tell me the output.
    ```

    

    The agent replies with a hostname that starts with `cma-sandbox-`. That’s the name of the sandbox container that ran the command, which confirms that the tool ran in a sandbox and not on your machine.

5.  5

    ### Find the sandbox container

    Leave the chat open. In the first terminal, list the sandbox containers:

    ``` shiki
    docker ps --filter label=cma-server.sandbox
    ```

    

    The list shows the container that the agent reported. The container exits about a minute after a turn ends, and the session’s next message starts a new container. If the list is empty, ask the agent to run `hostname` again, and list the containers again while it replies.

    To leave the chat, press Ctrl+C in its terminal. The session keeps running.

## Try the console on your server

This section is optional. The console needs single sign-on. To try it, restart the stack with the release’s mock sign-in provider. Port 8080 on your machine must be free.



Use the mock provider with throwaway data only. It gives an administrator’s token to anyone who reaches it. On Docker Desktop, that includes the sandbox containers. Under some Docker Engine releases before 28.3.3, it includes machines on your network.

1.  1

    ### Restart the stack with the mock sign-in provider

    Run these commands in the first terminal:

    ``` shiki
    export COMPOSE_FILE=docker-compose.yml:docker-compose.oidc.yml
    docker compose up --build -d
    ```

    

    The `export` line holds for the first terminal only, so run it again in any new terminal that you open for `docker compose`. To change the server’s settings in this stack, edit `compose.config.oidc.yaml`, not `compose.config.yaml`, and then run `docker compose restart cma-server`.

2.  2

    ### Open the session

    In a browser on the same machine, open `http://127.0.0.1:8400/`, click **Continue with SSO**, and select **alice**, the demo administrator. In the sidebar, select **Sessions**, and then select the session.

    The page updates as the agent works, and you can send the agent a message from it.

To create agents and start sessions in the console too, see [Run an agent from the console](managed-agents-self-hosted-console.md#run-an-agent-from-the-console).

## Stop the stack

In the first terminal, run this command:

```python
docker compose down --remove-orphans
```



The command deletes the containers and keeps the database. To also delete the database, with every agent, session, and session history in it, run `docker compose down --remove-orphans -v`.

## Troubleshooting

- **Your archive has no `compose` directory:** The archive holds an earlier release, and this page’s commands don’t match it. Ask your Anthropic account team for the current release. To move a running deployment to the current release, see [Upgrade self-hosted Claude Managed Agents](managed-agents-self-hosted-upgrade.md).
- **The server never comes up:** Run `docker compose logs migrate`. The one-time `migrate` container creates the database tables. It must exit with status `0` before the server starts.
- **The readiness check stays `degraded`, or every turn fails:** If you ran `docker compose up` in a terminal where `ANTHROPIC_BASE_URL` is `http://127.0.0.1:8400`, the server calls itself instead of the Claude API. Run `docker compose up -d` again in the first terminal, where the variable isn’t set. Otherwise, the server log shows what failed. To read it, run `docker compose logs -f cma-server` again.
- **The readiness check answers `not_ready`:** In the answer, find the check with the state `failed`:
  - **`upstream`:** The Claude API rejected your Claude API key. Correct `ANTHROPIC_API_KEY` in `.env`, then run `docker compose up -d` again in the first terminal. If your shell also sets `ANTHROPIC_API_KEY`, Compose uses the shell’s value, so run `unset ANTHROPIC_API_KEY` first.
  - **`database`:** Either the database rejected the server’s login, for example because of a wrong password, or an open connection to the database broke. To see which, run `docker compose logs -f cma-server` again.
- **The agent replies but its tool call never finishes:** No worker is polling the environment. Check the workers’ log with `docker compose logs sandbox`. A worker that can’t reach the Docker daemon’s socket exits with a message that names `CMA_DOCKER_SOCKET`. Set that variable in `.env` to your daemon’s socket path, then run `docker compose up -d` again in the first terminal.
- **The workers are running, but a tool call still never finishes:** The stack starts 10 workers, and each one runs one session’s container at a time. A session takes a free worker when you create it, and a session that never gets a message keeps its worker for up to an hour. With all 10 taken, any other session’s tool calls wait for a worker. If the `docker ps` command in the “Find the sandbox container” step lists 10 containers, archive the sessions that you don’t use:
  1.  In the first terminal, run `docker ps --filter label=cma-server.sandbox --format '{{.Label "cma-server.session"}}'`. It prints the ID of the session behind each container. The session that waits has no container yet, so it isn’t in the list.
  2.  In the second terminal, press Ctrl+C to leave the chat, and run `ant beta:sessions archive --session-id <session-id>` for each listed session that you don’t use.
  3.  Run `ant beta:sessions connect "$SESSION_ID"` again. The tool call finishes when a worker takes its session.

## Next steps



[Call the API](managed-agents-self-hosted-call-the-api.md)

Point the SDK and the `ant` CLI at your server.

[Differences from the hosted service](managed-agents-self-hosted-differences.md)

Check which features behave differently or aren’t available.

[Console on your server](managed-agents-self-hosted-console.md)

Set up sign-in, and create agents and run sessions in a browser.
