---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:07:27Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/skills"
title: "Skills - Claude API Reference"
---

Copy page

TypeScript

# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

client.beta.skills.create(SkillCreateParams { display_title, files, betas } params?, RequestOptionsoptions?): [SkillCreateResponse](/docs/en/api/beta#skill_create_response) { id, created_at, display_title, 4 more }

post/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

client.beta.skills.list(SkillListParams { limit, page, source, betas } params?, RequestOptionsoptions?): PageCursor\<[SkillListResponse](/docs/en/api/beta#skill_list_response) { id, created_at, display_title, 4 more } \>

get/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

client.beta.skills.retrieve(stringskillID, SkillRetrieveParams { betas } params?, RequestOptionsoptions?): [SkillRetrieveResponse](/docs/en/api/beta#skill_retrieve_response) { id, created_at, display_title, 4 more }

get/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

client.beta.skills.delete(stringskillID, SkillDeleteParams { betas } params?, RequestOptionsoptions?): [SkillDeleteResponse](/docs/en/api/beta#skill_delete_response) { id, type }

delete/v1/skills/{skill_id}

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

client.beta.skills.versions.create(stringskillID, VersionCreateParams { files, betas } params?, RequestOptionsoptions?): [VersionCreateResponse](/docs/en/api/beta#version_create_response) { id, created_at, description, 5 more }

post/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

client.beta.skills.versions.list(stringskillID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor\<[VersionListResponse](/docs/en/api/beta#version_list_response) { id, created_at, description, 5 more } \>

get/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill_id, betas } params, RequestOptionsoptions?): [VersionRetrieveResponse](/docs/en/api/beta#version_retrieve_response) { id, created_at, description, 5 more }

get/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

client.beta.skills.versions.delete(stringversion, VersionDeleteParams { skill_id, betas } params, RequestOptionsoptions?): [VersionDeleteResponse](/docs/en/api/beta#version_delete_response) { id, type }

delete/v1/skills/{skill_id}/versions/{version}

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
