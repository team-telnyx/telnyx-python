# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SqldbListParams"]


class SqldbListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Filter by exact name match."""

    filter_status: Annotated[
        Literal["pending", "provision_ok", "provision_failed", "deleting", "delete_failed"],
        PropertyInfo(alias="filter[status]"),
    ]
    """Filter by provisioning status."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page. Values above 250 are treated as 250."""

    sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at"]
    """Sort field; prefix with `-` for descending order."""
