# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MdrUsageReportFetchSyncParams"]


class MdrUsageReportFetchSyncParams(TypedDict, total=False):
    aggregation_type: Required[Literal["NO_AGGREGATION", "PROFILE", "TAGS"]]
    """Type of aggregation to apply to the results."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the date range filter (inclusive, ISO 8601)."""

    profiles: SequenceNotStr[str]
    """Filter results by profile."""

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the date range filter (inclusive, ISO 8601)."""
