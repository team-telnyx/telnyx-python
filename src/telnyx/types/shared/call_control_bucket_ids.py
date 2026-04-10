# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CallControlBucketIDs"]


class CallControlBucketIDs(BaseModel):
    bucket_ids: List[str]

    max_num_results: Optional[int] = None
    """The maximum number of results to retrieve as context for the language model."""
