# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["NumberHealthMetrics"]


class NumberHealthMetrics(BaseModel):
    inbound_outbound_ratio: float
    """The ratio of messages received to the number of messages sent."""

    message_count: int
    """The number of messages analyzed for the health metrics."""

    spam_ratio: float
    """The ratio of messages blocked for spam to the number of messages attempted."""

    success_ratio: float
    """
    The ratio of messages sucessfully delivered to the number of messages attempted.
    """
