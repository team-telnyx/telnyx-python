# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .record import Record
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["NetworkListResponse", "Data"]


class Data(Record):
    name: Optional[str] = None
    """A user specified name for the network."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""


class NetworkListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
