# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.simple_sim_card import SimpleSimCard
from .wireless_error_c5290d5308 import WirelessErrorC5290d5308

__all__ = ["PurchaseCreateResponse"]


class PurchaseCreateResponse(BaseModel):
    data: Optional[List[SimpleSimCard]] = None
    """Successfully registered SIM cards."""

    errors: Optional[List[WirelessErrorC5290d5308]] = None
