# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["ReportListWdrsParams", "Page"]


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

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    phone_number: str
    """Phone number"""

    sim_card_id: str
    """Sim card unique identifier"""

    sim_group_id: str
    """Sim group unique identifier"""

    sim_group_name: str
    """Sim group name"""

    sort: List[str]
    """Field used to order the data.

    If no field is specified, default value is 'created_at'
    """

    start_date: str
    """Start date"""


class Page(TypedDict, total=False):
    number: int
    """Page number"""

    size: int
    """Size of the page"""
