# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeetingListParams"]


class MeetingListParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Window start; defaults to now."""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Window end; defaults to seven days from now."""
