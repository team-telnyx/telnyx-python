# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailEventRetrieveStatsParams"]


class EmailEventRetrieveStatsParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted."""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Inclusive ISO 8601 end timestamp.

    When `from` is provided without `to`, defaults to `from + 30 days`.
    """
