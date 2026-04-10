# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .call_control_bucket_ids import CallControlBucketIDs

__all__ = ["CallControlRetrievalTool"]


class CallControlRetrievalTool(BaseModel):
    retrieval: CallControlBucketIDs

    type: Literal["retrieval"]
