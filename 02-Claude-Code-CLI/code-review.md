---
title: "Code Review"
source_url: "https://code.claude.com/docs/en/code-review.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
tags: ["claude-code"]
---

# Code Review

Set up automated PR reviews that catch logic errors, security vulnerabilities, and regressions using multi-agent analysis of your full codebase.

> Code Review is in research preview, available for Team and Enterprise subscriptions. Not available for organizations with Zero Data Retention enabled.

Code Review analyzes your GitHub pull requests and posts findings as inline comments on the lines of code where it found issues. A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and subtle regressions.

Findings are tagged by severity and don't approve or block your PR, so existing review workflows stay intact.

## How reviews work

Reviews trigger when a PR opens, on every push, or when manually requested. When a review runs, multiple agents analyze the diff and surrounding code in parallel on Anthropic infrastructure. Results are deduplicated, ranked by severity, and posted as inline comments.

### Severity levels

| Marker | Severity     | Meaning                                                |
| :----- | :----------- | :----------------------------------------------------- |
| 🔴     | Important    | A bug that should be fixed before merging              |
| 🟡     | Nit          | A minor issue, worth fixing but not blocking           |
| 🟣     | Pre-existing | A bug in the codebase not introduced by this PR        |

### Rate and reply to findings

Each comment arrives with 👍 and 👎 already attached for one-click rating. Anthropic collects reactions after merge to tune the reviewer. Replying to an inline comment does not prompt Claude to respond.

### Check run output

Each review populates the **Claude Code Review** check run. The check run always completes with a neutral conclusion so it never blocks merging.

Machine-readable severity data:

```bash
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
```

## Set up Code Review

1. Go to claude.ai/admin-settings/claude-code → Code Review section
2. Click **Setup** → Install Claude GitHub App
3. Select repositories to enable
4. Set review triggers per repo:
   - **Once after PR creation**: review runs once when PR opens
   - **After every push**: review runs on every push
   - **Manual**: reviews start only with `@claude review`

## Manually trigger reviews

| Command               | What it does                                                    |
| :-------------------- | :-------------------------------------------------------------- |
| `@claude review`      | Starts review and subscribes PR to push-triggered reviews       |
| `@claude review once` | Starts a single review without subscribing to future pushes     |

Post as a top-level PR comment. Requires owner, member, or collaborator access.

## Customize reviews

### CLAUDE.md

Code Review reads your repository's `CLAUDE.md` files and treats newly-introduced violations as nit-level findings.

### REVIEW.md

Add a `REVIEW.md` file to your repository root for review-specific rules:

```markdown
# Code Review Guidelines

## Always check
- New API endpoints have corresponding integration tests
- Database migrations are backward-compatible
- Error messages don't leak internal details to users

## Skip
- Generated files under `src/gen/`
- Formatting-only changes in `*.lock` files
```

## Pricing

Each review averages $15-25 in cost, scaling with PR size and complexity. Billed separately through extra usage.

## Troubleshooting

### Retrigger a failed review

Comment `@claude review once` on the PR. The **Re-run** button in GitHub's Checks tab does not retrigger Code Review.

### Find issues not showing as inline comments

Check: Details in the check run, Files changed annotations, or Review body under "Additional findings".

## See Also

- [GitHub Actions](claude-code-github-actions-claude-code-docs-0d633fbd8a.md)
- [GitLab CI/CD](claude-code-gitlab-ci-cd-claude-code-docs-fbcd915fee.md)
- [Memory](how-claude-remembers-your-project-claude-code-docs-f1c064262d.md) — How `CLAUDE.md` files work
