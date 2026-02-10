# Claude CLI command syntax error

## User

claude --allow-dangerously-skip-permissions --include-partial-messages --print --output-format=stream-json Error: Input must be provided either through stdin or as a prompt argument when using --print

--
how do I use this properly?

## Assistant

 The `--print` flag expects input. You need to either:

**Option 1: Pipe stdin**
```bash
echo "your prompt here" | claude --print --output-format=stream-json
```

**Option 2: Provide prompt as argument**
```bash
claude --print "your prompt here" --output-format=stream-json
```

**Option 3: Heredoc for multiline**
```bash
claude --print --output-format=stream-json << 'EOF'
your multiline
prompt here
EOF
```

The `--allow-dangerously-skip-permissions` and `--include-partial-messages` flags are fine, but `--print` mode requires you to provide the actual prompt content somehow.

If you're trying to start an interactive session, drop the `--print` flag entirely:
```bash
claude --allow-dangerously-skip-permissions --include-partial-messages
```

## User

`claude --allow-dangerously-skip-permissions --include-partial-messages`

## Assistant

 That command starts an interactive Claude session in your terminal with:

- `--allow-dangerously-skip-permissions`: Skips the approval prompt for tool use (computer use, bash commands, etc.)
- `--include-partial-messages`: Shows streaming partial responses as they're generated

Once you run it, you'll get an interactive prompt where you can type messages directly and Claude will respond in real-time with tool execution happening automatically without confirmation.

Just run:
```bash
claude --allow-dangerously-skip-permissions --include-partial-messages
```

Then start typing your prompts at the interactive prompt that appears.

If you want to pipe the output somewhere or need non-interactive mode for scripting, that's when you'd use `--print` with a prompt argument or stdin.

## User

How should I update to latest version w/ max dev option

## Assistant

 ```bash
# Update codex CLI (Rust version - recommended)
cargo install codex-cli --force

# Or if you're on the TypeScript version
npm install -g @anthropic-ai/claude-cli@latest
```

For max dev options, your command becomes:
```bash
claude \
  --allow-dangerously-skip-permissions \
  --include-partial-messages \
  --dangerously-force-approve-all-commands \
  --max-tokens 8192
```

Or if you want this as default, add to your shell config (`~/.zshrc` or `~/.bashrc`):
```bash
alias claudedev='claude --allow-dangerously-skip-permissions --include-partial-messages --dangerously-force-approve-all-commands --max-tokens 8192'
```

The Rust version (codex-cli) is now the default and has better performance. If you're still on the TypeScript version and want to switch:
```bash
npm uninstall -g @anthropic-ai/claude-cli
cargo install codex-cli
```

Check version after install:
```bash
claude --version
```
