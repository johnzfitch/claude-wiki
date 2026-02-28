---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T11:22:23Z"
source_url: "https://support.claude.com/en/articles/13364135-use-cowork-safely"
title: "Use Cowork safely | Claude Help Center"
---

# Use Cowork safely


## Availability

Cowork is available as a research preview for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows** (x64 only)

  - Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

  - Windows arm64 is not supported.

------------------------------------------------------------------------

## Understanding the risks

**[Cowork](https://claude.com/product/cowork)** is a research preview with unique risks due to its agentic nature and internet access.

**To minimize risks:**

- Avoid granting access to local files with sensitive information, like financial documents.

- When using the Claude in Chrome extension, limit access to trusted sites.

- If you chose to extend Claude’s default internet access settings, be careful to only extend internet access to sites you trust.

- Monitor Claude for suspicious actions that may indicate prompt injection.

- Ensure you’re using trusted MCPs (as always).

**Important:** Cowork has access to Claude in Chrome; we strongly advise against using Claude in Chrome to manage or take actions involving sensitive information. See **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely#h_044f6a88a7)** for more information about the potential risks.

Cowork activity is not captured in audit logs, Compliance API, or data exports. Do not use Cowork for regulated workloads. For more information, see Cowork for Team and Enterprise plans.

## Our safety measures

We've implemented multiple layers of protection:

- **Model training:** We use reinforcement learning to train Claude to recognize and refuse malicious instructions—even when they appear authoritative or urgent.

- **Content classifiers:** We scan all untrusted content entering Claude's context and flag potential injections before they can affect behavior.

- **Deletion protection:** Cowork requires your explicit permission before permanently deleting any files. You'll see a permission prompt and must select "Allow" before Claude can perform deletion tasks.

**Important:** While we've enacted these safety measures to reduce risks, the chances of an attack are still non-zero. Always exercise caution when using Cowork.

------------------------------------------------------------------------

## Protecting yourself from malicious attackers

**1. Be selective about file access**

You control which local files Claude can access. Since Claude can read, write, and permanently delete these files, be cautious about granting access to sensitive information like financial documents, credentials, or personal records. Consider creating a dedicated working folder for Claude rather than granting broad access, and keep backups of important files.

**2. Monitor tasks, not just commands**

Cowork executes code and commands on your behalf. While we surface what Claude is doing, you shouldn't expect to validate every individual command—instead, watch for unexpected patterns: Is Claude accessing files or websites you didn't mention? Is the task scope creeping beyond what you asked for? If something feels off, stop the task immediately.

**3. Be cautious with scheduled tasks**

Scheduled tasks run automatically, which means Claude may be working without you actively watching. Because you can't monitor these tasks in real time, take extra care when setting them up:

- **Start simple.** Begin with low-risk tasks like generating summaries or compiling information before automating anything more complex.

- **Avoid sensitive data and consequential actions.** Don't schedule tasks that access sensitive files, send messages on your behalf, make purchases, or take other actions that are difficult to undo.

- **Review outputs after each run.** Check the results of scheduled tasks regularly to make sure Claude is performing as expected. You can review past runs from the "Scheduled" page in the left sidebar.

- **Pause tasks you're not actively using.** If you no longer need a scheduled task, pause or delete it rather than leaving it running in the background.

Scheduled tasks only run while your computer is awake and the Claude Desktop app is open.

For more on setting up and managing scheduled tasks, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

**4. Limit browser and web access to trusted sources**

If you're using the Claude in Chrome extension with Cowork, limit access to sites you trust. Web content is a primary vector for prompt injection attacks—malicious instructions can be hidden in websites, emails, or documents that Claude accesses. Claude's default network access is intentionally restricted; only extend it to sites you trust.

Note that network egress permissions don't apply to the **[web search tool](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)**, which can access the broader web regardless of your network settings.

**5. Be especially cautious with unfamiliar MCPs and plugins**

Desktop extensions (MCPs) and plugins expand what Claude can do, but each one introduces new ways for attacks to reach Claude. Plugins bundle together skills, connectors, slash commands, and sub-agents into a single package, which means installing one can significantly expand Claude's scope of action.

Stick to verified extensions from the Claude Desktop directory, and carefully evaluate the permissions any extension or plugin requests before installing.

For more on plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

**6. Be mindful of cross-app data sharing**

When using the Claude in Excel and Claude in PowerPoint add-ins with Cowork, Claude can read, edit, and pass context between these applications. For example, Claude might analyze data in Excel and move a chart into a presentation—without you explicitly directing that transfer. Be aware that data from one application may flow into another during a Cowork session, and avoid working with sensitive information in these add-ins while Cowork is active.

**7. Report suspicious behavior immediately**

If Claude suddenly starts discussing unrelated topics, attempts to access unexpected resources, or requests sensitive information unprompted, stop the task and report it to [\[email protected\]](/cdn-cgi/l/email-protection#9ce9eff9eeeffdfaf9e8e5dcfdf2e8f4eef3ecf5ffb2fff3f1) or use the in-app feedback button. Your reports help us improve our defenses.

------------------------------------------------------------------------

## Your responsibility

You remain responsible for all actions taken by Claude performed on your behalf. This includes:

- Any content published or messages sent

- Purchases or financial transactions

- Data accessed or modified

- Actions taken by scheduled tasks running on your behalf

- Respecting third-party website terms of service, including any restrictions on automated access

For more information about using AI agents safely, please review our **[Acceptable Use Policy for Agents](https://support.claude.com/en/articles/12005017-using-agents-according-to-our-usage-policy)**.

------------------------------------------------------------------------

Related Articles


Installing Claude Desktop


Release notes


Get started with Cowork


Cowork for Team and Enterprise plans


Schedule recurring tasks in Cowork
