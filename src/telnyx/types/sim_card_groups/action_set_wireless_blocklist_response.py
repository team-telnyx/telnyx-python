# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .sim_card_group_action import SimCardGroupAction

__all__ = ["ActionSetWirelessBlocklistResponse"]


class ActionSetWirelessBlocklistResponse(BaseModel):
    data: Optional[SimCardGroupAction] = None
    """This object represents a SIM card group action request.

    It allows tracking the current status of an operation that impacts the SIM card
    group and SIM card in it.
    """
