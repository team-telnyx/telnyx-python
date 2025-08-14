# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PartnerCampaignListSharedByMeParams"]


class PartnerCampaignListSharedByMeParams(TypedDict, total=False):
    page: int
    """The 1-indexed page number to get. The default value is `1`."""

    records_per_page: Annotated[int, PropertyInfo(alias="recordsPerPage")]
    """The amount of records per page, limited to between 1 and 500 inclusive.

    The default value is `10`.
    """
