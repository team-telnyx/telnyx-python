# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WirelessRetrieveRegionsResponse", "Data"]


class Data(BaseModel):
    code: str
    """The unique code of the region."""

    name: str
    """The name of the region."""

    inserted_at: Optional[datetime] = None
    """Timestamp when the region was inserted."""

    updated_at: Optional[datetime] = None
    """Timestamp when the region was last updated."""


class WirelessRetrieveRegionsResponse(BaseModel):
    data: Optional[List[Data]] = None
