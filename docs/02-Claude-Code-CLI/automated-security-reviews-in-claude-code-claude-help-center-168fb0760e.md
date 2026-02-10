---
category: "02-Claude-Code-CLI"
fetched_at: "2026-02-08T20:51:46Z"
source_url: "https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code"
title: "Automated Security Reviews in Claude Code | Claude Help Center"
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

[](#h_e1354dfce5)

[](#h_74eb419a31)

[](#h_da29da4277)

[](#h_be98d5bcc4)

[](#h_be5cf79b8c)

[](#h_920c1ed5b3)

[](#h_3d11a75473)

[All Collections](/en/)

[Claude Code](https://support.claude.com/en/collections/14445694-claude-code)

Automated Security Reviews in Claude Code

# Automated Security Reviews in Claude Code

Updated yesterday

Table of contents

[](#h_e1354dfce5)

[](#h_74eb419a31)

[](#h_da29da4277)

[](#h_be98d5bcc4)

[](#h_be5cf79b8c)

[](#h_920c1ed5b3)

[](#h_3d11a75473)

Claude Code now includes automated security review features to help you identify and fix vulnerabilities in your code. This guide explains how to use the /security-review command and GitHub Actions to improve your code security.

**Note:** While automated security reviews help identify many common vulnerabilities, they should complement, not replace, your existing security practices and manual code reviews.

## Overview

Automated security reviews in Claude Code help developers catch vulnerabilities before they reach production. These features check for common security issues including SQL injection risks, cross-site scripting (XSS) vulnerabilities, authentication flaws, insecure data handling, and dependency vulnerabilities.

You can use security reviews in two ways: through the /security-review command for on-demand checks in your terminal, or through GitHub Actions for automatic review of pull requests.

## Availability

These features are available for all Claude Code users, including:

- Users on individual paid plans (Pro or Max).

- Individual users or enterprises with pay-as-you-go API Console accounts.

## Using the /security-review command

The /security-review command lets you run security analysis directly from your terminal before committing code.

### Running a Security Review

To check your code for vulnerabilities:

1.  Open Claude Code in your project directory.

2.  Run /security-review in the terminal.

3.  Claude will analyze your codebase and identify potential security concerns.

4.  Review the detailed explanations provided for each issue found.

### Implementing Fixes

After Claude identifies vulnerabilities, you can ask it to implement fixes directly. This keeps security reviews integrated into your development workflow, allowing you to address issues when they're easiest to resolve.

### Customizing the Command

You can customize the /security-review command for your specific needs. See the [security review documentation](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command) for configuration options.

## Setting up GitHub Actions for automated PR reviews

After installing and configuring the GitHub action, it will automatically review every pull request for security vulnerabilities when it's opened.

### Installation

To set up automated security reviews for your repository:

1.  Navigate to your repository's GitHub Actions settings

2.  Follow the [step-by-step installation guide](https://github.com/anthropics/claude-code-security-review) in our documentation

3.  Configure the action according to your team's security requirements

### How It Works

Once configured, the GitHub action:

- Triggers automatically when new pull requests are opened.

- Reviews code changes for security vulnerabilities.

- Applies customizable filtering rules to reduce false positives.

- Posts inline comments on the PR with identified concerns and recommended fixes.

This creates a consistent security review process across your entire team, ensuring code is checked for vulnerabilities before merging.

### Customization Options

You can customize the GitHub action to match your team's security policies, including setting specific rules for your codebase and adjusting sensitivity levels for different vulnerability types.

## What security issues can be detected?

Both the /security-review command and GitHub action check for common vulnerability patterns:

- **SQL injection risks**: Identifies potential database query vulnerabilities.

- **Cross-site scripting (XSS)**: Detects client-side script injection vulnerabilities.

- **Authentication and authorization flaws**: Finds issues with access control.

- **Insecure data handling**: Identifies problems with data validation and sanitization.

- **Dependency vulnerabilities**: Checks for known issues in third-party packages.

## Getting Started

To start using automated security reviews:

- **For the /security-review command**: Update Claude Code to the latest version (run), then run `/security-review` in your project directory.

  - Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes, but you can also run `claude update` to update manually.

- **For the GitHub actions**: Visit our [documentation](https://github.com/anthropics/claude-code-security-review) for installation and configuration instructions.

## Best Practices

For optimal results, we recommend running /security-review before committing significant changes and configuring the GitHub action for all repositories containing production code. Consider adjusting the filtering rules based on your team's specific security requirements and codebase characteristics.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)

Create and edit files with Claude

[](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)

Claude Code usage analytics

[](https://support.claude.com/en/articles/12386420-claude-code-faq)

Claude Code FAQ

[](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)

Claude Code on the web

[](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)

Using Claude in Chrome Safely

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
