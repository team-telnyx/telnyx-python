# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["NumberListParams"]


class NumberListParams(TypedDict, total=False):
    filter_ownership_status: Annotated["ReputationOwnershipStatus", PropertyInfo(alias="filter[ownership_status]")]
    """Only numbers with this ownership status.

    `removed` lists the numbers that were removed, each with its `removal_reason`
    and `removed_at`; removed numbers are not returned otherwise.
    """

    filter_phone_number_contains: Annotated[str, PropertyInfo(alias="filter[phone_number][contains]")]
    """Partial match on phone number. Must contain at least 5 digits."""

    filter_phone_number_eq: Annotated[str, PropertyInfo(alias="filter[phone_number][eq]")]
    """Exact phone-number match (E.164)."""

    filter_source: Annotated["ReputationNumberSource", PropertyInfo(alias="filter[source]")]
    """Only numbers with this source."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Default 10. Maximum 250; values above are clamped to 250."""


from .reputation_number_source import ReputationNumberSource
from .reputation_ownership_status import ReputationOwnershipStatus
