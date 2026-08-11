# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentInteractionParam"]


class AgentInteractionParam(TypedDict, total=False):
    interaction_type: Required[
        Literal[
            "TRANSACTIONAL_UPDATES",
            "CUSTOMER_SUPPORT",
            "LOYALTY_OR_REWARD",
            "MARKETING_OR_PROMOTIONAL",
            "ACCOUNT_ALERTS",
            "TWO_WAY_CONVERSATION",
            "OTHER",
        ]
    ]

    description: Optional[str]
    """Required when interaction_type is `OTHER`."""
