# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["SessionAnalysisRetrieveResponse", "Cost", "Meta"]


class Cost(BaseModel):
    currency: str
    """ISO 4217 currency code."""

    total: str
    """Total session cost as a decimal string."""


class Meta(BaseModel):
    event_count: int
    """Total number of events in the session tree."""

    products: List[str]
    """List of distinct products involved in the session."""


class SessionAnalysisRetrieveResponse(BaseModel):
    cost: Cost

    meta: Meta

    root: "EventNode"

    session_id: str
    """Identifier for the analyzed session."""


from .event_node import EventNode
