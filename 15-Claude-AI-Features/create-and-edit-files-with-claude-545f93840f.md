---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude"
---


Claude can now execute code to create and work with files directly in your conversations. Prompt Claude using natural language to generate Excel spreadsheets, PowerPoint presentations, Word documents, and PDF files that you can download and use immediately.

Code execution and file creation is available to all Claude users (free, Pro, Max, Team, and Enterprise) on the web, Claude Desktop, and Claude Mobile.

These capabilities make it easy to produce professional documents by simply chatting with Claude. You can create financial models in Excel with working formulas, perform advanced analyses on uploaded data, produce reports with charts and visualizations, and generate presentations from your documents—all without specialized software skills.

 

Claude's file creation abilities are powered by Sonnet 4.5, which excels at working with documents, spreadsheets, and presentations. You can expect accurate Excel formulas, better document formatting, and more reliable file manipulation overall.

 

Availability

Pro and Max plans:

Code execution and file creation is enabled by default

Network access is enabled, allowing Claude to install packages from approved sources

Team plan:

Code execution and file creation is enabled by default for all members once an organization owner turns it on

Network access is disabled by default; owners can enable it in organization settings

New organizations have this feature disabled by default

Enterprise plan:

Code execution and file creation is disabled by default

Organization owners must enable it in Settings

Network access is disabled by default

Owners can configure network access controls, including domain whitelisting 

 

How to get started
Enabling on web and desktop

Enterprise plans: This capability is disabled by default at the organization level. Owners can manually enable it in Admin settings > Capabilities by toggling Code execution and file creation on. Individual members still need to opt in to file creation in Settings > Capabilities before using this feature.

 

Team plans: This capability is enabled by default at the organization level with Allow network egress toggled on with access to package managers only. An organization Owner can manually disable this for the organization in Admin settings > Capabilities if needed, or individual members can disable it in Settings > Capabilities for their accounts.

 

Max, Pro, and free plans: Enable file creation from Settings > Capabilities by toggling Code execution and file creation on:

 

To give Claude access to external data sources, toggle Allow limited network access on when prompted:

 

Enabling on Claude Mobile

To enable or disable this feature on Claude for iOS or Android, tap your initials or name in the left sidebar to open Settings. Select "Capabilities" and toggle Code execution and file creation on or off.

 

Configuring network access (Team and Enterprise plans)

Team and Enterprise organization Owners can control network access settings in Admin settings > Capabilities. After enabling code execution and file creation, choose from the following options to configure network access for your team:

 

Allow network egress toggled off: Claude operates with pre-installed packages only, with no internet access. This provides maximum security for sensitive environments.

 

Allow network egress to package managers only (default): Claude can access approved package managers (npm, PyPI, GitHub, etc.) to install necessary software packages. This balances functionality with security, but some advanced features may be limited.

 

Allow network egress to package managers and specific domains: Claude can access package managers plus additional domains you specify. Add domains individually to whitelist specific resources your organization needs:

 

 

All domains: Claude has full internet access except for domains on Anthropic's legal blocklist. While this provides maximum flexibility for file creation and analysis tasks, it’s also the riskiest option. Please review the security considerations below before enabling “All domains”:

 

Note: We just introduced Skills for Claude. These are packaged instructions Claude can reference to complete specific tasks. Refer to this article for more information: What are Skills?

 

How does disabling network access address security concerns with code execution and file creation?

Short answer: Disabling network access prevents data from leaving Claude's sandboxed environment - even if something goes wrong.

 

How it works

When Claude executes code or creates files, it operates within an isolated, sandboxed container. This means the work happens in a controlled environment separate from your systems. However, if network access is enabled, there's a potential risk: through prompt injection or other attacks, Claude could theoretically be tricked into sending data to external servers.

 

Disabling network access eliminates this risk entirely. Your team still gets Claude's full code execution and file creation capabilities - building Excel models, creating presentations, analyzing data - but with the assurance that nothing can be transmitted outside the sandbox.

 

A phased approach to network access

