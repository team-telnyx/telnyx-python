# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..wireless_error import WirelessError
from ..shared.simple_sim_card import SimpleSimCard

__all__ = ["PurchaseCreateResponse"]


class PurchaseCreateResponse(BaseModel):
    data: Optional[List[SimpleSimCard]] = None
    """Successfully registered SIM cards."""

    errors: Optional[List[WirelessError]] = None
