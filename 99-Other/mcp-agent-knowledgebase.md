# MCP Agent Persona & Knowledgebase — Engineering Reference

> Derived from binary analysis of Claude Code 2.1.59/2.1.70 JS payload.
> Covers all verified extension points for embedding agent personas and knowledgebases into MCP servers.

---

## 1. The Four Injection Channels

Claude Code builds its system prompt from multiple sources. An MCP server can touch **two of them directly**, and the other two are file-system-based extensions the MCP can register:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Claude Code System Prompt                        │
│                                                                      │
│  ┌──────────────────┐  ┌───────────────────┐  ┌──────────────────┐  │
│  │  Core Identity   │  │  MCP Instructions │  │  Skill Listings  │  │
│  │  (hardcoded)     │  │  ← CHANNEL 1      │  │  (auto-injected) │  │
│  └──────────────────┘  └───────────────────┘  └──────────────────┘  │
│                                                                      │
│  ┌──────────────────┐  ┌───────────────────┐                        │
│  │  Agent Persona   │  │  Invoked Skills   │                        │
│  │  ← CHANNEL 2     │  │  ← CHANNEL 3      │                        │
│  └──────────────────┘  └───────────────────┘                        │
│                                                                      │
│  CHANNEL 4: MCP Prompts (slash commands / getPrompt)                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Channel 1 — MCP Server `instructions` Field

### How it works

During the MCP `initialize` handshake, a server can return an `instructions` string in its response. Claude Code captures this and passes it to `hw1()` (called as `mcp_instructions` in the system prompt builder).

The exact system prompt section rendered (from decompiled source, line 1202):

```
# MCP Server Instructions
The following MCP servers have provided instructions for how to use their tools and resources:

## <server_name>
<instructions>
```

The section only appears when at least one connected server has a non-empty `instructions` field.

### Implementation (Python MCP SDK)

```python
from mcp.server import Server
from mcp.server.models import InitializationOptions

app = Server("raleys-grocery")

# This string becomes Channel 1 — injected into every system prompt
INSTRUCTIONS = """
You are connected to the Raley's Grocery Shopping Assistant.

## Your Role
You help plan grocery shopping optimized for:
- Type 1 diabetes management (low glycemic, carb-aware)
- Seasonal and local California produce
- Budget-conscious fresh ingredients
- Delicious, satisfying meals (not just "healthy" food)

## How to Use These Tools
- `search_products`: Search the Raley's product catalog by name, category, or dietary tag
- `get_seasonal_produce`: Returns what's in season at Raley's for the current week and region
- `build_cart`: Add items to a cart with quantity and unit
- `get_nutrition`: Fetch detailed nutrition facts for any product
- `get_recipes`: Query the embedded diabetes-friendly recipe knowledgebase
- `estimate_cost`: Get current prices and total for a cart

## Dietary Guidelines Active
The knowledgebase is pre-filtered for Type 1 diabetes suitability.
Always mention glycemic index, carb count, and insulin considerations when relevant.
"""

@app.initialize()
async def initialize():
    return InitializationOptions(
        server_name="raleys-grocery",
        server_version="1.0.0",
        instructions=INSTRUCTIONS,   # <-- Channel 1
        capabilities=app.get_capabilities(...)
    )
```

### Key properties
- Injected **at system prompt build time**, before the first user message
- **Always active** for the session — no invocation needed
- **Ideal for**: tool usage guidance, persona framing, dietary/domain context
- Section is re-evaluated each turn (marked `"MCP servers connect/disconnect between turns"`)

---

## Channel 2 — Agent Definition File (`.claude/agents/<name>.md`)

### How it works

Claude Code loads markdown files from `.claude/agents/` as agent definitions. Each file has YAML frontmatter with `name`, `description` (= `whenToUse`), `tools`, `model`, `memory`. The agent's `systemPrompt` is the markdown body after the frontmatter.

The agent is listed in the model's context as:
```
Available custom agents configured:
- raleys-shopper: <whenToUse text>
```

When the model decides to spawn it (or you invoke `/agent raleys-shopper`), it runs as an isolated sub-agent with its own system prompt.

### File format

