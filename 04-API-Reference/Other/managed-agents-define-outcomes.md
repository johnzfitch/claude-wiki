---
title: "Define outcomes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/define-outcomes"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fdefine-outcomes)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

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

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

# Define outcomes

Copy page



Tell the agent what 'done' looks like, and let it iterate until it gets there.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

An outcome tells the session what the end result should look like and how to measure its quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.

When you define an outcome, the harness automatically provisions a *grader* to evaluate the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices.

The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric. That feedback is handed back to the agent for the next iteration.

## Create a rubric

A rubric is a markdown document describing per-criterion scoring. The rubric is required.

### Tips for writing effective rubrics

Structure the rubric as explicit, gradeable criteria, such as "The CSV contains a price column with numeric values" rather than "The data looks good." The grader scores each criterion independently, so vague criteria produce noisy evaluations.

If you don't have a rubric on hand, try giving Claude an example of a known-good artifact and asking it to analyze what makes that content good, then turn that analysis into a rubric. This middle-ground approach often produces better results than writing criteria from scratch.

Example rubric:

```python
# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
- Growth rate assumptions are explicitly stated and reasonable

## Cost Structure
- COGS and operating expenses are modeled separately
- Margins are consistent with historical trends or deviations are justified

## Discount Rate
- WACC is calculated with stated assumptions for cost of equity and cost of debt
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Terminal Value
- Uses either perpetuity growth or exit multiple method (stated which)
- Terminal growth rate does not exceed long-term GDP growth

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
- Key assumptions are on a separate "Assumptions" sheet
- Sensitivity analysis on WACC and terminal growth rate is included
```



