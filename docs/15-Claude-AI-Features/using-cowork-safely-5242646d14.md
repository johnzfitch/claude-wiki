---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/13364135-using-cowork-safely"
---


Cowork is available as a research preview for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS.

 

Download for macOS

 

Understanding the risks

Cowork is a research preview with unique risks due to its agentic nature and internet access.

 

To minimize risks:

Avoid granting access to local files with sensitive information, like financial documents.

When using the Claude in Chrome extension, limit access to trusted sites.

If you chose to extend Claude’s default internet access settings, be careful to only extend internet access to sites you trust.

Monitor Claude for suspicious actions that may indicate prompt injection.

Ensure you’re using trusted MCPs (as always).

Important: Cowork has access to Claude in Chrome; we strongly advise against using Claude in Chrome to manage or take actions involving sensitive information. See Using Claude in Chrome safely for more information about the potential risks.

 

Our safety measures

We've implemented multiple layers of protection:

Model training: We use reinforcement learning to train Claude to recognize and refuse malicious instructions—even when they appear authoritative or urgent.

Content classifiers: We scan all untrusted content entering Claude's context and flag potential injections before they can affect behavior.

Important: While we've enacted these safety measures to reduce risks, the chances of an attack are still non-zero. Always exercise caution when using Cowork.

 

 

Protecting yourself from malicious attackers

1. Be selective about file access

You control which local files Claude can access. Since Claude can read, write, and permanently delete these files, be cautious about granting access to sensitive information like financial documents, credentials, or personal records. Consider creating a dedicated working folder for Claude rather than granting broad access, and keep backups of important files.

 

2. Monitor tasks, not just commands

Cowork executes code and commands on your behalf. While we surface what Claude is doing, you shouldn't expect to validate every individual command—instead, watch for unexpected patterns: Is Claude accessing files or websites you didn't mention? Is the task scope creeping beyond what you asked for? If something feels off, stop the task immediately.

 

3. Limit browser and web access to trusted sources

If you're using the Claude in Chrome extension with Cowork, limit access to sites you trust. Web content is a primary vector for prompt injection attacks—malicious instructions can be hidden in websites, emails, or documents that Claude accesses. Claude's default network access is intentionally restricted; only extend it to sites you trust.

 

4. Be especially cautious with unfamiliar MCPs

Desktop extensions (MCPs) expand what Claude can do, but each one introduces new ways for attacks to reach Claude. Stick to verified extensions from the Claude Desktop directory, and carefully evaluate the permissions any extension requests before installing.

 

5. Report suspicious behavior immediately

If Claude suddenly starts discussing unrelated topics, attempts to access unexpected resources, or requests sensitive information unprompted, stop the task and report it to usersafety@anthropic.com or use the in-app feedback button. Your reports help us improve our defenses.

 

 

Your responsibility

You remain responsible for all actions taken by Claude performed on your behalf. This includes:

Any content published or messages sent

Purchases or financial transactions

Data accessed or modified

Respecting third-party website terms of service, including any restrictions on automated access

For more information about using AI agents safely, please review our Acceptable Use Policy for Agents.

Related Articles
Installing Claude Desktop
When to Use Desktop and Web Connectors
Using Claude in Chrome Safely
Getting started with Cowork
Cowork for Team and Enterprise plans