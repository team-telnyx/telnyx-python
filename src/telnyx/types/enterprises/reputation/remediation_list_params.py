# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .remediation_status import RemediationStatus

__all__ = ["RemediationListParams"]


class RemediationListParams(TypedDict, total=False):
    filter_created_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[created_at][gte]", format="iso8601")
    ]
    """Only requests created on or after this timestamp (ISO 8601)."""

    filter_created_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[created_at][lte]", format="iso8601")
    ]
    """Only requests created on or before this timestamp (ISO 8601)."""

    filter_status: Annotated[RemediationStatus, PropertyInfo(alias="filter[status]")]
    """Filter by customer-facing status."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""