Pass the rubric as inline text on `user.define_outcome` (see [Create a session with an outcome](#create-a-session-with-an-outcome)), or upload it through the Files API for reuse across sessions.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import time
from pathlib import Path

from anthropic import Anthropic

client = Anthropic()

RUBRIC = """# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
"""
Path("/tmp/rubric.md").write_text(RUBRIC)

rubric = client.files.upload(file=Path("/tmp/rubric.md"))
print(f"Uploaded rubric: {rubric.id}")
```

## Create a session with an outcome

The following examples create a [session](managed-agents-sessions.md) for an existing [agent](managed-agents-agent-setup.md) and [environment](managed-agents-environments.md) (both created separately), then send a `user.define_outcome` event. The agent begins work immediately. No additional user message event is required.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# Create a session
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Financial analysis on Costco",
)

# Define the outcome — agent starts working on receipt
client.beta.sessions.events.send(
    session_id=session.id,
    events=[
        {
            "type": "user.define_outcome",
            "description": "Build a DCF model for Costco in .xlsx",
            "rubric": {"type": "text", "content": RUBRIC},
            # or: "rubric": {"type": "file", "file_id": rubric.id},
            "max_iterations": 5,  # optional; default 3, max 20
        }
    ],
)
```



You can also define the outcome in the create request itself: pass a single `user.define_outcome` event in [`initial_events`](managed-agents-sessions.md#seed-the-session-with-initial-events) to create the session and start work toward the outcome in one call.

## Outcome events

Progress on an outcome-oriented session is surfaced on the events [stream](managed-agents-events-and-streaming.md).

- `agent.*` events (such as messages and tool use) show progress toward the outcome.
- `span.outcome_evaluation_*` events are only emitted for outcome-oriented sessions and show the number of iteration loops and the grader's feedback process.
- You can also send `user.message` [events](managed-agents-reference.md#event-types) to an outcome-oriented session to direct the agent's work as it progresses, but it isn't required: the agent works toward the outcome on its own, iterating until it succeeds or runs out of iterations.
- A `user.interrupt` event pauses work on the current outcome and marks the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.
- After the final outcome evaluation, the session can be continued as a conversational session, or a new outcome can be started. The session retains history of the prior outcome.

### Define outcome user event



Only one outcome is supported at a time, but you may chain outcomes in sequence. To do this, send a new `user.define_outcome` event after the terminal `span.outcome_evaluation_end` event of the previous outcome.

This is the event you send to initiate an outcome. It is echoed back on receipt, including a `processed_at` timestamp and `outcome_id`.

```python
{
  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": { "type": "file", "file_id": "file_01..." },
  "max_iterations": 5
}
```



### Outcome evaluation start

Emitted once the grader starts an evaluation over one iteration loop. The `iteration` field is a 0-indexed revision counter: `0` is the first evaluation, `1` is the re-evaluation after the first revision, and so on.

```python
{
  "type": "span.outcome_evaluation_start",
  "id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:01:45Z"
}
```



### Outcome evaluation ongoing

Heartbeat emitted while the grader runs. The grader's internal reasoning is opaque: you see that it's working, not what it's thinking.

```python
{
  "type": "span.outcome_evaluation_ongoing",
  "id": "sevt_01ghi...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:02:10Z"
}
```



### Outcome evaluation end

Emitted when an outcome evaluation cycle ends: after the grader finishes evaluating one iteration, or when the session is interrupted while an outcome is active. The `result` field indicates what happens next.

| Result                   | Next                                                                                                                                                                                                                      |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `satisfied`              | Session transitions to `idle`.                                                                                                                                                                                            |
| `needs_revision`         | Agent starts a new iteration cycle.                                                                                                                                                                                       |
| `max_iterations_reached` | One final acknowledgment turn follows before the session transitions to `idle`. No further evaluation runs.                                                                                                               |
| `failed`                 | Session transitions to `idle`. Returned when the rubric does not apply to the deliverables, for example if the description and rubric contradict each other.                                                              |
| `interrupted`            | Emitted when the session is interrupted while an outcome is active, even if evaluation hadn't started yet. If no `outcome_evaluation_start` fired before the interrupt, `outcome_evaluation_start_id` is an empty string. |

```python
{
  "type": "span.outcome_evaluation_end",
  "id": "sevt_01jkl...",
  "outcome_evaluation_start_id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated, sensitivity table is included...",
  "iteration": 0,
  "usage": {
    "input_tokens": 2400,
    "output_tokens": 350,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 1800
  },
  "processed_at": "2026-03-25T14:03:00Z"
}
```



## Check outcome status

You can either listen on the [event stream](managed-agents-events-and-streaming.md) for `span.outcome_evaluation_end`, or poll `GET /v1/sessions/{session_id}` and read `outcome_evaluations[].result`. Until an evaluation completes, `result` reports `pending`, `running`, or `evaluating`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
session = client.beta.sessions.retrieve(session.id)

for outcome in session.outcome_evaluations:
    print(f"{outcome.outcome_id}: {outcome.result}")
    # outc_01a...: satisfied
```

## Retrieve deliverables

The agent writes output files to `/mnt/session/outputs/` inside the sandbox. To retrieve them, list files through the [Files API](../Guides/build-with-claude-files.md) with the session ID as the `scope_id`, then download them by ID. Filtering by `scope_id` requires the `managed-agents-2026-04-01` beta header on the list request, so the SDK and CLI examples make that call through the `beta` namespace and pass the header explicitly. Files appear in the list shortly after the agent finishes writing them, sometimes a few seconds after the session goes idle. If a file you expect is not listed yet, list again after a short delay; once it appears in the list, its upload has finished.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# List files produced by this session
# scope_id filtering requires the managed-agents beta on the files request
files = client.beta.files.list(scope_id=session.id, betas=["managed-agents-2026-04-01"])
for file in files:
    print(file.id, file.filename)

# Download a file
if files.data:
    content = client.files.download(files.data[0].id)
    content.write_to_file("/tmp/output.txt")
```

## Next steps

[Authenticate with vaults](managed-agents-vaults.md)

Register per-user credentials when creating sessions.



[Session event stream](managed-agents-events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.



[Adding files](managed-agents-files.md)

Upload files and mount them in your sandbox for reading and processing.
