# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = [
    "NotificationChannelListParams",
    "Filter",
    "FilterAssociatedRecordType",
    "FilterChannelTypeID",
    "FilterNotificationChannel",
    "FilterNotificationEventConditionID",
    "FilterNotificationProfileID",
    "FilterStatus",
    "Page",
]


class NotificationChannelListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[associated_record_type][eq], filter[channel_type_id][eq],
    filter[notification_profile_id][eq], filter[notification_channel][eq],
    filter[notification_event_condition_id][eq], filter[status][eq]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterAssociatedRecordType(TypedDict, total=False):
    eq: Literal["account", "phone_number"]
    """Filter by the associated record type"""


class FilterChannelTypeID(TypedDict, total=False):
    eq: Literal["webhook", "sms", "email", "voice"]
    """Filter by the id of a channel type"""


class FilterNotificationChannel(TypedDict, total=False):
    eq: str
    """Filter by the id of a notification channel"""


class FilterNotificationEventConditionID(TypedDict, total=False):
    eq: str
    """Filter by the id of a notification channel"""


class FilterNotificationProfileID(TypedDict, total=False):
    eq: str
    """Filter by the id of a notification profile"""


class FilterStatus(TypedDict, total=False):
    eq: Literal[
        "enabled",
        "enable-received",
        "enable-pending",
        "enable-submtited",
        "delete-received",
        "delete-pending",
        "delete-submitted",
        "deleted",
    ]
    """The status of a notification setting"""


class Filter(TypedDict, total=False):
    associated_record_type: FilterAssociatedRecordType

    channel_type_id: FilterChannelTypeID

    notification_channel: FilterNotificationChannel

    notification_event_condition_id: FilterNotificationEventConditionID

    notification_profile_id: FilterNotificationProfileID

    status: FilterStatus


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
