# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CdrUsageReportFetchSyncParams"]


class CdrUsageReportFetchSyncParams(TypedDict, total=False):
    aggregation_type: Required[Literal["NO_AGGREGATION", "CONNECTION", "TAG", "BILLING_GROUP"]]

    product_breakdown: Required[Literal["NO_BREAKDOWN", "DID_VS_TOLL_FREE", "COUNTRY", "DID_VS_TOLL_FREE_PER_COUNTRY"]]

    connections: Iterable[float]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
