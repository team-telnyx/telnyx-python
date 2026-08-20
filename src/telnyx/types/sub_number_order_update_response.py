# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .numbers_sub_number_order import NumbersSubNumberOrder

__all__ = ["SubNumberOrderUpdateResponse"]


class SubNumberOrderUpdateResponse(BaseModel):
    data: Optional[NumbersSubNumberOrder] = None
