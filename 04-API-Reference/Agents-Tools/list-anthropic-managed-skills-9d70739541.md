---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart"
title: "List Anthropic-managed Skills"
---


Agent Skills
Get started with Agent Skills in the API
Copy page
Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.

This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a simple request, and access the generated file.

Prerequisites
Anthropic API key
Python 3.7+ or curl installed
Basic familiarity with making API requests
What are Agent Skills?

Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks like creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:

PowerPoint (pptx): Create and edit presentations
Excel (xlsx): Create and analyze spreadsheets
Word (docx): Create and edit documents
PDF (pdf): Generate PDF documents

Want to create custom Skills? See the Agent Skills Cookbook for examples of building your own Skills with domain-specific expertise.

Step 1: List available Skills

First, let's see what Skills are available. We'll use the Skills API to list all Anthropic-managed Skills:

Python
import anthropic

client = anthropic.Anthropic()

# List Anthropic-managed Skills
skills = client.beta.skills.list(
 source="anthropic",
 betas=["skills-2025-10-02"]
)

for skill in skills.data:
 print(f"{skill.id}: {skill.display_title}")

You see the following Skills: pptx, xlsx, docx, and pdf.

This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of progressive disclosure, where Claude discovers Skills without loading their full instructions yet.

Step 2: Create a presentation

Now we'll use the PowerPoint Skill to create a presentation about renewable energy. We specify Skills using the container parameter in the Messages API:

Python
import anthropic

client = anthropic.Anthropic()

# Create a message with the PowerPoint Skill
response = client.beta.messages.create(
 model="claude-sonnet-4-5-20250929",
 max_tokens=4096,
 betas=["code-execution-2025-08-25", "skills-2025-10-02"],
 container={
 "skills": [
 {
 "type": "anthropic",
 "skill_id": "pptx",
 "version": "latest"
 }
 ]
 },
 messages=[{
 "role": "user",
 "content": "Create a presentation about renewable energy with 5 slides"
 }],
 tools=[{
 "type": "code_execution_20250825",
 "name": "code_execution"
 }]
)

print(response.content)

Let's break down what each part does:

container.skills: Specifies which Skills Claude can use
type: "anthropic": Indicates this is an Anthropic-managed Skill
skill_id: "pptx": The PowerPoint Skill identifier
version: "latest": The Skill version set to the most recently published
tools: Enables code execution (required for Skills)
Beta headers: code-execution-2025-08-25 and skills-2025-10-02

When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.

Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:

Python
# Extract file ID from response
file_id = None
for block in response.content:
 if block.type == 'tool_use' and block.name == 'code_execution':
 # File ID is in the tool result
 for result_block in block.content:
 if hasattr(result_block, 'file_id'):
 file_id = result_block.file_id
 break

if file_id:
 # Download the file
 file_content = client.beta.files.download(
 file_id=file_id,
 betas=["files-api-2025-04-14"]
 )

 # Save to disk
 with open("renewable_energy.pptx", "wb") as f:
 file_content.write_to_file(f.name)

 print(f"Presentation saved to renewable_energy.pptx")

For complete details on working with generated files, see the code execution tool documentation.

Try more examples

Now that you've created your first document with Skills, try these variations:

Create a spreadsheet
Python
response = client.beta.messages.create(
 model="claude-sonnet-4-5-20250929",
 max_tokens=4096,
 betas=["code-execution-2025-08-25", "skills-2025-10-02"],
 container={
 "skills": [
 {
 "type": "anthropic",
 "skill_id": "xlsx",
 "version": "latest"
 }
 ]
 },
 messages=[{
 "role": "user",
 "content": "Create a quarterly sales tracking spreadsheet with sample data"
 }],
 tools=[{
 "type": "code_execution_20250825",
 "name": "code_execution"
 }]
)
Create a Word document
Python
response = client.beta.messages.create(
 model="claude-sonnet-4-5-20250929",
 max_tokens=4096,
 betas=["code-execution-2025-08-25", "skills-2025-10-02"],
 container={
 "skills": [
 {
 "type": "anthropic",
 "skill_id": "docx",
 "version": "latest"
 }
 ]
 },
 messages=[{
 "role": "user",
 "content": "Write a 2-page report on the benefits of renewable energy"
 }],
 tools=[{
 "type": "code_execution_20250825",
 "name": "code_execution"
 }]
)
Generate a PDF
Python
response = client.beta.messages.create(
 model="claude-sonnet-4-5-20250929",
 max_tokens=4096,
 betas=["code-execution-2025-08-25", "skills-2025-10-02"],
 container={
 "skills": [
 {
 "type": "anthropic",
 "skill_id": "pdf",
 "version": "latest"
 }
 ]
 },
 messages=[{
 "role": "user",
 "content": "Generate a PDF invoice template"
 }],
 tools=[{
 "type": "code_execution_20250825",
 "name": "code_execution"
 }]
)
Next steps

Now that you've used pre-built Agent Skills, you can:

API Guide

Use Skills with the Claude API

Create Custom Skills

Upload your own Skills for specialized tasks

Authoring Guide

Learn best practices for writing effective Skills

Use Skills in Claude Code

Learn about Skills in Claude Code

Use Skills in the Agent SDK

Use Skills programmatically in TypeScript and Python

Agent Skills Cookbook

Explore example Skills and implementation patterns

Was this page helpful?