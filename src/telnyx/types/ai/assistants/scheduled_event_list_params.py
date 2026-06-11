# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledEventListParams"]


class ScheduledEventListParams(TypedDict, total=False):
    conversation_channel: ConversationChannelType
    """Filter results by conversation channel."""

    from_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the date range filter (inclusive, ISO 8601)."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    to_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the date range filter (inclusive, ISO 8601)."""
