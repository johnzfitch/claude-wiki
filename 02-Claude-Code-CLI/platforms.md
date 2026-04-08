---
source_url: "https://code.claude.com/docs/en/platforms.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Platforms and integrations

Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.

Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working.

## Where to run Claude Code

| Platform   | Best for                                          | What you get                                                             |
| :--------- | :------------------------------------------------ | :----------------------------------------------------------------------- |
| CLI        | Terminal workflows, scripting, remote servers      | Full feature set, Agent SDK, computer use on macOS, third-party providers |
| Desktop    | Visual review, parallel sessions, managed setup    | Diff viewer, app preview, computer use and Dispatch on Pro and Max       |
| VS Code    | Working inside VS Code                            | Inline diffs, integrated terminal, file context                          |
| JetBrains  | Working inside IntelliJ, PyCharm, WebStorm        | Diff viewer, selection sharing, terminal session                         |
| Web        | Long-running tasks, work that continues offline    | Anthropic-managed cloud, continues after disconnect                      |
| Mobile     | Starting and monitoring tasks away from computer   | Cloud sessions, Remote Control, Dispatch to Desktop                      |

The CLI is the most complete surface. Desktop and IDE extensions trade some CLI-only features for visual review. The web runs in Anthropic's cloud. Mobile is a thin client.

## Connect your tools

| Integration      | What it does                                    | Use it for                                        |
| :--------------- | :---------------------------------------------- | :------------------------------------------------ |
| Chrome           | Controls your browser with logged-in sessions   | Testing web apps, automating sites without API    |
| GitHub Actions   | Runs Claude in your CI pipeline                 | Automated PR reviews, issue triage                |
| GitLab CI/CD     | Same for GitLab                                 | CI-driven automation on GitLab                    |
| Code Review      | Reviews every PR automatically                  | Catching bugs before human review                 |
| Slack            | Responds to `@Claude` mentions                  | Turning bug reports into PRs from team chat       |

For integrations not listed here, MCP servers and connectors let you connect almost anything.

## Work when you are away from your terminal

|                  | Trigger                                    | Claude runs on         | Best for                                      |
| :--------------- | :----------------------------------------- | :--------------------- | :-------------------------------------------- |
| Dispatch         | Message from Claude mobile app             | Your machine (Desktop) | Delegating work while away                    |
| Remote Control   | Drive from claude.ai/code or mobile        | Your machine (CLI/VS)  | Steering in-progress work from another device |
| Channels         | Push events from chat app or your server   | Your machine (CLI)     | Reacting to external events                   |
| Slack            | Mention `@Claude` in team channel          | Anthropic cloud        | PRs and reviews from team chat                |
| Scheduled tasks  | Set a schedule                             | CLI, Desktop, or cloud | Recurring automation                          |

## See Also

- [CLI quickstart](/en/quickstart)
- [Desktop](/en/desktop)
- [VS Code](/en/vs-code)
- [JetBrains](/en/jetbrains)
- [Claude Code on the web](/en/claude-code-on-the-web)
- [Chrome](/en/chrome)
- [GitHub Actions](/en/github-actions)
- [GitLab CI/CD](/en/gitlab-ci-cd)
- [Slack](/en/slack)
- [Remote Control](/en/remote-control)
- [Channels](/en/channels)
- [Scheduled tasks](/en/scheduled-tasks)
