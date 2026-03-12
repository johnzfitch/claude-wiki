---
category: "20-Models"
fetched_at: "2026-03-12T08:16:36Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

client.models.list(ModelListParams { after_id, before_id, limit, betas } params?, RequestOptionsoptions?): Page\<[ModelInfo](/docs/en/api/models#model_info) { id, created_at, display_name, type } \>

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

client.models.retrieve(stringmodelID, ModelRetrieveParams { betas } params?, RequestOptionsoptions?): [ModelInfo](/docs/en/api/models#model_info) { id, created_at, display_name, type }

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

ModelInfo { id, created_at, display_name, type }

id: string

Unique model identifier.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.
