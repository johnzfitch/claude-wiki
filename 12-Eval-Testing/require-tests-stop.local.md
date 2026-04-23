---
title: "Require Tests Stop.Local"
category: "12-Eval-Testing"
---

Before stopping, please run tests to verify your changes work correctly.

Look for test commands like:
- `npm test`
- `pytest`
- `cargo test`

**Note:** This rule blocks stopping if no test commands appear in the transcript.
Enable this rule only when you want strict test enforcement.
