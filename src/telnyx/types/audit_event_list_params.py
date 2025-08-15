# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuditEventListParams", "Filter", "Page"]


class AuditEventListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[created_before], filter[created_after]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: Literal["asc", "desc"]
    """Set the order of the results by the creation date."""


class Filter(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for audit events created after a specific date."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for audit events created before a specific date."""


class Page(TypedDict, total=False):
    number: int
    """Page number to load."""

    size: int
    """Number of items per page."""
