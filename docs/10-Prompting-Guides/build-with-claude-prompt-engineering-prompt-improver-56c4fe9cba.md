---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-improver"
---


Prompt engineering
Use our prompt improver to optimize your prompts
Copy page

Our prompt improver is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see here.

The prompt improver helps you quickly iterate and improve your prompts through automated analysis and enhancement. It excels at making prompts more robust for complex tasks that require high accuracy.

Before you begin

You'll need:

A prompt template to improve
Feedback on current issues with Claude's outputs (optional but recommended)
Example inputs and ideal outputs (optional but recommended)
How the prompt improver works

The prompt improver enhances your prompts in 4 steps:

Example identification: Locates and extracts examples from your prompt template
Initial draft: Creates a structured template with clear sections and XML tags
Chain of thought refinement: Adds and refines detailed reasoning instructions
Example enhancement: Updates examples to demonstrate the new reasoning process

You can watch these steps happen in real-time in the improvement modal.

What you get

The prompt improver generates templates with:

Detailed chain-of-thought instructions that guide Claude's reasoning process and typically improve its performance
Clear organization using XML tags to separate different components
Standardized example formatting that demonstrates step-by-step reasoning from input to output
Strategic prefills that guide Claude's initial responses

While examples appear separately in the Workbench UI, they're included at the start of the first user message in the actual API call. View the raw format by clicking "</> Get Code" or insert examples as raw text via the Examples box.

How to use the prompt improver
Submit your prompt template
Add any feedback about issues with Claude's current outputs (e.g., "summaries are too basic for expert audiences")
Include example inputs and ideal outputs
Review the improved prompt
Generate test examples

Don't have examples yet? Use our Test Case Generator to:

Generate sample inputs
Get Claude's responses
Edit the responses to match your ideal outputs
Add the polished examples to your prompt
When to use the prompt improver

The prompt improver works best for:

Complex tasks requiring detailed reasoning
Situations where accuracy is more important than speed
Problems where Claude's current outputs need significant improvement

For latency or cost-sensitive applications, consider using simpler prompts. The prompt improver creates templates that produce longer, more thorough, but slower responses.

Example improvement

Here's how the prompt improver enhances a basic classification prompt:

Original prompt
Improved prompt

Notice how the improved prompt:

Adds clear step-by-step reasoning instructions
Uses XML tags to organize content
Provides explicit output formatting requirements
Guides Claude through the analysis process
Troubleshooting

Common issues and solutions:

Examples not appearing in output: Check that examples are properly formatted with XML tags and appear at the start of the first user message
Chain of thought too verbose: Add specific instructions about desired output length and level of detail
Reasoning steps don't match your needs: Modify the steps section to match your specific use case
Next steps
Prompt library

Get inspired by example prompts for various tasks.

GitHub prompting tutorial

Learn prompting best practices with our interactive tutorial.

Test your prompts

Use our evaluation tool to test your improved prompts.

Was this page helpful?