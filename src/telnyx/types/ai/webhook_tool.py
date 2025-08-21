# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .inference_embedding_webhook_tool_params import InferenceEmbeddingWebhookToolParams

__all__ = ["WebhookTool"]


class WebhookTool(BaseModel):
    type: Literal["webhook"]

    webhook: InferenceEmbeddingWebhookToolParams
