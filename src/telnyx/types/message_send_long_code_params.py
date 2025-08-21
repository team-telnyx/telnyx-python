# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendLongCodeParams"]


class MessageSendLongCodeParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Phone number, in +E.164 format, used to send the message."""

    to: Required[str]
    """Receiving address (+E.164 formatted phone number or short code)."""

    auto_detect: bool
    """
    Automatically detect if an SMS message is unusually long and exceeds a
    recommended limit of message parts.
    """

    media_urls: List[str]
    """A list of media URLs. The total media size must be less than 1 MB.

    **Required for MMS**
    """

    subject: str
    """Subject of multimedia message"""

    text: str
    """Message body (i.e., content) as a non-empty string.

    **Required for SMS**
    """

    type: Literal["SMS", "MMS"]
    """The protocol for sending the message, either SMS or MMS."""

    use_profile_webhooks: bool
    """
    If the profile this number is associated with has webhooks, use them for
    delivery notifications. If webhooks are also specified on the message itself,
    they will be attempted first, then those on the profile.
    """

    webhook_failover_url: str
    """
    The failover URL where webhooks related to this message will be sent if sending
    to the primary URL fails.
    """

    webhook_url: str
    """The URL where webhooks related to this message will be sent."""
