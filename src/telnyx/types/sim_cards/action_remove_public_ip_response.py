# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .sim_card_action import SimCardAction

__all__ = ["ActionRemovePublicIPResponse"]


class ActionRemovePublicIPResponse(BaseModel):
    data: Optional[SimCardAction] = None
    """This object represents a SIM card action.

    It allows tracking the current status of an operation that impacts the SIM card.
    """
