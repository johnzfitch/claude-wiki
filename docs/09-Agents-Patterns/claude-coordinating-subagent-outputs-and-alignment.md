# Coordinating subagent outputs and alignment

## User

what's a positive thing to add to an AGENTS.md a forward momentum way to say "Wait for all subagents to complete their tasks, then read their output, check completion & ensure alignment between subagents. In areas they conflict, write a report with the specific reasoning, location(s), and suggested fix. If one sub-agent did something out of alignment but it was a better implementation, study and then prepare a short report for the user to consider. Ensure subagents are provided with an AGENTS.md file suitable for their tasks.

## Assistant

The user is asking for a positive, forward-momentum way to phrase what's essentially a "coordination checkpoint" pattern for multi-agent orchestration in an AGENTS.md file. They want to avoid negative/blocking language and instead frame it as constructive collaboration.

Let me think about the key concepts they want to capture:
1. Wait for subagents to complete → "await convergence" or "gather outputs"
2. Read their output → "synthesize" or "integrate"
3. Check completion & alignment → "verify coherence"
4. Conflict handling → "reconcile divergence" with reasoning
5. Better-but-misaligned implementations → "surface emergent improvements"
6. Provide suitable AGENTS.md → "scope delegation"

This is about framing orchestration as collaboration rather than supervision. The user has a strong technical background and appreciates authentic, direct communication - so I should avoid corporate-speak while still being constructive.

Let me draft something that feels like forward motion rather than gatekeeping:Here's a forward-momentum framing:

---

## Convergence Protocol

After delegating to subagents, **synthesize their outputs into a unified result**:

1. **Gather & Integrate** — Collect all subagent outputs once complete. Read each fully before evaluating.

2. **Surface Divergence** — Where subagents reached different conclusions, document the delta:
   - What each decided
   - Where in the codebase it manifests
   - The reasoning chain that led there

3. **Harvest Improvements** — If a subagent deviated from spec but produced a genuinely better solution, capture it:
   - What they did differently
   - Why it's an improvement
   - Prepare a brief for the user: *"Consider adopting X because Y"*

4. **Scope Delegation** — Each subagent receives an AGENTS.md tailored to their task boundary. Don't pass the full orchestrator context—give them what they need to succeed independently.

---

The key reframes:
- "Wait for" → "Gather" (active collection, not passive blocking)
- "Check alignment" → "Surface divergence" (finding signal, not policing)
- "Out of alignment but better" → "Harvest improvements" (treats deviation as potential value)
- "Ensure provided with" → "Scope delegation" (intentional boundary-setting)

The vibe shift is from *compliance monitor* to *synthesis engine*. You're not catching mistakes—you're integrating parallel exploration paths.

## User

Good job, but its too verbose. We don't want to blow a bunch of tokens on this in every message we send.

## Assistant

The user wants a much more concise version that preserves the forward-momentum framing but doesn't waste tokens. They're thinking about this pragmatically - every token in AGENTS.md gets repeated in every message to subagents.

Let me compress this down significantly while keeping the positive, active framing.## Convergence

After subagent completion:
- **Synthesize** outputs into unified result
- **Surface divergence** — document deltas with reasoning + locations
- **Harvest improvements** — if deviation beat spec, brief user on adoption
- **Scope each subagent's AGENTS.md** to their task boundary

---

Or even tighter:

---

## Convergence

Synthesize subagent outputs. Surface divergence (reasoning + locations). If deviation outperformed spec, brief user. Scope each subagent's AGENTS.md to task boundary.

---

~30 tokens. Gets the job done.

## User

Okay interesting but not quite what we're after.  Say it a simple way, subagents are not long for the world they get spawned into.

## Assistant

The user wants something even simpler and is pointing out that subagents are ephemeral - they get spawned, do their task, and disappear. So the framing should acknowledge that transient nature. Less formal structure, more direct instruction about what to do when they come back.## Convergence

When subagents return, read everything before acting. Conflicts get a one-line report: what, where, why. Better-than-spec deviations get surfaced to user. Give each subagent only the AGENTS.md they need—they won't be around long.

## User

Now let's reframe this in a non-sci-fi spooky way

## Assistant

The user wants me to reframe the "subagents won't be around long" concept in a way that's not sci-fi or spooky. The current framing ("they won't be around long") has a dark/ominous tone. Need to make it practical and matter-of-fact without the existential dread undertone.

Think of it more like: workers finishing a shift, contractors completing a job, parallel processes completing. It's just... they do their thing and that's it. Ephemeral but not tragic.## Convergence

