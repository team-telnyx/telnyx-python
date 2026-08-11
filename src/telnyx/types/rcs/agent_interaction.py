# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentInteraction"]


class AgentInteraction(BaseModel):
    interaction_type: Literal[
        "TRANSACTIONAL_UPDATES",
        "CUSTOMER_SUPPORT",
        "LOYALTY_OR_REWARD",
        "MARKETING_OR_PROMOTIONAL",
        "ACCOUNT_ALERTS",
        "TWO_WAY_CONVERSATION",
        "OTHER",
    ]

    description: Optional[str] = None
    """Required when interaction_type is `OTHER`."""
