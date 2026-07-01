# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .sub_number_order import SubNumberOrder

__all__ = ["SubNumberOrderCancelResponse"]


class SubNumberOrderCancelResponse(BaseModel):
    data: Optional[SubNumberOrder] = None
