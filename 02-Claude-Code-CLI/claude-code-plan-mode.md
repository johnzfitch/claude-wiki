# Claude Code Plan Mode Configuration

Comprehensive guide to plan mode behavior, environment variables, and agent configuration.

## Two Plan Mode Variants

### V2 Phase-Based Mode (Default)
Structured 3-phase workflow with **mandatory parallel subagents**.

**Phases:**
1. **Phase 1: Initial Understanding** - Parallel exploration with Explore agents
2. **Phase 2: Design** - Architecture planning with Plan agents
3. **Phase 3: Review** - Main agent asks clarifying questions

**Characteristics:**
- Always spawns subagents (minimum 1 per phase)
- Structured workflow
- Less interactive upfront
- Gather everything → design → review

### Interview/Iterative Mode
Conversational plan mode with **optional subagents**.

**Workflow:**
- Iterative loop: Explore code → Update plan file → Ask user → Repeat
- Subagents are available but not mandatory
- More interactive and conversational
- Pair-planning approach

**Enable with:**
```bash
export CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE=true
```

---

## Environment Variables

### CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE

**Purpose:** Switch between V2 phase-based mode and interview mode.

**Accepted Values:**

Truthy (enable interview mode):
- `1`
- `true`
- `yes`
- `on`

Falsy (disable, use V2 phase-based):
- `0`
- `false`
- `no`
- `off`

**Notes:**
- Case-insensitive
- Values are trimmed
- Falls back to tengu flag `tengu_plan_mode_interview_phase` if unset (default: false)

**Implementation:**
```javascript
function tH(H) {  // isTruthy
  if (!H) return false;
  if (typeof H === "boolean") return H;
  let $ = H.toLowerCase().trim();
  return ["1", "true", "yes", "on"].includes($);
}

function CK(H) {  // isFalsy
  if (H === void 0) return false;
  if (typeof H === "boolean") return !H;
  if (!H) return false;
  let $ = H.toLowerCase().trim();
  return ["0", "false", "no", "off"].includes($);
}
```

---

### CLAUDE_CODE_PLAN_V2_AGENT_COUNT

**Purpose:** Number of Plan agents spawned in Phase 2.

**Validation:** Must be integer 1-10 (0 is rejected).

**Defaults:**
- `1` - standard models
- `3` - if model is "max" AND config is "default_claude_max_20x"
- `3` - if model is "enterprise" or "team"

**Implementation:**
```javascript
function a_D() {
  if (process.env.CLAUDE_CODE_PLAN_V2_AGENT_COUNT) {
    let A = parseInt(process.env.CLAUDE_CODE_PLAN_V2_AGENT_COUNT, 10);
    if (!isNaN(A) && A > 0 && A <= 10) return A;
  }
  let H = C9(), $ = Qb();
  if (H === "max" && $ === "default_claude_max_20x") return 3;
  if (H === "enterprise" || H === "team") return 3;
  return 1;
}
```

**Setting to 0:** Falls back to defaults (does NOT disable subagents).

---

### CLAUDE_CODE_PLAN_V2_EXPLORE_AGENT_COUNT

**Purpose:** Number of Explore agents spawned in Phase 1.

**Validation:** Must be integer 1-10 (0 is rejected).

**Default:** `3`

**Implementation:**
```javascript
function t_D() {
  if (process.env.CLAUDE_CODE_PLAN_V2_EXPLORE_AGENT_COUNT) {
    let H = parseInt(process.env.CLAUDE_CODE_PLAN_V2_EXPLORE_AGENT_COUNT, 10);
    if (!isNaN(H) && H > 0 && H <= 10) return H;
  }
  return 3;
}
```

**Setting to 0:** Falls back to 3 (does NOT disable subagents).

---

## Agent Configuration by Phase

### Phase 1: Initial Understanding

| Property | Value |
|----------|-------|
| **Agent Type** | `Explore` (zp.agentType) |
| **Default Count** | 3 |
| **Env Override** | `CLAUDE_CODE_PLAN_V2_EXPLORE_AGENT_COUNT` |
| **Valid Range** | 1-10 |
| **Model** | Haiku |
| **Mode** | READ-ONLY |

**Disallowed Tools:**
- Edit
- Write
- NotebookEdit
- EnterPlanMode
- ExitPlanMode

**Allowed Tools:**
- Read, Grep, Glob, Bash
- Agent (nested subagents)
- AskUserQuestion
- TaskCreate/TaskUpdate/TaskGet
- All MCP tools

