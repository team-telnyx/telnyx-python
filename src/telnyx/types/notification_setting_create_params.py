# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["NotificationSettingCreateParams", "Parameter"]


class NotificationSettingCreateParams(TypedDict, total=False):
    notification_channel_id: str
    """A UUID reference to the associated Notification Channel."""

    notification_event_condition_id: str
    """A UUID reference to the associated Notification Event Condition."""

    notification_profile_id: str
    """A UUID reference to the associated Notification Profile."""

    parameters: Iterable[Parameter]


class Parameter(TypedDict, total=False):
    name: str

    value: str
