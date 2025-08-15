# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sim_card_order import SimCardOrder

__all__ = ["SimCardOrderCreateResponse"]


class SimCardOrderCreateResponse(BaseModel):
    data: Optional[SimCardOrder] = None
