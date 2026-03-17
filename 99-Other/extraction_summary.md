# Prompt Extraction Summary (2.1.39 vs 2.1.41 vs 2.1.42)

## Unique counts by category
- 2.1.39
  - system_prompts: 144
  - reminder_prompts: 260
  - warning_prompts: 1784
  - hidden_prompts: 316
  - security_mode_related: 832
- 2.1.41
  - system_prompts: 140
  - reminder_prompts: 220
  - warning_prompts: 1772
  - hidden_prompts: 332
  - security_mode_related: 996
- 2.1.42
  - system_prompts: 148
  - reminder_prompts: 224
  - warning_prompts: 1752
  - hidden_prompts: 336
  - security_mode_related: 984

## 2.1.42 secure mode activation words
- --allow-dangerously-skip-permissions
- --dangerously-skip-permissions
- --permission-mode
- --permission-prompt-tool
- --plan-mode-required
- --mode
- acceptEdits
- bypassPermissions
- default
- dontAsk
- plan
- delegate
- untrusted
- never

## Delta files
- /home/zack/claude-binary/extracted_prompts_v2/2.1.42_vs_2.1.41.*.added.txt
- /home/zack/claude-binary/extracted_prompts_v2/2.1.42_vs_2.1.41.*.removed.txt
- /home/zack/claude-binary/extracted_prompts_v2/2.1.42_vs_2.1.39.*.added.txt
- /home/zack/claude-binary/extracted_prompts_v2/2.1.42_vs_2.1.39.*.removed.txt
