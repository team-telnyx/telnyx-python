# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageScheduleParams"]


class MessageScheduleParams(TypedDict, total=False):
    to: Required[str]
    """Receiving address (+E.164 formatted phone number or short code)."""

    auto_detect: bool
    """
    Automatically detect if an SMS message is unusually long and exceeds a
    recommended limit of message parts.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).

    **Required if sending with a phone number, short code, or alphanumeric sender
    ID.**
    """

    media_urls: List[str]
    """A list of media URLs. The total media size must be less than 1 MB.

    **Required for MMS**
    """

    messaging_profile_id: str
    """Unique identifier for a messaging profile.

    **Required if sending via number pool or with an alphanumeric sender ID.**
    """

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    ISO 8601 formatted date indicating when to send the message - accurate up till a
    minute.
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
