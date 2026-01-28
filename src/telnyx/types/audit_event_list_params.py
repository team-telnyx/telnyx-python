# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuditEventListParams", "Filter"]


class AuditEventListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[created_before], filter[created_after]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["asc", "desc"]
    """Set the order of the results by the creation date."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[created_before], filter[created_after]
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for audit events created after a specific date."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for audit events created before a specific date."""
