# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .number_reservation import NumberReservation

__all__ = ["NumberReservationRetrieveResponse"]


class NumberReservationRetrieveResponse(BaseModel):
    data: Optional[NumberReservation] = None
