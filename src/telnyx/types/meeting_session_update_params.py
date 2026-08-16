# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MeetingSessionUpdateParams"]


class MeetingSessionUpdateParams(TypedDict, total=False):
    bot_name: str
    """Updated display name for the bot."""

    join_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO-8601 timestamp for the bot to join. May be updated to reschedule."""
