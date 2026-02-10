---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prefill-claudes-response"
---


Prompt engineering
Prefill Claude's response for greater output control
Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here.

Prefilling is only available for non-extended thinking modes. It's not currently supported with extended thinking.

When using Claude, you have the unique ability to guide its responses by prefilling the Assistant message. This powerful technique allows you to direct Claude's actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios.

In some cases where Claude is not performing as expected, a few prefilled sentences can vastly improve Claude's performance. A little prefilling goes a long way!

How to prefill Claude's response

To prefill, include the desired initial text in the Assistant message (Claude's response will continue from where the Assistant message leaves off):

import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
 model="claude-sonnet-4-5",
 max_tokens=1024,
 messages=[
 {"role": "user", "content": "What is your favorite color?"},
 {"role": "assistant", "content": "As an AI assistant, I don't have a favorite color, But if I had to pick, it would be green because"} # Prefill here
 ]
)

The prefill content cannot end with trailing whitespace. A prefill like "As an AI assistant, I " (with a space at the end) will result in an error.

Examples
Example 1: Controlling output formatting and skipping the preamble
Power user tip: Prefilling { forces Claude to skip the preamble and directly output the JSON object. This is cleaner, more concise, and easier for programs to parse without additional processing. For guaranteed JSON output that conforms to a specific schema, consider using Structured Outputs instead of prefilling. Structured outputs ensure Claude's response always matches your defined JSON schema, making it ideal for production applications that require strict format compliance.
Example: Structured data extraction without prefilling
Example: Structured data extraction with prefilling
Example 2: Maintaining character in roleplay scenarios
Role-play tip: Prefilling a bracketed [ROLE_NAME] can remind Claude stay in character, even for longer and more complex conversations. This is especially powerful when combined with role prompting in the system parameter.
Example: Maintaining character without role prompting
Example: Maintaining character with role prompting
Working with Messages

See more examples of prefill and other Messages API patterns.

Prompt library

Get inspired by a curated selection of prompts for various tasks and use cases.

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?