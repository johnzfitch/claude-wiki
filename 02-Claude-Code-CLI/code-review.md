---
title: "Code Review - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/code-review"
category: "02-Claude-Code-CLI"
fetched_at: "2026-10-23T06:28:26Z"
tags: ["claude-code"]
---

## On this page

- [Availability](#availability)
- [Set up and use Code Review](#set-up-and-use-code-review)
- [How reviews work](#how-reviews-work)
  - [Review levels](#review-levels)
  - [What a review can access](#what-a-review-can-access)
  - [Who controls a review](#who-controls-a-review)
- [Compare ways to get a review](#compare-ways-to-get-a-review)
- [Related resources](#related-resources)

Code Review

# Code Review

Copy pageCopy page

Catch bugs in GitHub pull requests with Code Review: Claude reviews each change, verifies its findings, and comments inline. For Team and Enterprise plans

Copy pageCopy page

With Code Review, Claude reviews the pull requests in your GitHub repositories. Several agents read each change alongside the surrounding code, looking for issues such as logic errors, security vulnerabilities, or broken edge cases. A verification step checks findings against the code before they’re reported. Findings arrive as inline comments on the lines concerned, ranked by [severity](code-review-pull-requests.md#severity-levels), with a summary and a check run on the pull request. A review never approves or blocks the pull request, so the decision to merge stays with your team.

Code Review uses AI to review code and may miss bugs, security vulnerabilities, or other issues. A review with no findings doesn’t mean your code is error-free or secure.

To turn on Code Review, an Owner of your Claude organization follows [Set up Code Review](code-review-setup.md). Claude can also review code without this service. Run [`/code-review`](code-review-local.md) in your Claude Code session on any plan, or [compare all the options](#compare-ways-to-get-a-review).


[​](#availability)

Availability

Check that your organization qualifies before you set up Code Review:

- **Plans**: [Team and Enterprise](feature-availability.md)
- **Code hosts**: repositories hosted on GitHub, including [GitHub Enterprise Server](github-enterprise-server.md) and GitHub Enterprise Cloud with data residency. For data residency, have an Owner follow the [GitHub Enterprise Server admin setup](github-enterprise-server.md#admin-setup) and enter your enterprise’s `ghe.com` hostname.
- **Data retention**: Code Review isn’t available to organizations with [Zero Data Retention](zero-data-retention.md) enabled or with the [HIPAA configuration](hipaa-setup.md) applied, and isn’t covered under Anthropic’s Business Associate Agreement (BAA).
- **Encryption keys**: Code Review isn’t yet available for organizations that use customer-managed encryption keys (CMEK).
- **Cloud providers**: you need a Claude organization on one of these plans even if your developers use Claude Code through Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry


[​](#set-up-and-use-code-review)

Set up and use Code Review

Pick the page for what you need to do:

## Set up Code Review

Check the requirements, install the Claude GitHub App, and choose repositories, a review level, and when reviews run

## Customize Code Review

Tune what gets flagged with `REVIEW.md` and `CLAUDE.md` files in your repository

## Read and request reviews on a pull request

Read the findings and their severities, and request another review with a comment

## Troubleshoot Code Review

Fix a review that didn’t start, failed, or was skipped for budget

## Code Review costs and usage

See how reviews are billed, estimate spend, set the monthly spend limit, and track review activity


[​](#how-reviews-work)

How reviews work

By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage. To change what it flags, [add guidance files](code-review-customize.md) to your repository. A review runs on Anthropic infrastructure in four stages:

1.  **Find**: several agents examine the diff and the surrounding code in parallel.
2.  **Verify**: a verification step checks the candidate findings against the code and filters out false positives.
3.  **Rank**: the findings that remain are deduplicated and ranked by severity.
4.  **Post**: the review posts its results on the pull request.

Each review leaves these on the pull request:

- **Findings**: inline comments on the lines concerned, with a summary in the review body
- **A check run**: named **Claude Code Review**, with the findings listed in its [details](code-review-pull-requests.md#check-run-output). The check run doesn’t conclude as a failure.
- **When it finds nothing**: the check run’s title reads **Code review found no issues**, and Claude posts the same short note on the pull request

Code Review chooses the Claude models that reviews run on, and its admin settings don’t offer a model choice. To make reviews more or less thorough, change the [review level](#review-levels). After an Owner turns on Code Review, each repository has a setting for [when reviews run](code-review-setup.md#set-when-reviews-run): once when a pull request opens, after every push, or only on request. Whichever it is, someone with write access to the repository can comment `@claude review` on a pull request to [start a review](code-review-pull-requests.md#comment-commands).


[​](#review-levels)

Review levels

The review level sets how thorough each review is, and a more thorough review costs more:

- **Quick**: a lighter pass. The fastest level, at the lowest cost.
- **Standard**: balanced depth, speed, and cost. The default level.
- **Deep**: the most thorough pass. Takes the longest and costs the most.

An Owner [chooses one level for the organization](code-review-setup.md#set-the-default-review-level) and can give an individual repository its own, such as Quick for a routine codebase and Deep for a critical one. For what else drives the cost of each review, see [Code Review costs and usage](code-review-costs.md).


[​](#what-a-review-can-access)

What a review can access

A review reaches your repository through the Claude GitHub App that an Owner [installs during setup](code-review-setup.md#turn-on-code-review):

- **Where it runs**: on Anthropic infrastructure, in a managed environment. Reviews don’t run in [self-hosted environments](../13-Enterprise-Admin/self-hosted-environments.md).
- **What it reads and writes**: inside a review, access to your repository is read-only, and a review doesn’t push commits. On the pull request, it posts comments and the [check run](code-review-pull-requests.md#check-run-output), resolves its own earlier comment threads, and can react to a comment command with 👀. The app itself holds a [broader permission set](github-actions.md#github-app-permissions) that other Claude features share.
- **How it examines your code**: a review works from reading the diff and the surrounding code, without building or running your code.


[​](#who-controls-a-review)

Who controls a review

- **Who can start one**: where reviews run automatically, opening or pushing to a pull request starts a review, [except on drafts and forks](code-review-pull-requests.md#review-drafts-and-pull-requests-from-forks). After some pushes, Code Review [keeps the earlier result](code-review-pull-requests.md#when-a-push-keeps-the-earlier-result) instead. A [comment command](code-review-pull-requests.md#comment-commands) starts one only when it comes from a person with write access to the repository.
- **Which instructions it follows**: `REVIEW.md` from the base or default branch and [never from the pull request’s own changes](code-review-customize.md#which-branch-review-md-is-read-from).


[​](#compare-ways-to-get-a-review)

Compare ways to get a review

To find the options open to you, check the **Who can use it** column against your plan and code host:

| Option                                                                                                         | What starts a review                                                             | Where it runs                | Who can use it                                                                                                     |
|:---------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [Code Review](#how-reviews-work)                                                                               | Pull request activity, as each repository is set, or an `@claude review` comment | Anthropic infrastructure     | Organizations on a Team or Enterprise plan with GitHub repositories, once an Owner turns it on                     |
| [`/code-review`](code-review-local.md)                                                                   | You run the command on your branch                                               | Your Claude Code session     | Anyone, on any plan                                                                                                |
| [Ultrareview](ultrareview.md)                                                                            | You start it from Claude Code                                                    | A cloud sandbox              | Requires signing in with a claude.ai account. See [Ultrareview](ultrareview.md) for where it isn’t available |
| Claude in your own CI, with [GitHub Actions](github-actions.md) or [GitLab CI/CD](gitlab-ci-cd.md) | Your pipeline’s events, such as every pull request or merge request              | Your own CI runners          | Anyone with a Claude API key or cloud provider credentials, on GitHub or GitLab                                    |
| Your own reviewer, as a [subagent](../09-Agents-Patterns/sub-agents.md) or [skill](../08-Plugins-Skills/skills.md)                            | You or Claude invoke it during a session                                         | Wherever you run Claude Code | Anyone who writes one                                                                                              |


[​](#related-resources)

Related resources

- [GitHub Enterprise Server](github-enterprise-server.md): use Code Review with a self-hosted GitHub instance
- [GitHub App permissions](github-actions.md#github-app-permissions): the full permission set the Claude GitHub App requests
- [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle): how automated review fits as one layer of Anthropic’s secure development process
