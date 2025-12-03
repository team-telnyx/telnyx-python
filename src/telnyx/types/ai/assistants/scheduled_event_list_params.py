# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledEventListParams", "Page"]


class ScheduledEventListParams(TypedDict, total=False):
    conversation_channel: ConversationChannelType

    from_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    to_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class Page(TypedDict, total=False):
    number: int

    size: int
