---
title: "Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rate_limits"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:23Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Rate Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

##### Models



OrganizationRateLimit object{ type: "rate_limit", id, group, 2 more }





OrganizationRateLimitBatchGroup object{ type: "batch", id }





type: "batch"



Always `batch`: the Message Batches API.

defaultbatch

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitFilesGroup object{ type: "files", id }





type: "files"



Always `files`: the Files API.

defaultfiles

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitModelGroup object{ type: "model_group", id, display_name }





type: "model_group"



Always `model_group`: a family of models.

defaultmodel_group

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

display_name: string



Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.



OrganizationRateLimitSkillsGroup object{ type: "skills", id }





type: "skills"



Always `skills`: the Skills API.

defaultskills

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitTokenCountGroup object{ type: "token_count", id }





type: "token_count"



Always `token_count`: the Token Count API.

defaulttoken_count

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.



OrganizationRateLimitValue object{ type, value }



type: string



The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number



The configured limit value for this limiter type.



OrganizationRateLimitWebSearchGroup object{ type: "web_search", id }





type: "web_search"



Always `web_search`: the Messages API web search tool.

defaultweb_search

id: string



Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.
