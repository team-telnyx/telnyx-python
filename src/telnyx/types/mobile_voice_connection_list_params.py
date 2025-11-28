# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MobileVoiceConnectionListParams"]


class MobileVoiceConnectionListParams(TypedDict, total=False):
    filter_connection_name_contains: Annotated[str, PropertyInfo(alias="filter[connection_name][contains]")]
    """Filter by connection name containing the given string"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page"""

    sort: str
    """Sort by field (e.g., created_at, connection_name, active).

    Prefix with - for descending order.
    """
