# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MdrUsageReportCreateParams"]


class MdrUsageReportCreateParams(TypedDict, total=False):
    aggregation_type: Required[Literal["NO_AGGREGATION", "PROFILE", "TAGS"]]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    profiles: str
