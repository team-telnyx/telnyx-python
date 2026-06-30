# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..number_reservation import NumberReservation

__all__ = ["ActionExtendResponse"]


class ActionExtendResponse(BaseModel):
    data: Optional[NumberReservation] = None
