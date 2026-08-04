# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .wireless_sim_card_action import WirelessSimCardAction

__all__ = ["ActionDisableResponse"]


class ActionDisableResponse(BaseModel):
    data: Optional[WirelessSimCardAction] = None
    """This object represents a SIM card action.

    It allows tracking the current status of an operation that impacts the SIM card.
    """
