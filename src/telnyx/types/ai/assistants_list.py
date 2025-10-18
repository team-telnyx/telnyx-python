# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .inference_embedding import InferenceEmbedding

__all__ = ["AssistantsList"]


class AssistantsList(BaseModel):
    data: List[InferenceEmbedding]
