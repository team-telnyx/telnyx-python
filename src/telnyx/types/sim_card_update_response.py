# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .sim_card import SimCard

__all__ = ["SimCardUpdateResponse"]


class SimCardUpdateResponse(BaseModel):
    data: Optional[SimCard] = None
