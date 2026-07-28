# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailBlockListParams"]


class EmailBlockListParams(TypedDict, total=False):
    filter_created_after: Annotated[Union[str, datetime], PropertyInfo(alias="filter[created_after]", format="iso8601")]
    """`created_at > value` (ISO 8601)."""

    filter_created_before: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[created_before]", format="iso8601")
    ]
    """`created_at < value` (ISO 8601)."""

    filter_domain_id: Annotated[str, PropertyInfo(alias="filter[domain_id]")]
    """Exact-match filter on domain_id (UUID)."""

    filter_reason: Annotated[
        Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"],
        PropertyInfo(alias="filter[reason]"),
    ]
    """Exact-match filter on reason."""

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor (`Base.url_encode64` of `{"created_at","id"}`).

    Cursor mode; mutually exclusive with `page[number]` and `page[before]`.
    """

    page_before: Annotated[str, PropertyInfo(alias="page[before]")]
    """Opaque cursor (see `page[after]`).

    Mutually exclusive with `page[after]` and `page[number]`.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Offset page number (≥1, default 1)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Page size (1–100, default 25)."""

    sort: Literal["created_at", "-created_at"]
    """Sort field.

    Leading `-` = desc; only `created_at` is sortable. Default `-created_at`. `--`
    is an error.
    """
