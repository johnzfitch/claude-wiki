---
category: "99-Other"
fetched_at: "2026-02-10T10:49:27Z"
source_url: "https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code"
title: "Managing API key environment variables in Claude Code | Claude Help Center"
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

[](#h_7322aad2c3)

[](#h_dcadaffa24)

[](#h_804d6f7f6a)

[](#h_2a867e8983)

[](#h_4adf2119d7)

[](#h_a1d0fd399e)

[](#h_93fc3d36f7)

[](#h_11d98ff8ef)

[](#h_5c189539d9)

[All Collections](/en/)

[Claude Code](https://support.claude.com/en/collections/14445694-claude-code)

Managing API key environment variables in Claude Code

# Managing API key environment variables in Claude Code

Updated this week

Table of contents

[](#h_7322aad2c3)

[](#h_dcadaffa24)

[](#h_804d6f7f6a)

[](#h_2a867e8983)

[](#h_4adf2119d7)

[](#h_a1d0fd399e)

[](#h_93fc3d36f7)

[](#h_11d98ff8ef)

[](#h_5c189539d9)

## Understanding authentication priority in Claude Code

When using Claude Code, it's important to understand how authentication methods are prioritized to avoid unexpected API charges and ensure you're using your intended account.

## How authentication works

- Claude Code prioritizes environment variable API keys over authenticated subscriptions.

- This is intentional behavior designed to give you flexibility in choosing your authentication method.

- When an API key is set as an environment variable, you'll be charged via API pay-as-you-go rates using the API account associated with that key.

- This happens even if you're logged into Claude Code with a claude.ai subscription or a different Console account.

## Best practices

**To use Claude Code with your Claude subscription:** Keep the ANTHROPIC_API_KEY environment variable unset.

- This prevents unexpected API charges and ensures you're using your subscription's included usage.

- If you need to use a specific API key occasionally, set it temporarily only when needed.

- Run /status in Claude Code periodically to verify your current authentication method.

## Authentication conflict warnings

Claude Code will notify you when there's a conflict between your authenticated subscription and an environment variable API key:

1.  During initial setup, if an API key is detected in your environment variables, Claude Code will ask you to confirm which authentication method you want to use.

2.  After successful login, you'll see a notification if both credentials are active, alerting you to the potential for unexpected API charges.

## Checking your current configuration

To verify if an API key is set as an environment variable, run /status in Claude Code. This will show you which authentication method is currently active.

To check your environment variable directly, run one of these commands in a terminal (outside of Claude Code):

macOS/Linux:

    echo $ANTHROPIC_API_KEY

Windows CMD:

    echo %ANTHROPIC_API_KEY%

Windows PowerShell:

    echo $env:ANTHROPIC_API_KEY

## Setting an API key temporarily

If you need to use an API key for the current terminal session only:

macOS/Linux:

    export ANTHROPIC_API_KEY='your-api-key-here'

Windows CMD:

    set ANTHROPIC_API_KEY=your-api-key-here

Windows PowerShell:

    $env:ANTHROPIC_API_KEY="your-api-key-here"

## Setting an API key environment variable permanently

macOS/Linux:

    For zsh (default on macOS):
    bash
    # Add to shell config file
    echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc

    # Apply changes
    source ~/.zshrc
    For bash:
    bash
    # Add to shell config file
    echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bash_profile

    # Apply changes
    source ~/.bash_profile

Windows:

1.  Open System Properties → Advanced → Environment Variables

2.  Under "User variables", click "New"

3.  Variable name: ANTHROPIC_API_KEY

4.  Variable value: your-api-key-here

5.  Click OK and restart your terminal

## Removing an API key environment variable

macOS/Linux (temporary):

    unset ANTHROPIC_API_KEY

macOS (permanent):

    # Remove from config file
    sed -i '' '/ANTHROPIC_API_KEY/d' ~/.zshrc
    source ~/.zshrc

Linux (permanent)

    sed -i '/ANTHROPIC_API_KEY/d' ~/.zshrc

Windows CMD:

    set ANTHROPIC_API_KEY=

Windows PowerShell:

    Remove-Item Env:ANTHROPIC_API_KEY

Windows (permanent): Delete the variable from System Environment Variables settings.

## Common issues to avoid

- Setting environment variables in shell configuration files and forgetting about them.

- Not restarting your terminal after changing environment variables.

- Assuming you're using your subscription when an API key is configured in your environment.

If you have any questions, please [contact our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support).

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure)

API Key Best Practices: Keeping Your Keys Safe and Secure

[](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)

Using Claude Code with your Pro or Max plan

[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)

Claude Code model configuration

[](https://support.claude.com/en/articles/12386420-claude-code-faq)

Claude Code FAQ

[](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)

Claude Code on the web

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
