# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .number_reservation import NumberReservation

__all__ = ["NumberReservationListResponse"]


class NumberReservationListResponse(BaseModel):
    data: Optional[List[NumberReservation]] = None

    meta: Optional[PaginationMeta] = None
