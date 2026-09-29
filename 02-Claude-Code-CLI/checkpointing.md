---
title: "Checkpointing - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/checkpointing"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-26T06:37:53Z"
tags: ["claude-code"]
---

## On this page

- [How checkpoints work](#how-checkpoints-work)
  - [Automatic tracking](#automatic-tracking)
  - [Rewind and summarize](#rewind-and-summarize)
  - [Rewind past a cleared conversation](#rewind-past-a-cleared-conversation)
  - [Guide a summary](#guide-a-summary)
- [Common use cases](#common-use-cases)
- [Limitations](#limitations)
  - [Bash command changes not tracked](#bash-command-changes-not-tracked)
  - [Subagent edits not restored](#subagent-edits-not-restored)
  - [External changes not tracked](#external-changes-not-tracked)
  - [Messages sent mid-turn not checkpointed](#messages-sent-mid-turn-not-checkpointed)
  - [Symlinked and hard-linked paths not restored](#symlinked-and-hard-linked-paths-not-restored)
  - [Not a replacement for version control](#not-a-replacement-for-version-control)
- [See also](#see-also)

Reference

# Checkpointing

Copy pageCopy page

Track, rewind, and summarize Claude’s edits and conversation to manage session state.

Copy pageCopy page

Claude Code automatically tracks Claude’s file edits as you work, allowing you to quickly undo changes and rewind to previous states if anything gets off track.


[​](#how-checkpoints-work)

How checkpoints work

As you work with Claude, checkpointing automatically captures the state of your code before each prompt you send that starts a turn.


[​](#automatic-tracking)

Automatic tracking

Claude Code tracks all changes made by its file editing tools:

- Every prompt you send that starts a turn creates a new checkpoint
- Claude Code keeps file snapshots for the 100 most recent checkpoints in a session. Discarding an older checkpoint deletes the snapshot files that no remaining checkpoint references, except each file’s first snapshot, which the VS Code extension uses as the baseline for its session diffs.
- Claude Code saves checkpoints with the conversation, so you can still run `/rewind` after you resume a session
- Claude Code deletes a session’s file snapshots in the [retention sweep](claude-directory.md#cleaned-up-automatically), by default about 30 days after the session last saved one. Rewinding to a checkpoint whose snapshots are gone can fail with [`No files were restored`](errors.md#no-files-were-restored). To keep snapshots longer, set [`cleanupPeriodDays`](settings-reference.md#cleanupperioddays).


[​](#rewind-and-summarize)

Rewind and summarize

Run `/rewind`, or press `Esc` twice when the prompt input is empty, to open the rewind menu.

If the prompt input contains text, double `Esc` clears it instead of opening the menu. The cleared text is saved to your input history, so press `Up` to recall it after you finish in the rewind menu.

The rewind menu lists each prompt you sent during the session, except [messages that joined a running turn](#messages-sent-mid-turn-not-checkpointed). Select the point you want to act on, then choose an action:

- **Restore code and conversation**: revert both code and conversation to that point
- **Restore conversation**: rewind to that message while keeping current code
- **Restore code**: revert file changes while keeping the conversation
- **Summarize from here**: compress the conversation from this point forward into a summary, freeing context window space
- **Summarize up to here**: compress the conversation before this point into a summary, keeping later messages intact
- **Never mind**: return to the message list without making changes

The two code restore options appear only when the selected checkpoint has tracked file changes to revert. If no file edits were captured after that point, the menu offers only **Restore conversation**, the summarize options, and **Never mind**. After restoring the conversation or choosing Summarize from here, the original prompt from the selected message is restored into the input field so you can re-send or edit it. Choosing Summarize up to here leaves you at the end of the conversation with the input empty. With either summarize option, a **Summarized conversation** marker appears in the conversation where the compressed messages were.


[​](#rewind-past-a-cleared-conversation)

Rewind past a cleared conversation

If you ran `/clear` earlier in the same Claude Code process, the rewind menu shows an additional entry at the top of the list labeled `/resume <session-id> (previous session)`. Select it to resume the conversation that was active before `/clear` ran. The entry is available until you exit Claude Code or resume a different session.


[​](#guide-a-summary)

Guide a summary

Summarizing doesn’t change files on disk, and the original messages stay in the session transcript, so Claude can still reference the details. To guide what the summary focuses on, highlight a **Summarize** option with the arrow keys and type instructions where the row reads **add context (optional)**, then press `Enter`. Selecting the option with its number key summarizes immediately without instructions.

Summarize keeps you in the same session and compresses context, like a targeted `/compact`. To branch off and try a different approach while preserving the original session intact, use [`/branch`](sessions.md#branch-a-session) or `claude --continue --fork-session` instead.


[​](#common-use-cases)

Common use cases

Checkpoints are particularly useful when:

- **Exploring alternatives**: try different implementation approaches without losing your starting point
- **Recovering from mistakes**: quickly undo changes that introduced bugs or broke functionality
- **Iterating on features**: experiment with variations knowing you can revert to working states
- **Freeing context space**: summarize a verbose debugging session from the midpoint forward, keeping your initial instructions intact


[​](#limitations)

Limitations


[​](#bash-command-changes-not-tracked)

Bash command changes not tracked

Checkpointing does not track files modified by Bash commands. For example, if Claude Code runs:

```python
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt
```

These file modifications cannot be undone through rewind. Only direct file edits made through Claude’s file editing tools are tracked.


[​](#subagent-edits-not-restored)

Subagent edits not restored

A [subagent](../09-Agents-Patterns/sub-agents.md) makes edits with Claude’s file editing tools, but Claude Code usually doesn’t capture those edits in your session’s checkpoints. Whether rewinding restores them depends on how the subagent runs:

- **Foreground forked skill**: a [skill with `context: fork`](../08-Plugins-Skills/skills.md#run-skills-in-a-subagent) that runs in the foreground edits your working tree during your own turn, so rewinding restores its edits as usual. Set `background: false` to run a fork in the foreground; a few situations, [listed on the skills page](../08-Plugins-Skills/skills.md#run-skills-in-a-subagent), run it there regardless of the setting.
- **Any other subagent**: rewinding doesn’t restore the edits. Use git to revert them. This includes a forked skill that runs in the background, the default, and a background [`/code-review --fix`](code-review.md) run.


[​](#external-changes-not-tracked)

External changes not tracked

Checkpointing only tracks files that have been edited within the current session. Manual changes you make to files outside of Claude Code and edits from other concurrent sessions are normally not captured, unless they happen to modify the same files as the current session.


[​](#messages-sent-mid-turn-not-checkpointed)

Messages sent mid-turn not checkpointed

When a message you [queue while Claude works](interactive-mode.md#queue-messages-while-claude-works) reaches Claude within the running turn, it joins that turn instead of starting a new one. The message appears in the conversation, but Claude Code doesn’t create a checkpoint for it, and the rewind menu doesn’t list it. A queued message that Claude Code sends as part of a new turn gets a checkpoint as usual, including when several queued messages [share that turn](interactive-mode.md#when-claude-code-sends-what-you-queued). To remove such a message, or undo the edits Claude made after it, rewind to the prompt that started the turn. That rewinds the whole turn, including the work Claude did before your message arrived.


[​](#symlinked-and-hard-linked-paths-not-restored)

Symlinked and hard-linked paths not restored

Checkpointing doesn’t rewind symlinked or hard-linked files. When you pick **Restore code** or **Restore code and conversation** from the `/rewind` menu, Claude Code skips any tracked path that is a symlink or hard link and shows a `Restored the code, but skipped N files` warning. The skipped files keep their current contents. To undo the session’s changes to one of them, ask Claude to reverse the edit or edit the file yourself. Config files a dotfile manager symlinks into your project and files pnpm hard-links into place both fall into this category. To see which paths a restore skips, turn on debug logging with `/debug` before you restore: the debug log at `~/.claude/debug/<session-id>.txt` names each skipped path. For every skip reason and the recovery steps, see [the skipped-files entry in the error reference](errors.md#restored-the-code-but-skipped-files).


[​](#not-a-replacement-for-version-control)

Not a replacement for version control

Checkpoints are designed for quick, session-level recovery. For permanent version history and collaboration, continue using version control, such as Git, for commits, branches, and long-term history.


[​](#see-also)

See also

- [Interactive mode](interactive-mode.md) - Keyboard shortcuts and session controls
- [Commands](commands.md) - Accessing checkpoints using `/rewind`
- [CLI reference](cli-reference.md) - Command-line options
