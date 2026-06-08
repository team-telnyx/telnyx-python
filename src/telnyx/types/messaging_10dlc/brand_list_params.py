# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandListParams"]


class BrandListParams(TypedDict, total=False):
    brand_id: Annotated[str, PropertyInfo(alias="brandId")]
    """Filter results by the Telnyx Brand id"""

    country: str
    """Filter results by country."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Filter results by display name."""

    entity_type: Annotated[str, PropertyInfo(alias="entityType")]
    """Filter results by entity type."""

    page: int
    """Page number to retrieve (1-based)."""

    records_per_page: Annotated[int, PropertyInfo(alias="recordsPerPage")]
    """number of records per page. maximum of 500"""

    sort: Literal[
        "assignedCampaignsCount",
        "-assignedCampaignsCount",
        "brandId",
        "-brandId",
        "createdAt",
        "-createdAt",
        "displayName",
        "-displayName",
        "identityStatus",
        "-identityStatus",
        "status",
        "-status",
        "tcrBrandId",
        "-tcrBrandId",
    ]
    """Specifies the sort order for results.

    If not given, results are sorted by createdAt in descending order.
    """

    state: str
    """Filter results by state."""

    tcr_brand_id: Annotated[str, PropertyInfo(alias="tcrBrandId")]
    """Filter results by the TCR Brand id"""
