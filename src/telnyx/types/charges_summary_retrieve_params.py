# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChargesSummaryRetrieveParams"]


class ChargesSummaryRetrieveParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End date for the charges summary in ISO date format (YYYY-MM-DD).

    The date is exclusive, data for the end_date itself is not included in the
    report. The interval between start_date and end_date cannot exceed 31 days.
    """

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date for the charges summary in ISO date format (YYYY-MM-DD)"""
