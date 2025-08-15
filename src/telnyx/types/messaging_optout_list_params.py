# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessagingOptoutListParams", "CreatedAt", "Filter", "Page"]


class MessagingOptoutListParams(TypedDict, total=False):
    created_at: CreatedAt
    """Consolidated created_at parameter (deepObject style).

    Originally: created_at[gte], created_at[lte]
    """

    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[messaging_profile_id], filter[from]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    redaction_enabled: str
    """If receiving address (+E.164 formatted phone number) should be redacted"""


class CreatedAt(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter opt-outs created after this date (ISO-8601 format)"""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter opt-outs created before this date (ISO-8601 format)"""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    messaging_profile_id: str
    """The ID of the messaging profile to retrieve opt-outs for"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