Claude is most powerful with network access enabled - it can install new packages and dependencies, pull in real-time data, and interact with web services. For organizations comfortable with that risk profile, enabling access to vetted, trusted domains unlocks the full potential of code execution and file creation.

For those taking a more cautious approach, we recommend starting with network access disabled and adjusting as your team builds confidence:

Start with network access off. This is the most secure configuration. Claude can execute code and create files, but cannot communicate externally.

Enable package managers. Unlocks pip, npm, and other package managers to install dependencies - significantly expands what Claude can build.

Expand network access as needed. Add specific domains to an allowlist based on business requirements, maintaining visibility into what's permitted.

This approach gives you defense in depth - even if there were vulnerabilities in the sandbox or a successful prompt injection, disabled network access acts as a final barrier preventing data from leaving Anthropic's infrastructure.

Note: If MCP (Model Context Protocol) integrations are enabled, network communication remains possible through those connections regardless of the network egress setting. Organizations should evaluate MCP configurations separately.

 

 

Using code execution and file creation

When enabled, simply describe what you need in your message. For example, you might say "Create an Excel spreadsheet to track monthly expenses" or "Convert this document into a PowerPoint presentation." Claude will generate the file, which you can then download directly from the conversation.

 

Start with simple tasks to familiarize yourself with Claude's capabilities, then progress to more complex workflows. Be specific in your requests—describe the structure, content, and formatting you want. You may need to review and refine Claude's outputs to meet your exact requirements.

 

Supported file types

Claude can create Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

 

With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization.

 

The maximum file size is 30MB per file for both uploads and downloads.

 

Key capabilities
Direct file creation and editing

Claude creates Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

 

The maximum file size is 30MB per file for both uploads and downloads. For PDFs larger than 30MB, Claude can process them through its computing environment without loading them into the context window.

 

Advanced data analysis

Claude can perform sophisticated data analysis and data science work, including:

Creating Python scripts for data analysis

Generating data visualizations as image files (PNG)

Processing CSV, TSV, and other data files

Building machine learning models

Project files integration

Files in your projects are now accessible through Claude's computing environment while remaining in context. This enables seamless reference and workflow integration across your project files.

 

Extended context window

The context window has been expanded to support more complex multi-step workflows, particularly for conversations that use code execution and file creation extensively.

 

Language support

Claude provides full support for multiple languages in both the user interface and generated files, with proper formatting and regional standards.

 

Security and network access
How it works

Code execution and file creation gives Claude a sandboxed computing environment. Claude’s internet access will vary based on your network egress settings.

 

Network access allows Claude to:

Download and install packages from approved package managers (npm, PyPI, etc.)

Access resources needed for file creation and analysis 

Security considerations

It is possible for a bad actor to inconspicuously add instructions via external files or websites that trick Claude into:

Downloading and running untrusted code in the sandbox environment for malicious purposes

Reading sensitive data from a connected knowledge source (for example, Remote MCP, projects) and using the sandbox environment to make an external network request to leak the data

This means Claude can be tricked into sending information from its context (for example, prompts, projects, data via MCP, Google integrations) to malicious third parties. To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly. You can report issues to us using the thumbs down function directly in claude.ai.

In line with our safe and trustworthy agents framework, we have applied the following mitigations:

Given you full control of the feature. You can turn it on or off at any time

Designed Claude to give you user-friendly summaries of its actions so you can see what it is doing. You can stop Claude's actions at any time and we recommend monitoring Claude's work while using the feature

Given you the ability to review and audit actions taken by Claude within the sandbox environment

Disabled public sharing of conversations that include any file artifacts from the code execution and file creation feature for Pro and Max users

Limited the duration of tasks that can be completed by Claude and the length of time you can use a single sandbox container to avoid loops of malicious activity

Implemented sandbox isolation such that no sandbox environments are ever shared between users

Intentionally limited the network, container, and storage resources

Implemented a prompt injection classifier to detect malicious prompt manipulation and stop execution if detected

We have performed red-teaming and security testing on this feature. We have a continuous process for ongoing security testing and red-teaming. We encourage organizations to evaluate these protections against their specific security requirements when deciding whether to enable this feature.

 

