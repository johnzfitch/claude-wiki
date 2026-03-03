---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:06:56Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/skills/delete"
title: "Delete Skill - Claude API Reference"
---

# Delete Skill

[SkillDeleteResponse](/docs/en/api/beta#SkillDeleteResponse) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill_id}

Delete Skill

##### ParametersExpand Collapse 

SkillDeleteParams parameters

required string skillID

Unique identifier for the skill.

The format and length of IDs may change over time.

IReadOnlyList\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024_09_24

"prompt-caching-2024-07-31"PromptCaching2024_07_31

"computer-use-2024-10-22"ComputerUse2024_10_22

"computer-use-2025-01-24"ComputerUse2025_01_24

"pdfs-2024-09-25"Pdfs2024_09_25

"token-counting-2024-11-01"TokenCounting2024_11_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19

"output-128k-2025-02-19"Output128k2025_02_19

"files-api-2025-04-14"FilesApi2025_04_14

"mcp-client-2025-04-04"McpClient2025_04_04

"mcp-client-2025-11-20"McpClient2025_11_20

"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14

"code-execution-2025-05-22"CodeExecution2025_05_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11

"context-1m-2025-08-07"Context1m2025_08_07

"context-management-2025-06-27"ContextManagement2025_06_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26

"skills-2025-10-02"Skills2025_10_02

"fast-mode-2026-02-01"FastMode2026_02_01

##### ReturnsExpand Collapse 

class SkillDeleteResponse:

required string ID

Unique identifier for the skill.

The format and length of IDs may change over time.

required string Type

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

C#

``` shiki
SkillDeleteParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Delete(parameters);

Console.WriteLine(skill);
```

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
