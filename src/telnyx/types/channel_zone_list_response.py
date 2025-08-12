# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["ChannelZoneListResponse", "Data"]


class Data(BaseModel):
    id: str

    channels: int

    countries: List[str]
    """
    List of countries (in ISO 3166-2, capitalized) members of the billing channel
    zone
    """

    name: str

    record_type: Literal["channel_zone"]

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the channel zone was created"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the channel zone was updated"""


class ChannelZoneListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
