# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ReportListWdrsParams"]


class ReportListWdrsParams(TypedDict, total=False):
    id: str
    """Filter results by identifier."""

    end_date: str
    """End date"""

    imsi: str
    """Filter results by imsi."""

    mcc: str
    """Filter results by mcc."""

    mnc: str
    """Filter results by mnc."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    phone_number: str
    """Filter results by phone number."""

    sim_card_id: str
    """Filter results by sim card id."""

    sim_group_id: str
    """Filter results by sim group id."""

    sim_group_name: str
    """Filter results by sim group name."""

    sort: SequenceNotStr[str]
    """Field and direction to sort the results by."""

    start_date: str
    """Start date"""