For Team and Enterprise Owners

Team and Enterprise Owners have full control over this feature, including:

Enabling or disabling the feature organization-wide

Controlling network access settings

Configuring domain whitelisting to allow access only to specific approved domains

Note: Claude can only be tricked into leaking data it has access to in a conversation via an individual user's prompt, project, or activated connections.

 

Approved network domains

When network access is enabled, Claude can access the following approved domains:

Anthropic Services (Explicit): api.anthropic.com, statsig.anthropic.com

​GitHub: github.com

NPM: registry.npmjs.org, npmjs.com, npmjs.org

​Python: pypi.org, files.pythonhosted.org, pythonhosted.org

Rust: crates.io, index.crates.io, static.crates.io

Ubuntu: archive.ubuntu.com, security.ubuntu.com

Yarn: yarnpkg.com, registry.yarnpkg.com 

 

Common workflows

Note: Refer to Create and edit files with Claude to eliminate hours of busy work for use cases and demo videos, and Financial Analysis Workflows with Claude for guidelines specific to Claude for Financial Services customers.

Build a financial model in Excel

Generate spreadsheets with working formulas and calculations by describing your needs. Try:

Create a monthly budget tracker with income, expenses categories, and 
automatic calculations for savings.

Claude will produce an Excel file with proper formulas, formatting, and even charts to visualize your data.

 

Generate a professional report

Combine data analysis with document creation by providing your information and requirements. Try:

Create a quarterly sales report using this CSV data, including trend 
analysis and recommendations.

Claude will analyze your data and produce a formatted Word document or PDF with charts, insights, and professional formatting.

 

Convert between file formats

Change any document from one format to another while preserving or enhancing the content. Try:

Convert this Word document to a presentation.

or

Explain this Excel spreadsheet in a Word report with commentary.

Claude can even support workflows requiring multiple file format conversions. For instance, you could upload a CSV file and prompt Claude to create a financial model, write a memo summarizing it, and generate a PowerPoint to share the results. 

 

Extract and analyze PDF data

Upload a PDF containing tables or forms and ask Claude to extract the information. Try:

Extract all the data from this PDF into an Excel spreadsheet and create a 
summary chart.

Claude will pull the data, organize it in spreadsheet format, and add visualizations for quick insights.

 

Perform Complex Analyses

Upload a CSV with data and ask Claude to build a machine learning model to predict a particular outcome. Have Claude output a report summarizing what it did and the results. Claude will use python to train a model on your data, and provide an explanation of what it did, including the quality of the model, and the results.

 

 

FAQ
How does file creation work? 

We have given Claude a private computing environment directly in claude.ai. This allows Claude to write and run code (for example Python or Javascript). It uses common code packages to create documents, spreadsheets, and slides. Users can also have Claude use its computing environment for other things like data analysis, debugging code snippets, and fun tasks like gif-creation.

 

How do Claude’s file creation capabilities impact usage limits?

Use of this capability draws from the same usage limits offered by your plan. Note that creating files will use more of your limit compared to normal chats with Claude.

 

Can Claude work with more than one file at a time?

Claude can handle multiple files in a single chat, allowing you to create comprehensive multi-file reports and analyses. Files remain available for download throughout your conversation.

 

Is file creation supported on Claude for iOS or Android?

File creation is now supported on Claude for iOS and Android. Note that when you tap "Download" on Claude Mobile, the file will open in either the system preview or a separate app (for example, the Word app for .docx files).

 

Do artifacts work with file creation? 

Yes you are still able to create artifacts (e.g., HTML or react apps, markdown documents, mermaid diagrams, SVGs) with file creation on. Claude now uses the computing environment to create artifacts so the user experience may look slightly different than users are used to. Please report any issues or feedback using the thumbs up/down functionality in claude.ai.

Related Articles
Installing Claude Desktop
Create and edit files with Claude to eliminate hours of busy work
Create professional results across tools with Claude Sonnet 4.5
Using Skills in Claude
Claude for Financial Services Skills