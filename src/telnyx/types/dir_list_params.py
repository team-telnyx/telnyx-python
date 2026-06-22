# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .dir_status import DirStatus

__all__ = ["DirListParams"]


class DirListParams(TypedDict, total=False):
    filter_call_reason_contains: Annotated[str, PropertyInfo(alias="filter[call_reason][contains]")]
    """Case-insensitive partial match on call reason."""

    filter_display_name_contains: Annotated[str, PropertyInfo(alias="filter[display_name][contains]")]
    """Case-insensitive partial match on display name."""

    filter_enterprise_id: Annotated[str, PropertyInfo(alias="filter[enterprise_id]")]
    """Filter by enterprise ID."""

    filter_expiring_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[expiring_at][gte]", format="iso8601")
    ]
    """Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp.

    Pairs with the `[lte]` variant to build renewal-window dashboards.
    """

    filter_expiring_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[expiring_at][lte]", format="iso8601")
    ]
    """Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp."""

    filter_status: Annotated[DirStatus, PropertyInfo(alias="filter[status]")]
    """Filter by DIR status."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""

    sort: Literal[
        "created_at", "-created_at", "updated_at", "-updated_at", "display_name", "-display_name", "status", "-status"
    ]
    """Sort field.

    Allowed values: `created_at`, `updated_at`, `display_name`, `status`. Prefix
    with `-` for descending. Default `-created_at`.
    """
