# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

if TYPE_CHECKING:
    from ..dir_status import DirStatus

__all__ = ["DirListParams"]


class DirListParams(TypedDict, total=False):
    filter_call_reason_contains: Annotated[str, PropertyInfo(alias="filter[call_reason][contains]")]
    """Case-insensitive partial match on call reason."""

    filter_display_name_contains: Annotated[str, PropertyInfo(alias="filter[display_name][contains]")]
    """Case-insensitive partial match on display name."""

    filter_expiring_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[expiring_at][gte]", format="iso8601")
    ]
    """Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp."""

    filter_expiring_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[expiring_at][lte]", format="iso8601")
    ]
    """Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp."""

    filter_expiring_within_days: Annotated[int, PropertyInfo(alias="filter[expiring_within_days]")]
    """
    Convenience: returns DIRs whose `expiring_at` falls within the next N days
    (1–365). Equivalent to setting `filter[expiring_at][gte]=<now>` +
    `filter[expiring_at][lte]=<now+N>`. Mutually exclusive with the explicit
    `[gte]`/`[lte]` filters - combining returns 400.
    """

    filter_status: Annotated[DirStatus, PropertyInfo(alias="filter[status]")]
    """Filter by DIR status."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""

    sort: Literal[
        "created_at",
        "-created_at",
        "updated_at",
        "-updated_at",
        "display_name",
        "-display_name",
        "status",
        "-status",
        "submitted_at",
        "-submitted_at",
        "verified_at",
        "-verified_at",
        "expiring_at",
        "-expiring_at",
    ]
    """Sort field.

    Allowed: `created_at`, `updated_at`, `display_name`, `status`, `submitted_at`,
    `verified_at`, `expiring_at`. Prefix with `-` for descending. Default
    `-created_at`.
    """
