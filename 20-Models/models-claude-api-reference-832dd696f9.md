---
category: "20-Models"
fetched_at: "2026-03-03T15:03:47Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

models.list(\*\*kwargs) -\> Page\<[ModelInfo](/docs/en/api/models#model_info) { id, created_at, display_name, type } \>

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

models.retrieve(model_id, \*\*kwargs) -\> [ModelInfo](/docs/en/api/models#model_info) { id, created_at, display_name, type }

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class ModelInfo { id, created_at, display_name, type }

id: String

Unique model identifier.

created_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: String

A human-readable name for the model.

type: :model

Object type.

For Models, this is always `"model"`.
