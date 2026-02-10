::: {#0d4a77a4 .cell .markdown}
# Building a One-Liner Research Agent

Research tasks consume hours of expert time: market analysts manually
gathering competitive intelligence, legal teams tracking regulatory
changes, engineers investigating bug reports across documentation. The
core challenge isn\'t finding information but knowing what to search for
next based on what you just discovered.

The Claude Agent SDK makes it possible to build agents that autonomously
explore external systems without a predefined workflow. Unlike
traditional workflow automations that follow fixed steps, research
agents adapt their strategy based on what they find\--following
promising leads, synthesizing conflicting sources, and knowing when they
have enough information to answer the question.

## By the end of this cookbook, you\'ll be able to:

- Build a research agent that autonomously searches and synthesizes
  information with a few lines of code

This foundation applies to any task where the information needed isn\'t
available upfront: competitive analysis, technical troubleshooting,
investment research, or literature reviews.

# Why Research Agents?

Research is an ideal agentic use case for two reasons:

1.  **Information isn\'t self-contained**. The input question alone
    doesn\'t contain the answer. The agent must interact with external
    systems (search engines, databases, APIs) to gather what it needs.
2.  **The path emerges during exploration**. You can\'t predetermine the
    workflow. Whether an agent should search for company financials or
    regulatory filings depends on what it discovers about the business
    model. The optimal strategy reveals itself through investigation.

In its simplest form, a research agent searches the web and synthesizes
findings. Below, we\'ll build exactly that with the Claude Agent SDK\'s
built-in web search tool in just a few lines of code.

Note: You can also view the full list of [Claude Code\'s built-in
tools](https://docs.claude.com/en/docs/claude-code/settings#tools-available-to-claude)
:::

::: {#301fb086 .cell .markdown}
# Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

- Python fundamentals - comfortable with async/await, functions, and
  basic data structures
- Basic understanding of agentic patterns - we recommend reading
  [Building effective
  agents](https://www.anthropic.com/engineering/building-effective-agents)
  first if you\'re new to agents

**Required Tools**

- Python 3.11 or higher
- Anthropic API key [(get one here)](https://console.anthropic.com)

**Recommended:**

- Familiarity with the Claude Agent SDK concepts
- Understanding of tool use patterns in LLMs

## Setup

First, install the required dependencies:
:::

::: {#ab9830f9 .cell .code}
``` python
%%capture
%pip install -U claude-agent-sdk python-dotenv
```
:::

::: {#d88272cf .cell .markdown}
Note: Ensure your .env file contains:

``` bash
ANTHROPIC_API_KEY=your_key_here
```

Load your environment variables and configure the client:
:::

::: {#c41abcdf .cell .code execution_count="2"}
``` python
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-opus-4-5"
```
:::

::: {#041415b8 .cell .markdown}
## Building Your First Research Agent

Let\'s start with the simplest possible implementation: a research agent
that can search the web and synthesize findings. With the Claude Agent
SDK, this takes just a few lines of code.

The key is the query() function, which creates a stateless agent
interaction. We\'ll provide Claude with a single tool, WebSearch, and
let it autonomously decide when and how to use it based on our research
question.
:::

:::: {#b00890fb .cell .code execution_count="3"}
``` python
from utils.agent_visualizer import (
    display_agent_response,
    print_activity,
)

from claude_agent_sdk import ClaudeAgentOptions, query

messages = []
async for msg in query(
    prompt="Research the latest trends in AI agents and give me a brief summary and relevant citiations links.",
    options=ClaudeAgentOptions(model=MODEL, allowed_tools=["WebSearch"]),
):
    print_activity(msg)
    messages.append(msg)
```

::: {.output .stream .stdout}
    🤖 Using: WebSearch()
    🤖 Using: WebSearch()
    🤖 Using: WebSearch()
    ✓ Tool completed
    ✓ Tool completed
    ✓ Tool completed
    🤖 Thinking...
:::
::::

:::: {#e4556936 .cell .code execution_count="4"}
``` python
display_agent_response(messages)
```

::: {.output .display_data}

<style>
.pretty-card {
    font-family: ui-sans-serif, system-ui;
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 14px 16px;
    margin: 10px 0;
    background: linear-gradient(#fff, #fff) padding-box,
                linear-gradient(135deg, #3b82f6, #9333ea) border-box;
    color: #111;
    box-shadow: 0 4px 12px rgba(0,0,0,.08);
}
.pretty-title {
    font-weight: 700;
    margin-bottom: 8px;
    font-size: 14px;
    color: #111;
}
.pretty-card pre,
.pretty-card code {
    background: #f3f4f6;
    color: #111;
    padding: 8px;
    border-radius: 8px;
    display: block;
    overflow-x: auto;
    font-size: 13px;
    white-space: pre-wrap;
}
.pretty-card img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
/* Tables: both pandas (.pretty-table) and markdown-rendered */
.pretty-card table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
    color: #111;
    margin: 0.5em 0;
}
.pretty-card th,
.pretty-card td {
    border: 1px solid #e5e7eb;
    padding: 6px 8px;
    text-align: left;
}
.pretty-card th {
    background: #f9fafb;
    font-weight: 600;
}
/* Markdown headings */
.pretty-card h1, .pretty-card h2, .pretty-card h3, .pretty-card h4 {
    margin: 0.5em 0 0.3em 0;
    color: #111;
}
.pretty-card h1 { font-size: 1.4em; }
.pretty-card h2 { font-size: 1.2em; }
.pretty-card h3 { font-size: 1.1em; }
/* Markdown lists and paragraphs */
.pretty-card ul, .pretty-card ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
.pretty-card p {
    margin: 0.5em 0;
}
.pretty-card hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1em 0;
}
</style>
<div class="pretty-card"><div class="pretty-title">Agent Response</div><h2>Latest Trends in AI Agents (2025) - Summary</h2>
<h3>🚀 Market Growth &amp; Adoption</h3>
<p>The AI agent market is experiencing explosive growth, nearly doubling from <strong>$3.7 billion (2023) to $7.38 billion (2025)</strong>, with projections reaching <strong>$103.6 billion by 2032</strong>. According to PwC's 2025 survey, <strong>79% of organizations</strong> have adopted AI agents, with <strong>88% of executives</strong> piloting or scaling autonomous agent systems.</p>
<h3>🔑 Key Trends</h3>
<p><strong>1. Rise of Multi-Agent Systems</strong><br />
Instead of single AI systems trying to do everything, 2025 has introduced the "orchestra approach" where multiple specialized agents collaborate—one gathers research, another drafts reports, and a third reviews. Frameworks like <strong>CrewAI, AutoGen, and LangGraph</strong> are enabling this coordination across enterprise departments.</p>
<p><strong>2. From Assistants to Autonomous Decision-Makers</strong><br />
AI agents are evolving from knowledge assistants to <strong>self-directed workers</strong> that can take initiative, make decisions, and complete multi-step tasks without constant human input. By 2029, <strong>80% of customer service issues</strong> are expected to be resolved entirely by autonomous agents.</p>
<p><strong>3. Model Context Protocol (MCP)</strong><br />
Anthropic's open standard provides a "USB-C for AI"—standardizing how language models connect with external systems, enabling structured multi-step workflows and access to real-time information.</p>
<p><strong>4. Two-Speed Enterprise Landscape</strong><br />
A divide is emerging: companies with existing automation are racing ahead with agentic AI, while others watch from the sidelines. Among highly automated enterprises, <strong>50%</strong> have either adopted or are preparing to adopt autonomous agents.</p>
<h3>⚠️ Key Challenges</h3>
<ul>
<li><strong>Integration with legacy systems</strong> (cited by ~60% of AI leaders)</li>
<li><strong>Trust issues</strong> for high-stakes tasks like financial transactions</li>
<li><strong>Enterprise readiness</strong>—organizations need to expose APIs and prepare infrastructure</li>
<li><strong>Reliability concerns</strong>—agents can misinterpret instructions or fail on edge cases</li>
</ul>
<h3>💼 Impact</h3>
<ul>
<li><strong>66%</strong> of adopters report measurable productivity gains</li>
<li>Early movers are cutting operational costs by up to <strong>40%</strong></li>
<li><strong>75% of executives</strong> believe AI agents will reshape the workplace more than the internet did</li>
<li><strong>87%</strong> agree AI agents augment roles rather than replace them</li>
</ul>
<hr />
<h2>Sources:</h2>
<ul>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai">The State of AI in 2025 - McKinsey</a></li>
<li><a href="https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality">AI Agents in 2025: Expectations vs. Reality - IBM</a></li>
<li><a href="https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html">PwC's AI Agent Survey</a></li>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage">Seizing the Agentic AI Advantage - McKinsey</a></li>
<li><a href="https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025">Gartner Hype Cycle Identifies Top AI Innovations in 2025</a></li>
<li><a href="https://www.deloitte.com/us/en/services/consulting/blogs/ai-adoption-challenges-ai-trends.html">AI Trends 2025: Adoption Barriers - Deloitte</a></li>
<li><a href="https://aws.amazon.com/blogs/aws-insights/the-rise-of-autonomous-agents-what-enterprise-leaders-need-to-know-about-the-next-wave-of-ai/">The Rise of Autonomous Agents - AWS</a></li>
<li><a href="https://terralogic.com/multi-agent-ai-systems-why-they-matter-2025/">Multi-Agent AI Systems in 2025 - Terralogic</a></li>
<li><a href="https://www.index.dev/blog/ai-agents-statistics">50+ Key AI Agent Statistics - Index.dev</a></li>
<li><a href="https://www.salesforce.com/news/stories/future-of-ai-agents-2025/">Future of AI Agents 2025 - Salesforce</a></li>
<li><a href="https://superagi.com/top-5-agentic-ai-trends-in-2025-from-multi-agent-collaboration-to-self-healing-systems/">Top 5 Agentic AI Trends - SuperAGI</a></li>
</ul></div>
:::
::::

::: {#b965c2ee .cell .markdown}
## What\'s happening here:

- `query()` creates a single-turn agent interaction (no conversation
  memory)
- `allowed_tools=["WebSearch"]` gives Claude permission to search the
  web without asking for approval
- The agent autonomously decides when to search, what queries to run,
  and how to synthesize results

**Visualization utilities from `utils.agent_visualizer`:**

- `print_activity()` - Shows the agent\'s actions in real-time (tool
  calls, thinking)
- `display_agent_response()` - Renders the final response as a styled
  HTML card
- `visualize_conversation()` - Creates a timeline view of the full
  conversation

That\'s it! A functional research agent in just a few lines of code. The
agent will search for relevant information, follow up on promising
leads, and provide a synthesized summary with citations.
:::

::: {#6b888772 .cell .markdown}
The query() function creates a stateless agent interaction. Each call is
independent---no conversation memory, no context from previous queries.
This makes it perfect for one-off research tasks where you need a quick
answer without maintaining state.

**How tool permissions work:**

The `allowed_tools=["WebSearch"]` parameter gives Claude permission to
search without asking for approval. This is critical for autonomous
operation:

- `Allowed tools` - Claude can use these freely (in this case,
  WebSearch)
- `Other tools` - Available but require approval before use
- `Read-only tools` - Tools like Read are always allowed by default
- `Disallowed tools` - Add tools to disallowed_tools to remove them
  entirely from Claude\'s context

**When to use stateless queries:**

- One-off research questions where context doesn\'t matter
- Parallel processing of independent research tasks
- Scenarios where you want fresh context for each query

**When not to use stateless queries:**

- Multi-turn investigations that build on previous findings
- Iterative refinement of research based on initial results
- Complex analysis requiring sustained context

Let\'s inspect what the agent actually did using the
visualize_conversation helper:
:::

:::: {#1d7c6d90 .cell .code execution_count="5"}
``` python
from utils.agent_visualizer import visualize_conversation

visualize_conversation(messages)
```

::: {.output .display_data}

    
<style>
.conversation-timeline {
    font-family: ui-sans-serif, system-ui;
    max-width: 900px;
    margin: 1em 0;
}
.timeline-header {
    background: linear-gradient(135deg, #3b82f6, #9333ea);
    color: white;
    padding: 12px 16px;
    border-radius: 12px 12px 0 0;
    font-weight: 700;
    font-size: 14px;
}
.timeline-body {
    border: 1px solid #e5e7eb;
    border-top: none;
    border-radius: 0 0 12px 12px;
    padding: 12px;
    background: #fafafa;
}
.msg-block {
    margin: 8px 0;
    padding: 10px 12px;
    border-radius: 8px;
    background: white;
    border-left: 3px solid #e5e7eb;
}
.msg-block.system { border-left-color: #6b7280; }
.msg-block.assistant { border-left-color: #3b82f6; }
.msg-block.tool { border-left-color: #10b981; background: #f0fdf4; }
.msg-block.subagent { border-left-color: #9333ea; background: #faf5ff; }
.msg-block.result { border-left-color: #f59e0b; background: #fffbeb; }
.msg-label {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 4px;
}
.msg-content {
    font-size: 13px;
    color: #111;
}
.msg-content pre {
    background: #f3f4f6;
    padding: 8px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 12px;
}
.tool-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
}
.tool-badge {
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-family: monospace;
}
.stats-bar {
    display: flex;
    gap: 16px;
    padding: 10px 12px;
    background: #f9fafb;
    border-radius: 8px;
    font-size: 12px;
    color: #374151;
    margin-top: 8px;
}
.stat-item { display: flex; gap: 4px; }
.stat-label { color: #6b7280; }
</style>

    <div class="conversation-timeline">
        <div class="timeline-header">🤖 Agent Conversation Timeline • claude-opus-4-5</div>
        <div class="timeline-body">
            <div class="msg-block system"><div class="msg-label">⚙️ System</div><div class="msg-content">Initialized (4e8497a9...)</div></div><div class="msg-block tool"><div class="msg-label">🔧 Tools</div><div class="tool-list"><span class="tool-badge">WebSearch: &quot;AI agents trends 2025 latest d...&quot;</span><span class="tool-badge">WebSearch: &quot;autonomous AI agents enterpris...&quot;</span><span class="tool-badge">WebSearch: &quot;multi-agent AI systems trends ...&quot;</span></div></div><div class="msg-block assistant"><div class="msg-label">🤖 Assistant</div><div class="msg-content"><h2>Latest Trends in AI Agents (2025) - Summary</h2>
<h3>🚀 Market Growth &amp; Adoption</h3>
<p>The AI agent market is experiencing explosive growth, nearly doubling from <strong>$3.7 billion (2023) to $7.38 billion (2025)</strong>, with projections reaching <strong>$103.6 billion by 2032</strong>. According to PwC's 2025 survey, <strong>79% of organizations</strong> have adopted AI agents, with <strong>88% of executives</strong> piloting or scaling autonomous agent systems.</p>
<h3>🔑 Key Trends</h3>
<p><strong>1. Rise of Multi-Agent Systems</strong><br />
Instead of single AI systems trying to do everything, 2025 has introduced the "orchestra approach" where multiple specialized agents collaborate—one gathers research, another drafts reports, and a third reviews. Frameworks like <strong>CrewAI, AutoGen, and LangGraph</strong> are enabling this coordination across enterprise departments.</p>
<p><strong>2. From Assistants to Autonomous Decision-Makers</strong><br />
AI agents are evolving from knowledge assistants to <strong>self-directed workers</strong> that can take initiative, make decisions, and complete multi-step tasks without constant human input. By 2029, <strong>80% of customer service issues</strong> are expected to be resolved entirely by autonomous agents.</p>
<p><strong>3. Model Context Protocol (MCP)</strong><br />
Anthropic's open standard provides a "USB-C for AI"—standardizing how language models connect with external systems, enabling structured multi-step workflows and access to real-time information.</p>
<p><strong>4. Two-Speed Enterprise Landscape</strong><br />
A divide is emerging: companies with existing automation are racing ahead with agentic AI, while others watch from the sidelines. Among highly automated enterprises, <strong>50%</strong> have either adopted or are preparing to adopt autonomous agents.</p>
<h3>⚠️ Key Challenges</h3>
<ul>
<li><strong>Integration with legacy systems</strong> (cited by ~60% of AI leaders)</li>
<li><strong>Trust issues</strong> for high-stakes tasks like financial transactions</li>
<li><strong>Enterprise readiness</strong>—organizations need to expose APIs and prepare infrastructure</li>
<li><strong>Reliability concerns</strong>—agents can misinterpret instructions or fail on edge cases</li>
</ul>
<h3>💼 Impact</h3>
<ul>
<li><strong>66%</strong> of adopters report measurable productivity gains</li>
<li>Early movers are cutting operational costs by up to <strong>40%</strong></li>
<li><strong>75% of executives</strong> believe AI agents will reshape the workplace more than the internet did</li>
<li><strong>87%</strong> agree AI agents augment roles rather than replace them</li>
</ul>
<hr />
<h2>Sources:</h2>
<ul>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai">The State of AI in 2025 - McKinsey</a></li>
<li><a href="https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality">AI Agents in 2025: Expectations vs. Reality - IBM</a></li>
<li><a href="https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html">PwC's AI Agent Survey</a></li>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage">Seizing the Agentic AI Advantage - McKinsey</a></li>
<li><a href="https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025">Gartner Hype Cycle Identifies Top AI Innovations in 2025</a></li>
<li><a href="https://www.deloitte.com/us/en/services/consulting/blogs/ai-adoption-challenges-ai-trends.html">AI Trends 2025: Adoption Barriers - Deloitte</a></li>
<li><a href="https://aws.amazon.com/blogs/aws-insights/the-rise-of-autonomous-agents-what-enterprise-leaders-need-to-know-about-the-next-wave-of-ai/">The Rise of Autonomous Agents - AWS</a></li>
<li><a href="https://terralogic.com/multi-agent-ai-systems-why-they-matter-2025/">Multi-Agent AI Systems in 2025 - Terralogic</a></li>
<li><a href="https://www.index.dev/blog/ai-agents-statistics">50+ Key AI Agent Statistics - Index.dev</a></li>
<li><a href="https://www.salesforce.com/news/stories/future-of-ai-agents-2025/">Future of AI Agents 2025 - Salesforce</a></li>
<li><a href="https://superagi.com/top-5-agentic-ai-trends-in-2025-from-multi-agent-collaboration-to-self-healing-systems/">Top 5 Agentic AI Trends - SuperAGI</a></li>
</ul></div></div><div class="msg-block result"><div class="msg-label">✅ Complete</div><div class="stats-bar"><span class="stat-item"><span class="stat-label">Turns:</span> 4</span> <span class="stat-item"><span class="stat-label">Tokens:</span> 4,145</span> <span class="stat-item"><span class="stat-label">Cost:</span> $0.51</span> <span class="stat-item"><span class="stat-label">Duration:</span> 51.1s</span></div></div>
        </div>
    </div>
    
:::
::::

::: {#22426729 .cell .markdown}
## From Prototype to Production: Three Key Improvements

Our one-line research agent works, but it\'s limited. Single queries
without memory can\'t handle iterative research (\"find X, then analyze
Y based on what you found\"). Let\'s explore three ways we can further
improve our implementation.

**1. Conversation Memory with ClaudeSDKClient**: Stateless queries
can\'t build on previous findings. If you ask \"What are the top AI
startups?\" then \"How are they funded?\", the second query has no
context about which startups you mean. We can use `ClaudeSDKClient` to
maintain conversation history across multiple queries.

**2. System Prompts for Specialized Behavior**: Research domains often
have specific requirements. Financial analysis needs different rigor
than tech news summaries. Use the system prompt to encode your research
standards, preferred sources, citation format, or output structure. See
our [agent prompting
guide](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents/prompts)
for research-specific examples.

**3. Multimodal Research with the Read Tool**: Real research isn\'t just
text. Market reports have charts, technical docs have diagrams,
competitive analysis requires screenshot comparison. Enable the `Read`
tool so Claude can analyze images, PDFs, and other visual content.

Let\'s implement these three changes for our research agent.
:::

:::: {#fa4c4d8f .cell .code execution_count="6"}
``` python
from claude_agent_sdk import ClaudeSDKClient

# System prompt with citation requirements for research quality
RESEARCH_SYSTEM_PROMPT = """You are a research agent specialized in AI.

When providing research findings:
- Always include source URLs as citations
- Format citations as markdown links: [Source Title](URL)
- Group sources in a "Sources:" section at the end of your response"""

messages = []
async with ClaudeSDKClient(
    options=ClaudeAgentOptions(
        model=MODEL,
        cwd="research_agent",
        system_prompt=RESEARCH_SYSTEM_PROMPT,
        allowed_tools=["WebSearch", "Read"],
        max_buffer_size=10 * 1024 * 1024,  # Increase to 10MB for image handling
    )
) as research_agent:
    # First query: Analyze the chart image
    await research_agent.query("Analyze the chart in research_agent/projects_claude.png")
    async for msg in research_agent.receive_response():
        print_activity(msg)
        messages.append(msg)

    # Second query: Use web search to validate/contextualize the chart findings
    await research_agent.query(
        "Based on the chart analysis, search for recent news or data that validates or provides context for these findings. Include source URLs."
    )
    async for msg in research_agent.receive_response():
        print_activity(msg)
        messages.append(msg)
```

::: {.output .stream .stdout}
    🤖 Using: Read()
    ✓ Tool completed
    🤖 Thinking...
    🤖 Using: Glob()
    ✓ Tool completed
    🤖 Thinking...
    🤖 Using: Read()
    ✓ Tool completed
    🤖 Thinking...
    🤖 Using: WebSearch()
    🤖 Using: WebSearch()
    🤖 Using: WebSearch()
    🤖 Using: WebSearch()
    ✓ Tool completed
    ✓ Tool completed
    ✓ Tool completed
    ✓ Tool completed
    🤖 Thinking...
:::
::::

::: {#i4blqsetg8 .cell .markdown}
### 🔧 Handling Large Responses and Buffer Limits {#wrench-handling-large-responses-and-buffer-limits}

When working with images or large data, you may encounter buffer
overflow errors:

    Fatal error in message reader: Failed to decode JSON: JSON message exceeded maximum buffer size of 1048576 bytes

**Why this happens:**

- The default `max_buffer_size` is 1MB (1,048,576 bytes)
- Images are base64-encoded in messages, significantly increasing size
- The chart image (\~200KB on disk) becomes \~270KB+ when
  base64-encoded, plus message overhead

**Solution:** Set `max_buffer_size` in `ClaudeAgentOptions` to a higher
value (e.g., 10MB) when working with images or large tool outputs.

**Best practices:**

- Set buffer size based on your use case: 10MB for typical multimodal
  work, higher for large document processing
- Consider if you really need to pass full images - sometimes
  descriptions or smaller thumbnails suffice
- Monitor for buffer errors and adjust accordingly
- Include citation requirements in your system prompt to ensure
  verifiable research outputs
:::

::: {#6eb4ed21 .cell .markdown}
## What\'s happening here: {#whats-happening-here}

This example combines all three improvements: conversation memory,
citation-aware system prompt, and multimodal analysis.

**Key components:**

  -----------------------------------------------------------------------
  Component                               Purpose
  --------------------------------------- -------------------------------
  `ClaudeSDKClient`                       Maintains conversation state
                                          across multiple queries

  `RESEARCH_SYSTEM_PROMPT`                Enforces citation formatting
                                          and source URLs

  `allowed_tools=["WebSearch", "Read"]`   Enables web search and
                                          image/document analysis

  `max_buffer_size=10MB`                  Handles base64-encoded images
                                          without overflow
  -----------------------------------------------------------------------

**Execution flow:**

1.  **First query** - Analyzes the chart image using the `Read` tool
2.  **First response loop** - Collects all messages until the agent
    completes
3.  **Second query** - Searches the web to validate/contextualize the
    chart findings
4.  **Context inheritance** - The second query remembers the chart
    analysis from the first

**Why `ClaudeSDKClient` vs `query()`:**

The `async with ClaudeSDKClient()` context manager maintains
conversation state. Each `receive_response()` call builds on previous
context. This differs from `query()` which creates independent,
stateless sessions.
:::

:::: {#7971eae4-3ff1-48d8-99ef-fecca7332163 .cell .code execution_count="7"}
``` python
visualize_conversation(messages)
```

::: {.output .display_data}

    
<style>
.conversation-timeline {
    font-family: ui-sans-serif, system-ui;
    max-width: 900px;
    margin: 1em 0;
}
.timeline-header {
    background: linear-gradient(135deg, #3b82f6, #9333ea);
    color: white;
    padding: 12px 16px;
    border-radius: 12px 12px 0 0;
    font-weight: 700;
    font-size: 14px;
}
.timeline-body {
    border: 1px solid #e5e7eb;
    border-top: none;
    border-radius: 0 0 12px 12px;
    padding: 12px;
    background: #fafafa;
}
.msg-block {
    margin: 8px 0;
    padding: 10px 12px;
    border-radius: 8px;
    background: white;
    border-left: 3px solid #e5e7eb;
}
.msg-block.system { border-left-color: #6b7280; }
.msg-block.assistant { border-left-color: #3b82f6; }
.msg-block.tool { border-left-color: #10b981; background: #f0fdf4; }
.msg-block.subagent { border-left-color: #9333ea; background: #faf5ff; }
.msg-block.result { border-left-color: #f59e0b; background: #fffbeb; }
.msg-label {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 4px;
}
.msg-content {
    font-size: 13px;
    color: #111;
}
.msg-content pre {
    background: #f3f4f6;
    padding: 8px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 12px;
}
.tool-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
}
.tool-badge {
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-family: monospace;
}
.stats-bar {
    display: flex;
    gap: 16px;
    padding: 10px 12px;
    background: #f9fafb;
    border-radius: 8px;
    font-size: 12px;
    color: #374151;
    margin-top: 8px;
}
.stat-item { display: flex; gap: 4px; }
.stat-label { color: #6b7280; }
</style>

    <div class="conversation-timeline">
        <div class="timeline-header">🤖 Agent Conversation Timeline • claude-opus-4-5</div>
        <div class="timeline-body">
            <div class="msg-block system"><div class="msg-label">⚙️ System</div><div class="msg-content">Initialized (9d494ab0...)</div></div><div class="msg-block tool"><div class="msg-label">🔧 Tools</div><div class="tool-list"><span class="tool-badge">Read: projects_claude.png</span></div></div><div class="msg-block assistant"><div class="msg-label">🤖 Assistant</div><div class="msg-content"><p>Let me search for the file in different locations:</p></div></div><div class="msg-block tool"><div class="msg-label">🔧 Tools</div><div class="tool-list"><span class="tool-badge">Glob</span></div></div><div class="msg-block assistant"><div class="msg-label">🤖 Assistant</div><div class="msg-content"><p>Found it. Let me read the image:</p></div></div><div class="msg-block tool"><div class="msg-label">🔧 Tools</div><div class="tool-list"><span class="tool-badge">Read: projects_claude.png</span></div></div><div class="msg-block assistant"><div class="msg-label">🤖 Assistant</div><div class="msg-content"><h2>Analysis of the Chart: Types of Projects in Claude.ai and Claude Code</h2>
<p>This is a <strong>dumbbell chart</strong> (also called a connected dot plot) that compares the prevalence of different project types between two Anthropic products: <strong>Claude.ai</strong> (blue dots) and <strong>Claude Code</strong> (orange dots).</p>
<h3>Key Findings</h3>
<h4>1. <strong>Personal Projects Lead Both Platforms</strong></h4>
<ul>
<li><strong>Claude Code</strong>: 36.0%</li>
<li><strong>Claude.ai</strong>: 30.2%</li>
<li>This is the most common use case for both platforms, with Claude Code having a slight edge (~6% higher).</li>
</ul>
<h4>2. <strong>Startup Work Shows the Largest Gap</strong></h4>
<ul>
<li><strong>Claude Code</strong>: 32.9%</li>
<li><strong>Claude.ai</strong>: 13.1%</li>
<li>This represents the <strong>biggest difference</strong> between the two platforms (~20% gap), indicating Claude Code is heavily favored for startup development work.</li>
</ul>
<h4>3. <strong>Enterprise Work is Relatively Balanced</strong></h4>
<ul>
<li><strong>Claude.ai</strong>: 25.9%</li>
<li><strong>Claude Code</strong>: 23.8%</li>
<li>Both platforms see similar usage for enterprise work, with Claude.ai slightly ahead (~2% difference).</li>
</ul>
<h4>4. <strong>Learning &amp; Academic Use Favors Claude.ai</strong></h4>
<ul>
<li><strong>Tutorial or Learning</strong>: Claude.ai (12.2%) vs Claude Code (0.7%)</li>
<li><strong>Academic Research</strong>: Claude.ai (11.9%) vs Claude Code (2.2%)</li>
<li><strong>Coursework</strong>: Claude.ai (4.9%) vs Claude Code (0.4%)</li>
<li>These categories show Claude.ai is significantly more popular for educational purposes, likely due to its conversational interface being more accessible for learning.</li>
</ul>
<h4>5. <strong>Open Source Projects are Low for Both</strong></h4>
<ul>
<li><strong>Claude Code</strong>: 4.0%</li>
<li><strong>Claude.ai</strong>: 1.8%</li>
<li>Neither platform sees heavy use for open source contributions, though Claude Code is used slightly more.</li>
</ul>
<h3>Insights &amp; Interpretation</h3>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Implication</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claude Code dominates Startup Work</strong></td>
<td>Developers building products at startups prefer the code-focused interface for rapid development</td>
</tr>
<tr>
<td><strong>Claude.ai leads in educational contexts</strong></td>
<td>The conversational nature of Claude.ai makes it more approachable for learning, research, and coursework</td>
</tr>
<tr>
<td><strong>Personal Projects are universal</strong></td>
<td>Both platforms serve individual developers working on side projects equally well</td>
</tr>
<tr>
<td><strong>Enterprise usage is balanced</strong></td>
<td>Both products have found their place in professional enterprise environments</td>
</tr>
</tbody>
</table>
<h3>Summary</h3>
<p>The chart reveals clear <strong>product differentiation</strong>: <br />
- <strong>Claude Code</strong> is preferred for <strong>active software development</strong> (startups, personal coding projects, open source)<br />
- <strong>Claude.ai</strong> excels in <strong>knowledge work and learning</strong> (tutorials, academic research, coursework)</p>
<p>This aligns with the nature of each product—Claude Code is a development tool while Claude.ai is a general-purpose AI assistant with a broader conversational interface.</p></div></div><div class="msg-block result"><div class="msg-label">✅ Complete</div><div class="stats-bar"><span class="stat-item"><span class="stat-label">Turns:</span> 4</span> <span class="stat-item"><span class="stat-label">Tokens:</span> 887</span> <span class="stat-item"><span class="stat-label">Cost:</span> $0.07</span> <span class="stat-item"><span class="stat-label">Duration:</span> 27.6s</span></div></div><div class="msg-block system"><div class="msg-label">⚙️ System</div><div class="msg-content">Initialized (9d494ab0...)</div></div><div class="msg-block tool"><div class="msg-label">🔧 Tools</div><div class="tool-list"><span class="tool-badge">WebSearch: &quot;Claude Code developer adoption...&quot;</span><span class="tool-badge">WebSearch: &quot;Claude AI education academic r...&quot;</span><span class="tool-badge">WebSearch: &quot;Anthropic Claude Code vs Claud...&quot;</span><span class="tool-badge">WebSearch: &quot;AI coding assistants startup d...&quot;</span></div></div><div class="msg-block assistant"><div class="msg-label">🤖 Assistant</div><div class="msg-content"><h2>Validation &amp; Context for Chart Findings</h2>
<p>Based on my research, here's how recent news and data validate or provide context for the chart analysis:</p>
<hr />
<h3>1. ✅ <strong>Startup Dominance in Claude Code - VALIDATED</strong></h3>
<p>The chart showed Claude Code usage for Startup Work at <strong>32.9%</strong> vs only <strong>13.1%</strong> for Claude.ai—the largest gap in the data. Recent news strongly confirms this:</p>
<blockquote>
<p><strong>"Startups are the main early adopters of Claude Code, suggesting that smaller, agile businesses are leveraging this AI tool to gain a technological advantage."</strong> - <a href="https://blockchain.news/flashnews/startups-lead-claude-code-adoption-key-trends-for-crypto-project-development-in-2025">Blockchain News</a></p>
</blockquote>
<p><strong>YC Startups as Case Studies:</strong><br />
- <strong>HumanLayer (F24)</strong> - Built their entire platform with Claude Code<br />
- <strong>Ambral (W25)</strong> - Scaling AI-powered account management with sub-agent workflows<br />
- <strong>Vulcan Technologies (S25)</strong> - Using Claude Code for regulatory complexity</p>
<p>As noted by <a href="https://www.claude.com/blog/building-companies-with-claude-code">Anthropic's blog</a>: <em>"Founders can now ship products directly from the terminal, compressing development cycles from weeks to hours."</em></p>
<hr />
<h3>2. ✅ <strong>Educational Use Favors Claude.ai - VALIDATED</strong></h3>
<p>The chart showed Claude.ai leading significantly in:<br />
- Tutorial or Learning: <strong>12.2%</strong> (vs 0.7% for Claude Code)<br />
- Academic Research: <strong>11.9%</strong> (vs 2.2%)<br />
- Coursework: <strong>4.9%</strong> (vs 0.4%)</p>
<p>This aligns perfectly with Anthropic's dedicated education initiatives:</p>
<blockquote>
<p><strong>Anthropic launched "Claude for Education"</strong> with features like <strong>"Learning Mode"</strong> that uses Socratic questioning rather than giving direct answers. - <a href="https://venturebeat.com/ai/anthropic-flips-the-script-on-ai-in-education-claude-learning-mode-makes-students-do-the-thinking/">VentureBeat</a></p>
</blockquote>
<p><strong>Key Statistics from Anthropic's Education Report:</strong><br />
- <strong>39.3%</strong> of student conversations involve creating and improving educational content<br />
- <strong>33.5%</strong> involve getting technical explanations for academic assignments<br />
- <strong>57%</strong> of higher ed instructor chats involved developing curricula<br />
- <strong>13%</strong> were conducting academic research</p>
<p>Early adopters include <strong>Northeastern University</strong> (50,000+ students across 13 campuses), <strong>London School of Economics</strong>, and <strong>Champlain College</strong>. - <a href="https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude">Anthropic Education Report</a></p>
<hr />
<h3>3. ✅ <strong>Coding/Development Dominance - VALIDATED</strong></h3>
<p>The chart showed Personal Projects and Startup Work (both development-heavy) as top uses for Claude Code (<strong>36%</strong> and <strong>32.9%</strong>).</p>
<p>Anthropic's own research confirms:</p>
<blockquote>
<p><strong>"About 44% of API traffic involved coding, compared with 36% on Claude.ai."</strong> - <a href="https://www.anthropic.com/research/anthropic-economic-index-september-2025-report">Anthropic Economic Index</a></p>
<p><strong>"Software development remains Claude's most common use case, making up more than a third of activity globally."</strong> - <a href="https://www.eweek.com/news/anthropic-economic-index-claude-ai-usage/">eWeek</a></p>
</blockquote>
<hr />
<h3>4. ✅ <strong>Product Differentiation (Claude Code vs Claude.ai) - VALIDATED</strong></h3>
<p>The chart's overall pattern showing Claude Code for development and Claude.ai for knowledge work is confirmed by Fortune:</p>
<blockquote>
<p><strong>"ChatGPT is emerging increasingly as a personal or exploratory tool... while Claude is a more work-focused productivity tool, used heavily for coding, research, and business automation."</strong> - <a href="https://fortune.com/2025/09/15/openai-chatgpt-claude-anthropic-work-personal-use-new-data/">Fortune</a></p>
</blockquote>
<p><strong>Automation patterns differ by platform:</strong><br />
- <strong>77% of API tasks</strong> are automated (full task delegation)<br />
- <strong>~50% of Claude.ai tasks</strong> are automated (more collaborative)</p>
<hr />
<h3>5. 📊 <strong>Broader AI Coding Assistant Context</strong></h3>
<p>The chart's findings fit into the larger industry trend:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>2025 Data</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI-generated/assisted code</td>
<td><strong>41%</strong> of all code globally</td>
</tr>
<tr>
<td>Developers using AI coding assistants</td>
<td><strong>82%</strong> daily or weekly</td>
</tr>
<tr>
<td>Market size projection</td>
<td><strong>$30.1 billion by 2032</strong></td>
</tr>
<tr>
<td>Google's AI-assisted code</td>
<td><strong>25%</strong></td>
</tr>
</tbody>
</table>
<p>Source: <a href="https://www.secondtalent.com/resources/ai-coding-assistant-statistics/">AI Coding Assistant Statistics</a></p>
<hr />
<h3>6. ⚠️ <strong>Enterprise Work Balance - PARTIALLY EXPLAINED</strong></h3>
<p>The chart showed Enterprise Work relatively balanced (Claude.ai: 25.9%, Claude Code: 23.8%). This makes sense given:</p>
<ul>
<li><strong>70-75% of Anthropic's revenue</strong> comes from enterprise API consumption</li>
<li>Enterprises use both products depending on use case</li>
<li>Security features like <strong>FedRAMP High certification</strong> drive enterprise adoption of both platforms</li>
</ul>
<hr />
<h2>Summary</h2>
<p>The chart's findings are <strong>strongly validated</strong> by recent data:</p>
<table>
<thead>
<tr>
<th>Chart Finding</th>
<th>Validation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Startups prefer Claude Code (32.9% vs 13.1%)</td>
<td>✅ Confirmed by Anthropic &amp; YC case studies</td>
</tr>
<tr>
<td>Education favors Claude.ai (12.2% vs 0.7%)</td>
<td>✅ Confirmed by Anthropic Education Report</td>
</tr>
<tr>
<td>Personal projects lead both platforms</td>
<td>✅ Confirmed by usage statistics</td>
</tr>
<tr>
<td>Claude Code = development tool</td>
<td>✅ Confirmed (44% API traffic is coding)</td>
</tr>
<tr>
<td>Claude.ai = knowledge/learning tool</td>
<td>✅ Confirmed by education initiatives</td>
</tr>
</tbody>
</table>
<hr />
<h2>Sources</h2>
<ul>
<li><a href="https://www.claude.com/blog/building-companies-with-claude-code">How Three YC Startups Built Their Companies with Claude Code</a></li>
<li><a href="https://www.anthropic.com/startups">Anthropic Startups Program</a></li>
<li><a href="https://blockchain.news/flashnews/startups-lead-claude-code-adoption-key-trends-for-crypto-project-development-in-2025">Startups Lead Claude Code Adoption - Blockchain News</a></li>
<li><a href="https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude">Anthropic Education Report: How Educators Use Claude</a></li>
<li><a href="https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude">How University Students Use Claude</a></li>
<li><a href="https://www.anthropic.com/news/introducing-claude-for-education">Introducing Claude for Education</a></li>
<li><a href="https://www.eweek.com/news/anthropic-economic-index-claude-ai-usage/">Anthropic's AI Usage Study: Coding Still Dominates - eWeek</a></li>
<li><a href="https://www.anthropic.com/research/anthropic-economic-index-september-2025-report">Anthropic Economic Index September 2025 Report</a></li>
<li><a href="https://fortune.com/2025/09/15/openai-chatgpt-claude-anthropic-work-personal-use-new-data/">New Studies Show What People Really Use ChatGPT and Claude For - Fortune</a></li>
<li><a href="https://backlinko.com/claude-users">Claude Statistics 2025 - Backlinko</a></li>
<li><a href="https://www.secondtalent.com/resources/ai-coding-assistant-statistics/">AI Coding Assistant Statistics &amp; Trends 2025</a></li>
<li><a href="https://venturebeat.com/ai/anthropic-flips-the-script-on-ai-in-education-claude-learning-mode-makes-students-do-the-thinking/">Anthropic Flips the Script on AI in Education - VentureBeat</a></li>
<li><a href="https://keywordseverywhere.com/blog/anthropic-claude-stats/">55 Latest Anthropic Claude Stats - Keywords Everywhere</a></li>
</ul></div></div><div class="msg-block result"><div class="msg-label">✅ Complete</div><div class="stats-bar"><span class="stat-item"><span class="stat-label">Turns:</span> 5</span> <span class="stat-item"><span class="stat-label">Tokens:</span> 2,152</span> <span class="stat-item"><span class="stat-label">Cost:</span> $0.76</span> <span class="stat-item"><span class="stat-label">Duration:</span> 73.0s</span></div></div>
        </div>
    </div>
    
:::
::::

::: {#38256581 .cell .markdown}
## Building for Production

Jupyter notebooks are great for learning, but production systems need
reusable modules. We\'ve packaged the research agent into
`research_agent/agent.py` with a clean interface:

### Core functions:

- `print_activity()` - Shows what the agent is doing in real-time
  (imported from shared utilities)
- `get_activity_text()` - Extract activity text for custom handlers,
  such as logging or monitoring
- `send_query()` - Main entry point for research queries with built-in
  activity display

### Built-in best practices:

The module includes the `RESEARCH_SYSTEM_PROMPT` which ensures:

- Source URLs are always included as citations
- Citations are formatted as markdown links for clean rendering
- A \"Sources:\" section groups all references

### Display control:

The `send_query()` function has a `display_result` parameter (default:
`True`):

- `display_result=True` - Renders a styled HTML card in Jupyter
  notebooks
- `display_result=False` - Returns only the text result for programmatic
  use

This agent can now be used in any Python script!
:::

::: {#e220b5c7-463b-4171-b687-b1ec974958de .cell .markdown}
For independent questions where conversation context doesn\'t matter.

The module automatically handles:

- Activity display during execution
- Context reset for new conversations
- Styled HTML rendering of the final response
:::

::::: {#3c2ca449-7a36-4b67-af47-fdb68fb3e36b .cell .code execution_count="8"}
``` python
from research_agent.agent import send_query

# The module handles activity display, context reset, and result visualization internally
result = await send_query("What is the Claude Code SDK? Only do one websearch and be concise")
```

::: {.output .stream .stdout}
    🤖 Using: WebSearch()
    ✓ Tool completed
    🤖 Thinking...
:::

::: {.output .display_data}

<style>
.pretty-card {
    font-family: ui-sans-serif, system-ui;
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 14px 16px;
    margin: 10px 0;
    background: linear-gradient(#fff, #fff) padding-box,
                linear-gradient(135deg, #3b82f6, #9333ea) border-box;
    color: #111;
    box-shadow: 0 4px 12px rgba(0,0,0,.08);
}
.pretty-title {
    font-weight: 700;
    margin-bottom: 8px;
    font-size: 14px;
    color: #111;
}
.pretty-card pre,
.pretty-card code {
    background: #f3f4f6;
    color: #111;
    padding: 8px;
    border-radius: 8px;
    display: block;
    overflow-x: auto;
    font-size: 13px;
    white-space: pre-wrap;
}
.pretty-card img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
/* Tables: both pandas (.pretty-table) and markdown-rendered */
.pretty-card table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
    color: #111;
    margin: 0.5em 0;
}
.pretty-card th,
.pretty-card td {
    border: 1px solid #e5e7eb;
    padding: 6px 8px;
    text-align: left;
}
.pretty-card th {
    background: #f9fafb;
    font-weight: 600;
}
/* Markdown headings */
.pretty-card h1, .pretty-card h2, .pretty-card h3, .pretty-card h4 {
    margin: 0.5em 0 0.3em 0;
    color: #111;
}
.pretty-card h1 { font-size: 1.4em; }
.pretty-card h2 { font-size: 1.2em; }
.pretty-card h3 { font-size: 1.1em; }
/* Markdown lists and paragraphs */
.pretty-card ul, .pretty-card ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
.pretty-card p {
    margin: 0.5em 0;
}
.pretty-card hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1em 0;
}
</style>
<div class="pretty-card"><div class="pretty-title">Agent Response</div><h2>Claude Code SDK</h2>
<p>The <strong>Claude Code SDK</strong> (now renamed to <strong>Claude Agent SDK</strong>) is a toolkit from Anthropic that allows developers to build AI agents using the same infrastructure that powers Claude Code.</p>
<p><strong>Key capabilities:</strong><br />
- <strong>Context management</strong> - Automatic compaction to prevent running out of context<br />
- <strong>Rich tool ecosystem</strong> - File operations, code execution, web search, MCP extensibility<br />
- <strong>Fine-grained permissions</strong> - Control over agent capabilities<br />
- <strong>Production features</strong> - Error handling, session management, monitoring</p>
<p><strong>Available in:</strong><br />
- TypeScript (<code>@anthropic-ai/claude-code</code>)<br />
- Python (<code>pip install claude-code-sdk</code>)<br />
- Command line</p>
<p>It enables building agents for coding automation, customer support, personal assistants, and more—all using the same core systems that power Claude Code.</p>
<hr />
<p><strong>Sources:</strong><br />
- <a href="https://docs.anthropic.com/en/docs/claude-code/sdk">Agent SDK overview - Claude Docs</a><br />
- <a href="https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk">Building agents with the Claude Agent SDK</a><br />
- <a href="https://www.infoq.com/news/2025/06/claude-code-sdk/">Anthropic Releases Claude Code SDK - InfoQ</a></p></div>
:::
:::::

::: {#466155ec-9f54-49d4-83cb-00032b077147 .cell .markdown}
Now we test out a multi-turn conversation that reuses the same
conversation.

Multi-turn conversations work seamlessly---just pass
`continue_conversation=True`:
:::

::::: {#38ba1eda .cell .code execution_count="9"}
``` python
result1 = await send_query("What is Anthropic? Only do one websearch and be concise")
```

::: {.output .stream .stdout}
    🤖 Using: WebSearch()
    ✓ Tool completed
    🤖 Thinking...
:::

::: {.output .display_data}

<style>
.pretty-card {
    font-family: ui-sans-serif, system-ui;
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 14px 16px;
    margin: 10px 0;
    background: linear-gradient(#fff, #fff) padding-box,
                linear-gradient(135deg, #3b82f6, #9333ea) border-box;
    color: #111;
    box-shadow: 0 4px 12px rgba(0,0,0,.08);
}
.pretty-title {
    font-weight: 700;
    margin-bottom: 8px;
    font-size: 14px;
    color: #111;
}
.pretty-card pre,
.pretty-card code {
    background: #f3f4f6;
    color: #111;
    padding: 8px;
    border-radius: 8px;
    display: block;
    overflow-x: auto;
    font-size: 13px;
    white-space: pre-wrap;
}
.pretty-card img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
/* Tables: both pandas (.pretty-table) and markdown-rendered */
.pretty-card table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
    color: #111;
    margin: 0.5em 0;
}
.pretty-card th,
.pretty-card td {
    border: 1px solid #e5e7eb;
    padding: 6px 8px;
    text-align: left;
}
.pretty-card th {
    background: #f9fafb;
    font-weight: 600;
}
/* Markdown headings */
.pretty-card h1, .pretty-card h2, .pretty-card h3, .pretty-card h4 {
    margin: 0.5em 0 0.3em 0;
    color: #111;
}
.pretty-card h1 { font-size: 1.4em; }
.pretty-card h2 { font-size: 1.2em; }
.pretty-card h3 { font-size: 1.1em; }
/* Markdown lists and paragraphs */
.pretty-card ul, .pretty-card ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
.pretty-card p {
    margin: 0.5em 0;
}
.pretty-card hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1em 0;
}
</style>
<div class="pretty-card"><div class="pretty-title">Agent Response</div><p><strong>Anthropic</strong> is an American AI safety company founded in 2021 by former OpenAI executives, including siblings Dario and Daniela Amodei. The company builds Claude, a family of large language models, with a focus on creating reliable, interpretable, and safe AI systems. Anthropic is valued at approximately $183 billion and has received major investments from Amazon, Google, Microsoft, and NVIDIA. Its Claude Code product recently reached $1 billion in run-rate revenue.</p>
<p>Sources:<br />
- <a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a><br />
- <a href="https://www.anthropic.com/">Anthropic Homepage</a><br />
- <a href="https://www.voiceflow.com/blog/anthropic-ai">What's Anthropic AI? - Voiceflow</a></p></div>
:::
:::::

::::: {#36931a9e .cell .code execution_count="10"}
``` python
# Continue the conversation to dig deeper by setting continue_conversation=True
result2 = await send_query(
    "What are some of their products?",
    continue_conversation=True,
)
```

::: {.output .stream .stdout}
    🤖 Thinking...
:::

::: {.output .display_data}

<style>
.pretty-card {
    font-family: ui-sans-serif, system-ui;
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 14px 16px;
    margin: 10px 0;
    background: linear-gradient(#fff, #fff) padding-box,
                linear-gradient(135deg, #3b82f6, #9333ea) border-box;
    color: #111;
    box-shadow: 0 4px 12px rgba(0,0,0,.08);
}
.pretty-title {
    font-weight: 700;
    margin-bottom: 8px;
    font-size: 14px;
    color: #111;
}
.pretty-card pre,
.pretty-card code {
    background: #f3f4f6;
    color: #111;
    padding: 8px;
    border-radius: 8px;
    display: block;
    overflow-x: auto;
    font-size: 13px;
    white-space: pre-wrap;
}
.pretty-card img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
/* Tables: both pandas (.pretty-table) and markdown-rendered */
.pretty-card table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
    color: #111;
    margin: 0.5em 0;
}
.pretty-card th,
.pretty-card td {
    border: 1px solid #e5e7eb;
    padding: 6px 8px;
    text-align: left;
}
.pretty-card th {
    background: #f9fafb;
    font-weight: 600;
}
/* Markdown headings */
.pretty-card h1, .pretty-card h2, .pretty-card h3, .pretty-card h4 {
    margin: 0.5em 0 0.3em 0;
    color: #111;
}
.pretty-card h1 { font-size: 1.4em; }
.pretty-card h2 { font-size: 1.2em; }
.pretty-card h3 { font-size: 1.1em; }
/* Markdown lists and paragraphs */
.pretty-card ul, .pretty-card ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
.pretty-card p {
    margin: 0.5em 0;
}
.pretty-card hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1em 0;
}
</style>
<div class="pretty-card"><div class="pretty-title">Agent Response</div><p>Based on my previous search results, here are Anthropic's main products:</p>
<ol>
<li>
<p><strong>Claude</strong> - Their flagship AI assistant and family of large language models, which incorporates "Constitutional AI" for safety. Named after mathematician Claude Shannon.</p>
</li>
<li>
<p><strong>Claude Code</strong> - A developer tool that recently reached $1 billion in run-rate revenue just six months after public launch.</p>
</li>
<li>
<p><strong>Bun</strong> - A JavaScript runtime that Anthropic recently acquired to accelerate Claude Code's capabilities.</p>
</li>
</ol>
<p>Anthropic offers Claude through their website, API access for developers, and enterprise solutions.</p>
<p>Sources:<br />
- <a href="https://www.anthropic.com/">Anthropic Homepage</a><br />
- <a href="https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone">Anthropic acquires Bun as Claude Code reaches $1B milestone</a></p></div>
:::
:::::

::: {#5344587c .cell .markdown}
## Conclusion

### What You Built

In this cookbook, you built three progressively sophisticated research
agents:

- Stateless research agent - One-line queries for independent research
  tasks
- Stateful agent with memory - Multi-turn investigations that build on
  previous findings
- Production module - Reusable research functions for integration into
  applications

### Key Takeaways

**When to use stateless queries (query()):**

- Independent research questions
- Parallel processing of unrelated tasks
- Scenarios requiring fresh context each time

**When to use stateful agents (ClaudeSDKClient):**

- Multi-turn investigations building on previous findings
- Iterative refinement of research
- Complex analysis requiring sustained context

Research agents excel when information isn\'t self-contained and the
optimal workflow emerges during exploration---competitive analysis,
technical troubleshooting, literature reviews, and investigative
journalism all fit this pattern.

### Next Steps

This foundation in autonomous research prepares you for enterprise-grade
multi-agent systems. In the next notebook, you\'ll learn to:

Orchestrate specialized subagents under a coordinating agent Implement
governance through hooks and custom commands Adapt output styles for
different stakeholders (executives vs. technical teams)

Next:
[01_The_chief_of_staff_agent.ipynb](01_The_chief_of_staff_agent.ipynb) -
From single agents to multi-agent orchestration.
:::
