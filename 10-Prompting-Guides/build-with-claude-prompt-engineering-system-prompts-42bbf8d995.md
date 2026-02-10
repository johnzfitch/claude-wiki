---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts"
---


Prompt engineering
Giving Claude a role with a system prompt
Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here.

When using Claude, you can dramatically improve its performance by using the system parameter to give it a role. This technique, known as role prompting, is the most powerful way to use system prompts with Claude.

The right role can turn Claude from a general assistant into your virtual domain expert!

System prompt tips: Use the system parameter to set Claude's role. Put everything else, like task-specific instructions, in the user turn instead.
Why use role prompting?
Enhanced accuracy: In complex scenarios like legal analysis or financial modeling, role prompting can significantly boost Claude's performance.
Tailored tone: Whether you need a CFO's brevity or a copywriter's flair, role prompting adjusts Claude's communication style.
Improved focus: By setting the role context, Claude stays more within the bounds of your task's specific requirements.
How to give Claude a role

Use the system parameter in the Messages API to set Claude's role:

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
 model="claude-sonnet-4-5-20250929",
 max_tokens=2048,
 system="You are a seasoned data scientist at a Fortune 500 company.", # <-- role prompt
 messages=[
 {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
 ]
)

print(response.content)
Role prompting tip: Experiment with roles! A data scientist might see different insights than a marketing strategist for the same data. A data scientist specializing in customer insight analysis for Fortune 500 companies might yield different results still!
Examples
Example 1: Legal contract analysis

Without a role, Claude might miss critical issues:

Legal contract analysis without role prompting

With a role, Claude catches critical issues that could cost millions:

Legal contract analysis with role prompting
Example 2: Financial analysis

Without a role, Claude's analysis lacks depth:

Financial analysis without role prompting

With a role, Claude delivers actionable insights:

Financial analysis with role prompting
Prompt library

Get inspired by a curated selection of prompts for various tasks and use cases.

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?