```markdown
---
name: raleys-shopper
description: >
  Use this agent when the user asks to plan a grocery trip, create a
  shopping list, find diabetes-friendly recipes, check seasonal produce,
  or estimate grocery costs. Invoke proactively whenever shopping or
  meal planning is mentioned.
model: claude-sonnet-4-6
tools:
  - mcp__raleys-grocery__search_products
  - mcp__raleys-grocery__get_seasonal_produce
  - mcp__raleys-grocery__build_cart
  - mcp__raleys-grocery__get_nutrition
  - mcp__raleys-grocery__get_recipes
  - mcp__raleys-grocery__estimate_cost
  - Read
memory: >
  Update your agent memory as you discover:
  - User's preferred products and brands at Raley's
  - Insulin-to-carb ratios and carb targets this user follows
  - Recipes that worked well (note name + glycemic rating)
  - Seasonal availability patterns in user's area
  - Budget targets and spending patterns
---

You are the Raley's Grocery Shopping Assistant — a specialist in
Type 1 diabetes-friendly grocery planning with deep knowledge of
Raley's product catalog, California seasonal produce, and practical
nutrition for blood sugar management.

## Diabetes Nutrition Principles
- Prioritize low glycemic index foods (GI < 55 preferred)
- Always report carbohydrate counts per serving
- Flag high-glycemic items and suggest swaps
- Account for fiber when calculating net carbs
- Highlight foods rich in chromium, magnesium, omega-3s (improve
  insulin sensitivity)

## Shopping Philosophy
Fresh > packaged. Seasonal = cheaper + more nutritious.
A beautiful meal people actually want to eat is better than
a technically optimal one no one finishes.

## Response Format
For shopping lists:
1. Group by store section (produce, proteins, dairy, pantry)
2. Include estimated cost per item
3. Flag any item with GI > 70 with [HIGH-GI — consider swap]
4. Suggest seasonal alternatives when available

For recipes:
- Lead with carb count and GI rating
- Include prep time, difficulty, cost estimate
- Note insulin timing recommendations when relevant
```

### Key properties
- Runs as an **isolated forked sub-agent** (full tool access, own context)
- The `memory` field triggers persistent memory instructions across sessions
- `whenToUse` / `description` is what the orchestrating Claude reads to decide when to invoke
- Tools list restricts what the sub-agent can call (security boundary)
- File can be placed at `.claude/agents/` (project-scope) or `~/.claude/agents/` (user-scope)

---

## Channel 3 — SKILL.md Inline Injection

### How it works

A `SKILL.md` in `.claude/skills/<name>/SKILL.md` is invoked as a slash command or via the `Skill` tool. When invoked, its content is injected as a system-level message into the **current conversation** (not a sub-agent). The model treats it as authoritative instructions that persist for the session.

This is the right channel for **knowledgebase lookup guides** — injecting reference material and search instructions into the conversation.

### File format

```markdown
---
name: Diabetes Grocery Guide
description: >
  Load the Type 1 diabetes grocery planning guide. Use this when
  helping plan meals, interpret nutrition labels, or shop for
  blood-sugar-friendly ingredients.
allowed-tools:
  - mcp__raleys-grocery__search_products
  - mcp__raleys-grocery__get_nutrition
  - mcp__raleys-grocery__get_recipes
  - mcp__raleys-grocery__get_seasonal_produce
when_to_use: >
  Invoke automatically whenever the user asks about diabetes-friendly
  food, meal planning, grocery shopping, blood sugar, or carb counting.
---

# Type 1 Diabetes Grocery Planning Guide

## Knowledgebase Sources Available
The following books are indexed in `get_recipes` and searchable by topic:

| Source | Query Tag | Focus |
|--------|-----------|-------|
| "Think Like a Pancreas" (Scheiner) | `#tlap` | Carb counting, insulin math |
| "Bright Spots & Landmines" (Close) | `#bslm` | Practical low-carb eating |
| "The Diabetes Cookbook" (Dunn-Lewis) | `#cookbook` | Full recipes with GI ratings |
| "Mastering Diabetes" (Khambatta) | `#master` | Whole food plant-based approach |
| "The Complete Diabetes Cookbook" (ATK) | `#atk` | Test-kitchen recipes |

## GI Reference (memorize these)

**Low GI (< 55) — Prefer these:**
- Leafy greens, broccoli, cauliflower, zucchini (GI ~15)
- Berries: strawberries (GI 40), blueberries (GI 53)
- Legumes: lentils (GI 32), chickpeas (GI 28), black beans (GI 30)
- Whole grains: barley (GI 28), bulgur (GI 48)
- Dairy: Greek yogurt (GI 11), milk (GI 39)
- Proteins: all meats, fish, eggs (GI ~0)
- Healthy fats: avocado, olive oil, nuts (GI ~0)

**Medium GI (55–69) — Use in portions:**
- Brown rice (GI 68), whole wheat bread (GI 69), oats (GI 58)
- Corn (GI 52 fresh, higher processed), banana (GI 51–62)
- Sweet potato (GI 63)

**High GI (> 70) — Flag and offer swaps:**
- White rice (GI 73), white bread (GI 75), potatoes (GI 78)
- Watermelon (GI 72), pineapple (GI 66–74)
- Most breakfast cereals (GI 70–90)

## Seasonal California Produce Calendar (Raley's sourcing)
Always call `get_seasonal_produce` for current week — this is general guidance only.

