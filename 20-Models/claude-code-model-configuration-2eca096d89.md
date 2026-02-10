---
category: "20-Models"
source_url: "https://support.claude.com/en/articles/11940350-claude-code-model-configuration"
---


This guide shows you three ways to change which Claude model you're using with Claude Code: the quick /model command for instant changes, the --model flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

 

Easiest Method: Use /model Command

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

Start Claude Code: claude

Type /model and choose your desired model from the interactive menu.

Your model change takes effect immediately.

Note: You can check your current model anytime by running /status in Claude Code.

Supported Models

Opus 4.5, claude-opus-4-5-20251101

Haiku 4.5, claude-haiku-4-5-20251001

Sonnet 4.5, claude-sonnet-4-5-20250929 (default)

Sonnet 4, claude-sonnet-4-20250514

Haiku 3.5, claude-3-5-haiku-20241022

⚠️ Model Access: When using a Pro plan with Claude Code, you will only be able to use Opus models after enabling and purchasing extra usage.

Change model for current session only

Use the --model flag when starting Claude Code. 

Start a fresh Terminal session.

Enter the following commands (depending on the model you’d like to use for that session):

For Opus 4.5: claude --model claude-opus-4-5-20251101

For Haiku 4.5: claude --model claude-haiku-4-5-20251001

For Sonnet 4.5: claude --model claude-sonnet-4-5-20250929

For Sonnet 4: claude --model claude-sonnet-4-20250514

For 3.5 Haiku: claude --model claude-3-5-haiku-20241022

 

Change default model for all future sessions 

Step 1) Check your shell type by running: echo $SHELL

/bin/zsh → You're using zsh (macOS default)

/bin/bash → You're using bash (Linux default)

Step 2) Add model setting to your shell config:

 

For ZSH users (macOS)

Opus 4.5: echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc

Haiku 4.5: echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.zshrc

Sonnet 4.5: echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.zshrc

Sonnet 4: echo 'export ANTHROPIC_MODEL="claude-sonnet-4-20250514"' >> ~/.zshrc

3.5 Haiku: echo 'export ANTHROPIC_MODEL="claude-3-5-haiku-20241022"' >> ~/.zshrc

For BASH users (Linux)

Opus 4.5: echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.bashrc

Haiku 4.5: echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.bashrc

Sonnet 4.5: echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.bashrc

Sonnet 4: echo 'export ANTHROPIC_MODEL="claude-sonnet-4-20250514"' >> ~/.bashrc

3.5 Haiku: echo 'export ANTHROPIC_MODEL="claude-3-5-haiku-20241022"' >> ~/.bashrc 

Step 3) Apply the changes:

For ZSH: source ~/.zshrc

For BASH: source ~/.bashrc

Step 4) Close Terminal completely, then reopen it.

 

Step 5) Start Claude Code in a fresh Terminal session: claude.

 

Now your chosen model will be the default for all future Claude Code sessions.

Related Articles
How up-to-date is Claude's training data?
Release Notes
Claude in Chrome Release Notes
Using Claude in Microsoft Foundry
Applying Claude Opus 4.5’s strengths to your everyday work