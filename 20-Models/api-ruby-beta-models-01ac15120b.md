---
category: "20-Models"
fetched_at: "2026-03-12T08:17:15Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

beta.models.list(\*\*kwargs) -\> Page\<[BetaModelInfo](/docs/en/api/beta#beta_model_info) { id, created_at, display_name, type } \>

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

beta.models.retrieve(model_id, \*\*kwargs) -\> [BetaModelInfo](/docs/en/api/beta#beta_model_info) { id, created_at, display_name, type }

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaModelInfo { id, created_at, display_name, type }

id: String

Unique model identifier.

created_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: String

A human-readable name for the model.

type: :model

Object type.

For Models, this is always `"model"`.
