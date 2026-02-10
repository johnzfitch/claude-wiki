---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:51:50Z"
source_url: "https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude"
title: "Create and edit files with Claude | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_4167966b8b)

[](#h_1c99382190)

[](#h_fa8fada4af)

[](#h_b12780b988)

[](#h_f00443cd61)

[](#h_a09d77f0fa)

[](#h_6b7e833898)

[](#h_27fc9da35e)

[](#h_1010adf0ee)

[](#h_2e2d7b155a)

[](#h_3b711c653d)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

Create and edit files with Claude

# Create and edit files with Claude

Updated yesterday

Table of contents

[](#h_4167966b8b)

[](#h_1c99382190)

[](#h_fa8fada4af)

[](#h_b12780b988)

[](#h_f00443cd61)

[](#h_a09d77f0fa)

[](#h_6b7e833898)

[](#h_27fc9da35e)

[](#h_1010adf0ee)

[](#h_2e2d7b155a)

[](#h_3b711c653d)

Claude can now execute code to create and work with files directly in your conversations. Prompt Claude using natural language to generate Excel spreadsheets, PowerPoint presentations, Word documents, and PDF files that you can download and use immediately.

Code execution and file creation is available to all Claude users (free, Pro, Max, Team, and Enterprise) on the web, Claude Desktop, and Claude Mobile.

These capabilities make it easy to produce professional documents by simply chatting with Claude. You can create financial models in Excel with working formulas, perform advanced analyses on uploaded data, produce reports with charts and visualizations, and generate presentations from your documents—all without specialized software skills.

Claude's file creation abilities are powered by Sonnet 4.5, which excels at working with documents, spreadsheets, and presentations. You can expect accurate Excel formulas, better document formatting, and more reliable file manipulation overall.

## Availability

**Pro and Max plans:**

- Code execution and file creation is enabled by default

- Network access is enabled, allowing Claude to install packages from approved sources

**Team plan:**

- Code execution and file creation is enabled by default for all members once an organization owner turns it on

- Network access is disabled by default; owners can enable it in organization settings

- New organizations have this feature disabled by default

**Enterprise plan:**

- Code execution and file creation is disabled by default

- Organization owners must enable it in Settings

- Network access is disabled by default

- Owners can configure network access controls, including domain whitelisting

## How to get started

### Enabling on web and desktop

**Enterprise plans:** This capability is disabled by default at the organization level. Owners can manually enable it in [Admin settings \> Capabilities](http://claude.ai/admin-settings/capabilities) by toggling **Code execution and file creation** on. Individual members still need to opt in to file creation in [Settings \> Capabilities](http://claude.ai/settings/capabilities) before using this feature.

**Team plans:** This capability is enabled by default at the organization level with **Allow network egress** toggled on with access to package managers only. An organization Owner can manually disable this for the organization in [Admin settings \> Capabilities](http://claude.ai/admin-settings/capabilities) if needed, or individual members can disable it in [Settings \> Capabilities](http://claude.ai/settings/capabilities) for their accounts.

**Max, Pro, and free plans:** Enable file creation from [Settings \> Capabilities](http://claude.ai/settings/capabilities) by toggling **Code execution and file creation** on:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789944704/f7218ce5e2e9bcff6f9354ddea43/6a2df26e-c3d8-4df4-b975-16719afa61aa?expires=1770585300&signature=5985fa3f97ec8123d0edf15db3359c52c8d9e654aaadae388fa2fa2590fe7f44&req=dScvH8B6mYZfXfMW1HO4zXcFZns7Zjh9GF3%2FYdESAcWm2EEV56v%2B8DtAaIHS%0AticcWUcYUwOW6x%2F57dk%3D%0A)

To give Claude access to external data sources, toggle **Allow limited network access** on when prompted:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789944703/e9af099affd9b52e18cf9decd373/8ecc03cc-e50b-43b0-8694-c500638cb781?expires=1770585300&signature=7c6cefce5c76d718b0a55c4695e23546dcc3beae22cddeeabc936c8308c737b9&req=dScvH8B6mYZfWvMW1HO4zYwjyX4sOo0TNv1GpC923dnqwxXV8tqCNIpJHrBi%0AroiiRXPPQGLP%2Bij22PY%3D%0A)

### Enabling on Claude Mobile

To enable or disable this feature on Claude for iOS or Android, tap your initials or name in the left sidebar to open Settings. Select "Capabilities" and toggle **Code execution and file creation** on or off.

## Configuring network access (Team and Enterprise plans)

Team and Enterprise organization Owners can control network access settings in [Admin settings \> Capabilities](http://claude.ai/admin-settings/capabilities). After enabling code execution and file creation, choose from the following options to configure network access for your team:

**Allow network egress toggled off:** Claude operates with pre-installed packages only, with no internet access. This provides maximum security for sensitive environments.

**Allow network egress to package managers only (default):** Claude can access approved package managers (npm, PyPI, GitHub, etc.) to install necessary software packages. This balances functionality with security, but some advanced features may be limited.

**Allow network egress to package managers and specific domains:** Claude can access package managers plus additional domains you specify. Add domains individually to whitelist specific resources your organization needs:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945362/ad72504d5429960f369b8b91b43c/86f06c0e-6eaa-4574-a4cb-2c38b273613a?expires=1770585300&signature=74e5d65be22ffc6061097d26c844d7d8b91b303264131fcd87cf5f02c0fcc8eb&req=dScvH8B6mIJZW%2FMW1HO4zXJcCW1GnSxIpMW6Iph6YZeDn5ieYV9AAyX6vOdY%0AyWWvr13NOsLsBcgJo5c%3D%0A)

**All domains:** Claude has full internet access except for domains on Anthropic's legal blocklist. While this provides maximum flexibility for file creation and analysis tasks, it’s also the riskiest option. Please review the [security considerations below](#h_0ee9d698a1) before enabling “All domains”:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945361/e3188cb8edb9ca7c303615da6378/f1c99a7d-5956-48d5-9ec7-b7ae6c8c3d28?expires=1770585300&signature=4f18f4512c4cfbe6b79a2389219c245476800401943f27626abc70d536859cd5&req=dScvH8B6mIJZWPMW1HO4zdnsdxSX5jqhqgKIA6CM1toDlqo%2BdrFqnXBgb5k9%0AoXb%2FZZYHmFvykrlNHfY%3D%0A)

**Note:** We just introduced Skills for Claude. These are packaged instructions Claude can reference to complete specific tasks. Refer to this article for more information: [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)

## How does disabling network access address security concerns with code execution and file creation?

**Short answer:** Disabling network access prevents data from leaving Claude's sandboxed environment - even if something goes wrong.

### How it works

When Claude executes code or creates files, it operates within an isolated, sandboxed container. This means the work happens in a controlled environment separate from your systems. However, if network access is enabled, there's a potential risk: through prompt injection or other attacks, Claude could theoretically be tricked into sending data to external servers.

Disabling network access eliminates this risk entirely. Your team still gets Claude's full code execution and file creation capabilities - building Excel models, creating presentations, analyzing data - but with the assurance that nothing can be transmitted outside the sandbox.

### A phased approach to network access

Claude is most powerful with network access enabled - it can install new packages and dependencies, pull in real-time data, and interact with web services. For organizations comfortable with that risk profile, enabling access to vetted, trusted domains unlocks the full potential of code execution and file creation.

For those taking a more cautious approach, we recommend starting with network access disabled and adjusting as your team builds confidence:

1.  **Start with network access off.** This is the most secure configuration. Claude can execute code and create files, but cannot communicate externally.

2.  **Enable package managers.** Unlocks pip, npm, and other package managers to install dependencies - significantly expands what Claude can build.

3.  **Expand network access as needed.** Add specific domains to an allowlist based on business requirements, maintaining visibility into what's permitted.

This approach gives you defense in depth - even if there were vulnerabilities in the sandbox or a successful prompt injection, disabled network access acts as a final barrier preventing data from leaving Anthropic's infrastructure.

**Note:** If MCP (Model Context Protocol) integrations are enabled, network communication remains possible through those connections regardless of the network egress setting. Organizations should evaluate MCP configurations separately.

------------------------------------------------------------------------

## Using code execution and file creation

When enabled, simply describe what you need in your message. For example, you might say "Create an Excel spreadsheet to track monthly expenses" or "Convert this document into a PowerPoint presentation." Claude will generate the file, which you can then download directly from the conversation.

Start with simple tasks to familiarize yourself with Claude's capabilities, then progress to more complex workflows. Be specific in your requests—describe the structure, content, and formatting you want. You may need to review and refine Claude's outputs to meet your exact requirements.

### Supported file types

Claude can create Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization.

The maximum file size is 30MB per file for both uploads and downloads.

## Key capabilities

### Direct file creation and editing

Claude creates Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

The maximum file size is 30MB per file for both uploads and downloads. For PDFs larger than 30MB, Claude can process them through its computing environment without loading them into the context window.

### Advanced data analysis

Claude can perform sophisticated data analysis and data science work, including:

- Creating Python scripts for data analysis

- Generating data visualizations as image files (PNG)

- Processing CSV, TSV, and other data files

- Building machine learning models

### Project files integration

Files in your projects are now accessible through Claude's computing environment while remaining in context. This enables seamless reference and workflow integration across your project files.

### Extended context window

The context window has been expanded to support more complex multi-step workflows, particularly for conversations that use code execution and file creation extensively.

### Language support

Claude provides full support for multiple languages in both the user interface and generated files, with proper formatting and regional standards.

## Security and network access

### How it works

Code execution and file creation gives Claude a sandboxed computing environment. Claude’s internet access will vary based on your network egress settings.

**Network access allows Claude to:**

- Download and install packages from approved package managers (npm, PyPI, etc.)

- Access resources needed for file creation and analysis

## Security considerations

It is possible for a bad actor to inconspicuously add instructions via external files or websites that trick Claude into:

1.  Downloading and running untrusted code in the sandbox environment for malicious purposes

2.  Reading sensitive data from a connected knowledge source (for example, Remote MCP, projects) and using the sandbox environment to make an external network request to leak the data

This means Claude can be tricked into sending information from its context (for example, prompts, projects, data via MCP, Google integrations) to malicious third parties. To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly. You can report issues to us using the thumbs down function directly in claude.ai.

In line with our [safe and trustworthy agents framework](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents), we have applied the following mitigations:

- Given you full control of the feature. You can turn it on or off at any time

- Designed Claude to give you user-friendly summaries of its actions so you can see what it is doing. You can stop Claude's actions at any time and we recommend monitoring Claude's work while using the feature

- Given you the ability to review and audit actions taken by Claude within the sandbox environment

- Disabled public sharing of conversations that include any file artifacts from the code execution and file creation feature for Pro and Max users

- Limited the duration of tasks that can be completed by Claude and the length of time you can use a single sandbox container to avoid loops of malicious activity

- Implemented sandbox isolation such that no sandbox environments are ever shared between users

- Intentionally limited the network, container, and storage resources

- Implemented a prompt injection classifier to detect malicious prompt manipulation and stop execution if detected

We have performed red-teaming and security testing on this feature. We have a continuous process for ongoing security testing and red-teaming. We encourage organizations to evaluate these protections against their specific security requirements when deciding whether to enable this feature.

### For Team and Enterprise Owners

Team and Enterprise Owners have full control over this feature, including:

- Enabling or disabling the feature organization-wide

- Controlling network access settings

- Configuring domain whitelisting to allow access only to specific approved domains

**Note:** Claude can only be tricked into leaking data it has access to in a conversation via an individual user's prompt, project, or activated connections.

## Approved network domains

When network access is enabled, Claude can access the following approved domains:

- **Anthropic Services (Explicit):** [api.anthropic.com](http://api.anthropic.com/), [statsig.anthropic.com](http://statsig.anthropic.com/)

- ​**GitHub:** [github.com](http://github.com/)

- **NPM:** [registry.npmjs.org](http://registry.npmjs.org/), [npmjs.com](http://npmjs.com/), [npmjs.org](http://npmjs.org/)

- ​**Python:** [pypi.org](http://pypi.org/), [files.pythonhosted.org](http://files.pythonhosted.org/), [pythonhosted.org](http://pythonhosted.org/)

- **Rust:** [crates.io](https://crates.io), [index.crates.io](https://index.crates.io), [static.crates.io](https://static.crates.io)

- **Ubuntu:** [archive.ubuntu.com](https://archive.ubuntu.com), [security.ubuntu.com](https://security.ubuntu.com)

- **Yarn:** [yarnpkg.com](http://yarnpkg.com/), [registry.yarnpkg.com](http://registry.yarnpkg.com/)

------------------------------------------------------------------------

## Common workflows

**Note:** Refer to [Create and edit files with Claude to eliminate hours of busy work](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work) for use cases and demo videos, and [Financial Analysis Workflows with Claude](https://support.claude.com/en/articles/12220298-financial-analysis-workflows-with-claude) for guidelines specific to Claude for Financial Services customers.

### Build a financial model in Excel

Generate spreadsheets with working formulas and calculations by describing your needs. Try:

    Create a monthly budget tracker with income, expenses categories, and 
    automatic calculations for savings.

Claude will produce an Excel file with proper formulas, formatting, and even charts to visualize your data.

### Generate a professional report

Combine data analysis with document creation by providing your information and requirements. Try:

    Create a quarterly sales report using this CSV data, including trend 
    analysis and recommendations.

Claude will analyze your data and produce a formatted Word document or PDF with charts, insights, and professional formatting.

### Convert between file formats

Change any document from one format to another while preserving or enhancing the content. Try:

    Convert this Word document to a presentation.

or

    Explain this Excel spreadsheet in a Word report with commentary.

Claude can even support workflows requiring multiple file format conversions. For instance, you could upload a CSV file and prompt Claude to create a financial model, write a memo summarizing it, and generate a PowerPoint to share the results.

### Extract and analyze PDF data

Upload a PDF containing tables or forms and ask Claude to extract the information. Try:

    Extract all the data from this PDF into an Excel spreadsheet and create a 
    summary chart.

Claude will pull the data, organize it in spreadsheet format, and add visualizations for quick insights.

### Perform Complex Analyses

Upload a CSV with data and ask Claude to build a machine learning model to predict a particular outcome. Have Claude output a report summarizing what it did and the results. Claude will use python to train a model on your data, and provide an explanation of what it did, including the quality of the model, and the results.

------------------------------------------------------------------------

## FAQ

### How does file creation work?

We have given Claude a private computing environment directly in claude.ai. This allows Claude to write and run code (for example Python or Javascript). It uses common code packages to create documents, spreadsheets, and slides. Users can also have Claude use its computing environment for other things like data analysis, debugging code snippets, and fun tasks like gif-creation.

### How do Claude’s file creation capabilities impact usage limits?

Use of this capability draws from the same usage limits offered by your plan. Note that creating files will use more of your limit compared to normal chats with Claude.

### Can Claude work with more than one file at a time?

Claude can handle multiple files in a single chat, allowing you to create comprehensive multi-file reports and analyses. Files remain available for download throughout your conversation.

### Is file creation supported on Claude for iOS or Android?

File creation is now supported on Claude for iOS and Android. Note that when you tap "Download" on Claude Mobile, the file will open in either the system preview or a separate app (for example, the Word app for .docx files).

### Do artifacts work with file creation?

Yes you are still able to create artifacts (e.g., HTML or react apps, markdown documents, mermaid diagrams, SVGs) with file creation on. Claude now uses the computing environment to create artifacts so the user experience may look slightly different than users are used to. Please report any issues or feedback using the thumbs up/down functionality in [claude.ai](http://claude.ai).

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10065433-installing-claude-desktop)

Installing Claude Desktop

[](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work)

Create and edit files with Claude to eliminate hours of busy work

[](https://support.claude.com/en/articles/12439380-create-professional-results-across-tools-with-claude-sonnet-4-5)

Create professional results across tools with Claude Sonnet 4.5

[](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

Using Skills in Claude

[](https://support.claude.com/en/articles/12663107-claude-for-financial-services-skills)

Claude for Financial Services Skills

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
