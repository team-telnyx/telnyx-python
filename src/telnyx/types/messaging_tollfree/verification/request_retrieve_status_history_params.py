# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RequestRetrieveStatusHistoryParams"]


class RequestRetrieveStatusHistoryParams(TypedDict, total=False):
    page_number: Required[Annotated[int, PropertyInfo(alias="page[number]")]]
    """Page number to retrieve (1-based)."""

    page_size: Required[Annotated[int, PropertyInfo(alias="page[size]")]]
    """Number of items to return per page."""
