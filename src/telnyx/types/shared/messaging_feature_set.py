# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MessagingFeatureSet"]


class MessagingFeatureSet(BaseModel):
    domestic_two_way: bool
    """Send messages to and receive messages from numbers in the same country."""

    international_inbound: bool
    """Receive messages from numbers in other countries."""

    international_outbound: bool
    """Send messages to numbers in other countries."""
