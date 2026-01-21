# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .bucket_ids import BucketIDs

__all__ = ["RetrievalTool"]


class RetrievalTool(BaseModel):
    retrieval: BucketIDs

    type: Literal["retrieval"]
