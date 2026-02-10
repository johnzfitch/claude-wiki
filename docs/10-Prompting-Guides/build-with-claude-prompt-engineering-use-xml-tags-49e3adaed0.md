---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags"
---


Prompt engineering
Use XML tags to structure your prompts
Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here.

When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

XML tip: Use tags like <instructions>, <example>, and <formatting> to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.
Why use XML tags?
Clarity: Clearly separate different parts of your prompt and ensure your prompt is well structured.
Accuracy: Reduce errors caused by Claude misinterpreting parts of your prompt.
Flexibility: Easily find, add, remove, or modify parts of your prompt without rewriting everything.
Parseability: Having Claude use XML tags in its output makes it easier to extract specific parts of its response by post-processing.
There are no canonical "best" XML tags that Claude has been trained with in particular, although we recommend that your tag names make sense with the information they surround.
Tagging best practices
Be consistent: Use the same tag names throughout your prompts, and refer to those tag names when talking about the content (e.g, Using the contract in <contract> tags...).
Nest tags: You should nest tags <outer><inner></inner></outer> for hierarchical content.
Power user tip: Combine XML tags with other techniques like multishot prompting (<examples>) or chain of thought (<thinking>, <answer>). This creates super-structured, high-performance prompts.
Examples
Example: Generating financial reports
Example: Legal contract analysis
Prompt library

Get inspired by a curated selection of prompts for various tasks and use cases.

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?