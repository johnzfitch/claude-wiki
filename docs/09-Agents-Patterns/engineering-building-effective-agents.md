<!-- Source: https://www.anthropic.com/engineering/building-effective-agents -->

# Building Effective Agents

**Published:** Dec 19, 2024
**Authors:** Erik Schluntz and Barry Zhang

## Introduction

After collaborating with numerous teams developing LLM agents across industries, Anthropic found that "the most successful implementations weren't using complex frameworks or specialized libraries."

## What are agents?

The term "agent" has multiple definitions. Some define agents as fully autonomous systems operating independently over extended periods using various tools. Others describe more prescriptive implementations following predefined workflows.

Anthropic distinguishes between two agentic system types:

- **Workflows**: Systems where LLMs and tools are orchestrated through predefined code paths
- **Agents**: Systems where LLMs dynamically direct their own processes and tool usage

## When (and when not) to use agents

Developers should pursue "the simplest solution possible, and only increasing complexity when needed." Agentic systems trade latency and cost for better task performance. Workflows offer predictability for well-defined tasks, while agents suit situations requiring flexibility and model-driven decision-making at scale.

## When and how to use frameworks

Available frameworks include the Claude Agent SDK, Strands Agents SDK by AWS, Rivet, and Vellum. These simplify standard tasks like calling LLMs and chaining calls together. However, they create abstraction layers that obscure underlying prompts and responses, making debugging harder.

Developers should "start by using LLM APIs directly: many patterns can be implemented in a few lines of code."

## Building blocks, workflows, and agents

### The Augmented LLM

The foundational building block enhances LLMs with retrieval, tools, and memory capabilities. Models can generate search queries, select tools, and determine what information to retain.

### Workflow: Prompt Chaining

This decomposes tasks into sequential steps where each LLM call processes the previous output. Programmatic checks ensure the process stays on track. Use this for tasks decomposable into fixed subtasks, trading latency for accuracy.

**Examples**: Marketing copy generation followed by translation; document outline creation with validation before writing.

### Workflow: Routing

Routing classifies inputs and directs them to specialized followup tasks, enabling separation of concerns and specialized prompts.

**Examples**: Directing different customer service query types to appropriate processes; routing easy questions to smaller models like Claude Haiku and complex ones to Claude Sonnet.

### Workflow: Parallelization

Two variations exist:
- **Sectioning**: Breaking tasks into independent parallel subtasks
- **Voting**: Running the same task multiple times for diverse outputs

Parallelization works when subtasks parallelize for speed or when multiple perspectives increase confidence.

**Examples**: Guardrail screening; code vulnerability reviews; content appropriateness evaluation.

### Workflow: Orchestrator-workers

A central LLM dynamically breaks down tasks, delegates to worker LLMs, and synthesizes results. This suits complex tasks with unpredictable subtask needs.

**Examples**: Coding products making complex multi-file changes; search tasks gathering information from multiple sources.

### Workflow: Evaluator-optimizer

One LLM generates responses while another provides evaluation and feedback in a loop. Effective when clear evaluation criteria exist and iterative refinement adds measurable value.

**Examples**: Literary translation refinement; complex multi-round search tasks.

### Agents

Agents are emerging in production as LLMs mature in reasoning, planning, tool usage, and error recovery. They "begin their work with either a command from, or interactive discussion with, the human user."

During execution, agents gain "ground truth" from the environment at each step to assess progress. They may pause for human feedback at checkpoints or when encountering blockers.

"Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop."

**When to use**: Open-ended problems where required steps are unpredictable and a fixed path cannot be hardcoded. Agents' autonomy makes them ideal for scaling trusted-environment tasks, though they incur higher costs and potential for compounding errors.

**Examples**: Coding agents resolving SWE-bench tasks; computer use implementations.

## Core principles for implementation

1. Maintain **simplicity** in agent design
2. Prioritize **transparency** by explicitly showing planning steps
3. Craft agent-computer interfaces through thorough tool **documentation and testing**

## Appendix 1: Agents in practice

### Customer support

Customer support naturally combines chatbot interfaces with tool-enhanced capabilities. Success can be measured through user-defined resolutions. Some companies use usage-based pricing, charging only for successful resolutions.

### Coding agents

Software development shows remarkable potential for LLM features. Solutions are verifiable through automated testing, enabling iterative refinement. Agents can solve real GitHub issues, though human review remains crucial for broader system requirements.

## Appendix 2: Prompt engineering your tools

Tool definitions deserve equal prompt engineering attention as overall prompts. "Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts."

When designing tool formats:
- Provide sufficient tokens for reasoning before models constrain themselves
- Keep formats close to naturally occurring internet text
- Eliminate formatting overhead like line counting

Invest effort in agent-computer interfaces (ACI) equal to human-computer interface (HCI) design. Include example usage, edge cases, input requirements, and clear tool boundaries in definitions.
