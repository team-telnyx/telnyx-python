# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SpeechToTextCreateParams"]


class SpeechToTextCreateParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date in ISO format with timezone (date range must be up to one month)"""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date in ISO format with timezone"""
