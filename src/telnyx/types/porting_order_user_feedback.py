# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PortingOrderUserFeedback"]


class PortingOrderUserFeedback(BaseModel):
    user_comment: Optional[str] = None
    """A comment related to the customer rating."""

    user_rating: Optional[int] = None
    """
    Once an order is ported, cancellation is requested or the request is cancelled,
    the user may rate their experience
    """
