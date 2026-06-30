# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .number_block_order import NumberBlockOrder

__all__ = ["NumberBlockOrderCreateResponse"]


class NumberBlockOrderCreateResponse(BaseModel):
    data: Optional[NumberBlockOrder] = None
