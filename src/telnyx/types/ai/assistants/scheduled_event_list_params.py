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

    from_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    to_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
