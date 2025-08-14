# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendGroupMmsParams"]


class MessageSendGroupMmsParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Phone number, in +E.164 format, used to send the message."""

    to: Required[List[str]]
    """A list of destinations. No more than 8 destinations are allowed."""

    media_urls: List[str]
    """A list of media URLs. The total media size must be less than 1 MB."""

    subject: str
    """Subject of multimedia message"""

    text: str
    """Message body (i.e., content) as a non-empty string."""

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
