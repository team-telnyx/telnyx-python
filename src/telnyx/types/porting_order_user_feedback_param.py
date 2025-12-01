# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PortingOrderUserFeedbackParam"]


class PortingOrderUserFeedbackParam(TypedDict, total=False):
    user_comment: Optional[str]
    """A comment related to the customer rating."""

    user_rating: Optional[int]
    """
    Once an order is ported, cancellation is requested or the request is cancelled,
    the user may rate their experience
    """
