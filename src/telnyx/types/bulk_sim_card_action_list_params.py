# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BulkSimCardActionListParams"]


class BulkSimCardActionListParams(TypedDict, total=False):
    filter_action_type: Annotated[Literal["bulk_set_public_ips"], PropertyInfo(alias="filter[action_type]")]
    """Filter by action type."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""
