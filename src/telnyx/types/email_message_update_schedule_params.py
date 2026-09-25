# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailMessageUpdateScheduleParams"]


class EmailMessageUpdateScheduleParams(TypedDict, total=False):
    scheduled_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """New ISO 8601 delivery time. Must be strictly in the future."""
