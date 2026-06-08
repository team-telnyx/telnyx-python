# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Filter results by filter name."""

    filter_type: Annotated[str, PropertyInfo(alias="filter[type]")]
    """Filter results by filter type."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to retrieve (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of items to return per page."""
