---
title: "Run prompts on a schedule"
source_url: "https://code.claude.com/docs/en/scheduled-tasks.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
tags: ["claude-code", "prompting"]
---

# Run prompts on a schedule

Use /loop and the cron scheduling tools to run prompts repeatedly, poll for status, or set one-time reminders within a Claude Code session.

> Scheduled tasks require Claude Code v2.1.72 or later.

Scheduled tasks let Claude re-run a prompt automatically on an interval. Use them to poll a deployment, babysit a PR, check back on a long-running build, or remind yourself to do something later.

Tasks are session-scoped: they live in the current Claude Code process and are gone when you exit. For durable scheduling, use Cloud or Desktop scheduled tasks, or GitHub Actions.

## Compare scheduling options

|                            | Cloud              | Desktop            | `/loop`            |
| :------------------------- | :----------------- | :----------------- | :----------------- |
| Runs on                    | Anthropic cloud    | Your machine       | Your machine       |
| Requires machine on        | No                 | Yes                | Yes                |
| Requires open session      | No                 | No                 | Yes                |
| Persistent across restarts | Yes                | Yes                | No                 |
| Access to local files      | No (fresh clone)   | Yes                | Yes                |
| Minimum interval           | 1 hour             | 1 minute           | 1 minute           |

## Schedule a recurring prompt with /loop

```
/loop 5m check if the deployment finished and tell me what happened
```

### Interval syntax

| Form                    | Example                               | Parsed interval              |
| :---------------------- | :------------------------------------ | :--------------------------- |
| Leading token           | `/loop 30m check the build`           | every 30 minutes             |
| Trailing `every` clause | `/loop check the build every 2 hours` | every 2 hours                |
| No interval             | `/loop check the build`               | defaults to every 10 minutes |

Supported units: `s` (seconds), `m` (minutes), `h` (hours), `d` (days). Seconds are rounded up to nearest minute.

### Loop over another command

```
/loop 20m /review-pr 1234
```

## Set a one-time reminder

```
remind me at 3pm to push the release branch
```

```
in 45 minutes, check whether the integration tests passed
```

## Manage scheduled tasks

```
what scheduled tasks do I have?
cancel the deploy check job
```

| Tool         | Purpose                                   |
| :----------- | :---------------------------------------- |
| `CronCreate` | Schedule a new task                       |
| `CronList`   | List all scheduled tasks                  |
| `CronDelete` | Cancel a task by ID                       |

Each task has an 8-character ID. A session can hold up to 50 scheduled tasks.

## How scheduled tasks run

The scheduler checks every second for due tasks and enqueues them at low priority. A scheduled prompt fires between your turns, not while Claude is mid-response. All times are in your local timezone.

### Jitter

- Recurring tasks fire up to 10% of their period late, capped at 15 minutes
- One-shot tasks at top/bottom of hour fire up to 90 seconds early

### Seven-day expiry

Recurring tasks automatically expire 7 days after creation.

## Cron expression reference

`CronCreate` accepts standard 5-field cron expressions: `minute hour day-of-month month day-of-week`.

| Example        | Meaning                      |
| :------------- | :--------------------------- |
| `*/5 * * * *`  | Every 5 minutes              |
| `0 * * * *`    | Every hour on the hour       |
| `0 9 * * *`    | Every day at 9am local       |
| `0 9 * * 1-5`  | Weekdays at 9am local        |

## Disable scheduled tasks

Set `CLAUDE_CODE_DISABLE_CRON=1` in your environment to disable the scheduler entirely.

## Limitations

- Tasks only fire while Claude Code is running and idle
- No catch-up for missed fires
- No persistence across restarts

## See Also

- [Cloud scheduled tasks](web-scheduled-tasks.md)
- [Desktop scheduled tasks](../16-Mobile-Desktop/desktop-scheduled-tasks.md)
- [GitHub Actions](/en/github-actions)
