# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PortingListUkCarriersResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the UK carrier."""

    alternative_cupids: Optional[List[str]] = None
    """Alternative CUPIDs of the carrier."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    cupid: Optional[str] = None
    """The CUPID of the carrier.

    This is a 3 digit number code that identifies the carrier in the UK.
    """

    name: Optional[str] = None
    """The name of the carrier."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class PortingListUkCarriersResponse(BaseModel):
    data: Optional[List[Data]] = None
