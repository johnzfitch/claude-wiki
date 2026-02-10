---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/eval-tool"
---


Test & evaluate
Using the Evaluation Tool
Copy page
The Claude Console features an Evaluation tool that allows you to test your prompts under various scenarios.
Accessing the Evaluate Feature

To get started with the Evaluation tool:

Open the Claude Console and navigate to the prompt editor.
After composing your prompt, look for the 'Evaluate' tab at the top of the screen.

Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: {{variable}}. This is required for creating eval test sets.

Generating Prompts

The Console offers a built-in prompt generator powered by Claude Opus 4.1:

1

Click 'Generate Prompt'

Clicking the 'Generate Prompt' helper tool will open a modal that allows you to enter your task information.

2

Describe your task

Describe your desired task (e.g., "Triage inbound customer support requests") with as much or as little detail as you desire. The more context you include, the more Claude can tailor its generated prompt to your specific needs.

3

Generate your prompt

Clicking the orange 'Generate Prompt' button at the bottom will have Claude generate a high quality prompt for you. You can then further improve those prompts using the Evaluation screen in the Console.

This feature makes it easier to create prompts with the appropriate variable syntax for evaluation.

Creating Test Cases

When you access the Evaluation screen, you have several options to create test cases:

Click the '+ Add Row' button at the bottom left to manually add a case.
Use the 'Generate Test Case' feature to have Claude automatically generate test cases for you.
Import test cases from a CSV file.

To use the 'Generate Test Case' feature:

1

Click on 'Generate Test Case'

Claude will generate test cases for you, one row at a time for each time you click the button.

2

Edit generation logic (optional)

You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the 'Generate Test Case' button, then on 'Show generation logic' at the top of the Variables window that pops up. You may have to click `Generate' on the top right of this window to populate initial generation logic.

Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.

Here's an example of a populated Evaluation screen with several test cases:

If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.

Tips for Effective Evaluation
Prompt Structure for Evaluation

Use the 'Generate a prompt' helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.

Understanding and comparing results

The Evaluation tool offers several features to help you refine your prompts:

Side-by-side comparison: Compare the outputs of two or more prompts to quickly see the impact of your changes.
Quality grading: Grade response quality on a 5-point scale to track improvements in response quality per prompt.
Prompt versioning: Create new versions of your prompt and re-run the test suite to quickly iterate and improve results.

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments to your prompt more efficiently.

Start evaluating your prompts today to build more robust AI applications with Claude!

Was this page helpful?