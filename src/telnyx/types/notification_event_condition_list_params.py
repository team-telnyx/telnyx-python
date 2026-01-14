# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "NotificationEventConditionListParams",
    "Filter",
    "FilterAssociatedRecordType",
    "FilterChannelTypeID",
    "FilterNotificationChannel",
    "FilterNotificationEventConditionID",
    "FilterNotificationProfileID",
    "FilterStatus",
]


class NotificationEventConditionListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[associated_record_type][eq], filter[channel_type_id][eq],
    filter[notification_profile_id][eq], filter[notification_channel][eq],
    filter[notification_event_condition_id][eq], filter[status][eq]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


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
    """Consolidated filter parameter (deepObject style).

    Originally: filter[associated_record_type][eq], filter[channel_type_id][eq], filter[notification_profile_id][eq], filter[notification_channel][eq], filter[notification_event_condition_id][eq], filter[status][eq]
    """

    associated_record_type: FilterAssociatedRecordType

    channel_type_id: FilterChannelTypeID

    notification_channel: FilterNotificationChannel

    notification_event_condition_id: FilterNotificationEventConditionID

    notification_profile_id: FilterNotificationProfileID

    status: FilterStatus
