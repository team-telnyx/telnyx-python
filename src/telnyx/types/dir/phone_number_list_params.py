# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhoneNumberListParams"]


class PhoneNumberListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""

    status: Literal[
        "submitted", "in_review", "verified", "unsuccessful", "suspended", "expired", "permanently_rejected"
    ]
    """Filter by phone-number status."""
