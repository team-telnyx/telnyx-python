# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhoneNumberBatchListParams"]


class PhoneNumberBatchListParams(TypedDict, total=False):
    filter_status: Annotated[
        Literal["submitted", "in_review", "verified", "unsuccessful", "suspended", "expired", "permanently_rejected"],
        PropertyInfo(alias="filter[status]"),
    ]
    """Restrict to batches whose aggregate status equals this value."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""
