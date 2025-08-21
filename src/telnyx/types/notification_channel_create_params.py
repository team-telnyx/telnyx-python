# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NotificationChannelCreateParams"]


class NotificationChannelCreateParams(TypedDict, total=False):
    channel_destination: str
    """The destination associated with the channel type."""

    channel_type_id: Literal["sms", "voice", "email", "webhook"]
    """A Channel Type ID"""

    notification_profile_id: str
    """A UUID reference to the associated Notification Profile."""
