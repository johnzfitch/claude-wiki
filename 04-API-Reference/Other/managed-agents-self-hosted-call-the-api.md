---
title: "Call the API on a self-hosted server - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted/call-the-api"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:53Z"
tags: ["api", "cli"]
---

# Call the API on a self-hosted server

Copy page



Point the official SDK, cURL, or the ant CLI at your self-hosted Claude Managed Agents server, start a session, and read the agent’s reply. Then connect workers of your own, if you need them.

Copy page





To request access to self-hosted Claude Managed Agents, contact your Anthropic account team.

A self-hosted Claude Managed Agents server has the same API as Anthropic’s hosted [Managed Agents](managed-agents-overview.md) service. Your code calls it with the official SDK, cURL, or the `ant` CLI. Two things change: the base URL is your server’s address, and the API key is your [server API key](managed-agents-self-hosted.md#the-three-credentials) instead of a Claude API key.

To create agents and run sessions in a browser, see [Use the console on your server](managed-agents-self-hosted-console.md).

## Prerequisites

- **A running server:** Start one with [Get started with self-hosted Claude Managed Agents](managed-agents-self-hosted-quickstart.md) or [Deploy on Kubernetes](managed-agents-self-hosted-kubernetes.md).
- **Access to the server:** If someone else runs the server, ask them for its address and how to authenticate. If they use single sign-on, see [Let developers log in from a terminal](managed-agents-self-hosted-configure.md#let-developers-log-in-from-a-terminal).
- **The `ant` CLI:** Install the latest version, as the [CLI quickstart](cli-sdks-libraries-cli-quickstart.md#installation) shows.

## Point your client at your server

The SDK and the `ant` CLI read the server address from `ANTHROPIC_BASE_URL` and the API key from `ANTHROPIC_API_KEY`. Set both variables in a terminal that you keep for this server.

For the [quickstart stack](managed-agents-self-hosted-quickstart.md), run these commands from the directory that holds your `.env` file:

```python
export ANTHROPIC_BASE_URL=http://127.0.0.1:8400
export ANTHROPIC_API_KEY=$(grep '^CMA_SERVER__API_KEY=' .env | cut -d= -f2)
```



On Kubernetes, set the two variables as [Run a session](managed-agents-self-hosted-kubernetes.md#run-a-session) shows, and keep its port-forward running.

In that terminal, every `ant` command, such as `ant beta:agents list`, reaches your server. Don’t run Claude Code or `docker compose` in that terminal, because they read the same variables.

## Start a session

A session needs the ID of an agent and the ID of an environment:

- **Agent:** Create one as [Create an agent](managed-agents-agent-setup.md#create-an-agent) shows, with your client pointed at your server. If you send raw HTTP requests, replace `https://api.anthropic.com` in the URL with `$ANTHROPIC_BASE_URL`.
- **Environment:** The quickstart stack creates one named `compose-sandbox`, and the Helm charts create one named `default`. `ant beta:environments list` prints each environment’s name and ID. For your own workers, it’s the ID that the admin CLI printed in [Run your own workers](#point-a-worker-at-your-server).

Put your two IDs in your shell, in place of these example IDs:

```python
export AGENT_ID=agent_011CYm1BLqPXpQRk5khsSXrs
export ENVIRONMENT_ID=env_01595EKxaaTTGwwY3kyXdtbs
```



The following example creates a session and sends its first message in the same request:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
import os

from anthropic import Anthropic

client = Anthropic()

session = client.beta.sessions.create(
    agent=os.environ["AGENT_ID"],
    environment_id=os.environ["ENVIRONMENT_ID"],
    initial_events=[
        {
            "type": "user.message",
            "content": [
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
print(session.id)
```

The response holds the session’s ID, which starts with `sesn_`. The agent starts work at once. Its built-in tools, such as `bash`, run on a worker that serves the environment.

To watch the session, open the [console on your server](managed-agents-self-hosted-console.md) in a browser, select **Sessions**, and then select the session. A session that you started with the server API key, as on this page, appears only to administrators.

To follow the session in your terminal instead, pass its ID to [`ant beta:sessions connect`](cli-sdks-libraries-cli-sessions-connect.md):

```python
ant beta:sessions connect sesn_011CZkZAtmR3yMPDzynEDxu7
```



For what else a session can do, such as pinning an agent version, see [Start a session](managed-agents-sessions.md).

## Send a message and read the reply

Put your session’s ID in your shell, in place of this example ID:

```python
export SESSION_ID=sesn_011CZkZAtmR3yMPDzynEDxu7
```



Wait until the session is idle before you run the next example. The example stops reading when a turn ends. If an earlier turn is still running, its end can stop the example before the reply to your message arrives. The console and `ant beta:sessions connect` both show the session’s status.

The following example sends a message and prints the agent’s reply. It opens the session’s event stream first, because a stream delivers only the events that come after it opens:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
import os

from anthropic import Anthropic

client = Anthropic()
session_id = os.environ["SESSION_ID"]

with client.beta.sessions.events.stream(session_id) as stream:
    client.beta.sessions.events.send(
        session_id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {"type": "text", "text": "Summarize what you did in one sentence."}
                ],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.error":
                error_message = event.error.message if event.error else "unknown"
                print(f"\n[Error: {error_message}]")
            case "session.status_idle":
                if event.stop_reason.type != "requires_action":
                    break
            case "session.status_terminated":
                break
```

Besides printing `agent.message` text, the loop handles three events:

- **`session.status_idle`:** The loop ends, unless the event’s `stop_reason.type` is `requires_action`.
- **`session.status_terminated`:** The loop ends.
- **`session.error`:** The loop prints the error’s message and keeps reading, because the server can retry a failed model call and finish the turn.

`requires_action` means that the session has paused for a tool call. What ends the pause depends on the call:

- **A custom tool call, or a request to confirm a tool call:** Only your code can answer it. If your agent uses either, see [Answer tool calls that pause the session](managed-agents-events-and-streaming.md#answer-tool-calls-that-pause-the-session).
- **A call to a tool that a worker runs, such as `bash`:** This call normally doesn’t pause the session. If no worker takes the call for about 3 minutes, the session pauses until a worker returns the result. Your code has nothing to answer then. Keep the stream open, and the turn resumes when a worker runs the call.

For the other events that a session sends, and how to reconnect without missing any, see [Session event stream](managed-agents-events-and-streaming.md).

## Move data in and out of a session

Data reaches a session and leaves it through the worker’s working directory.

On the quickstart stack, each session’s container starts with an empty `/workspace` directory, apart from clones of the session’s repositories. By default, about a minute after a turn ends, the container exits, and Docker deletes it together with that directory. Anything a session must keep has to leave through a tool call, such as an upload or a `git push`, before then.

A container also exits about an hour after it starts, even in the middle of a turn. No setting changes that. The turn continues in a new container, usually after a minute or two, and your client gets no event for the switch. The switch has two costs:

- **Commands:** Everything that runs in the old container stops. The new container runs the interrupted tool call again from the start, but nothing restarts a command that the agent left running in the background.
- **Files:** The new container’s `/workspace` is empty again, apart from fresh clones of the session’s repositories.

In a long turn, have the agent upload or push its work as it goes, and avoid commands that cause harm if they run twice.

On Kubernetes, a session keeps one pod for about an hour at most, and the turn continues in the same way. Two things differ: the new pod finds the session’s files in `/workspace`, and it starts about 6 minutes after the old pod stops.

For workers that you start yourself, put input files in the working directory before you send the message that needs them. Read output files from it afterward.

When you start a container for each session yourself, mount a directory that holds the session’s input files as the container’s working directory. Collect the output files from it after the container exits. See [Stage files for a session](managed-agents-self-hosted-sandboxes-workers.md#stage-files-for-a-session).

## Find more examples in the hosted guides

The hosted service’s guides explain the API’s [core concepts](managed-agents-overview.md#core-concepts) and have examples for each feature. Their SDK and CLI examples call your server when you run them in the terminal where `ANTHROPIC_BASE_URL` and `ANTHROPIC_API_KEY` are set. Their cURL examples name `https://api.anthropic.com`, so replace that address with `$ANTHROPIC_BASE_URL` before you run one.

For some features, your server needs a setting first, or an example needs a change:

| Task | Hosted guide | On your server |
|----|----|----|
| Set an agent’s model, system prompt, and versions | [Define your agent](managed-agents-agent-setup.md) | Some fields [depend on your inference provider](managed-agents-self-hosted-differences.md#differences-that-depend-on-your-inference-provider). |
| Choose built-in tools, or add custom tools | [Tools](managed-agents-tools.md) | To use the web tools, turn them on first, as [Web tools need a server setting](managed-agents-self-hosted-differences.md#web-tools-need-a-server-setting) describes. Which ones exist depends on your inference provider. |
| Connect an MCP server and store its token | [MCP connector](managed-agents-mcp-connector.md) and [Authenticate with vaults](managed-agents-vaults.md) | Add the MCP server’s host to the [allowlist for MCP servers](managed-agents-self-hosted-differences.md#mcp-servers-need-an-allowlist-entry). Store the token as a `static_bearer` credential. |
| Give an agent skills | [Skills](managed-agents-skills.md) | Upload each skill as individual files, because your server refuses a zip archive. The [prebuilt skills](managed-agents-self-hosted-differences.md#features-that-arent-available) in that guide’s examples aren’t available. |
| Keep memory across sessions | [Using agent memory](managed-agents-memory.md) | If you run your own workers, give them a writable `/mnt/memory` directory, as in [Memory stores in self-hosted sandboxes](managed-agents-self-hosted-sandboxes-memory.md). |
| Hand work to other agents | [Multiagent orchestration](managed-agents-multiagent-orchestration.md) | Replace the `multiagent_20261001` block in that guide’s examples with a [`coordinator` block](managed-agents-self-hosted-differences.md#features-that-behave-differently). |
| Work in a Git repository | [Accessing GitHub](managed-agents-github.md) | List the Git host in your server’s settings, as [Git repositories need an allowlist entry](managed-agents-self-hosted-differences.md#git-repositories-need-an-allowlist-entry) describes. That guide’s example agent also needs `api.githubcopilot.com` on the allowlist for MCP servers. |
| Have a grader check the work against a rubric | [Define outcomes](managed-agents-define-outcomes.md) | Send the rubric as text. The Files API isn’t available, so [collect output files](#move-data-in-and-out-of-a-session) from the working directory. |
| Follow a session and answer its tool calls | [Session event stream](managed-agents-events-and-streaming.md) | That guide’s first example closes the stream at any pause, so start from the loop in [Send a message and read the reply](#send-a-message-and-read-the-reply) instead. |

[Differences from the hosted service](managed-agents-self-hosted-differences.md) has the full list. Check it before you move an existing application.

## Run your own workers

The [quickstart stack](managed-agents-self-hosted-quickstart.md) creates an environment and runs its workers. So do the Helm charts in [Deploy on Kubernetes](managed-agents-self-hosted-kubernetes.md). If those workers are all that you need, skip this section.

You run workers as you do for [self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md): the same `ant beta:worker` commands and SDK workers, in the ways that [Deploy self-hosted workers](managed-agents-self-hosted-sandboxes-workers.md) shows. The exception is workers triggered by webhooks, because your server sends none.

### Create an environment and its key

Create an environment and an environment key with the admin CLI, not in the Claude Console. The CLI, `cma-server-admin`, is at the top of the release archive, so run the command from there. For `-base-url`, pass the address where your workers reach the server:

- **Workers on the machine that runs the quickstart stack:** `http://127.0.0.1:8400`
- **Workers on another machine:** the `https` address of the [TLS proxy that you put in front of the server](managed-agents-self-hosted-kubernetes.md#put-tls-in-front-of-the-server)

The admin CLI calls the server at the same address, so run it on a machine that can reach that address.

```python
echo "$ANTHROPIC_API_KEY" | ./cma-server-admin bootstrap \
  -base-url http://127.0.0.1:8400 -name my-env -key-file -
```



The command prints the worker’s settings, the command that starts a worker, and the key’s ID and expiry:

```python
export ANTHROPIC_BASE_URL='http://127.0.0.1:8400'
export ANTHROPIC_ENVIRONMENT_ID='env_...'
export ANTHROPIC_ENVIRONMENT_KEY='sk-ant-oat01-...'
# then: histchars= HISTFILE=/dev/null ant beta:worker poll --workdir /workspace
# key id: 'etok_...'  expires: '...'
```



The command shows the key only once, so store the key, its ID, and its expiry in your secret manager. The key stops working after 365 days. Before then, follow [Replace an environment key for your own workers](managed-agents-self-hosted-kubernetes.md#replace-an-environment-key-for-your-own-workers).

Keep the server API key off the machines that run workers. Run workers in a container or VM that holds nothing you need to protect. For your other security duties, see [Your security responsibilities](managed-agents-self-hosted.md#your-security-responsibilities).

### Run a local experiment

Run the three `export` lines in the shell where you start the worker. Then start the worker with these commands, not the printed one. The first command creates the worker’s working directory, because the worker doesn’t create it:

```python
mkdir -p "$HOME/cma-workspace" "$HOME/.config/cma"
cat > "$HOME/.config/cma/worker.inputrc" <<'EOF'
$include /etc/inputrc
set disable-completion on
EOF
histchars= HISTFILE=/dev/null INPUTRC="$HOME/.config/cma/worker.inputrc" \
  ant beta:worker poll --workdir "$HOME/cma-workspace"
```



`histchars`, `INPUTRC`, and `HISTFILE` set up the shell behind the worker’s `bash` tool, so that it runs each command as the agent wrote it:

- **`histchars=`:** The shell doesn’t treat `!` as a reference to its command history.
- **`INPUTRC`:** The file turns off completion, which would otherwise consume each tab character in a command. Keep the file out of the working directory, where the agent’s file tools could rewrite it.
- **`HISTFILE=/dev/null`:** The shell neither reads nor writes a history file.

Use this worker for nothing else. It holds the environment key and runs every session’s tools in one process. It doesn’t clone a session’s repositories either. The session runs without them, and your client gets no error.

### Run workers in production

For anything but a local experiment, start one container for each session and run `ant beta:worker run` in it, as [Run one sandbox per session](managed-agents-self-hosted-sandboxes-workers.md#run-one-sandbox-per-session) shows. Give its image what [Build your own sandbox image](#build-your-own-sandbox-image) lists, and change three things in that setup:

- **Environment key:** Don’t pass `ANTHROPIC_ENVIRONMENT_KEY` into a session’s container. The server accepts that key for every session in the environment, and the container needs access to one session only.
- **Work item’s secret:** Pass this secret in place of the key, because the server accepts it for that one session only. [Forward the work item’s secret](managed-agents-self-hosted-sandboxes-workers.md#forward-the-work-items-secret) shows where your code receives it. Where that section sets `ANTHROPIC_WORK_SECRET`, put the secret in a file that only the container’s user can read. For example, pipe the secret to the container’s standard input, and have the container write the file before it starts the worker. Then set `ANTHROPIC_WORK_SECRET_FILE` to the file’s path.
- **Server address:** Set `ANTHROPIC_BASE_URL` to an address that the container can reach. `http://127.0.0.1:8400` isn’t one.

For an SDK worker, two more points apply:

- **Version:** Build the worker on the latest version of the SDK, as [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md) describes. That version’s worker waits for approval before it runs a tool call that needs it, and never runs a call that a policy denies. A worker built on an earlier version runs every tool call as soon as it arrives.
- **Samples:** The samples in [Run the SDK worker inside the sandbox](managed-agents-self-hosted-sandboxes-workers.md#run-the-sdk-worker-inside-the-sandbox) read the environment key, so they don’t work here as they are.

### Build your own sandbox image

An image of your own needs these packages and settings:

- **Packages:** Git 2.38 or later, `curl`, `jq`, and ripgrep, which the worker’s `grep` tool searches with.

- **Shell settings:** `histchars`, `HISTFILE`, and `INPUTRC`, as in the local experiment, and `TERMINFO`. Put these lines in the Dockerfile, before any `USER` line:

  ``` shiki
  ENV histchars=
  RUN printf '\nset disable-completion on\n' >> /etc/inputrc
  ENV INPUTRC=/etc/inputrc TERMINFO=/etc/terminfo HISTFILE=/dev/null
  RUN test -r /etc/terminfo/d/dumb
  ```

  

  `TERMINFO` must name the directory that holds `d/dumb`, the terminal description that the worker’s `bash` reads. On Alpine with `bash` installed, that’s `/etc/terminfo`, as shown. On another base, such as Debian or Ubuntu, it’s `/lib/terminfo` or `/usr/share/terminfo`, whichever holds `d/dumb`. Write that directory in the `TERMINFO` setting and in the `RUN test` line, which stops the build if the file is missing.

The image also needs two scripts from the archive, which run before the worker starts:

1.  Copy `image-build/with-repositories.sh` to `/usr/local/bin/cma-with-repositories`. It clones one session’s repositories.
2.  Copy `image-build/with-egress.sh` to `/usr/local/bin/cma-with-egress`. It points the session’s tools at the [egress gateway](managed-agents-self-hosted-agent-identity.md#environment-variable-credentials), if your server runs one.
3.  Make both files executable.
4.  Put both in front of the worker’s command, as in `cma-with-egress cma-with-repositories ant beta:worker run ...`. Skip this step if your image runs the archive’s `kubernetes/sandbox/worker.sh`, because that script starts the worker this way.

A worker that starts without `cma-with-repositories` runs the session with no repository. Your client gets no error.

### Move workers from the hosted service

If you already run workers for Anthropic’s hosted service, the same workers can serve your server instead. Do three things:

- Give the process that polls for work the three `export` values that the admin CLI printed.
- Start that process with `histchars`, `HISTFILE`, and `INPUTRC` set, as in the local experiment.
- Make the changes that [Run workers in production](#run-workers-in-production) describes, and check each session’s image against [Build your own sandbox image](#build-your-own-sandbox-image).

## Next steps

- [Let developers log in from a terminal](managed-agents-self-hosted-configure.md#let-developers-log-in-from-a-terminal): Set up single sign-on, so that developers use the `ant` CLI under their own identity, in a terminal without `ANTHROPIC_API_KEY`.
- [Agent identity and credentials](managed-agents-self-hosted-agent-identity.md): Let outside systems trust your agents, and keep vault credentials in your secret manager.
- [Inference provider](managed-agents-self-hosted-inference-provider.md): Send model calls to a cloud provider or your own model gateway.
