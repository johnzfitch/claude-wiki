---
category: "20-Models"
fetched_at: "2026-03-03T15:00:59Z"
source_url: "https://platform.claude.com/docs/en/api/java/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

[ModelInfo](/docs/en/api/models#model_info) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class ModelInfo:

String id

Unique model identifier.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

JsonValue; type "model"constant

"model"constant

Object type.

For Models, this is always `"model"`.
