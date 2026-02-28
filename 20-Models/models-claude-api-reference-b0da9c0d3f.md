---
category: "20-Models"
fetched_at: "2026-02-22T13:40:04Z"
source_url: "https://platform.claude.com/docs/en/api/python/models"
title: "Models - Claude API Reference"
---
# Models

##### [List Models](/docs/en/api/models/list)

models.list(ModelListParams\*\*kwargs) -\> SyncPage\[[ModelInfo](/docs/en/api/models#model_info)\]

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

models.retrieve(strmodel_id, ModelRetrieveParams\*\*kwargs) -\> [ModelInfo](/docs/en/api/models#model_info)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class ModelInfo: …

id: str

Unique model identifier.

created_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: str

A human-readable name for the model.

type: Literal\["model"\]

Object type.

For Models, this is always `"model"`.
