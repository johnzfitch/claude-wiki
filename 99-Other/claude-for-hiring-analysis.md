# claude-for-hiring Model Analysis

**Binary Version:** 2.1.74
**Discovery Date:** 2026-03-11
**Updated:** 2026-03-13 (corrections from deep analysis)
**Status:** Internal Anthropic project — repo detection only

## Summary

`claude-for-hiring` is an **internal Anthropic GitHub repository** listed in the `SN1`
detection array alongside 18 other internal repos. Its only effect in the binary: when
Claude Code runs inside this repo, git commits get the real model name in `Co-Authored-By`
instead of the hardcoded fallback "Claude Opus 4.6".

It is NOT a model, NOT a special routing path, NOT a telemetry fork.

## Evidence

### 1. `SN1` — Complete Internal Repo Whitelist (L1089)

```javascript
SN1 = [
  "github.com:anthropics/claude-cli-internal",  "github.com/anthropics/claude-cli-internal",
  "github.com:anthropics/anthropic",            "github.com/anthropics/anthropic",
  "github.com:anthropics/apps",                 "github.com/anthropics/apps",
  "github.com:anthropics/casino",               "github.com/anthropics/casino",
  "github.com:anthropics/dbt",                  "github.com/anthropics/dbt",
  "github.com:anthropics/dotfiles",             "github.com/anthropics/dotfiles",
  "github.com:anthropics/terraform-config",     "github.com/anthropics/terraform-config",
  "github.com:anthropics/hex-export",           "github.com/anthropics/hex-export",
  "github.com:anthropics/feedback-v2",          "github.com/anthropics/feedback-v2",
  "github.com:anthropics/labs",                 "github.com/anthropics/labs",
  "github.com:anthropics/argo-rollouts",        "github.com/anthropics/argo-rollouts",
  "github.com:anthropics/starling-configs",     "github.com/anthropics/starling-configs",
  "github.com:anthropics/ts-tools",             "github.com/anthropics/ts-tools",
  "github.com:anthropics/ts-capsules",          "github.com/anthropics/ts-capsules",
  "github.com:anthropics/feldspar-testing",     "github.com/anthropics/feldspar-testing",
  "github.com:anthropics/trellis",              "github.com/anthropics/trellis",
  "github.com:anthropics/claude-for-hiring",    "github.com/anthropics/claude-for-hiring",
  "github.com:anthropics/forge-web",            "github.com/anthropics/forge-web",
  "github.com:anthropics/infra-manifests",      "github.com/anthropics/infra-manifests",
]
```

### 2. `OBD` — Async Detection (memoized, L1089)

```javascript
OBD = _x(async () => {
  if (VpH !== null) return VpH === "internal";
  let H = cI$();           // get CWD
  let $ = await AM$(H);    // get git remote URL
  if (!$) return VpH = "none", false;
  let A = SN1.some((L) => $.includes(L));
  return VpH = A ? "internal" : "external", A;
});
```

`_x()` is a once/memoize wrapper. Result cached in `VpH`: `"internal"` | `"external"` | `"none"`.

### 3. `PBD` — Synchronous Cache Reader

```javascript
function PBD() { return VpH === "internal" }
```

### 4. The Only Call Site — Commit Attribution (L4024)

`PBD()` is called **exactly once** in the binary (corrects prior claim of "2 times"):

```javascript
let A = PBD() || $ ? eUA(H) : "Claude Opus 4.6"
let D = `Co-Authored-By: ${A} <noreply@anthropic.com>`
```

- `$` = `JnH(H) !== null` (some session/auth check)
- If internal OR authenticated: `eUA(H)` = real dynamic model name
- Otherwise: hardcoded `"Claude Opus 4.6"`

The feature gate is: **git commit Co-Authored-By footer only**. Nothing else.

## What It's NOT (confirmed via exhaustive search)

- NOT a model ID (does not appear in model routing or API call paths)
- NOT referenced in telemetry forks
- NOT in any special tooling or skill paths
- NOT related to `claude-code-feedback` (separate model ID, separate purpose)

## Corrections to Original Analysis

| Claim | Correct status |
|-------|---------------|
| `PBD()` called 2 times | Called **1 time** only |
| `CLAUDE_SONNET_4_6` is a runtime env var | **Wrong** — it's `Model.CLAUDE_SONNET_4_6` Java enum in embedded SDK docs |
| Feature gating for telemetry/debugging | **Wrong** — gating is commit attribution only |
| `claude-for-hiring` in model IDs | **Wrong** — it's in repo detection array, not model IDs |

## Hypothesis: Recruitment Tool

Given the name alongside:
- `anthropics/feedback-v2` (user feedback system)
- `anthropics/forge-web` (internal web UI)
- `anthropics/casino` (unknown internal tool)
- `anthropics/trellis` (internal tool)

`claude-for-hiring` is likely a recruitment workflow application built using Claude Code
internally. The repo detection just ensures Anthropic engineers get proper model attribution
in commits when working on it. There is no special model or behavior for this repo beyond that.
