# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MdrUsageReportFetchSyncParams"]


class MdrUsageReportFetchSyncParams(TypedDict, total=False):
    aggregation_type: Required[Literal["NO_AGGREGATION", "PROFILE", "TAGS"]]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    profiles: List[str]

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
