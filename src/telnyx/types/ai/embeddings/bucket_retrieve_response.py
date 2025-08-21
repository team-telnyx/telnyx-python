# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BucketRetrieveResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    filename: str

    status: str

    error_reason: Optional[str] = None

    last_embedded_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class BucketRetrieveResponse(BaseModel):
    data: List[Data]
