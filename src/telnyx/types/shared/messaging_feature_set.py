# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MessagingFeatureSet"]


class MessagingFeatureSet(BaseModel):
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features
    can vary depending on the characteristics the phone number, as well as its current
    product configuration.
    """

    domestic_two_way: bool
    """Send messages to and receive messages from numbers in the same country."""

    international_inbound: bool
    """Receive messages from numbers in other countries."""

    international_outbound: bool
    """Send messages to numbers in other countries."""
