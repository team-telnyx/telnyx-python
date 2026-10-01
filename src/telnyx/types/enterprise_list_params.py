# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnterpriseListParams"]


class EnterpriseListParams(TypedDict, total=False):
    filter_legal_name_contains: Annotated[str, PropertyInfo(alias="filter[legal_name][contains]")]
    """Case-insensitive partial match on legal name."""

    filter_role_type: Annotated[Literal["enterprise", "bpo"], PropertyInfo(alias="filter[role_type]")]
    """
    Only return enterprises of this type: `bpo` for call-center (BPO) enterprises,
    `enterprise` for normal enterprises. Omit to return both.
    """

    legal_name: str
    """Filter by legal name (partial match)."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Default 10. Maximum 250; values above are clamped to 250."""
