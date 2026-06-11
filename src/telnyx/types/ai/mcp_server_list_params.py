# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["McpServerListParams"]


class McpServerListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to retrieve (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of items to return per page."""

    type: str
    """Filter results by type."""

    url: str
    """Filter results by url."""
