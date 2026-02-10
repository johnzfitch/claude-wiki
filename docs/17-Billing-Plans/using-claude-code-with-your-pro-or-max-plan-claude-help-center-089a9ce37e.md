---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:20Z"
source_url: "https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan"
title: "Using Claude Code with your Pro or Max plan | Claude Help Center"
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

[](#h_58481ca9d7)

[](#h_091d4329f6)

[](#h_a2542a08e2)

[](#h_52cf4ff05e)

[All Collections](/en/)

[Claude Code](https://support.claude.com/en/collections/14445694-claude-code)

Using Claude Code with your Pro or Max plan

# Using Claude Code with your Pro or Max plan

Updated this week

Table of contents

[](#h_58481ca9d7)

[](#h_091d4329f6)

[](#h_a2542a08e2)

[](#h_52cf4ff05e)

This article applies to individual consumers using Pro or Max plan subscriptions to access Claude Code. If you’re a member of a Team or Enterprise plan organization, see **[Using Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)**.

## What is Claude Code?

Claude Code is a command line tool that gives you access to Claude models directly in your terminal, allowing you to delegate complex coding tasks while maintaining transparency and control. With Pro and Max plans, you now have access to both Claude on the web, desktop, and mobile apps and Claude Code in your terminal with one unified subscription.

### Why use Claude and Claude Code?

Use two powerful AI products in one simple subscription.

- Use Claude for writing, research, analysis, and more — at work and at home.

- Use Claude Code for your terminal-based coding workflows.

------------------------------------------------------------------------

## How to connect Claude Code to your Pro or Max plan

1.  **Ensure you have an active Pro or Max plan subscription**

    - If you're not already subscribed, upgrade at **[claude.ai/upgrade](https://claude.ai/upgrade)**

2.  **Install Claude Code**

    - Visit the **[Claude Code page in our Claude Docs](https://code.claude.com/docs/en/overview#install-and-authenticate)** to download and install Claude Code.

    - Follow the installation instructions for your operating system.

3.  **Authenticate with your Claude credentials**

    - When prompted during setup or first use, log in with the same credentials you use for Claude.

    - This will connect your Pro or Max plan subscription to Claude Code.

    - If you're already logged in to Claude Code via Claude Console PAYG, run /login from within Claude Code to switch to your subscription plan.

### Having trouble using your Pro or Max plan to access Claude Code?

If you're not seeing the option to authenticate with your preferred account, follow these steps to update Claude Code:

1.  Log out of your active session completely using the `/logout` command.

2.  Run `claude update`.

3.  Restart your terminal completely for the change to take effect.

4.  Run `claude` and select the correct account to use Claude Code.

**Important:** If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription (Pro, Max, Team, or Enterprise plans), resulting in API usage charges rather than using your subscription's included usage. See this article for more information: **[Managing API key environment variables in Claude Code](https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code).**

------------------------------------------------------------------------

## What happens when you hit usage limits

Both Pro and Max plans offer usage limits that are shared across Claude and Claude Code, meaning all activity in both tools counts against the same usage limits. To help you monitor your usage, you will see warning messages about remaining capacity.

When you reach your usage limits, you can select from a few options based on your needs:

### Pro plan users

- Consider upgrading to the Max 5x plan if you consistently hit limits and need more capacity for larger repositories.

- **[Enable extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)** to continue using Claude with your Pro plan after hitting the included usage limit.

- You will have the flexibility to switch to **[pay-as-you-go usage](https://support.claude.com/en/articles/8114526-how-will-i-be-billed-for-claude-api-use)** with a Claude Console account for intensive coding sprints.

- Wait until your usage limits reset.

### Max plan users

- If you're on the Max 5x plan, consider upgrading to the Max 20x plan if you consistently hit limits.

- **[Enable extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)** to continue using Claude with your Max plan after hitting the included usage limit.

- You will have the flexibility to switch to **[pay-as-you-go usage](https://support.claude.com/en/articles/8114526-how-will-i-be-billed-for-claude-api-use)** with a Claude Console account for intensive coding sprints.

- Wait until your usage limits reset.

For more details on efficient usage, refer to our **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)**.

------------------------------------------------------------------------

## Claude Code billing

### Understanding two distinct systems

It's important to recognize these are separate systems:

- **Claude Code:** Presents options for continuing usage through API credits.

- **Claude Console / Claude API:** Contains optional auto-reload settings for API credit management where your terminal is located.

### Choosing to use API credits

If you want to use API credits through Claude Code:

- Usage will be billed at **[standard API rates](https://claude.com/pricing#api)** (distinct from Pro/Max Plan pricing).

- If auto-reload is enabled in your Console account, additional credits will be automatically added when your balance runs low.

### Staying within your plan

To maintain usage strictly within your Pro or Max Plan allocation:

- Decline the API credit option when presented.

- Allow your usage period to reset before continuing to use Claude Code.

- Monitor your remaining allocation using the /status command.

### Opting out of API credits for Claude Code

If you prefer to prevent the API credit option from appearing entirely:

- Run `claude logout` in your terminal.

- Run `claude login` and authenticate using only your Pro or Max plan credentials.

- Avoid adding any Claude Console credentials during the login process.

This ensures Claude Code will only use your plan allocation and you won't be prompted to use API credits when you reach your limits.

### Managing auto-reload settings

Auto-reload functionality is managed within your Claude Console account, not through Claude Code:

- Review your **[Console Billing settings](https://platform.claude.com/settings/billing)** to check auto-reload status.

- Adjust these settings in the Console if you prefer to avoid automatic credit purchases.

- Remember, auto-reload only applies when you've chosen to use API credits.

### Summary

- Claude Code maintains strict user control over billing decisions.

- All transitions to API credit usage require explicit user consent.

- Auto-reload is an independent Claude Console feature.

- To maintain your Pro or Max plan budget, simply decline API credit options when offered.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)

What is the Pro plan?

[](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage)

How do I pay for my Claude API usage?

[](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)

What is the Max plan?

[](https://support.claude.com/en/articles/12386420-claude-code-faq)

Claude Code FAQ

[](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)

Extra usage for paid Claude plans

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
