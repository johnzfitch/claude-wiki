---
title: "Code Review by Claude | AI code review tool for pull requests"
source_url: "https://www.claude.com/product/code-review"
category: "15-Claude-AI-Features"
fetched_at: "2026-11-18T06:29:36Z"
tags: ["claude-ai"]
---

# Code Review

Find bugs at the pace of agentic code

Claude automatically reviews PRs, verifies findings, and posts comments ranked by severity, so you can catch bugs before they reach production.

[Turn on Code Review](https://claude.ai/admin-settings/claude-code#code-review)[Read documentation (opens in new tab)](../02-Claude-Code-CLI/code-review.md)

Available on Claude Team and Enterprise plans with repos on GitHub. [Compare plans](../17-Billing-Plans/pricing.md#team-&-enterprise).

## Capabilities

Coding agents help teams write more code than reviewers have time to read closely. When pull requests pile up, a quick read can miss race conditions, security flaws, and other issues. Code Review reads each change closely first to help catch these before you have merged.

### Find bugs beyond the diff

Code Review reads each change and the code around it to help catch bugs a pull request exposes but didn’t cause.

### Verify findings before they post

Bugs Claude finds are checked against your code before posting, so reviewers get findings worth their time.

### Rank bugs above nits

Findings are ranked by severity and tagged Important, Nit, or Pre-existing, so serious ones are shown and can be actioned first.

### Post findings as inline comments

Findings are shared as inline comments with a summary. With reviews on every push, comments resolve once you fix them.

### Focus on what breaks production

By default, reviews look for bugs that would break production. Your team can change what gets flagged in `REVIEW.md`.

### Get findings while the change is fresh

Most reviews finish in 6 to 10 minutes, so findings are waiting by the time a reviewer opens the pull request.

## Run a review from the terminal

If you’re not an admin or not on Team or Enterprise yet, you can still run a review yourself. Ultrareview is a deeper review you start from Claude Code with the command `/code-review ultra`, on a branch or a github.com pull request. Reviewer agents look for bugs in a cloud sandbox while you keep coding, and findings are verified before you see them. Ultrareview is in research preview, and paid runs need usage credits turned on.

[Read documentation (opens in new tab)](../02-Claude-Code-CLI/ultrareview.md)

## Set where, when, and how deeply reviews run

Your team sets the rules, and merging stays with you.

Review runs

Review level

Comments

### Pick where reviews run

Run a review when a pull request opens, on every push, or only when someone asks. New repos start on every push.

### Choose repos and a review level

Pick a repo you want to review. Each starts on Standard, or set your own level: Quick for routine code, Deep for what’s critical.

### Ask for a review in a comment

Anyone with write access can comment `@claude review` on a pull request to start a review, drafts and forks included.

## Built and used by Anthropic to review code

We built Code Review to keep up with the code Claude writes. After months of daily use, it’s one part of how we handle more volume with more coverage and better quality. Our advice is to let it take a first pass on each change, so your reviewers can focus on the riskiest code. Here are the numbers from our own repos in 2026.

[Read how we review code (opens in new tab)](https://claude.dev/blog/solving-code-review-at-anthropic/)

- ### 30,000+ changes merged a day

  As of September, with Anthropic developers writing more of their code with Claude. Up from about 2,500 in May.

- ### 54% get substantive comments

  Up from 16% of our pull requests before Code Review. That’s more than three times the share, as of our research preview.

- ### 40% drop in Claude Code revert rate

  From June to September, merged pull requests more than doubled while the share we had to revert fell.

## FAQ

### What is Code Review?

Code Review is an AI code review tool that reads each GitHub pull request and posts the bugs it finds as comments for reviewers. It allows Claude, the AI technology behind Code Review, to take a first pass at code reviews. Code Review uses AI and may miss bugs, security vulnerabilities, or other issues.

### Which setups does Code Review support?

Code Review works with repos on GitHub, including GitHub Enterprise Server and GitHub Enterprise Cloud with data residency. It doesn’t support GitLab, per-user access controls, or self-hosted environments. It isn’t available to organizations with zero data retention, the HIPAA configuration, or customer-managed encryption keys.

### Do we need Claude Code to use Code Review?

No. Code Review runs on your GitHub pull requests and doesn’t require Claude Code.

### We’re not on a Team or Enterprise plan. Can Claude still review our code?

Yes. Run /code-review in a Claude Code session on any plan to review your own branch. Reviews on every pull request need a Team or Enterprise plan.

### We use Claude Code through Amazon Bedrock, Google Cloud, or Microsoft Foundry. Can we use Code Review?

Yes, with a Claude Team or Enterprise organization. Reviews run on Anthropic infrastructure and are billed by Anthropic.

### What can a review access in our repo?

Inside a review, access to your repo is read-only and nothing is pushed. The Claude GitHub App you install holds broader permissions that other Claude features share. A review reads the diff and the surrounding code without building or running it, then posts comments and a check run on the pull request. When a later push fixes a finding, the review resolves its own comment.

### How do we set up Code Review?

Setup has two steps, one in Claude and one in GitHub. In Claude, an organization owner should turn on Code Review in admin settings. In GitHub, an organization owner should install the Claude GitHub app. Next, choose which repos Code Review can review. If you don’t have owner access in either, send your contact the [setup guide](../02-Claude-Code-CLI/code-review-setup.md).

### Can we choose which models run reviews?

No. Code Review picks the models. To make reviews more or less thorough, change the review level.

### How is Code Review billed?

Code Review is billed on token usage through usage credits, separately from your plan’s included usage. Admins can set a monthly spend limit and see the average cost per review for each repo.

Blog

Solving code review at Anthropic

If Claude writes most of the code, who reviews it?

[Read more (opens in new tab)](https://claude.dev/blog/solving-code-review-at-anthropic/)

Webinar

How the Claude Code team does code review

When agents write the code, pull requests pile up faster than anyone can read them.

[Register](https://www.claude.com/resources/webinars/how-the-claude-code-team-does-code-review)

Webinar

How the Claude Code team does code review

When agents write the code, pull requests pile up faster than anyone can read them.

[Register](https://www.claude.com/resources/webinars/how-the-claude-code-team-does-code-review)

Blog

Solving code review at Anthropic

If Claude writes most of the code, who reviews it?

[Read more (opens in new tab)](https://claude.dev/blog/solving-code-review-at-anthropic/)

## See what a review finds in your code

Try it on one repo, then add more.

[Turn on Code Review](https://claude.ai/admin-settings/claude-code#code-review)[Read the setup guide (opens in new tab)](../02-Claude-Code-CLI/code-review-setup.md)
