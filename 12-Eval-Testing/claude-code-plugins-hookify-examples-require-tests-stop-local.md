---
title: "Require Tests Stop.Local"
source_url: "https://github.com/anthropics/claude-code/blob/main/plugins/hookify/examples/require-tests-stop.local.md"
category: "12-Eval-Testing"
tags: ["evaluation", "testing"]
---

Before stopping, please run tests to verify your changes work correctly.

Look for test commands like:
- `npm test`
- `pytest`
- `cargo test`

**Note:** This rule blocks stopping if no test commands appear in the transcript.
Enable this rule only when you want strict test enforcement.
