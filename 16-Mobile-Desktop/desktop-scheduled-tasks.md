---
source_url: "https://code.claude.com/docs/en/desktop-scheduled-tasks.md"
category: "16-Mobile-Desktop"
fetched_at: "2026-04-08"
---

# Schedule recurring tasks in Claude Code Desktop

Set up scheduled tasks in Claude Code Desktop to run Claude automatically on a recurring basis for daily code reviews, dependency audits, or morning briefings.

By default, scheduled tasks start a new session automatically at a time and frequency you choose.

## Compare scheduling options

|                            | Cloud              | Desktop            | `/loop`            |
| :------------------------- | :----------------- | :----------------- | :----------------- |
| Runs on                    | Anthropic cloud    | Your machine       | Your machine       |
| Requires machine on        | No                 | Yes                | Yes                |
| Requires open session      | No                 | No                 | Yes                |
| Persistent across restarts | Yes                | Yes                | No                 |
| Access to local files      | No (fresh clone)   | Yes                | Yes                |
| Minimum interval           | 1 hour             | 1 minute           | 1 minute           |

The Schedule page supports two kinds of tasks:

- **Local tasks**: run on your machine with direct access to local files and tools. Desktop app must be open and computer awake.
- **Remote tasks**: run on Anthropic-managed cloud infrastructure. Keep running even when your computer is off.

## Create a scheduled task

Click **Schedule** in the sidebar, click **New task**, and choose **New local task**. Configure:

| Field       | Description                                               |
| ----------- | --------------------------------------------------------- |
| Name        | Identifier for the task (lowercase kebab-case)            |
| Description | Short summary shown in the task list                      |
| Prompt      | Instructions sent to Claude when the task runs            |
| Frequency   | How often the task runs                                   |

## Frequency options

- **Manual**: no schedule, only runs when you click **Run now**
- **Hourly**: runs every hour with a fixed offset of up to 10 minutes
- **Daily**: shows a time picker, defaults to 9:00 AM local
- **Weekdays**: same as Daily but skips Saturday and Sunday
- **Weekly**: shows a time and day picker

For custom intervals, ask Claude in any Desktop session.

## How scheduled tasks run

Desktop checks the schedule every minute while the app is open and starts a fresh session when a task is due. Each task gets a fixed delay of up to 10 minutes for staggering.

When a task fires:
- Desktop notification appears
- New session under **Scheduled** section in sidebar
- Claude can edit files, run commands, create commits, open PRs

Tasks only run while the desktop app is running and your computer is awake. Enable **Keep computer awake** in Settings to prevent idle-sleep.

## Missed runs

When the app starts or your computer wakes, Desktop checks whether each task missed any runs in the last seven days. If it did, exactly one catch-up run starts for the most recently missed time.

## Permissions for scheduled tasks

Each task has its own permission mode. Allow rules from `~/.claude/settings.json` also apply.

To avoid stalls, click **Run now** after creating a task, watch for permission prompts, and select "always allow" for each one.

## Manage scheduled tasks

From a task's detail page:

- **Run now**: start immediately
- **Toggle repeats**: pause/resume scheduled runs
- **Edit**: change prompt, frequency, folder, or settings
- **Review history**: see past runs
- **Review allowed permissions**: see and revoke tool approvals
- **Delete**: remove the task

Task prompts on disk: `~/.claude/scheduled-tasks/<task-name>/SKILL.md`

## See Also

- [Cloud scheduled tasks](/en/web-scheduled-tasks)
- [Run prompts on a schedule](/en/scheduled-tasks) — session-scoped `/loop`
- [Claude Code GitHub Actions](/en/github-actions)
- [Use Claude Code Desktop](/en/desktop)
