---
source_url: "https://code.claude.com/docs/en/computer-use.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Let Claude use your computer from the CLI

Enable computer use in the Claude Code CLI so Claude can open apps, click, type, and see your screen on macOS. Test native apps, debug visual issues, and automate GUI-only tools without leaving your terminal.

> Computer use is a research preview on macOS that requires a Pro or Max plan. It requires Claude Code v2.1.85 or later and an interactive session (not available with `-p` flag).

Computer use lets Claude open apps, control your screen, and work on your machine the way you would. From the CLI, Claude can compile a Swift app, launch it, click through every button, and screenshot the result.

## What you can do

- **Build and validate native apps**: write Swift, compile, launch, and click through controls to verify
- **End-to-end UI testing**: open an Electron app, click through signup, screenshot each step
- **Debug visual and layout issues**: resize windows, reproduce bugs, patch CSS, verify fixes
- **Drive GUI-only tools**: interact with design tools, hardware control panels, iOS Simulator

## When computer use applies

Claude tries the most precise tool first:

1. MCP server for the service
2. Bash for shell commands
3. Claude in Chrome for browser work
4. Computer use for everything else (native apps, simulators, tools without APIs)

## Enable computer use

1. Run `/mcp` in an interactive session
2. Find `computer-use` and select **Enable**
3. Grant macOS permissions:
   - **Accessibility**: lets Claude click, type, and scroll
   - **Screen Recording**: lets Claude see your screen

## Approve apps per session

The first time Claude needs a specific app in a session, a prompt appears showing which apps Claude wants to control. Choose **Allow for this session** or **Deny**.

Apps with broad reach show extra warnings:

| Warning                    | Applies to                           |
| :------------------------- | :----------------------------------- |
| Equivalent to shell access | Terminal, iTerm, VS Code, Warp       |
| Can read or write any file | Finder                               |
| Can change system settings | System Settings                      |

## How Claude works on your screen

- **One session at a time**: machine-wide lock while active
- **Apps hidden during use**: other apps are hidden so Claude interacts only with approved apps
- **Terminal excluded from screenshots**: Claude never sees its own output
- **Stop at any time**: press `Esc` anywhere or `Ctrl+C` in terminal

## Safety

- **Per-app approval**: Claude only controls approved apps
- **Sentinel warnings**: apps with shell/filesystem/system access are flagged
- **Global escape**: `Esc` key aborts computer use immediately
- **Lock file**: only one session can control your machine at a time

## Differences from Desktop app

| Feature              | Desktop                                       | CLI                             |
| :------------------- | :-------------------------------------------- | :------------------------------ |
| Platforms            | macOS and Windows                             | macOS only                      |
| Enable               | Toggle in Settings > General                  | Enable `computer-use` in `/mcp` |
| Denied apps list     | Configurable in Settings                      | Not yet available               |

## Troubleshooting

- **"Computer use is in use by another session"**: finish or exit the other session
- **macOS permissions prompt keeps reappearing**: quit Claude Code completely and restart
- **`computer-use` doesn't appear in `/mcp`**: check macOS, v2.1.85+, Pro/Max plan, claude.ai auth

## See Also

- [Computer use in Desktop](/en/desktop#let-claude-use-your-computer)
- [Claude in Chrome](/en/chrome)
- [MCP](/en/mcp)
- [Sandboxing](/en/sandboxing)
