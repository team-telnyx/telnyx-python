# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sim_card import SimCard

__all__ = ["SimCardRetrieveResponse"]


class SimCardRetrieveResponse(BaseModel):
    data: Optional[SimCard] = None
