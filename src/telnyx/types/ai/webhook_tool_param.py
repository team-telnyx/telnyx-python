# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .inference_embedding_webhook_tool_params_param import InferenceEmbeddingWebhookToolParamsParam

__all__ = ["WebhookToolParam"]


class WebhookToolParam(TypedDict, total=False):
    type: Required[Literal["webhook"]]

    webhook: Required[InferenceEmbeddingWebhookToolParamsParam]