**Template Variables:**
- `${A}` = explore agent count (3 default)
- `${zp.agentType}` = "Explore"

---

### Phase 2: Design

| Property | Value |
|----------|-------|
| **Agent Type** | `Plan` (UG$.agentType) |
| **Default Count** | 1 (or 3 for max/enterprise/team) |
| **Env Override** | `CLAUDE_CODE_PLAN_V2_AGENT_COUNT` |
| **Valid Range** | 1-10 |
| **Model** | Inherit from parent |
| **Mode** | READ-ONLY |

**Tool Restrictions:** Same as Phase 1 (references zp.tools)

**Template Variables:**
- `${$}` = plan agent count (1 or 3 default)
- `${UG$.agentType}` = "Plan"

---

### Phase 3: Review

| Property | Value |
|----------|-------|
| **Agent Type** | Main agent (no subagent) |
| **Tool Used** | `AskUserQuestion` (g7) |
| **Purpose** | Clarify remaining questions |

**Template Variable:**
- `${g7}` = AskUserQuestion tool

---

## Plan File Tools

Both modes use these tools for plan file management:

- `${Oj.name}` = Edit tool (for editing existing plan)
- `${fj.name}` = Write tool (for creating new plan)
- `${CY.name}` = Tool to request plan approval

---

## Interview Mode Details

When `CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE=true`:

### Workflow
```
Repeat until plan is complete:
1. Explore - Use Read/Grep/Glob/Bash or optionally Explore agents
2. Update plan file - Capture findings incrementally
3. Ask user - Use AskUserQuestion when needed
```

### Key Differences from V2
- **No mandatory subagents** - direct tool use preferred for simple queries
- **Explore agents optional** - "You can use the Explore agent type... though for straightforward queries direct tools are simpler"
- **Incremental planning** - update plan file as you go
- **More user interaction** - ask questions throughout, not just at the end

### Turn Endings
Each turn must end with either:
- `AskUserQuestion` - to gather more information
- Plan approval tool - when plan is ready

### Plan File Structure
- **Context section** - why the change is needed
- **Recommended approach** - single approach, not all alternatives
- **Critical files** - paths to files to be modified
- **Reusable code** - existing functions/utilities with paths
- **Verification** - how to test changes

---

## Token Optimization Configuration

**Minimal subagent spawning:**
```bash
export CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE=true  # Enable interview mode
export CLAUDE_CODE_PLAN_V2_AGENT_COUNT=1           # Minimum Plan agents if spawned
export CLAUDE_CODE_PLAN_V2_EXPLORE_AGENT_COUNT=1   # Minimum Explore agents if spawned
```

**Effect:**
- Interview mode makes subagents optional
- If subagents ARE spawned, only 1 will be created
- Most work happens in main agent context
- Significant token savings

---

## Function Reference

**Plan mode entry point:** `pe6()`
```javascript
// Selects between Interview and V2 modes
if (OP()) return Ue6(H);  // Interview mode
// else: V2 phase-based mode
```

**Mode selector:** `OP()`
```javascript
function OP() {
  let H = process.env.CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE;
  if (tH(H)) return true;   // Interview mode
  if (CK(H)) return false;  // V2 mode
  return IA("tengu_plan_mode_interview_phase", false);  // Default: V2
}
```

**Interview mode template:** `Ue6(H)`
- Returns iterative workflow instructions
- No mandatory subagent spawning
- Emphasis on incremental planning

**V2 mode template:** (default pe6 path)
- Returns 3-phase structured workflow
- Mandatory parallel subagent spawning
- Explore → Plan → Review phases

---

## Summary Table

| Aspect | Interview Mode | V2 Phase-Based |
|--------|---------------|----------------|
| **Trigger** | `CLAUDE_CODE_PLAN_MODE_INTERVIEW_PHASE=true` | Default |
| **Subagents** | Optional | Mandatory |
| **Default Explore Count** | N/A (optional) | 3 |
| **Default Plan Count** | N/A (optional) | 1-3 |
| **Workflow** | Iterative loop | 3 structured phases |
| **User Interaction** | Throughout | Primarily at end |
| **Plan File Updates** | Incremental | After phase completion |
| **Token Usage** | Lower (fewer subagents) | Higher (parallel agents) |

---

## Validated in Binary Version

- **2.1.75** - All values confirmed via cli.js extraction
- Functions: `OP()`, `tH()`, `CK()`, `a_D()`, `t_D()`, `pe6()`, `Ue6()`
