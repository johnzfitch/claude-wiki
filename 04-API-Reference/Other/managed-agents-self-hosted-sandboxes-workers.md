---
title: "Deploy self-hosted workers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers"
category: "04-API-Reference/Other"
fetched_at: "2026-10-19T06:28:06Z"
tags: ["api", "hooks"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fself-hosted-sandboxes-workers)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

[Overview and quickstart](managed-agents-self-hosted-sandboxes.md)[Deploy workers](managed-agents-self-hosted-sandboxes-workers.md)[Memory stores](managed-agents-self-hosted-sandboxes-memory.md)[Custom tools and MCP servers](managed-agents-self-hosted-sandboxes-custom-tools.md)[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)[Worker reference](managed-agents-self-hosted-sandboxes-reference.md)[Security model](managed-agents-self-hosted-sandboxes-security.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Self-hosted sandboxes

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Deploy self-hosted workers

Copy page



Choose how self-hosted sandbox workers claim work and where sessions run: always-on or webhook-triggered, in one process or one sandbox per session.

Copy page



The [quickstart](managed-agents-self-hosted-sandboxes.md#quickstart) runs one `ant` CLI worker that polls continuously and runs every session in one process. This page covers the other ways to run a worker and how to choose between them.

## Choose a deployment pattern

When deploying workers, you need to make two choices: how the worker claims work, and where each session runs.

**How the worker claims work:**

- **Always-on:** A long-running process polls the queue continuously and needs only outbound HTTPS. This is the simplest setup.
- **Webhook-triggered:** A handler wakes on `session.status_run_started` and starts polling. This avoids an idle poller, but requires a [webhook](managed-agents-webhooks.md) endpoint that Anthropic can reach.

**Where each session runs:**

- **In process:** The worker that claims a session also runs its tool calls, in one shared working directory.
- **Sandbox per session:** A poller launches a fresh sandbox for each claimed session. Choose this for stronger isolation: a fresh filesystem, resource limits, or per-session network controls.

The CLI and SDK workers support different combinations:

| Capability                                                                 | `ant` CLI                       | SDK (Python, TypeScript, Go) |
|----------------------------------------------------------------------------|---------------------------------|------------------------------|
| Always-on polling                                                          | Yes                             | Yes                          |
| Webhook-triggered                                                          | No                              | Yes                          |
| Sandbox per session                                                        | Yes                             | Yes                          |
| [Memory stores](managed-agents-self-hosted-sandboxes-memory.md)      | Yes, with default sync settings | Yes, with configurable sync  |
| [Custom tools](managed-agents-self-hosted-sandboxes-custom-tools.md) | No                              | Yes                          |

See [Self-hosted worker reference](managed-agents-self-hosted-sandboxes-reference.md) for every CLI flag and SDK option. For more control, call the [Environments Work endpoints](../Endpoints/beta-environments-work.md) directly and implement your own worker.

## Run an always-on worker

Start a worker that polls the queue continuously. It authenticates with the [environment key](managed-agents-self-hosted-sandboxes.md#run-your-first-session) from the quickstart:

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
import asyncio
import contextlib
import os
import signal
from anthropic import AsyncAnthropic
from anthropic.lib.environments import EnvironmentWorker


async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        worker = EnvironmentWorker(
            client,
            environment_id=environment_id,
            environment_key=environment_key,
            workdir="/workspace",
        )
        task = asyncio.create_task(worker.run())
        # Cancelling the task, rather than killing the process, lets the worker stop its
        # in-flight work item and upload changed memory files before it exits.
        loop = asyncio.get_running_loop()
        for signum in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(signum, task.cancel)
        with contextlib.suppress(asyncio.CancelledError):
            await task


asyncio.run(main())
```

## Trigger workers from webhooks

1.  1

    ### Subscribe to session webhooks

    In the [Console](https://platform.claude.com/settings/workspaces/default/webhooks), define a webhook endpoint that listens for `session.status_run_started` events. See [Webhooks](managed-agents-webhooks.md) for details.

2.  2

    ### Export the webhook signing key

    Along with the environment ID and key from the [quickstart](managed-agents-self-hosted-sandboxes.md#run-your-first-session), export the webhook signing key on your handler host. The handler uses it to verify incoming payloads.

    ``` shiki
    export ANTHROPIC_WEBHOOK_SIGNING_KEY="whsec_..."
    ```

    

3.  3

    ### Implement the webhook handler

    Invoke the worker when `session.status_run_started` fires. The handler drains the queue and hands each claimed work item to `handle_item()`, which downloads skills, executes tool calls, posts results back, and returns.

    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    To verify webhook signatures, install the webhooks extra: `pip install "anthropic[webhooks]"`.

    ``` shiki
    import asyncio
    import os
    import anthropic
    import standardwebhooks  # installed by the anthropic[webhooks] extra

    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    client = anthropic.AsyncAnthropic(
        auth_token=environment_key,
    )
    # Cancelled by shutdown() so an in-flight work item can upload changed memory files and
    # remove its store directories before the process exits.
    inflight: set[asyncio.Task[None]] = set()


    # Await this from the host's shutdown hook, such as an ASGI lifespan shutdown (the code after
    # `yield` in a FastAPI lifespan), which uvicorn runs on SIGTERM. uvicorn lets open requests
    # finish before that hook runs, so set --timeout-graceful-shutdown to bound the wait.
    async def shutdown() -> None:
        for task in inflight:
            task.cancel()
        await asyncio.gather(*inflight, return_exceptions=True)


    async def handle(raw: bytes, headers: dict[str, str]) -> tuple[dict[str, str], int]:
        try:
            event = client.beta.webhooks.unwrap(raw.decode(), headers=headers)
        except standardwebhooks.WebhookVerificationError:
            return {"error": "signature verification failed"}, 401
        if event.data.type != "session.status_run_started":
            return {"status": "ignored"}, 200
        task = asyncio.create_task(run_queued_work())
        inflight.add(task)
        task.add_done_callback(inflight.discard)
        try:
            # Shielded: a dropped or timed-out delivery must not cancel the item; shutdown() does.
            await asyncio.shield(task)
        except asyncio.CancelledError:
            return {"status": "shutting down"}, 503
        return {"status": "ok"}, 200


    async def run_queued_work() -> None:
        async for work in client.beta.environments.work.poller(
            environment_id=environment_id,
            environment_key=environment_key,
            block_ms=None,
            reclaim_older_than_ms=2000,
            drain=True,
            auto_stop=False,
        ):
            await client.beta.environments.work.worker(workdir="/workspace").handle_item(
                work_id=work.id,
                environment_id=environment_id,
                session_id=work.data.id,
                environment_key=environment_key,
                # The per-session secret is what lets the worker mount the session's memory stores.
                work_secret=work.secret,
            )
    ```

    Because the handler claims work itself, it must [forward the work item's secret](#forward-the-work-items-secret), as the `work_secret` argument does here.

This handler runs every claimed item in one process on one host. If your sessions attach the same memory store, see [Isolate sessions that share a store](managed-agents-self-hosted-sandboxes-memory.md#isolate-sessions-that-share-a-store).

## Run one sandbox per session

A poller on the host claims work and calls your script once per work item. The script launches a sandbox for that one session.

1.  1

    ### Build the sandbox image

    Install `ant` and set `ant beta:worker run` as the entrypoint. When a sandbox starts, it reads session details from environment variables, handles that session, and exits. The base image must provide `/bin/bash`; `curl` is only used at build time.

    ``` shiki
    FROM your-base-image
    ARG ANT_VERSION=1.42.0
    ARG TARGETARCH
    RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
        curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
          | tar -xz -C /usr/local/bin ant
    WORKDIR /workspace
    VOLUME /workspace
    ENTRYPOINT ["ant", "beta:worker", "run"]
    ```

    

2.  2

    ### Write the spawn script

    The script forwards the session details into a fresh sandbox. It requires `jq` on the poller host.

    ``` shiki
    #!/bin/bash
    # spawn.sh: called once per claimed work item
    # The claimed work item arrives as JSON on stdin.
    ANTHROPIC_WORK_SECRET="$(jq -r '.secret // empty')"
    export ANTHROPIC_WORK_SECRET
    mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
    exec docker run --rm \
      -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
      -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
      -e ANTHROPIC_WORK_SECRET \
      -v "/host/outputs/$ANTHROPIC_SESSION_ID":/workspace \
      your-image
    ```

    

    The poller sets the `ANTHROPIC_*` variables that the script forwards, except the secret. See [Environment variables](managed-agents-self-hosted-sandboxes-reference.md#environment-variables).

    `/host/outputs` is a host directory you choose. Mounting it at `/workspace` lets you retrieve the session's deliverables after the sandbox exits. The mount also picks up the downloaded `skills/` tree and any intermediate files.

3.  3

    ### Start the poller

    ``` shiki
    ant beta:worker poll --on-work ./spawn.sh
    ```

    

### Forward the work item's secret

Each claimed work item can carry a per-session `secret`, which Anthropic issues. The worker that runs the session needs it to mount [memory stores](managed-agents-self-hosted-sandboxes-memory.md).

A worker that claims and runs sessions in one process (`ant beta:worker poll` without `--on-work`, or `EnvironmentWorker` with `run()`) passes the secret along itself. When your own code sits between the claim and the worker, you forward it:

| You claim work with              | The secret arrives as                                                    | Pass it to the worker as                                                                               |
|----------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `ant beta:worker poll --on-work` | The `secret` field of the work item JSON on your script's standard input | `ANTHROPIC_WORK_SECRET` in the sandbox's environment                                                   |
| The SDK's `work.poller()`        | The `secret` field of each claimed work item                             | `ANTHROPIC_WORK_SECRET` in the sandbox's environment, or the `work_secret` argument to `handle_item()` |

Pass the secret only into the sandbox that serves that session, and never log it. See [Security model](managed-agents-self-hosted-sandboxes-security.md) for how it relates to the environment key.

### Launch sandboxes from the SDK poller

To claim work from your own code instead of `ant beta:worker poll --on-work`, use `work.poller()`. It polls the queue and gives you each claimed session, and you launch the sandbox:

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
import asyncio
import os

from anthropic import AsyncAnthropic
from anthropic.types.beta.environments import BetaSelfHostedWork

SANDBOX_ENV = (
    "ANTHROPIC_ENVIRONMENT_ID",
    "ANTHROPIC_ENVIRONMENT_KEY",
    "ANTHROPIC_WORK_ID",
    "ANTHROPIC_SESSION_ID",
    "ANTHROPIC_WORK_SECRET",
    "ANTHROPIC_BASE_URL",  # forwarded only when set on this host
)


async def launch_container(work: BetaSelfHostedWork) -> None:
    print(f"claimed session {work.data.id}")
    # Replace `docker run` with your own sandbox launcher. Forward the environment
    # key (never your API key) and the work item's per-session secret: the worker
    # inside needs the secret to mount the session's memory stores.
    env = os.environ | {
        "ANTHROPIC_WORK_ID": work.id,
        "ANTHROPIC_SESSION_ID": work.data.id,
        "ANTHROPIC_WORK_SECRET": work.secret or "",
    }
    forward = [arg for name in SANDBOX_ENV for arg in ("-e", name)]
    launcher = await asyncio.create_subprocess_exec(
        "docker", "run", "--rm", "--detach", *forward, "your-image", env=env
    )
    await launcher.wait()


async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        async for work in client.beta.environments.work.poller(
            environment_id=environment_id,
            environment_key=environment_key,
            auto_stop=False,  # the launched sandbox owns the stop call
        ):
            await launch_container(work)


asyncio.run(main())
```

### Run the SDK worker inside the sandbox

Replace the `ant beta:worker run` entrypoint with an SDK entrypoint when the sandbox must [serve custom tools](managed-agents-self-hosted-sandboxes-custom-tools.md) or use [non-default memory sync settings](managed-agents-self-hosted-sandboxes-memory.md#configure-sync). The entrypoint constructs `EnvironmentWorker` and calls `handle_item()`, which reads the same `ANTHROPIC_*` variables that the spawn script forwards.

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
import asyncio
import contextlib
import os
import signal
from anthropic import AsyncAnthropic
from anthropic.lib.environments import EnvironmentWorker


async def main() -> None:
    async with AsyncAnthropic(auth_token=os.environ["ANTHROPIC_ENVIRONMENT_KEY"]) as client:
        worker = EnvironmentWorker(client, workdir="/workspace")
        # With no arguments, handle_item() reads the ANTHROPIC_* variables the spawn
        # script forwarded, including ANTHROPIC_WORK_SECRET.
        task = asyncio.create_task(worker.handle_item())
        # Cancelling the task when the container is stopped lets the worker upload
        # changed memory files and remove the store directories before it exits.
        loop = asyncio.get_running_loop()
        for signum in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(signum, task.cancel)
        with contextlib.suppress(asyncio.CancelledError):
            await task


asyncio.run(main())
```

## Stage files for a session

Anthropic doesn't mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available:

1.  Pass file references, such as an S3 path or commit SHA, in the session's `metadata` field.
2.  In your spawn script or `--on-work` handler, retrieve the session (`GET /v1/sessions/{session_id}`) and read `metadata`. The claimed work item carries the session ID but not the metadata.
3.  Stage the files into the working directory before tool execution begins.

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
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    metadata={"input_file": "s3://my-bucket/data.csv"},
)
```

## Next steps



[Monitor and troubleshoot](managed-agents-self-hosted-sandboxes-operations.md)

Read queue depth, stop sessions and workers cleanly, and fix common failures.



[Security model](managed-agents-self-hosted-sandboxes-security.md)

Shared responsibility model for self-hosted sandbox environments.
