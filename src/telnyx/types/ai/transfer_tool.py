# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .inference_embedding_transfer_tool_params import InferenceEmbeddingTransferToolParams

__all__ = ["TransferTool"]


class TransferTool(BaseModel):
    transfer: InferenceEmbeddingTransferToolParams

    type: Literal["transfer"]
