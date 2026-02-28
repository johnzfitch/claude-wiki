---
category: "20-Models"
fetched_at: "2026-02-22T13:46:40Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/models"
title: "Models - Claude API Reference"
---
# Models

##### [List Models](/docs/en/api/beta/models/list)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

[BetaModelInfo](/docs/en/api/beta#beta_model_info) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaModelInfo:

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
