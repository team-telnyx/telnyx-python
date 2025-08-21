# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberCampaignListParams", "Filter"]


class PhoneNumberCampaignListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[telnyx_campaign_id], filter[telnyx_brand_id],
    filter[tcr_campaign_id], filter[tcr_brand_id]
    """

    page: int

    records_per_page: Annotated[int, PropertyInfo(alias="recordsPerPage")]

    sort: Literal["assignmentStatus", "-assignmentStatus", "createdAt", "-createdAt", "phoneNumber", "-phoneNumber"]
    """Specifies the sort order for results.

    If not given, results are sorted by createdAt in descending order.
    """


class Filter(TypedDict, total=False):
    tcr_brand_id: str
    """Filter results by the TCR Brand id"""

    tcr_campaign_id: str
    """Filter results by the TCR Campaign id"""

    telnyx_brand_id: str
    """Filter results by the Telnyx Brand id"""

    telnyx_campaign_id: str
    """Filter results by the Telnyx Campaign id"""