- **Spring (Mar–May)**: asparagus, artichokes, peas, strawberries, cherries
- **Summer (Jun–Aug)**: stone fruits, tomatoes, corn, zucchini, peppers, basil
- **Fall (Sep–Nov)**: winter squash, apples, pears, grapes, Brussels sprouts
- **Winter (Dec–Feb)**: citrus, kale, root vegetables, pomegranates

## Carb Budget Planning
Typical T1D targets (always defer to user's own ratio):
- Per meal: 30–60g carbs (varies widely by individual)
- Per snack: 15–20g carbs
- Net carbs = total carbs − dietary fiber (−50% for sugar alcohols)

## How to Use the Recipe Knowledgebase
Call `get_recipes` with:
- `query`: plain language (e.g., "high-protein breakfast under 20g carbs")
- `tags`: filter by source book (e.g., `["#cookbook", "#atk"]`)
- `max_gi`: glycemic index ceiling (default 55)
- `max_carbs_per_serving`: carb limit per serving in grams
- `season`: "spring" | "summer" | "fall" | "winter" | "current"
- `budget`: "low" | "medium" | "any"
```

### Key properties
- **Auto-allow** if no `model` override + no `context: fork` (zero friction to invoke)
- The `when_to_use` field is listed in the model's `skill_listing` attachment at session start
- Injected content **persists** for the entire session after first invocation
- File watcher picks up edits instantly — no restart needed

---

## Channel 4 — MCP Prompts (Slash Commands)

### How it works

An MCP server can expose a `prompts/list` capability. Each prompt becomes a slash command: `/mcp__<server>__<prompt_name>`. Invoking it calls `prompts/get` on the server which returns structured message content injected into the conversation.

This is the right channel for **on-demand knowledgebase queries** — the user types `/mcp__raleys-grocery__weekly_plan` and the server returns a pre-built context payload.

### Implementation

```python
from mcp.server import Server
from mcp.types import GetPromptResult, PromptMessage, TextContent

@app.list_prompts()
async def list_prompts():
    return [
        {
            "name": "weekly_plan",
            "description": "Generate a diabetes-friendly weekly meal and shopping plan",
            "arguments": [
                {"name": "budget", "description": "Weekly budget in dollars", "required": False},
                {"name": "servings", "description": "Number of people", "required": False},
            ]
        },
        {
            "name": "recipe_lookup",
            "description": "Look up a specific recipe from the diabetes cookbook knowledgebase",
            "arguments": [
                {"name": "query", "description": "Recipe name or description", "required": True},
            ]
        }
    ]

@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> GetPromptResult:
    if name == "weekly_plan":
        budget = arguments.get("budget", "100")
        servings = arguments.get("servings", "2")
        content = await build_weekly_plan_context(budget, servings)
        return GetPromptResult(messages=[
            PromptMessage(role="user", content=TextContent(
                type="text",
                text=content
            ))
        ])
```

### Key properties
- Invoked on-demand, not persistent
- Returns structured `messages` array injected into conversation
- Arguments passed via `/mcp__server__prompt_name arg1 arg2`
- Exposed as `type: "prompt"` in the merged skills view — appears in `/` menu

---

## Extension Point Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│               Raley's Grocery Assistant — Extension Map                  │
│                                                                          │
│  Channel 1: MCP instructions field (initialize response)                 │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ • Tool usage guide (how to call each tool)                       │    │
│  │ • Persona framing ("You are connected to...")                    │    │
│  │ • Active dietary mode declaration                                │    │
│  │ ALWAYS ON — injected every turn, no user action needed           │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  Channel 2: .claude/agents/raleys-shopper.md                            │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ • Full agent persona with deep T1D nutrition knowledge           │    │
│  │ • Tool restrictions (only grocery MCP tools)                     │    │
│  │ • Memory instructions for learning user preferences              │    │
│  │ • whenToUse triggers auto-invocation                            │    │
│  │ FORKED — runs as isolated sub-agent, returns clean result        │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  Channel 3: .claude/skills/diabetes-grocery-guide/SKILL.md             │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ • GI reference tables                                            │    │
│  │ • Knowledgebase source index (which books → which query tags)    │    │
│  │ • Seasonal produce calendar                                      │    │
│  │ • Carb budget planning formulas                                  │    │
│  │ • Recipe query API guide                                         │    │
│  │ INLINE — injected into current convo, persists for session       │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  Channel 4: MCP prompts/list                                            │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ • /mcp__raleys-grocery__weekly_plan [budget] [servings]          │    │
│  │ • /mcp__raleys-grocery__recipe_lookup [query]                    │    │
│  │ • /mcp__raleys-grocery__seasonal_now                             │    │
│  │ ON-DEMAND — user-triggered slash commands                        │    │
│  └─────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## MCP Server File Layout (Recommended)

```
raleys-grocery-mcp/
├── server.py                    # Main MCP server (Channel 1: instructions)
├── tools/
│   ├── catalog.py               # search_products, get_nutrition
│   ├── seasonal.py              # get_seasonal_produce
│   ├── cart.py                  # build_cart, estimate_cost
│   └── recipes.py               # get_recipes → queries knowledgebase
├── knowledgebase/
│   ├── books/
│   │   ├── think-like-a-pancreas.md
│   │   ├── bright-spots-landmines.md
│   │   ├── diabetes-cookbook.md
│   │   ├── mastering-diabetes.md
│   │   └── atk-diabetes-cookbook.md
│   ├── gi-index.json            # GI values database
│   └── recipes/                 # Extracted/adapted recipes with metadata
│       ├── breakfast/
│       ├── lunch/
│       ├── dinner/
│       └── snacks/
└── prompts/
    ├── weekly_plan.py           # Channel 4: builds weekly meal plan context
    └── recipe_lookup.py         # Channel 4: queries knowledgebase
```

```
# Claude Code project integration
project-root/
├── .mcp.json                    # Register raleys-grocery server
├── .claude/
│   ├── agents/
│   │   └── raleys-shopper.md   # Channel 2: agent persona
│   └── skills/
│       └── diabetes-grocery-guide/
│           └── SKILL.md        # Channel 3: knowledgebase reference
```

---

## .mcp.json Registration

```json
{
  "mcpServers": {
    "raleys-grocery": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "--directory", "/path/to/raleys-grocery-mcp", "python", "server.py"],
      "env": {
        "RALEYS_API_KEY": "${RALEYS_API_KEY}",
        "KNOWLEDGEBASE_PATH": "/path/to/raleys-grocery-mcp/knowledgebase"
      }
    }
  }
}
```

---

## Priority / Precedence Rules

| Source | Priority | Overridable By |
|--------|----------|----------------|
| MCP instructions (Channel 1) | Always-on | Nothing — injected verbatim |
| Project agents (`.claude/agents/`) | Medium | User-scope agents (`~/.claude/agents/`) |
| User agents (`~/.claude/agents/`) | High | Policy agents (`~/.config/anthropic/`) |
| Project skills (`.claude/skills/`) | Medium | User-scope skills |
| Bundled skills (binary) | Lowest | All other sources |

When two skills/agents share the same name, **later-loaded source wins**.

---

## What Goes Where — Decision Guide

| Content Type | Best Channel | Why |
|--------------|-------------|-----|
| Tool usage guide ("how to call search_products") | Channel 1 (MCP instructions) | Always present, no user action |
| Persona framing ("You are a T1D nutrition expert") | Channel 1 + Channel 2 | Ch1 for every turn; Ch2 for deep sub-agent work |
| GI reference tables | Channel 3 (SKILL.md) | Large content, inject when needed |
| Book knowledgebase index | Channel 3 (SKILL.md) | Session-persistent reference |
| Seasonal produce calendar (static) | Channel 3 (SKILL.md) | Semi-static, session reference |
| Weekly meal plan builder | Channel 4 (MCP prompt) | User-triggered, dynamic server output |
| Recipe lookup with live query | Channel 4 (MCP prompt) | Server-side search, structured result |
| User preference memory | Channel 2 (agent `memory`) | Persists across sessions |
| Carb budget / insulin ratio | Channel 2 (agent) or Channel 3 | Deep session context |

---

## Key Binary-Verified Facts

1. **MCP `instructions` is re-evaluated each turn** — the `mcp_instructions` system prompt section is tagged `"MCP servers connect/disconnect between turns"` in the lazy evaluator, meaning it's rebuilt dynamically. Keep instructions stateless or they may flicker.

2. **Skills auto-allow with no frontmatter restrictions** — a SKILL.md with no `allowed-tools`, no `model`, no `context: fork`, no `paths`, no `hooks` is classified "empty context" and bypasses the permission prompt entirely. Maximally frictionless.

3. **Agent `whenToUse` is shown to the orchestrating Claude** — the exact text appears in the `skill_listing` / `agent_listing` attachment at session start. Write it as a trigger description, not a capability description: "Use this when..." not "This agent can..."

4. **Forked agents get full tool isolation** — the `kN()` sub-agent runner resolves tools via `od(agentDef, tools, isAsync)` and only exposes what's in `agentDef.tools`. The grocery agent cannot accidentally call Edit or Bash.

5. **MCP prompts become slash commands automatically** — `duH()` maps every `prompts/list` entry to a `type: "prompt"` slash command prefixed `mcp__<server>__<name>`. No registration needed beyond implementing `prompts/list`.

6. **Plugin `agents/` directory** — plugins can bundle agent `.md` files in a `agents/` subdirectory. The plugin loader checks for this path automatically (same as `commands/` and `skills/`). This means the MCP server can be packaged as a Claude Code plugin that ships its own agents and skills.
