# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnterpriseListParams"]


class EnterpriseListParams(TypedDict, total=False):
    legal_name: str
    """Filter by legal name (partial match)"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number (1-indexed)"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of items per page"""
