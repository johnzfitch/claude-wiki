# Change Breakdown: 2.1.42 vs 2.1.41

## High-level
- Most differences are minifier/symbol churn.
- Core anchor prompts and secure mode vocabulary are unchanged.
- A specific memory-curation instruction block present in 2.1.41 is not found in 2.1.42.
- One web-search example was reworded from template placeholders to explicit "current year" wording.

## Stable
- Anchor prompts present in both: 
  - You are Claude Code, Anthropic's official CLI for Claude.
  - You are Claude Code, Anthropic's official CLI for Claude, running within the Claude Agent SDK.
  - You are a Claude agent, built on Anthropic's Claude Agent SDK.
- Random name word lists unchanged (adjectives, nouns, verbs).
- Permission mode terms unchanged: default, acceptEdits, plan, bypassPermissions, dontAsk, untrusted, never.

## Confirmed textual changes
- Hidden prompt year example changed:
  - 2.1.41: "search for \"React documentation ${H}\", NOT \"React documentation ${H-1}\""
  - 2.1.42: "search for \"React documentation\" with the current year, NOT last year"

## Removed in 2.1.42 (not found by string scan)
- "## CRITICAL: Evidence Threshold (2+ Sessions Required)"
- "Always use AskUserQuestion before ANY changes"
- "Never ask questions via plain text output. Use the AskUserQuestion tool for ALL confirmations."
- "Only extract themes and patterns that appear in 2 or more sessions..."
- "...modified since the last /remember run"

## Still present in 2.1.42
- Permission denial guidance string: "Permission for this tool use was denied..."
- Suspicious Windows path pattern guardrail text remains present.
- Permission mode validation text remains present.

## Category diff counts (text.unique, 2.1.42 - 2.1.41)
- system_prompts: +17 / -17
- reminder_prompts: +31 / -29
- warning_prompts: +254 / -358
- hidden_prompts: +66 / -68
- security_mode_related: +70 / -70
