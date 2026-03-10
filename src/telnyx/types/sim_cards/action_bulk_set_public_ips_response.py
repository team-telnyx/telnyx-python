# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .bulk_sim_card_action import BulkSimCardAction

__all__ = ["ActionBulkSetPublicIPsResponse"]


class ActionBulkSetPublicIPsResponse(BaseModel):
    data: Optional[BulkSimCardAction] = None
    """This object represents a bulk SIM card action.

    It groups SIM card actions created through a bulk endpoint under a single
    resource for further lookup.
    """
