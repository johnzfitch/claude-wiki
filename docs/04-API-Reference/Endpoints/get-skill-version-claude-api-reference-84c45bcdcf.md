---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:10:15Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/skills/versions/retrieve"
title: "Get Skill Version - Claude API Reference"
---

Copy page

Go

# Get Skill Version

client.Beta.Skills.Versions.Get(ctx, version, params) (\*[BetaSkillVersionGetResponse](/docs/en/api/beta#BetaSkillVersionGetResponse), error)

get/v1/skills/{skill_id}/versions/{version}

Get Skill Version

##### ParametersExpand Collapse 

version string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

params BetaSkillVersionGetParams

SkillID param.Field\[string\]

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.

Betas param.Field\[\[\]AnthropicBeta\]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"

##### ReturnsExpand Collapse 

type BetaSkillVersionGetResponse struct{…}

ID string

Unique identifier for the skill version.

The format and length of IDs may change over time.

CreatedAt string

ISO 8601 timestamp of when the skill version was created.

Description string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

Directory string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

Name string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

SkillID string

Identifier for the skill that this version belongs to.

Type string

Object type.

For Skill Versions, this is always `"skill_version"`.

Version string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Get Skill Version

Go

``` shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  version, err := client.Beta.Skills.Versions.Get(
    context.TODO(),
    "version",
    anthropic.BetaSkillVersionGetParams{
      SkillID: "skill_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", version.ID)
}
```

Response 200

``` shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
