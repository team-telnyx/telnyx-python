# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayConnectorListParams"]


class PayConnectorListParams(TypedDict, total=False):
    filter_created_at_eq: Annotated[str, PropertyInfo(alias="filter[created_at][eq]")]
    """Equal to this created_at timestamp."""

    filter_created_at_gt: Annotated[str, PropertyInfo(alias="filter[created_at][gt]")]
    """After this created_at timestamp."""

    filter_created_at_gte: Annotated[str, PropertyInfo(alias="filter[created_at][gte]")]
    """At or after this created_at timestamp."""

    filter_created_at_lt: Annotated[str, PropertyInfo(alias="filter[created_at][lt]")]
    """Before this created_at timestamp."""

    filter_created_at_lte: Annotated[str, PropertyInfo(alias="filter[created_at][lte]")]
    """At or before this created_at timestamp."""

    filter_mode: Annotated[str, PropertyInfo(alias="filter[mode]")]
    """Exact match on mode."""

    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Exact match on name."""

    filter_type: Annotated[str, PropertyInfo(alias="filter[type]")]
    """Exact match on type."""

    filter_updated_at_eq: Annotated[str, PropertyInfo(alias="filter[updated_at][eq]")]
    """Equal to this updated_at timestamp."""

    filter_updated_at_gt: Annotated[str, PropertyInfo(alias="filter[updated_at][gt]")]
    """After this updated_at timestamp."""

    filter_updated_at_gte: Annotated[str, PropertyInfo(alias="filter[updated_at][gte]")]
    """At or after this updated_at timestamp."""

    filter_updated_at_lt: Annotated[str, PropertyInfo(alias="filter[updated_at][lt]")]
    """Before this updated_at timestamp."""

    filter_updated_at_lte: Annotated[str, PropertyInfo(alias="filter[updated_at][lte]")]
    """At or before this updated_at timestamp."""

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor from meta.end_cursor."""

    page_before: Annotated[str, PropertyInfo(alias="page[before]")]
    """Opaque cursor from meta.start_cursor."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of records per page."""

    sort: str
    """
    Comma-separated created_at or updated_at fields, optionally prefixed with - for
    descending order.
    """
