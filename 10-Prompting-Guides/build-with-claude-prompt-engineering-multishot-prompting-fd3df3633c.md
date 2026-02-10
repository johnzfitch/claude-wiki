---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting"
---


Prompt engineering
Use examples (multishot prompting) to guide Claude's behavior
Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here.

Examples are your secret weapon shortcut for getting Claude to generate exactly what you need. By providing a few well-crafted examples in your prompt, you can dramatically improve the accuracy, consistency, and quality of Claude's outputs. This technique, known as few-shot or multishot prompting, is particularly effective for tasks that require structured outputs or adherence to specific formats.

Power up your prompts: Include 3-5 diverse, relevant examples to show Claude exactly what you want. More examples = better performance, especially for complex tasks.
Why use examples?
Accuracy: Examples reduce misinterpretation of instructions.
Consistency: Examples enforce uniform structure and style.
Performance: Well-chosen examples boost Claude's ability to handle complex tasks.
Crafting effective examples

For maximum effectiveness, make sure that your examples are:

Relevant: Your examples mirror your actual use case.
Diverse: Your examples cover edge cases and potential challenges, and vary enough that Claude doesn't inadvertently pick up on unintended patterns.
Clear: Your examples are wrapped in <example> tags (if multiple, nested within <examples> tags) for structure.
Ask Claude to evaluate your examples for relevance, diversity, or clarity. Or have Claude generate more examples based on your initial set.
Example: Analyzing customer feedback
Prompt library

Get inspired by a curated selection of prompts for various tasks and use cases.

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?