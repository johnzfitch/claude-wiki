---
title: "Prompt engineering overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview"
category: "10-Prompting-Guides"
fetched_at: "2026-09-26T06:39:25Z"
tags: ["prompting"]
---

# Prompt engineering overview

Copy page



Learn when prompt engineering is the right solution, and find Claude prompting techniques and interactive tutorials.

Copy page



## Before prompt engineering

This guide assumes that you have:

1.  A clear definition of the success criteria for your use case
2.  Some ways to empirically test against those criteria
3.  A first draft prompt you want to improve

If not, spend time establishing that first. Check out [Define success criteria and build evaluations](/docs/en/test-and-evaluate/develop-tests) for tips and guidance.



[Prompt generator notebook](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb)

Don't have a first draft prompt? Generate one with the metaprompt recipe from the Claude Cookbook.



[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

For model-specific tuning guidance for Claude's latest models, start here.

------------------------------------------------------------------------

## When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by selecting a different model.

------------------------------------------------------------------------

## How to prompt engineer

All prompting techniques (from clarity and examples to XML structuring, role prompting, thinking, and prompt chaining) are covered in [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). That's the living reference; start there.

For general prompt engineering craft beyond Claude-specific techniques, see the blog post on [best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering).

------------------------------------------------------------------------

## Prompt engineering tutorial

If you're an interactive learner, you can start with the interactive tutorials instead!




An example-filled tutorial that covers the prompt engineering concepts found in the docs.



[Google Sheets prompting tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

A lighter-weight version of the prompt engineering tutorial, as an interactive spreadsheet.
