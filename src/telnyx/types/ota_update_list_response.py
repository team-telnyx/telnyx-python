# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["OtaUpdateListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    sim_card_id: Optional[str] = None
    """The identification UUID of the related SIM card resource."""

    status: Optional[Literal["in-progress", "completed", "failed"]] = None

    type: Optional[Literal["sim_card_network_preferences"]] = None
    """Represents the type of the operation requested.

    This will relate directly to the source of the request.
    """

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class OtaUpdateListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
