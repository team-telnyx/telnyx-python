# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .inference_embedding_bucket_ids import InferenceEmbeddingBucketIDs

__all__ = ["RetrievalTool"]


class RetrievalTool(BaseModel):
    retrieval: InferenceEmbeddingBucketIDs

    type: Literal["retrieval"]