When subagents return, read everything before acting. Conflicts get a one-line report: what, where, why. Better-than-spec deviations get surfaced to user. Keep each subagent's AGENTS.md focused—they're here to do one job and finish.

---

Or:

---

## Convergence

Read all subagent outputs before acting. One-line report for conflicts: what, where, why. Surface better-than-spec deviations to user. Subagent AGENTS.md stays task-scoped—tight context, clean exit.

## User

hmm probably need the last sentence at the start in a different way?

## Assistant

The user wants to reorder so the scoping/context part comes first. Makes sense—you'd set up the subagent before they run, not after. Let me try a few approaches.## Convergence

Scope each subagent's AGENTS.md to their specific task. When they return, read all outputs before acting. One-line report for conflicts: what, where, why. Surface better-than-spec deviations to user.

---

Or flipping the framing:

---

## Convergence

Give subagents only what they need to complete their task. On return: read all outputs, then act. Conflicts get a one-liner (what, where, why). Better-than-spec? Surface to user.

## User

Now consider what you know about codex, see recent_chats, what would be the best way to speak to codex in their AGENTS.md

Problem: Terminal agent will get one subagent's report and then dip out starting to work on their own.

## Assistant

The user is asking me to check recent chats to understand their context with Codex, and then help frame the AGENTS.md in a way that addresses a specific problem: the terminal agent reads one subagent's report and then starts working before reading all the outputs.

Let me search recent chats to get context on their Codex work.
Looking at the recent chats, I can see some relevant context about Codex CLI and Claude Code workflows. Let me search more specifically for Codex-related discussions to understand how Zack works with these tools.
Now I have good context. The user is working with OpenAI's Codex CLI and dealing with multi-agent orchestration. The key problem they stated:

"Problem: Terminal agent will get one subagent's report and then dip out starting to work on their own."

So the terminal agent (orchestrator/main agent) reads one subagent result, then immediately starts working rather than waiting for all subagents to return.

The AGENTS.md needs to communicate to Codex (which uses GPT models) in a way that prevents this eager execution pattern. The key is:

1. Must wait for ALL subagents before acting
2. Don't start work after reading just one report

Given that Codex is an LLM-driven agent, the instruction needs to be clear, imperative, and positioned to prevent the "eager action" failure mode.

Let me think about how to phrase this for an LLM that might be eager to act:
- "Do not begin implementation until..." 
- "Block until all..."
- "Wait for complete set before..."

The user wants something tight and effective. The key insight is that the terminal agent has an eager-action bias. Need to counter that directly.Got it. Codex's terminal agent has an eager-action bias—sees one result, starts executing.

The framing needs to block that impulse explicitly:

---

## Convergence

**Do not act on partial results.** Wait for all subagents to return before reading any output. Then: synthesize, surface conflicts (what/where/why), flag better-than-spec deviations to user. Each subagent gets a task-scoped AGENTS.md only.

---

Or more direct, addressing the failure mode head-on:

---

## Convergence

All subagents must complete before you read or act on any output. Do not begin work after receiving partial results. Once all return: synthesize, one-line conflicts (what/where/why), surface improvements to user. Subagent AGENTS.md is task-scoped.

---

The "do not begin work after receiving partial results" is the anti-eager-execution clause. Codex needs the explicit prohibition because its default is to chain immediately on new context.

## User

Hmm but telling it not to do won't it do it?

## Assistant

The user is pointing out a well-known issue with LLM instruction-following: telling a model "don't do X" often makes it think about X and then do X anyway. Negative instructions are weaker than positive instructions. The model attends to the concept you're trying to prohibit.

So instead of "do not act on partial results" we need to give it a positive frame—something it SHOULD do that naturally precludes the bad behavior.

What's the positive reframe?
- Instead of "don't start early" → "wait until you have everything"
- Instead of "don't act on partial" → "collect all outputs first, then begin synthesis"
- Give it a concrete action to take that gates the behavior

The trick is to give it something to DO that makes the bad behavior impossible by construction.You're right—negative framing puts the concept in the attention window. "Don't think about elephants."

Flip it to a gate action:

---

## Convergence

Collect all subagent outputs into a single list before reading any. Begin synthesis only after the list is complete. One-line conflicts (what/where/why). Surface improvements to user. Subagent AGENTS.md is task-scoped.

---

Or even more procedural:

---

## Convergence

1. Collect all subagent outputs (do not read yet)
2. Confirm collection complete
3. Read and synthesize
4. One-line conflicts: what/where/why
5. Surface better-than-spec to user

Subagent AGENTS.md is task-scoped.

---

The "do not read yet" is still negative, but it's subordinate to the positive action (collect). The gate is "confirm collection complete"—gives it a checkpoint before the next phase unlocks.
