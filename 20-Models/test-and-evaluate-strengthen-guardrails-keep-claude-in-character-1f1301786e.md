---
category: "20-Models"
fetched_at: "2026-02-07T10:05:03Z"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/keep-claude-in-character"
title: "Keep Claude in character with role prompting and prefilling - Claude API Docs"
---
# Keep Claude in character with role prompting and prefilling


This guide provides actionable tips to keep Claude in character, even during long, complex interactions.

Prefilling is deprecated and not supported on Claude Opus 4.6 and Claude Sonnet 4.5. Use [structured outputs](/docs/en/build-with-claude/structured-outputs) or system prompt instructions instead.

- **Use system prompts to set the role:** Use [system prompts](/docs/en/build-with-claude/prompt-engineering/system-prompts) to define Claude's role and personality. This sets a strong foundation for consistent responses.

  When setting up the character, provide detailed information about the personality, background, and any specific traits or quirks. This will help the model better emulate and generalize the character's traits.
- **Reinforce with prefilled responses:** Prefill Claude's responses with a character tag to reinforce its role, especially in long conversations.
- **Prepare Claude for possible scenarios:** Provide a list of common scenarios and expected responses in your prompts. This "trains" Claude to handle diverse situations without breaking character.

### Example: Enterprise chatbot for role prompting
