# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["BucketListResponse", "Data"]


class Data(BaseModel):
    buckets: List[str]


class BucketListResponse(BaseModel):
    data: Data
