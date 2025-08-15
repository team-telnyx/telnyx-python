# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = [
    "WebhookDeliveryListParams",
    "Filter",
    "FilterAttempts",
    "FilterFinishedAt",
    "FilterStartedAt",
    "FilterStatus",
    "FilterWebhook",
    "Page",
]


class WebhookDeliveryListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status][eq], filter[event_type], filter[webhook][contains],
    filter[attempts][contains], filter[started_at][gte], filter[started_at][lte],
    filter[finished_at][gte], filter[finished_at][lte]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterAttempts(TypedDict, total=False):
    contains: str
    """
    Return only webhook_deliveries whose `attempts` component contains the given
    text
    """


class FilterFinishedAt(TypedDict, total=False):
    gte: str
    """
    Return only webhook_deliveries whose delivery finished later than or at given
    ISO 8601 datetime
    """

    lte: str
    """
    Return only webhook_deliveries whose delivery finished earlier than or at given
    ISO 8601 datetime
    """


class FilterStartedAt(TypedDict, total=False):
    gte: str
    """
    Return only webhook_deliveries whose delivery started later than or at given ISO
    8601 datetime
    """

    lte: str
    """
    Return only webhook_deliveries whose delivery started earlier than or at given
    ISO 8601 datetime
    """


class FilterStatus(TypedDict, total=False):
    eq: Literal["delivered", "failed"]
    """Return only webhook_deliveries matching the given `status`"""


class FilterWebhook(TypedDict, total=False):
    contains: str
    """
    Return only webhook deliveries whose `webhook` component contains the given text
    """


class Filter(TypedDict, total=False):
    attempts: FilterAttempts

    event_type: str
    """Return only webhook_deliveries matching the given value of `event_type`.

    Accepts multiple values separated by a `,`.
    """

    finished_at: FilterFinishedAt

    started_at: FilterStartedAt

    status: FilterStatus

    webhook: FilterWebhook


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
