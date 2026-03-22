---
category: "19-Reference"
fetched_at: "2026-03-20T10:37:07Z"
source_url: "https://www.anthropic.com/research/long-running-tasks"
title: "Long-Running Claude for Scientific Research \\ Anthropic"
---

# Long-Running Claude for Scientific Research

Feb 1, 2026

## The Premise

Use of coding agents for scientific research today typically follows a conversational pattern: you ask a question, get a response, and iterate. Certain flavors of scientific computing tasks don’t clearly fit that model—e.g. reimplementing a numerical solver, converting legacy scientific software written in an old Fortran dialect to a modern language like Rust, or debugging a large codebase against a reference implementation. These are tasks where the work is well-scoped, the success criteria are clear, and human oversight might be needed occasionally rather than continuously to guide overall approach. These could take days or even weeks of wall-clock time.

The [C compiler project](https://www.anthropic.com/engineering/building-c-compiler) demonstrated a version of this, where Claude worked across roughly 2,000 sessions to build a C compiler capable of compiling the Linux kernel. With a set of tests, progress tracking, and an autonomous execution loop, a parallel team of Claudes was able to make sustained progress on a large technical project across many independent sessions until all success criteria were met.

This tutorial describes how to set up a similar pattern for scientific computing using Claude Code, with a typical academic lab in mind. We’ll use an HPC cluster running the SLURM job scheduler as our working example, but the core ideas—a progress file, a test oracle, an agent prompt with clear rules—apply regardless of where you run Claude Code. As of writing, a 5x or 20x Max plan subscription, depending on the scope of task, should be adequate for most workflows of this nature.

## Iterate on the Plan Locally

In this new way of working, you should spend most of your time crafting the project brief that clearly articulates the project’s deliverables and relevant context. Before moving to the cluster, it is useful to iterate on this brief locally, working with Claude to refine it. Save the result as a file named `CLAUDE.md` at the project root; Claude will automatically keep it in its context.

A good project prompt should also have an orientation protocol, which tells the agent what to do first at the start of a new session before it writes any code, e.g. “Read CHANGELOG.md—especially ‘Current status’ and ‘Next steps’. Pick the highest-impact task from the priority list.” This prevents the failure mode of the agent diving into code without understanding what’s already been done or re-attempting approaches that already failed.

The initial parts of the project could also be done on [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web), and then the `/teleport` command can be used to transfer the conversation and its context to a local terminal or compute cluster when needed.

## Memory Across Sessions

The progress file, which by convention we call here `CHANGELOG.md`, is the agent’s portable long-term memory, acting as a sort of lab notes. A good progress file might track: (1) current status, (2) completed tasks, (3) failed approaches and why they didn’t work, (4) accuracy tables at key checkpoints, and (5) known limitations. The failed approaches are the most important—without them, successive sessions will re-attempt the same dead ends. An entry might look like: “Tried using Tsit5 for the perturbation ODE, system is too stiff. Switched to Kvaerno5.” Your `CLAUDE.md` should instruct the agent to update `CHANGELOG.md` continuously.

## The Test Oracle

Long-running autonomous work depends on the agent having a way to know whether it’s making progress. For scientific code, this could be a reference implementation, a clearly quantifiable objective, or an existing test suite. It can be helpful to instruct the agent to expand the test suite and run tests as it works, to prevent regressions.

## Git as Coordination

Git and GitHub are good ways to monitor and coordinate the agent’s progress in a hands-off manner. The agent should commit and push after every meaningful unit of work. This gives you a recoverable history if something goes awry, makes progress visible locally, and prevents work from being lost if e.g. your compute allocation runs out mid-session.

Practically, this could be a set of instructions in `CLAUDE.md`, e.g. “Commit and push after every meaningful unit of work. Run `pytest tests/ -x -q` before every commit. Never commit code that breaks existing passing tests.”

For steering the agent, you can always SSH into the cluster and manually reprompt and/or update its instructions. You can also use Claude Code hooks to enable collaborative steering without attaching to the session directly. For example, a `PostToolUse` hook can periodically pull from the remote repository and check a designated file (like `STEERING.md`) for new instructions from collaborators. When new instructions appear, the hook injects them into Claude’s context, letting you or collaborators redirect the agent mid-task. This lets multiple people coordinate a run by simply pushing a file to the repo. See the [hooks guide](https://code.claude.com/docs/en/hooks-guide) for setup details.

## The Execution Loop

As mentioned above, it’s often useful to first iterate on the plan locally until you have one that looks reasonable, and is encoded in `CLAUDE.md`. Once you’re ready, start a Claude Code session inside a terminal multiplexer like tmux on a compute node, tell the agent where to find your codebase, and let it work. Because the session runs inside tmux, you can detach, close your laptop, and occasionally check on progress. On an HPC cluster you might request a node through SLURM; on a cloud VM or workstation you can typically just start tmux directly.

An example SLURM job script that launches Claude Code in a tmux session might look like the following:

```
bash#!/bin/bash
#SBATCH --job-name=claude-agent
#SBATCH --partition=GPU-shared
#SBATCH --gres=gpu:h100-32:1
#SBATCH --time=48:00:00
#SBATCH --output=agent_%j.log

cd $PROJECT/my-solver
source .venv/bin/activate
export TERM=xterm-256color

tmux new-session -d -s claude "claude; exec bash"
tmux wait-for claude
```

Copy

Once the job starts, you attach to the tmux session, give Claude Code direction (e.g., “Read `CHANGELOG.md` and pick up the next task”), and detach when you’re satisfied it’s on the right track. You can re-attach whenever you want to check in, steer, or start a new task using something like:

```
bashsrun --jobid=JOBID --overlap --pty tmux attach -t claude
```

Copy

### The Ralph loop

As models get better, they require less bespoke orchestration (prompt engineering, RAG, context stuffing, …). Current models can however suffer from *agentic laziness*—when asked to complete a complex, multi-part task, they can sometimes finish part of the task before finding an excuse to stop (“It’s getting late, let’s pick back up again tomorrow”).

A useful orchestration pattern today is the [*Ralph loop*](https://ghuntley.com/loop/), which is essentially a for loop which kicks the agent back into context when it’s done, and asks if it’s *really* done. This can be useful for long-running tasks since the agent will admit the task is not up to spec, and continue until it is.

Ralph can be installed via `/plugin`. A typical invocation prompt in Claude Code could look like:

```
claude code/ralph-loop:ralph-loop "Please keep working on the task until the success criterion
of 0.1% accuracy across the entire parameter range is achieved."
--max-iterations 20 --completion-promise "DONE"
```

Copy

Here, Claude will iterate up to 20 times until it guarantees that the task is done with a “DONE” incantation. Instead of manually SSH’ing into the cluster and running commands inside the interactive Claude Code session, you can always ask a local version of Claude Code (e.g., on your laptop) to do this.

## An Application, and Conclusions

As a concrete example, I used these patterns with Claude Opus 4.6 to [implement a differentiable cosmological Boltzmann solver](https://github.com/smsharma/clax), which is a numerical code that predicts what the afterglow of the Big Bang—the Cosmic Microwave Background, or CMB—should look like given a set of cosmological parameters (e.g., dark energy fraction). It does this by evolving coupled equations for photons, baryons, neutrinos, and dark matter through the early universe. Boltzmann solvers like [CLASS](http://class-code.net/) and [CAMB](https://camb.info/) are core pieces of scientific infrastructure in cosmology, enabling parameter estimation from surveys like *Planck* and the *Simons Observatory*.

The implementation is fully differentiable through JAX, enabling gradient-based inference. Complementing [existing codes](https://github.com/ohahn/DISCO-EB) which come with significant simplifications, this solver covers the full pipeline through to various CMB observables. Using the [CLASS C source](https://github.com/lesgourg/class_public) as a test oracle and a progress file tracking accuracy tables and failed numerical approaches, Claude built it from scratch over a few days of wall-clock time, reaching sub-percent agreement with CLASS. This kind of task is structurally different from the C compiler project, which can be farmed out to a large number of parallel agents. A Boltzmann solver on the other hand is a deeply coupled pipeline: a subtle error in the recombination module can silently shift the visibility function, which changes the diffusion damping scale, and so on. Debugging requires tracing causally through the entire chain, which is better suited to a single agent working sequentially, spawning sub-agents as needed, and using the reference implementation to bisect discrepancies and continuously testing its work.

I asked Claude to reconstruct the accuracy of some of the main deliverables of the code—the various CMB angular power spectra—over the course of the project, also labeling milestones. It produced the plot above, showing the path to sub-percent accuracy after running for a few days (the agent wasn’t running continuously during this period, and was restarted several times). The agent’s progress was a bit clunky—it can make mistakes that would be obvious to a cosmologist, such as tripping over different gauge conventions—but it kept making sustained progress towards the stated goal of sub-percent accuracy.

While the resulting solver is not production-grade, it demonstrates that agent-driven development can compress months or even years of researcher work into days.

A universal experience in machine learning research is wanting to launch an experiment (e.g., a training run) overnight and then have the satisfaction of seeing the results in the morning. Not running the experiment comes with an opportunity cost. These days, not running agents feels like it has a cost as well. If you have a compute allocation, a codebase with a test suite, and a well-defined accuracy target, every night you *don’t* run a session is potential progress left on the table. Scientific computing often bottlenecks on exactly the kind of work agents handle well—tracking down factors of 2, comparing intermediate values against a reference, running validation sweeps across parameter space. These are tasks researchers defer because they’re boring, not because they’re impossible.

#### Footnotes


## Related content

### Labor market impacts of AI: A new measure and early evidence

[Read more](/research/labor-market-impacts)

### An update on our model deprecation commitments for Claude Opus 3

[Read more](/research/deprecation-updates-opus-3)

### The persona selection model

[Read more](/research/persona-selection-model)
