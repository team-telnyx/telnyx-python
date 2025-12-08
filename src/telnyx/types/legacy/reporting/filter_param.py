# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FilterParam"]


class FilterParam(TypedDict, total=False):
    """Query filter criteria.

    Note: The first filter object must specify filter_type as 'and'. You cannot follow an 'or' with another 'and'.
    """

    billing_group: str
    """Billing group UUID to filter by"""

    cld: str
    """Called line identification (destination number)"""

    cld_filter: Literal["contains", "starts_with", "ends_with"]
    """Filter type for CLD matching"""

    cli: str
    """Calling line identification (caller ID)"""

    cli_filter: Literal["contains", "starts_with", "ends_with"]
    """Filter type for CLI matching"""

    filter_type: Literal["and", "or"]
    """Logical operator for combining filters"""

    tags_list: str
    """Tag name to filter by"""
