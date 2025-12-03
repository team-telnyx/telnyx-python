# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ReportListWdrsParams"]


class ReportListWdrsParams(TypedDict, total=False):
    id: str
    """WDR uuid"""

    end_date: str
    """End date"""

    imsi: str
    """International mobile subscriber identity"""

    mcc: str
    """Mobile country code"""

    mnc: str
    """Mobile network code"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    phone_number: str
    """Phone number"""

    sim_card_id: str
    """Sim card unique identifier"""

    sim_group_id: str
    """Sim group unique identifier"""

    sim_group_name: str
    """Sim group name"""

    sort: SequenceNotStr[str]
    """Field used to order the data.

    If no field is specified, default value is 'created_at'
    """

    start_date: str
    """Start date"""
